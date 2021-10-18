# Creator =  MatheusTGamerPro ©
# GitHub = github.com/MatheusTGamerPro
# Version = 1.0_Beta
# Release = 16/10/2021 - Beta
# NOT remove the Crédits

import os
from os import makedirs
import shutil
from wget import download
from termcolor import colored
from time import sleep
from cpuinfo import get_cpu_info
from psutil import virtual_memory
from platform import system
import requests

# Módulos de instalação:
# Abra o Terminal e digite um por vez:
			
# pip install wget
# pip install termcolor
# pip install cpuinfo
# pip install psutil

# Você precisa instalar Todos os Módulos Acima!


# Info System Configuration...
SYSTEM = system()
ARCHITECTURE = get_cpu_info()["bits"]
PROCESSADOR = get_cpu_info()["hardware_raw"]
MEMORY_RAM = virtual_memory().total
FORMAT_RAM = str(MEMORY_RAM)
# Verify System Architecture for the MCinaBox

def Verificar_Internet (url ='http://www.google.com'):
    try:
        CONECT = requests.head(url)
        return True

    except requests.ConnectionError:
        return False
WI_FI = Verificar_Internet()

def Manager_Main ():
	print(colored("[===========[ MCinaBox_Manager 1.0-Alpha ]===========]",'white',attrs=["bold"]))
	
	print(colored("\n[1] - Instalar MCinaBox",'green'))
	
	print(colored("\n[2] - Limpar Registros Logs",'green'))
	
	print(colored("\n[3] - Gerar Pastas do MCinaBox",'green'))
	
	print(colored("\n[4] - Deletar MCinaBox (Beta)",'green'))
	
	print(colored("\n[5] - Sobre o Manager",'green'))
	
	print(colored("\n[6] - Meu Aparelho",'green'))
	
	print(colored("\n[7] - Otimizador de FPS (Em Teste)",'yellow'))
	
	print(colored("\n[8] - Fechar Gerenciador\n",'red',attrs=["bold"]))
	print(colored("[==================[ MatheusTGP© ]=================]",'white',attrs=["bold"]))

	select = int(input(colored("\nOpção: ","white",attrs=["bold"])))
	
	if select == 1:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		sleep(1)
		print(colored("Instalador do MCinaBox Para Android",'white',attrs=["bold","underline"]))
		sleep(1)
		print(colored("\n Você está prestes a Instalar o MCinaBox Minecraft Java no seu Dispositivo, junto contem o pacote do APK+Runtime,não se preocupe o próprio código identifica sua arquitetura!",'cyan',attrs=["bold"]))
		sleep(1)
		confirm_install = input("\nVocê Deseja Instalar o APK + Runtime do MCinaBox? [s/n]: ")
		if confirm_install == "s":
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(1)
			print(colored("Verificando Arquitetura do Sistema...",'white',attrs=["bold","underline"]))
			sleep(1)
			if ARCHITECTURE == 32:
				sleep(1)
				print(colored(f"\nArquitetura Detectada: {ARCHITECTURE}-Bits",'yellow',attrs=["bold"]))
				sleep(1)
				
				APK = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p5/MCinaBox.v0.1.4-p5.apk'
				
				RUNTIME_32 = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p2/aarch32-20200928.tar.xz'
				
				locate = '/storage/emulated/0/MCinaBox_Manager/MCinaBox_Installed'
				
				print(colored("\n[ Start ] [Info-Installer_x32 ] : Baixando APK do MCinaBox: ",'magenta',attrs=["bold"]))
				
				if WI_FI == True:
					download(APK,locate)
				
					sleep(1)
					print(colored(f"\n[ Start ] [Info-Installer_x32 ] : Baixando Java o Runtime: {ARCHITECTURE}-Bits: ",'magenta',attrs=["bold"]))
				
					download(RUNTIME_32,locate)
				
					print(colored("\n[ Finish ] [ Info-Installer_x32 ] : Download do MCinaBox Finalizado.",'green'))
					print(colored("[=======================================]",'white',attrs=["bold"]))
					sleep(2)
					os.system('clear')
					Manager_Main()
				elif WI_FI == False:
					print(colored("\nErro: Você não está conectado a internet, retornando...",'red',attrs=["bold"]))
					sleep(5)
					os.system('clear')
					Manager_Main()

			elif ARCHITECTURE == 64:
					print(colored(f"Arquitetura Detectada: {ARCHITECTURE}-Bits",'yellow'))
					sleep(1)
					
					APK = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p5/MCinaBox.v0.1.4-p5.apk'
					
					RUNTIME_64 = 'https://github.com/AOF-Dev/MCinaBox/releases/download/v0.1.4-p2/aarch64-20200927.tar.xz'
					
					locate = '/storage/emulated/0/MCinaBox_Manager/MCinaBox_Installed'
					print(colored("\n[ Start ] [ Info-Installer_x64 ] : Baixando APK do MCinaBox: ",'white',attrs=["bold"]))
					if WI_FI == True:
						download(APK,locate)
					
						sleep(1)
						print(colored(f"[ Start ] [ Info-Installer_x64] : Baixando o Java Runtime {ARCHITECTURE}-Bits: ",'magenta',attrs=["bold"]))
						download(RUNTIME_64,locate)
						sleep(1)
						print(colored(f"\n[ Start ] [ Info-Installer-Finish] : MCinaBox Baixado com Sucesso! ",'magenta',attrs=["bold"]))
					elif WI_FI == False:
						print(colored("\nErro: Você não está conectado a internet, retornando...",'red',attrs=["bold"]))
						sleep(5)
						os.system('clear')
						Manager_Main()
					print(colored("[=======================================]",'white',attrs=["bold"]))
					sleep(2)
					os.system('clear')
					Manager_Main()
		elif confirm_install == "n":
			print("Instalação Cancelada, Retornando...")
			sleep(1)
			os.system('clear')
			Manager_Main()

	elif select == 2:
		print("[=============================]")
		print(colored("Limpador de Registros (LOGS)",'white',attrs=["bold"]))
		delete_logs = input(colored("\nVocê deseja Excluir os Registros Logs [s/n]: ",'white',attrs=["bold"]))
		if delete_logs == "s":
			DIR_LOGS = r'/storage/emulated/0/MCinaBox/gamedir/logs'
			if os.path.exists(DIR_LOGS):
				sleep(1)
				print(colored("Deletando Registro de Logs...",'red'))
				
				shutil.rmtree(DIR_LOGS)
				
				sleep(1)
				print(colored("Logs Deletado com Sucesso!",'green',attrs=["bold"]))
				print("[=============================]")
				sleep(2)
				os.system('clear')
				Manager_Main()
			else:
				print(colored("Não a Registros de Logs!",'red',attrs=["bold"]))
				sleep(2)
				os.system('clear')
				Manager_Main()
		else:
				print("o Usuário Cancelou a operação!")
				sleep(1)
				os.system('clear')
				Manager_Main()
				
				sleep(1)
				print(colored("Os Registros foram Deletados!",'green',attrs=["bold"]))
		
		
	elif select == 3:
		print("[=============================]")
		print(colored("Construir Pastas do MCinaBox",'white',attrs=["bold"]))
		directory_mcinabox = r'/storage/emulated/0/MCinaBox/gamedir'
		confirmar = input("Deseja Gerar a Pasta 'MCinaBox/gamedir'[s/n]: ")
		if confirmar == "s":
			print(colored("Gerando Diretório...",'yellow',attrs=["bold"]))
			sleep(1)
			try:
				makedirs(directory_mcinabox)
				sleep(1)
				print(colored("Diretório Criado com Sucesso!",'green',attrs=["bold"]))
			except FileExistsError:
				print(colored("O Diretório do MCinaBox já existe!",'red',attrs=["bold"]))
				sleep(2)
				os.system('clear')
				Manager_Main()
		else:
			print("O Usuário cancelou a operação, retornando!")
			sleep(1)
			os.system('clear')
			Manager_Main()
	elif select == 4:
		print("[=============================]")
		print(colored("Exclusão do MCinaBox Diretório",'white',attrs=["bold"]))
		delete_mcinabox = input("\nVocê realmente quer deletar o diretório MCinaBox [s/n]: ")
		if delete_mcinabox == "s":
			print(colored("Procurando Diretório...","yellow"))
			MCinaBox_dirfull = r'/storage/emulated/0/MCinaBox'
			sleep(1)
			print(colored("Excluindo Pasta do MCinaBox...","red"))
			
			shutil.rmtree(MCinaBox_dirfull)
			
			sleep(1)
			print(colored("Pasta do MCinaBox Excluída!","red",attrs=["bold"]))
			sleep(2)
			os.system('clear')
			Manager_Main()

		elif delete_mcinabox == "n":
			print("Cancelado, Obrigado pelo escolha! \n")
			sleep(1)
			os.system('clear')
			Manager_Main()
			
	elif select == 5:
		sleep(1)
		print("[=============================]")
		print(colored("Sobre o MCinaBox Manager","white",attrs=["bold"]))
		
		print(colored("\nMCinaBox Manager foi feito na intenção de ajudar a deixar o lançador mais rápido é deixa-lo mais organizado, o código fará com que exclua e adicione Items e pastas para deixar o MCinaBox mais ágil, em breve será adicionado mais Funções, acessando nosso Site na GitHub você pode mencionar um Bug ou até mesmo instalar as versões mais Recentes do Código!","white"))
		
		print(colored("\nDesenvolvedor: MatheusTGamerPro ",'green'))
		print(colored("Versão: V1.0-Beta\n",'white'))
		back = input("Para Voltar digite 'voltar': ")
		if back == "voltar":
			os.system('clear')
			Manager_Main()
		else:
			print("o Usuário Optou para Cancelar")
		print("[=============================]")

	elif select == 6:
		print("[=============================]")
		print(colored("\nVerificando seu Dispositivo...",'white',attrs=["bold"]))
		sleep(1)
		info = [SYSTEM, ARCHITECTURE, PROCESSADOR, FORMAT_RAM]
		
		print(f'''\nSistema: {info[0]}
Bits da Arquitetura: {info[1]}-Bits
Processador: {info[2]}
Memória RAM: {FORMAT_RAM[0:1]}GB\n''')
		print("[=============================]")
		back = input(colored("Para voltar ao menu digite 'voltar': ",'white'))
		if back == "voltar":
			os.system('clear')
			Manager_Main()
		else:
			print("o Usuário Optou para Cancelar")
			sleep(2)
			os.system('clear')
			Manager_Main()

		print("[=============================]")
		
	elif select == 7:
		print("Verificando...")
		sleep(1)
		print(colored("Desculpe! está função ainda não foi implementada aguarde até o próximo Update.",'red',attrs=["bold"]))
		sleep(2)
		os.system('clear')
		Manager_Main()
		
	elif select == 8:
		exit("Gerenciador Fechado")
	elif select > 8:
		print(colored("Está Opção não existe\n",'red',attrs=["bold"]))
		sleep(1)
		os.system('clear')
		Manager_Main()
sleep(1)
print(colored("Gerenciador do MCinaBox Versão Beta, Carregando informações...\n",'blue'))

def Setup ():
	directory_manager = r'/storage/emulated/0/MCinaBox_Manager'
	
	directory_optfine = r'/storage/emulated/0/MCinaBox_Manager/OptFines'

	directory_installedMC = r'/storage/emulated/0/MCinaBox_Manager/MCinaBox_Installed'

	if os.path.exists(directory_manager):
		Manager_Main()
	else:
		sleep(1)
		print(colored("Seja Bem Vindo ao MCinaBox Manager! \nCriador: MatheusTGamerPro\n","white"))
		setup_config = input(colored("Você deseja instalar o MCinaBox Manager? [s/n]: ",'white',attrs=["bold"]))
		if setup_config == "s":
			print(colored("Criando Diretório...",'green'))
			sleep(1)
			print(colored("80% █████▒▒ Directory Create1",'green',attrs=["bold"]))
			
			create_dir1 = makedirs(directory_manager)
			
			sleep(1)
			print(colored("90% ██████▒ Directory Create 2",'green',attrs=["bold"]))
			
			create_dir2 = makedirs(directory_optfine)
			create_dir3 = makedirs(directory_installedMC)
			
			sleep(1)
			print(colored("100% ███████ Finish",'green',attrs=["bold"]))
			print(colored("Manager Instalado com Sucesso, Abrindo Menu...",'yellow',attrs=["bold"]))
			sleep(3)
			os.system('clear')
			Manager_Main()
			
		else:
			print(colored('Setup Cancelado','red'))

		print(colored("MCinaBox Manager Instalado!",'green',attrs=["bold"]))
		sleep(2)
		os.system('clear')
		Manager_Main()		

Setup()
