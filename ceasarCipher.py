#################################
## Rebekah Soard Ceasar Cipher
#################################

import random
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cont = True

while(cont == True):

	eOrD = input("enter \"encrypt\" if you would like to encrypt text or \"decrypt\" if you would like to decrypt text: ").strip()
	if(eOrD.lower() == "encrypt"):
		##do encrypt
		encryptText = input("enter text to encrypt: ").upper().strip()
		encryptOut = ""
		print("\n			",encryptText,"		\n")
		uShift = input("would you like to shift a specific amount? (y/n): ").strip()
		if(uShift.lower() == "y"):
			uShift = int(input("enter amount to shift by: ").strip())
			for x in encryptText:
				if (x in alphabet):
					if((alphabet.index(x)+uShift) > 25):
						nShift = (alphabet.index(x)+uShift)-26
						encryptOut = encryptOut + alphabet[nShift]
					else:
						nShift = alphabet.index(x)+uShift
						encryptOut = encryptOut + alphabet[nShift]
				else: 
					encryptOut = encryptOut + x
			print("\n			",encryptOut,"		\n")
		else:
			rand = random.randint(1,25)
			print("shifting letters over by randomly generated times: ",rand)
			for x in encryptText:
				if (x in alphabet):
					if((alphabet.index(x)+rand) > 25):
						rShift = (alphabet.index(x)+rand)-26
						encryptOut = encryptOut + alphabet[rShift]
					else:
						rShift = alphabet.index(x)+rand
						encryptOut = encryptOut + alphabet[rShift]
				else: 
					encryptOut = encryptOut + x
			print("\n			",encryptOut,"		\n")

	elif(eOrD.lower == "decrypt"):
		##do decrypt
		print()
