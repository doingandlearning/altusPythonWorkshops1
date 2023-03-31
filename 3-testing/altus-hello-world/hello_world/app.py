from aws_lambda_powertools.event_handler import APIGatewayRestResolver
import logging
import os

from pythonjsonlogger import jsonlogger

logger = logging.getLogger("APP")
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(fmt="%(asctime)s %(levelname)s %(name)s %(message)s")
logHandler.setFormatter(formatter)
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))


app = APIGatewayRestResolver()

@app.get("/hello/<name>")
def hello_name(name):
    logger.info(f"Request from {name} received")
    return {"message": f"hello {name}"}

@app.get("/hello")
def hello():
    logger.info(f"Request from unknown received")
    return {"message": "Hello unknown!"}



def lambda_handler(event, context):
    return app.resolve(event, context)