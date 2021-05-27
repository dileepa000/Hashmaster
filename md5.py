import hashlib

pass_hash  = input("enter md5 hash:")

wordlist = input("file name:")

try:
	pass_file = open(wordlist,"r")
except:
	print("no file found")
	quit( )
	
for word in pass_file:
	
	enc_wrd = word.encode(Utf-8)
	dihest = hashlib.md5(enc_wrd.strip()).hexdigest( )
	
	
	if digest == pass_hash:
		print("password found")
		print("password is " + word)
		flag = 1
		break 
		
		if flag == 0:
			print("password/passphrase is not in the list")
