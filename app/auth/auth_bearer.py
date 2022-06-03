from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT

#Now we need to verify the protected route, by checking whether the request is authorized or not.
class JWTBearer(HTTPBearer):
    """
        FastAPI provides the basic validation via the HTTPBearer class
    """
    def __init__(self, auto_error : bool =True):
        """
            In the __init__ method, we enabled automatic error reporting by setting the 
            boolean auto_error to True.
        """
        super(JWTBearer, self).__init__(auto_error=auto_error)


    async def __call__(self, request, Request):
        """
            In the __call__ method, we defined a variable called credentials of type 
            HTTPAuthorizationCredentials, which is created when the JWTBearer class is invoked.
        """
        credentials : HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalif=d tokrn or expire token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")


def verify_jwt(self, jwtoken: str) -> bool:
    """
        - The verify_jwt method verifies whether a token is valid. 
        - The method takes a jwtoken string which it then passes to the decodeJWT function and 
          returns a boolean value based on the outcome from decodeJWT.
    """
    isTokenValid: bool = False

    try:
        payload = decodeJWT(jwtoken)
    except:
         payload = None
    if payload:
        isTokenValid = True
    return isTokenValid