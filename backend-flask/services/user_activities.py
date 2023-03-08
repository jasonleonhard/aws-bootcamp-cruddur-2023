from datetime import datetime, timezone
# import XRay SDK libraries
from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

from lib import created_at, expires_at


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
                            'created_at': created_at(7),
                            'display_name': user_handle,
                            'expires_at': expires_at(42),
                            'handle':  user_handle,
                            'likes_count': 15,
                            'message': 'Cloud is fun! they say',
                            'replies_count': 1,
                            'reposts_count': 0,
                            'user_handle': user_handle,
                            'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a',
                        },
                        {
                            'created_at': created_at(3),
                            'display_name': user_handle,
                            'expires_at': expires_at(11),
                            'handle':  user_handle,
                            'likes_count': 3,
                            'message': 'Cloud is fun they say!',
                            'replies_count': 0,
                            'reposts_count': 2,
                            'user_handle': user_handle,
                            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
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
