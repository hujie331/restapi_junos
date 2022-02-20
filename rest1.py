import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import requests

temp_y = 1
def update_line(num, data, line):
    if num == 0:
        return line,
    global temp_y
    x_data.append(num)
    if num is not 0 and num%8 == 1:
        r = requests.get('scheme://device:port/rpc/get-route-engine-information@format=json', auth=('username', 'password'))
        if r: temp_y = r.json()["route-engine-information"][0]["route-engine"][0]["load-average-one"][0]["data"]
    y_data.append(temp_y)
    line.set_data(x_data, y_data)
    return line,

fig1 = plt.figure()
x_data = []
y_data = []
l, = plt.plot([], [])
plt.xlim(0, 80)
plt.ylim(0, 1.5)
plt.xlabel('Time in seconds')
plt.ylabel('CPU utilization (load average)')
plt.title('REST-API test')
line_ani = animation.FuncAnimation(fig1, update_line, 80, fargs=(0, l), interval=1000, blit=True)
plt.show()