"""
Модуль для обробки даних про дні народження користувачів та групування їх за днями тижня.

Даний модуль містить функцію `get_birthdays_per_week`, яка приймає список користувачів
і повертає словник, де ключами є дні тижня, а значеннями — 
списки імен користувачів, що мають дні народження протягом наступного тижня.

"""
from collections import defaultdict
from datetime import datetime

# Function that helps find birthday which are going to be in less than 7 days
def get_birthdays_per_week(users):
    """
    Групує імена користувачів за днями тижня їх днів народження протягом наступного тижня.

    Параметри:
    users (list): Список словників, кожен з яких містить ім'я користувача та його день народження.

    Повертає:
    Друкую дны народження до яких залишилось менше тижня
    None
    """
    dict_required_data = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)
        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            if (birthday_this_year.strftime("%A") == 'Sunday' or
                birthday_this_year.strftime("%A") == 'Saturday'):
                weekday = 'Monday'
            else:
                weekday = user["birthday"].strftime("%A")
            dict_required_data[weekday].append(name)
    for day, names in dict_required_data.items():
        print(f"{day}: {', '.join(names)}")
    return None
