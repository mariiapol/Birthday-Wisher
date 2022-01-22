import smtplib
import datetime as dt
import pandas, random


def send_email(birthday_person):

    my_email = "*******"
    password = "********"
    b_email = birthday_person["email"]
    b_name = birthday_person["name"]

    # random letter, replace name
    text = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    file = random.choice(text)

    with open(f"letter_templates/{file}") as letter:
        my_letter = letter.read()
        my_text = my_letter.replace("[NAME]", b_name)

    #send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                    to_addrs=b_email,
                    msg=f"Subject: Happy Birthday!\n\n{my_text}")


now = dt.datetime.now()
day_t = now.day
month_t = now.month
birthdays_dict = {}
birthdays_list = pandas.read_csv("birthdays.csv")
dict = birthdays_list.to_dict(orient="records")
for item in dict:
    if item["day"] == day_t and item["month"] == month_t:
        send_email(item)

