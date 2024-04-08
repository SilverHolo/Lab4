import json
import logging
import sys

import greengrasssdk

# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# SDK Client
client = greengrasssdk.client("iot-data")

# Counter
my_counter = 0
def function_handler(event, context):
    co2 - event['co2']
    logger.debug(str(co2))
    
    client.publish(
        topic="emissions/recieve",
        queueFullPolicy-"AllOreException"
        payload=json.dumps(
            {"message": "Recieved", "co2maxnumber":max(co2), "target":event['target']}
        ),
    )
except Exception as e: 
    logger.error{"failed to publish message: " + repr(e)}
    return