import json
import jwt
USERS= {
    'witek':'1234',
}
def checkUser(username:str):
    '''
    check if user exist in USERS pool
    '''
    if username in USERS.keys():
        return True
    else:
        return False
def validateUser(username:str,password:str):
    '''
    function to verify if valid user is signing in
    '''
    if username in USERS.keys():
        if password== USERS[username]:
            return True
        else:
            return False
    else:
        return False
def decodeJWT(res,secret):
    '''
    decode jwt based on given response and app configuration
    '''
    return jwt.decode(json.loads(res.content)['access_token'], secret, algorithms=['HS256'])
