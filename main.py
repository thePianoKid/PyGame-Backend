from typing import Union

from fastapi import FastAPI

app = FastAPI()

# r: the mobile phone user will be assigned to move right
# l: the mobile phone user will be assigned to move left
# u: the mobile phone user will be assigned to move up
# s: the mobile phone user will be assigned to shoot
actions = ["r", "l", "u", "s"]

@app.get("/actions")
def read_root():
    if len(actions) > 0:
        action = actions.pop()
    else:
        action = None
        
    return {"action": action}