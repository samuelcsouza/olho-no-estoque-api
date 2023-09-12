from socketify import Request, Response
from config.socketify import router


@router.get("/")
def hello_world(res: Response, req: Request):
    data = {
        "hello": "world"
    }

    res.end(data)
