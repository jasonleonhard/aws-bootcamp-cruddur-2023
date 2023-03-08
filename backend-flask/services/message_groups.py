# from datetime import datetime, timedelta, timezone


# class MessageGroups:
#     def run(user_handle):
#         model = {
#             'errors': None,
#             'data': None
#         }

#         now = datetime.now(timezone.utc).astimezone()
#         results = [
#             {
#                 'uuid': '24b95582-9e7b-4e0a-9ad1-639773ab7552',
#                 # 'display_name': 'Jason Leonhard',
#                 # 'handle':  'jasonleonhard',
#                 'display_name': 'Jason Leonhard',
#                 'handle':  'jasonleonhard',
#                 'created_at': now.isoformat()
#             },
#             {
#                 'uuid': '417c360e-c4e6-4fce-873b-d2d71469b4ac',
#                 # 'display_name': 'YourFriend',
#                 # 'handle':  'YourFriend',
#                 'display_name': 'Worf',
#                 'handle':  'worf',
#                 'created_at': now.isoformat()
#             }]
#         model['data'] = results
#         return model


from lib import created_at, expires_at, created_at_hours, expires_at_hours


class MessageGroups:
    def run(user_handle):
        model = {
            'errors': None,
            'data': None
        }

        results = [
            {
                'uuid': '24b95582-9e7b-4e0a-9ad1-639773ab7552',
                'display_name': 'Jason Leonhard',
                'handle':  'jasonleonhard',
                'user_handle':  '@jasonleonhard',
                'created_at': created_at(7),
                'expires_at': expires_at(9),
                'likes_count': 5,
                'replies_count': 1,
                'reposts_count': 0,
            },
            {
                'uuid': '417c360e-c4e6-4fce-873b-d2d71469b4ac',
                'display_name': 'Worf',
                'handle':  'worf',
                'user_handle':  '@worf',
                'created_at': created_at(3),
                'expires_at': expires_at(7),
                'likes_count': 5,
                'replies_count': 1,
                'reposts_count': 0,
            },
            {
                'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                'display_name': 'Garek',
                'handle': 'garek',
                'user_handle': '@garek',
                'message': 'My dear doctor, I am just simple tailor',
                'created_at': created_at_hours(1),
                'expires_at': expires_at_hours(12),
                # 'likes': 0,
                # 'replies': []
                'likes_count': 5,
                'replies_count': 1,
                'reposts_count': 0,
            },
            {
                'uuid': '22f126b0-1ceb-4a33-88be-d90fa7109eee',
                'display_name': 'Conan',
                'handle': 'coco',
                'user_handle': '@coco',
                'message': 'I am conan',
                'created_at': created_at(2),
                'created_at': expires_at(5),
                'likes_count': 5,
                'replies_count': 1,
                'reposts_count': 0,
            }
        ]
        model['data'] = results
        return model
