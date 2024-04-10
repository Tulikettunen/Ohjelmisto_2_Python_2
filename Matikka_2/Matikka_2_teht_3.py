import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.subplots()

# Piirrä yksikköympyrä
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y)

# Merkkaile halutut kulmat
angles_degrees = [30, 45, 60, 90, 120, 150, 180, 270]
angles_radians = np.radians(angles_degrees)

for angle_deg, angle_rad in zip(angles_degrees, angles_radians):
    plt.scatter(np.cos(angle_rad), np.sin(angle_rad), color='red')
    plt.annotate(str(angle_deg) + u'\u00b0', (np.cos(angle_rad), np.sin(angle_rad)), textcoords="offset points", xytext=(10,10), ha='center')

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

ax.axis('equal')
plt.grid(False)
plt.title('Yksikköympyrä johon merkattu kulmat kehälle')
plt.show()




import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

# Levennä kuva kolminkertaiseksi
plt.figure(figsize=(6.4*3, 4.8))

plt.plot(X,C)
plt.plot(X,S)

# Piirrä käyrät ja vaihda värit sekä piirtotyyli
plt.plot(X, C, color='violet', linestyle='--', label='Kosini')
plt.plot(X, S, color='pink', linestyle='-.', label='Sini')

# Aseta akselien tekstit muotoon π, π/2 jne ...
plt.xticks([-3*np.pi, -2*np.pi, -1*np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
           [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$'])
plt.yticks([-1, 0, 1], ['-1', '0', '1'])

# Lisää selite
plt.legend()

plt.show()