messages_file = open('input.txt', 'r')
messages = messages_file.read().split('\n')

test_input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

occurence_dict = {
	'1': {},
	'2': {},
	'3': {},
	'4': {},
	'5': {},
	'6': {},
	'7': {},
	'8': {},
}

#messages = test_input.split('\n')

for message in messages:
		for i in xrange(len(message)):
			letter = message[i]
			i_string = str(i+1)
			occurence = occurence_dict[i_string].get(letter)
			if occurence:
					occurence_dict[i_string][letter] += 1
			else:
					occurence_dict[i_string][letter] = 1

correct_message_list = list('********')
for column in occurence_dict.iteritems():
	index = int(column[0]) - 1
	lowest_occurence = 1000000
	letter = "*"
	for letter_occurence in column[1].iteritems():
		occurence = letter_occurence[1]
		if occurence < lowest_occurence:
				lowest_occurence = occurence
				letter = letter_occurence[0]
	correct_message_list[index] = letter	

print "".join(correct_message_list)

messages_file.close()
