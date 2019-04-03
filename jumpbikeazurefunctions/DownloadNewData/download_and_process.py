import requests
import logging
from datetime import datetime


def get_data():
    """Get raw data"""
    url = "https://sea.jumpbikes.com/opendata/free_bike_status.json"
    response = requests.get(url)
    if response.status_code != 200:
        logging.error("Error in request: " + response.content)
    return response.json()


def get_timestamp(data) -> datetime:
    """Extract the timestamp from the data as a datetime"""
    return datetime.fromtimestamp(int(data['last_updated']))


def get_bikes(data) -> list:
    return data['data']['bikes']

