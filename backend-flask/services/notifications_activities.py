from opentelemetry import trace

from lib import created_at, expires_at, created_at_hours, expires_at_hours

tracer = trace.get_tracer("notification.activities")


class NotificationsActivities:
    def run():
        results = [{
            'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'display_name': 'Jason Leonhard',
            'handle': 'jasonleonhard',
            'user_handle': '@jasonleonhard',
            'message': 'Flask is fun.',
            'created_at': created_at(2),
            'expires_at': expires_at(5),
            'likes_count': 5,
            'replies_count': 1,
            'reposts_count': 0,
            'replies': [
                {
                    'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                    'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                    'display_name': 'Worf',
                    'handle': 'worf',
                    'user_handle': '@worf',
                    'message': 'this post has no honor!',
                    'likes_count': 0,
                    'replies_count': 0,
                    'reposts_count': 0,
                    'created_at': created_at(2),
                    'expires_at': expires_at(11),
                },
                {
                    'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
                    'display_name': 'Worf',
                    'handle': 'worf',
                    'user_handle': '@worf',
                    'message': 'I am out of prune juice',
                    'created_at': created_at(7),
                    'expires_at': expires_at(9),
                    'likes': 0,
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
                    'likes': 0,
                    'replies': []
                },
                {
                    'uuid': '22f126b0-1ceb-4a33-88be-d90fa7109eee',
                    'display_name': 'Conan',
                    'handle': 'coco',
                    'user_handle': '@coco',
                    'message': 'I am conan',
                    'created_at': created_at(2),
                    'expires_at': expires_at(5),
                    'likes_count': 5,
                    'replies_count': 1,
                    'reposts_count': 0,

                }
            ]
        }]
        return results
# #######################################


# # class HomeActivities:
# #     def run():
# #       # logger.info("HomeActivities")
# #       # with tracer.start_as_current_span("home-activities-mock-data"):
# #         # span = trace.get_current_span()
# #         # now = datetime.now(timezone.utc).astimezone()
# #         # span.set_attribute("app.now", now.isoformat())
# #         results = [{
# #             'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
# #             'handle': 'coco',
# #             'message': 'I am white unicorn',
# #             # 'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
# #             # 'handle': 'Jason Leonhard',
# #             # 'message': 'Cloud is very fun!',
# #             'created_at': (now - timedelta(days=2)).isoformat(),
# #             'expires_at': (now + timedelta(days=5)).isoformat(),
# #             'likes_count': 5,
# #             'replies_count': 1,
# #             'reposts_count': 0,
# #             'replies': [{
# #                 'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
# #                 'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
# #                 'handle': 'worf',
# #                 'message': 'This post has no honor!',
# #                 'likes_count': 0,
# #                 'replies_count': 0,
# #                 'reposts_count': 0,
# #                 'created_at': (now - timedelta(days=2)).isoformat()
# #             }],
# #         },
# #             {
# #             'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
# #             'handle': 'worf',
# #             'message': 'I am out of prune juice',
# #             'created_at': (now - timedelta(days=7)).isoformat(),
# #             'expires_at': (now + timedelta(days=9)).isoformat(),
# #             'likes': 0,
# #             'replies': []
# #         },
# #             {
# #             'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
# #             'handle': 'garek',
# #             'message': 'My dear doctor, I am just simple tailor',
# #             'created_at': (now - timedelta(hours=1)).isoformat(),
# #             'expires_at': (now + timedelta(hours=12)).isoformat(),
# #             'likes': 0,
# #             'replies': []
# #         }
# #         ]
# #         # span.set_attribute("app.result_length", len(results))
# #         return results
# ###################################################
# NOT WORKING YET

# from datetime import datetime, timedelta, timezone
# from opentelemetry import trace


# def created_at(days):
#     now = datetime.now(timezone.utc).astimezone()
#     return (now - timedelta(days=days)).isoformat()


# def expires_at(days):
#     now = datetime.now(timezone.utc).astimezone()
#     return (now + timedelta(days=days)).isoformat()


# def created_at_hours(hours):
#     now = datetime.now(timezone.utc).astimezone()
#     return (now - timedelta(hours=hours)).isoformat()


# def expires_at_hours(hours):
#     now = datetime.now(timezone.utc).astimezone()
#     return (now + timedelta(hours=hours)).isoformat()


# class NotificationsActivities:
#     def run():
#         results = [{
#             'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
#             'handle': 'Jason Leonhard',
#             'message': 'Notifications Feature is now live!',
#             'created_at': created_at(1),
#             'expires_at': expires_at(15),
#             'likes_count': 23985,
#             'replies_count': 1,
#             'reposts_count': 0,
#             'replies': [
#                 {
#                     'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
#                     'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
#                     'handle': 'worf',
#                     'message': 'this post has no honor!',
#                     'likes_count': 0,
#                     'replies_count': 0,
#                     'reposts_count': 0,
#                     'created_at': (now - timedelta(days=2)).isoformat()
#                 },
#                 {
#                     'uuid': '96e12864-1c26-5c3a-9658-97a10f8fea69',
#                     'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
#                     'handle': 'worf',
#                     'message': 'Well done!',
#                     'likes_count': 235,
#                     'replies_count': 0,
#                     'reposts_count': 0,
#                     'created_at': created_at(1)
#                 }],
#         },
#             {
#             'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
#             'handle': 'worf',
#             'message': 'i am out of prune juice',
#             'created_at': (now - timedelta(days=7)).isoformat(),
#             'expires_at': (now + timedelta(days=9)).isoformat(),
#             'likes': 0,
#             'replies': []
#         },
#             {
#             'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
#             'handle': 'garek',
#             'message': 'my dear doctor, i am just simple tailor',
#             'created_at': (now - timedelta(hours=1)).isoformat(),
#             'expires_at': (now + timedelta(hours=12)).isoformat(),
#             'likes': 0,
#             'replies': []
#         },
#             {
#             'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
#             'handle': 'Jason Leonhard',
#             'message': 'And now we will move on to other todos',
#             'created_at': created_at(2),
#             'expires_at': expires_at(9),
#             'likes': 827,
#             'replies': [{
#                 'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
#                 'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
#                 'handle': 'worf',
#                 'message': 'Yup, Yup!',
#                 'likes_count': 0,
#                 'replies_count': 0,
#                 'reposts_count': 0,
#                 'created_at': created_at(2)
#             }],
#         },
#             {
#             'uuid': '38f126b0-1ceb-4a33-88be-d90fa7109ee3',
#             'handle': 'Jason Leonhard',
#             'message': 'Other messages to be added at a later date',
#             'created_at': created_at_hours(1),
#             'expires_at': expires_at_hours(12),
#             'likes': 253,
#             'replies': []
#         }
#         ]
#         return results
