from lib import created_at, expires_at


class Messages:
    def run(user_sender_handle, user_receiver_handle):
        model = {
            'errors': None,
            'data': None
        }

        results = [
            {
                'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a',
                'display_name': 'Jason Leonhard',
                'handle':  'jasonleonhard',
                'user_handle': '@jasonleonhard',
                'message': 'Cloud is fun! idk',
                'created_at': created_at(7),
                'expires_at': expires_at(9),
                'likes_count': 5,
                'replies_count': 1,
                'reposts_count': 0,
            },
            {
                'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
                'display_name': 'Worf',
                'handle':  'worf',
                'user_handle':  '@worf',
                'message': 'This platform is great!',
                'created_at': created_at(7),
                'expires_at': expires_at(31),
                'likes_count': 5,
                'replies_count': 1,
                'reposts_count': 0,
            }]
        model['data'] = results
        return model
#################################################################
# from datetime import datetime, timedelta, timezone


# class Messages:
#     # def run(user_sender_handle, user_receiver_handle):
#     def run(self, user_handle):
#         model = {
#             'errors': None,
#             'data': None
#         }

#         now = datetime.now(timezone.utc).astimezone()

#         if user_handle == '@worf':
#             results = [
#                 {
#                     'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
#                     'display_name': 'Worf',
#                     'handle':  'worf',
#                     'user_handle':  '@worf',
#                     'message': 'This platform is great!',
#                     # 'created_at': now.isoformat(),
#                     'created_at': (now - timedelta(days=7)).isoformat(),
#                     'expires_at': (now + timedelta(days=31)).isoformat(),
#                     'likes_count': 5,
#                     'replies_count': 1,
#                     'reposts_count': 0,
#                 }]
#         elif user_handle == '@garek':
#             results = [
#                 {
#                     'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
#                     'display_name': 'Garek',
#                     'handle': 'garek',
#                     'user_handle': '@garek',
#                     'message': 'My dear doctor, I am just simple tailor',
#                     'created_at': (now - timedelta(hours=1)).isoformat(),
#                     'expires_at': (now + timedelta(hours=12)).isoformat(),
#                     # 'likes': 0,
#                     # 'replies': []
#                     'likes_count': 5,
#                     'replies_count': 1,
#                     'reposts_count': 0,
#                 },
#             ]
#         else:
#             results = [
#                 {
#                     'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a',
#                     'display_name': 'Jason Leonhard',
#                     'handle':  'jasonleonhard',
#                     'user_handle': '@jasonleonhard',
#                     'message': 'Cloud is fun! idk',
#                     # 'created_at': now.isoformat(),
#                     'created_at': (now - timedelta(days=7)).isoformat(),
#                     'expires_at': (now + timedelta(days=9)).isoformat(),
#                     'likes_count': 5,
#                     'replies_count': 1,
#                     'reposts_count': 0,
#                 }]

#         model['data'] = results
#         return model
