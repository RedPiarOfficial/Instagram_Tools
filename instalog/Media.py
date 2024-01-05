import os
import atexit
import pyperclip
import time
class Media:
	def __init__(self, client, exit_module):
		self.client = client
		self._exit = exit_module
	def get_media_id(self,):
		os.system("cls")
		url_to_post = input("Enter link to media post: ")
		media_id = self.client.media_pk_from_url(url=url_to_post)
		print(f"[media_id]: {media_id}")
		access_to_buffer = input("Save media_id to buffer?[Y/N]: ")
		if access_to_buffer.lower() == "y":
			pyperclip.copy(str(media_id))
			print("Save is successful!(time wait: 3 sec)")
			time.sleep(3)
		self.selector()

	def get_user_medias(self,):
		os.system("cls")
		username = input("Enter username[username/me]: ")
		user_medias = 0
		if str(username).lower() == "me":
			user_medias = self.client.user_medias(user_id=self.client.user_id)
		else:
			user_id = self.client.user_id_from_username(username=username)
			user_medias = self.client.user_medias(user_id=user_id)
		with open(f"./medias/user_medias/posts_{username}.txt", "w", encoding="utf-8") as file:
			pass
		for media in user_medias:
			with open(f"./medias/user_medias/posts_{username}.txt", "a", encoding="utf-8") as saver:
				saver.write(f"""
_____________________________
|Post    | {media.code}
|media_id| {media.pk}
|comments| {media.comment_count}
|likes   | {media.like_count}
|caption | {media.caption_text}
|usertags| {media.usertags}
|tagsSP  | {media.sponsor_tags}
|videourl| {media.video_url}
|views   | {media.view_count}
[0]-----------------------[0]
""")
		print("get data and save is successful!(time wait: 3 sec)")
		time.sleep(3)
		self.selector()

	def get_media_info(self,):
		os.system("cls")
		media_url = input("Enter link to post: ")
		media_id = self.client.media_pk_from_url(url=media_url)
		media = self.client.media_info(media_pk = media_id)
		with open(f"./medias/media_info/post_{media.code}.txt", "w", encoding="utf-8") as saver:
			saver.write(f"""
_____________________________
|Post    | {media.code}
|media_id| {media.pk}
|comments| {media.comment_count}
|likes   | {media.like_count}
|caption | {media.caption_text}
|usertags| {media.usertags}
|tagsSP  | {media.sponsor_tags}
|videourl| {media.video_url}
|views   | {media.view_count}
[0]-----------------------[0]
""")
		print("get data and save is successful!(time wait: 3 sec)")
		time.sleep(3)
		self.selector()

	def get_media_liker(self,):
		os.system("cls")
		media_url = input("Enter link to post: ")
		media_pk = self.client.media_pk_from_url(url=media_url)
		media_id = self.client.media_id(media_pk=media_pk)
		users = self.client.media_likers(media_id=media_id)

		with open(f"./medias/media_likers/users_{media_pk}.txt", "w", encoding="utf-8") as file:
			pass

		for user in users:
			with open(f"./medias/media_likers/users_{media_pk}.txt", "a", encoding="utf-8") as saver:
				saver.write(f"""
_____________________________
|username| {user.username}
|user_id | {user.pk}
|prof_pic| {user.profile_pic_url}
|private | {user.is_private}
|fullname| {user.full_name}
|stories | {user.stories}
[0]-----------------------[0]
""")
		print("get data and save is successful!(time wait: 3 sec)")
		time.sleep(3)
		self.selector()

	def like_media(self,):
		os.system("cls")
		media_url = input("Enter link to post: ")
		media_pk = self.client.media_pk_from_url(url=media_url)
		media_id = self.client.media_id(media_pk=media_pk)
		self.client.media_like(media_id = media_id)
		print(True)
		self.selector()

	def unlike_media(self,):
		os.system("cls")
		media_url = input("Enter link to post: ")
		media_pk = self.client.media_pk_from_url(url=media_url)
		media_id = self.client.media_id(media_pk=media_pk)
		self.client.media_unlike(media_id = media_id)
		print(True)
		self.selector()
	def banner(self,):
		os.system("cls")
		print(r"""
	 --------------------------------------------------- 
	  ___           _          __  __          _ _       
	 |_ _|_ __  ___| |_ __ _  |  \/  | ___  __| (_) __ _ 
	  | || '_ \/ __| __/ _` | | |\/| |/ _ \/ _` | |/ _` |
	  | || | | \__ \ || (_| | | |  | |  __/ (_| | | (_| |
	 |___|_| |_|___/\__\__,_| |_|  |_|\___|\__,_|_|\__,_|

	 telegram: @RedPiar|channel: @BotesForTelegram
	 ---------------------------------------------------     
""")
	def selector(self):
		self.banner()
		select = input("""
[1] get media id
[2] get user medias
[3] get media info
[4] get media likers
[0]----------------[0]
[5] like media
[6] unlike media
[0] back

[>] """)
		if int(select) == 1:
			self.get_media_id()
		elif int(select) == 2:
			self.get_user_medias()
		elif int(select) == 3:
			self.get_media_info()
		elif int(select) == 4:
			self.get_media_liker()
		elif int(select) == 5:
			self.like_media()
		elif int(select) == 6:
			self.unlike_media()
		elif int(select) == 0:
			self._exit()
