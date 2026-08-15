COURSES_DB: dict = {
    "course-04": {
        "id": "course-04",
        "title": "Git & GitHub for Teams",
        "description": "Master version control workflows, branching strategies, pull requests, and CI/CD pipelines used in real dev teams.",
        "image_url": "https://placehold.co/600x340/f57c00/ffffff?text=Git+%26+GitHub",
        "sections": {
            "section-07": {
                "id": "section-07",
                "course_id": "course-04",
                "title": "Git Core Concepts",
                "order": 1,
                "lessons": {
                    "lesson-07-01": {
                        "id": "lesson-07-01",
                        "section_id": "section-07",
                        "title": "Commits, Staging & History",
                        "order": 1,
                        "content": "# Commits, Staging & History\n\nGit tracks changes in three areas:\n\n- **Working Directory** — your local file edits\n- **Staging Area (Index)** — changes marked for the next commit\n- **Repository** — committed history\n\n```bash\ngit add src/app.py      # stage a specific file\ngit commit -m 'feat: add login route'\ngit log --oneline       # compact history view\n```",
                    },
                    "lesson-07-02": {
                        "id": "lesson-07-02",
                        "section_id": "section-07",
                        "title": "Branching & Merging",
                        "order": 2,
                        "content": "# Branching & Merging\n\nBranches let you work in isolation without affecting `main`.\n\n```bash\ngit checkout -b feature/auth   # create and switch\ngit merge feature/auth          # merge into current branch\ngit branch -d feature/auth      # delete after merge\n```\n\n## Fast-Forward vs. 3-Way Merge\n- **Fast-forward:** no divergence — Git simply moves the pointer.\n- **3-way merge:** branches diverged — Git creates a merge commit.",
                    },
                    "lesson-07-03": {
                        "id": "lesson-07-03",
                        "section_id": "section-07",
                        "title": "Rebase & Cherry-Pick",
                        "order": 3,
                        "content": "# Rebase & Cherry-Pick\n\n`rebase` replays your commits on top of another branch — keeps history linear.\n\n```bash\ngit rebase main            # replay current branch on top of main\ngit cherry-pick a1b2c3d   # apply a single commit to current branch\n```\n\n> Never rebase commits already pushed to a shared branch.",
                    },
                },
            },
            "section-08": {
                "id": "section-08",
                "course_id": "course-04",
                "title": "GitHub Workflows",
                "order": 2,
                "lessons": {
                    "lesson-08-01": {
                        "id": "lesson-08-01",
                        "section_id": "section-08",
                        "title": "Pull Requests & Code Review",
                        "order": 1,
                        "content": "# Pull Requests & Code Review\n\nA PR proposes changes from one branch into another and triggers a review process.\n\n## Good PR Hygiene\n- Keep PRs small and focused on a single concern.\n- Write a clear description: *what* changed and *why*.\n- Link to the related issue.\n\n## Review Etiquette\n- Comment on the code, not the person.\n- Use *Suggest Changes* for minor fixes.",
                    },
                    "lesson-08-02": {
                        "id": "lesson-08-02",
                        "section_id": "section-08",
                        "title": "GitHub Actions CI/CD",
                        "order": 2,
                        "content": "# GitHub Actions CI/CD\n\nAutomate tests and deployments on every push.\n\n```yaml\nname: CI\non: [push, pull_request]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with: { python-version: '3.12' }\n      - run: pip install -r requirements.txt\n      - run: pytest\n```",
                    },
                    "lesson-08-03": {
                        "id": "lesson-08-03",
                        "section_id": "section-08",
                        "title": "Branch Protection & Secrets",
                        "order": 3,
                        "content": "# Branch Protection & Secrets\n\n## Branch Protection Rules\n- Require PR reviews before merging to `main`.\n- Require status checks (CI) to pass.\n- Restrict force-pushes.\n\n## Managing Secrets\n- Store API keys in **GitHub Secrets** (Settings → Secrets).\n- Reference in workflows: `${{ secrets.API_KEY }}`.\n- Never commit secrets to the repository.",
                    },
                },
            },
        },
    },
    "course-05": {
        "id": "course-05",
        "title": "CSS & UI Design Fundamentals",
        "description": "Go from zero to confident UI developer. Master Flexbox, Grid, animations, and design systems.",
        "image_url": "https://placehold.co/600x340/7b1fa2/ffffff?text=CSS+%26+UI+Design",
        "sections": {
            "section-09": {
                "id": "section-09",
                "course_id": "course-05",
                "title": "Layout Systems",
                "order": 1,
                "lessons": {
                    "lesson-09-01": {
                        "id": "lesson-09-01",
                        "section_id": "section-09",
                        "title": "Flexbox Mastery",
                        "order": 1,
                        "content": "# Flexbox Mastery\n\nFlexbox is a one-dimensional layout system (row OR column).\n\n```css\n.container {\n  display: flex;\n  justify-content: space-between; /* main axis */\n  align-items: center;            /* cross axis */\n  gap: 16px;\n}\n```\n\n## Key Properties\n- `flex-grow` — how much extra space an item takes.\n- `flex-shrink` — how much an item shrinks.\n- `flex-basis` — the item's ideal starting size.",
                    },
                    "lesson-09-02": {
                        "id": "lesson-09-02",
                        "section_id": "section-09",
                        "title": "CSS Grid",
                        "order": 2,
                        "content": "# CSS Grid\n\nGrid is a two-dimensional layout system (rows AND columns simultaneously).\n\n```css\n.grid {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 24px;\n}\n\n.featured {\n  grid-column: span 2; /* takes 2 columns */\n}\n```\n\nUse Grid for page-level layout; use Flexbox for component-level alignment.",
                    },
                    "lesson-09-03": {
                        "id": "lesson-09-03",
                        "section_id": "section-09",
                        "title": "Responsive Design & Media Queries",
                        "order": 3,
                        "content": "# Responsive Design & Media Queries\n\n## Mobile-First Approach\nWrite base styles for mobile, then add complexity for larger screens.\n\n```css\n.card { font-size: 14px; }\n\n@media (min-width: 768px) {\n  .card { font-size: 16px; }\n}\n\n@media (min-width: 1200px) {\n  .card { font-size: 18px; }\n}\n```\n\nUse `rem` units for scalable typography.",
                    },
                },
            },
            "section-10": {
                "id": "section-10",
                "course_id": "course-05",
                "title": "Design Systems",
                "order": 2,
                "lessons": {
                    "lesson-10-01": {
                        "id": "lesson-10-01",
                        "section_id": "section-10",
                        "title": "Design Tokens & Variables",
                        "order": 1,
                        "content": "# Design Tokens & Variables\n\nDesign tokens are the smallest reusable design decisions (colors, spacing, font sizes).\n\n```css\n:root {\n  --color-primary: #1976d2;\n  --color-surface: #ffffff;\n  --spacing-md: 16px;\n  --radius-md: 8px;\n  --font-body: 'Inter', sans-serif;\n}\n\n.button {\n  background: var(--color-primary);\n  padding: var(--spacing-md);\n  border-radius: var(--radius-md);\n}\n```",
                    },
                    "lesson-10-02": {
                        "id": "lesson-10-02",
                        "section_id": "section-10",
                        "title": "CSS Animations & Transitions",
                        "order": 2,
                        "content": "# CSS Animations & Transitions\n\n## Transitions\nSmooth change between two states.\n```css\n.button {\n  transition: background 0.2s ease, transform 0.15s ease;\n}\n.button:hover {\n  background: #1565c0;\n  transform: translateY(-2px);\n}\n```\n\n## Keyframe Animations\n```css\n@keyframes fadeIn {\n  from { opacity: 0; transform: translateY(8px); }\n  to   { opacity: 1; transform: translateY(0); }\n}\n.card { animation: fadeIn 0.3s ease forwards; }\n```",
                    },
                    "lesson-10-03": {
                        "id": "lesson-10-03",
                        "section_id": "section-10",
                        "title": "Typography & Color Theory",
                        "order": 3,
                        "content": "# Typography & Color Theory\n\n## Type Scale\nUse a consistent modular scale: 12 / 14 / 16 / 20 / 24 / 32 / 48px.\n\n## Color Roles\n- **Primary** — main brand action (buttons, links)\n- **Surface** — background of cards and panels\n- **On-Surface** — text placed on surfaces\n- **Error / Success / Warning** — semantic states\n\n## Contrast\nEnsure at least **4.5:1** contrast ratio for body text (WCAG AA).",
                    },
                },
            },
        },
    },
    "course-06": {
        "id": "course-06",
        "title": "Algorithms & Data Structures",
        "description": "Ace technical interviews and write efficient code. Covers sorting, trees, graphs, dynamic programming and more.",
        "image_url": "https://placehold.co/600x340/c62828/ffffff?text=Algorithms+%26+DSA",
        "sections": {
            "section-11": {
                "id": "section-11",
                "course_id": "course-06",
                "title": "Core Data Structures",
                "order": 1,
                "lessons": {
                    "lesson-11-01": {
                        "id": "lesson-11-01",
                        "section_id": "section-11",
                        "title": "Arrays & Hash Maps",
                        "order": 1,
                        "content": "# Arrays & Hash Maps\n\n## Arrays\n- O(1) read by index, O(n) search.\n- Best for ordered, fixed-size collections.\n\n## Hash Maps\n- O(1) average insert, lookup, delete.\n- Python: `dict`. JS: `Map` or plain object.\n\n```python\n# Two-Sum using a hash map — O(n)\ndef two_sum(nums, target):\n    seen = {}\n    for i, n in enumerate(nums):\n        complement = target - n\n        if complement in seen:\n            return [seen[complement], i]\n        seen[n] = i\n```",
                    },
                    "lesson-11-02": {
                        "id": "lesson-11-02",
                        "section_id": "section-11",
                        "title": "Stacks & Queues",
                        "order": 2,
                        "content": "# Stacks & Queues\n\n## Stack — LIFO\n```python\nstack = []\nstack.append(1)   # push\nstack.pop()       # pop  → O(1)\n```\nUse for: undo history, DFS, balanced parentheses.\n\n## Queue — FIFO\n```python\nfrom collections import deque\nq = deque()\nq.append(1)       # enqueue\nq.popleft()       # dequeue → O(1)\n```\nUse for: BFS, task scheduling.",
                    },
                    "lesson-11-03": {
                        "id": "lesson-11-03",
                        "section_id": "section-11",
                        "title": "Binary Trees & BST",
                        "order": 3,
                        "content": "# Binary Trees & BST\n\nA **Binary Search Tree** satisfies: left child < node < right child.\n\n```python\nclass Node:\n    def __init__(self, val):\n        self.val = val\n        self.left = self.right = None\n\ndef inorder(node):\n    if node:\n        inorder(node.left)\n        print(node.val)\n        inorder(node.right)\n```\n\n## Complexities (Balanced BST)\n- Search, Insert, Delete: O(log n)\n- Worst case (skewed): O(n)",
                    },
                },
            },
            "section-12": {
                "id": "section-12",
                "course_id": "course-06",
                "title": "Sorting & Searching",
                "order": 2,
                "lessons": {
                    "lesson-12-01": {
                        "id": "lesson-12-01",
                        "section_id": "section-12",
                        "title": "Binary Search",
                        "order": 1,
                        "content": "# Binary Search\n\nFind a value in a **sorted** array in O(log n).\n\n```python\ndef binary_search(arr, target):\n    lo, hi = 0, len(arr) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1\n```\n\nAlways ask: *is the input sorted?* If yes, think binary search first.",
                    },
                    "lesson-12-02": {
                        "id": "lesson-12-02",
                        "section_id": "section-12",
                        "title": "Merge Sort & Quick Sort",
                        "order": 2,
                        "content": "# Merge Sort & Quick Sort\n\n## Merge Sort — O(n log n) guaranteed\n- Divide array in half, sort each half, merge.\n- Stable sort. Uses O(n) extra space.\n\n## Quick Sort — O(n log n) average\n- Pick a pivot, partition around it, recurse.\n- In-place, O(log n) stack space.\n- Worst case O(n²) with bad pivot choice.\n\n**Interview rule:** Default to Merge Sort when stability matters; Quick Sort for raw speed.",
                    },
                    "lesson-12-03": {
                        "id": "lesson-12-03",
                        "section_id": "section-12",
                        "title": "Dynamic Programming Intro",
                        "order": 3,
                        "content": "# Dynamic Programming Intro\n\nDP solves problems by breaking them into overlapping subproblems and caching results.\n\n## Fibonacci — Naive O(2ⁿ) → DP O(n)\n```python\ndef fib(n, memo={}):\n    if n <= 1: return n\n    if n not in memo:\n        memo[n] = fib(n-1) + fib(n-2)\n    return memo[n]\n```\n\n## When to use DP\n- Optimal substructure: optimal solution built from optimal sub-solutions.\n- Overlapping subproblems: same sub-problems computed multiple times.",
                    },
                },
            },
        },
    },
    "course-02": {
        "id": "course-02",
        "title": "React & TypeScript Mastery",
        "description": "Build modern, type-safe web applications with React 18, TypeScript, and the latest ecosystem tools.",
        "image_url": "https://placehold.co/600x340/0288d1/ffffff?text=React+%26+TypeScript",
        "sections": {
            "section-03": {
                "id": "section-03",
                "course_id": "course-02",
                "title": "TypeScript Foundations",
                "order": 1,
                "lessons": {
                    "lesson-03-01": {
                        "id": "lesson-03-01",
                        "section_id": "section-03",
                        "title": "Types, Interfaces & Generics",
                        "order": 1,
                        "content": (
                            "# Types, Interfaces & Generics\n\n"
                            "TypeScript adds a static type layer on top of JavaScript.\n\n"
                            "```typescript\n"
                            "interface User {\n"
                            "  id: number\n"
                            "  name: string\n"
                            "  role: 'admin' | 'student'\n"
                            "}\n\n"
                            "function identity<T>(value: T): T {\n"
                            "  return value\n"
                            "}\n"
                            "```\n\n"
                            "Generics let you write reusable, type-safe utilities without sacrificing flexibility."
                        ),
                    },
                    "lesson-03-02": {
                        "id": "lesson-03-02",
                        "section_id": "section-03",
                        "title": "Type Narrowing & Guards",
                        "order": 2,
                        "content": (
                            "# Type Narrowing & Guards\n\n"
                            "TypeScript narrows union types inside conditional blocks automatically.\n\n"
                            "```typescript\n"
                            "type Result = { ok: true; data: string } | { ok: false; error: string }\n\n"
                            "function handle(result: Result) {\n"
                            "  if (result.ok) {\n"
                            "    console.log(result.data)   // string\n"
                            "  } else {\n"
                            "    console.error(result.error) // string\n"
                            "  }\n"
                            "}\n"
                            "```"
                        ),
                    },
                    "lesson-03-03": {
                        "id": "lesson-03-03",
                        "section_id": "section-03",
                        "title": "Utility Types",
                        "order": 3,
                        "content": (
                            "# Utility Types\n\n"
                            "TypeScript ships with built-in mapped types that transform existing types.\n\n"
                            "```typescript\n"
                            "interface Course {\n"
                            "  id: string\n"
                            "  title: string\n"
                            "  published: boolean\n"
                            "}\n\n"
                            "type CoursePreview = Pick<Course, 'id' | 'title'>\n"
                            "type DraftCourse   = Partial<Course>\n"
                            "type ReadonlyCourse = Readonly<Course>\n"
                            "```\n\n"
                            "These patterns keep types DRY and prevent accidental mutation."
                        ),
                    },
                },
            },
            "section-04": {
                "id": "section-04",
                "course_id": "course-02",
                "title": "React 18 Patterns",
                "order": 2,
                "lessons": {
                    "lesson-04-01": {
                        "id": "lesson-04-01",
                        "section_id": "section-04",
                        "title": "useState & useReducer",
                        "order": 1,
                        "content": (
                            "# useState & useReducer\n\n"
                            "Use `useState` for simple values and `useReducer` for complex state machines.\n\n"
                            "```typescript\n"
                            "type Action = { type: 'increment' } | { type: 'reset' }\n\n"
                            "function reducer(state: number, action: Action): number {\n"
                            "  switch (action.type) {\n"
                            "    case 'increment': return state + 1\n"
                            "    case 'reset':     return 0\n"
                            "  }\n"
                            "}\n\n"
                            "const [count, dispatch] = useReducer(reducer, 0)\n"
                            "```"
                        ),
                    },
                    "lesson-04-02": {
                        "id": "lesson-04-02",
                        "section_id": "section-04",
                        "title": "useEffect & Data Fetching",
                        "order": 2,
                        "content": (
                            "# useEffect & Data Fetching\n\n"
                            "`useEffect` runs after render. Always clean up subscriptions.\n\n"
                            "```typescript\n"
                            "useEffect(() => {\n"
                            "  let active = true\n\n"
                            "  fetch('/api/courses')\n"
                            "    .then(r => r.json())\n"
                            "    .then(data => { if (active) setCourses(data) })\n\n"
                            "  return () => { active = false }\n"
                            "}, [])\n"
                            "```\n\n"
                            "The `active` flag prevents state updates on unmounted components."
                        ),
                    },
                    "lesson-04-03": {
                        "id": "lesson-04-03",
                        "section_id": "section-04",
                        "title": "Custom Hooks",
                        "order": 3,
                        "content": (
                            "# Custom Hooks\n\n"
                            "Extract reusable stateful logic into functions prefixed with `use`.\n\n"
                            "```typescript\n"
                            "function useFetch<T>(url: string) {\n"
                            "  const [data, setData] = useState<T | null>(null)\n"
                            "  const [loading, setLoading] = useState(true)\n\n"
                            "  useEffect(() => {\n"
                            "    fetch(url).then(r => r.json()).then(setData).finally(() => setLoading(false))\n"
                            "  }, [url])\n\n"
                            "  return { data, loading }\n"
                            "}\n"
                            "```"
                        ),
                    },
                },
            },
        },
    },
    "course-03": {
        "id": "course-03",
        "title": "System Design for Developers",
        "description": "Learn how to design scalable, fault-tolerant distributed systems — from databases to load balancers.",
        "image_url": "https://placehold.co/600x340/388e3c/ffffff?text=System+Design",
        "sections": {
            "section-05": {
                "id": "section-05",
                "course_id": "course-03",
                "title": "Core Concepts",
                "order": 1,
                "lessons": {
                    "lesson-05-01": {
                        "id": "lesson-05-01",
                        "section_id": "section-05",
                        "title": "Scalability vs. Performance",
                        "order": 1,
                        "content": (
                            "# Scalability vs. Performance\n\n"
                            "- **Performance** is about making a single request faster.\n"
                            "- **Scalability** is about handling more requests without degradation.\n\n"
                            "## Vertical vs. Horizontal Scaling\n"
                            "- **Vertical (scale up):** Bigger machine — more CPU, RAM. Simple but has a ceiling.\n"
                            "- **Horizontal (scale out):** More machines. Requires stateless services and a load balancer."
                        ),
                    },
                    "lesson-05-02": {
                        "id": "lesson-05-02",
                        "section_id": "section-05",
                        "title": "CAP Theorem",
                        "order": 2,
                        "content": (
                            "# CAP Theorem\n\n"
                            "A distributed system can guarantee at most **2 of 3** properties:\n\n"
                            "- **C**onsistency — every read returns the latest write.\n"
                            "- **A**vailability — every request gets a response (not necessarily latest).\n"
                            "- **P**artition Tolerance — the system works even when nodes can't communicate.\n\n"
                            "In practice, network partitions happen — so you choose between **CP** or **AP**."
                        ),
                    },
                    "lesson-05-03": {
                        "id": "lesson-05-03",
                        "section_id": "section-05",
                        "title": "Load Balancers",
                        "order": 3,
                        "content": (
                            "# Load Balancers\n\n"
                            "A load balancer distributes incoming traffic across multiple servers.\n\n"
                            "## Common Strategies\n"
                            "- **Round Robin** — requests cycle through servers in order.\n"
                            "- **Least Connections** — routes to the server with fewest active connections.\n"
                            "- **IP Hash** — same client IP always hits the same server (useful for sessions).\n\n"
                            "## Layer 4 vs. Layer 7\n"
                            "- **L4** operates on TCP/UDP — fast, no content inspection.\n"
                            "- **L7** operates on HTTP — can route by URL path, headers, or cookies."
                        ),
                    },
                },
            },
            "section-06": {
                "id": "section-06",
                "course_id": "course-03",
                "title": "Data Storage Strategies",
                "order": 2,
                "lessons": {
                    "lesson-06-01": {
                        "id": "lesson-06-01",
                        "section_id": "section-06",
                        "title": "SQL vs. NoSQL",
                        "order": 1,
                        "content": (
                            "# SQL vs. NoSQL\n\n"
                            "## SQL (Relational)\n"
                            "- Structured schema, ACID transactions, powerful joins.\n"
                            "- Best for: financial systems, ERP, anything requiring strong consistency.\n\n"
                            "## NoSQL\n"
                            "- Flexible schema, horizontal scaling, eventual consistency.\n"
                            "- Types: Document (MongoDB), Key-Value (Redis), Column (Cassandra), Graph (Neo4j).\n\n"
                            "## Rule of Thumb\n"
                            "Start with SQL. Switch to NoSQL only when you have a concrete scaling problem SQL cannot solve."
                        ),
                    },
                    "lesson-06-02": {
                        "id": "lesson-06-02",
                        "section_id": "section-06",
                        "title": "Caching Strategies",
                        "order": 2,
                        "content": (
                            "# Caching Strategies\n\n"
                            "Caching reduces latency and database load by storing computed results.\n\n"
                            "## Patterns\n"
                            "- **Cache-Aside:** App checks cache first; on miss, loads from DB and populates cache.\n"
                            "- **Write-Through:** Write to cache and DB simultaneously.\n"
                            "- **Write-Behind:** Write to cache immediately; sync to DB asynchronously.\n\n"
                            "## Eviction Policies\n"
                            "- **LRU** (Least Recently Used) — most common, good general purpose.\n"
                            "- **TTL** (Time To Live) — expire entries after a fixed duration."
                        ),
                    },
                    "lesson-06-03": {
                        "id": "lesson-06-03",
                        "section_id": "section-06",
                        "title": "Database Sharding",
                        "order": 3,
                        "content": (
                            "# Database Sharding\n\n"
                            "Sharding splits a large dataset across multiple database nodes (shards).\n\n"
                            "## Shard Key Selection\n"
                            "The shard key determines which node stores each row. A poor key causes **hotspots**.\n\n"
                            "- **Good key:** `user_id` — distributes writes evenly across shards.\n"
                            "- **Bad key:** `created_at` — all new writes hit the same shard (time-based hotspot).\n\n"
                            "## Downsides\n"
                            "- Cross-shard joins are expensive or impossible.\n"
                            "- Re-sharding is painful — plan the key carefully upfront."
                        ),
                    },
                },
            },
        },
    },
    "course-01": {
        "id": "course-01",
        "id": "course-01",
        "title": "Full-Stack Python Bootcamp",
        "description": "Master Python, FastAPI, and React from zero to production-ready developer.",
        "image_url": "https://placehold.co/600x340/1976d2/ffffff?text=Python+Bootcamp",
        "sections": {
            "section-01": {
                "id": "section-01",
                "course_id": "course-01",
                "title": "Python Fundamentals",
                "order": 1,
                "lessons": {
                    "lesson-01-01": {
                        "id": "lesson-01-01",
                        "section_id": "section-01",
                        "title": "Variables & Data Types",
                        "order": 1,
                        "content": (
                            "# Variables & Data Types\n\n"
                            "In Python every value has a type. The most common built-in types are:\n\n"
                            "```python\n"
                            "name: str = 'Alice'\n"
                            "age: int = 30\n"
                            "height: float = 1.72\n"
                            "is_student: bool = True\n"
                            "```\n\n"
                            "Python infers the type at runtime, but using type hints makes the code self-documenting "
                            "and enables static analysis tools like `mypy`.\n\n"
                            "## Key Rules\n"
                            "- Variable names are `snake_case`.\n"
                            "- Use `=` for assignment, `:` for type annotations.\n"
                            "- Strings can use single or double quotes — be consistent."
                        ),
                    },
                    "lesson-01-02": {
                        "id": "lesson-01-02",
                        "section_id": "section-01",
                        "title": "Control Flow: if / elif / else",
                        "order": 2,
                        "content": (
                            "# Control Flow\n\n"
                            "Python uses indentation (4 spaces) to define code blocks — no braces needed.\n\n"
                            "```python\n"
                            "score = 85\n\n"
                            "if score >= 90:\n"
                            "    grade = 'A'\n"
                            "elif score >= 80:\n"
                            "    grade = 'B'\n"
                            "else:\n"
                            "    grade = 'C'\n\n"
                            "print(grade)  # B\n"
                            "```\n\n"
                            "## Ternary Expression\n"
                            "```python\n"
                            "label = 'pass' if score >= 60 else 'fail'\n"
                            "```"
                        ),
                    },
                    "lesson-01-03": {
                        "id": "lesson-01-03",
                        "section_id": "section-01",
                        "title": "Functions & Scope",
                        "order": 3,
                        "content": (
                            "# Functions & Scope\n\n"
                            "Functions are defined with `def` and support default arguments, *args, and **kwargs.\n\n"
                            "```python\n"
                            "def greet(name: str, greeting: str = 'Hello') -> str:\n"
                            "    return f'{greeting}, {name}!'\n\n"
                            "print(greet('Bob'))           # Hello, Bob!\n"
                            "print(greet('Bob', 'Shalom')) # Shalom, Bob!\n"
                            "```\n\n"
                            "## Scope Rules (LEGB)\n"
                            "Python resolves names in this order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in."
                        ),
                    },
                },
            },
            "section-02": {
                "id": "section-02",
                "course_id": "course-01",
                "title": "FastAPI Essentials",
                "order": 2,
                "lessons": {
                    "lesson-02-01": {
                        "id": "lesson-02-01",
                        "section_id": "section-02",
                        "title": "Your First FastAPI App",
                        "order": 1,
                        "content": (
                            "# Your First FastAPI App\n\n"
                            "FastAPI is a modern, high-performance web framework built on top of Starlette and Pydantic.\n\n"
                            "```python\n"
                            "from fastapi import FastAPI\n\n"
                            "app = FastAPI()\n\n"
                            "@app.get('/')\n"
                            "def root():\n"
                            "    return {'message': 'Hello World'}\n"
                            "```\n\n"
                            "Run with:\n"
                            "```bash\n"
                            "uvicorn main:app --reload\n"
                            "```\n\n"
                            "Visit `http://localhost:8000/docs` for the auto-generated Swagger UI."
                        ),
                    },
                    "lesson-02-02": {
                        "id": "lesson-02-02",
                        "section_id": "section-02",
                        "title": "Path & Query Parameters",
                        "order": 2,
                        "content": (
                            "# Path & Query Parameters\n\n"
                            "FastAPI automatically parses and validates parameters from the URL.\n\n"
                            "```python\n"
                            "@app.get('/items/{item_id}')\n"
                            "def get_item(item_id: int, q: str | None = None):\n"
                            "    return {'item_id': item_id, 'query': q}\n"
                            "```\n\n"
                            "- `item_id` is a **path parameter** — declared in the route string.\n"
                            "- `q` is a **query parameter** — appended to the URL: `?q=search`.\n"
                            "- Pydantic validates types automatically; invalid input returns HTTP 422."
                        ),
                    },
                    "lesson-02-03": {
                        "id": "lesson-02-03",
                        "section_id": "section-02",
                        "title": "Request Bodies with Pydantic",
                        "order": 3,
                        "content": (
                            "# Request Bodies with Pydantic\n\n"
                            "Declare the expected JSON shape using a `BaseModel` subclass.\n\n"
                            "```python\n"
                            "from pydantic import BaseModel\n\n"
                            "class Item(BaseModel):\n"
                            "    name: str\n"
                            "    price: float\n"
                            "    in_stock: bool = True\n\n"
                            "@app.post('/items')\n"
                            "def create_item(item: Item):\n"
                            "    return item\n"
                            "```\n\n"
                            "FastAPI will:\n"
                            "1. Parse the incoming JSON body.\n"
                            "2. Validate every field against its type.\n"
                            "3. Return a detailed 422 error for any mismatch — automatically."
                        ),
                    },
                },
            },
        },
    }
}

PROGRESS_DB: dict = {
    "user_id": "default_user",
    "current_course_id": "course-01",
    "current_section_id": "section-01",
    "current_lesson_id": "lesson-01-01",
    "completion_percentage": 0.0,
}
