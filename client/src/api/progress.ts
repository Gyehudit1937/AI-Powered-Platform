import type { Progress, ProgressUpdatePayload } from '../types'

const BASE = '/api'

export async function fetchProgress(): Promise<Progress> {
  const res = await fetch(`${BASE}/progress`)
  if (!res.ok) throw new Error('Failed to load progress')
  return res.json()
}

export async function updateProgress(payload: ProgressUpdatePayload): Promise<Progress> {
  const res = await fetch(`${BASE}/progress`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
  if (!res.ok) throw new Error('Failed to update progress')
  return res.json()
}
