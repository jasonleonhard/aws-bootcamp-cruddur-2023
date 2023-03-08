from lib import created_at, expires_at


class ShowActivities:
    def run(activity_uuid):
        results = [{
            'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'display_name': 'Jason Leonhard',
            'handle':  'jasonleonhard',
            'user_handle': '@jasonleonhard',
            'message': 'Cloud is fun? maybe!',
            'created_at': created_at(2),
            'expires_at': expires_at(5),
            'likes_count': 5,
            'replies_count': 1,
            'reposts_count': 2,
            'replies': {
                'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                'handle':  'worf',
                'message': 'This post has no honor!',
                'created_at': created_at(2),
                'expires_at': expires_at(5)
            },
        }]
        return results
