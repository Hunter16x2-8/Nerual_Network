#Importing Modules
import math

# Defining Activation Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Implementing Summation on multiplication of Weights and Inputs 
def activation(inputs, weights):
    h = 0
    for x, w in zip(inputs, weights):
        h += x * w
    return sigmoid(h)
# Getting inputs from User 
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    my_list = []
    for i in range(n):
        my_list.append(float(input("Enter element {}: ".format(i+1))))

    weights = [0.3, 0.5, 0.8]
    output = activation(my_list, weights)
    print(output)
    