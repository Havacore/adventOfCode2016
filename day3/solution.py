file = open('day3_input.txt', 'r')
triangles = [x.strip().split() for x in file.read().split('\n')]
# print triangles[0]

bullshit_triangles = triangles

new_triangles = []

for bullshit_index in xrange(0, len(bullshit_triangles), 3):

	six_shitty_triangles = bullshit_triangles[bullshit_index:bullshit_index + 6]
	new_triangles.append([six_shitty_triangles[0][0], six_shitty_triangles[1][0], six_shitty_triangles[2][0]])
	new_triangles.append([six_shitty_triangles[0][1], six_shitty_triangles[1][1], six_shitty_triangles[2][1]])			
	new_triangles.append([six_shitty_triangles[0][2], six_shitty_triangles[1][2], six_shitty_triangles[2][2]])

print new_triangles

def is_triangle_possible(triangle):
	if triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[0] + triangle[2] > triangle[1]:
		return True
	return False

num_possible_triangles = 0
for triangle in new_triangles:
	triangle = [int(side) for side in triangle]
	num_possible_triangles = num_possible_triangles + 1 if is_triangle_possible(triangle) else num_possible_triangles

print num_possible_triangles
print len(new_triangles)

file.close()