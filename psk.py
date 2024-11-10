# Phase Shift Keying Waveform in the time domain
import numpy as np
import matplotlib.pyplot as plt

t_min = 0
t_max = 4   # We can change 't_max' but it has to match the length of the 'data' list
f = 4

# Create a vector of 1000 evenly spaced points between t_min and t_max
num_t = 1000
t = np.linspace(t_min, t_max, num_t)

# Splice list to get time vector for a single unit of time
# New list goes from time = 0 to time = (number of points)/(total number of time units)
t_unit = t[int(t_min):int(num_t/t_max)]

# List of binary values to be mapped onto waveform
# Length of data list must match t_max
data = [1, 0, 1, 0]
# data = [1, 0, 1, 0, 1, 0, 1, 1] # => for example

long_data = []

phase_shift = 3

# Loop through data list, if logic 1, phase shift; if logic 0, no phase shift
for i in data:
    if i == 1:
        # Shift in phase
        xt = np.sin(2*np.pi*f*t_unit + phase_shift*i)
        # Convert numpy array to a list so t and the waveform lists have the same dimensions
        xt = list(xt)
        # If we use the 'append' method we get a list of 5 lists since we have 5 bits in the 'data' list
        # long_data.append(xt) # forms a list of lists
        # Using the += operation we are CONCATENATING each list's elements onto the 'long_data' list instead of
        # APPENDING IT
        long_data += xt
    elif i == 0:
        # No shift in phase
        xt = np.sin(2*np.pi*f*t_unit + phase_shift*i)
        xt = list(xt)
        # In both cases add
        # long_data.append(xt)
        long_data += xt


print("Long data ", long_data)
print(type(long_data))
print(len(long_data))

# Set figure aspect ratio
plt.figure(figsize=(8, 5))
# Plot PSK waveform
plt.plot(t, long_data)

# Title and axes labels
plt.title("Phase Shift Modulated Sine Wave", fontfamily="Jost", fontsize="16")
plt.xlabel("Time (small multiple of seconds)", fontfamily="Jost", fontsize="12")
plt.ylabel("Amplitude (V)", fontfamily="Jost", fontsize="12")
plt.yticks(fontfamily="Jost", fontsize="12")
plt.xticks(fontfamily="Jost", fontsize="12")

# Save a figure without a grid
plt.savefig("psk_example_wave.png", dpi=800, transparent=False)

# Save a figure with a grid
plt.grid()
plt.savefig("psk_example_wave-grid.png", dpi=800, transparent=False)
plt.show()





