import { useState, useEffect, useCallback } from 'react'
import { fetchProgress, updateProgress } from '../api/progress'
import type { Progress } from '../types'

export function useProgress() {
  const [progress, setProgress] = useState<Progress | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchProgress()
      .then(setProgress)
      .finally(() => setLoading(false))
  }, [])

  const advance = useCallback(async (lessonId: string) => {
    const updated = await updateProgress({ current_lesson_id: lessonId })
    setProgress(updated)
    return updated
  }, [])

  return { progress, loading, advance }
}
