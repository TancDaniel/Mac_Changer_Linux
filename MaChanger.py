import subprocess
import random
import re

if __name__ == "__main__":

	try:

		manual_or_random_mac = input("Do you want to change it manually? y/n (no means random MAC):")

		if manual_or_random_mac == 'n':

			interface_input = input('Choose the interface: ')

			def Random_Mac():

				random_string = "abcdef123456789" 

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

			ifconfig_result = subprocess.check_output(["ifconfig", interface_input]).decode('utf-8')

			print("\n" + '[+] Changing MAC address for ' + interface_input+ ' to ' + "\033[92m" + MaChanger_X + "\033[0m" + "\n")

			print(ifconfig_result)

			mac_address_interface = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

			verify_step_mac_address = mac_address_interface.group(0)

			if verify_step_mac_address == MaChanger_X:
				print("\033[92m" + "[+] MAC address changed with success!" + "\033[0m")
			else:
				print("\033[91m" + "[+] MAC address could not be changed!" + "\033[0m")

		else:

			interface_input = input('Choose the interface: ')

			Input_MAC = input('New MAC address: ')

			subprocess.call("sudo ifconfig " + interface_input + " down", shell=True)

			subprocess.call("sudo ifconfig " + interface_input + " hw ether " + Input_MAC ,shell=True)

			subprocess.call("sudo ifconfig " + interface_input + " up", shell=True)

			ifconfig_result = subprocess.check_output(["ifconfig", interface_input]).decode('utf-8') # print the cmmands "ifconfig" in to the cmd

			print("\n" + '[+] Changing MAC address for ' + interface_input + ' to ' + "\033[92m" + Input_MAC + "\033[0m" + "\n")

			print(ifconfig_result)

			mac_address_interface = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

			verify_step_mac_address = mac_address_interface.group(0)

			if verify_step_mac_address == Input_MAC:
				print("\033[92m" + "[+] MAC address changed with success!" + "\033[0m")
			else:
				print("\033[91m" + "[+] MAC address could not be changed!" + "\033[0m")

	except Exception as e: print(e)


# Input: str = ???01-23-45-67-89-AB???; 
# Output: true 
# Explanation: 
# The given string satisfies all the above mentioned conditions. Therefore, it is a valid MAC address.

# Input: str = ???01-23-45-67-89-AH???; 
# Output: false 
# Explanation: 
# The given string contains ???H???, the valid hexadecimal digits should be followed by letter from a-f, A-F, and 0-9. Therefore, it is not a valid MAC address.

# Input: str = ???01-23-45-67-AH???; 
# Output: false 
# Explanation: 
# The given string has five groups of two hexadecimal digits. Therefore, it is not a valid MAC address. 

# subprocess.call("ip addr show $(awk 'NR==3{print $1}' /proc/net/wireless | tr -d :) | awk '/ether/{print $2}'", shell=True)