import asyncio

from fastapi import HTTPException
from sqlalchemy.orm import Session

from server.models import Progress as ProgressModel
from server.schemas.progress import Progress, ProgressUpdatePayload
from server.services.course_service import CourseService

_progress_lock = asyncio.Lock()

DEFAULT_USER_ID = "default_user"


class ProgressService:
    def __init__(self, db: Session, course_service: CourseService) -> None:
        self._db = db
        self._courses = course_service

    async def get_progress(self) -> Progress:
        progress = self._db.get(ProgressModel, DEFAULT_USER_ID)
        return Progress(
            user_id=progress.user_id,
            current_course_id=progress.current_course_id,
            current_section_id=progress.current_section_id,
            current_lesson_id=progress.current_lesson_id,
            completion_percentage=progress.completion_percentage,
        )

    async def update_progress(self, payload: ProgressUpdatePayload) -> Progress:
        result = self._courses.find_lesson(payload.current_lesson_id)
        if result is None:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": {
                        "code": "LESSON_NOT_FOUND",
                        "message": f"Lesson '{payload.current_lesson_id}' does not exist.",
                        "details": None,
                    }
                },
            )

        percentage = round((result["lesson_order"] / result["total_lessons"]) * 100, 1)

        async with _progress_lock:
            progress = self._db.get(ProgressModel, DEFAULT_USER_ID)
            progress.current_course_id = result["course_id"]
            progress.current_section_id = result["section_id"]
            progress.current_lesson_id = payload.current_lesson_id
            progress.completion_percentage = percentage
            self._db.commit()
            self._db.refresh(progress)

        return Progress(
            user_id=progress.user_id,
            current_course_id=progress.current_course_id,
            current_section_id=progress.current_section_id,
            current_lesson_id=progress.current_lesson_id,
            completion_percentage=progress.completion_percentage,
        )
