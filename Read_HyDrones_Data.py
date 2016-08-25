#!/usr/bin/python
# -*- coding: utf-8 -*-


# Code de lecture des données acquises par
# l'instrument Hydrones


# Librairies:
# -----------
import datetime as dt
import struct
import numpy as np
import matplotlib.pyplot as plt
import glob

from mpl_toolkits.basemap import Basemap
from matplotlib import cm, colors



# dictionnaire de recetion des data:
# ---------------------------------
hdMeas = dict()
hdMeas['year'] = np.array([])
hdMeas['month'] = np.array([])
hdMeas['day'] = np.array([])
hdMeas['hour'] = np.array([])
hdMeas['min'] = np.array([])
hdMeas['sec'] = np.array([])
hdMeas['usec'] = np.array([])

hdMeas['gps_lat'] = np.array([])
hdMeas['gps_lon'] = np.array([])
hdMeas['gps_geoidheight'] = np.array([])
hdMeas['gps_nbsat'] = np.array([])
hdMeas['gps_altitude'] = np.array([])

hdMeas['leddar_range'] = np.array([])
hdMeas['leddar_ampl'] = np.array([])

hdMeas['baro_pressure'] = np.array([])
hdMeas['baro_sea_level_pressure'] = np.array([])
hdMeas['baro_altitude'] = np.array([])
hdMeas['baro_temperature'] = np.array([])

hdMeas['imu_pitch_angle'] = np.array([])
hdMeas['imu_roll_angle'] = np.array([])


# Description de la structure binaire du fichier:
# -----------------------------------------------
Structure = "<HBBBBBIfffIffIffffff"
s = struct.Struct(Structure)
sizeMeas = struct.calcsize(Structure)


# On parcourt tous les fichiers:
# ------------------------------
listFile = glob.glob('HD_test_*')
listFile.sort()

for fname in listFile:
    hdFile = open(fname,"rb")

    nbMesures = 0
    try:
        while True:
            measure = hdFile.read(sizeMeas)
            if len(measure) != sizeMeas:
                break

            # Recuperation des donnees
            readMeasure = s.unpack(measure)

            hdMeas['year'] = np.append(hdMeas['year'], readMeasure[0])
            hdMeas['month'] = np.append(hdMeas['month'], readMeasure[1])
            hdMeas['day'] = np.append(hdMeas['day'], readMeasure[2])
            hdMeas['hour'] = np.append(hdMeas['hour'], readMeasure[3])
            hdMeas['min'] = np.append(hdMeas['min'], readMeasure[4])
            hdMeas['sec'] = np.append(hdMeas['sec'], readMeasure[5])
            hdMeas['usec'] = np.append(hdMeas['usec'], readMeasure[6])
            hdMeas['gps_lat'] = np.append(hdMeas['gps_lat'], readMeasure[7])
            hdMeas['gps_lon'] = np.append(hdMeas['gps_lon'], readMeasure[8])
            hdMeas['gps_geoidheight'] = np.append(hdMeas['gps_geoidheight'], readMeasure[9])
            hdMeas['gps_nbsat'] = np.append(hdMeas['gps_nbsat'], readMeasure[10])
            hdMeas['gps_height_above_geoid'] = np.append(hdMeas['gps_lat'], readMeasure[11])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[12])
            hdMeas['leddar_ampl'] = np.append(hdMeas['leddar_ampl'], readMeasure[13])
            hdMeas['baro_pressure'] = np.append(hdMeas['baro_pressure'], readMeasure[14])
            hdMeas['baro_sea_level_pressure'] = np.append(hdMeas['baro_sea_level_pressure'], readMeasure[15])
            hdMeas['baro_altitude'] = np.append(hdMeas['baro_altitude'], readMeasure[16])
            hdMeas['baro_temperature'] = np.append(hdMeas['baro_temperature'], readMeasure[17])
            hdMeas['imu_pitch_angle'] = np.append(hdMeas['imu_pitch_angle'], readMeasure[18])
            hdMeas['imu_roll_angle'] = np.append(hdMeas['imu_roll_angle'], readMeasure[19])

            nbMesures += 1

    except IOError:
        print("Erreur de lecture de la mesure")
        pass




# # Carto Data
# plt.figure(1, figsize=(10,7))
# m = Basemap(projection='gall', lon_0=0,llcrnrlat=-90,urcrnrlat=90, llcrnrlon=-180,urcrnrlon=180,resolution='c')
# m.drawcoastlines()
# m.drawparallels(np.arange(-90.,91.,30.))
# m.drawmeridians(np.arange(-180.,181.,60.))
# # m.etopo()
# x, y = m(hdMeas['gps_lon'],hdMeas['gps_lat'])
# m.scatter(x, y, c='red', marker='x', s=12, lw=3)
# # cbar=plt.colorbar(orientation='horizontal')
# # cbar.set_label('SWH (m)')
# plt.title('First HyDrones data\n', fontweight='bold')


# plt.show()








