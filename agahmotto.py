#!/usr/bin/python

# import ascii_art
import boto3, time, sys
from colorama import Fore
from ascii_art import image, banner
from menu_ajuda import menu_ajuda_pt, menu_ajuda_en
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def menu_idioma():
	while True:
		try:
			print(Fore.WHITE + "\n##################################################\n")
			print("Which language do you want to use in the program?\n\n1 - English\n2 - Português\n3 - Quit Program\n")
			print("##################################################\n")
			lang_choice = int(input("Pick your language: "))

			if lang_choice == 1:
				if a == "help":
					menu_ajuda_en()
					break
				else:
					ingles()
					break
			elif lang_choice == 2:
				if a == "help":
					menu_ajuda_pt()
					break
				else:
					portugues()
					break
			elif lang_choice == 3:
				sys.exit()
			else:
				print("\nInvalid choice. Make sure to take a language for the program.")
		except ValueError:
			print("\n\nInvalid choice. Make sure to take a language for the program.")

def awsinstanceenglish():
	while True:
		try:
			print(Fore.RED + "The Eye requests your access keys...\n")
			aws_access_key = input("Provide your Access Key: ")
			aws_secret_access_key = input("Now, provide your Secret Key: ")
			region_name = input("It also wants to know which region you are calling from: ")

			ec2_client = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)

			def action_instance(action, instance_ids):
				if action == "1":
					ec2_client.start_instances(InstanceIds=instance_ids)
				elif action == "2":
					ec2_client.stop_instances(InstanceIds=instance_ids)
				else:
					print("The Eye did not understand the request.")

			instance_id = input("\nVery well. Now, what are your target instances? Provide the IDs: ")
			eye_action = input("Finally, what is your wish? Start or stop the instance? 1 - Start / 2 - Stop: ")

			action_instance(action=eye_action, instance_ids=[instance_id])

			if eye_action == "1":
				print("\nExcellent! Now, wait 30 seconds and observe what the Eye was able to find...")
				time.sleep(30)

				response = ec2_client.describe_instances(InstanceIds=[instance_id])
				reservations = response['Reservations']
				instances = reservations[0]['Instances']
				instance = instances[0]
				ipv4 = instance.get('PublicIpAddress')

				if ipv4:
					print(f'\n[+] Here is the entry gate - https://{ipv4}/')
					break
				else:
					retry = input('Unfortunately, the Eye could not find what was provided. Would you like to try again? 1 - Yes / 2 - No: ')
					if retry == "2":
						break
			elif eye_action == "2":
				print("\nThe Eye bids you farewell... Now, your instance will be stopped.")
				break

		except NoCredentialsError:
			print('\nError: No credentials found.')
		except PartialCredentialsError:
			print('\nError: Incomplete credentials.')
		except Exception as e:
			print(f'\nUnexpected error: {e}')

def awsintanciaportugues():
	while True:
		try:
			print(Fore.RED + "O Olho deseja as suas chaves de acesso...\n")
			aws_access_key = input("Entregue-o a sua Access Key: ")
			aws_secret_access_key = input("Agora, a sua Secret Key: ")
			region_name = input("Ele também quer saber de qual região você o chama: ")

			ec2_client = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)

			def action_instance(action, instance_ids):
				if action == "1":
					ec2_client.start_instances(InstanceIds=instance_ids)
				elif action == "2":
					ec2_client.stop_instances(InstanceIds=instance_ids)
				else:
					print("O Olho não entendeu qual é o seu desejo.")

			instance_id = input("\nMuito bem. Agora, quais são as suas instâncias alvo? Informe-o os IDs: ")
			eye_action = input("Por fim, qual é o seu desejo? Ligar ou desligar a instância? 1 - Ligar / 2 - Desligar: ")

			action_instance(action=eye_action, instance_ids=[instance_id])

			if eye_action == "1":
				print("\nExcelente! Agora, aguarde 30 segundos e observe tudo o que Olho foi capaz de encontrar...")
				time.sleep(30)

				response = ec2_client.describe_instances(InstanceIds=[instance_id])
				reservations = response['Reservations']
				instances = reservations[0]['Instances']
				instance = instances[0]
				ipv4 = instance.get('PublicIpAddress')

				if ipv4:
					print(f'\n[+] Eis aqui o portão de entrada - https://{ipv4}/')
					break
				else:
					nova_tentativa = input('Infelizmente, o Olho não encontrou o que lhe foi passado. Deseja tentar novamente? 1 - Sim / 2 - Não: ')
					if nova_tentativa == "2":
						break
			elif eye_action == "2":
				print("\nO Olho, então, lhe dá adeus... Agora, a sua instância será desligada.")
				break

		except NoCredentialsError:
			print('\nErro: Nenhuma credencial encontrada.')
		except PartialCredentialsError:
			print('\nErro: Credenciais incompletas.')
		except Exception as e:
			print(f'\nErro inesperado: {e}')

def ingles():
	# ascii_art()
	print("\nWelcome to Agahmotto. This program is a combination of tools focused on SIEM for analysis in your environment.\nBe prepared for the truths that the Eye will reveal...\n\n--> For information on how to use and prepare the environment, use -h or --help.\n\n- Bruno, Lucas, Rodrigo and Gabriel\n\n")
	awsinstanceenglish()
	sys.exit()

def portugues():
	# ascii_art()
	print("\nBem-vindo ao Agahmotto. Esse programa é uma combinação de ferramentas com foco em SIEM para análise do seu ambiente.\nEsteja preparado(a) para as verdades que o Olho revelará...\n\n--> Para informações sobre o modo de uso e preparação do ambiente, use -h ou --help.\n\n- Bruno, Lucas, Rodrigo e Gabriel\n\n")
	awsintanciaportugues()
	sys.exit()

try:
	if len(sys.argv) >= 3:
		print("Invalid data entry. Make sure you only use -h or --help as a parameter.")
	elif sys.argv[1] in ["-h", "--help"]:
		image()
		banner()
		time.sleep(1.5)
		a = "help"
		menu_idioma()
	elif sys.argv[1] not in ["-h", "--help"]:
		print("Invalid parameter. Make sure you only use -h or --help as a parameter.")
except IndexError:
	image()
	banner()
	time.sleep(1.5)
	a = "none"
	menu_idioma()

