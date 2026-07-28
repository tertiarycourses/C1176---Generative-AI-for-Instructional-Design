#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the labs/ markdown from the SAME single source as the deck/LP/LG
(course_data.py + data_domainN.py), so labs stay 100% aligned with the other
artifacts. Emits labs/lab-NN-*.md, labs/README.md and refreshes nothing else
(tools.md and the brief pack are hand-authored). Enrichment sections
(Prerequisites, Troubleshooting, Challenge, Reflection, Deliverable) live in the
ENRICH table below, keyed by lab number.

Run:  python gen_labs.py
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")

# ------------------------------------------------------------------ load labs
DOMS = []
for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.splitext(os.path.basename(f))[0])
    key = [k for k in dir(mod) if k.startswith("DOMAIN")][0]
    DOMS.append((getattr(mod, key), getattr(mod, "SCENARIO", None)))

LABSLIST = []
SCENARIO = None
for dom, scen in DOMS:
    if scen and not SCENARIO:
        SCENARIO = scen
    LABSLIST.extend(dom)

TOPIC_TITLE = {t["num"]: t["title"] for t in C.TOPICS}

# ------------------------------------------------------------------ approx minutes per lab
# Derived from the schedule lab blocks so the labs match the Lesson Plan timing.
def approx_minutes():
    sched = C.SCHEDULE(lambda nums: "\x00".join(str(n) for n in nums))
    mins = {}
    for _day, (_theme, rows) in sched.items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                per = round(row[2] / len(nums))
                for n in nums:
                    mins[n] = per
    return mins


MINS = approx_minutes()

# ------------------------------------------------------------------ per-lab enrichment
ENRICH = {
 1: dict(
    prereqs=[
        "A laptop with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection.",
        "An account for at least one chat assistant (ChatGPT, Claude or Gemini) and access to an AI image tool.",
        "The supplied Meridian training brief to hand (labs/reference-pack/).",
    ],
    trouble=[
        "**A tool won't let you sign in or generate.** Try a different one — you only need one chat assistant and one image tool to follow the labs; tell the trainer what you have.",
        "**The image tool is not obvious.** Image generation is built into ChatGPT and Gemini and into Microsoft Copilot / Designer — any of these is enough; a dedicated tool like Firefly or Canva is optional.",
        "**The two assistants give very different answers.** That's normal — they differ in tone and length; the prompting and review skills you learn work across all of them.",
    ],
    challenge="Ask a third assistant the same instructional-design question and rank the three answers — which was most useful for a real course, and why?",
    lo=1,
    deliverable="Keep your Meridian-Service-Course-Kit folder with your toolkit notes and the brief — it is the home for everything you build across the next labs.",
 ),
 2: dict(
    prereqs=[
        "Completed Lab 1 (your tools are set up and responding).",
        "The supplied Meridian training brief open (labs/reference-pack/).",
    ],
    trouble=[
        "**The AI's draft is generic.** Add a role and real context (audience, level, mode, constraints); a vague prompt always gives a generic course.",
        "**The AI invents company policies or facts.** Tell it explicitly not to invent Meridian specifics and to leave placeholders — you add the real context from the brief in Lab 3.",
        "**The reply is the wrong length or format.** State the format you want (a numbered list, a word limit, a table) as a constraint and regenerate.",
    ],
    challenge="Write a structured prompt for a completely different course of your own using the same five parts, proving the template travels beyond Meridian.",
    lo=2,
    deliverable="Keep your reusable prompt library — you run its templates for needs analysis, objectives, content, assessment and job aids in every later lab.",
 ),
 3: dict(
    prereqs=[
        "Completed Lab 2 (you can write structured prompts).",
        "The supplied Meridian training brief with the audience and business need to hand.",
    ],
    trouble=[
        "**The objectives are vague ('understand customer service').** Insist on observable action verbs (describe, demonstrate, handle, decide) and reject any verb you cannot assess.",
        "**The personas feel like stereotypes.** Prompt for realistic, respectful profiles grounded in the brief, and strip any assumption not supported by it.",
        "**The AI states a fact as certain.** Treat every fact it produces as unverified — confirm it against the brief or a subject expert, and mark the rest [VERIFY].",
    ],
    challenge="Take one objective and draft how you would assess it, then check the objective is written well enough that the assessment is obvious — if it isn't, sharpen the verb.",
    lo=3,
    deliverable="Keep your needs analysis, learner personas and measurable objectives — the foundation every later artifact must align to.",
 ),
 4: dict(
    prereqs=[
        "Completed Lab 3 (you have measurable objectives and personas).",
        "Your objectives ready to paste into the curriculum-map prompt.",
    ],
    trouble=[
        "**A module serves no objective (an orphan).** Cut it or tie it to an objective — every module must earn its place in a three-hour course.",
        "**An objective has no module (a gap).** Add or extend a module to cover it; an objective you never teach is a promise you can't keep.",
        "**The times don't add up.** Ask the AI to rebalance to about three hours including a welcome, a break and a wrap-up, and trim the over-weighted module.",
    ],
    challenge="Re-sequence the modules for a purely self-paced e-learning version instead of a workshop, and note how the structure and timing would change.",
    lo=4,
    deliverable="Keep the curriculum map — the blueprint you turn into lesson plans in Lab 5 and fill with content in Topic 2.",
 ),
 5: dict(
    prereqs=[
        "Completed Lab 4 (you have a curriculum map).",
        "Your curriculum map ready to expand, one module at a time.",
    ],
    trouble=[
        "**A lesson is all lecture.** Add at least one activity where learners do or say something — the workshop earns its time through practice, not telling.",
        "**The timing overruns.** Trim content, not the practice; a shorter lesson that learners apply beats a full one they only hear.",
        "**Lessons repeat or jump.** Check the flow end to end and reorder so each lesson builds on the last without gaps or repetition.",
    ],
    challenge="Add a two-minute 'what if the customer is angry?' moment to one lesson and decide where it best fits the flow — small active beats extend engagement.",
    lo=5,
    deliverable="Keep the sequenced lesson plans — the detailed spine you develop into content, assessment and media across Topic 2.",
 ),
 6: dict(
    prereqs=[
        "Completed Lab 5 (you have detailed lesson plans).",
        "One lesson plan open to develop into content and activities.",
    ],
    trouble=[
        "**The content is a wall of text.** Chunk it into short sections with headings and cut every sentence you can — new staff skim, they don't study.",
        "**The scenario feels unrealistic.** Ground it in a real neighbourhood-store moment and give the learner genuine, plausible choices, not one obviously right answer.",
        "**An example carries a stereotype.** Rewrite it to be fair and inclusive of customers and staff alike; run the bias-check step on every example.",
    ],
    challenge="Write a second, harder branching scenario (an angry customer who is also right) and see whether your service model still holds — stretch the content against a tough case.",
    lo=6,
    deliverable="Keep the developed content, activities and scenarios — what you assess in Lab 7 and produce as media in Lab 8.",
 ),
 7: dict(
    prereqs=[
        "Completed Lab 6 (you have content and activities).",
        "Your learning objectives ready — every item must measure one.",
    ],
    trouble=[
        "**A quiz item doesn't map to an objective.** Cut it or rewrite it — assessment that measures nothing you promised wastes learners' time.",
        "**The distractors are obviously wrong.** Ask for plausible wrong options based on common mistakes, and remove giveaway cues like 'all of the above'.",
        "**The rubric is vague.** Make each level describe observable behaviour, so two markers would score the same performance the same way.",
    ],
    challenge="Take one multiple-choice item and rewrite it as a short scenario question at a higher cognitive level — see how the same objective can be tested more authentically.",
    lo=7,
    deliverable="Keep the quiz with its answer guide, the performance task and the calibrated rubric — the aligned assessment that slots into the package.",
 ),
 8: dict(
    prereqs=[
        "Completed Lab 7 (the content and assessment exist).",
        "An AI image tool (image generation in ChatGPT / Gemini / Copilot, or Firefly / Canva).",
    ],
    trouble=[
        "**The narration reads like a document.** Rewrite it to be heard — short spoken sentences, warm and clear, not paragraphs on a screen.",
        "**The images look off-brand or inconsistent.** Fix a style (colours, character look) and reuse it in every prompt; regenerate anything that doesn't match.",
        "**A job aid is too wordy to use.** Cut it to action-first steps a nervous associate could glance at mid-shift — if it needs reading, it isn't a job aid.",
    ],
    challenge="Generate an alternative visual style for the module (photographic instead of illustration) and decide which better suits new retail staff — then commit to one.",
    lo=8,
    deliverable="Keep the storyboard and narration script, the on-brand visuals with alt text, and the take-away job aids — the learner-facing media of the course.",
 ),
 9: dict(
    prereqs=[
        "Completed Labs 3-8 (every artifact exists).",
        "Your objectives and a list of all your artifacts ready to map.",
    ],
    trouble=[
        "**The AI 'confirms' its own facts.** It cannot — verify every flagged claim against the brief or a subject expert yourself, never on the AI's word.",
        "**The matrix hides a gap.** If an objective has no assessment, add one; every objective must be both taught and measured.",
        "**Readability still feels high.** Ask for a plain-language rewrite at a secondary-school level and check images all have alt text before you sign it off.",
    ],
    challenge="Pick the objective with the weakest coverage and strengthen its whole chain — content, activity and assessment — then re-run the matrix to prove the fix.",
    lo=9,
    deliverable="Keep the alignment matrix and the quality-check report — the evidence the package is aligned, accurate, fair and accessible.",
 ),
 10: dict(
    prereqs=[
        "Completed Labs 1-9 (you have every reviewed artifact).",
        "Your project folder with all artifacts ready to assemble.",
    ],
    trouble=[
        "**The package reads as disconnected parts.** Run the consistency pass — one voice, consistent terms and objective numbering — so it flows as one course.",
        "**A [VERIFY] or TODO is still in the package.** Do not deliver it — confirm the fact or remove the claim before you finalise.",
        "**The facilitator set and learner set are mixed up.** Split them cleanly — the answer guide and rubric belong only in the facilitator guide.",
    ],
    challenge="Hand the learner set to a colleague who knows nothing about the course and ask them to spot one confusing point — then fix it, as a real pilot would.",
    lo=10,
    deliverable="Keep the complete, exported Meridian Service Excellence course kit — facilitator guide and learner set — the finished, aligned course package the course set out to build.",
 ),
}


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def steps_md(steps):
    out = []
    for i, (instr, cmd) in enumerate(steps, 1):
        out.append(f"### Step {i}\n\n{instr}")
        if cmd:
            out.append("Prompt to use (paste into your AI assistant — ChatGPT, Claude or Gemini — or your image tool where the step says so, and adapt the bracketed parts):\n\n```text\n" + cmd + "\n```")
    return "\n\n".join(out)


def lab_filename(lab):
    return f"lab-{lab['num']:02d}-{slug(lab['title'])}.md"


def build_lab(lab):
    e = ENRICH[lab["num"]]
    topic = lab["topic"]
    mins = MINS.get(lab["num"], 40)
    parts = []
    parts.append(f"# Lab {lab['num']} — {lab['title']}\n")
    parts.append(
        f"**Topic 0{topic}:** {TOPIC_TITLE[topic]}  |  **Day 1**  |  "
        f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n"
    )
    if SCENARIO:
        parts.append("## Scenario\n\n" + SCENARIO + "\n")
    parts.append("## Goal\n\n" + lab["objective"] + "\n")
    parts.append("## What you'll build\n\n" + lab["build"] + "\n")
    parts.append("**Tools and techniques:** " + lab["services"] + "\n")
    parts.append("## Prerequisites\n\n" + "\n".join("- " + p for p in e["prereqs"]) + "\n")
    parts.append("## Steps\n\n" + steps_md(lab["steps"]) + "\n")
    parts.append("## Test it\n\n" + lab["test"] + "\n")
    parts.append("## Troubleshooting\n\n" + "\n".join("- " + t for t in e["trouble"]) + "\n")
    parts.append("## Challenge\n\n" + e["challenge"] + "\n")
    lo = C.LEARNING_OUTCOMES[e["lo"] - 1]
    lo_text = lo.split(":", 1)[1].strip().rstrip(".")
    parts.append(f"## Reflection\n\nLO{e['lo']} — In your own words: {lo_text}?\n")
    parts.append("## Deliverable\n\n" + e["deliverable"] + "\n")
    parts.append("---\n")
    parts.append(
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"
    )
    return "\n".join(parts) + "\n"


def build_readme(files):
    rows = []
    for lab in LABSLIST:
        fn = files[lab["num"]]
        rows.append(
            f"| 1 | 0{lab['topic']} | {lab['num']:02d} | [{lab['title']}]({fn}) |"
        )
    md = []
    md.append(f"# Labs — {C.TITLE}\n")
    md.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
    md.append(
        "All 10 labs build one connected **Meridian Service Excellence course kit**, which you begin in Lab 1 "
        "and finish in Lab 10 — taking a fictional retail chain's new-hire customer-service course from a "
        "training request to a finished, aligned package with ChatGPT, Claude, Gemini and an AI image tool: "
        "setting up the toolkit and a prompt library, analysing the need, audience and objectives, and "
        "structuring the course and its lessons; then generating content, activities and scenarios, creating "
        "quizzes, assessments and rubrics, producing scripts, visuals and job aids, aligning everything to the "
        "outcomes and quality-checking the AI output, and assembling the facilitator and learner package. A "
        "Meridian training brief is supplied in `reference-pack/`; use your own non-confidential course "
        "wherever you prefer. There is **no assessment** — each lab verifies itself with a 'Test it' step.\n"
    )
    md.append("| Day | Topic | Lab | Title |")
    md.append("|---:|---|---:|---|")
    md.extend(rows)
    md.append("")
    md.append("## Tools\n")
    md.append("See [tools.md](tools.md) for the accounts and tools used across the labs, and "
              "[reference-pack/](reference-pack/) for the Meridian training brief.")
    return "\n".join(md) + "\n"


def main():
    os.makedirs(LABS, exist_ok=True)
    # remove stale lab-*.md so renamed labs don't linger
    for old in glob.glob(os.path.join(LABS, "lab-*.md")):
        os.remove(old)
    files = {}
    for lab in LABSLIST:
        fn = lab_filename(lab)
        files[lab["num"]] = fn
        with open(os.path.join(LABS, fn), "w", encoding="utf-8") as fh:
            fh.write(build_lab(lab))
        print("wrote labs/" + fn)
    with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(build_readme(files))
    print("wrote labs/README.md")


if __name__ == "__main__":
    main()
