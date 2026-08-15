# System Architecture

## Context
- High-performance, lightweight, and completely decoupled educational simulator for Phase 1 MVP.
- **Core Constraint:** 100% database-free and stateless execution utilizing structured in-memory dictionaries with zero unhandled exceptions across boundaries.

## Primary Components & Structural Boundaries

### 1. Client Architecture (Frontend Workspace)
- **Technology Stack:** React, Vite, TypeScript, React Router, Material UI.
- **State & Navigation Management:** Simple, top-level context or custom hook state holding the active `Progress Model`.
- **Code Enforcement:** Absolutely no trailing semicolons across any client-side file.

### 2. Server Architecture (Backend Layers)
The Python (FastAPI) layer enforces a strict architectural separation of concerns:
- **API Layer (Routers):** Exposes explicit HTTP endpoints (`/api/courses`, `/api/progress`, `/api/chat`), validates incoming contracts using Pydantic, and handles CORS configurations. Implements a "Fail Fast" mechanism.
- **Application Layer (Services):** Coordinates data state and business logic.
  - `CourseService`: Reads static course curriculum and structures from the central database simulation.
  - `ProgressService`: Calculates structural navigation and percentage completion logic. **Strict Dependency:** Enforces a one-way dependency on `CourseService` to fetch total lesson counts for percentage calculations (avoids circular imports).
  - `ChatService`: Orchestrates prompt contextualization and interacts with the AI abstraction layer.
- **Infrastructure Layer (Providers):** Interacts exclusively with a decoupled `BaseAIProvider` abstraction.

## Centralized In-Memory Data Storage (Source of Truth)
To prevent data duplication and guarantee a single source of truth, all Phase 1 runtime simulation data resides in a dedicated repository module:
- **Location:** `server/data/store.py`
- **Static Seed Data:** Holds the hardcoded dictionary containing a minimum of 1 course, 2 sections, and 3 lessons per section.
- **Global Runtime State:** Stores the active user's progress utilizing a single module-level dictionary (`Progress Model`). In Python, this module-level state acts as a singleton, ensuring both `GET` and `POST` progress operations share and mutate the exact same in-memory instance.

## Component Flow & Data Boundaries

```text
React Frontend Layout (Workspace Browser)
       │
       ▼ (Valid JSON Payload via Fetch API / Axios)
FastAPI API Router [API Layer] (Validates via Pydantic Schemas)
       │
       ▼ (Passes Primitive Attributes / Explicit Schemas)
Application Domain Services [Application Layer] 
       │ (ProgressService invokes CourseService internally for total counts)
       ▼ (Reads/Writes to central Module-Level Singleton: server/data/store.py)
Central In-Memory Storage & Decoupled MockAIProvider