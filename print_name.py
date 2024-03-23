# pseudocode
from pyfiglet import Figlet

# ask user to input name
user_name = str(input("What is your name? (Given name only): "))

# ask user to input their dream job
user_dream_job = str(input("What is your dream job?: "))

# ask user what their hobby is
user_hobby = str(input("What is your hobby?: "))

# print name in fancy way
font = Figlet(font="cosmic")
print("-------------------------------------------------------------")
text_style1 = (font.renderText(user_name))
print('\033[91m' + "Your name is: ")
print('\033[93m' + text_style1)

# print dream job in fancy way
text_style2 = (font.renderText(user_dream_job))
print('\033[91m' + "Your dream job is: ")
print('\033[93m' + text_style2)

# print hobby in fancy way
text_style3 = (font.renderText(user_hobby))
print('\033[91m' + "Your hobby is: ")
print('\033[93m' + text_style3)
# display the inputs of the user
# End