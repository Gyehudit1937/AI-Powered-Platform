# Product Definition

## Purpose
- Define shared product intent so planning, architecture, and delivery stay aligned.

## Product Vision
- To build the ultimate AI-driven educational ecosystem that transforms aspiring developers into production-ready software engineers. The platform acts as an active, hyper-personalized mentor that dynamically adapts learning paths, generates bespoke portfolios based on personal hobbies, conducts realistic technical interviews with grading, and crafts customized cheat sheets based on individual friction points.

## User Roles
### Student
- Browse and learn active courses based on modular sections and lessons.
- Interact with the contextual AI Mentor (The Course Navigator).
- Track learning velocity, quiz scores, and career preparation milestones.

### Admin
- Create, manage, and structure courses, sections, and lessons.
- Review global user analytics and pinpoint concept bottlenecks.
- Manage prompt weights and system-wide configurations.
- **Note:** Admin capabilities are defined for future vision only and are strictly NOT implemented in Phase 1 MVP.

## Target Users
- Primary users:
	- Aspiring software developers and tech students looking for an accelerated, practical path to their first tech role.
	- Learners seeking instant, contextual code debugging and mentor-level guidance.
- Secondary users:
	- Instructors and community managers tracking student progress, velocity, and core conceptual bottlenecks.

## Problem Statement
- Traditional coding platforms offer generic, static curricula where students easily get stuck on minor syntax or logical errors without immediate help. Furthermore, students graduate with identical portfolio projects, fail behavioral and technical interviews due to a lack of realistic simulation, and struggle to bridge the gap between abstract tutorials and live market job requirements.

## Value Proposition
- **The Course Navigator:** Real-time, contextual AI assistance with scaffolded hints instead of direct answers to ensure genuine learning.
- **The Portfolio Architect:** GenAI engineering that blends target technologies with user hobbies to create 100% unique production-grade repositories.
- **The Technical Interviewer:** A rigorous simulation module that interviews users, analyzes code submissions, delivers industry-standard grades, and uncovers gaps.
- **The Custom Codex (Cheat Sheets):** Background compilation of user errors and chat interactions into beautifully formatted, high-value PDF cheat sheets focusing strictly on their weak areas.

## Product Scope
- In scope (Long-term Target Architecture):
	- High-performance Python (FastAPI) backend coupled with a responsive React (TypeScript) frontend workspace.
	- Clean architectural separation: Router -> Service -> AI Provider Abstraction Layer (`BaseAIProvider`).
	- Live bidirectional chat interaction passing explicit context parameters (`course_id`, `lesson_id`, `student_level`).
- Out of scope (MVP Stage):
	- Payment gateways/billing pipelines, multi-tenant video streaming servers, third-party live job scraping APIs, and live AI provider APIs (OpenAI/Gemini).

## Phase 1 MVP (Strict Boundary)
To maintain velocity and avoid agent scope-creep, Phase 1 focuses exclusively on the core interface loop using local data. The Agent must not implement advanced generative features or admin panels yet.
- **Course List:** Simple dashboard showing available structured content.
- **Course Details:** Overview of sections and navigation layout.
- **Lesson Viewer:** Dedicated content layout to read/consume a specific lesson block.
- **Progress Tracking:** In-memory retention utilizing the explicit Progress Model structure.
- **Mock AI Chat:** Full client-server messaging loop using a predictable `MockAIProvider` simulation.
- **In-Memory Data Storage:** Localized python dictionaries simulating database state with explicit Seed Data requirements.
- **Note:** Phase 1 uses a `MockAIProvider` implementation. Real Gemini/OpenAI providers will be introduced in Phase 2.

## Phase 1 API Contract & Endpoints
The backend must expose exactly these endpoints with stable JSON contract definitions:
- `GET /api/courses` - Returns a list of available basic Course models (for the dashboard).
- `GET /api/courses/{course_id}` - Returns a nested `CourseDetail` response containing fully embedded sections and lessons.
- `GET /api/progress` - Returns the progress model for the single active user.
- `POST /api/progress` - Updates user progress. Payload must strictly contain only `{ "current_lesson_id": "string" }`. The backend service must automatically derive `current_section_id` and `current_course_id`, update the state, and dynamically recalculates `completion_percentage`.
- `POST /api/chat` - Submits a question and receives a context-aware simulated mentor response.

## Phase 1 Data Models & Pydantic Schemas
The Agent must implement explicit model fields exactly as structured below:

### Course Model (Summary)
- `id`: string
- `title`: string
- `description`: string
- `image_url`: string

### Lesson Model
- `id`: string
- `section_id`: string
- `title`: string
- `content`: string (Markdown support)
- `order`: integer

### Section Model (With Embedded Lessons)
- `id`: string
- `course_id`: string
- `title`: string
- `order`: integer
- `lessons`: List of Lesson Models

### CourseDetail Model (Nested Response for GET /api/courses/{id})
- `id`: string
- `title`: string
- `description`: string
- `image_url`: string
- `sections`: List of Section Models

### Progress Model
- `user_id`: string (defaulted to "default_user" for Phase 1 simulation)
- `current_course_id`: string
- `current_section_id`: string
- `current_lesson_id`: string
- `completion_percentage`: float

### Chat Input Payload
- `user_message`: string
- `course_id`: string
- `lesson_id`: string
- `student_level`: string ('beginner' | 'intermediate' | 'advanced')

## Phase 1 Seed Data Requirements
The in-memory dictionary must contain a pre-populated baseline dataset to thoroughly validate navigation and UI rendering. The absolute minimum requirement is:
- **Minimum 1 active course.**
- **Minimum 2 sections within that course.**
- **Minimum 3 lessons structured within each section.**

## MockAIProvider Implementation Specification
The `MockAIProvider` must not return a static string. It should simulate an expert mentor loop by using a structured dictionary lookup or conditional mapping:
- If `user_message` contains keywords like "error", "bug", or "help", return a scaffolded hint tailored to the `lesson_id` content without giving the direct answer.
- Echo back contextual parameter validations like: `[Level: {student_level}]` or `[Context: {lesson_id}]` embedded gracefully into natural-sounding Hebrew text responses.

## Future Phases
### Phase 2: Live Core & Cost Optimization
- Gemini/OpenAI Concrete Integration via `BaseAIProvider`.
- **Semantic Caching Layer:** Implement background vector lookup via `pgvector` to intercept repetitive student queries and minimize LLM API costs.
- Portfolio Architect (Basic core flow).
- **Performance Optimization:** Split the embedded `CourseDetail` response. Introduce `GET /api/lessons/{lesson_id}` to fetch full Markdown content lazily and lighten the initial course load payload.

### Phase 3: Advanced Simulations & Tooling
- Technical Interview Simulator (Text-Based).
- **Voice-Mode Upgrade:** Evaluate Speech-to-Text (STT) web integrations for verbal interview simulations.
- Personalized Cheat Sheets generation engine (Custom Codex).
- Job Pipeline Exploration: Pivot from strict LinkedIn APIs toward resilient alternative aggregators (e.g., Jooble, Adzuna) or controlled local scrapers to bypass rate limits.

### Phase 4: Analytics, Community, and Scale
- **Analytical Progress Dashboard:** Track metrics including average completion time, concept drop-off coordinates, and AI response effectiveness.
- **AI Peer Matching Engine:** Automated dynamically composed "study groups" matching students based on velocity, calendar availability, and conceptual alignment.
- Job Matching Engine and automated resume optimization tracking.

## Technology Stack (Phase 1)
### Frontend Stack
- React
- Vite
- TypeScript
- React Router
- Material UI

### Backend Stack
- Python
- FastAPI (Must include CORSMiddleware configured to allow communication from the Frontend port)
- Uvicorn
- Pydantic

## Course & Content Structure
- **Course**: Top-level curriculum identity.
- **Sections**: Modular chapters splitting core domain concepts.
- **Lessons**: Individual theory, video reference, or workspace text elements.
- **Exercises**: Interactive code tasks or syntax trials.
- **Quiz**: Validation blocks for checkpoint testing.
- **Resources**: External links, reading lists, or file downloads.

## Chat Context Rules
- The chat engine must consume and inject the following parameters into the system window simulation on every request:
  - `course_context`: Metadata details of the active course.
  - `lesson_context`: Exact text content/errors from the current active lesson.
  - `student_level`: Experience indicator (Beginner, Intermediate, Advanced) to adapt explanation depth.

## Success Metrics
- Product metrics:
	- System Latency: Mock server response time under 500ms.
	- Code Quality: Consistent TypeScript typing and reusable component architecture.
	- Reliability: Zero unhandled exceptions across API boundaries.

## Constraints and Assumptions
- Technical: Completely stateless database-free simulation for Phase 1 using robust in-memory data structures.
- Code Quality: Strictly obey `coding-rules.md`—absolutely **no trailing semicolons** across the entire JavaScript/TypeScript architecture.
- Resiliency: Adhere strictly to `error-handling-rules.md` by failing fast and returning machine-readable JSON structures instead of leaky provider stack traces.

## Prioritization Rules
- Prioritize work that most improves user outcomes and core metrics.
- Secure and stabilize the Client-Server pipeline first using the decoupled `BaseAIProvider`.
- Absolutely forbid any expansion into automatic portfolio generation, admin dashboards, resume scanners, or interview simulators until Phase 1 MVP is flawless.