from datetime import datetime,  timezone
from opentelemetry import trace

from lib import created_at, created_at_hours, expires_at, expires_at_hours

# CloudWatch logs and WatchTower
# import watchtower
# import logging
# from time import strftime

tracer = trace.get_tracer("home.activities")


class HomeActivities:
    def run():
        # def run(logger): # CloudWatch logs and WatchTower
        # LOGGER.info('Hello Cloudwatch! Home Activities from  /api/activities/home') # CloudWatch logs and WatchTower
        # logger.info("HomeActivities") # CloudWatch logs and WatchTower
        with tracer.start_as_current_span("home-activities-mock-data"):
            span = trace.get_current_span()
            now = datetime.now(timezone.utc).astimezone()
            span.set_attribute("app.now", now.isoformat())
            results = [{
                'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                'display_name': 'Jason Leonhard',
                'handle': 'jasonleonhard',
                'user_handle': '@jasonleonhard',
                'message': 'Cloud is very fun!',
                'created_at': created_at(2),
                'expires_at': expires_at(5),
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
                        'created_at': created_at(2),
                        'expires_at': expires_at(5)
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
                        'created_at': created_at(2),
                        'expires_at': expires_at(5)
                    }
                ],

            },
                {
                'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
                'display_name': 'Worf',
                'handle': 'worf',
                'user_handle': '@worf',
                'message': 'I am captain now',
                'created_at': created_at(7),
                'expires_at': expires_at(9),
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
                'created_at': created_at_hours(1),
                'expires_at': expires_at_hours(12),
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
                    'created_at': created_at(2),
                    'expires_at': expires_at(5)
                }],

            }
            ]
            span.set_attribute("app.result_length", len(results))
            return results
