import requests,json
import random
from datetime import datetime
import pytz

def greet():
    greet=["Hi I am chatbot and will do you what you ask me to do","Hello I am chatbot and I will you whatever you ask me to do","Welcome to chatbot. I will answer to whatever you ask"]
    print(random.choice(greet))

def welcome(name):
    print("Hi",name)
    print("Nice to meeet you!... How can I help you?")

def show_menu():
    print("---------------------------------------------------------------")
    print("       1.I will tell you what is date and time")
    print("       2.I will tell you the weather for the place you ask")
    print("       3.Exit this chat")
    print("---------------------------------------------------------------")
    try:
        return int(input("Enter the number of which you want to know : "))
    except:
        print("Only numbers")

def ask_question(question):
    try:
        return question
    except:
        print("Ask a question")

def weather():
    place=input("Enter the place you want to know : ")
    api="https://api.openweathermap.org/data/2.5/weather?"+"q="+place+"&appid="+"1d0fdde520d4cb39c12c77e46601fcdd"
    res=requests.get(api)
    if res.status_code==200:
        data_weather=res.json()
        main=data_weather['main']
        # getting temperature
        temp=main['temp']
        #getting weather condition
        condition= data_weather['weather']
        print("The temperature in ",place," is ",temp," degrees.")
        print("The weather condition in ",place," is ",condition)
    else:
        print("The city is not found.Please enter correct name")

def date_time():
    tz=pytz.utc
    country=int(input("Enter your option from \n1.Asia/Kolkata \n2.America/New York : "))
    if country==1:
        time_asia=pytz.timezone("Asia/Kolkata")
        date_asia=datetime.now(time_asia)
        time=date_asia.astimezone(tz)
        print(time.strftime("Date: %Y-%m-%d\n Time: %H-%M-%S"))
    elif country==2:
        time_us=pytz.timezone("America/New_York")
        date_us=datetime.now(time_us)
        time1=date_us.astimezone(tz)
        print(time1.strftime("Date: %Y-%m-%d\n Time: %H-%M-%S"))
    else:
        print("Enter correct number")


def bot():
    greeting=input()
    greet()
    name=input('Your good name please?')
    welcome(name)
    question=input()
    ask_question(question)
    option=show_menu()
    while option!=3:
        if option==1:
            date_time()
        elif option==2:
            weather()
        option=show_menu()
    else:
        print("Thank you!.. Let's meet next time")
        
bot()