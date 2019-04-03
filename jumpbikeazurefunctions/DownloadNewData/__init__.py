import datetime
import logging

import azure.functions as func

from .download_and_process import get_data, get_bikes, get_timestamp
from .write_to_blob import write_blob


def main(mytimer: func.TimerRequest) -> None:

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Downloading')
    data = get_data()
    timestamp = get_timestamp(data)
    bikes = get_bikes(data)
    for bike in bikes:
        bike['timestamp'] = timestamp.isoformat()
    logging.info("Done for time {0} with {1} bikes".format(timestamp, len(bikes)))
    write_blob(timestamp, bikes)
