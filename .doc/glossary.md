# Glossary

## Purpose
- Define canonical domain terms and approved short forms used across code, API routes, docs, and plans to maintain strict agent alignment.

## Core Terms
- `course`
    - Canonical meaning: The top-level educational curriculum entity representing a complete study path (e.g., "Full-Stack Python Bootcamp").
    - Use: Managed as a static memory-mapped dictionary in `server/data/store.py`.
- `section`
    - Canonical meaning: A modular chapter or division splitting core domain concepts within a course.
    - Use: Embedded directly inside the nested `CourseDetail` array payload.
- `lesson`
    - Canonical meaning: The individual instructional text block containing the actual theory material formatted in Markdown.
    - Use: The lowest granularity element containing the target `content` string read by the client workspace.
- `progress`
    - Canonical meaning: The dynamic model tracking a student's active learning coordinates (completion percentage, current IDs).
    - Use: Kept as a module-level dictionary singleton mapping within `server/data/store.py`.
- `navigator`
    - Canonical meaning: The contextual AI Mentor interface companion guiding students with scaffolded hints.
    - Use: This is the product/experience name for the feature. Technologically, it maps strictly to the `chat` context across the codebase. The implementation must exclusively use `api/chat` for routing, `ChatService` for application logic, and `ChatInput` for payload schemas to prevent structural duplication. Handled deterministically in Phase 1 via the decoupled `MockAIProvider`.

## Naming Alignment
- Keep this glossary aligned with naming decisions in `../.rule/naming-rules.md`.
- Ensure all API JSON payloads, TypeScript types, and Python Pydantic models use these exact terms strictly (e.g., `course_id`, `lesson_id`, `chat`).

## Update Rules
- Add new terms here when introducing a new bounded context, entity, or shared API concept in future phases (e.g., Phase 2 portfolio features).
- Avoid synonyms for existing terms (do not mix `course` with `syllabus` or `lesson` with `unit`) to protect the Agent from logical duplication.