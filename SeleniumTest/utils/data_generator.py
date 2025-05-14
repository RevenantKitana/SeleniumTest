import random
import requests
from bs4 import BeautifulSoup
from data.test_data import first_names, last_names, addresses, postcodes, cities, states

def get_random_email():
    try:
        response = requests.get("https://10minutemail.net/")
        soup = BeautifulSoup(response.text, "html.parser")
        email = soup.find("input", {"id": "fe_text"})["value"]
        return email
    except Exception as e:
        return f"test{random.randint(1000,9999)}@example.com"

def generate_user_data():
    email = get_random_email()
    username = email.split("@")[0].replace(".", "")
    phone = '0' + ''.join(random.choices('0123456789', k=random.choice([8, 9])))
    password = "A1b2c3"
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    address = random.choice(addresses)
    city = random.choice(cities)
    postcode = random.choice(postcodes)
    state = random.choice(states)
    return {
        "username": username,
        "email": email,
        "password": password,
        "phone": phone,
        "first_name": first_name,
        "last_name": last_name,
        "city": city,
        "address": address,
        "postcode": postcode,
        "state": state,
        "country": "Vietnam"
    }