import hashlib, bcrypt



print('\033[94m' "              ░█████╗░██████╗░░█████╗░░█████╗░█╗░░██╗")
print('\033[94m' "              ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝")
print('\033[91m' "              ██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░")
print('\033[91m' "              ██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░")
print('\033[95m' "              ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗")
print('\033[95m' "              ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝")
print("")
print("")
print('\033[95m'  "     too create by,    ")
print('\033[95m'  "            ◻ risala ")
print('\033[95m' "             ◻ PAPPU   ")
print('\033[95m' "   powerd by cyber exploit unkown")
print("")
print("")
print("")
password = input("Enter password to hash\n ⇒ ")
print("\n==[::::::::> SHA1:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
print("\n==[:::::::::> MD5:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.md5(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
print("\n==[:::::::::> BCRYPT:\n")
for i in range(3):
    hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))
