import md5

door_id = "abbhdwsy"
index = 0

hashed = md5.new(door_id).hexdigest()
password = list("********")

while "*" in password:
		next_id = door_id + str(index)
		hashed = md5.new(next_id).hexdigest()
		if hashed[:5] == "00000":
				position = (hashed[5])
				if  55 >= ord(position) >= 48:
						position = int(position)
						character = hashed[6]
						if password[position] == "*":	
								password[position] = character 
								print password
		index += 1
print "".join(password)
