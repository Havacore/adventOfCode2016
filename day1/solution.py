import sys

input = """R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3"""

def calculate_direction(going, facing):
	cardinal = None 
	if going == 'R':
		if facing == 'north':
			cardinal = 'east'
		elif facing == 'east':
			cardinal = 'south'
		elif facing == 'south':
			cardinal = 'west'
		elif facing == 'west':
			cardinal = 'north'

	elif going == 'L':
		if facing == 'north':
			cardinal = 'west'
		elif facing == 'west':
			cardinal = 'south' 
		elif facing == 'south':
			cardinal = 'east'
		elif facing == 'east':
			cardinal = 'north'

	if not cardinal:
		print "ERROR, not R or L"
		sys.exit()
	return cardinal

def calculate_position(facing, vector, current_position, visited_points):
	if facing == 'north':
		difference = (0, vector)
	elif facing == 'south':
		difference = (0, -vector)
	elif facing == 'west':
		difference = (-vector, 0)
	elif facing == 'east':
		difference = (vector, 0)
	
	for i in xrange(abs(vector)):
		if facing == 'north':
			pos = (current_position[0], current_position[1] + i)
			if pos in visited_points:
				print "first position re-visited: {}".format(pos)
		if facing == 'south':
			pos = (current_position[0], current_position[1] - i)
			if pos in visited_points:
				print "first position re-visited: {}".format(pos)
		if facing == 'west':
			pos = (current_position[0] - i, current_position[1])
			if pos in visited_points:
				print "first position re-visited: {}".format(pos)
		if facing == 'east':
			pos = (current_position[0] + i, current_position[1])
			if pos in visited_points:
				print "first position re-visited: {}".format(pos)
			
		visited_points.append(pos)


	new_position = (current_position[0] + difference[0], current_position[1] + difference[1]), visited_points
	return new_position

directions = [x.strip() for x in input.split(',')]

facing = 'north'
current_position = (0, 0)
visited_points = []

for direction in directions:
	going = direction[0]
	vector = int(direction[1:])
	facing = calculate_direction(going, facing)
	current_position, visited_points = calculate_position(facing, vector, current_position, visited_points)

x_difference = abs(current_position[0])
y_difference = abs(current_position[1])
print visited_points
print x_difference + y_difference
print current_position
