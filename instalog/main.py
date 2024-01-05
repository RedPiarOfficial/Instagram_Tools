from instagrapi import Client
import atexit
from user import User
from Media import Media
import configparser
import os
import time
import json
os.system("cls")

class Instagram:
	def __init__(self,):
		self.client = Client()
		self._config = configparser.ConfigParser()

	def cleanup_session(self):
		time.sleep(3)
		os.remove("session.json")

	def login(self,):
		os.system("cls")
		username = input("Enter Username: ")
		password = input("Enter password: ")
		save_acc_data = input("save account data?[Y/N]: ")
		if save_acc_data.lower() == "y":
			self._config.read('settings.ini')
			self._config.set('Login Data', 'username', username)
			self._config.set('Login Data', 'password', password)
			with open('settings.ini', 'w') as configfile:
				self._config.write(configfile)
		status = self.client.login(username, password)
		if status == True:
			print("login is successful!(time wait: 3 sec)")
			time.sleep(3)
			self.selector()
		else:
			print("login failed!")

	def login_by_data(self,):
		self._config.read("settings.ini")
		status = self.client.login(self._config["Login Data"]["username"], self._config["Login Data"]["password"])
		if status == True:
			print("login is successful!(time wait: 3 sec)")
			time.sleep(3)
			self.selector()
		else:
			print("login failed!")
	def selector(self,):
		os.system("cls")
		print(r"""
	--------------------------------------------------- 
	  ___           _                                  
	 |_ _|_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
	  | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
	  | || | | \__ \ || (_| | (_| | | | (_| | | | | | |
	 |___|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
	                         |___/                     

	telegram: @RedPiar|channel: @BotesForTelegram
	---------------------------------------------------                                                                                               
	""")
		select = input("""
[1] login
[2] load settings.ini
[0]------------------[0]
[3] Media
[4] User
[0] exit

[>] """)
		if int(select) == 1:
			self.login()
		elif int(select) == 2:
			self.login_by_data()
		elif int(select) == 3:
			Media(client=self.client, exit_module=self.selector).selector()
		elif int(select) == 4:
			User(client=self.client, exit_module=self.selector).selector()


#print(self.client.hashtag_medias_top(name = "undertale", amount = 1))

if __name__ == "__main__":
	Instagram().selector()