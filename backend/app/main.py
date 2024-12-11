import logging
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import get_db
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Business Bazaar API")

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Добавьте CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend-domain.com",
        "http://localhost:3000"  # для разработки
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Добавьте обработчик ошибок
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to Business Bazaar API"}

@app.get("/proposals/", response_model=List[schemas.Proposal])
def read_proposals(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    proposals = db.query(models.Proposal).offset(skip).limit(limit).all()
    return proposals

@app.post("/proposals/", response_model=schemas.Proposal, status_code=status.HTTP_201_CREATED)
def create_proposal(
    proposal: schemas.ProposalCreate, 
    db: Session = Depends(get_db)
):
    db_proposal = models.Proposal(**proposal.dict())
    db.add(db_proposal)
    db.commit()
    db.refresh(db_proposal)
    return db_proposal

@app.get("/proposals/{proposal_id}", response_model=schemas.Proposal)
def read_proposal(proposal_id: int, db: Session = Depends(get_db)):
    proposal = db.query(models.Proposal).filter(models.Proposal.id == proposal_id).first()
    if proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return proposal 