## Peasant Algorithm

def Peasant(x, y):
	sum = 0
	while x>0:
		if x % 2 == 1: sum += y
		y = y << 1
		x = x >> 1
	return sum

StartX = 48
StartY = 65

print Peasant(StartX, StartY)