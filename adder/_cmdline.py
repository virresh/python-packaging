#!/usr/bin/env python
from adder import add
import sys


def main():
	if len(sys.argv) != 3:
		print("Usage : adder <number_1> <number_2>")
		return
	numOne = int(sys.argv[1])
	numTwo = int(sys.argv[2])
	if numOne < 0 or numTwo < 0:
		print("Only positive integers allowed")
		return
	sumR = add.add(numOne, numTwo)
	print("{} + {} = {}".format(numOne,numTwo,sumR))
	return (sumR)

if __name__ == '__main__':
	main()