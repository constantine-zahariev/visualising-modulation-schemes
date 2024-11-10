import numpy as np
import matplotlib.pyplot as plt
import scipy

t_min = 0
t_max = 8   # We can change this as long as it matches the number of bits in the 'data' list
f = 3

# Create vector of 1000 evenly spaced points between t_min and t_max
num_t = 1000
t = np.linspace(t_min, t_max, num_t)

# Signal
xt = np.sin(2*np.pi*f*t)

# List of binary values to be mapped onto waveform
data = [1, 0, 1, 0, 1, 1, 0, 1]

# Calculate how many samples per unit of time
# Each unit of time will contain one data symbol
samples_per_unit_time = num_t / (t_max - t_min)
print("Samples per unit time: ", samples_per_unit_time)

# Empty list to store repeated sample values to be used as varying amplitude
long_data = []

# Loop through data list, if logic 1, high amplitude; if logic 0, low amplitude
for i in data:
    if i == 1:
        # long_data.append([3*i] * int(samples_per_unit_time))
        # Note: 'append' method does not produce a 1-by-N array, not sure of workaround
        long_data += [2*i] * int(samples_per_unit_time)
    elif i == 0:
        # long_data.append([(i+1)] * int(samples_per_unit_time))
        long_data += [i+1] * int(samples_per_unit_time)

# Modulate sine wave by multiplying with amplitude vector
xt_mod = np.array(long_data)*xt

# For debugging purposes
print("The amplitude vector is ", long_data)
print("The amplitude modulated values are ", xt_mod)

# Plot ASK waveform
plt.figure(figsize=(8, 5))
plt.plot(t, xt_mod)
plt.title("Amplitude Modulated Sine Wave", fontfamily="Jost", fontsize="16")
plt.xlabel("Time (small multiple of seconds)", fontfamily="Jost", fontsize="12")
plt.ylabel("Amplitude (V)", fontfamily="Jost", fontsize="12")
plt.yticks(fontfamily="Jost", fontsize="12")
plt.xticks(fontfamily="Jost", fontsize="12")

# Save a figure without a grid
plt.savefig("ask_example_wave.png", dpi=800, transparent=False)

plt.grid()

# Save a figure with a grid
plt.savefig("ask_example_wave-grid.png", dpi=800, transparent=False)
plt.show()
