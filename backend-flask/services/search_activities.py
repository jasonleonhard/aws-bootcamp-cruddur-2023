from lib import now


class SearchActivities:
    def run(search_term):
        model = {
            'errors': None,
            'data': None
        }

        if search_term == None or len(search_term) < 1:
            model['errors'] = ['search_term_blank']
        else:
            results = [{
                'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                'handle':  'Jason Leonhard',
                'message': 'Cloud is fun or not!',
                'created_at': now()
            }]
            model['data'] = results
        return model
