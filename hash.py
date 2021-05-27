import hashlib


def convert_texttext_to_sha1(text):
	digest = hashlib.sha1(
	text.encode()
	).hexdigest
	
	return digest


def main():
	user_sha1   = input   (" Enter the sha1 to crack: ")
	cleaned_user_sha1 = user_sha1.strip().lower()
	
	with open( " requirements.txt","r" ) as f:
		for line in f:
			password = line.strip()
			converted_sha1= convert_text_to_sha1(
			password)
			
			if cleaned_user_sha1 == converted_sha1:
				print (f"password found : {password }")
				return
				
	print("could not find the password ")
				
	

if __name__ == "__main__":
	pass
