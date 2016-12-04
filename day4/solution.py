import re

test_input = """aaaaa-bbb-z-y-x-100[abxyz]
a-b-c-d-e-f-g-h-100[abcde]
not-a-real-room-100[oarel]
not-a-reaal-room-100[oarel]
not-a-real-rom-100[aorel]
totally-real-room-100[decoy]"""

# test_input = """totally-real-room-200[decoy]"""

file = open('input.txt', 'r')
input = file.read()
rooms = input.split('\n')

room_num_sum = 0

def split_room(room):

	checksum = re.search(r"\[.*\]", room).group()
	checksum = checksum.replace('[', '').replace(']', '')
	sector_id = re.search(r"\d+", room).group()
	room_number = re.search(r"([a-z]|-)*", room).group()
	return checksum, int(sector_id), room_number


def is_real_room(checksum, room_number):
	common_letters = {}
	for letter in room_number:
		if not common_letters.get(letter):
			common_letters[letter] = 1
		else:
			common_letters[letter] = common_letters[letter] + 1
	common_letters.pop('-', None)

	for letter in checksum:
		num_occurences = common_letters.get(letter)
		if not num_occurences:
			return False
		common_letters.pop(letter)
		for entry in common_letters.iteritems():
			if entry[1] >= num_occurences:
				if entry[1] == num_occurences:
					if ord(letter) > ord(entry[0]):
						return False
				else:
					return False

	return True

# for room in rooms:
# 	checksum, sector_id, room_number = split_room(room)
# 	real = is_real_room(checksum, room_number)
# 	if real:
# 		room_num_sum += sector_id
# 	print room_num_sum





# room_number = room[:room.index("[")]
# checksum = room[room.index("["):]
# sector_id = 

# print checksum
# print room_number



file.close()