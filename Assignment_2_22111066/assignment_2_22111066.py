from statistics import variance
import numpy as np
import matplotlib.pyplot as plt

#a, b
distances = [7, 23, 52, 93, 129]
rssi = [
    -64, -65, -67, -62, -66,
    -74, -75, -76, -76, -75,
    -82, -84, -81, -80, -80,
    -87, -88, -84, -85, -84,
    -89, -91, -89, -92, -90
]

distances = np.log10(distances)
distances = np.repeat(distances, 5)

#c
plt.xlabel('Distances (log scale)')
plt.ylabel('RSSI Value dBm')
plt.scatter(distances, rssi)

bestFit = np.polyfit(distances, rssi, 1)
plt.plot(distances, bestFit[0]*distances + bestFit[1], 'r')
plt.show()

#d
slopeBestFit = bestFit[0]
pathLossExponent = abs(slopeBestFit/10)

print("The slope of the best fit straight line is", slopeBestFit)
print("The path loss exponent is", pathLossExponent)

#e
variance = 0
for i in range(len(rssi)):
    variance += (slopeBestFit * distances[i] + bestFit[1] - rssi[i]) ** 2

print("(e) Variance of these RSSI samples w.r.t the best fit line", variance)


d0 = 1
prd0 = bestFit[0] * np.log10(d0) + bestFit[1]
print("prd0", prd0)

def estimateDistance(prd):
    estimatedDistance = pow(10, (prd - prd0)/slopeBestFit)
    return estimatedDistance

prd = -89
print('Estimated distance', estimateDistance(prd))

prdList = [-51, -71, -89]
actualDistance = [1, 16, 117]
errorInDistance = []

for i in range(len(prdList)):
    ed = estimateDistance(prdList[i])
    error = ed - actualDistance[i] 
    errorInDistance.append(error)

print("Average error", np.average(errorInDistance))