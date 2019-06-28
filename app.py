from url_shortener import create_application

app = create_application()

@app.listener('after_server_start')
async def connect_to_db():
    await app.db.connect()

@app.listener('after_server_stop')
async def disconnect_from_db():
    await app.db.disconnect()

app.run(host="0.0.0.0", port=8000, debug=True)
