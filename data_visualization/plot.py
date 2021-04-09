from random import randint
import matplotlib.pyplot as plt
squares =[]
for i in range (100):
    squares.append(randint(0,10*i))
fig, ax = plt.subplots()
ax.plot (squares)
plt.show()