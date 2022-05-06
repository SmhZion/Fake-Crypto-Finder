import colorama
from colorama import init, Fore, Style, Back
import time
import random
import string
import ctypes
init()
init(autoreset=True)
init(convert=True)
def GenerateFalseToken(Length):
	Letters = string.ascii_lowercase
	TokenGenerated = "".join(random.choice(Letters) for i in range(Length))
	print(f"{Fore.LIGHTBLACK_EX}» {Fore.RED}BTC"+TokenGenerated+f" {Fore.LIGHTBLACK_EX}[{Fore.RED}$0{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.RED}0.00000000 BTC{Fore.LIGHTBLACK_EX}]")

def GenerateTrueToken(Length):
	Letters = string.ascii_lowercase
	TokenGenerated = "".join(random.choice(Letters) for i in range(Length))
	RandomNumberNonString = random.randint(500,1000)
	RandomNumber = str(RandomNumberNonString)
	RandomBitcoinNumberNonString = random.random()
	RandomBitcoinNumber = str(RandomBitcoinNumberNonString)
	print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}BTC"+TokenGenerated+f" {Fore.LIGHTBLACK_EX}[{Fore.GREEN}$"+RandomNumber+f"{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.GREEN}"+RandomBitcoinNumber+f" BTC{Fore.LIGHTBLACK_EX}]")

ctypes.windll.kernel32.SetConsoleTitleW(f"Crypto Finder | Version 1.0")
time.sleep(0.2)
print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Credits to SmhZion#6012")
time.sleep(0.2)
print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Which Crypto would you like to choose?")
time.sleep(0.2)
print(f"  {Fore.LIGHTBLACK_EX}• {Fore.YELLOW}Bitcoin {Fore.LIGHTBLACK_EX}[{Fore.YELLOW}BTC{Fore.LIGHTBLACK_EX}]")
time.sleep(0.2)
print(f"  {Fore.LIGHTBLACK_EX}• {Fore.YELLOW}Cardano {Fore.LIGHTBLACK_EX}[{Fore.YELLOW}ADA{Fore.LIGHTBLACK_EX}]")
time.sleep(0.2)
print(f"  {Fore.LIGHTBLACK_EX}• {Fore.YELLOW}Ethereum {Fore.LIGHTBLACK_EX}[{Fore.YELLOW}ETH{Fore.LIGHTBLACK_EX}]")
time.sleep(0.2)
print(f"  {Fore.LIGHTBLACK_EX}• {Fore.YELLOW}Litecoin {Fore.LIGHTBLACK_EX}[{Fore.YELLOW}LTC{Fore.LIGHTBLACK_EX}]")
time.sleep(0.2)

print(f"{Fore.LIGHTBLACK_EX}» {Fore.YELLOW}", end="")
CryptoOption = input().lower()
if CryptoOption == "bitcoin":
	time.sleep(0.2)
	print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Would you like to proceed with the Crypto Bitcoin/BTC? {Fore.LIGHTBLACK_EX}[{Fore.GREEN}Y{Fore.LIGHTBLACK_EX}/{Fore.RED}N{Fore.LIGHTBLACK_EX}]")
	time.sleep(0.2)
	print(f"{Fore.LIGHTBLACK_EX}» {Fore.YELLOW}", end="")
	YOrN = input().lower()
	if YOrN == "y":
		time.sleep(0.2)
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Starting to look for Accounts...")
		time.sleep(0.2)
		for i in range(500):
			time.sleep(0.01)
			GenerateFalseToken(60)
		GenerateTrueToken(60)
		time.sleep(0.2)
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Would you like to access this found account? {Fore.LIGHTBLACK_EX}[{Fore.GREEN}Y{Fore.LIGHTBLACK_EX}/{Fore.RED}N{Fore.LIGHTBLACK_EX}]")
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.YELLOW}", end="")
		YOrNAccount = input().lower()
		if YOrNAccount == "y":
			time.sleep(0.2)
			print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Uh oh! There has been an error while getting the account, please try again.")
			time.sleep(3)
		elif YOrNAccount == "n":
			time.sleep(0.2)
			print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Uh oh! That is not a valid option, please restart the Crypto Miner and try again!")
			time.sleep(3)
		else:
			time.sleep(0.2)
			print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Uh oh! That is not a valid option, please restart the Crypto Miner and try again!")
			time.sleep(3)
	elif YOrN == "n":
		time.sleep(0.2)
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Thank you for trying our Crypto Miner, if you'd like to continue please relaunch!")
		time.sleep(3)
elif CryptoOption == "btc":
	time.sleep(0.2)
	print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Would you like to proceed with the Crypto Bitcoin/BTC? {Fore.LIGHTBLACK_EX}[{Fore.GREEN}Y{Fore.LIGHTBLACK_EX}/{Fore.RED}N{Fore.LIGHTBLACK_EX}]")
	time.sleep(0.2)
	print(f"{Fore.LIGHTBLACK_EX}» {Fore.YELLOW}", end="")
	YOrN = input().lower()
	if YOrN == "y":
		time.sleep(0.2)
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Starting to look for Accounts...")
		time.sleep(0.2)
		for i in range(700):
			time.sleep(0.01)
			GenerateFalseToken(60)
		GenerateTrueToken(60)
		time.sleep(0.2)
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Would you like to access this found account? {Fore.LIGHTBLACK_EX}[{Fore.GREEN}Y{Fore.LIGHTBLACK_EX}/{Fore.RED}N{Fore.LIGHTBLACK_EX}]")
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.YELLOW}", end="")
		YOrNAccount = input().lower()
		if YOrNAccount == "y":
			time.sleep(0.2)
			print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Uh oh! There has been an error while getting the account, please try again.")
			time.sleep(3)
		elif YOrNAccount == "n":
			time.sleep(0.2)
			print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Uh oh! That is not a valid option, please restart the Crypto Miner and try again!")
			time.sleep(3)
		else:
			time.sleep(0.2)
			print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Uh oh! That is not a valid option, please restart the Crypto Miner and try again!")
			time.sleep(3)
	elif YOrN == "n":
		time.sleep(0.2)
		print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Thank you for trying our Crypto Miner, if you'd like to continue please relaunch!")
		time.sleep(3)
else:
	time.sleep(0.2)
	print(f"{Fore.LIGHTBLACK_EX}» {Fore.GREEN}Uh oh! Looks like this Crypto is not supported yet.")
	time.sleep(3)
