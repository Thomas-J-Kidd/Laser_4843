import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


raw_android_data_1ms = pd.read_csv('Lab05_Data\\raw_data.txt', sep="\t", header=None, names = ["Wavelength", "Intensity"])

print(raw_android_data_1ms)
#plt.plot(raw_android_data_1ms["Wavelength"], raw_android_data_1ms["Intensity"], c='Blue')
plt.scatter(raw_android_data_1ms["Wavelength"], raw_android_data_1ms["Intensity"], c='Red', linewidths=0.01)
plt.title("Android Phone with 1ms exposure time")
plt.xlabel("wavelength in nm")
plt.ylabel("intensity")
plt.show()