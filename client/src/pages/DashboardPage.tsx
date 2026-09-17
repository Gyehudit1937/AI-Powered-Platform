import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Avatar,
  Box,
  Card,
  CardActionArea,
  CardContent,
  CardMedia,
  Chip,
  CircularProgress,
  Container,
  Divider,
  LinearProgress,
  Stack,
  Typography,
} from '@mui/material'
import SchoolIcon from '@mui/icons-material/School'
import PlayCircleIcon from '@mui/icons-material/PlayCircle'
import MenuBookIcon from '@mui/icons-material/MenuBook'
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents'
import TrendingUpIcon from '@mui/icons-material/TrendingUp'
import { fetchCourses } from '../api/courses'
import { useProgress } from '../hooks/useProgress'
import type { Course } from '../types'

const STATS = [
  { icon: <MenuBookIcon />, label: 'קורסים', value: '6' },
  { icon: <SchoolIcon />, label: 'שיעורים', value: '36' },
  { icon: <EmojiEventsIcon />, label: 'סטודנטים', value: '1,240' },
  { icon: <TrendingUpIcon />, label: 'שיעור השלמה', value: '87%' },
]

export default function DashboardPage() {
  const navigate = useNavigate()
  const [courses, setCourses] = useState<Course[]>([])
  const [coursesLoading, setCoursesLoading] = useState(true)
  const { progress, loading: progressLoading } = useProgress()

  useEffect(() => {
    fetchCourses()
      .then(setCourses)
      .finally(() => setCoursesLoading(false))
  }, [])

  const isActive = (course: Course) =>
    !progressLoading && progress?.current_course_id === course.id

  return (
    <Box sx={{ bgcolor: '#f5f7fa', minHeight: '100vh' }}>

      {/* ── Top Nav ── */}
      <Box sx={{ bgcolor: 'white', borderBottom: '1px solid #e8eaf0', px: 4, py: 1.5 }}>
        <Container maxWidth="lg">
          <Stack direction="row" alignItems="center" justifyContent="space-between">
            <Stack direction="row" alignItems="center" spacing={1.5}>
              <Avatar sx={{ bgcolor: 'primary.main', width: 36, height: 36 }}>
                <SchoolIcon sx={{ fontSize: 20 }} />
              </Avatar>
              <Typography variant="h6" fontWeight={800} color="primary.main">
                האקדמיה לתכנות
              </Typography>
            </Stack>
            <Stack direction="row" spacing={3}>
              {['קורסים', 'הלמידה שלי', 'קהילה'].map((item) => (
                <Typography
                  key={item}
                  variant="body2"
                  fontWeight={500}
                  color="text.secondary"
                  sx={{ cursor: 'pointer', '&:hover': { color: 'primary.main' } }}
                >
                  {item}
                </Typography>
              ))}
            </Stack>
          </Stack>
        </Container>
      </Box>

      {/* ── Hero ── */}
      <Box
        sx={{
          background: 'linear-gradient(135deg, #1565c0 0%, #1976d2 50%, #42a5f5 100%)',
          py: { xs: 6, md: 10 },
          px: 4,
          color: 'white',
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        <Box
          sx={{
            position: 'absolute', inset: 0, opacity: 0.06,
            backgroundImage: 'radial-gradient(circle at 20% 50%, white 1px, transparent 1px), radial-gradient(circle at 80% 20%, white 1px, transparent 1px)',
            backgroundSize: '60px 60px',
          }}
        />
        <Container maxWidth="lg" sx={{ position: 'relative' }}>
          <Typography variant="overline" sx={{ opacity: 0.8, letterSpacing: 3, fontSize: 12 }}>
            פלטפורמת הלמידה שלך
          </Typography>
          <Typography variant="h3" fontWeight={800} mt={1} mb={2} sx={{ lineHeight: 1.2 }}>
            הפכו למפתחי תוכנה
            <br />
            ברמת Production
          </Typography>
          <Typography variant="h6" sx={{ opacity: 0.85, fontWeight: 400, maxWidth: 560 }}>
            קורסים מובנים מבוססי פרויקטים שלוקחים אתכם מרעיון ועד קוד בפריסה —
            עם מנטור AI שמלווה כל צעד.
          </Typography>

          {/* Stats row */}
          <Stack direction="row" spacing={4} mt={5} flexWrap="wrap">
            {STATS.map((s) => (
              <Stack key={s.label} direction="row" alignItems="center" spacing={1}>
                <Box sx={{ opacity: 0.7 }}>{s.icon}</Box>
                <Box>
                  <Typography variant="h6" fontWeight={800} lineHeight={1}>{s.value}</Typography>
                  <Typography variant="caption" sx={{ opacity: 0.75 }}>{s.label}</Typography>
                </Box>
              </Stack>
            ))}
          </Stack>
        </Container>
      </Box>

      <Container maxWidth="lg" sx={{ py: 6 }}>

        {/* ── Continue learning banner ── */}
        {!progressLoading && progress && progress.completion_percentage > 0 && (
          <Box
            onClick={() => navigate(`/courses/${progress.current_course_id}`)}
            sx={{
              mb: 5, p: 3, borderRadius: 3, bgcolor: 'white',
              border: '1.5px solid', borderColor: 'primary.200',
              cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 3,
              boxShadow: '0 2px 12px rgba(25,118,210,0.10)',
              '&:hover': { boxShadow: '0 4px 20px rgba(25,118,210,0.18)' },
              transition: 'box-shadow 0.2s',
            }}
          >
            <Avatar sx={{ bgcolor: 'primary.main', width: 48, height: 48 }}>
              <PlayCircleIcon />
            </Avatar>
            <Box flex={1}>
              <Typography variant="caption" color="primary" fontWeight={700} sx={{ textTransform: 'uppercase', letterSpacing: 1 }}>
                תמשיכו מאיפה שהפסקתם
              </Typography>
              <Typography variant="subtitle1" fontWeight={700} mt={0.3}>
                {progress.current_lesson_id.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}
              </Typography>
              <Stack direction="row" alignItems="center" spacing={1.5} mt={1}>
                <LinearProgress
                  variant="determinate"
                  value={progress.completion_percentage}
                  sx={{ flex: 1, height: 7, borderRadius: 4 }}
                />
                <Typography variant="caption" fontWeight={700} color="primary">
                  {progress.completion_percentage}%
                </Typography>
              </Stack>
            </Box>
          </Box>
        )}

        {/* ── Section heading ── */}
        <Stack direction="row" alignItems="baseline" justifyContent="space-between" mb={3}>
          <Box>
            <Typography variant="h5" fontWeight={800}>כל הקורסים</Typography>
            <Typography variant="body2" color="text.secondary">
              {courses.length} קורסים · בחרו במה להתחיל
            </Typography>
          </Box>
        </Stack>
        <Divider sx={{ mb: 4 }} />

        {coursesLoading ? (
          <Box display="flex" justifyContent="center" mt={10}>
            <CircularProgress />
          </Box>
        ) : (
          <Box
            sx={{
              display: 'grid',
              gridTemplateColumns: { xs: '1fr', sm: 'repeat(2, 1fr)', md: 'repeat(3, 1fr)' },
              gap: 3,
            }}
          >
            {courses.map((course) => {
              const active = isActive(course)
              return (
                <Card
                  key={course.id}
                  elevation={0}
                  sx={{
                    borderRadius: 3,
                    border: '1.5px solid',
                    borderColor: active ? 'primary.main' : '#e8eaf0',
                    bgcolor: 'white',
                    transition: 'transform 0.18s, box-shadow 0.18s, border-color 0.18s',
                    '&:hover': {
                      transform: 'translateY(-5px)',
                      boxShadow: '0 12px 32px rgba(0,0,0,0.10)',
                      borderColor: 'primary.light',
                    },
                    display: 'flex',
                    flexDirection: 'column',
                  }}
                >
                  <CardActionArea
                    onClick={() => navigate(`/courses/${course.id}`)}
                    sx={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'stretch' }}
                  >
                    <Box sx={{ position: 'relative' }}>
                      <CardMedia
                        component="img"
                        height={168}
                        image={course.image_url}
                        alt={course.title}
                        sx={{ objectFit: 'cover' }}
                      />
                      {active && (
                        <Chip
                          icon={<PlayCircleIcon sx={{ fontSize: 15 }} />}
                          label="בתהליך"
                          color="primary"
                          size="small"
                          sx={{
                            position: 'absolute', top: 12, left: 12,
                            fontWeight: 700, fontSize: 11,
                            boxShadow: '0 2px 8px rgba(0,0,0,0.25)',
                          }}
                        />
                      )}
                    </Box>

                    <CardContent sx={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 1 }}>
                      <Typography variant="subtitle1" fontWeight={800} lineHeight={1.3}>
                        {course.title}
                      </Typography>
                      <Typography variant="body2" color="text.secondary" sx={{ flex: 1 }}>
                        {course.description}
                      </Typography>

                      {active && progress ? (
                        <Box mt={1}>
                          <Stack direction="row" justifyContent="space-between" mb={0.5}>
                            <Typography variant="caption" color="primary.main" fontWeight={700}>
                              ההתקדמות שלך
                            </Typography>
                            <Typography variant="caption" color="primary.main" fontWeight={700}>
                              {progress.completion_percentage}%
                            </Typography>
                          </Stack>
                          <LinearProgress
                            variant="determinate"
                            value={progress.completion_percentage}
                            sx={{ height: 7, borderRadius: 4 }}
                          />
                        </Box>
                      ) : (
                        <Chip
                          label="← התחל קורס"
                          size="small"
                          variant="outlined"
                          color="primary"
                          sx={{ alignSelf: 'flex-start', mt: 1, fontWeight: 600, fontSize: 11 }}
                        />
                      )}
                    </CardContent>
                  </CardActionArea>
                </Card>
              )
            })}
          </Box>
        )}
      </Container>
    </Box>
  )
}
