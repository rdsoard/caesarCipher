#################################
## Rebekah Soard Ceasar Cipher
#################################
import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cont = True

while(cont == True):

	eOrD = input("enter \"encrypt\" if you would like to encrypt text or \"decrypt\" if you would like to decrypt text: ").strip()
	if(eOrD.lower() == "encrypt"):
		##do encrypt
		encryptText = input("enter text to encrypt: ").strip()
		print("\n			",encryptText.upper(),"		\n")
		lKey = input("would you like to use a letter key (i.e. \"A = T\")? (y/n): ").strip()
		if(lKey.lower() == "y"):
			lKey == input("enter key in the format of \"A=X\", \"E=T\" etc: ").strip()
		else:
			rand = 0
			print("shifting letters over by randomly generated times: ",rand)
			print("result")

	elif(eOrD.lower == "decrypt"):
		##do decrypt
		print()
