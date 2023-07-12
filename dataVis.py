import numpy as np
import matplotlib.pyplot as plt

loads = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

x = np.zeros(len(loads))
y = np.zeros(len(loads))

for i, load in enumerate(loads):
    file_name = "PS_LOAD_%.1f.txt" % load
    my_file = open(file_name, "r")

    # reading the file
    data = my_file.read()

    # replacing and splitting the text
    # when a newline ('\n') is seen.
    data_into_list = data.split("\n")
    my_file.close()

    # Exclude empty strings from the data
    completion_times = np.array([float(x) for x in data_into_list if x], dtype=float)

    x[i] = load
    y[i] = np.average(completion_times)

    print(np.average(completion_times))

plt.plot(x, y)
plt.xlabel('Load')
plt.ylabel('Average Completion Time')
plt.title('PS Load vs. Average Completion Time')

plt.ylim(0, 10)  # Set the y-axis limits from 0 to 20
plt.yticks(np.arange(0, 12, 2))  # Set the y-axis tick locations and labels from 0 to 20 with an increment of 2

plt.show()
