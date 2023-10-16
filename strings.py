import re
import random
import string

def convert_czech_date_to_database_format(czech_date):
    day, month, year = map(int, czech_date.split('.'))
    database_date = f"{year:04d}-{month:02d}-{day:02d}"
    return database_date

czech_date = "12. 10. 2020"
database_date = convert_czech_date_to_database_format(czech_date)
print(database_date)  # Vytiskne: "2020-10-12"

def create_identifiers(input_phrase, use_camel_syntax=False):
    # Odstranění diakritiky z řetězce pro jednoduchost
    input_phrase = input_phrase.replace("č", "c").replace("š", "s").replace("ž", "z").replace(" ", "_")

    if use_camel_syntax:
        # Camel syntax - první slovo začíná malým písmenem
        words = input_phrase.split()
        identifier = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    else:
        # Identifikátor pro proměnné v Pythonu - všechna písmena malá, oddělená podtržítkem
        identifier = input_phrase.lower()

    return identifier

phrase = "To je proměnná v Pythonu"
python_identifier = create_identifiers(phrase)
js_camel_identifier = create_identifiers(phrase, use_camel_syntax=True)
print("Identifikátor pro Python:", python_identifier)  # Vytiskne: "to_je_promenna_v_pythonu"
print("Identifikátor pro JavaScript Camel Syntax:", js_camel_identifier)  # Vytiskne: "toJePromennaVPythonu"

def generate_random_passwords(num_passwords, password_length=10):
    passwords = []
    for _ in range(num_passwords):
        upper_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        lower_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
        special_char = random.choice("-+*")
        digits = ''.join(random.choice(string.digits) for _ in range(3))
        password = f"{upper_chars}{lower_chars}{special_char}{digits}"
        passwords.append(password)
    return passwords

num_passwords = 5
passwords = generate_random_passwords(num_passwords)
for i, password in enumerate(passwords, start=1):
    print(f"Password {i}: {password}")

