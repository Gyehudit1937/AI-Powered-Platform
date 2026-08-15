export interface Course {
  id: string
  title: string
  description: string
  image_url: string
}

export interface Lesson {
  id: string
  section_id: string
  title: string
  content: string
  order: number
}

export interface Section {
  id: string
  course_id: string
  title: string
  order: number
  lessons: Lesson[]
}

export interface CourseDetail extends Course {
  sections: Section[]
}

export interface Progress {
  user_id: string
  current_course_id: string
  current_section_id: string
  current_lesson_id: string
  completion_percentage: number
}

export interface ProgressUpdatePayload {
  current_lesson_id: string
}
