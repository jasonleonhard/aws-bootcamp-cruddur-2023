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
