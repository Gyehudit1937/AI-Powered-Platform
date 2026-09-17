import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import {
  Box,
  Breadcrumbs,
  Button,
  CircularProgress,
  Container,
  Divider,
  Paper,
  Snackbar,
  Stack,
  Typography,
} from '@mui/material'
import ArrowBackIcon from '@mui/icons-material/ArrowBack'
import CheckCircleIcon from '@mui/icons-material/CheckCircle'
import { fetchCourseDetail } from '../api/courses'
import { useProgress } from '../hooks/useProgress'
import type { CourseDetail, Lesson, Section } from '../types'

function MarkdownContent({ content }: { content: string }) {
  const lines = content.split('\n')
  const elements: React.ReactNode[] = []
  let codeBuffer: string[] = []
  let inCode = false
  let key = 0

  for (const line of lines) {
    if (line.startsWith('```')) {
      if (inCode) {
        elements.push(
          <Box
            key={key++}
            component="pre"
            dir="ltr"
            my={2}
            style={{
              backgroundColor: '#1e1e1e',
              color: '#d4d4d4',
              padding: '20px',
              borderRadius: 8,
              overflowX: 'auto',
              fontSize: '0.875rem',
              fontFamily: 'monospace',
              textAlign: 'left',
              direction: 'ltr',
            }}
          >
            <code>{codeBuffer.join('\n')}</code>
          </Box>
        )
        codeBuffer = []
        inCode = false
      } else {
        inCode = true
      }
    } else if (inCode) {
      codeBuffer.push(line)
    } else if (line.startsWith('# ')) {
      elements.push(<Typography key={key++} variant="h4" fontWeight={700} mt={3} mb={1}>{line.slice(2)}</Typography>)
    } else if (line.startsWith('## ')) {
      elements.push(<Typography key={key++} variant="h5" fontWeight={700} mt={2.5} mb={0.5}>{line.slice(3)}</Typography>)
    } else if (line.startsWith('- ')) {
      elements.push(<Typography key={key++} component="li" variant="body1" sx={{ ml: 2, my: 0.25 }}>{line.slice(2)}</Typography>)
    } else if (line.trim() === '') {
      elements.push(<Box key={key++} sx={{ height: 8 }} />)
    } else {
      elements.push(<Typography key={key++} variant="body1" sx={{ my: 0.5 }}>{line}</Typography>)
    }
  }

  return <Box>{elements}</Box>
}

export default function LessonViewerPage() {
  const { courseId, lessonId } = useParams<{ courseId: string; lessonId: string }>()
  const navigate = useNavigate()
  const { progress, advance } = useProgress()
  const [course, setCourse] = useState<CourseDetail | null>(null)
  const [lesson, setLesson] = useState<Lesson | null>(null)
  const [section, setSection] = useState<Section | null>(null)
  const [nextLesson, setNextLesson] = useState<Lesson | null>(null)
  const [loading, setLoading] = useState(true)
  const [snackOpen, setSnackOpen] = useState(false)

  useEffect(() => {
    if (!courseId || !lessonId) return
    fetchCourseDetail(courseId).then((c) => {
      setCourse(c)
      for (const sec of c.sections) {
        const found = sec.lessons.find((l) => l.id === lessonId)
        if (found) {
          setLesson(found)
          setSection(sec)
          const idx = sec.lessons.indexOf(found)
          const next = sec.lessons[idx + 1] ?? null
          if (next) {
            setNextLesson(next)
          } else {
            const secIdx = c.sections.indexOf(sec)
            const nextSec = c.sections[secIdx + 1]
            setNextLesson(nextSec?.lessons[0] ?? null)
          }
          break
        }
      }
      setLoading(false)
    })
  }, [courseId, lessonId])

  const handleComplete = async () => {
    if (!lessonId) return
    await advance(lessonId)
    setSnackOpen(true)
    if (nextLesson) {
      setTimeout(() => navigate(`/courses/${courseId}/lessons/${nextLesson.id}`), 900)
    }
  }

  if (loading) return <Box display="flex" justifyContent="center" mt={12}><CircularProgress /></Box>
  if (!lesson || !section || !course) return (
    <Container maxWidth="md" sx={{ py: 6 }}>
      <Typography color="error">השיעור לא נמצא.</Typography>
    </Container>
  )

  const isCurrentLesson = progress?.current_lesson_id === lessonId

  return (
    <Container maxWidth="md" sx={{ py: 6 }}>
      <Breadcrumbs sx={{ mb: 3 }}>
        <Button size="small" startIcon={<ArrowBackIcon />} onClick={() => navigate('/')}>
          דף הבית
        </Button>
        <Button size="small" onClick={() => navigate(`/courses/${courseId}`)}>
          {course.title}
        </Button>
        <Typography color="text.primary">{lesson.title}</Typography>
      </Breadcrumbs>

      <Typography variant="overline" color="primary" fontWeight={700}>
        {section.title}
      </Typography>
      <Typography variant="h4" fontWeight={700} gutterBottom>
        {lesson.title}
      </Typography>
      <Divider sx={{ mb: 4 }} />

      <Paper elevation={0} sx={{ bgcolor: 'grey.50', p: 4, borderRadius: 3 }}>
        <MarkdownContent content={lesson.content} />
      </Paper>

      <Stack direction="row" justifyContent="flex-end" mt={4} spacing={2}>
        {nextLesson && !isCurrentLesson && (
          <Button
            variant="contained"
            size="large"
            startIcon={<CheckCircleIcon />}
            onClick={handleComplete}
          >
            סמן כהושלם והמשך
          </Button>
        )}
        {isCurrentLesson && nextLesson && (
          <Button
            variant="outlined"
            size="large"
            onClick={() => navigate(`/courses/${courseId}/lessons/${nextLesson.id}`)}
          >
            ← השיעור הבא
          </Button>
        )}
        {!nextLesson && (
          <Button variant="contained" color="success" size="large" startIcon={<CheckCircleIcon />} onClick={handleComplete}>
            סיימו את הקורס 🎉
          </Button>
        )}
      </Stack>

      <Snackbar
        open={snackOpen}
        autoHideDuration={1500}
        onClose={() => setSnackOpen(false)}
        message="ההתקדמות נשמרה!"
      />
    </Container>
  )
}
