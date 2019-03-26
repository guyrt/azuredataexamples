from azure.storage.blob import BlockBlobService
from json import dumps
from io import StringIO


path = "sea/year={year}/month={month}/day={day}/hour={hour}/{filename}"
container_name ='rawjumpbikedata'

def write_blob(timestamp, bikedata):
    block_blob_service = BlockBlobService(account_name='accountname', account_key='accountkey')
    resolved_path = path.format(
        year=timestamp.strftime('%Y'),
        month=timestamp.strftime('%m'),
        day=timestamp.strftime('%d'),
        hour=timestamp.strftime('%H'),
        filename=timestamp.strftime('%M%S.json')
    )

    data = '\n'.join([dumps(b) for b in bikedata])

    block_blob_service.create_blob_from_stream(container_name, resolved_path, StringIO(data))
