import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Let's define some physical constants we'll be using for
#Planck's law and Rayleigh-Jeans Law

#Planck's constant in joules*second
h = 6.626e-34
#speed of light in meters per second
c = 3.0e8
#Boltzmann's constant in Joules per second
k_B = 1.38e-23
#Temperature in kelvin K representing approximate surface temp:
T = 5000

#Let's define the wavelength range:
#We'll be defining the range of wavelength over which we'll calculate the spectral radiance
#Starts from 1 nanometer (1e-9 meters) to 3 micrometers (3e-6 meters)
#500 points between 1 nm to 3 micrometers
wavelengths = np.linspace(1e-9, 3e-6, 500)

#let's define Placnk's law:
#this function calculates spectral radiance for a given wavelength and temperature:
def plancks_law(wavelength, T):
    return  (2*h*c**2) / ((wavelength**5) * 1)  / (np.exp((h * c) / (wavelength * k_B * T)) - 1)
