from sqlalchemy.orm import Session

from server.models import Course as CourseModel
from server.models import Lesson as LessonModel
from server.schemas.course import Course, CourseDetail, Lesson, Section


class CourseService:
    def __init__(self, db: Session) -> None:
        self._db = db

    def get_all_courses(self) -> list[Course]:
        courses = self._db.query(CourseModel).all()
        return [
            Course(
                id=c.id,
                title=c.title,
                description=c.description,
                image_url=c.image_url,
            )
            for c in courses
        ]

    def get_course_detail(self, course_id: str) -> CourseDetail | None:
        course = self._db.get(CourseModel, course_id)
        if course is None:
            return None

        return CourseDetail(
            id=course.id,
            title=course.title,
            description=course.description,
            image_url=course.image_url,
            sections=[
                Section(
                    id=s.id,
                    course_id=s.course_id,
                    title=s.title,
                    order=s.order,
                    lessons=[
                        Lesson(
                            id=l.id,
                            section_id=l.section_id,
                            title=l.title,
                            content=l.content,
                            order=l.order,
                        )
                        for l in s.lessons
                    ],
                )
                for s in course.sections
            ],
        )

    def get_total_lesson_count(self, course_id: str) -> int:
        course = self._db.get(CourseModel, course_id)
        if course is None:
            return 0
        return sum(len(s.lessons) for s in course.sections)

    def find_lesson(self, lesson_id: str) -> dict | None:
        lesson = self._db.get(LessonModel, lesson_id)
        if lesson is None:
            return None

        section = lesson.section
        course = section.course

        return {
            "lesson": lesson,
            "section_id": section.id,
            "course_id": course.id,
            "lesson_order": lesson.order,
            "total_lessons": self.get_total_lesson_count(course.id),
        }
