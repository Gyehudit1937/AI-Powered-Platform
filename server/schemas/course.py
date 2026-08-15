from pydantic import BaseModel


class Course(BaseModel):
    id: str
    title: str
    description: str
    image_url: str


class Lesson(BaseModel):
    id: str
    section_id: str
    title: str
    content: str
    order: int


class Section(BaseModel):
    id: str
    course_id: str
    title: str
    order: int
    lessons: list[Lesson]


class CourseDetail(BaseModel):
    id: str
    title: str
    description: str
    image_url: str
    sections: list[Section]
