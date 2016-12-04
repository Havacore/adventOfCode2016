from solution import split_room

file = open('input.txt', 'r')
input = file.read()
rooms = input.split('\n')

test_input = """qzmt-zixmtkozy-ivhz-343[abcdef]"""

rooms = input.split('\n')

def decrypt(room_number, sector):
	decrypted_string = ""
	for letter in room_number:
		if letter == "-":
			decrypted_string += " "
			continue
		ordinal = ord(letter)
		ordinal += sector
		while ordinal > 122:
			ordinal -= 26

		decrypted_string += chr(ordinal)

	return decrypted_string


for room in rooms:
	checksum, sector, room_number = split_room(room)
	decrypted_string = decrypt(room_number, sector)
	if decrypted_string == "northpole object storage ":
		print "found it"
		print sector
	# print decrypted_string


file.close()