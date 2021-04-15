# Linear regression

import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading

    input_file = StringIO(train_string)
    inp = np.genfromtxt(input_file, skip_header=1, dtype="int")
    pricePos = len(inp) - 1
    x_train = np.asarray([x[:pricePos] for x in inp])
    y_train = np.asarray([y[pricePos] for y in inp])

    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train, rcond=None)[0]

    # read in the test data and separate x_test from it
    test_inp = np.genfromtxt(StringIO(test_string), skip_header=1, dtype="int")
    x_test = [x[:pricePos] for x in test_inp]

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()