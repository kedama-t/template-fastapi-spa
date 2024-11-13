import os
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 開発用CORS
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


def is_nuitka():
    # Nuitkaでコンパイルされているかどうかを確認
    return "__compiled__" in globals()


def get_dir():
    # ディレクトリパスの取得
    if is_nuitka():
        return os.path.dirname(os.path.abspath(sys.argv[0]))
    else:
        return "."


# フロントエンドの配信
frontend_dir = directory = Path(get_dir()) / "frontend/build/client"
if frontend_dir.exists():
    app.mount(
        "/",
        StaticFiles(directory=frontend_dir, html=True),
        name="rr",
    )

if __name__ == "__main__":
    import uvicorn

    if is_nuitka():
        # Nuitkaで実行時はブラウザを開く
        import webbrowser

        webbrowser.open("http://127.0.0.1:8000/", new=2, autoraise=True)

    uvicorn.run(app, host="127.0.0.1", port=8000)
