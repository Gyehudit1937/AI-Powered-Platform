from server.data.store import COURSES_DB, PROGRESS_DB
from server.database import SessionLocal
from server.models import Course, Lesson, Progress, Section


def seed() -> None:
    db = SessionLocal()
    try:
        if db.query(Course).count() > 0:
            print("Database already has courses — skipping seed.")
            return

        for course_data in COURSES_DB.values():
            course = Course(
                id=course_data["id"],
                title=course_data["title"],
                description=course_data["description"],
                image_url=course_data["image_url"],
            )
            db.add(course)

            for section_data in course_data["sections"].values():
                section = Section(
                    id=section_data["id"],
                    course_id=section_data["course_id"],
                    title=section_data["title"],
                    order=section_data["order"],
                )
                db.add(section)

                for lesson_data in section_data["lessons"].values():
                    lesson = Lesson(
                        id=lesson_data["id"],
                        section_id=lesson_data["section_id"],
                        title=lesson_data["title"],
                        content=lesson_data["content"],
                        order=lesson_data["order"],
                    )
                    db.add(lesson)

        db.flush()

        db.add(
            Progress(
                user_id=PROGRESS_DB["user_id"],
                current_course_id=PROGRESS_DB["current_course_id"],
                current_section_id=PROGRESS_DB["current_section_id"],
                current_lesson_id=PROGRESS_DB["current_lesson_id"],
                completion_percentage=PROGRESS_DB["completion_percentage"],
            )
        )

        db.commit()
        print(f"Seeded {len(COURSES_DB)} courses successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
