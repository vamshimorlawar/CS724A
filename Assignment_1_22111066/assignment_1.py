import numpy as np
import matplotlib.pyplot as plt

speed_of_light = 3 * pow(10, 8)
user_loc = np.array([100, 100, 100])

satellite_1_loc = np.array([120, 276, 9900])
satellite_2_loc = np.array([20, 320, 9700])
satellite_3_loc = np.array([50, 162, 10870])
satellite_4_loc = np.array([90, 20, 10230])
satellite_5_loc = np.array([160, 127, 10040])

distance_u_1 = (np.linalg.norm(satellite_1_loc - user_loc))
distance_u_2 = (np.linalg.norm(satellite_2_loc - user_loc))
distance_u_3 = (np.linalg.norm(satellite_3_loc - user_loc))
distance_u_4 = (np.linalg.norm(satellite_4_loc - user_loc))
distance_u_5 = (np.linalg.norm(satellite_5_loc - user_loc))

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

A = np.array([
    [2*(satellite_2_loc[0] - satellite_1_loc[0]), 2*(satellite_2_loc[1] - satellite_1_loc[1]), 2*(satellite_2_loc[2] - satellite_1_loc[2])],
    [2*(satellite_3_loc[0] - satellite_2_loc[0]), 2*(satellite_3_loc[1] - satellite_2_loc[1]), 2*(satellite_3_loc[2] - satellite_2_loc[2])],
    [2*(satellite_4_loc[0] - satellite_3_loc[0]), 2*(satellite_4_loc[1] - satellite_3_loc[1]), 2*(satellite_4_loc[2] - satellite_3_loc[2])],
    [2*(satellite_5_loc[0] - satellite_4_loc[0]), 2*(satellite_5_loc[1] - satellite_4_loc[1]), 2*(satellite_5_loc[2] - satellite_4_loc[2])]
])

b = np.array([
    [(distance_u_1**2 - distance_u_2**2) - (satellite_1_loc[0]**2 - satellite_2_loc[0]**2) - (satellite_1_loc[1]**2 - satellite_2_loc[1]**2) - (satellite_1_loc[2]**2 - satellite_2_loc[2]**2)],
    [(distance_u_2**2 - distance_u_3**2) - (satellite_2_loc[0]**2 - satellite_3_loc[0]**2) - (satellite_2_loc[1]**2 - satellite_3_loc[1]**2) - (satellite_2_loc[2]**2 - satellite_3_loc[2]**2)],
    [(distance_u_3**2 - distance_u_4**2) - (satellite_3_loc[0]**2 - satellite_4_loc[0]**2) - (satellite_3_loc[1]**2 - satellite_4_loc[1]**2) - (satellite_3_loc[2]**2 - satellite_4_loc[2]**2)],
    [(distance_u_4**2 - distance_u_5**2) - (satellite_4_loc[0]**2 - satellite_5_loc[0]**2) - (satellite_4_loc[1]**2 - satellite_5_loc[1]**2) - (satellite_4_loc[2]**2 - satellite_5_loc[2]**2)]
])

#b
x1 = np.linalg.inv((np.dot(A.transpose(), A))) 
x2 = np.dot(x1, A.transpose())
user_loc_calculated = np.dot(x2, b)

print(
    '\n(b) Use the satellite locations and the times to find out the location of the user. Check whether it is coming exactly as (100,100,100)?', 
    '\nx -', user_loc_calculated[0][0], 
    '\ny -', user_loc_calculated[1][0], 
    '\nz -', user_loc_calculated[2][0]
)

def localizationError(rand_time_error):
    distance_1 = (time_u_1 + rand_time_error) * speed_of_light
    distance_2 = (time_u_2 + rand_time_error) * speed_of_light
    distance_3 = (time_u_3 + rand_time_error) * speed_of_light
    distance_4 = (time_u_4 + rand_time_error) * speed_of_light
    distance_5 = (time_u_5 + rand_time_error) * speed_of_light 

    A = np.array([
        [2*(satellite_2_loc[0] - satellite_1_loc[0]), 2*(satellite_2_loc[1] - satellite_1_loc[1]), 2*(satellite_2_loc[2] - satellite_1_loc[2])],
        [2*(satellite_3_loc[0] - satellite_2_loc[0]), 2*(satellite_3_loc[1] - satellite_2_loc[1]), 2*(satellite_3_loc[2] - satellite_2_loc[2])],
        [2*(satellite_4_loc[0] - satellite_3_loc[0]), 2*(satellite_4_loc[1] - satellite_3_loc[1]), 2*(satellite_4_loc[2] - satellite_3_loc[2])],
        [2*(satellite_5_loc[0] - satellite_4_loc[0]), 2*(satellite_5_loc[1] - satellite_4_loc[1]), 2*(satellite_5_loc[2] - satellite_4_loc[2])]
    ])

    b = np.array([
        [(distance_1**2 - distance_2**2) - (satellite_1_loc[0]**2 - satellite_2_loc[0]**2) - (satellite_1_loc[1]**2 - satellite_2_loc[1]**2) - (satellite_1_loc[2]**2 - satellite_2_loc[2]**2)],
        [(distance_2**2 - distance_3**2) - (satellite_2_loc[0]**2 - satellite_3_loc[0]**2) - (satellite_2_loc[1]**2 - satellite_3_loc[1]**2) - (satellite_2_loc[2]**2 - satellite_3_loc[2]**2)],
        [(distance_3**2 - distance_4**2) - (satellite_3_loc[0]**2 - satellite_4_loc[0]**2) - (satellite_3_loc[1]**2 - satellite_4_loc[1]**2) - (satellite_3_loc[2]**2 - satellite_4_loc[2]**2)],
        [(distance_4**2 - distance_5**2) - (satellite_4_loc[0]**2 - satellite_5_loc[0]**2) - (satellite_4_loc[1]**2 - satellite_5_loc[1]**2) - (satellite_4_loc[2]**2 - satellite_5_loc[2]**2)]
    ])

    x1 = np.linalg.inv((np.dot(A.transpose(), A))) 
    x2 = np.dot(x1, A.transpose())
    user_loc_calculated = np.dot(x2, b)

    new_user_loc_calculated = np.array([user_loc_calculated[0][0], user_loc_calculated[1][0], user_loc_calculated[2][0]])
    localization_error = (np.linalg.norm(new_user_loc_calculated - user_loc))
    
    return localization_error

#c
rand_time_error = np.random.uniform(pow(10,-9), 99*pow(10,-9))
localization_error = localizationError(rand_time_error)
print('\n(c) Check how much location inaccuracy it showing up?\ntime error - ', rand_time_error, 's, location inaccuracy - ', localization_error)

localization_error_list = []
time_error_list = []
for i in range(100):
    time_error_list.append(np.random.uniform(pow(10,-9), 99*pow(10,-9)))

for time_error in time_error_list:
    localization_error_list.append(localizationError(time_error))

#d
average_localization_error = sum(localization_error_list)/len(localization_error_list)
print('\n(d) Take the average localization errors = ', average_localization_error)

plt.figure(num=0, dpi=120)
plt.title('(d) timing errors vs localization error')
plt.xlabel('Time Errors in (Seconds)')
plt.ylabel('Localization Errors in (Meters)')

plt.plot(time_error_list, localization_error_list)
plt.scatter(time_error_list, localization_error_list, c='purple')
plt.show()