import seaborn as sea
import random as rand
import matplotlib.pyplot as plt

def main(numSims: int) -> None:
    numbPointsinCircle = 0
    data ={'x': [], 'y': [], 'color': []}
    for _ in range(numSims):
        x,y  = rand.random(), rand.random()
        r = (x - 0.5)**2 + (y-0.5) ** 2 <= (0.5 **2)
        numbPointsinCircle += r <= .25
        data['color'].append('green' if r <= 0.25 else 'red')
        data['x'].append(x)
        data['y'].append(y)
        

    print(numbPointsinCircle)
    print(f"pi = {4*numbPointsinCircle/numSims}")

    sea.scatterplot(data=data, x='x', y='y', hue='color', palette={'red': 'red', 'green': 'green'})
    plt.legend(title='Color', labels=['Within Radius', 'Outside Radius'])
    plt.axis('equal')
    plt.show()
    return

if __name__=="__main__":
    main(100000000)