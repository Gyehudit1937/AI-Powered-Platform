from server.data.store import COURSES_DB
from server.database import SessionLocal
from server.models import Course, Lesson, Section


def update_content() -> None:
    db = SessionLocal()
    try:
        for course_data in COURSES_DB.values():
            course = db.get(Course, course_data["id"])
            if course is None:
                print(f"Skipping missing course {course_data['id']}")
                continue
            course.title = course_data["title"]
            course.description = course_data["description"]

            for section_data in course_data["sections"].values():
                section = db.get(Section, section_data["id"])
                if section is None:
                    print(f"Skipping missing section {section_data['id']}")
                    continue
                section.title = section_data["title"]

                for lesson_data in section_data["lessons"].values():
                    lesson = db.get(Lesson, lesson_data["id"])
                    if lesson is None:
                        print(f"Skipping missing lesson {lesson_data['id']}")
                        continue
                    lesson.title = lesson_data["title"]
                    lesson.content = lesson_data["content"]

        db.commit()
        print("Updated all course/section/lesson content to Hebrew.")
    finally:
        db.close()


if __name__ == "__main__":
    update_content()
