import datetime
import logging

import azure.functions as func

from .download_and_process import get_data, get_bikes, get_timestamp
from .write_to_blob import write_blob


def main(mytimer: func.TimerRequest) -> None:

    if mytimer.past_due:
        logging.info('The timer is past due!')

    data = get_data()
    timestamp = get_timestamp(data)
    bikes = get_bikes(data)

    write_blob(timestamp, bikes)


