import os
import time
import pyperclip

class User:
	def __init__(self, client, exit_module):
		self.client = client
		self._exit = exit_module

	def user_following(self,):
		username = input("Enter username [username/im]: ")
		getting_userid = 0
		if username == "im":
			getting_userid = self.client.user_id
		else:
			getting_userid = self.client.user_id_from_username(username = username)
		with open(f"./users/user_following/users.txt", "w", encoding="utf-8") as file:
			pass
		followers = self.client.user_following(getting_userid)
		for user_id in followers.keys():
			format_dict = followers.get(f"{user_id}")
			with open(f"./users/user_following/users.txt", "a", encoding="utf-8") as users:
				users.write(f"""
_____________________________
|user_id | {format_dict.pk}
|username| {format_dict.username}
|fullname| {format_dict.full_name}
|private | {format_dict.is_private}
[0]-----------------------[0]
""")
		self.selector()

	def user_followers(self):
		username = input("Enter username [username/im]: ")
		getting_userid = 0
		if username == "im":
			getting_userid = self.client.user_id
		else:
			getting_userid = self.client.user_id_from_username(username = username)
		with open(f"./users/user_followers/users.txt", "w", encoding="utf-8") as file:
			pass
		followers = self.client.user_followers(getting_userid)
		for user_id in followers.keys():
			format_dict = followers.get(f"{user_id}")
			with open(f"./users/user_followers/users.txt", "a", encoding="utf-8") as users:
				users.write(f"""
_____________________________
|user_id | {format_dict.pk}
|username| {format_dict.username}
|fullname| {format_dict.full_name}
|private | {format_dict.is_private}
[0]-----------------------[0]
""")
		self.selector()

	def follow_user(self):
		username = input("enter the username to follow: ")
		user_id = self.client.user_id_from_username(username)
		self.client.user_follow(user_id = user_id)
		print(True)
		time.sleep(3)
		self.selector()

	def unfollow_user(self):
		username = input("enter the username to follow: ")
		user_id = self.client.user_id_from_username(username)
		self.client.user_unfollow(user_id = user_id)
		print(True)
		time.sleep(3)
		self.selector()

	def user_id(self):
		username = input("Enter username [username/im]: ")

		getting_userid = 0
		if username == "im":
			getting_userid = self.client.user_id
			print(f"[UserId] {getting_userid}")
		else:
			getting_userid = self.client.user_id_from_username(username = username)
			print(f"[UserId] {getting_userid}")

		access_to_buffer = input("save ID to buffer?[Y/N]: ")

		if access_to_buffer.lower() == "y":
			pyperclip.copy(str(media_id))
			print("Save is successful!(time wait: 3 sec)")
			time.sleep(3)
		self.selector()


	def banner(self,):
		os.system("cls")
		print(r"""
	--------------------------------------------------- 
	  ___           _          _   _               
	 |_ _|_ __  ___| |_ __ _  | | | |___  ___ _ __ 
	  | || '_ \/ __| __/ _` | | | | / __|/ _ \ '__|
	  | || | | \__ \ || (_| | | |_| \__ \  __/ |   
	 |___|_| |_|___/\__\__,_|  \___/|___/\___|_|   

	telegram: @RedPiar|channel: @BotesForTelegram
	---------------------------------------------------
""")
	def selector(self):
		self.banner()
		select = input("""
[1] user following
[2] user followers
[3] follow user
[4] unfollow user
[0]----------------------[0]
[5] get user_id
[0] back

[>] """)
		if int(select) == 1:
			self.user_following()
		elif int(select) == 2:
			self.user_followers()
		elif int(select) == 3:
			self.follow_user()
		elif int(select) == 4:
			self.unfollow_user()
		elif int(select) == 5:
			self.user_id()
		elif int(select) == 0:
			self._exit()