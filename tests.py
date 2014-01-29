#! /usr/bin/env python

def add(x, y):
	return x + y

def test_1():
	result = add(1, 2)
	assert result == 3

def test_2():
	result = add(4, 3)
	assert result != 6

