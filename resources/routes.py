from .tasks import UserTimeLogApi, UserTimeLogOpsApi, UsersApi, AdminTimeLogApi, LeavesApi

def initialize_routes(api):
    api.add_resource(AdminTimeLogApi, '/adminlog')
    api.add_resource(UserTimeLogApi, '/userlog')
    api.add_resource(UserTimeLogOpsApi, '/user_ops')
    api.add_resource(UsersApi, '/users')
    api.add_resource(LeavesApi, '/leaves')
