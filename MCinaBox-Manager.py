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
# pip install py-cpuinfo
# pip install psutil

# Você precisa instalar Todos os Módulos Acima!

SYSTEM = system()
ARCHITECTURE = get_cpu_info()["bits"]
PROCESSADOR = get_cpu_info()["brand_raw"]
HARDWARE = get_cpu_info()["hardware_raw"]
MEMORY_RAM_TOTAL = virtual_memory().total
MEMORY_RAM_FREE = virtual_memory().available
FORMAT_RAM_TOTAL = str(MEMORY_RAM_TOTAL)
FORMAT_RAM_FREE = str(MEMORY_RAM_FREE)[0:3]

def Verificar_Internet (url ='http://www.google.com'):
    try:
        CONECT = requests.head(url)
        return True

    except requests.ConnectionError:
        return False
WI_FI = Verificar_Internet()

# Start The Manager

def Manager_Main ():
	print(colored("[===========[ Painel de Controle MCinaBox v1.5 ]===========]",'white',attrs=["bold"]))
	
	print(colored("\n[1] - Instalar MCinaBox",'green'))
	
	print(colored("\n[2] - Limpar Registros Logs",'green'))
	
	print(colored("\n[3] - Gerar Pastas do MCinaBox",'green'))
	
	print(colored("\n[4] - Deletar MCinaBox",'green'))
	
	print(colored("\n[5] - Sobre o Manager",'green'))
	
	print(colored("\n[6] - Meu Aparelho",'green'))
	
	print(colored("\n[7] - Otimizador de FPS (Em Teste)",'magenta'))
	
	print(colored("\n[8] - Desinstalar o Manager",'red'))
	
	print(colored("\n[9] - Fechar Gerenciador\n",'red',attrs=["bold"]))
	print(colored("[======================[ MatheusTGP© ]===================]",'white',attrs=["bold"]))

	select = int(input(colored("\nOpção: ","yellow",attrs=["bold"])))
	
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
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("Limpador de Registros (LOGS)",'white',attrs=["bold"]))
		delete_logs = input(colored("\nVocê deseja Excluir os Registros Logs [s/n]: ",'yellow',attrs=["bold"]))
		if delete_logs == "s":
			DIR_LOGS = r'/storage/emulated/0/MCinaBox/gamedir/logs'
			if os.path.exists(DIR_LOGS):
				sleep(1)
				print(colored("[ Start ] [ Delete-Logs ] : Deletando Registro de Logs...",'red'))
				
				shutil.rmtree(DIR_LOGS)
				
				sleep(1)
				print(colored("[ Start ] [ Delete-Logs ] : Registros deletados.",'green',attrs=["bold"]))
				print(colored("[=======================================]",'white',attrs=["bold"]))
				
				sleep(2)
				os.system('clear')
				Manager_Main()
			else:
				print(colored("\nNão a Registros de Logs!",'red',attrs=["bold"]))
				print(colored("[=======================================]",'white',attrs=["bold"]))
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
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("Gerador de Pastas do MCinaBox",'white',attrs=["bold","underline"]))
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
				print(colored("[=======================================]",'white',attrs=["bold"]))
				sleep(2)
				os.system('clear')
				Manager_Main()
		else:
			print("O Usuário cancelou a operação, retornando!")
			sleep(1)
			os.system('clear')
			Manager_Main()
	elif select == 4:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("Exclusão do MCinaBox Diretório",'white',attrs=["bold"]))
		delete_mcinabox = input("\nVocê realmente quer deletar o diretório MCinaBox [s/n]: ")
		if delete_mcinabox == "s":
			print(colored("Procurando Diretório...","yellow"))
			MCinaBox_dirfull = r'/storage/emulated/0/MCinaBox'
			sleep(1)
			print(colored("Excluindo Pasta do MCinaBox...","red"))
			
			shutil.rmtree(MCinaBox_dirfull)
			
			sleep(1)
			print(colored("\nPasta do MCinaBox Excluída!","red",attrs=["bold"]))
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(2)
			os.system('clear')
			Manager_Main()

		elif delete_mcinabox == "n":
			print("Cancelado, Obrigado pelo escolha! \n")
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(1)
			os.system('clear')
			Manager_Main()
			
	elif select == 5:
		sleep(1)
		print("[=============================]")
		print(colored("Sobre o MCinaBox Manager","white",attrs=["bold"]))
		
		print(colored("\nMCinaBox Manager foi Construido na intenção de ajudar a deixar o lançador mais rápido é deixa-lo mais organizado, o código fará com que exclua e adicione Items e pastas para deixar o MCinaBox mais ágil, em breve será adicionado mais Funções, acessando nosso Site na GitHub você pode mencionar um Bug ou até mesmo instalar as versões mais Recentes do Código!","white"))
		
		print(colored("\nDesenvolvedor: MatheusTGamerPro ",'green'))
		print(colored("Versão: V1.0-Beta\n",'white'))
		
		print(colored("[=======================================]",'white',attrs=["bold"]))
		
		back = input("Para Voltar digite 'voltar': ")
		if back == "voltar":
			os.system('clear')
			Manager_Main()
		else:
			print("o Usuário Optou para Cancelar")
		print(colored("[=======================================]",'white',attrs=["bold"]))

	elif select == 6:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		print(colored("\nCarregando Informações do dispositivo...",'white',attrs=["bold"]))
		sleep(1)
		info = [SYSTEM, ARCHITECTURE, PROCESSADOR, HARDWARE , FORMAT_RAM_TOTAL, FORMAT_RAM_FREE]
		
		print(colored(f'''\nSistema: {info[0]}-Android

Bits da Arquitetura: {info[1]}-Bits

Processador: {info[2]}

Hardware da CPU: {info[3]}

Memória RAM Total: {info[4][0:1]}GB

Memória RAM Livre: {info[5][0:1]}.{info[5][0:2]}GB\n''','white'))
		print(colored("[=======================================]",'white',attrs=["bold"]))
		back = input(colored("Para voltar ao menu digite 'voltar': ",'yellow',attrs=["bold"]))
		if back == "voltar":
			os.system('clear')
			Manager_Main()
		else:
			print("o Usuário Optou para Cancelar")
			sleep(2)
			os.system('clear')
			Manager_Main()

		print(colored("[=======================================]",'white',attrs=["bold"]))
		
	elif select == 7:
		print("Coletando dados do FPS Boost...")
		sleep(1)
		print(colored("Desculpe! está função ainda não foi implementada aguarde até os próximos Update.",'red',attrs=["bold"]))
		sleep(2)
		os.system('clear')
		Manager_Main()
		
	elif select == 8:
		print(colored("[=======================================]",'white',attrs=["bold"]))
		
		print(colored("Carregando Setup Desinstalador do Manager",'white',attrs=["bold","underline"]))
		sleep(2)
		directory_manager = r'/storage/emulated/0/MCinaBox_Manager'
		uninstall_confirm = input(colored("Você deseja Desinstalar o Gerenciador? [s/n]: ",'yellow',attrs=["bold"]))
		
		if uninstall_confirm == "s":
			print(colored("\n[ Startup ] [ Manager-Uninstall ] : Fazendo a Desinstalação...",'red',attrs=["bold"]))
			sleep(2)
			
			shutil.rmtree(directory_manager)
			
			print(colored("\n[ Startup ] [ Manager-Uninstall ] : Desinstalação Completada",'green',attrs=["bold"]))
			sleep(1)
			print(colored("\nAté a Próxima, Voltando ao Lobby...",'green',attrs=["bold"]))
			print(colored("[=======================================]",'white',attrs=["bold"]))
			sleep(2)
			os.system('clear')
			Setup()
		elif uninstall_confirm == "n":
			print(colored("\nObrigado pela Escolha! Retornando...",'green',attrs=["bold"]))
			sleep(2)
			os.system('clear')
			Manager_Main()		
		
	elif select == 9:
		exit("Gerenciador Fechado, até a Próxima!")
		
	elif select > 9:
		print(colored("Está Opção não existe\n",'red',attrs=["bold"]))
		sleep(1)
		os.system('clear')
		Manager_Main()
sleep(1)
print(colored("[ MCinaBox Manager - V1.5 ]\n",'white',attrs=["bold","underline"]))

def Setup ():
	directory_manager = r'/storage/emulated/0/MCinaBox_Manager'
	
	directory_optfine = r'/storage/emulated/0/MCinaBox_Manager/OptFines'

	directory_installedMC = r'/storage/emulated/0/MCinaBox_Manager/MCinaBox_Installed'

	if os.path.exists(directory_manager):
		Manager_Main()
	else:
		sleep(1)
		print(colored("Seja Bem Vindo ao MCinaBox Manager! \nCriador: MatheusTGamerPro\n","magenta",attrs=["bold"]))
		print(colored("[=======================================]",'white',attrs=["bold"]))
		setup_config = input(colored("Você deseja instalar o MCinaBox Manager? [s/n]: ",'yellow',attrs=["bold"]))
		if setup_config == "s":
			print(colored("[=======================================]",'white',attrs=["bold"]))
			print(colored("\nAguarde, Fazendo a instalação do Gerenciador...",'green',attrs=["bold","underline"]))
			sleep(1)
			print(colored("\n[ 80% ] [ █████▒▒ ] : Gerando diretório primário...",'green',attrs=["bold"]))
			
			create_dir1 = makedirs(directory_manager)
			
			sleep(1)
			print(colored("\n [ 93% ][ ██████▒ ] : Gerando Diretório do OptFine...",'green',attrs=["bold"]))
			
			create_dir2 = makedirs(directory_optfine)
			create_dir3 = makedirs(directory_installedMC)
			
			sleep(2)
			print(colored("\n  [ 100%] [ ███████ ] : Instalação Finalizada.",'green',attrs=["bold"]))
			print(colored("\nGerenciador foi instalado com sucesso!",'yellow',attrs=["bold"]))
			print(colored("[=======================================]",'white',attrs=["bold"]))
			confirm_startup = input(colored("Deseja abrir o Menu? [s/n]: ",'yellow',attrs=["bold"]))
			if confirm_startup == "s":
				os.system('clear')
				Manager_Main()
			elif confirm_startup == "n":
				print("Okay, Quando desejar entrar, somente inicie o Código!")
			
		else:
			print(colored('Setup Instalador não finalizado.','red',attrs=["bold"]))
			exit()

		print(colored("MCinaBox Manager Instalado!",'green',attrs=["bold"])) # Corrigir erro do Bold
		sleep(2)
		os.system('clear')
		Manager_Main()		

Setup()
