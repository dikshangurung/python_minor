##################### Hard Starting Project ######################
import random

import pandas
import datetime as dt
import smtplib
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
#


#My method bruhhhhhhhhhh
data_Frame = pandas.read_csv("birthdays.csv")
data_dict_list = data_Frame.to_dict(orient="records")
print(data_dict_list)
# data = data_Frame.iterrows()
# print(data)
now = dt.datetime.now()
now_day = now.day
now_month = now.month

today_birthday = [data for data in data_dict_list if data["month"] == 1 and data["day"] == 6]

my_email = "pythontest3967@gmail.com"
my_password = "ruevmynqbbpslzkk"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=my_password)
for data in today_birthday:
    with open(file=f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        final_letter = letter.replace("[NAME]",f"{data['name']}").replace("Angela","Dikshan")
    connection.sendmail(from_addr=my_email,to_addrs=data['email'],msg=f"Subject: Happy Birthday \n\n {final_letter}")

connection.close()

# print(today_birthday)
# print(final_letter)
# import pandas
# month =0
# day = 0
# data_Frame = pandas.read_csv("birthdays.csv")
# data_dict_list = data_Frame.to_dict(orient="records")
# birthday_dict = {}
# for data in data_dict_list:
#     birthday_dict[('month','day')] = (data['month'],data['day'])
# print(birthday_dict)
# print(data_dict_list)