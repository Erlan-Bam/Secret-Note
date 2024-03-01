from fastapi import APIRouter, Depends, HTTPException, Response, status
from database import AsyncSession, get_async_session
from utils import hash_id, hash_password, check_password
from note.repository import NoteController as note_controller

router = APIRouter(
    prefix='/note',
    tags=['Note']
)

@router.post('/create-note', status_code=status.HTTP_201_CREATED)
async def create_note(text: str, password: str, db: AsyncSession = Depends(get_async_session)):
    # get values for creating a note
    hashed_id = hash_id(text=text, password=password)
    hashed_password = hash_password(password=password)
    # create a new note
    note = {
        "text": text,
        "hashed_id": hashed_id,
        "hashed_password": hashed_password
    }
    new_note = await note_controller.create_note(note, db)

    return {"ID": new_note.hashed_id}

@router.get('/read-note', status_code=status.HTTP_200_OK)
async def read_note(hashed_id: str, password: str, db: AsyncSession = Depends(get_async_session)):
    note = await note_controller.get_note_by_hashed_id(hashed_id, db)

    if not note:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect ID"
        )
    
    if not check_password(password=password, hashed_password=note.hashed_password):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect secret phrase"
        )

    await note_controller.delete_note_by_id(note.id, db)

    return note