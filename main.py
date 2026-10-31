import os

import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route


async def index(request):
    return JSONResponse({"message": "Hello from Starlette!"})


async def health(request):
    return PlainTextResponse("ok\n")


app = Starlette(routes=[Route("/", index), Route("/health", health)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
