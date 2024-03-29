# Instagram Tools

![Welcome](https://i.pinimg.com/originals/06/80/81/068081ee5b913a47003a64f7233825fe.gif)

Before starting, you will need to [log](/#login) in to your account or load your data from [settings.ini]("/#settings.ini")

# Classes
| [Media](/#Media) | [User](/#User) |
|----------|----------|
| [get media id](/#Get_Media_Id) | [user following](/#User_Following) |
| [get user medias](/#Get_User_Medias) | [user followers](/#User_Followers) |
| [get media info](/#Get_Media_Info) | [follow user](/#Follow_User) |
| [get media likers](/#Get_Media_Likers) | [unfollow user](/#Unfollow_User) |
| [like media](/#Like_Media) | [get user id](/#Get_User_Id) |
| [unlike media](/#Unlike_Media) | None |

| [Exceptions](/#Exceptions) |
|----------|
| ClientLoginRequired |
| ReloginAttemptExceeded |
| RecaptchaChallengeForm |
| MediaNotFound |
| FeedbackRequired |
| RateLimitError |

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

> login required
>
> params: link
### Get_User_Medias
With this function, you can retrieve all posts from any public profile. Afterward, all the data is saved to a .txt file in a table format within the ./medias/user_medias directory.

> login required
>
> params: link
### Get_Media_Info
This function retrieves complete information about a post through a link and then saves this information to a file in table format within the ./medias/media_info directory.

> login required
>
> params: link
### Get_Media_Likers
This function retrieves people up to the Instagram limit who have liked a post through the post link, then saves their information in table format to the ./users/ directory.

> login required
>
> params: link
### Like_Media
Like a post via the link.

> login required
>
> params: link
### Unlike_Media
Remove a like from a post via the link.
> login required
>
> params: link

# User
User - This class is used for interacting with the user and is also utilized for automation on their behalf.

> Functions: 5
> 
> version: 1.0.0beta
> 
> testing: True

### User_Following
This function shows who the user is following

There are two options:

1. Enter a username
2. Enter 'im' and get your own following list.

> login required
>
> params: username

### User_Followers
This function shows the followers of the user's account.

1. Enter a username
2. Enter 'im' and get your own following list.

> login required
>
> params: username

### Follow_User
This function allows you to follow a user through the script.

> login required
>
> params: username

### Unfollow_User
This function allows you to unfollow a user through the script.

> login required
>
> params: username

### Get_User_Id
This function retrieves the user ID using the username, and there is an option to save the ID to the clipboard

> login required
>
> params: username


# Exceptions

1. ClientLoginRequired - Raised when Instagram required Login
2. ReloginAttemptExceeded - Raised when all attempts exceeded
3. RecaptchaChallengeForm - Raise when get challengeType=RecaptchaChallengeForm
4. MediaNotFound - Raise when user unavailable
5. FeedbackRequired - Raise when get message=feedback_required
6. RateLimitError - Raise when get message=rate_limit_error
