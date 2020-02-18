from .tasks import UserTimeLogApi, UserTimeLogOpsApi

def initialize_routes(api):
    api.add_resource(UserTimeLogApi, '/user_log/<string:username>')
    api.add_resource(UserTimeLogOpsApi, '/user_ops')
