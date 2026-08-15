from pydantic import BaseModel


class ProgressUpdatePayload(BaseModel):
    current_lesson_id: str


class Progress(BaseModel):
    user_id: str
    current_course_id: str
    current_section_id: str
    current_lesson_id: str
    completion_percentage: float
