import numpy as np
import matplotlib.pyplot as plt

# Plotting the constellation diagram for non-rectangular QAM
# Two separate square PSK constellations can build up an 8-QAM constellation
# One 4-PSK at 0 degrees and one 4-PSK with a larger amplitude at 90 degrees

num_symbols = 1000
mod_order = 4
# Generate data symbols
x_int = np.random.randint(0, mod_order, num_symbols)
noise_power = 0.02


# Strictly speaking we don't need to put these in functions; it looks neater
def first_constellation(input_signal, mod_n, rotation, noise_pow):
    # Calculate angle for each symbol
    x_degrees = input_signal*360 / mod_n + rotation
    x_radians = x_degrees * np.pi/180

    x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians)
    awgn = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2)

    r = x_symbols + awgn * np.sqrt(noise_pow)

    return r


def second_constellation(input_signal, mod_n, rotation, noise_pow):
    # Calculate angle for each symbol
    x_degrees = input_signal * 360 / mod_n + rotation
    x_radians = x_degrees * np.pi / 180

    x_symbols = 2*(np.cos(x_radians) + 1j * np.sin(x_radians))
    awgn = (np.random.randn(num_symbols) + 1j * np.random.randn(num_symbols)) / np.sqrt(2)

    r = x_symbols + awgn * np.sqrt(noise_pow)

    return r


# Set figure aspect ratio
plt.figure(figsize=(5, 4.5))

r1 = first_constellation(x_int, 4, 45, noise_power)
r2 = second_constellation(x_int, 4, 0, noise_power)

plt.plot(np.real(r1), np.imag(r1), '.', color="teal")
plt.plot(np.real(r2), np.imag(r2), '.', color="teal")

plt.title("8-QAM Non-Rectangular Constellation", fontfamily="Jost", fontsize="16")
plt.xlabel("In-Phase", fontfamily="Jost", fontsize="12")
plt.ylabel("Quadrature", fontfamily="Jost", fontsize="12")
plt.yticks(fontfamily="Jost", fontsize="12")
plt.xticks(fontfamily="Jost", fontsize="12")

plt.show()
