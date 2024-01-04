# Instagram Tools

![Welcome](https://i.pinimg.com/originals/06/80/81/068081ee5b913a47003a64f7233825fe.gif)

Before starting, you will need to [log](/#login) in to your account or load your data from [settings.ini]("/#settings.ini")

# Classes
| [Media](/#Media) | User |
|----------|----------|
| [get media id](/#Get_Media_Id) | user following |
| [get user medias](/#Get_User_Medias) | user followers |
| get media info | follow user |
| get media likers | unfollow user |
| like media | get user_id |
| unlike media | None |

# login
To log in to your account, you should run the main.py script, then choose option 1 (login), enter your username and password, and optionally select the **'save account data'** option

### settings.ini
If you have already [log](/#login) into your account using login and chosen to save account data in settings.ini, you can quickly log in by selecting option 2 (load settings.ini). After a short wait, you will receive a message confirming the login.

# Media
Media - this class is designed for interacting with media posts. Using this class, you can obtain media ID, like posts, and perform other related actions.

> Functions: 6
> 
> version: 1.0.0
> 
> testing: True

### Get_Media_Id
With this function, we obtain the post ID in Instagram Tools, and the post ID is automatically detected in each function! Also, after obtaining the ID, there will be a message 'Save media_id to buffer?' If you choose 'Y,' the media ID will be saved to your clipboard

### Get_User_Medias
