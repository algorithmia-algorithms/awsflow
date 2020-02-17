from awsflow.tools.emr import logging
from awsflow.version import __version__
import Algorithmia

client = Algorithmia.client("PROVIDE_YOUR_API_KEY")


def hello_world(event, context):
    """
    Test function, calls algorithmia algorithm
    :param event: AWS lambdas function event
    :param context: AWS lambdas function context
    :return:
    """
    if "algorithm" in event:
        algo_name = event['algorithm']
    else:
        raise Exception("'algorithm' field not found.")
    if "username" in event:
        name = event['username']
    else:
        raise Exception("'username' field not found.")

    result = client.algo(algo_name).pipe(name).result
    return {"message": result}
