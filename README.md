# C1176 — Generative AI for Instructional Design

Courseware for **Generative AI for Instructional Design (C1176)**, a one-day
(7.5-hour), hands-on, non-WSQ short course by **Tertiary Infotech Academy Pte
Ltd**. Learners use generative AI (ChatGPT, Claude, Gemini and an AI image tool)
to plan courses, write learning content, create assessments and produce learning
materials — building one connected **Meridian Service Excellence course kit** end
to end across 10 practical labs.

- **Storefront:** https://www.tertiarycourses.com.sg/generative-ai-for-instructional-design.html
- **Level:** Beginner · **Duration:** 1 day (7.5 hours) · **Mode:** Instructor-led, hands-on labs

## Topics

1. **Getting Started with Generative AI for Instructional Design** — introduction to instructional design and generative AI, setting up AI tools, analysing learning needs, audiences and objectives, and structuring courses and lessons.
2. **Creating Learning Content and Assessments with AI** — generating content, activities and scenarios; creating quizzes, assessments and rubrics; producing scripts, visuals and job aids; and aligning to outcomes and quality-checking AI output.

## What's in this repository

| Path | Contents |
|---|---|
| [`courseware/`](courseware/) | Trainer slides (PPTX) + PDF, Lesson Plan (LP) and Learner Guide (LG) as DOCX + PDF |
| [`labs/`](labs/) | The 10 hands-on labs, `tools.md`, and the `reference-pack/` Meridian training brief |
| [`LG-Generative AI for Instructional Design (C1176).md`](LG-Generative%20AI%20for%20Instructional%20Design%20%28C1176%29.md) | Markdown mirror of the Learner Guide |
| `.claude/skills/non-wsq-courseware-build/` | The single-source build pipeline (`course_data.py` + `data_domainN.py` drive every artifact) |

## Rebuilding

All artifacts are generated from one source (`course_data.py` + `data_domain1.py`
+ `data_domain2.py`) so the PPT, LP, LG and labs stay 100% aligned:

```bash
cd .claude/skills/non-wsq-courseware-build/build
python gen_labs.py                       # regenerate labs/
SOFFICE="/path/to/soffice" bash build_courseware.sh   # PPT + LP + LG (DOCX + PDF) with TOC
```

There is **no assessment** — this is a commercial short course; each lab verifies
itself with a *Test it* step.

---

© 2026 Tertiary Infotech Academy Pte Ltd
