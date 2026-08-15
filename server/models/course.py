from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database import Base


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    image_url: Mapped[str]

    sections: Mapped[list["Section"]] = relationship(
        back_populates="course", cascade="all, delete-orphan", order_by="Section.order"
    )


class Section(Base):
    __tablename__ = "sections"

    id: Mapped[str] = mapped_column(primary_key=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"))
    title: Mapped[str]
    order: Mapped[int] = mapped_column(Integer)

    course: Mapped["Course"] = relationship(back_populates="sections")
    lessons: Mapped[list["Lesson"]] = relationship(
        back_populates="section", cascade="all, delete-orphan", order_by="Lesson.order"
    )


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[str] = mapped_column(primary_key=True)
    section_id: Mapped[str] = mapped_column(ForeignKey("sections.id", ondelete="CASCADE"))
    title: Mapped[str]
    content: Mapped[str] = mapped_column(Text)
    order: Mapped[int] = mapped_column(Integer)

    section: Mapped["Section"] = relationship(back_populates="lessons")
