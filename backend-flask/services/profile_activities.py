# ADDED AND NOT SURE WILL WORK

from datetime import datetime, timezone
from lib import created_at, expires_at


class ProfileActivities:
    def run():
        results = [{
            'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'display_name': 'Jason Leonhard',
            'handle':  'jasonleonhard',
            'user_handle': '@jasonleonhard',
            'message': 'Notifications Feature is now live!',
            'likes_count': 5,
            'replies_count': 1,
            'reposts_count': 2,
            'url': 'url here',
            'title': 'title here',
            'profile-avatar': 'profile-avatar here',
            'profile-desc': 'profile-desc here',
            'profile-display-name': 'profile-display-name here',
            'profile-username': 'profile-username here',
            'profile-desc': 'profile-desc here',
            'created_at': created_at(2),
            'expires_at': expires_at(5),
            'likes_count': 5,
            'replies_count': 1,
            'reposts_count': 0,
            'replies': [{
                'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                'handle':  'worf',
                'message': 'this post has no honor!',
                'likes_count': 0,
                'replies_count': 0,
                'reposts_count': 0,
                'created_at': created_at(2),
                'expires_at': expires_at(5),
            }],
        }
        ]
        return results
