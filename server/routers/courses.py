import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from server.database import get_db
from server.schemas.course import Course, CourseDetail
from server.services.course_service import CourseService

router = APIRouter(prefix="/api/courses", tags=["courses"])


@router.get("", response_model=list[Course])
def list_courses(db: Session = Depends(get_db)):
    return CourseService(db).get_all_courses()


@router.get("/{course_id}", response_model=CourseDetail)
def get_course(course_id: str, db: Session = Depends(get_db)):
    detail = CourseService(db).get_course_detail(course_id)
    if detail is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "COURSE_NOT_FOUND",
                    "message": f"Course '{course_id}' does not exist.",
                    "details": None,
                },
                "requestId": str(uuid.uuid4()),
            },
        )
    return detail
