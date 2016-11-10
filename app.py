import sys
import os

curpath = os.path.dirname(__file__)
if(curpath not in sys.path):
    sys.path.append(curpath)

import falcon
import users
import auth

api = application = falcon.API()

db = os.path.join(curpath, 'data.db')

usersManage = users.UserResource(db)
userCollection = users.UserCollectionResource(db)

api.add_route('/users/{userID}', usersManage)
api.add_route('/users', userCollection)

authResource = auth.AuthResource(db)
api.add_route('/auth', authResource)