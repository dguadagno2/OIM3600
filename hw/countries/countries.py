import urllib.request
import json
import random
import pprint


def get_country_info(country_name):
    """
    Take Country name as input, make API request to retrieve information on country, parse JSON response, return dictionary with country name, capital, population, area, and list of languages
    """
    URL = "https://restcountries.com/v3.1/all"
    try:
        with urllib.request.urlopen(URL) as response:
            data = response.read()
            data = json.loads(data)

        for country in data:
            if country_name == country.get("name", {}).get(
                "common", ""
            ):  # Was having dificulties retrieving country information and used chatGPT to debug https://chatgpt.com/share/67107ffa-e3d8-8011-88b7-8b724af8e69e
                country_info = {
                    "name": country.get("name", {}).get("common", "Unknown"),
                    "capital": country.get("capital", ["Unknown"])[0],
                    "population": country.get("population", "Unknown"),
                    "area": country.get("area", "Unkown"),
                    "languages": list(country.get("languages", {}).values()),
                }
                return country_info
    except Exception as e:
        print("Could not retrieve")
    return None


def display_country_info(country_info):
    """
    Take dictionary returned and display information through pprint
    """
    if country_info:
        pprint.pprint(country_info)
    else:
        print("Could not retrieve data")


def quiz_random_country():
    """
    Randomly select a country, retrieve its information, then ask user a quiz question on countrys fact capital, population, or language spoken and provide feedback on user answer
    """
    all_countries = [
        "France",
        "Germany",
        "Japan",
        "Brazil",
        "Australia",
    ]  # Couldn't get code to prompt quiz questions used chatGPT to debug https://chatgpt.com/share/67107ffa-e3d8-8011-88b7-8b724af8e69e
    random_country = random.choice(all_countries)
    country_info = get_country_info(random_country)

    question_type = random.choice(["capital", "population", "languages"])
    if question_type == "capital":
        correct_answer = country_info["capital"]
        user_answer = input(f"What is the capital of {random_country}?")
        if user_answer == correct_answer:
            print(
                f"You are correct. The answer is {correct_answer}."
            )  # Used chatGPT to debug and changed code to be an f string https://chatgpt.com/share/67107ffa-e3d8-8011-88b7-8b724af8e69e
        else:
            print(f"You are incorrect.The answer is {correct_answer}.")
        user_answer = input(
            f"What is the capital of {random_country}?"
        )  # used chatGPT to debug and changed code to f string https://chatgpt.com/share/67107ffa-e3d8-8011-88b7-8b724af8e69e
    elif question_type == "population":
        correct_answer = country_info["population"]
        user_answer = input(f"What is the population of {random_country}?")
        if user_answer == correct_answer:
            print("You are correct.")
        else:
            print(f"You are incorrect. The answer is {correct_answer}.")
        user_answer = input(f"What is the population of {random_country}?")
    elif question_type == "languages":
        correct_answer = country_info["languages"]
        user_answer = input(f"What is the languages of {random_country}?")
        if user_answer == correct_answer:
            print(f"You are correct. The answer is {correct_answer}.")
        else:
            print(f"You are incorrect.The answer is {correct_answer}.")
        user_answer = input(f"What is the languages of {correct_answer}?")


def main():
    country_name = input("Country name >>")
    country_info = get_country_info(country_name)
    display_country_info(country_info)
    quiz_random_country()


if (
    __name__ == "__main__"
):  # Added this portion after debugging with chatGPT https://chatgpt.com/share/67107ffa-e3d8-8011-88b7-8b724af8e69e
    main()
