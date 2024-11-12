import sys
import webbrowser
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
origins = [
    "http://127.0.0.1:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
def read_root():
    return {"Hello": "World"}


def base_dir():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    else:
        return Path(".")


# Serve Frontend
app.mount(
    "/",
    StaticFiles(directory=base_dir() / "frontend/build/client", html=True),
    name="rr",
)

if __name__ == "__main__":
    import uvicorn

    webbrowser.open("http://127.0.0.1:8000/", new=2, autoraise=True)
    uvicorn.run(app, host="127.0.0.1", port=8000)
