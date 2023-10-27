import seaborn as sea
import random as rand
import matplotlib.pyplot as plt
from math import sqrt

def main(numSims: int, visualize: bool, radius: float = 0.5) -> None:
    numbPointsinCircle = 0
    data ={'x': [], 'y': [], 'color': []}
    for _ in range(numSims):
        x,y = rand.uniform(0,(radius*2)), rand.uniform(0,(radius*2))
        # print(x,y)
        r = sqrt((x - radius)**2 + (y-radius) ** 2)
        # print(r)
        numbPointsinCircle += r <= (radius)
        data['color'].append('green' if r <= (radius) else 'red') if visualize else None
        data['x'].append(x)
        data['y'].append(y)
        

    print(numbPointsinCircle)
    print(f"pi = {4*(numbPointsinCircle/numSims)}")
    if visualize:
        sea.scatterplot(data=data, x='x', y='y', hue='color')
        plt.legend(title='Color', labels=['Within Radius', 'Outside Radius'], loc="upper right")
        plt.axis('equal')
        plt.show()
    return

if __name__=="__main__":
    main(10000, True, 50)