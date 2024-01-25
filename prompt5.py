import numpy as np
import math


def sin_thousand(a,b,c):
    x_array = np.linspace(a, b, c)
    sinx_array = np.sin(x_array)
    print("{:<10} {:<10}".format('x', 'sin(x)'))
    for x, sin_x in zip(x_array, sinx_array):
        print("{:<10.2f} {:<10.2f}".format(x, sin_x))
    

def main():
    sin_thousand(0, 2 * np.pi, 1000)

if __name__ == "__main__":
    main()
