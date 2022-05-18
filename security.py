import hmac

from models.user import UserModel


#this is creating of test data with out database
#this is usernamemapping and this is used as the username is mapped to all the attributes of the user
#username_mapping={u.username:u for u in users} -- neglected as we have made a function that gets the data from the database
#this mapping is also for the same thing and this is id mapping
#userid_mapping={u.id:u for u in users} -- neglected as we have made a function that gets the data from the database
#this is the authenticate module and which is used for authenticating
def authenticate(username,password):
    user = UserModel.find_by_username(username)
    #user = username_mapping.get(username,None)
    if user and hmac.compare_digest(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    #return userid_mapping(user.id,None)
    return UserModel.find_by_id(user_id)
