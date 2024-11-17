import numpy as np
import matplotlib.pyplot as plt

# Magnitude and angle for 16-QAM symbols
# https://dsplog.com/2008/06/01/binary-to-gray-code-for-16qam/

num_symbols = 1000

# 16-QAM symbol coordinates are hardcoded
modulation_16_qam = {
    '0': (-1, 1), '1': (-1/3, 1), '2': (1/3, 1), '3': (1, 1),
    '4': (-1, 1/3), '5': (-1/3, 1/3), '6': (1/3, 1/3), '7': (1, 1/3),
    '8': (-1, -1/3), '9': (-1/3, -1/3), '10': (1/3, -1/3), '11': (1, -1/3),
    '12': (-1, -1), '13': (-1/3, -1), '14': (1/3, -1), '15': (1, -1),
}

# Generate random sequence of integers in range 0 to 15
# Number of values equals number of data dymbols
sym_vals = np.random.randint(0, 16, num_symbols)

# Empty list for storing complex numbers
sym = []

for i in sym_vals:
    # For every value in sym_vals
    # Get corresponding symbol coordinates
    # and convert to a complex number
    # then we can introduce noise and distortion and plot the symbols
    current_sym = modulation_16_qam[str(i)]
    sym.append(current_sym[0] + 1j*current_sym[1])

# For verification
print("List of complex symbols: ", sym)

# Convert list of symbols to numpy array so we can do matrix multiplication
sym_array = np.array(sym)

# Additive White Gaussian Noise complex values
awgn = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2)

# Set noise power
noise_power = 0.01

# Add on Additive White Gaussian Noise to data symbol values
r = sym + awgn*np.sqrt(noise_power)

# Set figure aspect ratio
plt.figure(figsize=(5.5, 5))

plt.plot(np.real(r), np.imag(r), '.', color="steelblue")

# plt.grid(True)
plt.title("16-QAM Constellation", fontfamily="Jost", fontsize="16")
plt.xlabel("In-Phase", fontfamily="Jost", fontsize="12")
plt.ylabel("Quadrature", fontfamily="Jost", fontsize="12")
plt.yticks(fontfamily="Jost", fontsize="12")
plt.xticks(fontfamily="Jost", fontsize="12")

# Reference constellation - this can be commented out
for k, v in modulation_16_qam.items():
    plt.plot(v[0], v[1], 'x', color="firebrick")


# Save a figure without a grid
plt.savefig("16-qam.png", dpi=800, transparent=False)

plt.grid()

# Save a figure with a grid
plt.savefig("16-qam.png", dpi=800, transparent=False)

plt.show()
