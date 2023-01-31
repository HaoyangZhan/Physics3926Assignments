import numpy as np
import matplotlib.pyplot as plt

# Part 1
def ErrorString():# A function for showing a error sentence entering the wrong string in the input
    """Entered wrong string"""
    return 0
#Creating a dictionary which is including the physical constants
def Phys_Cons(key):
    physcont = {
        'c': 2.99792458e8,
        'h' : 6.62606896e-34,
        'k' : 1.3806504e-23,
        'me' : 9.10938215e-31,
        'amu' : 1.660538782e-27,
        'e' : 1.602176487e-19,
        'a0' : 5.2917720859e-11,
        'g' : 6.67428e-11,
        'sigma' : 5.670400e-8,
        }
    #check if the string is in the dictionary
    if key.lower() in physcont:
        return physcont[key]
    else:
        return ErrorString.__doc__
       
#Showing what kinds of constants are in the dictionary
def PhysicalConstant():
    """
    Available constants:
        Speed of light(c), Planck's Constant(h),
        Boltzmann's Constant(k), Electron Mass(Me),
        Atomic Mass Unit(amu), Electron Charge(e),
        Bohr Radius(a0), Gravitational Constant(G),
        Stefan-Boltzmann Constant(Sigma)
    """
    return 0
print(PhysicalConstant.__doc__)
#testing the function with speed of light 
print(Phys_Cons('c'))

#Part 2
#defining a equation that is using physical constant to calculate
def PlanckRadiation(Temp,Freq):
    a = (2*Phys_Cons('h')*(Freq**3)/(Phys_Cons('c')**2))
    b = (np.exp(Phys_Cons('h')*Freq/(Phys_Cons('k')*Temp))-1)**(-1)
    return a*b
# #creating the lists for calculation
T = np.array([100.0, 200.0, 300.0, 400.0, 500.0])
F = np.array([50, 100, 150, 200])
# #printing the array of the answers
print(PlanckRadiation(T[:,np.newaxis], F))

# #Part 3
# #defining the range for the wavelength
wave = np.arange(10e-9,2000.1e-9,10e-9)
# #setting the three temperature
temp1 = np.array([5000])
temp2 = np.array([10000])
temp3 = np.array([15000])
# #defining an another equation that works for the wavelength instead of frequency
def PlanckRadiation2(Temp,wavel):
    c = (2*Phys_Cons('h')*(Phys_Cons('c')**2)/(wave**5))
    d = (np.exp(Phys_Cons('h')*Phys_Cons('c')/(wave*Phys_Cons('k')*Temp))-1)**(-1)
    return c*d
#putting the result into the array
y1 = np.array([PlanckRadiation2(temp1,wave)])
y2 = np.array([PlanckRadiation2(temp2,wave)])
y3 = np.array([PlanckRadiation2(temp3,wave)])
#plotting three different lines in the plots
plt.plot(wave,y1[0,:], label = "5000K")
plt.plot(wave,y2[0,:], label = "10000K")
plt.plot(wave,y3[0,:], label = "15000K")
plt.legend()
plt.show()

# Part 4
#defining the stefan-boltzmann function
def Stefan_Boltzmann(Temp):
    return Phys_Cons('sigma')*Temp**4/np.pi
#creating the new array for new temperature and wavelength
Temperature = np.array([500, 1000, 1500, 2000])
WaveLength = np.array([100e-9, 200e-9, 300e-9, 400e-9])
#making the calculation
integral = np.trapz(PlanckRadiation2(Temperature[:,np.newaxis],WaveLength), dx=500)
print(integral)
print(Stefan_Boltzmann(Temperature))

plt.plot(Temperature,Stefan_Boltzmann(Temperature), label = "Stefan_Boltzmann")
# plt.plot(Temperature,integral, label = "integral")
plt.legend()
plt.show()
