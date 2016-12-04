somechar = 'q'

expected = 'v'
sector = 343

ordinal = ord(somechar)
print ordinal

ordinal += 343

while ordinal > ord('z'):
	ordinal -= 26

print chr(ordinal)

