# Creator =  MatheusTGamerPro ©
# GitHub = github.com/MatheusTGamerPro
# Version = 1.0_Beta
# Release = 16/10/2021 - Beta
# NOT remove the Crédits

import sys
import os
import shutil
from psutil import virtual_memory
from termcolor import colored
from wget import download
from os import system as console
from os import makedirs
from time import sleep
from cpuinfo import get_cpu_info
from platform import system
from requests import head

from MLauncherManager import MLauncherManager

SYSTEM = system()
ARCHITECTURE = get_cpu_info()["bits"]
MEMORY_RAM_TOTAL = virtual_memory().total
MEMORY_RAM_FREE = virtual_memory().available
FORMAT_RAM_TOTAL = str(MEMORY_RAM_TOTAL)
FORMAT_RAM_FREE = str(MEMORY_RAM_FREE)[0:3]

def Check_Connection(url ='http://www.google.com'):
    try:
        CONECT = head(url)
        return True

    except requests.ConnectionError:
        return False
    
WI_FI = Check_Connection()


def Manager_Main():
	print(colored("[===========[ MCinaBox v1.5 Control Panel ]===========]",'white',attrs=["bold"]))
	
	print(colored("\n[1] - Install MCinaBox",'green'))
	
	print(colored("\n[2] - Clean Logs",'green'))
	
	print(colored("\n[3] - Generate MCinaBox Folders",'green'))
	
	print(colored("\n[4] - Delete MCinaBox",'green'))
	
	print(colored("\n[5] - About MLauncher",'green'))
	
	print(colored("\n[6] - My Device",'green'))
	
	print(colored("\n[7] - FPS Optimizer (In Test)",'magenta'))
	
	print(colored("\n[8] - Uninstall Manager",'red'))
	
	print(colored("\n[9] - Close Manager\n",'red',attrs=["bold"]))
	print(colored("[======================[ MatheusTGP© ]===================]",'white',attrs=["bold"]))

	select = int(input(colored("\nOption: ","yellow",attrs=["bold"])))
	
	if select == 1:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		sleep(1)
		print(colored("MCinaBox Installer for Android",'white',attrs=["bold","underline"]))
		sleep(1)
		print(colored("\n You are about to Install MCinaBox Minecraft Java on your Device, together it contains the APK+Runtime package, don't worry the code itself identifies your architecture!",'cyan',attrs=["bold"]))
		sleep(1)
		confirm_install = input("\nDo you Want to Install MCinaBox APK + Runtime? [y/n]: ")
		if confirm_install == "y":
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(1)
			print(colored("Checking System Architecture...",'white',attrs=["bold","underline"]))
			sleep(1)
			if ARCHITECTURE == 32:
				sleep(1)
				print(colored(f"\nArchitecture Detected: {ARCHITECTURE}-Bits",'yellow',attrs=["bold"]))
				sleep(1)
				
				APK = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p5/MCinaBox.v0.1.4-p5.apk'
				
				RUNTIME_32 = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p2/aarch32-20200928.tar.xz'
				
				locate = '/storage/emulated/0/MCinaBox_Manager/MCinaBox_Installed'
				
				print(colored("\n[ Start ] [Info-Installer_x32 ] : Downloading APK from MCinaBox: ",'magenta',attrs=["bold"]))
				
				if WI_FI == True:
					download(APK,locate)
				
					sleep(1)
					print(colored(f"\n[ Start ] [Info-Installer_x32 ] : Downloading Java Runtime: {ARCHITECTURE}-Bits: ",'magenta',attrs=["bold"]))
				
					download(RUNTIME_32,locate)
				
					print(colored("\n[ Finish ] [ Info-Installer_x32 ] : MCinaBox Download Completed.",'green'))
					print(colored("[=======================================]",'white',attrs=["bold"]))
					sleep(2)
					console('clear')
					Manager_Main()
				elif WI_FI == False:
					print(colored("\nError: You are not connected to the internet, returning...",'red',attrs=["bold"]))
					sleep(5)
					console('clear')
					Manager_Main()

			elif ARCHITECTURE == 64:
					print(colored(f"Architecture Detected: {ARCHITECTURE}-Bits",'yellow'))
					sleep(1)
					
					APK = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p5/MCinaBox.v0.1.4-p5.apk'
					
					RUNTIME_64 = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p2/aarch64-20200927.tar.xz'
					
					locate = '/storage/emulated/0/MCinaBox_Manager/MCinaBox_Installed'
					print(colored("\n[ Start ] [ Info-Installer_x64 ] :Downloading APK from MCinaBox: ",'white',attrs=["bold"]))
					if WI_FI == True:
						download(APK,locate)
					
						sleep(1)
						print(colored(f"[ Start ] [ Info-Installer_x64] : Downloading Java Runtime {ARCHITECTURE}-Bits: ",'magenta',attrs=["bold"]))
						download(RUNTIME_64,locate)
						sleep(1)
						print(colored(f"\n[ Start ] [ Info-Installer-Finish] : MCinaBox Downloaded Successfully! ",'magenta',attrs=["bold"]))
					elif WI_FI == False:
						print(colored("\nError: You are not connected to the internet, returning...",'red',attrs=["bold"]))
						sleep(5)
						console("clear")
						Manager_Main()
					print(colored("[=======================================]",'white',attrs=["bold"]))
					sleep(2)
					console('clear')
					Manager_Main()
		elif confirm_install == "n":
			print("Installation Canceled, Returning...")
			sleep(1)
			console('clear')
			Manager_Main()

	elif select == 2:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("Record Excluder (Logs)",'white',attrs=["bold"]))
		delete_logs = input(colored("\nDo you want to Delete Records Logs [y/n]: ",'yellow',attrs=["bold"]))
		if delete_logs == "s":
			DIR_LOGS = r'/storage/emulated/0/MCinaBox/gamedir/logs'
			if os.path.exists(DIR_LOGS):
				sleep(1)
				print(colored("[ Start ] [ Delete-Logs ] : Deleting Log Records...",'red'))
				
				shutil.rmtree(DIR_LOGS)
				
				sleep(1)
				print(colored("[ Start ] [ Delete-Logs ] : Deleted records.",'green',attrs=["bold"]))
				print(colored("[=======================================]",'white',attrs=["bold"]))
				
				sleep(2)
			        console('clear')
				Manager_Main()
			else:
				print(colored("\nNo to Log Records!",'red',attrs=["bold"]))
				print(colored("[=======================================]",'white',attrs=["bold"]))
				sleep(2)
				console('clear')
				Manager_Main()
		else:
				print("User Canceled the operation!")
				sleep(1)
				console('clear')
				Manager_Main()
				
				sleep(1)
				print(colored("Records have been Deleted!",'green',attrs=["bold"]))
		
		
	elif select == 3:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("MCinaBox Folder Generator",'white',attrs=["bold","underline"]))
		directory_mcinabox = r'/storage/emulated/0/MCinaBox/gamedir'
		confirmar = input("Want to Generate Folder 'MCinaBox/gamedir'[y/n]:")
		if confirmar == "y":
			print(colored("Generating Directory...",'yellow',attrs=["bold"]))
			sleep(1)
			try:
				makedirs(directory_mcinabox)
				sleep(1)
				print(colored("Directory Created Successfully!",'green',attrs=["bold"]))
			except FileExistsError:
				print(colored("MCinaBox Directory already exists!",'red',attrs=["bold"]))
				print(colored("[=======================================]",'white',attrs=["bold"]))
				sleep(2)
				console('clear')
				Manager_Main()
		else:
			print("The User canceled the operation, returning!")
			sleep(1)
			console('clear')
			Manager_Main()
	elif select == 4:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("Deleting MCinaBox Directory",'white',attrs=["bold"]))
		delete_mcinabox = input("\nDo you really want to delete the MCinaBox directory [y/n]: ")
		if delete_mcinabox == "y":
			print(colored("Searching Directory...","yellow"))
			MCinaBox_dirfull = r'/storage/emulated/0/MCinaBox'
			sleep(1)
			print(colored("Deleting Folder from MCinaBox...","red"))
			
			shutil.rmtree(MCinaBox_dirfull)
			
			sleep(1)
			print(colored("\nMCinaBox Folder Deleted!","red",attrs=["bold"]))
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(2)
			console('clear')
			Manager_Main()

		elif delete_mcinabox == "n":
			print("Canceled, Thanks for choosing!\n")
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(1)
			console('clear')
			Manager_Main()
			
	elif select == 5:
		sleep(1)
		print("[=============================]")
		print(colored("About MCinaBox Manager","white",attrs=["bold"]))
		
		print(colored("\nMCinaBox Manager was Built with the intention of helping to make the launcher faster and to make it more organized, the code will make you delete and add Items and folders to make MCinaBox more agile, more Functions will be added soon, by accessing our Site at GitHub you can mention a Bug or even install the Latest Versions of the Code!","white"))
		
		print(colored("\nDeveloper: MatheusTGamerPro ",'green'))
		print(colored("Version: V1.5.1-Beta\n",'white'))
		
		print(colored("[=======================================]",'white',attrs=["bold"]))
		
		back = input("To go back type 'back':")
		if back == "back":
			console('clear')
			Manager_Main()
		else:
			print("User Chose to Cancel")
		print(colored("[=======================================]",'white',attrs=["bold"]))

	elif select == 6:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("\nLoading Device Information...",'white',attrs=["bold"]))
		sleep(1)
		info = [SYSTEM, ARCHITECTURE , FORMAT_RAM_TOTAL, FORMAT_RAM_FREE]
		
		print(colored(f'''\nSystem: {info[0]}-Android

Architecture Bits: {info[1]}-Bits

Total RAM Memory: {info[2][0:1]}GB

Free RAM Memory: {info[3][0:1]}.{info[3][0:2]}GB\n''','white'))
		print(colored("[=======================================]",'white',attrs=["bold"]))
		back = input(colored("To return to the menu type 'back': ",'yellow',attrs=["bold"]))
		if back == "back":
			console('clear')
			Manager_Main()
		else:
			print("User Chose to Cancel")
			sleep(2)
			console('clear')
			Manager_Main()

		print(colored("[=======================================]",'white',attrs=["bold"]))
		
	elif select == 7:
		print("Collecting FPS Boost data...")
		sleep(1)
		print(colored("Sorry! this function has not yet been implemented wait for the next update.",'red',attrs=["bold"]))
		sleep(2)
		console('clear')
		Manager_Main()
		
	elif select == 8:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		
		print(colored("Loading Setup Manager Uninstaller",'white',attrs=["bold","underline"]))
		sleep(2)
		directory_manager = r'/storage/emulated/0/MCinaBox_Manager'
		uninstall_confirm = input(colored("Do you want to Uninstall Manager? [y/n]: ",'yellow',attrs=["bold"]))
		
		if uninstall_confirm == "y":
			print(colored("\n[ Startup ] [ Manager-Uninstall ] : Uninstalling...",'red',attrs=["bold"]))
			sleep(2)
			
			shutil.rmtree(directory_manager)
			
			print(colored("\n[ Startup ] [ Manager-Uninstall ] : Uninstall Completed",'green',attrs=["bold"]))
			sleep(1)
			print(colored("\nSee you next time, Back to the Lobby...",'green',attrs=["bold"]))
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(2)
			console('clear')
			Setup()
		elif uninstall_confirm == "n":
			print(colored("\nThanks for choosing! Returning...",'green',attrs=["bold"]))
			sleep(2)
			console('clear')
			Manager_Main()		
		
	elif select == 9:
		exit("Manager Closed, See You Next!")
		
	elif select > 9:
		print(colored("This Option does not exist\n",'red',attrs=["bold"]))
		sleep(1)
		console('clear')
		Manager_Main()
sleep(1)
print(colored("[ MCinaBox Manager - V1.5.1-Beta]\n",'white',attrs=["bold","underline"]))

def Setup ():
                      
	directory_manager = r'/storage/emulated/0/MCinaBox_Manager'
	
	directory_optfine = r'/storage/emulated/0/MCinaBox_Manager/OptFines'

	directory_installedMC = r'/storage/emulated/0/MCinaBox_Manager/MCinaBox_Installed'

	directory_libraries = r'/storage/emulated/0/MCinaBox_Manager/libraries'

	if os.path.exists(directory_manager):
		Manager_Main()
	else:
		sleep(1)
		print(colored("Welcome to MCinaBox Manager! \nCreator: MatheusTGamerPro\n","magenta",attrs=["bold"]))
		print(colored("[=======================================]",'white',attrs=["bold"]))
		setup_config = input(colored("Do you want to install MCinaBox Manager? [y/n]:",'yellow',attrs=["bold"]))
		if setup_config == "y":
			print(colored("[=======================================]",'white',attrs=["bold"]))
			print(colored("\nWait, Installing the Manager...",'green',attrs=["bold","underline"]))
			sleep(1)
			print(colored("\n[ 46% ] [ █▒▒▒▒▒ ] : Generating primary directory....",'green',attrs=["bold"]))
			
			create_dir1 = makedirs(directory_manager)
			sleep(1)
			print(colored("\n [ 63% ][ ████▒▒▒ ] : Generating OptFine Directory....",'green',attrs=["bold"]))
			
			create_dir2 = makedirs(directory_optfine)
			sleep(2)
			print(colored("\n [ 84% ][ █████▒▒ ] : Generating File Directory..",'green',attrs=["bold"]))
			create_dir3 = makedirs(directory_installedMC)

			sleep(2)
			print(colored("\n [ 94% ][ ██████▒] : Creating Code Libraries....",'green',attrs=["bold"]))
			create_dir4 = makedirs(directory_libraries)
                                                
			sleep(2)
			print(colored("\n  [ 100%] [ ███████ ] : Installation Completed.",'green',attrs=["bold"]))
			print(colored("\nManager has been successfully installed!",'yellow',attrs=["bold"]))
			print(colored("[=======================================]",'white',attrs=["bold"]))
			open_menu = input(colored("Do you want to open the Menu? [y/n]: ",'yellow',attrs=["bold"]))
			if open_menu == "s":
				console('clear')
				Manager_Main()
			else:
			        print("Okay, When you want to login, just start the Code!")
			
		else:
			print(colored('Setup Installer not finished.','red',attrs=["bold"]))
			exit()

		print(colored("MCinaBox Manager Installed!",'green',attrs=["bold"]))
		sleep(2)
		console('clear')
		Manager_Main()
    
Setup()
