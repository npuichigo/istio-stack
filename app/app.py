from random import randint
from flask import Flask, request
import logging
from opentelemetry import trace

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
tracer = trace.get_tracer(__name__)

@app.route("/rolldice")
def roll_dice():
    headers = dict(request.headers)
    logger.info(f"Received headers: {headers}")
    player = request.args.get('player', default = None, type = str)
    result = str(roll())
    if player:
        logger.warn("%s is rolling the dice: %s", player, result)
    else:
        logger.warn("Anonymous player is rolling the dice: %s", result)
    return result

def roll():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as rollspan:
        res = randint(1, 6)
        logger.warn("rolling dice is: %s", res)
        rollspan.set_attribute("roll.value", res)
        return res
