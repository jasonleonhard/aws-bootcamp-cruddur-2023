from datetime import datetime, timedelta, timezone


class Messages:
    def run(user_sender_handle, user_receiver_handle):
        model = {
            'errors': None,
            'data': None
        }

        now = datetime.now(timezone.utc).astimezone()

        results = [
            {
                'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a',
                'display_name': 'Jason Leonhard',
                'handle':  'jasonleonhard',
                'user_handle': '@jasonleonhard',
                'message': 'Cloud is fun! idk',
                # 'created_at': now.isoformat(),
                'created_at': (now - timedelta(days=7)).isoformat(),
                'expires_at': (now + timedelta(days=9)).isoformat(),
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
                # 'created_at': now.isoformat(),
                'created_at': (now - timedelta(days=7)).isoformat(),
                'expires_at': (now + timedelta(days=31)).isoformat(),
                'likes_count': 5,
                'replies_count': 1,
                'reposts_count': 0,
            }]
        model['data'] = results
        return model
