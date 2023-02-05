import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

people = [
    "Jeff Bezos",
    "Elon Musk",
    "Rupurt Murdoch",
    "Donald J. Trump",
]

causes = [
    "Boys and Girls Clubs of America",
    "NAACP",
    "Food for the Hungry",
]

def get_random_index(list_length):
    return int(random.uniform(0, list_length))

def lambda_handler(event, context):
    person = people[get_random_index(len(people))]
    cause = causes[get_random_index(len(causes))]

    print(f"Noted billionare {person} once again contributes nothing to {cause}.")
    # logger.info(f"Noted billionare {person} once again contributes nothing to {cause}.")

if __name__ == "__main__":
    lambda_handler()
