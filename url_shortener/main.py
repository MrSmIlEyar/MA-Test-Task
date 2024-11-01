from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from sqlite3 import Connection
import string
import random
from database import get_db
from models import create_short_url, get_original_url
from shemas import URLCreate, URL

app = FastAPI()


def generate_short_url(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.post("/shorten", response_model=URL)
def shorten_url(url: URLCreate, db: Connection = Depends(get_db)):
    short_url = generate_short_url()
    create_short_url(url.original_url, short_url)
    return URL(original_url=url.original_url, short_url=short_url)


@app.get("/{short_url}")
def redirect_to_original(short_url: str, db: Connection = Depends(get_db)):
    original_url = get_original_url(short_url)
    if not original_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=original_url)
