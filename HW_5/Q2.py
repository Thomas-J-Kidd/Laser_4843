import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------
# Q2.1 defining basic variables 
theta_1 = np.linspace(0,2*np.pi, 500)

R1_1 = 0.99
R2_1 = 0.9


# defining the power transmission coefficient
T_1 = ((1-R1_1)*(1-R2_1))/((1-np.sqrt(R1_1*R2_1))**2+(4*np.sqrt(R1_1*R2_1)*(np.sin(theta_1))**2))
# defining R
R_1 = 1-T_1

# plotting 
plt.subplots(layout="constrained")
plt.suptitle("Power tranmission coeff T and R vs Theta")

ax1 = plt.subplot(111)
plt.plot(T, theta, c='Blue',linewidth = 1, label = "T vs theta")
plt.xlabel("T or R")
plt.ylabel("theta")

ax2 = plt.subplot(111)
plt.plot(R, theta, c='red',linewidth = 1, label = "R vs theta")
plt.grid()
plt.legend()

plt.show()

#----------------------------------
# Q2.2 defining basic variables 
R1_2 = np.array([0.1,0.3,0.5,0.7,0.9])
R2_2 = np.array([0.1,0.3,0.5,0.7,0.9])
theta_2 = (2*np.pi)+(1/16*np.pi)

# defining the power transmission coefficient
T_2 = ((1-R1_2)*(1-R2_2))/((1-np.sqrt(R1_2*R2_2))**2+(4*np.sqrt(R1_2*R2_2)*(np.sin(theta_2))**2))
# defining R
R_2 = 1-T_2


# plotting 
ax1 = plt.subplot(121)
plt.scatter(T, R1, c='Blue',linewidth = 1, label = "T vs R1")
plt.plot(T, R1, c='Blue',linewidth = 1, label = "T vs R1")
plt.xlabel("T")
plt.ylabel("R1")
plt.title("")
plt.grid()
plt.legend()

ax2 = plt.subplot(122)
plt.scatter(T, R2, c='Red',linewidth = 1, label = "T vs R2")
plt.plot(T, R2, c='Red',linewidth = 1, label = "T vs R2")
plt.xlabel("T")
plt.ylabel("R2")
plt.title("")
plt.grid()
plt.legend()


plt.show()