from user import User
from post import Post

app_user_one = User("ll@ss.com", "Luke Skywalker", "noooooooo!", "Padawan")
app_user_one.get_user_info()

app_user_one.change_job_title("Jedi Master")
app_user_one.get_user_info()

app_user_two = User("dv@dv.com", "Darth Vader", "deathstar", "Sith Lord")
app_user_two.get_user_info()

app_user_two.change_password("you_are_my_son")
print(f"New password for user \"{app_user_two.name}\" is \"{app_user_two.password}\".")

new_post = Post("I should destroy the Death Star!", app_user_one.name)
new_post.get_post_info()