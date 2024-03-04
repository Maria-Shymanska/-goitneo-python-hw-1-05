'''
In the first step, you need to implement a function to display a list of colleagues 
who need to be congratulated on their birthdays during the week.
You have a list of user dictionaries, each dictionary in it must have the keys name and birthday.
This structure represents a model of a list of users with their names and birthdays.
Where 'name' - is the string with the username and 'birthday' is the datetime object in which the birthday is recorded.
for example:
{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}
Your task is to write a get_birthdays_per_week function
that receives a list of users as input and displays in the console (using print) a list of users
who need to be congratulated day by day next week.
'''

from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    
    birthdays_by_day = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
        if delta_days < 7:
            birthdays_by_day[day_of_week].append(name)
        # else:
        #     print("No birthdays")

        for day, names in birthdays_by_day.items():
        
            print(f"{day}: {', '.join(names)}")
        

users_example = [
    {
        "name": "Bill Gates",
        "birthday": datetime(1955, 11, 26),
    },
    {
        "name": "Chris Redfield",
        "birthday": datetime(1955, 11, 28),
    },
    {
        "name": "Albert Wesker",
        "birthday": datetime(1955, 11, 29),
    },
    {
        "name": "Bogdan",
        "birthday": datetime(1993, 5, 7),
    },
    {
        "name": "Maria",
        "birthday": datetime(1989, 1, 1),
    },
    {
        "name": "Oleg",
        "birthday": datetime(2008, 2, 26),
    },
    {
        "name": "Daniel",
        "birthday": datetime(2011, 8, 21),
    },
]

get_birthdays_per_week(users_example)
