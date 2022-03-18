from kombu import Queue, Exchange
# from

from config import BROKER_URL, RESULT_BACKEND


task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('_queue', Exchange('_ex'), routing_key='_route')
)


task_routes = {

}