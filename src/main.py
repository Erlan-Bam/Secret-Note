from fastapi import FastAPI
from note.router import router as note_router

app = FastAPI(
    title="Secret Note"
)

app.include_router(note_router, prefix='/api')