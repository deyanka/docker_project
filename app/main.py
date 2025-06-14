from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import mysql.connector
from mysql.connector import pooling, Error
from typing import List, Optional
import os
import time

app = FastAPI(
    title="Winx Club Magic API",
    description="<b>Только вместе мы сильны, чудеса творить вольны </b>",
    contact={
        "name": "Winx Fairy all the important info",
        "url": "https://winx.fandom.com"
    },
    swagger_ui_css_url="/static/swagger-theme.css",
    swagger_ui_parameters={
        "syntaxHighlight": True,
        "tryItOutEnabled": True,
        "displayRequestDuration": True
    }
)


app.mount("/static", StaticFiles(directory="static"), name="static")

class Fairy(BaseModel):
    fairy_name: str
    age: int
    zodiac_sign: str
    wing_color: str
    magic_power: str

class FairyResponse(Fairy):
    id: int

def get_connection():
    return connection_pool.get_connection()

def wait_for_mysql():
    """Были проблемы с тем что докер просто не дожидался
    подключения к дб и все ломалось поэтому так"""
    max_attempts = 10
    wait_seconds = 20

    for attempt in range(max_attempts):
        try:
            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST", "winx_mysql"),
                user=os.getenv("DB_USER", "flora"),
                password=os.getenv("DB_PASSWORD"),
                port=3306
            )
            conn.close()
            return True
        except Error as e:
            print(f"Attempt {attempt + 1}/{max_attempts}: MySQL not ready - {e}")
            time.sleep(wait_seconds)
    raise RuntimeError(f"Could not connect to MySQL after {max_attempts} attempts")


wait_for_mysql()

db_config = {
    "host": os.getenv("DB_HOST", "winx_mysql"),
    "user": os.getenv("DB_USER", "flora"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "winx_club_db"),
    "pool_name": "winx_pool",
    "pool_size": 5,
    "pool_reset_session": True
}

try:
    connection_pool = pooling.MySQLConnectionPool(**db_config)
except Error as e:
    print(f"Error creating connection pool: {e}")
    raise

@app.post("/fairies/", response_model=FairyResponse)
def create_fairy(fairy: Fairy):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """INSERT INTO winx_fairies
            (fairy_name, age, zodiac_sign, wing_color, magic_power)
            VALUES (%s, %s, %s, %s, %s)""",
            (fairy.fairy_name, fairy.age, fairy.zodiac_sign,
             fairy.wing_color, fairy.magic_power)
        )
        fairy_id = cursor.lastrowid
        conn.commit()
        return {**fairy.dict(), "id": fairy_id}
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=400,
            detail=f"Giiirl u've made a mistake: {err}"
        )
    finally:
        cursor.close()
        conn.close()

@app.get("/fairies/", response_model=List[FairyResponse])
def get_all_fairies():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM winx_fairies")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

@app.get("/fairies/{fairy_id}", response_model=FairyResponse)
def get_fairy(fairy_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM winx_fairies WHERE id = %s",
            (fairy_id,)
        )
        fairy = cursor.fetchone()
        if not fairy:
            raise HTTPException(
                status_code=404,
                detail="Mama i don't know her"
            )
        return fairy
    finally:
        cursor.close()
        conn.close()

@app.delete("/fairies/{fairy_id}")
def delete_fairy(fairy_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM winx_fairies WHERE id = %s",
            (fairy_id,)
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Can't kill a bitch if a bitch isn't there"
            )
        return {"message": "RIP"}
    finally:
        cursor.close()
        conn.close()
