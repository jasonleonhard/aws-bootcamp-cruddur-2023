# when at https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/activities/@jasonleonhard
# "exception.message": "UserActivities.run() missing 1 required positional argument: 'user_handle'",

import os
from datetime import datetime, timedelta, timezone
# import XRay SDK libraries
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware


class UserActivities:
    def __init__(self, request):
        self.xray_recorder = xray_recorder
        self.request = request

    def run(self, user_handle):
        try:
            # Start a segment
            parent_subseg = xray_recorder.begin_subsegment(
                'user_activities_start')
            parent_subseg.put_annotation('url', self.request.url)
            model = {
                'errors': None,
                'data': None
            }

            now = datetime.now(timezone.utc).astimezone()
            # Add metadata or annotation here if necessary
            xray_dict = {'now': now.isoformat()}
            parent_subseg.put_metadata('now', xray_dict, 'user_activities')
            parent_subseg.put_metadata('method', self.request.method, 'http')
            parent_subseg.put_metadata('url', self.request.url, 'http')
            if user_handle == None or len(user_handle) < 1:
                model['errors'] = ['blank_user_handle']
            else:
                try:
                    # Start a subsegment
                    subsegment = xray_recorder.begin_subsegment(
                        'user_activities_nested_subsegment')
                    now = datetime.now()
                    results = [
                        {
                            'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a',
                            # 'display_name': 'Jason Leonhard',
                            # 'created_at': now.isoformat(),
                            # 'handle':  'jasonleonhard',
                            # 'user_handle': '@jasonleonhard',
                            'display_name': user_handle,
                            'handle':  user_handle,
                            'user_handle': user_handle,
                            # 'message': user_handle,
                            'message': 'Cloud is fun! idk',
                            'created_at': (now - timedelta(days=7)).isoformat(),
                            'expires_at': (now + timedelta(days=9)).isoformat(),
                            'likes_count': 15,
                            'replies_count': 1,
                            'reposts_count': 0,
                        },
                        {
                            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                            # 'display_name': 'Jason Leonhard',
                            # 'handle':  'jasonleonhard',
                            # 'user_handle':  '@jasonleonard',
                            # 'display_name': 'Worf',
                            # 'handle':  'worf',
                            'display_name': user_handle,
                            'handle':  user_handle,
                            'user_handle': user_handle,
                            # 'message': user_handle,
                            'message': 'Cloud is fun they say!',
                            'likes_count': 3,
                            'replies_count': 0,
                            'reposts_count': 2,
                            'created_at': (now - timedelta(days=1)).isoformat(),
                            'expires_at': (now + timedelta(days=31)).isoformat()
                        }
                    ]
                    model['data'] = results
                    xray_dict['results'] = len(model['data'])
                    subsegment.put_metadata(
                        'results', xray_dict, 'user_activities')
                except Exception as e:
                    # Raise the error in the segment
                    raise e
                finally:
                    xray_recorder.end_subsegment()
        except Exception as e:
            # Raise the error in the segment
            raise e
        finally:
            # Close the segment
            xray_recorder.end_subsegment()
        return model
