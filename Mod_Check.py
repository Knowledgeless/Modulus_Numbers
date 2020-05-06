'''
Let's check the mod values of a number.

'''

try:
	def modValue():
		while(True):
			count = 0
			j = 0
			print('''\n
				1. Check a number has 1 to 9 mod value or not?
				2. Find multimple numbers form a given range.
				3. Exit

			''')
			puser = int(input("Choose an option: "))
			if puser == 1:
				user = int(input("Enter your value: "))
				for j in range(2,11):
					if user%j == float(j-1):
						count = count+1
				if count == 9:
					print("\n\t[+] Yes, It has mod values from 1 to 9\n")
				else:
					print("\n\t[-] Sorry, it's not that number you are looking for.")
				count = 0

			elif puser == 2:
				user = int(input("Enter your value: "))
				print("\n")
				for i in range(2, user+1):
					for j in range(2,11):
						if i%j == float(j-1):
							count = count+1
					if count == 9:
						print(i, end=" ")
					count = 0

			elif puser == 3:
				break

			else:
				print("Wrong Input.")

	if __name__ == "__main__":
		modValue()

except ValueError:
	print("ValueError! Enter A Number.")
except KeyboardInterrupt:
	print("\nExiting The Process! Good Bye.")
