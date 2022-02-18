from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

auth_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.post('/token')
def generate_token(form_data : OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token":form_data.username,"token_type":"bearer"}

@app.get("/user/profilepic")
def profile_pic(token:str=Depends(auth_scheme)):
    print(token)
    return {"user":"vijay","profile_pic":"my_face"}
