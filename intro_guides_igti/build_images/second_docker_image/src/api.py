from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from redis import Redis

app = FastAPI()
redis = Redis(host="redis", port=6379)

@app.get("/", response_class=HTMLResponse)
async def root():
    redis.incr("count")
    count = str(redis.get("count"), "utf-8")
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Dev API</title>
            
            <style>
                body {{
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }}
                
                .title {{
                    font-size: 5rem;
                    font-weight: bold;
                    font-family: sans-serif;
                }}
                
            </style>
            
        </head>
        <body>
            <div class="title">
                Dev API [fastapi], count: {count} 
            </div>
        </body>
        </html>
    """

@app.get("/helthz")
async def helthz():
    return {
        "message": "ok!"
        }