from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

# Define a set of hardcoded username and password for demonstration purposes
fake_users_db = {
    "user1": "password1",
    "user2": "password2",
}


# Function to authenticate users
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username in fake_users_db and fake_users_db[username] == password:
        return username
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


# Protected endpoint
@app.get("/protected")
async def protected_endpoint(username: str = Depends(authenticate_user)):
    return {"message": f"Hello, {username}. This is a protected endpoint."}


app
