#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Code de lecture des données acquises par
# l'instrument Hydrones


# Librairies:
# -----------

def readPositionFromLog(nameLogFile):
    """
    Read Airborne flight log and extract position and attitude.

    Input: name of the Airborne flight log file

    Output: a dictionnary containning
        - 'TimeUS': microseconds since the drone switch on
        - 'AbsoluteDate': datetime object of the absolute date (UTC)
        - 'Alt': the precise altitude (computed using EKF)
        - 'RelAlt': the precise relative altitude (computed using EKF)
        - 'Lat': the precise drone latitude
        - 'Lng': the precise drone lon 
    """
    # Librairies
    import datetime as dt
    import numpy as np
    import pdb

    # Functions
    def logExtractVar(nomFic,variable):
        """
        Ne va lire dans un fichier Log Airborne que les lignes contenant la variable specifique.

        Entree:
            - nomFic : Nom du fichier texte
            - variable : Chaine de caractere que doit contenir la ligne

        Sortie:
            - data : dict contenant les lignes extraites sans Pattern
        """
        for ligne in open(nomFic,'r'):
            if (ligne.startswith('FMT') & (variable in ligne)):
                listLigne = ligne.rstrip().replace(' ','').split(',')[5:]
                nbVal = len(listLigne)
                data=dict.fromkeys(listLigne)
                for k in data.keys():
                    data[k] = np.array([])
            if ligne.startswith(variable):
                ligneSansVariable = ligne.replace(variable+',','')
                listVal = np.float_(ligneSansVariable.rstrip().split(','))
                for i in range(nbVal):
                    data[listLigne[i]] = np.append(data[listLigne[i]], listVal[i])

        return data


    # Read Log Airborne
    pos = logExtractVar(nameLogFile, 'POS')
    gps = logExtractVar(nameLogFile, 'GPS')
    ekf1 = logExtractVar(nameLogFile, 'EKF1')
    baro = logExtractVar(nameLogFile, 'BARO')

    # Datation des position a l'aide de la date GPS
    dateRef = dt.datetime(1980, 1, 6, 0, 0, 0, 0)
    clockPos = pos['TimeUS']
    clockGPS = gps['TimeUS']
    secGPSfromRef = np.array([gps['GMS'][i]/1e3 + gps['GWk'][i]*7*86400.0 for i in range(len(gps['TimeUS']))])
    secPosfromRef = np.interp(clockPos, clockGPS, secGPSfromRef)
    pos['AbsoluteDate'] = np.array([dateRef + dt.timedelta(seconds=s) for s in secPosfromRef])

    # Interpolation des roll/pitch/yaw angle sur la clockPos:
    clockEKF1 = ekf1['TimeUS']
    roll = ekf1['Roll']
    pitch = ekf1['Pitch']
    yaw = ekf1['Yaw']
    clockBaro = baro['TimeUS']
    baro_alt = baro['Alt']
    baro_temp = baro['Temp']
    pos['Roll'] = np.interp(clockPos, clockEKF1, roll)
    pos['Pitch'] = np.interp(clockPos, clockEKF1, pitch)
    pos['Yaw'] = np.interp(clockPos, clockEKF1, yaw)
    pos['Baro_Alt'] = np.interp(clockPos, clockBaro, baro_alt)
    pdb.set_trace()

    return pos
