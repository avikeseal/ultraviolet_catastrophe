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

#define rayleigh-jeans law:
#this function calculates the spectral radiance using the rayleigh-jeans approximation
#which is valid for longer wavelengths:
def rayleigh_jeans_law(wavelength, T):
    return (2*c*k_B*T) / (wavelength**4)

#initializing the plot:
#ax.set_xlim and ax.set_ylim define the wavelength (x-axis) and radiance (y-axis).
#we also create two lines, one for plancks and one for rayleigh-jeans:
fig, ax =  plt.subplots(figsize=(10, 6))

#wavelengths in nm converted from m:
ax.set_xlim(0, 3000)
#radiance values, adjusted for visualization:
ax.set_ylim(0, 2e13)

ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Spectral Radiance')
ax.set_title("Trnasition from Planck's Law to Rayleigh-Jeans Law:")
line1, = ax.plot([], [], label="Planck's Law")
line2, = ax.plot([], [], label="Rayleigh-Jeans Law", linestyle='dashed')
ax.legend()

#initializing the animation:
#this function sets initial conditions for the plot:
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

#this function updates the data for each frame in the animation
#it calculates th e spectral radiance of the current frame's wavelegth range 
#using both Planck's and Rayleigh-Jeans Law. It then updates the plot with the new data:
def update(frame):
    current_wavelengths = wavelengths[:frame]
    B_planck = plancks_law(current_wavelengths, T)
    B_rayleigh_jeans = rayleigh_jeans_law(current_wavelengths, T)

    #convert wavelength to nm:
    line1.set_data(current_wavelengths * 1e9, B_planck)
    line2.set_data(current_wavelengths * 1e9,  B_rayleigh_jeans)
    return line1, line2

#creating the animation:
anim = animation.FuncAnimation(fig, update, frames=len(wavelengths), init_func=init, blit=True, interval=50)






















