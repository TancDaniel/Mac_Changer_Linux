import subprocess
import optparse
import random

if __name__ == "__main__":

	parser = optparse.OptionParser(description= 'Change MAC address') # Handle user inputs

	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address") # -i or --interface is the argument and dest is the variable and help is for the help message

	parser.add_option("-r", "--random", action="store_false", help="Random MAC addres") # random == False if you dont give 'dest' the variable will be --random but without --

	parser.add_option("-m", "--manually", dest="manually_mac", help="New MAC address") # manually_mac = None or the user input 

	(options, arguments) = parser.parse_args() # Take the inputs (variables) options ---the user input | and arguments --- the commands

	try:


		if options.random is False:

			interface_input = options.interface

			def Random_Mac():

				random_string = "aAbBcCdDeEfF123456789" 

				rnd_list = []

				for x in range(10):

					rnd = random.choice(random_string)

					rnd_list.append(rnd)


				random_mac = f'00:{rnd_list[0]+rnd_list[1]}:{rnd_list[2]+rnd_list[3]}:{rnd_list[4]+rnd_list[5]}:{rnd_list[6]+rnd_list[7]}:{rnd_list[8]+rnd_list[9]}'
				

				return random_mac

			MaChanger_X = Random_Mac()

			subprocess.call("sudo ifconfig " + interface_input+ " down", shell=True)

			subprocess.call("sudo ifconfig " + interface_input + " hw ether " + MaChanger_X, shell=True)

			subprocess.call("sudo ifconfig " + interface_input + " up", shell=True)



			print('[+] Changing MAC address for ' + interface_input+ ' to ' + MaChanger_X)

		else:

			interface_input = options.interface

			subprocess.call("sudo ifconfig " + interface_input + " down", shell=True)

			subprocess.call("sudo ifconfig " + interface_input + " hw ether " + options.manually_mac ,shell=True)

			subprocess.call("sudo ifconfig " + interface_input + " up", shell=True)



			print('[+] Changing MAC address for ' + interface_input + ' to ' + options.manually_mac)


	except Exception as e: print(e)


# Input: str = “01-23-45-67-89-AB”; 
# Output: true 
# Explanation: 
# The given string satisfies all the above mentioned conditions. Therefore, it is a valid MAC address.

# Input: str = “01-23-45-67-89-AH”; 
# Output: false 
# Explanation: 
# The given string contains ‘H’, the valid hexadecimal digits should be followed by letter from a-f, A-F, and 0-9. Therefore, it is not a valid MAC address.

# Input: str = “01-23-45-67-AH”; 
# Output: false 
# Explanation: 
# The given string has five groups of two hexadecimal digits. Therefore, it is not a valid MAC address. 

# subprocess.call("ip addr show $(awk 'NR==3{print $1}' /proc/net/wireless | tr -d :) | awk '/ether/{print $2}'", shell=True)