import json
import logging
import os
import random
import tweepy

logger = logging.getLogger()
logger.setLevel(logging.INFO)

people = [
    "Jeff Bezos",
    "Elon Musk",
    "Rupert Murdoch",
    "Donald J. Trump",
    "Stanley Kroenke",
    "Andrew Beal",
    "John Menard Jr.",
    "Lukas Walton",
    "Larry Ellison",
    "Ken Griffin",
    "Jerry Jones",
    "Larry Page",
]

causes = [
    "The Boys and Girls Clubs of America",
    "The NAACP",
    "Food for the Hungry",
    "UNICEF USA",
    "The Wounded Warrior Project",
    "Doctors Without Borders",
    "Save the Children",
    "St. Jude Children's Research",
    "The American Red Cross",
    "The World Wildlife Fund",

]

def get_random_index(list_length):
    return int(random.uniform(0, list_length))


def sendTweet(tweet_string):
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    logger.info(tweet_string)

    client = tweepy.Client(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret,
        )  
    client.create_tweet(text = tweet_string)

def returnResponse(response_string):
    return{
        "statusCode": 200,
        "body": json.dumps(response_string)
    }


def lambda_handler(event, context):
    person = people[get_random_index(len(people))]
    cause = causes[get_random_index(len(causes))]
    message_string = f"Noted billionare {person} once again contributes nothing to {cause}."
    if event.get("source", False) == "aws.events":
        sendTweet(message_string)
    else:
        returnResponse(message_string)

if __name__ == "__main__":
    lambda_handler(None, None)
