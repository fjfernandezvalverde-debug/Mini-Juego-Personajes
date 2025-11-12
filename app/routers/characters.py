from fastapi import APIRouter, HTTPException, Query
from app.database import get_db
from app.models import Character

router = APIRouter(prefix="/api/v1/characters", tags=["Characters"])

@router.get("/", response_model=list[Character])
def list_characters(limit: int = Query(50, ge=1, le=200), offset: int = 0):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, year, name, game FROM characters ORDER BY year LIMIT ? OFFSET ?", (limit, offset))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

@router.get("/{id}", response_model=Character)
def get_character(id: int):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, year, name, game FROM characters WHERE id=?", (id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Character not found")
    return dict(row)
