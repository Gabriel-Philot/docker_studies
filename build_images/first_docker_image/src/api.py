from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Dev API</title>
            
            <style>
                body {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }
                
                .title {
                    font-size: 5rem;
                    font-weight: bold;
                    font-family: sans-serif;
                }
                
            </style>
            
        </head>
        <body>
            <div class="title">
                Dev API [fastapi]
            </div>
        </body>
        </html>
    """

@app.get("/helthz")
async def helth():
    return {
        "message": "ok!"
        }