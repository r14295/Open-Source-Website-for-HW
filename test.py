# 开发者：Robin Zhang
# 开发时间：2022/4/11 22:27
import matplotlib.pyplot as plt
xs, y1s, y2s =[], [], []
ns = list(range(-10000, 10000))
for i in ns:
    x = i/1000
    xs.append(x)
    y1 = (-x**2)*2 - 5*x + 17
    y2 = (x**2)*3 + 3*x + 5
    y1s.append(y1)
    y2s.append(y2)
min_delta_y = (y1s[0]-y2s[0])**2
for i in range(1, 20000):
    delta_y = (y1s[i]-y2s[i])**2
    if delta_y < min_delta_y:
        min_delta_y = delta_y
for i in range(1, 20000):
    if (y1s[i] - y2s[i])**2 == min_delta_y:
        print(min_delta_y, xs[i], y1s[i], y2s[i], i)

#print(xs, '\n', y1s, '\n', xs, '\n', y2s)

fig, ax = plt.subplots()
ax.plot(xs, y1s)
ax.plot(xs, y2s)
plt.show()