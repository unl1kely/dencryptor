# yo wassup
# decryptor.py


def binlist(prm_bin):
	if type(prm_bin)!=str:
		raise TypeError("Argument should be a string. Given : {}.".format(type(prm_bin)))
	binlist = [ ]
	a = 0
	z = 8
	ln=len(prm_bin)
	Bytes = int(ln / 8)
	del ln
	for x in range(Bytes):
		Byte = prm_bin[a:z]
		binlist.append(Byte)
		del Byte
		a += 8
		z += 8
	del prm_bin
	del a
	del z
	del Bytes
	return binlist

def bin2txt(given_bin):
	if type(given_bin)!=str:
		raise TypeError("Argument should be a string. Given : {}.".format(type(given_bin)))
	txtlist = [ ]
	binarray = binlist(given_bin)
	for Byte in binarray:
		character = chr(int(Byte, 2))#chr()
		txtlist.append(character)
		del character
	decrypted_bin = ''.join(txtlist)
	del txtlist
	#print('Code decrypted successfully :\n\t', end="")
	return decrypted_bin

def txt2bin(string):
	if type(string)!=str:
		raise TypeError("Argument should be a string. Given : {}.".format(type(string)))
	from binascii import hexlify
	result = bin(int(hexlify(string.encode()), 16))
	result = '0' + result[2:]
	return result

def hex2txt(given_hex):
	if type(given_hex)!=str:
		raise TypeError("Given Hexcode should be stored in a string !")
	from binascii import unhexlify
	# stringed hex > byted hex > byted str > str
	byted_hex = given_hex.encode()
	byted_str = unhexlify(byted_hex)
	string = str(byted_str, 'ascii')
	
	return string

def txt2hex(string, py_syntax=False):
	if type(string)!=str:
		raise TypeError("Argument should be a string. Given : {}.".format(type(string)))
	from binascii import hexlify
	# str > byted str >byted hex > stringedhex
	byted_str = string.encode()
	byted_hex = hexlify(byted_str)
	stringed_hex = str(byted_hex, 'ascii')
	if py_syntax == True:
		hex_list = []
		i=0
		for x in range(0, int(len(stringed_hex)/2)):
			hex_list.append("\\x" + stringed_hex[i:i+2])
			i+=2
		stringed_hex = "".join(hex_list)
	return stringed_hex
#	x=binascii.hexlify(x) # byted str to byted hex
#	y=str(x,'ascii') # byted hex to stringed hex
#	x=binascii.unhexlify(x) # byted hex to byted str
#	y=str(x,'ascii') # byted str to str

if __name__=="__main__":
	choice = int(input("What do you want to do ?\n\n1. Decrypt binary to text\n2. Encrypt text to binary\n3. Decrypt hex to text\n4. Encrypt text to hex\n> "))
	if choice==1:
		user_input = input("Running bin to text decryptor \nEnter your binary code :\n> ")
		if user_input:
			print(bin2txt(user_input))
	elif choice==2:
		user_input = input("Running text to bin encryptor \nEnter your text :\n> ")
		if user_input:
			print(txt2bin(user_input))
	elif choice==3:
		user_input = input("Running hex to text decryptor. \nEnter your hexadecimal(hex) code :\n> ")
		if user_input:
			print(hex2txt(user_input))
	elif choice==4:
		user_input = input("Running text to hex decryptor. \nEnter your text :\n> ")
		if user_input:
			print(txt2hex(user_input))
	input("Press Enter to exit...")