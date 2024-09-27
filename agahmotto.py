#!/usr/bin/python

import boto3, time, sys, gettext
from colorama import Fore
from main.ascii_art import image, banner
from main.menu_ajuda import menu_ajuda_pt, menu_ajuda_en
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Variável global de tradução
_ = gettext.gettext

def set_language_en():
    """Função que configura o idioma para inglês."""
    lang = gettext.translation('messages', localedir='locales', languages=['en'])
    lang.install()
    return lang.gettext

def set_language_pt():
    """Função que configura o idioma para português."""
    lang = gettext.translation('messages', localedir='locales', languages=['pt'])
    lang.install()
    return lang.gettext

def language_menu(help_requested=False):
    """Menu de seleção de linguagem do programa"""
    global _
    while True:
        try:
            print(Fore.WHITE + "\n--------------------------------------------------\n")
            print(_("Which language do you want to use in the program?\n\n1 - English\n2 - Português\n3 - Quit Program\n"))
            print("--------------------------------------------------\n")
            language = int(input(_("Pick your language: ")))

            if language == 1:
                _ = set_language_en()
                if help_requested:
                    menu_ajuda_en()
                else:
                    welcome()
                break
            elif language == 2:
                _ = set_language_pt()
                if help_requested:
                    menu_ajuda_pt()
                else:
                    welcome()
                break
            elif language == 3:
                sys.exit()
            else:
                print(_("\nInvalid choice. Make sure to pick a language for the program.\n"))
        except ValueError:
            print(_("\nInvalid choice. Make sure to pick a language for the program."))

def aws_instance():
    """Gerencia as instâncias EC2 na AWS"""
    while True:
        try:
            print(Fore.RED + _("The Eye requests your access keys..."))
            aws_access_key = input(_("Provide your Access Key: "))
            aws_secret_access_key = input(_("Now, provide your Secret Key: "))
            region_name = input(_("It also wants to know which region you are calling from: "))

            ec2_client = boto3.client('ec2', region_name=region_name, 
                                      aws_access_key_id=aws_access_key, 
                                      aws_secret_access_key=aws_secret_access_key)

            instance_id = input(_("Very well. Now, what are your target instances? Provide the IDs: "))
            eye_action = input(_("Finally, what is your wish? Start or stop the instance? 1 - Start / 2 - Stop: "))

            handle_instance_action(eye_action, instance_id, ec2_client)
        except NoCredentialsError:
            print(_("\nError: No credentials found.\n"))
        except PartialCredentialsError:
            print(_("\nError: Incomplete credentials.\n"))
        except Exception as e:
            print(_("\nUnexpected error: {e}\n").format(e=e))

def handle_instance_action(action, instance_id, ec2_client):
    """Executa a ação na instância AWS"""
    try:
        if action == "1":
            ec2_client.start_instances(InstanceIds=[instance_id])
            check_instance_status(instance_id, ec2_client)
        elif action == "2":
            ec2_client.stop_instances(InstanceIds=[instance_id])
            print(_("The Eye bids you farewell... Now, your instance will be stopped."))
        else:
            print(_("The Eye did not understand the request."))
    except Exception as e:
        print(_("\nError during instance action: {e}\n").format(e=e))

def check_instance_status(instance_id, ec2_client):
    """Verifica o status da instância após ação"""
    print(_("Excellent! Now, wait 30 seconds and observe what the Eye was able to find..."))
    time.sleep(30)

    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    ipv4 = response['Reservations'][0]['Instances'][0].get('PublicIpAddress')

    if ipv4:
        print(_("[+] Here is the entry gate - https://{ipv4}/").format(ipv4=ipv4))
    else:
        retry = input(_("Unfortunately, the Eye could not find what was provided. Would you like to try again? 1 - Yes / 2 - No: "))
        if retry == "1":
            check_instance_status(instance_id, ec2_client)

def welcome():
    """Exibe a tela de boas-vindas e chamada do menu AWS"""
    print(_("\nWelcome to Agahmotto!"))
    print(_("This program is a combination of tools focused on SIEM for analysis in your environment.\n"))
    print(_("Be prepared for the truths that the Eye will reveal...\n"))
    print(_("\nFor information on how to use and prepare the environment, use -h or --help."))
    print(_("Bruno, Gabriel, Lucas and Rodrigo.\n"))
    aws_instance()

def main():
    """Executa o programa principal"""
    try:
        if len(sys.argv) >= 3:
            print(_("Invalid data entry. Make sure you only use -h or --help as a parameter."))
        elif sys.argv[1] in ["-h", "--help"]:
            image()
            banner()
            time.sleep(1.5)
            language_menu(help_requested=True)
        else:
            print(_("Invalid parameter. Make sure you only use -h or --help as a parameter."))
    except IndexError:
        image()
        banner()
        time.sleep(1.5)
        language_menu()

if __name__ == "__main__":
    main()
