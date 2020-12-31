# yo wassup
# decryptor.py


def binlist(prm_bin):
	if type(prm_bin)!=str:
		message = "Argument should be a string. Given : {}.".format(type(prm_bin))
		raise TypeError(message)
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
	given_bin = given_bin.replace(" ", "")
	binarray = binlist(given_bin)
	for Byte in binarray:
		character = chr(int(Byte, 2))#chr()
		txtlist.append(character)
		del character
	decrypted_bin = ''.join(txtlist)
	del txtlist
	return decrypted_bin

def txt2bin(string):
	if type(string)!=str:
		raise TypeError("Argument should be a string. Given : {}.".format(type(string)))
	from binascii import hexlify
	string = string.replace(" ", "")
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

def bin2hex(user_bin, py_syntax=False):
	return txt2hex(bin2txt(bin_code), py_syntax=py_syntax)
def hex2bin(user_hex):
	return txt2bin(hex2txt(user_hex))
