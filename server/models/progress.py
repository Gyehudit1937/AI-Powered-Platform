from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from server.database import Base


class Progress(Base):
    __tablename__ = "progress"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    current_course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"))
    current_section_id: Mapped[str] = mapped_column(ForeignKey("sections.id"))
    current_lesson_id: Mapped[str] = mapped_column(ForeignKey("lessons.id"))
    completion_percentage: Mapped[float] = mapped_column(Float, default=0.0)
