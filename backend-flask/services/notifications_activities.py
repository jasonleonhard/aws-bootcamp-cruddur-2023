from datetime import datetime, timedelta, timezone


def created_at(days):
    now = datetime.now(timezone.utc).astimezone()
    return (now - timedelta(days=days)).isoformat()


def expires_at(days):
    now = datetime.now(timezone.utc).astimezone()
    return (now + timedelta(days=days)).isoformat()


def created_at_hours(hours):
    now = datetime.now(timezone.utc).astimezone()
    return (now - timedelta(hours=hours)).isoformat()


def expires_at_hours(hours):
    now = datetime.now(timezone.utc).astimezone()
    return (now + timedelta(hours=hours)).isoformat()


class NotificationsActivities:
    def run():
        results = [{
            'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle':  'Jason Leonhard',
            'message': 'Notifications Feature is now live!',
            'created_at': created_at(1),
            'expires_at': expires_at(15),
            'likes_count': 23985,
            'replies_count': 1,
            'reposts_count': 0,
            'replies': [{
                'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                'handle':  'YourFriend',
                'message': 'Well done!',
                'likes_count': 235,
                'replies_count': 0,
                'reposts_count': 0,
                'created_at': created_at(1)
            }],
        },
            {
            'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
            'handle':  'Jason Leonhard',
            'message': 'And now we will move on to other todos',
            'created_at': created_at(2),
            'expires_at': expires_at(9),
            'likes': 827,
            'replies': [{
                'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                'handle':  'YourFriend',
                'message': 'Yup, Yup!',
                'likes_count': 0,
                'replies_count': 0,
                'reposts_count': 0,
                'created_at': created_at(2)
            }],

        },
            {
            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
            'handle':  'Jason Leonhard',
            'message': 'Other messages to be added at a later date',
            'created_at': created_at_hours(1),
            'expires_at': expires_at_hours(12),
            'likes': 253,
            'replies': []
        }
        ]
        return results
