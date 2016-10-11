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

# from mpl_toolkits.basemap import Basemap
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
hdMeas['leddar_amplitude'] = np.array([])

hdMeas['baro_pressure'] = np.array([])
hdMeas['baro_sea_level_pressure'] = np.array([])
hdMeas['baro_altitude'] = np.array([])
hdMeas['baro_temperature'] = np.array([])

hdMeas['imu_pitch_angle'] = np.array([])
hdMeas['imu_roll_angle'] = np.array([])
hdMeas['imu_yaw_angle'] = np.array([])
hdMeas['imu_accel_x'] = np.array([])
hdMeas['imu_accel_y'] = np.array([])
hdMeas['imu_accel_z'] = np.array([])
hdMeas['imu_linear_accel_x'] = np.array([])
hdMeas['imu_linear_accel_y'] = np.array([])
hdMeas['imu_linear_accel_z'] = np.array([])
hdMeas['imu_grav_accel_x'] = np.array([])
hdMeas['imu_grav_accel_y'] = np.array([])
hdMeas['imu_grav_accel_z'] = np.array([])

hdClock = dict()
hdClock['gps'] = np.array([])
hdClock['baro'] = np.array([])
hdClock['leddar'] = np.array([])
hdClock['imu'] = np.array([])

# Description de la structure binaire du fichier:
# -----------------------------------------------
Structure = "<dH5BI3fIfd4fdfIdfIdfIdfId12fdfIdfIdfIdfId12fd4fdfIdfIdfIdfId12fdfIdfIdfIdfId12fdfIdfI"
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

            # GPS
            hdClock['gps'] = np.append(hdClock['gps'], readMeasure[0])
            hdMeas['year'] = np.append(hdMeas['year'], readMeasure[1])
            hdMeas['month'] = np.append(hdMeas['month'], readMeasure[2])
            hdMeas['day'] = np.append(hdMeas['day'], readMeasure[3])
            hdMeas['hour'] = np.append(hdMeas['hour'], readMeasure[4])
            hdMeas['min'] = np.append(hdMeas['min'], readMeasure[5])
            hdMeas['sec'] = np.append(hdMeas['sec'], readMeasure[6])
            hdMeas['usec'] = np.append(hdMeas['usec'], readMeasure[7])
            hdMeas['gps_lat'] = np.append(hdMeas['gps_lat'], readMeasure[8])
            hdMeas['gps_lon'] = np.append(hdMeas['gps_lon'], readMeasure[9])
            hdMeas['gps_geoidheight'] = np.append(hdMeas['gps_geoidheight'], readMeasure[10])
            hdMeas['gps_nbsat'] = np.append(hdMeas['gps_nbsat'], readMeasure[11])
            hdMeas['gps_altitude'] = np.append(hdMeas['gps_altitude'], readMeasure[12])
            # 1 baro
            hdClock['baro'] = np.append(hdClock['baro'], readMeasure[13])
            hdMeas['baro_pressure'] = np.append(hdMeas['baro_pressure'], readMeasure[14])
            hdMeas['baro_sea_level_pressure'] = np.append(hdMeas['baro_sea_level_pressure'], readMeasure[15])
            hdMeas['baro_altitude'] = np.append(hdMeas['baro_altitude'], readMeasure[16])
            hdMeas['baro_temperature'] = np.append(hdMeas['baro_temperature'], readMeasure[17])
            # 4 leddar measurements
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[18])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[19])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[20])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[21])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[22])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[23])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[24])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[25])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[26])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[27])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[28])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[29])
            # 1 IMU
            hdClock['imu'] = np.append(hdClock['imu'], readMeasure[30])
            hdMeas['imu_pitch_angle'] = np.append(hdMeas['imu_pitch_angle'], readMeasure[31])
            hdMeas['imu_roll_angle'] = np.append(hdMeas['imu_roll_angle'], readMeasure[32])
            hdMeas['imu_yaw_angle'] = np.append(hdMeas['imu_yaw_angle'], readMeasure[33])
            hdMeas['imu_accel_x'] = np.append(hdMeas['imu_accel_x'], readMeasure[34])
            hdMeas['imu_accel_y'] = np.append(hdMeas['imu_accel_y'], readMeasure[35])
            hdMeas['imu_accel_z'] = np.append(hdMeas['imu_accel_z'], readMeasure[36])
            hdMeas['imu_linear_accel_x'] = np.append(hdMeas['imu_linear_accel_x'], readMeasure[37])
            hdMeas['imu_linear_accel_y'] = np.append(hdMeas['imu_linear_accel_y'], readMeasure[38])
            hdMeas['imu_linear_accel_z'] = np.append(hdMeas['imu_linear_accel_z'], readMeasure[39])
            hdMeas['imu_grav_accel_x'] = np.append(hdMeas['imu_grav_accel_x'], readMeasure[40])
            hdMeas['imu_grav_accel_y'] = np.append(hdMeas['imu_grav_accel_y'], readMeasure[41])
            hdMeas['imu_grav_accel_z'] = np.append(hdMeas['imu_grav_accel_z'], readMeasure[42])
            # 4 leddar measurements
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[43])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[44])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[45])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[46])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[47])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[48])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[49])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[50])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[51])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[52])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[53])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[54])
            # 1 IMU
            hdClock['imu'] = np.append(hdClock['imu'], readMeasure[55])
            hdMeas['imu_pitch_angle'] = np.append(hdMeas['imu_pitch_angle'], readMeasure[56])
            hdMeas['imu_roll_angle'] = np.append(hdMeas['imu_roll_angle'], readMeasure[57])
            hdMeas['imu_yaw_angle'] = np.append(hdMeas['imu_yaw_angle'], readMeasure[58])
            hdMeas['imu_accel_x'] = np.append(hdMeas['imu_accel_x'], readMeasure[59])
            hdMeas['imu_accel_y'] = np.append(hdMeas['imu_accel_y'], readMeasure[60])
            hdMeas['imu_accel_z'] = np.append(hdMeas['imu_accel_z'], readMeasure[61])
            hdMeas['imu_linear_accel_x'] = np.append(hdMeas['imu_linear_accel_x'], readMeasure[62])
            hdMeas['imu_linear_accel_y'] = np.append(hdMeas['imu_linear_accel_y'], readMeasure[63])
            hdMeas['imu_linear_accel_z'] = np.append(hdMeas['imu_linear_accel_z'], readMeasure[64])
            hdMeas['imu_grav_accel_x'] = np.append(hdMeas['imu_grav_accel_x'], readMeasure[65])
            hdMeas['imu_grav_accel_y'] = np.append(hdMeas['imu_grav_accel_y'], readMeasure[66])
            hdMeas['imu_grav_accel_z'] = np.append(hdMeas['imu_grav_accel_z'], readMeasure[67])
            # 1 baro
            hdClock['baro'] = np.append(hdClock['baro'], readMeasure[68])
            hdMeas['baro_pressure'] = np.append(hdMeas['baro_pressure'], readMeasure[69])
            hdMeas['baro_sea_level_pressure'] = np.append(hdMeas['baro_sea_level_pressure'], readMeasure[70])
            hdMeas['baro_altitude'] = np.append(hdMeas['baro_altitude'], readMeasure[71])
            hdMeas['baro_temperature'] = np.append(hdMeas['baro_temperature'], readMeasure[72])

            # 4 leddar measurements
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[73])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[74])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[75])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[76])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[77])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[78])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[79])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[80])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[81])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[82])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[83])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[84])
            # 1 IMU
            hdClock['imu'] = np.append(hdClock['imu'], readMeasure[85])
            hdMeas['imu_pitch_angle'] = np.append(hdMeas['imu_pitch_angle'], readMeasure[86])
            hdMeas['imu_roll_angle'] = np.append(hdMeas['imu_roll_angle'], readMeasure[87])
            hdMeas['imu_yaw_angle'] = np.append(hdMeas['imu_yaw_angle'], readMeasure[88])
            hdMeas['imu_accel_x'] = np.append(hdMeas['imu_accel_x'], readMeasure[89])
            hdMeas['imu_accel_y'] = np.append(hdMeas['imu_accel_y'], readMeasure[90])
            hdMeas['imu_accel_z'] = np.append(hdMeas['imu_accel_z'], readMeasure[91])
            hdMeas['imu_linear_accel_x'] = np.append(hdMeas['imu_linear_accel_x'], readMeasure[92])
            hdMeas['imu_linear_accel_y'] = np.append(hdMeas['imu_linear_accel_y'], readMeasure[93])
            hdMeas['imu_linear_accel_z'] = np.append(hdMeas['imu_linear_accel_z'], readMeasure[94])
            hdMeas['imu_grav_accel_x'] = np.append(hdMeas['imu_grav_accel_x'], readMeasure[95])
            hdMeas['imu_grav_accel_y'] = np.append(hdMeas['imu_grav_accel_y'], readMeasure[96])
            hdMeas['imu_grav_accel_z'] = np.append(hdMeas['imu_grav_accel_z'], readMeasure[97])
            # 4 leddar measurements
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[98])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[99])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[100])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[101])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[102])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[103])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[104])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[105])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[106])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[107])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[108])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[109])
            # 1 IMU
            hdClock['imu'] = np.append(hdClock['imu'], readMeasure[110])
            hdMeas['imu_pitch_angle'] = np.append(hdMeas['imu_pitch_angle'], readMeasure[111])
            hdMeas['imu_roll_angle'] = np.append(hdMeas['imu_roll_angle'], readMeasure[112])
            hdMeas['imu_yaw_angle'] = np.append(hdMeas['imu_yaw_angle'], readMeasure[113])
            hdMeas['imu_accel_x'] = np.append(hdMeas['imu_accel_x'], readMeasure[114])
            hdMeas['imu_accel_y'] = np.append(hdMeas['imu_accel_y'], readMeasure[115])
            hdMeas['imu_accel_z'] = np.append(hdMeas['imu_accel_z'], readMeasure[116])
            hdMeas['imu_linear_accel_x'] = np.append(hdMeas['imu_linear_accel_x'], readMeasure[117])
            hdMeas['imu_linear_accel_y'] = np.append(hdMeas['imu_linear_accel_y'], readMeasure[118])
            hdMeas['imu_linear_accel_z'] = np.append(hdMeas['imu_linear_accel_z'], readMeasure[119])
            hdMeas['imu_grav_accel_x'] = np.append(hdMeas['imu_grav_accel_x'], readMeasure[120])
            hdMeas['imu_grav_accel_y'] = np.append(hdMeas['imu_grav_accel_y'], readMeasure[121])
            hdMeas['imu_grav_accel_z'] = np.append(hdMeas['imu_grav_accel_z'], readMeasure[122])
            # 2 leddar measurements
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[123])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[124])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[125])
            hdClock['leddar'] = np.append(hdClock['leddar'], readMeasure[126])
            hdMeas['leddar_range'] = np.append(hdMeas['leddar_range'], readMeasure[127])
            hdMeas['leddar_amplitude'] = np.append(hdMeas['leddar_amplitude'], readMeasure[128])



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
