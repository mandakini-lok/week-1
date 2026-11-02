import datetime

current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Good Morning!")

elif current_hour < 17:
    print("Good Afternoon!")

else:
    print("Good Evening!")