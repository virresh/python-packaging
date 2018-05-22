#!/usr/bin/env python
from adder.add import add

def multiply(a,b):
	if a<0 or b<0:
		return 0
	ans = 0
	for i in range(0,b):
		ans = add(ans,a)
	return ans
