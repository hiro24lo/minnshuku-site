from app import create_app  # ← まずcreate_appをインポート

app = create_app()          # ← 次にFlaskアプリを作成

if __name__ == '__main__':  # ← 最後にサーバー起動
    app.run(host='0.0.0.0', port=5001, debug=True)
