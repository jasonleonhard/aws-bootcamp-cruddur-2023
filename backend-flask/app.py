from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry import trace
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.core import xray_recorder
from services.user_activities import *
from services.show_activity import *
from services.search_activities import *
from services.notifications_activities import *
from services.messages import *
from services.message_groups import *
from services.create_reply import *
from services.create_message import *
from services.create_activity import *
from services.home_activities import *
from flask import got_request_exception
import rollbar.contrib.flask
import rollbar
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin
import os
import requests

from flask import Flask
app = Flask(__name__)

# ROLLBAR
# Rollbar init code. You'll need the following to use Rollbar with Flask.
# This requires the 'blinker' package to be installed
# import os


# x-ray

# honeycomb.io

# CloudWatch logs and WatchTower
# import watchtower
# import logging
# from time import strftime

# Configuring Logger to Use CloudWatch
# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.DEBUG)
# console_handler = logging.StreamHandler()
# cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
# LOGGER.addHandler(console_handler)
# LOGGER.addHandler(cw_handler)
# # LOGGER.info("Test app.py log: just configed Logger to Use CloudWatch")
# LOGGER.info("HomeActivities")

# honeycomb.io IInitialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
# refreshing endpoint will show in attached flask logs and honeycomb.io dashboard
# https://ui.honeycomb.io/jl-2c/environments/bootcamp/datasets/backend-flask/home
simple_processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(simple_processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)

# x-ray
try:
    xray_url = os.getenv("AWS_XRAY_URL")
    print(xray_url)
except:
    print("An exception occurred:", xray_url)

try:
    xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)
    XRayMiddleware(app, xray_recorder)
except:
    print("An exception occurred")

# honeycomb.io Initialize automatic instrumentation with Flask
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
origins = [frontend, backend]

cors = CORS(
    app,
    resources={r"/api/*": {"origins": origins}},
    expose_headers="location,link",
    allow_headers="content-type,if-modified-since",
    methods="OPTIONS,GET,HEAD,POST",
    allow_credentials=True
)  # added last line

# CloudWatch logs and WatchTower
# @app.after_request
# def after_request(response):
#     timestamp = strftime('[%Y-%b-%d %H:%M]')
#     LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
#     return response

# ROLLBAR


@app.before_first_request
def init_rollbar():
    ROLLBAR_ACCESS_TOKEN = os.getenv("ROLLBAR_ACCESS_TOKEN")
    """init rollbar module"""
    rollbar.init(
        # access token
        ROLLBAR_ACCESS_TOKEN,
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


@app.route('/health')
def health():
    return 'You are healthy!', 200


@app.route("/checkEnvVars", methods=['GET'])
def checkEnvVars():
    return frontend + " " + backend, 200


@app.route('/users')
def users():
    return jsonify({'users': ['Alice', 'Bob', 'Charlie']})


@app.route("/api/routes", methods=['GET'])
def routes():
    """This route shows all available routes"""
    routes = []
    for rule in app.url_map.iter_rules():
        route = {
            'url': str(rule),
            'methods': list(rule.methods),
            'endpoint': rule.endpoint
        }
        routes.append(route)
    data = jsonify(routes)
    return data, 200


@app.route("/api/message_groups", methods=['GET'])
# @xray_recorder.capture('message_groups')
def data_message_groups():
    user_handle = 'jasonleonhard'  # outputs data endpoint # required currently
    # user_handle = '@jasonleonhard' # idk looks same
    model = MessageGroups.run(user_handle=user_handle)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200

# was


@app.route("/api/messages/@<string:handle>", methods=['GET'])
# @xray_recorder.capture('messages/@<string:handle>')
def data_messages(handle):
    # user_sender_handle = 'jasonleonhard'
    user_sender_handle = handle
    user_receiver_handle = request.args.get('user_receiver_handle')
    model = Messages.run(user_sender_handle=user_sender_handle,
                         user_receiver_handle=user_receiver_handle)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200
    return
# now
# @app.route("/api/messages/@<string:user_handle>", methods=['GET'])
# def data_messages(user_handle):
#     # user_activities = UserActivities(request)
#     # messages = Messages(request)
#     # model = user_activities.run(user_handle=user_handle)

#     # user_sender_user_handle = 'jasonleonhard'
#     # user_receiver_user_handle = request.args.get('user_handle')
#     # user_receiver_user_handle = request.args.get('sender_handle')

#     # user_sender_handle = user_handle
#     user_handle = 'jasonleonhard'
#     user_receiver_handle = request.args.get('user_receiver_handle')
#     model = Messages.run(user_sender_handle=user_sender_handle,
#                          user_receiver_handle=user_receiver_handle)
#     if model['errors'] is not None:
#         return model['errors'], 422
#     else:
#         return model['data'], 200
#     return


@app.route("/api/messages", methods=['POST', 'OPTIONS'])
# @xray_recorder.capture('messages')
@cross_origin()
def data_create_message():
    user_sender_handle = 'jasonleonhard'
    user_receiver_handle = request.json['user_receiver_handle']
    message = request.json['message']
    model = CreateMessage.run(
        message=message, user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200
    return


@app.route("/api/activities/home", methods=['GET'])
# # @xray_recorder.capture('home')
def data_home():
    # data = HomeActivities.run(logger=LOGGER) # CloudWatch logs and WatchTower
    data = HomeActivities.run()
    return data, 200


@app.route("/api/activities/notifications", methods=['GET'])
# @xray_recorder.capture('notifications')
def data_notifications():
    # data = HomeActivities.run()
    data = NotificationsActivities.run()
    return data, 200


# # https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/activities/@jasonleonhard
# OG BELOW
# @app.route("/api/activities/@<string:handle>", methods=['GET'])
# @xray_recorder.capture('user_activities')
# def data_handle(handle):
#     user_activities = UserActivities(request)
#     model = UserActivities.run(handle)
#     if model['errors'] is not None:
#         return model['errors'], 422
#     else:
#         return model['data'], 200
#
# This returns data on the backend and appears to also render something on the frontend
@app.route("/api/activities/@<string:user_handle>", methods=['GET'])
# @xray_recorder.capture('user_activities')
@xray_recorder.capture('activities_users')
# @xray_recorder.capture('activities_user')
def data_user_handle(user_handle):
    user_activities = UserActivities(request)
    model = user_activities.run(user_handle=user_handle)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200

# # I can get data from this endpoint like so
# @app.route("/api/activities/@<string:handle>", methods=['GET'])
# # @xray_recorder.capture('user_activities')
# # @cross_origin()
# def data_handle(handle):
#     return jsonify({'data': handle}), 200
#     # return jsonify({'path': warning, 'routes': data}), 200
# or with
# @app.route("/api/activities/@<string:handle>", methods=['GET'])
# def data_handle(handle):
#     user_handle = "@" + handle
#     return jsonify({'data': user_handle}), 200

# @app.route("/api/activities/@<string:handle>", methods=['GET'])
# @xray_recorder.capture('user_activities')
# def data_handle(handle):
#     user_handle = "@" + handle
#     # user_handle = handle
#     # TypeError: UserActivities.run() missing 1 required positional argument: 'user_handle'
#     user_activities = UserActivities(request)
#     # model = UserActivities.run(handle)
#     # model = UserActivities.run(user_handle="@jasonleonhard")
#     # model = UserActivities.run(user_handle=user_handle) # TypeError: UserActivities.run() missing 1 required positional argument: 'self'
#     # model = UserActivities.run(self, user_handle=user_handle)
#     model = UserActivities.run(user_handle=user_handle)

#     if model['errors'] is not None:
#         return model['errors'], 422
#     else:
#         return model['data'], 200
#     # return jsonify({'data': user_handle}), 200

# @app.route("/api/activities/@<string:handle>", methods=['GET'])
# @xray_recorder.capture('user_activities')
# def data_handle(handle):
#     # return 'hi', 200

#     user_activities = UserActivities(request)
#     return user_activities, 200
#     # return model['data'], 200
#     # print(user_activities)
#     model = UserActivities.run(handle)
#     # return model, 200
#     return model['data'], 200

#     # user_handle = 'jasonleonhard' # added for now
#     # if model['errors'] is not None:
#     #     return model['errors'], 422
#     # else:
#     #     return model['data'], 200


# @app.route("/api/activities/@<string:handle>", methods=['GET'])
# # @xray_recorder.capture('user_activities')
# # @cross_origin()
# def data_handle(handle):
#     # return jsonify({'path': warning, 'routes': data}), 200
#     return jsonify({'data': handle}), 200
#     # return model['data'], 200
#     # return model[]

#     # added below starts
#     # handle = 'jasonleonhard'
#     # user_receiver_handle = request.args.get('user_receiver_handle')
#     # model = Messages.run(handle=handle,
#     #                          user_receiver_handle=user_receiver_handle)
#     # # added above ends
#     # user_activities = UserActivities(request)
#     # model = UserActivities.run(handle)
#     # if model['errors'] is not None:
#     #     return model['errors'], 422
#     # else:
#     #     return model['data'], 200

# # examples below to help example above capture user_handle
# # @app.route("/api/message_groups", methods=['GET'])
# # def data_message_groups():
# #     user_handle = 'jasonleonhard'
# #     model = MessageGroups.run(user_handle=user_handle)
# #     if model['errors'] is not None:
# #         return model['errors'], 422
# #     else:
# #         return model['data'], 200

# # @app.route("/api/messages/@<string:handle>", methods=['GET'])
# # def data_messages(handle):
# #     user_sender_handle = 'jasonleonhard'
# #     user_receiver_handle = request.args.get('user_receiver_handle')
# #     model = Messages.run(user_sender_handle=user_sender_handle,
# #                          user_receiver_handle=user_receiver_handle)
# #     if model['errors'] is not None:
# #         return model['errors'], 422
# #     else:
# #         return model['data'], 200
# #     return


@app.route("/api/activities/search", methods=['GET'])
# @xray_recorder.capture('search')
def data_search():
    term = request.args.get('term')
    model = SearchActivities.run(term)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200
    return


@app.route("/api/activities", methods=['POST', 'OPTIONS'])
@cross_origin()
# @xray_recorder.capture('user_activities')
# @xray_recorder.capture('activities_users')
# @xray_recorder.capture('activities')
def data_activities():
    user_handle = 'jasonleonhard'
    message = request.json['message']
    ttl = request.json['ttl']
    model = CreateActivity.run(message, user_handle, ttl)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200
    return


@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
# @xray_recorder.capture('user_activities')
# @xray_recorder.capture('activities_users')
# @xray_recorder.capture('activities')
def data_show_activity(activity_uuid):
    data = ShowActivity.run(activity_uuid=activity_uuid)
    return data, 200


@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST', 'OPTIONS'])
# @xray_recorder.capture('user_activities')
# @xray_recorder.capture('activities_users')
# @xray_recorder.capture('activities')
@cross_origin()
def data_activities_reply(activity_uuid):
    user_handle = 'jasonleonhard'
    message = request.json['message']
    model = CreateReply.run(message, user_handle, activity_uuid)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200
    return


@app.route('/', defaults={'path': ''})
# @xray_recorder.capture('path')
@app.route('/<path:path>')
def catch_all(path):
    """This route shows all available routes"""
    data = []
    warning = f"You entered '{path}'. This URL does not have a rule. Please return home. 🏘️🏡🐱🐈😹🐈‍⬛🐶🐕🦮🐕‍🦺 For your convenience we have provided the API routes that are available below as a reference guide."
    for rule in app.url_map.iter_rules():
        data.append(rule.endpoint)
    return jsonify({'path': warning, 'routes': data}), 200


# ROLLBAR
@app.route('/hello')
def hello():
    print("in hello")
    # x = None
    # x[5]
    return "Hello World!"


# ROLLBAR
@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message(
        'rollbar.report_message here and https://rollbar.com/awswell/all/items', 'warning')
    return "RollBar Test Route returns fine"


# @app.route('/home')
# def home():
#     data = HomeActivities.run()
#     # return data, 200
#     # return 'Welcome Home!🏠🏘️🏡🐱🐈😹🐈‍⬛🐶🐕🦮🐕‍🦺', 200
#     data = jsonify('Welcome Home!🏠🏘️🏡🐱🐈😹🐈‍⬛🐶🐕🦮🐕‍🦺')
#     return data, 200


if __name__ == "__main__":
    app.run(debug=True)
