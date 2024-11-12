## Python 環境

```sh
uv init template-python-spa
uv add fastapi
uv add "uvicorn[standard]"

# タスクランナー
uv add --dev go-task-bin

# ビルダー
uv add --dev pyinstaller
```

## フロントエンド

```sh
# React Router v7のプレリリースを使っている(@preは今後削除)
bunx create-react-router@pre frontend
# vite.config.tsでssr:falseにする

cd frontend
# Linter/Formatter
bun add --dev --exact @biomejs/biome
```

## 実行

```sh
uv run uvicorn main:app --reload
```
