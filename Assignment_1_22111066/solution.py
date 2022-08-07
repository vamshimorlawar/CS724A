import numpy as np
import matplotlib.pyplot as plt

speed_of_light = 3 * pow(10, 8)
user_loc = np.array([100, 100, 100])

satellite_1_loc = np.array([120, 220, 10000])
satellite_2_loc = np.array([220, 320, 10040])
satellite_3_loc = np.array([450, 760, 10550])
satellite_4_loc = np.array([90, 1220, 10300])
satellite_5_loc = np.array([560, 5720, 10400])

distance_u_1 = abs(np.linalg.norm(satellite_1_loc - user_loc))
distance_u_2 = abs(np.linalg.norm(satellite_2_loc - user_loc))
distance_u_3 = abs(np.linalg.norm(satellite_3_loc - user_loc))
distance_u_4 = abs(np.linalg.norm(satellite_4_loc - user_loc))
distance_u_5 = abs(np.linalg.norm(satellite_5_loc - user_loc))

time_u_1 = distance_u_1 / speed_of_light
time_u_2 = distance_u_2 / speed_of_light
time_u_3 = distance_u_3 / speed_of_light
time_u_4 = distance_u_4 / speed_of_light
time_u_5 = distance_u_5 / speed_of_light

#a
print(
    '(a) Calculate the time it takes for a signal to arrive from each one of these satellites to the user?',
    '\nSatellite 1 - ', time_u_1 , 's',
    '\nSatellite 2 - ', time_u_2 , 's', 
    '\nSatellite 3 - ', time_u_3 , 's', 
    '\nSatellite 4 - ', time_u_4 , 's', 
    '\nSatellite 5 - ', time_u_5 , 's'
)
# Time taken by signal to reach the user device is almost in micro-seconds


A = np.array([
    [2*(satellite_2_loc[0] - satellite_1_loc[0]), 2*(satellite_2_loc[1] - satellite_1_loc[1]), 2*(satellite_2_loc[2] - satellite_1_loc[2])],
    [2*(satellite_3_loc[0] - satellite_2_loc[0]), 2*(satellite_3_loc[1] - satellite_2_loc[1]), 2*(satellite_3_loc[2] - satellite_2_loc[2])],
    [2*(satellite_4_loc[0] - satellite_3_loc[0]), 2*(satellite_4_loc[1] - satellite_3_loc[1]), 2*(satellite_4_loc[2] - satellite_3_loc[2])]
])

b = np.array([
    [(distance_u_1**2 - distance_u_2**2) - (satellite_1_loc[0]**2 - satellite_2_loc[0]**2) - (satellite_1_loc[1]**2 - satellite_2_loc[1]**2) - (satellite_1_loc[2]**2 - satellite_2_loc[2]**2)],
    [(distance_u_2**2 - distance_u_3**2) - (satellite_2_loc[0]**2 - satellite_3_loc[0]**2) - (satellite_2_loc[1]**2 - satellite_3_loc[1]**2) - (satellite_2_loc[2]**2 - satellite_3_loc[2]**2)],
    [(distance_u_3**2 - distance_u_4**2) - (satellite_3_loc[0]**2 - satellite_4_loc[0]**2) - (satellite_3_loc[1]**2 - satellite_4_loc[1]**2) - (satellite_3_loc[2]**2 - satellite_4_loc[2]**2)]
])

user_loc_calculated = np.dot(np.linalg.inv(A), b)

print(
    '\n(b) Use the satellite locations and the times to find out the location of the user. Check whether it is coming exactly as (100,100,100)?', 
    '\nx -', user_loc_calculated[0][0], 
    '\ny -', user_loc_calculated[1][0], 
    '\nz -', user_loc_calculated[2][0]
)
#Using the times calculated in (a) and the satellite locations we get the user location very close to the considered location

