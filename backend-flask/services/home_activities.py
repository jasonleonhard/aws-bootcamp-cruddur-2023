# from datetime import datetime, timedelta, timezone
# from opentelemetry import trace

# tracer1 = trace.get_tracer(__name__, "that was the name")
# # tracer2 = trace.get_tracer("home.activities")


# class HomeActivities:
#     def run():
#         # with tracer.start_as_current_span("home-activities-mock-data"):
#         #     tracer = trace.get_tracer(__name__)

#         with tracer1.start_as_current_span("http-handler") as outer_span:
#             outer_span.set_attribute("outer", True)
#             now = datetime.now(timezone.utc).astimezone()
#             with tracer1.start_as_current_span("my-cool-function") as inner_span:
#                 inner_span.set_attribute("inner", True)
#                 results = [{
#                     'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
#                     'handle': 'Jason Leonhard',
#                     'message': 'Cloud is fun!',
#                     'created_at': (now - timedelta(days=2)).isoformat(),
#                     'expires_at': (now + timedelta(days=5)).isoformat(),
#                     'likes_count': 5,
#                     'replies_count': 1,
#                     'reposts_count': 0,
#                     'replies': [{
#                         'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
#                         'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
#                         'handle': 'worf',
#                         'message': 'This post has no honor!',
#                         'likes_count': 0,
#                         'replies_count': 0,
#                         'reposts_count': 0,
#                         'created_at': (now - timedelta(days=2)).isoformat()
#                     }],
#                 },
#                     {
#                     'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
#                     'handle': 'worf',
#                     'message': 'I am out of prune juice',
#                     'created_at': (now - timedelta(days=7)).isoformat(),
#                     'expires_at': (now + timedelta(days=9)).isoformat(),
#                     'likes': 0,
#                     'replies': []
#                 },
#                     {
#                     'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
#                     'handle': 'garek',
#                     'message': 'My dear doctor, I am just simple tailor',
#                     'created_at': (now - timedelta(hours=1)).isoformat(),
#                     'expires_at': (now + timedelta(hours=12)).isoformat(),
#                     'likes': 0,
#                     'replies': []
#                 }
#                 ]
#                 return results
##############################################################################################
# renders
# back: https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/activities/home
# front: https://3000-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/

from datetime import datetime, timedelta, timezone
from opentelemetry import trace

tracer = trace.get_tracer("home.activities")


class HomeActivities:
    def run():
        # logger.info("HomeActivities")
        with tracer.start_as_current_span("home-activites-mock-data"):
            span = trace.get_current_span()
            now = datetime.now(timezone.utc).astimezone()
            span.set_attribute("app.now", now.isoformat())
            results = [{
                'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                'display_name': 'Jason Leonhard',
                'handle': 'jasonleonhard',
                'user_handle': '@jasonleonhard',
                'message': 'Cloud is very fun!',
                'created_at': (now - timedelta(days=2)).isoformat(),
                'expires_at': (now + timedelta(days=5)).isoformat(),
                'likes_count': 16,
                'replies_count': 1,
                'reposts_count': 2,
                'replies': [
                    {
                        'uuid': '66e12864-1c26-5c3a-9658-97a10f8fea99',
                        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                        'display_name': 'Jean Luke Picard',
                        'handle': 'picard',
                        'user_handle': '@picard',
                        'message': 'Make it so!',
                        'likes_count': 11,
                        'replies_count': 0,
                        'reposts_count': 1,
                        'created_at': (now - timedelta(days=2)).isoformat(),
                        'expires_at': (now + timedelta(days=5)).isoformat()
                    },
                    {
                        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                        'display_name': 'Worf',
                        'handle': 'worf',
                        'user_handle': '@worf',
                        'message': 'This post has no honor!',
                        'likes_count': 1,
                        'replies_count': 0,
                        'reposts_count': 1,
                        'created_at': (now - timedelta(days=2)).isoformat(),
                        'expires_at': (now + timedelta(days=5)).isoformat()
                    }
                ],
            },
                {
                'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
                'display_name': 'Worf',
                'handle': 'worf',
                'user_handle': '@worf',
                'message': 'I am captin now',
                'created_at': (now - timedelta(days=7)).isoformat(),
                'expires_at': (now + timedelta(days=9)).isoformat(),
                'likes_count': 5,
                'replies_count': 0,
                'reposts_count': 2,
                'replies': []
            },
                {
                'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                'display_name': 'Garek',
                'handle': 'garek',
                'user_handle': '@garek',
                'message': 'My dear doctor, I am just simple tailor',
                'created_at': (now - timedelta(hours=1)).isoformat(),
                'expires_at': (now + timedelta(hours=12)).isoformat(),
                'likes_count': -2,
                'replies_count': 1,
                'reposts_count': 0,
                'replies': [{
                    'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                    'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                    'handle': 'worf',
                    'message': 'This post has no honor!',
                    'likes_count': 1,
                    'replies_count': 0,
                    'reposts_count': 1,
                    'created_at': (now - timedelta(days=2)).isoformat(),
                    'expires_at': (now + timedelta(days=5)).isoformat()
                }],

            }
            ]
            span.set_attribute("app.result_length", len(results))
            return results
