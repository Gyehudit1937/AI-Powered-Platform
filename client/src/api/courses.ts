import type { Course, CourseDetail } from '../types'

const BASE = '/api'

export async function fetchCourses(): Promise<Course[]> {
  const res = await fetch(`${BASE}/courses`)
  if (!res.ok) throw new Error('Failed to load courses')
  return res.json()
}

export async function fetchCourseDetail(courseId: string): Promise<CourseDetail> {
  const res = await fetch(`${BASE}/courses/${courseId}`)
  if (!res.ok) throw new Error(`Course ${courseId} not found`)
  return res.json()
}
