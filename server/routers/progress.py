from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.database import get_db
from server.schemas.progress import Progress, ProgressUpdatePayload
from server.services.course_service import CourseService
from server.services.progress_service import ProgressService

router = APIRouter(prefix="/api/progress", tags=["progress"])


def _get_progress_service(db: Session = Depends(get_db)) -> ProgressService:
    return ProgressService(db=db, course_service=CourseService(db))


@router.get("", response_model=Progress)
async def get_progress(service: ProgressService = Depends(_get_progress_service)):
    return await service.get_progress()


@router.post("", response_model=Progress)
async def update_progress(
    payload: ProgressUpdatePayload,
    service: ProgressService = Depends(_get_progress_service),
):
    return await service.update_progress(payload)
