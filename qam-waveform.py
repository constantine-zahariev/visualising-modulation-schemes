# 8-QAM Waveforms Plot
import numpy as np
import matplotlib.pyplot as plt

t_min = 0
t_max = 8   # We can change 't_max' but it has to match the length of the 'data' list
f = 2

# Create a vector of 1000 evenly spaced points between t_min and t_max
num_t = 1000
t = np.linspace(t_min, t_max, num_t)

# Splice list to get time vector for a single unit of time
# New list goes from time = 0 to time = (number of points)/(total number of time units)
t_unit = t[int(t_min):int(num_t/t_max)]

# List of binary values to be mapped onto waveform
# Length of data list must match t_max
# For 8-QAM we have a list of 3-bit strings

# Switch between two different lists for different waveforms
data = ['000', '001', '010', '011', '100', '101', '110', '111']
# data = ['010', '100', '000', '011', '001', '111', '110', '010']

long_data = []  # Empty list

phase_shifts_deg = [0, 45, 90, 135, 180, 225, 270, 315]
PI = np.pi
phase_shifts = [0, PI/4, PI/2, 3*PI/4, PI, 5*PI/4, 3*PI/2, 7*PI/4]

# Loop through data list, if logic 1, phase shift; if logic 0, no phase shift
for i in data:

    if i == '000':
        # Double the amplitude and select first phase in 'phase_shifts' list
        # For the remaining conditions, alternate amplitude and go through the 'phase_shifts' list
        xt = 2*np.sin(2 * np.pi * f * t_unit + phase_shifts[0])
        xt = list(xt)
        long_data += xt

    elif i == '001':
        xt = np.sin(2 * np.pi * f * t_unit + phase_shifts[1])
        xt = list(xt)
        long_data += xt

    elif i == '010':
        xt = 2*np.sin(2 * np.pi * f * t_unit + phase_shifts[2])
        xt = list(xt)
        long_data += xt

    elif i == '011':
        xt = np.sin(2 * np.pi * f * t_unit + phase_shifts[3])
        xt = list(xt)
        long_data += xt

    elif i == '100':
        xt = 2 * np.sin(2 * np.pi * f * t_unit + phase_shifts[4])
        xt = list(xt)
        long_data += xt

    elif i == '101':
        xt = np.sin(2 * np.pi * f * t_unit + phase_shifts[5])
        xt = list(xt)
        long_data += xt

    elif i == '110':
        xt = 2 * np.sin(2 * np.pi * f * t_unit + phase_shifts[6])
        xt = list(xt)
        long_data += xt

    elif i == '111':
        xt = np.sin(2 * np.pi * f * t_unit + phase_shifts[7])
        xt = list(xt)
        long_data += xt


# For debugging
print(type(long_data))
print(len(long_data))

# Set figure aspect ratio
plt.figure(figsize=(10, 5))
# Plot PSK waveform
plt.plot(t, long_data)

# Title and axes labels
plt.title("8-QAM Modulated Sine Wave", fontfamily="Jost", fontsize="16")
plt.xlabel("Time (small multiple of seconds)", fontfamily="Jost", fontsize="12")
plt.ylabel("Amplitude (V)", fontfamily="Jost", fontsize="12")
plt.yticks(fontfamily="Jost", fontsize="12")
plt.xticks(fontfamily="Jost", fontsize="12")

# Save a figure without a grid
plt.savefig("8-qam-waveform.png", dpi=800, transparent=False)

# Save a figure with a grid
plt.grid()
plt.savefig("8-qam-waveform.png", dpi=800, transparent=False)
plt.show()
