def menu_ajuda_pt():
	print("""

O Olho te dá boas vindas ao menu de ajuda... Aqui você irá encontrar um guia de como montar um ambiente AWS com Wazuh e Suricata para a utilização do programa com eficiência.

1. Acesso à AWS

	1.	Acesso ao Console AWS: Acesso o console da AWS usando minhas credenciais.

2. Preparação do Ambiente

	1.	Selecionar o Serviço EC2: Navego até o serviço EC2 no console AWS.

	2.	Configuração de Rede:

		- Verifico se já tenho uma VPC (Virtual Private Cloud) configurada ou crio uma nova para o isolamento do ambiente.
		- Configuro uma sub-rede e um grupo de segurança que permita o tráfego necessário:
			--> Porta 22: Para acesso SSH.
			--> Porta 443: Para o acesso ao painel web do Wazuh.
			--> Porta 1514/UDP e 1515/TCP: Para a comunicação entre o Wazuh Manager e os agentes.

3. Lançamento da Instância EC2

	1.	Iniciar Instância EC2: Clico em “Launch Instance” no painel EC2 e sigo as instruções:

		- Nome da Instância: Defino um nome como “Wazuh”.
		- Escolher a AMI: Encontre o Wazuh All-In-One Deployment e clique em “Select
		- Tipo de Instância: Escolho um tipo de instância que atenda às necessidades do Wazuh, como t3.medium para balancear custo e performance.
		- Par de Chaves SSH: Escolho ou crio um novo par de chaves para acessar a instância.
		- Configuração de Rede: Asseguro que a instância será lançada na VPC e sub-rede desejadas e aplico o grupo de segurança configurado anteriormente.
 		- Atribuo um IP Primário: Configurações de rede/ Configurações avançadas de rede (caso contrário toda vez que interromper a instancia o IP muda e desconecta os agents).

	2.	Configuração de Armazenamento:

		- Geralmente, mantenho o volume padrão de 30 GB para o sistema raiz, mas posso ajustar conforme a necessidade de armazenamento de logs.

	3.	Revisar e Lançar: Reviso todas as configurações e lanço a instância.

4. Preparação das Instâncias EC2

	1.	Lançar Instâncias EC2:

		- Acesso o console AWS e crio duas instâncias EC2, uma com Debian e outra com Ubuntu.
		- Certifico-me de que ambas as instâncias estão na mesma VPC e no mesmo grupo de segurança que a instância do Wazuh Server.
		- Asseguro que as portas necessárias estejam abertas (porta 22 para SSH e as portas 1514/UDP e 1515/TCP para comunicação com o Wazuh Server).

	2.	Obtenção dos IPs:

		- Anoto os endereços IP públicos ou privados (se estiver usando uma VPN) das instâncias Debian e Ubuntu.

	3.	Atualizar Sistemas:

		- Em ambas as instâncias, atualizo os pacotes:

				bash
		sudo apt update && sudo apt upgrade -y

	4.	Registrar os Agentes no Wazuh Dashboard

		1.	Acessar o Wazuh Dashboard:

			- No navegador, acesso o painel do Wazuh:

				https://<IP-do-Wazuh-Server>

			- Faço login com minhas credenciais.

		2.	Adicionar Agentes:

			- No dashboard, navego até "Agents" no menu lateral.
			- Clico em "Add agent" para adicionar os novos agentes.
			- Atribuo o IP primário do Wazuh Server
			- Crio um grupo (Linux) para atribuir as regras do suricata.

		3.	Registrar o Agente:

			- Volto ao terminal SSH conectado à instância e executo o comando copiado do dashboard para registrar o agente.
			- Repito o processo para a segunda instância.

		4.	Iniciar o Wazuh Agent:

			- Em ambas as instâncias, inicio o Wazuh Agent e configuro para iniciar automaticamente:

					bash
			sudo systemctl enable wazuh-agent
			sudo systemctl start wazuh-agent

		5.	Verificação:

			- No Wazuh Dashboard, verifico se ambos os agentes foram registrados corretamente e estão online.

5. Instalação do Suricata

	1.	Instalar Suricata:

		- Em ambas as instâncias, instalo o Suricata:

			bash
		sudo apt install suricata -y

	2.	Configuração do Suricata:

		- Configuro o Suricata para monitorar as interfaces de rede. Abro o arquivo de configuração:

			bash
		sudo nano /etc/suricata/suricata.yaml

	3.	Ajusto as interfaces de rede que o Suricata deve monitorar, geralmente a interface eth0: Iniciar Suricata:

		- Inicio o Suricata e configuro para iniciar automaticamente:

			bash
		sudo systemctl enable suricata
		sudo systemctl start suricata

6. Integração do Suricata com o Wazuh

	1.	Verificar Logs do Suricata:

		- Suricata gera logs que podem ser monitorados pelo Wazuh. Verifico o local onde os logs são armazenados, geralmente em /var/log/suricata/fast.log.

	2.	Configurar Wazuh para Monitorar Logs do Suricata:

		- No Wazuh Server, edito o arquivo de configuração /var/ossec/etc/ossec.conf para adicionar uma entrada que monitore os logs do Suricata:
		- Após a edição, reinicio o Wazuh Manager para aplicar as configurações:

			bash
		sudo systemctl restart wazuh-manager

7. Testes e Validação

	1.	Monitoramento via Wazuh Dashboard:
		- No Wazuh Dashboard, navego até "Security Events" para verificar se os eventos gerados pelo Suricata estão sendo monitorados.
		- Realizo um teste básico de tráfego na rede para verificar se o Suricata detecta e envia logs corretamente ao Wazuh.

	2.	Finalização:
		- Documentação de todas as configurações e procedimentos realizados.
		- Garantir que os agentes e Suricata estão funcionando corretamente em conjunto com o Wazuh Server.
""")

def menu_ajuda_en():
	print("""

The Eye welcomes you to the help menu... Here you will find a guide on setting up an AWS environment with Wazuh and Suricata for efficient use of the program.

1. AWS Access

	1. Accessing the AWS Console: Access the AWS console using your credentials.

2. Environment Preparation

	1. Selecting the EC2 Service: Navigate to the EC2 service in the AWS console.

	2. Network Configuration:

		- Check if you already have a VPC (Virtual Private Cloud) configured or create a new one for environment isolation.
		- Configure a subnet and a security group to allow the necessary traffic: 
			--> Port 22: For SSH access. 
			--> Port 443: For access to the Wazuh web interface. 
			--> Port 1514/UDP and 1515/TCP: For communication between the Wazuh Manager and agents.

3. Launching the EC2 Instance

	1. Start EC2 Instance: Click on “Launch Instance” in the EC2 panel and follow the instructions:

		- Instance Name: Set a name like “Wazuh”.
		- Choose the AMI: Find the Wazuh All-In-One Deployment and click on “Select”.
		- Instance Type: Choose an instance type that meets the needs of Wazuh, such as t3.medium to balance cost and performance.
		- SSH Key Pair: Choose or create a new key pair to access the instance.
		- Network Configuration: Ensure the instance will be launched in the desired VPC and subnet and apply the previously configured security group.
		- Assign a Primary IP: Network settings / Advanced network settings (otherwise, every time you stop the instance, the IP changes and disconnects the agents).

	2. Storage Configuration:

		- Generally, keep the default 30 GB volume for the root system but adjust as needed for log storage.

	3. Review and Launch: Review all settings and launch the instance.

4. Preparing EC2 Instances

	1. Launch EC2 Instances:

		- Access the AWS console and create two EC2 instances, one with Debian and another with Ubuntu.
		- Ensure both instances are in the same VPC and security group as the Wazuh Server instance.
		- Ensure that the necessary ports are open (port 22 for SSH and ports 1514/UDP and 1515/TCP for communication with the Wazuh Server).

	2. Obtain IPs:

		- Write the public or private IP addresses (if using a VPN) of the Debian and Ubuntu instances.

	3. Update Systems:

		- On both instances, update the packages:

				bash
		sudo apt update && sudo apt upgrade -y

	4. Register Agents in the Wazuh Dashboard

		1. Access the Wazuh Dashboard:

			- In the browser, access the Wazuh dashboard:

				https://<Wazuh-Server-IP>

			- Log in with my credentials.

		2. Add Agents:

			- In the dashboard, navigate to "Agents" in the side menu.
			- Click on "Add agent" to add the new agents.
			- Assign the primary IP of the Wazuh Server.
			- Create a group (Linux) to assign Suricata rules.

		3. Register the Agent:

			- Return to the SSH terminal connected to the instance and execute the command copied from the dashboard to register the agent.
			- Repeat the process for the second instance.

		4. Start the Wazuh Agent:

			- On both instances, start the Wazuh Agent and configure it to start automatically:

					bash
			sudo systemctl enable wazuh-agent
			sudo systemctl start wazuh-agent

		5. Verification:

			- In the Wazuh Dashboard, check if both agents have been correctly registered and are online.

5. Suricata Installation

	1. Install Suricata:

		- On both instances, install Suricata:

				bash
		sudo apt install suricata -y

	2. Configure Suricata:

		- Configure Suricata to monitor network interfaces. Open the configuration file:

				bash
		sudo nano /etc/suricata/suricata.yaml

	3. Adjust the network interfaces that Suricata should monitor, usually the eth0 interface:

		- Start Suricata and configure it to start automatically:

				bash
		sudo systemctl enable suricata
		sudo systemctl start suricata

6. Integrating Suricata with Wazuh

	1. Check Suricata Logs:

		- Suricata generates logs that can be monitored by Wazuh. Check where the logs are stored, usually in /var/log/suricata/fast.log.

	2. Configure Wazuh to Monitor Suricata Logs:

		- On the Wazuh Server, edit the configuration file /var/ossec/etc/ossec.conf to add an entry to monitor Suricata logs.
		- After editing, restart the Wazuh Manager to apply the changes:

				bash
		sudo systemctl restart wazuh-manager

7. Testing and Validation

	1. Monitoring via Wazuh Dashboard:

		- In the Wazuh Dashboard, navigate to "Security Events" to check if events generated by Suricata are being monitored.
		- Perform a basic network traffic test to verify if Suricata detects and sends logs correctly to Wazuh.

	2. Completion:

		- Document all configurations and procedures performed.
		- Ensure that agents and Suricata are working correctly in conjunction with the Wazuh Server.
""")
