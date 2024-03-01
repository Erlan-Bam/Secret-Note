from fastapi import HTTPException, status
from database import AsyncSession
from note.models import Note

class NoteController:
    async def get_note_by_hashed_id(note_hashed_id: str, db: AsyncSession):
        return await db.run_sync(lambda session: session.query(Note).filter(Note.hashed_id == note_hashed_id).first())
    
    async def create_note(note: dict, db: AsyncSession):
        note_db = Note( 
            text=note["text"], 
            hashed_id=note["hashed_id"], 
            hashed_password=note["hashed_password"]
        )
        db.add(note_db)
        await db.commit()
        await db.refresh(note_db)
        return note_db
    
    async def delete_note_by_id(note_id: int, db: AsyncSession):
        note_db = await db.run_sync(lambda session: session.query(Note).filter(Note.id == note_id).first())
        await db.delete(note_db)
        await db.commit()
        await db.close()
        return note_db
        

    