import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import {
  Box,
  Breadcrumbs,
  Button,
  CircularProgress,
  Container,
  Divider,
  List,
  ListItemButton,
  ListItemText,
  Stack,
  Typography,
} from '@mui/material'
import ArrowBackIcon from '@mui/icons-material/ArrowBack'
import MenuBookIcon from '@mui/icons-material/MenuBook'
import { fetchCourseDetail } from '../api/courses'
import type { CourseDetail } from '../types'

export default function CourseDetailPage() {
  const { courseId } = useParams<{ courseId: string }>()
  const navigate = useNavigate()
  const [course, setCourse] = useState<CourseDetail | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!courseId) return
    fetchCourseDetail(courseId)
      .then(setCourse)
      .catch(() => setError('Course not found.'))
      .finally(() => setLoading(false))
  }, [courseId])

  if (loading) return <Box display="flex" justifyContent="center" mt={12}><CircularProgress /></Box>
  if (error || !course) return (
    <Container maxWidth="md" sx={{ py: 6 }}>
      <Typography color="error">{error ?? 'Unknown error'}</Typography>
      <Button onClick={() => navigate('/')} sx={{ mt: 2 }}>Back to dashboard</Button>
    </Container>
  )

  return (
    <Container maxWidth="md" sx={{ py: 6 }}>
      <Breadcrumbs sx={{ mb: 3 }}>
        <Button size="small" startIcon={<ArrowBackIcon />} onClick={() => navigate('/')}>
          Dashboard
        </Button>
        <Typography color="text.primary">{course.title}</Typography>
      </Breadcrumbs>

      <Box
        component="img"
        src={course.image_url}
        alt={course.title}
        sx={{ width: '100%', borderRadius: 3, mb: 3, maxHeight: 220, objectFit: 'cover' }}
      />

      <Typography variant="h4" fontWeight={700} gutterBottom>
        {course.title}
      </Typography>
      <Typography variant="body1" color="text.secondary" mb={5}>
        {course.description}
      </Typography>

      <Stack spacing={4}>
        {course.sections.map((section) => (
          <Box key={section.id}>
            <Stack direction="row" spacing={1} alignItems="center" mb={1}>
              <MenuBookIcon color="primary" fontSize="small" />
              <Typography variant="h6" fontWeight={700}>
                {section.title}
              </Typography>
            </Stack>
            <Divider sx={{ mb: 1 }} />
            <List disablePadding>
              {section.lessons.map((lesson) => (
                <ListItemButton
                  key={lesson.id}
                  sx={{ borderRadius: 2, mb: 0.5 }}
                  onClick={() => navigate(`/courses/${courseId}/lessons/${lesson.id}`)}
                >
                  <ListItemText
                    primary={`${lesson.order}. ${lesson.title}`}
                    slotProps={{ primary: { variant: 'body1' } }}
                  />
                </ListItemButton>
              ))}
            </List>
          </Box>
        ))}
      </Stack>
    </Container>
  )
}
