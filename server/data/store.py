COURSES_DB: dict = {
    "course-04": {
        "id": "course-04",
        "title": "גיט ו-GitHub לצוותים",
        "description": "שליטה בתהליכי עבודה של בקרת גרסאות, אסטרטגיות ענפים (branching), Pull Requests וצנרות CI/CD כפי שהן משמשות בצוותי פיתוח אמיתיים.",
        "image_url": "https://placehold.co/600x340/f57c00/ffffff?text=Git+%26+GitHub",
        "sections": {
            "section-07": {
                "id": "section-07",
                "course_id": "course-04",
                "title": "מושגי יסוד ב-Git",
                "order": 1,
                "lessons": {
                    "lesson-07-01": {
                        "id": "lesson-07-01",
                        "section_id": "section-07",
                        "title": "Commits, Staging וההיסטוריה",
                        "order": 1,
                        "content": "# Commits, Staging וההיסטוריה\n\nGit עוקב אחרי שינויים בשלושה אזורים:\n\n- **Working Directory** — העריכות המקומיות שלכם בקבצים\n- **Staging Area (Index)** — שינויים שסומנו ל-commit הבא\n- **Repository** — ההיסטוריה שכבר בוצע לה commit\n\n```bash\ngit add src/app.py      # מוסיף קובץ ספציפי ל-staging\ngit commit -m 'feat: add login route'\ngit log --oneline       # תצוגה קומפקטית של ההיסטוריה\n```",
                    },
                    "lesson-07-02": {
                        "id": "lesson-07-02",
                        "section_id": "section-07",
                        "title": "Branching ו-Merging (ענפים ומיזוג)",
                        "order": 2,
                        "content": "# Branching ו-Merging (ענפים ומיזוג)\n\nענפים (branches) מאפשרים לכם לעבוד בבידוד בלי להשפיע על `main`.\n\n```bash\ngit checkout -b feature/auth   # יצירה ומעבר לענף חדש\ngit merge feature/auth          # מיזוג לענף הנוכחי\ngit branch -d feature/auth      # מחיקה אחרי המיזוג\n```\n\n## Fast-Forward מול מיזוג תלת-כיווני\n- **Fast-forward:** אין הסתעפות — Git פשוט מזיז את המצביע קדימה.\n- **מיזוג תלת-כיווני (3-way):** הענפים התפצלו — Git יוצר commit מיזוג ייעודי.",
                    },
                    "lesson-07-03": {
                        "id": "lesson-07-03",
                        "section_id": "section-07",
                        "title": "Rebase ו-Cherry-Pick",
                        "order": 3,
                        "content": "# Rebase ו-Cherry-Pick\n\n`rebase` מנגן מחדש את ה-commits שלכם מעל ענף אחר — שומר על היסטוריה ליניארית.\n\n```bash\ngit rebase main            # ניגון מחדש של הענף הנוכחי מעל main\ngit cherry-pick a1b2c3d   # החלת commit בודד על הענף הנוכחי\n```\n\n> לעולם אל תעשו rebase ל-commits שכבר נדחפו (pushed) לענף משותף.",
                    },
                },
            },
            "section-08": {
                "id": "section-08",
                "course_id": "course-04",
                "title": "תהליכי עבודה ב-GitHub",
                "order": 2,
                "lessons": {
                    "lesson-08-01": {
                        "id": "lesson-08-01",
                        "section_id": "section-08",
                        "title": "Pull Requests וסקירת קוד",
                        "order": 1,
                        "content": "# Pull Requests וסקירת קוד\n\nPR (Pull Request) מציע שינויים מענף אחד לתוך ענף אחר, ומפעיל תהליך סקירה.\n\n## היגיינת PR טובה\n- שמרו על PRs קטנים וממוקדים בנושא אחד.\n- כתבו תיאור ברור: *מה* השתנה ו*למה*.\n- קשרו לישוט (issue) הרלוונטי.\n\n## נימוסי סקירה\n- הערות על הקוד, לא על האדם.\n- השתמשו ב-*Suggest Changes* לתיקונים קטנים.",
                    },
                    "lesson-08-02": {
                        "id": "lesson-08-02",
                        "section_id": "section-08",
                        "title": "GitHub Actions ו-CI/CD",
                        "order": 2,
                        "content": "# GitHub Actions ו-CI/CD\n\nהרצה אוטומטית של טסטים ופריסות (deployments) על כל push.\n\n```yaml\nname: CI\non: [push, pull_request]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with: { python-version: '3.12' }\n      - run: pip install -r requirements.txt\n      - run: pytest\n```",
                    },
                    "lesson-08-03": {
                        "id": "lesson-08-03",
                        "section_id": "section-08",
                        "title": "הגנת ענפים (Branch Protection) וסודות (Secrets)",
                        "order": 3,
                        "content": "# הגנת ענפים (Branch Protection) וסודות (Secrets)\n\n## כללי הגנת ענפים\n- דרשו סקירות PR לפני מיזוג ל-`main`.\n- דרשו שבדיקות סטטוס (CI) יעברו בהצלחה.\n- הגבילו force-push.\n\n## ניהול Secrets\n- שמרו מפתחות API ב-**GitHub Secrets** (Settings → Secrets).\n- התייחסו אליהם ב-workflows: `${{ secrets.API_KEY }}`.\n- לעולם אל תעשו commit ל-secrets בתוך הריפוזיטורי.",
                    },
                },
            },
        },
    },
    "course-05": {
        "id": "course-05",
        "title": "יסודות CSS ועיצוב ממשק משתמש",
        "description": "מאפס למפתח/ת UI בטוח/ה בעצמו/ה. שליטה ב-Flexbox, Grid, אנימציות ומערכות עיצוב.",
        "image_url": "https://placehold.co/600x340/7b1fa2/ffffff?text=CSS+%26+UI+Design",
        "sections": {
            "section-09": {
                "id": "section-09",
                "course_id": "course-05",
                "title": "מערכות פריסה (Layout)",
                "order": 1,
                "lessons": {
                    "lesson-09-01": {
                        "id": "lesson-09-01",
                        "section_id": "section-09",
                        "title": "שליטה ב-Flexbox",
                        "order": 1,
                        "content": "# שליטה ב-Flexbox\n\nFlexbox היא מערכת פריסה חד-ממדית (שורה או עמודה).\n\n```css\n.container {\n  display: flex;\n  justify-content: space-between; /* ציר ראשי */\n  align-items: center;            /* ציר משני */\n  gap: 16px;\n}\n```\n\n## מאפיינים מרכזיים\n- `flex-grow` — כמה מקום נוסף פריט תופס.\n- `flex-shrink` — כמה פריט מתכווץ.\n- `flex-basis` — הגודל ההתחלתי האידאלי של הפריט.",
                    },
                    "lesson-09-02": {
                        "id": "lesson-09-02",
                        "section_id": "section-09",
                        "title": "CSS Grid",
                        "order": 2,
                        "content": "# CSS Grid\n\nGrid היא מערכת פריסה דו-ממדית (שורות ועמודות בו-זמנית).\n\n```css\n.grid {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 24px;\n}\n\n.featured {\n  grid-column: span 2; /* תופס 2 עמודות */\n}\n```\n\nהשתמשו ב-Grid לפריסת עמוד כללית; ב-Flexbox ליישור ברמת רכיב.",
                    },
                    "lesson-09-03": {
                        "id": "lesson-09-03",
                        "section_id": "section-09",
                        "title": "עיצוב רספונסיבי ו-Media Queries",
                        "order": 3,
                        "content": "# עיצוב רספונסיבי ו-Media Queries\n\n## גישת Mobile-First\nכתבו סגנונות בסיס למובייל, ואז הוסיפו מורכבות למסכים גדולים יותר.\n\n```css\n.card { font-size: 14px; }\n\n@media (min-width: 768px) {\n  .card { font-size: 16px; }\n}\n\n@media (min-width: 1200px) {\n  .card { font-size: 18px; }\n}\n```\n\nהשתמשו ביחידות `rem` לטיפוגרפיה גמישה.",
                    },
                },
            },
            "section-10": {
                "id": "section-10",
                "course_id": "course-05",
                "title": "מערכות עיצוב (Design Systems)",
                "order": 2,
                "lessons": {
                    "lesson-10-01": {
                        "id": "lesson-10-01",
                        "section_id": "section-10",
                        "title": "Design Tokens ומשתנים",
                        "order": 1,
                        "content": "# Design Tokens ומשתנים\n\nDesign Tokens הם החלטות העיצוב הקטנות ביותר הניתנות לשימוש חוזר (צבעים, ריווחים, גדלי גופן).\n\n```css\n:root {\n  --color-primary: #1976d2;\n  --color-surface: #ffffff;\n  --spacing-md: 16px;\n  --radius-md: 8px;\n  --font-body: 'Inter', sans-serif;\n}\n\n.button {\n  background: var(--color-primary);\n  padding: var(--spacing-md);\n  border-radius: var(--radius-md);\n}\n```",
                    },
                    "lesson-10-02": {
                        "id": "lesson-10-02",
                        "section_id": "section-10",
                        "title": "אנימציות ומעברים (Transitions) ב-CSS",
                        "order": 2,
                        "content": "# אנימציות ומעברים (Transitions) ב-CSS\n\n## Transitions\nמעבר חלק בין שני מצבים.\n```css\n.button {\n  transition: background 0.2s ease, transform 0.15s ease;\n}\n.button:hover {\n  background: #1565c0;\n  transform: translateY(-2px);\n}\n```\n\n## אנימציות Keyframe\n```css\n@keyframes fadeIn {\n  from { opacity: 0; transform: translateY(8px); }\n  to   { opacity: 1; transform: translateY(0); }\n}\n.card { animation: fadeIn 0.3s ease forwards; }\n```",
                    },
                    "lesson-10-03": {
                        "id": "lesson-10-03",
                        "section_id": "section-10",
                        "title": "טיפוגרפיה ותורת הצבע",
                        "order": 3,
                        "content": "# טיפוגרפיה ותורת הצבע\n\n## סולם גדלים (Type Scale)\nהשתמשו בסולם מודולרי עקבי: 12 / 14 / 16 / 20 / 24 / 32 / 48px.\n\n## תפקידי צבע\n- **Primary** — פעולת המותג המרכזית (כפתורים, קישורים)\n- **Surface** — רקע של כרטיסים ופאנלים\n- **On-Surface** — טקסט המונח על Surface\n- **Error / Success / Warning** — מצבים סמנטיים\n\n## ניגודיות (Contrast)\nודאו יחס ניגודיות של לפחות **4.5:1** לטקסט גוף (תקן WCAG AA).",
                    },
                },
            },
        },
    },
    "course-06": {
        "id": "course-06",
        "title": "אלגוריתמים ומבני נתונים",
        "description": "הצליחו בראיונות טכניים וכתבו קוד יעיל. כולל מיון, עצים, גרפים, תכנות דינמי ועוד.",
        "image_url": "https://placehold.co/600x340/c62828/ffffff?text=Algorithms+%26+DSA",
        "sections": {
            "section-11": {
                "id": "section-11",
                "course_id": "course-06",
                "title": "מבני נתונים בסיסיים",
                "order": 1,
                "lessons": {
                    "lesson-11-01": {
                        "id": "lesson-11-01",
                        "section_id": "section-11",
                        "title": "מערכים (Arrays) ו-Hash Maps",
                        "order": 1,
                        "content": "# מערכים (Arrays) ו-Hash Maps\n\n## מערכים (Arrays)\n- קריאה לפי אינדקס ב-O(1), חיפוש ב-O(n).\n- הכי טוב לאוספים מסודרים בגודל קבוע.\n\n## Hash Maps\n- הוספה, חיפוש ומחיקה ב-O(1) בממוצע.\n- Python: `dict`. JS: `Map` או אובייקט רגיל.\n\n```python\n# Two-Sum עם hash map — O(n)\ndef two_sum(nums, target):\n    seen = {}\n    for i, n in enumerate(nums):\n        complement = target - n\n        if complement in seen:\n            return [seen[complement], i]\n        seen[n] = i\n```",
                    },
                    "lesson-11-02": {
                        "id": "lesson-11-02",
                        "section_id": "section-11",
                        "title": "מחסניות (Stacks) ותורים (Queues)",
                        "order": 2,
                        "content": "# מחסניות (Stacks) ותורים (Queues)\n\n## Stack — LIFO (אחרון נכנס, ראשון יוצא)\n```python\nstack = []\nstack.append(1)   # push\nstack.pop()       # pop  → O(1)\n```\nשימושים: היסטוריית undo, DFS, בדיקת סוגריים מאוזנים.\n\n## Queue — FIFO (ראשון נכנס, ראשון יוצא)\n```python\nfrom collections import deque\nq = deque()\nq.append(1)       # enqueue\nq.popleft()       # dequeue → O(1)\n```\nשימושים: BFS, תזמון משימות.",
                    },
                    "lesson-11-03": {
                        "id": "lesson-11-03",
                        "section_id": "section-11",
                        "title": "עצים בינאריים ו-BST",
                        "order": 3,
                        "content": "# עצים בינאריים ו-BST\n\n**עץ חיפוש בינארי (BST)** מקיים: הבן השמאלי < הצומת < הבן הימני.\n\n```python\nclass Node:\n    def __init__(self, val):\n        self.val = val\n        self.left = self.right = None\n\ndef inorder(node):\n    if node:\n        inorder(node.left)\n        print(node.val)\n        inorder(node.right)\n```\n\n## סיבוכיות (עץ מאוזן)\n- חיפוש, הוספה, מחיקה: O(log n)\n- מקרה גרוע (עץ מוטה): O(n)",
                    },
                },
            },
            "section-12": {
                "id": "section-12",
                "course_id": "course-06",
                "title": "מיון וחיפוש",
                "order": 2,
                "lessons": {
                    "lesson-12-01": {
                        "id": "lesson-12-01",
                        "section_id": "section-12",
                        "title": "חיפוש בינארי (Binary Search)",
                        "order": 1,
                        "content": "# חיפוש בינארי (Binary Search)\n\nמציאת ערך במערך **ממוין** ב-O(log n).\n\n```python\ndef binary_search(arr, target):\n    lo, hi = 0, len(arr) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1\n```\n\nתמיד שאלו: *האם הקלט ממוין?* אם כן, חשבו קודם על חיפוש בינארי.",
                    },
                    "lesson-12-02": {
                        "id": "lesson-12-02",
                        "section_id": "section-12",
                        "title": "Merge Sort ו-Quick Sort",
                        "order": 2,
                        "content": "# Merge Sort ו-Quick Sort\n\n## Merge Sort — O(n log n) מובטח\n- מחלקים את המערך לשניים, ממיינים כל חצי, וממזגים.\n- מיון יציב (Stable). משתמש ב-O(n) זיכרון נוסף.\n\n## Quick Sort — O(n log n) בממוצע\n- בוחרים pivot, מחלקים סביבו, וקוראים רקורסיבית.\n- In-place, זיכרון מחסנית O(log n).\n- מקרה גרוע O(n²) עם בחירת pivot גרועה.\n\n**כלל אצבע לראיונות:** ברירת מחדל ל-Merge Sort כשיציבות חשובה; Quick Sort למהירות גולמית.",
                    },
                    "lesson-12-03": {
                        "id": "lesson-12-03",
                        "section_id": "section-12",
                        "title": "מבוא לתכנות דינמי (Dynamic Programming)",
                        "order": 3,
                        "content": "# מבוא לתכנות דינמי (Dynamic Programming)\n\nתכנות דינמי (DP) פותר בעיות על ידי פירוק לתת-בעיות חופפות ושמירת תוצאות ב-cache.\n\n## פיבונאצ'י — נאיבי O(2ⁿ) → DP O(n)\n```python\ndef fib(n, memo={}):\n    if n <= 1: return n\n    if n not in memo:\n        memo[n] = fib(n-1) + fib(n-2)\n    return memo[n]\n```\n\n## מתי להשתמש ב-DP\n- מבנה אופטימלי: פתרון אופטימלי בנוי מתת-פתרונות אופטימליים.\n- תת-בעיות חופפות: אותן תת-בעיות מחושבות שוב ושוב.",
                    },
                },
            },
        },
    },
    "course-02": {
        "id": "course-02",
        "title": "שליטה ב-React ו-TypeScript",
        "description": "בנו אפליקציות ווב מודרניות ובטוחות-טיפוסים עם React 18, TypeScript, וכלי האקוסיסטם העדכניים ביותר.",
        "image_url": "https://placehold.co/600x340/0288d1/ffffff?text=React+%26+TypeScript",
        "sections": {
            "section-03": {
                "id": "section-03",
                "course_id": "course-02",
                "title": "יסודות TypeScript",
                "order": 1,
                "lessons": {
                    "lesson-03-01": {
                        "id": "lesson-03-01",
                        "section_id": "section-03",
                        "title": "טיפוסים, Interfaces ו-Generics",
                        "order": 1,
                        "content": (
                            "# טיפוסים, Interfaces ו-Generics\n\n"
                            "TypeScript מוסיף שכבת טיפוסים סטטית מעל JavaScript.\n\n"
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
                            "Generics מאפשרים לכתוב כלי-עזר גנריים ובטוחי-טיפוסים בלי לוותר על גמישות."
                        ),
                    },
                    "lesson-03-02": {
                        "id": "lesson-03-02",
                        "section_id": "section-03",
                        "title": "צמצום טיפוסים (Type Narrowing) ו-Guards",
                        "order": 2,
                        "content": (
                            "# צמצום טיפוסים (Type Narrowing) ו-Guards\n\n"
                            "TypeScript מצמצם טיפוסי איחוד (union) בתוך בלוקים תנאיים באופן אוטומטי.\n\n"
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
                            "ל-TypeScript יש טיפוסי mapped מובנים שממירים טיפוסים קיימים.\n\n"
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
                            "הדפוסים האלה שומרים על הטיפוסים DRY ומונעים שינוי בשוגג."
                        ),
                    },
                },
            },
            "section-04": {
                "id": "section-04",
                "course_id": "course-02",
                "title": "דפוסי React 18",
                "order": 2,
                "lessons": {
                    "lesson-04-01": {
                        "id": "lesson-04-01",
                        "section_id": "section-04",
                        "title": "useState ו-useReducer",
                        "order": 1,
                        "content": (
                            "# useState ו-useReducer\n\n"
                            "השתמשו ב-`useState` לערכים פשוטים וב-`useReducer` למכונות מצב מורכבות.\n\n"
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
                        "title": "useEffect ושליפת נתונים",
                        "order": 2,
                        "content": (
                            "# useEffect ושליפת נתונים\n\n"
                            "`useEffect` רץ אחרי הרינדור. תמיד נקו (cleanup) subscriptions.\n\n"
                            "```typescript\n"
                            "useEffect(() => {\n"
                            "  let active = true\n\n"
                            "  fetch('/api/courses')\n"
                            "    .then(r => r.json())\n"
                            "    .then(data => { if (active) setCourses(data) })\n\n"
                            "  return () => { active = false }\n"
                            "}, [])\n"
                            "```\n\n"
                            "הדגל `active` מונע עדכוני מצב ברכיבים שכבר הוסרו (unmounted)."
                        ),
                    },
                    "lesson-04-03": {
                        "id": "lesson-04-03",
                        "section_id": "section-04",
                        "title": "Custom Hooks (הוקים מותאמים אישית)",
                        "order": 3,
                        "content": (
                            "# Custom Hooks (הוקים מותאמים אישית)\n\n"
                            "חילצו לוגיקת state ניתנת לשימוש חוזר לתוך פונקציות שמתחילות ב-`use`.\n\n"
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
        "title": "System Design למפתחים",
        "description": "למדו לתכנן מערכות מבוזרות מדרגיות ועמידות בפני תקלות — ממסדי נתונים ועד מאזני עומסים.",
        "image_url": "https://placehold.co/600x340/388e3c/ffffff?text=System+Design",
        "sections": {
            "section-05": {
                "id": "section-05",
                "course_id": "course-03",
                "title": "מושגי יסוד",
                "order": 1,
                "lessons": {
                    "lesson-05-01": {
                        "id": "lesson-05-01",
                        "section_id": "section-05",
                        "title": "Scalability מול Performance (מדרגיות מול ביצועים)",
                        "order": 1,
                        "content": (
                            "# Scalability מול Performance (מדרגיות מול ביצועים)\n\n"
                            "- **Performance (ביצועים)** — הפיכת בקשה בודדת למהירה יותר.\n"
                            "- **Scalability (מדרגיות)** — התמודדות עם יותר בקשות בלי פגיעה בביצועים.\n\n"
                            "## Scaling אנכי מול אופקי\n"
                            "- **אנכי (scale up):** מחשב חזק יותר — יותר CPU, RAM. פשוט אבל יש תקרה.\n"
                            "- **אופקי (scale out):** יותר מחשבים. דורש שירותים stateless ו-load balancer."
                        ),
                    },
                    "lesson-05-02": {
                        "id": "lesson-05-02",
                        "section_id": "section-05",
                        "title": "משפט CAP",
                        "order": 2,
                        "content": (
                            "# משפט CAP\n\n"
                            "מערכת מבוזרת יכולה להבטיח לכל היותר **2 מתוך 3** תכונות:\n\n"
                            "- **C**onsistency (עקביות) — כל קריאה מחזירה את הכתיבה העדכנית ביותר.\n"
                            "- **A**vailability (זמינות) — כל בקשה מקבלת תשובה (לא בהכרח העדכנית ביותר).\n"
                            "- **P**artition Tolerance (עמידות בפני חלוקה) — המערכת פועלת גם כשצמתים לא יכולים לתקשר.\n\n"
                            "בפועל, partitions ברשת קורים — אז בוחרים בין **CP** ל-**AP**."
                        ),
                    },
                    "lesson-05-03": {
                        "id": "lesson-05-03",
                        "section_id": "section-05",
                        "title": "מאזני עומסים (Load Balancers)",
                        "order": 3,
                        "content": (
                            "# מאזני עומסים (Load Balancers)\n\n"
                            "מאזן עומסים מפזר תעבורה נכנסת בין כמה שרתים.\n\n"
                            "## אסטרטגיות נפוצות\n"
                            "- **Round Robin** — בקשות עוברות בין שרתים לפי סדר.\n"
                            "- **Least Connections** — מנתב לשרת עם הכי פחות חיבורים פעילים.\n"
                            "- **IP Hash** — אותה כתובת IP תמיד מגיעה לאותו שרת (שימושי ל-sessions).\n\n"
                            "## Layer 4 מול Layer 7\n"
                            "- **L4** פועל על TCP/UDP — מהיר, בלי בדיקת תוכן.\n"
                            "- **L7** פועל על HTTP — יכול לנתב לפי נתיב URL, headers, או cookies."
                        ),
                    },
                },
            },
            "section-06": {
                "id": "section-06",
                "course_id": "course-03",
                "title": "אסטרטגיות אחסון נתונים",
                "order": 2,
                "lessons": {
                    "lesson-06-01": {
                        "id": "lesson-06-01",
                        "section_id": "section-06",
                        "title": "SQL מול NoSQL",
                        "order": 1,
                        "content": (
                            "# SQL מול NoSQL\n\n"
                            "## SQL (יחסי)\n"
                            "- סכימה מובנית, טרנזקציות ACID, joins עוצמתיים.\n"
                            "- הכי טוב עבור: מערכות פיננסיות, ERP, כל דבר שדורש עקביות חזקה.\n\n"
                            "## NoSQL\n"
                            "- סכימה גמישה, scaling אופקי, עקביות eventual.\n"
                            "- סוגים: Document (MongoDB), Key-Value (Redis), Column (Cassandra), Graph (Neo4j).\n\n"
                            "## כלל אצבע\n"
                            "התחילו עם SQL. עברו ל-NoSQL רק כשיש לכם בעיית scaling קונקרטית ש-SQL לא יכול לפתור."
                        ),
                    },
                    "lesson-06-02": {
                        "id": "lesson-06-02",
                        "section_id": "section-06",
                        "title": "אסטרטגיות Caching (מטמון)",
                        "order": 2,
                        "content": (
                            "# אסטרטגיות Caching (מטמון)\n\n"
                            "Caching מקטין latency ועומס על מסד הנתונים על ידי שמירת תוצאות מחושבות.\n\n"
                            "## דפוסים\n"
                            "- **Cache-Aside:** האפליקציה בודקת קודם ב-cache; אם אין (miss), טוענת מה-DB וממלאת את ה-cache.\n"
                            "- **Write-Through:** כותבים ל-cache ול-DB בו-זמנית.\n"
                            "- **Write-Behind:** כותבים ל-cache מיד; מסנכרנים ל-DB באופן אסינכרוני.\n\n"
                            "## מדיניות פינוי (Eviction)\n"
                            "- **LRU** (הכי פחות נעשה בו שימוש לאחרונה) — הכי נפוץ, מתאים לרוב המקרים.\n"
                            "- **TTL** (זמן חיים) — פוקע אחרי משך זמן קבוע."
                        ),
                    },
                    "lesson-06-03": {
                        "id": "lesson-06-03",
                        "section_id": "section-06",
                        "title": "Sharding למסדי נתונים",
                        "order": 3,
                        "content": (
                            "# Sharding למסדי נתונים\n\n"
                            "Sharding מפצל dataset גדול בין כמה צמתי מסד נתונים (shards).\n\n"
                            "## בחירת Shard Key\n"
                            "ה-shard key קובע איזה צומת שומר כל שורה. key גרוע גורם ל-**hotspots**.\n\n"
                            "- **key טוב:** `user_id` — מפזר כתיבות באופן שווה בין ה-shards.\n"
                            "- **key גרוע:** `created_at` — כל הכתיבות החדשות פוגעות באותו shard (hotspot מבוסס-זמן).\n\n"
                            "## חסרונות\n"
                            "- joins בין shards יקרים או בלתי אפשריים.\n"
                            "- re-sharding כואב — תכננו את ה-key בקפידה מראש."
                        ),
                    },
                },
            },
        },
    },
    "course-01": {
        "id": "course-01",
        "title": "בוטקמפ Full-Stack בפייתון",
        "description": "שליטה בפייתון, FastAPI ו-React — מאפס למפתח/ת מוכן/ה לפרודקשן.",
        "image_url": "https://placehold.co/600x340/1976d2/ffffff?text=Python+Bootcamp",
        "sections": {
            "section-01": {
                "id": "section-01",
                "course_id": "course-01",
                "title": "יסודות פייתון",
                "order": 1,
                "lessons": {
                    "lesson-01-01": {
                        "id": "lesson-01-01",
                        "section_id": "section-01",
                        "title": "משתנים וטיפוסי נתונים",
                        "order": 1,
                        "content": (
                            "# משתנים וטיפוסי נתונים\n\n"
                            "בפייתון לכל ערך יש טיפוס. הטיפוסים המובנים הנפוצים ביותר הם:\n\n"
                            "```python\n"
                            "name: str = 'Alice'\n"
                            "age: int = 30\n"
                            "height: float = 1.72\n"
                            "is_student: bool = True\n"
                            "```\n\n"
                            "פייתון מסיקה את הטיפוס בזמן ריצה, אבל שימוש ב-type hints הופך את הקוד למתועד יותר "
                            "ומאפשר כלי ניתוח סטטי כמו `mypy`.\n\n"
                            "## כללים מרכזיים\n"
                            "- שמות משתנים הם ב-`snake_case`.\n"
                            "- משתמשים ב-`=` להשמה, ב-`:` להערות טיפוס (type annotations).\n"
                            "- מחרוזות יכולות להשתמש בגרשיים בודדים או כפולים — היו עקביים."
                        ),
                    },
                    "lesson-01-02": {
                        "id": "lesson-01-02",
                        "section_id": "section-01",
                        "title": "בקרת זרימה: if / elif / else",
                        "order": 2,
                        "content": (
                            "# בקרת זרימה\n\n"
                            "פייתון משתמשת בהזחה (4 רווחים) להגדרת בלוקי קוד — בלי צורך בסוגריים מסולסלים.\n\n"
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
                            "## ביטוי תנאי (Ternary)\n"
                            "```python\n"
                            "label = 'pass' if score >= 60 else 'fail'\n"
                            "```"
                        ),
                    },
                    "lesson-01-03": {
                        "id": "lesson-01-03",
                        "section_id": "section-01",
                        "title": "פונקציות ו-Scope (תחום הכרה)",
                        "order": 3,
                        "content": (
                            "# פונקציות ו-Scope (תחום הכרה)\n\n"
                            "פונקציות מוגדרות עם `def` ותומכות בארגומנטים ברירת מחדל, *args ו-**kwargs.\n\n"
                            "```python\n"
                            "def greet(name: str, greeting: str = 'Hello') -> str:\n"
                            "    return f'{greeting}, {name}!'\n\n"
                            "print(greet('Bob'))           # Hello, Bob!\n"
                            "print(greet('Bob', 'Shalom')) # Shalom, Bob!\n"
                            "```\n\n"
                            "## כללי Scope (LEGB)\n"
                            "פייתון פותרת שמות בסדר הזה: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in."
                        ),
                    },
                },
            },
            "section-02": {
                "id": "section-02",
                "course_id": "course-01",
                "title": "יסודות FastAPI",
                "order": 2,
                "lessons": {
                    "lesson-02-01": {
                        "id": "lesson-02-01",
                        "section_id": "section-02",
                        "title": "אפליקציית FastAPI הראשונה שלכם",
                        "order": 1,
                        "content": (
                            "# אפליקציית FastAPI הראשונה שלכם\n\n"
                            "FastAPI הוא framework web מודרני וביצועי, בנוי מעל Starlette ו-Pydantic.\n\n"
                            "```python\n"
                            "from fastapi import FastAPI\n\n"
                            "app = FastAPI()\n\n"
                            "@app.get('/')\n"
                            "def root():\n"
                            "    return {'message': 'Hello World'}\n"
                            "```\n\n"
                            "הריצו עם:\n"
                            "```bash\n"
                            "uvicorn main:app --reload\n"
                            "```\n\n"
                            "בקרו ב-`http://localhost:8000/docs` לתיעוד Swagger שנוצר אוטומטית."
                        ),
                    },
                    "lesson-02-02": {
                        "id": "lesson-02-02",
                        "section_id": "section-02",
                        "title": "פרמטרים ב-Path וב-Query",
                        "order": 2,
                        "content": (
                            "# פרמטרים ב-Path וב-Query\n\n"
                            "FastAPI מפענח ומאמת פרמטרים מה-URL באופן אוטומטי.\n\n"
                            "```python\n"
                            "@app.get('/items/{item_id}')\n"
                            "def get_item(item_id: int, q: str | None = None):\n"
                            "    return {'item_id': item_id, 'query': q}\n"
                            "```\n\n"
                            "- `item_id` הוא **path parameter** — מוצהר בתוך מחרוזת הנתיב.\n"
                            "- `q` הוא **query parameter** — מצורף ל-URL: `?q=search`.\n"
                            "- Pydantic מאמת טיפוסים אוטומטית; קלט לא תקין מחזיר שגיאת HTTP 422."
                        ),
                    },
                    "lesson-02-03": {
                        "id": "lesson-02-03",
                        "section_id": "section-02",
                        "title": "גוף הבקשה (Request Body) עם Pydantic",
                        "order": 3,
                        "content": (
                            "# גוף הבקשה (Request Body) עם Pydantic\n\n"
                            "הצהירו על צורת ה-JSON הצפויה באמצעות מחלקה שיורשת מ-`BaseModel`.\n\n"
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
                            "FastAPI יבצע:\n"
                            "1. פענוח גוף ה-JSON הנכנס.\n"
                            "2. אימות כל שדה מול הטיפוס שלו.\n"
                            "3. החזרת שגיאת 422 מפורטת על כל אי-התאמה — אוטומטית."
                        ),
                    },
                },
            },
        },
    },
}

PROGRESS_DB: dict = {
    "user_id": "default_user",
    "current_course_id": "course-01",
    "current_section_id": "section-01",
    "current_lesson_id": "lesson-01-01",
    "completion_percentage": 0.0,
}
