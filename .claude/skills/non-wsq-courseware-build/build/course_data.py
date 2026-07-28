"""
SINGLE SOURCE OF TRUTH — C1176 Generative AI for Instructional Design (non-WSQ).

An intensive, one-day, hands-on course on using generative AI to plan courses,
write learning content, create assessments and produce learning materials end to
end. Using general chat assistants (ChatGPT, Claude and Gemini) together with an
AI image tool, learners take one training course — the Meridian Service Excellence
course kit — from a training request to a finished, aligned course package:
setting up an AI toolkit and prompt library, analysing learning needs, audience
and objectives, structuring the course and its lessons, generating content,
activities and scenarios, creating quizzes, assessments and rubrics, producing
scripts, visuals and job aids, aligning everything to the outcomes and
quality-checking the AI output, then assembling and finalising the package.
Every artifact (PPT, LP, LG, LG.md) and every lab is generated from this module
+ data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C1176.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Generative AI for Instructional Design (C1176)"
SHORT_TITLE  = "Generative AI for Instructional Design (C1176)"   # used in output filenames
COURSE_CODE  = "C1176"                                            # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how generative AI supports instructional design, and set up an AI toolkit — general chat assistants (ChatGPT, Claude, Gemini) and an AI image tool — for learning-design work.",
    "LO2: Write effective, structured prompts for instructional-design tasks and build a reusable prompt library.",
    "LO3: Use generative AI to analyse learning needs, profile the target learners, and write clear, measurable learning objectives.",
    "LO4: Use AI to structure a course — a curriculum map and module breakdown aligned to the objectives.",
    "LO5: Use AI to build lesson plans and sequence the learning into a coherent, timed flow.",
    "LO6: Generate engaging learning content, activities and scenarios with AI.",
    "LO7: Create quizzes, assessments and rubrics aligned to the learning objectives with AI.",
    "LO8: Produce learner-facing scripts, visuals and job aids with AI.",
    "LO9: Align every artifact to the learning outcomes and quality-check AI output for accuracy, bias and instructional soundness.",
    "LO10: Assemble, review and finalise the complete course package — facilitator and learner materials — ready to deliver.",
]
LO_TITLES = [
    "ID AI toolkit",
    "Prompting for ID",
    "Needs & objectives",
    "Course structure",
    "Lesson plans",
    "Content & activities",
    "Quizzes & rubrics",
    "Scripts, visuals, job aids",
    "Align & quality-check",
    "Assemble & deliver",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with Generative AI for Instructional Design",
         subtitle="Introduction to instructional design and generative AI · Setting up AI tools for learning design · Analysing learning needs, audiences and objectives with AI · Structuring courses and lessons with AI",
         weighting="50%",
         concepts=[
            "Instructional design in one view — instructional design is the systematic process of turning a learning need into an effective learning experience: you analyse the audience and goals, define measurable objectives, design and develop content and assessment, then implement and evaluate — the ADDIE cycle, or a backward-design flow from outcomes to activities.",
            "Generative AI for instructional design — a generative AI assistant is a drafting and design partner across the whole ID workflow; it drafts needs analyses, objectives, course outlines, content, activities, assessments and job aids, turning days of design work into a fast first draft that you review and refine.",
            "What AI is good (and not good) at — AI is strong at drafting, structuring, rephrasing and generating options at speed; it does not know your real learners, your organisation's context or your subject-matter truth, so you supply the facts, the audience insight and the pedagogical judgement.",
            "Two anchors: outcomes and audience — every good design decision traces back to who the learners are and what they must be able to DO afterwards; you use AI to get sharp on both before you generate a single slide, activity or quiz.",
            "Popular GenAI tools — ChatGPT, Claude and Gemini all take a text prompt and return a draft; paired with an AI image tool they cover analysis, content, assessment and visuals. The prompting and review skills you learn here transfer across all of them.",
            "The generate–review–refine loop — every AI task follows the same loop: you prompt, the AI drafts, you review it critically against your objectives and audience, and you refine with follow-up prompts and your own edits until it is right. This loop drives every lab in the course.",
            "Prompting is the core skill — a good ID prompt gives the AI a role (an instructional designer), the context (audience, level, mode, constraints), the exact task, the format you want back and any constraints; a vague ask gives generic content, a structured ask gives usable content.",
            "A reusable prompt library — the same ID tasks recur for every course (needs analysis, objectives, outlines, content, quizzes, rubrics, job aids), so you save your best prompts as reusable templates you can run for any future course.",
            "Learning objectives and alignment — clear, measurable objectives written with observable action verbs (for example Bloom's taxonomy) are the backbone of a course; content, activities and assessment must all align to them, and AI helps you draft objectives and check that alignment.",
            "Human judgement, accuracy and ethics — AI drafts and suggests, but you verify every fact with a subject expert, check examples for bias and stereotypes, protect learner and organisational data, respect copyright, and own the instructional quality of everything you publish.",
         ]),
    dict(num=2, code="02",
         title="Creating Learning Content and Assessments with AI",
         subtitle="Generating content, activities and scenarios · Creating quizzes, assessments and rubrics · Producing scripts, visuals and job aids · Aligning to outcomes and quality-checking AI output",
         weighting="50%",
         concepts=[
            "From structure to content — AI turns your objectives and outline into concrete learning content: clear explanations, relatable examples, analogies and the words a learner reads or hears, which you shape to your audience's level and context.",
            "Activities and scenarios — learning sticks when learners DO something; AI generates practice activities, discussion prompts, role-plays, branching scenarios and case studies that let learners apply the content rather than just read it.",
            "Writing for learning, not documents — AI helps you chunk content into digestible pieces, write in plain, active language at the right reading level, and keep a consistent, encouraging tone across the whole course.",
            "Assessment aligned to objectives — good assessment measures the stated objectives at the right level; AI drafts quiz questions, scenario questions and performance tasks, which you check for validity, fairness and alignment before use.",
            "Quizzes and question quality — AI writes multiple-choice, true/false, matching and short-answer items with plausible distractors and answer guides; you review each for exactly one correct answer, no giveaway cues, and a clear link to an objective.",
            "Rubrics and feedback — AI drafts clear, criteria-based rubrics and model feedback for open-ended tasks, so grading is consistent and learners know what good looks like; you calibrate the criteria and performance levels to your standard.",
            "Scripts, visuals and job aids — AI drafts narration scripts and storyboards for e-learning or video, image and slide prompts for visuals, and concise job aids, checklists and quick-reference guides that learners keep and use after the course.",
            "Media, plain language and accessibility — AI helps you write alt text, captions and plain-language versions and check that content is inclusive and accessible, so every learner — including those using assistive technology — can use the material.",
            "Aligning to outcomes — you map every piece of content, every activity and every assessment item back to a learning objective; AI runs an alignment check that surfaces gaps (an objective with no assessment) and orphans (content that serves no objective).",
            "Quality-checking AI output — every AI draft is reviewed for accuracy, currency, bias, reading level and instructional soundness before it reaches a learner; the designer, not the AI, is accountable for the quality of what is delivered.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Build the Meridian Service Excellence course kit end to end with AI — set up an AI instructional-design toolkit and prompt library, analyse the learning need, audience and objectives, and structure the course and its lessons; then generate the learning content, activities and scenarios, create quizzes, assessments and rubrics, produce scripts, visuals and job aids, align everything to the outcomes and quality-check the AI output, and assemble the finished facilitator and learner package",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The day totals exactly 480 scheduled minutes
# (excluding the 1-hour lunch); the 30 minutes of tea breaks sit inside that, so
# the instructional total is 7.5 hours.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:00","9:20",20,"admin","Welcome, course introduction, ground rules, and setup: signing in to ChatGPT, Claude and Gemini and an AI image tool, and confirming each tool is ready for the labs"),
        ("9:20","10:00",40,"topic","TOPIC 01 — Getting Started with Generative AI for Instructional Design: introduction to instructional design and generative AI; setting up AI tools for learning design; analysing learning needs, audiences and objectives with AI; structuring courses and lessons with AI (concepts + live demo)"),
        ("10:00","10:45",45,"lab","Hands-on: "+lab_titles([1])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([2,3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:35",35,"lab","Hands-on: "+lab_titles([5])),
        ("14:35","15:05",30,"topic","TOPIC 02 — Creating Learning Content and Assessments with AI: generating content, activities and scenarios; creating quizzes, assessments and rubrics; producing scripts, visuals and job aids; aligning to outcomes and quality-checking AI output (concepts + live demo)"),
        ("15:05","16:15",70,"lab","Hands-on: "+lab_titles([6,7])),
        ("16:15","16:30",15,"break","Tea break"),
        ("16:30","17:50",80,"lab","Hands-on: "+lab_titles([8,9,10])),
        ("17:50","18:00",10,"recap","Course wrap-up, delivering the Meridian Service Excellence course kit, responsible-AI, accuracy and alignment recap, and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Generative AI for Instructional Design Really Is",
    concepts=[
        "A partner for the whole workflow — you describe an instructional-design task in words and AI returns a usable first draft (a needs analysis, objectives, an outline, content, a quiz, a rubric, a job aid) in seconds, which you then review and refine.",
        "Outcomes and audience first — the craft is not making materials faster; it is being clear on who your learners are and what they must be able to do, then using AI to design a course that gets them there.",
        "Prompt, review, own — the workflow is always the same: give a structured prompt, review and correct the draft against your objectives, and take ownership of the result. The AI drafts; you decide, verify and stand behind the quality.",
        "Aligned end to end — every piece of content, activity and assessment traces back to a learning objective; AI helps you keep that alignment tight from analysis through to the finished package.",
    ],
    framework_title="The AI-Assisted Instructional-Design Workflow",
    framework=[
        ("Analyse", "Use AI to clarify the learning need, profile the learners, and write clear, measurable objectives — you supply the real context and verify the facts."),
        ("Design", "Structure the course into a curriculum map, modules and lesson plans, sequenced and timed so the learning flows logically toward the objectives."),
        ("Develop", "Turn the design into learning content, activities and scenarios, quizzes, assessments and rubrics, and scripts, visuals and job aids."),
        ("Align", "Map every artifact back to an objective and quality-check every AI draft for accuracy, bias, reading level and instructional soundness."),
        ("Deliver", "Assemble the facilitator and learner materials into one consistent package, finalise it, and hand it over ready to run."),
    ],
    statement=dict(
        headline="Generative AI gives you a fast first draft of every part of a course — the craft is prompting well, keeping outcomes and learners at the centre, verifying the facts, and owning the instructional quality yourself.",
        body="This course is hands-on: you take one training course — the Meridian Service Excellence course kit, a short blended customer-service course for a fictional Singapore retail chain's new frontline staff — from a training request to a finished, aligned course package, using ChatGPT, Claude, Gemini and an AI image tool.",
        kicker="THE INSTRUCTIONAL-DESIGN RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("An AI instructional-design toolkit", ["ChatGPT, Claude, Gemini and an image tool set up", "A reusable ID prompt library", "A needs analysis, learner personas and objectives"]),
        ("A structured course design", ["A curriculum map aligned to the objectives", "Module and lesson breakdowns", "Sequenced, timed lesson plans"]),
        ("Developed learning materials", ["Learning content, activities and scenarios", "Quizzes, assessments and rubrics", "Scripts, visuals and job aids"]),
        ("An aligned, finished package", ["An objective-by-artifact alignment check", "A quality-check for accuracy and bias", "An assembled facilitator and learner package"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the AI technique on the shared Meridian Service Excellence example.",
        "You run it yourself in ChatGPT, Claude, Gemini or your image tool using the supplied Meridian training brief.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You review and refine — correct the draft, fix any invented fact, and align it to your objectives — until it meets the standard.",
        "You keep the reviewed output — each becomes the next part of your Meridian Service Excellence course kit.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Generative AI for Instructional Design (C1176) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 10 hands-on labs, in the order you "
    "will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected deliverable — the Meridian Service Excellence course kit, a short "
    "blended customer-service course for the new frontline staff of a fictional Singapore retail chain, Meridian "
    "Retail Group. You start in Lab 1 by setting up ChatGPT, Claude, Gemini and an AI image tool as an "
    "instructional-design toolkit, then in every lab you take the course one stage further — a reusable prompt "
    "library, a needs analysis with learner personas and measurable objectives, a curriculum map, sequenced "
    "lesson plans, learning content with activities and scenarios, quizzes, assessments and rubrics, scripts, "
    "visuals and job aids, an alignment and quality check, and finally an assembled, finished facilitator and "
    "learner package ready to deliver. A Meridian training brief with the context you need is supplied in "
    "labs/reference-pack/; you may substitute your own non-confidential course wherever you prefer."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection — every generative feature runs in the cloud.",
        "Access to at least one general chat assistant — ChatGPT (chat.openai.com), Claude (claude.ai) or Gemini (gemini.google.com); a free account for each is enough to follow the labs, and the trainer will confirm what is available.",
        "Access to an AI image tool for the visuals and job aids (the image generation built into ChatGPT, Gemini or Microsoft Copilot / Designer is enough; a dedicated tool such as Adobe Firefly or Canva also works).",
        "A signed-in account for each tool you will use, tested before Lab 1 with a simple 'hello' prompt so you know it responds, plus somewhere to keep your work (a documents folder or notes app).",
        "The supplied Meridian training brief (the organisation, the audience, the business need and the course constraints) in labs/reference-pack/ — or a few notes from your own non-confidential course to use instead.",
    ],
    verify_text="Before Lab 1, confirm you can sign in to at least one chat assistant and an AI image tool, send a simple prompt and get a reply, and that you have the Meridian training brief to hand. If anything is missing, tell the trainer.",
    verify_code="Open chat.openai.com (ChatGPT) · claude.ai (Claude) · gemini.google.com (Gemini)  ·  sign in  ·  send \"Hello, are you ready to help me design a training course?\"  ·  confirm a reply  ·  run one test image in your image tool",
    conventions=[
        "Placeholders such as <YOUR TOPIC>, <YOUR AUDIENCE> or <PASTE OBJECTIVES> are replaced with your own values before you send a prompt.",
        "Prompts to paste into ChatGPT, Claude or Gemini — or your image tool where a step says so — are shown in the 'Prompt to use' blocks; adapt the bracketed parts to your own course.",
        "Where a lab says 'any assistant', use whichever chat tool you prefer; the visual steps use an AI image tool, and the prompting and review skills work across all of them.",
        "Every lab ends with a 'Test it' step — an explicit check that the reviewed output meets the standard before you move on.",
        "Keep every reviewed output and prompt in one project folder (Meridian-Service-Course-Kit) so your course package stays together, consistent and aligned.",
    ],
)
LAB_NOTE = (
    "Use only topics, data and material you are authorised to use. Do not paste confidential employee data, "
    "personal information, credentials or proprietary training material into a public AI tool. Use the supplied "
    "Meridian training brief rather than real client material, treat every AI output — especially facts, "
    "examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and "
    "checked for bias, and be transparent about AI assistance where appropriate before the course reaches real "
    "learners."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have taken one training course — the Meridian Service Excellence course kit — from a training request to a finished, aligned course package in a single day, using ChatGPT, Claude, Gemini and an AI image tool as drafting and design partners while keeping the outcomes, the learners and the instructional quality your own.",
    sections=[
        dict(title="What you built", bullets=[
            "An AI instructional-design toolkit — ChatGPT, Claude, Gemini and an AI image tool set up, plus a reusable ID prompt library.",
            "A clear foundation — a needs analysis, learner personas and clear, measurable learning objectives for the Meridian course.",
            "A structured design — a curriculum map, module breakdown and sequenced, timed lesson plans aligned to the objectives.",
            "Developed materials — learning content, activities and scenarios, quizzes, assessments and rubrics, and scripts, visuals and job aids.",
            "An aligned, finished package — an objective-by-artifact alignment check, a quality-check for accuracy and bias, and an assembled facilitator and learner package ready to deliver.",
        ]),
        dict(title="What to do next", bullets=[
            "Rebuild a course for a real, non-confidential training need of your own using the same workflow and prompt library.",
            "Introduce your saved prompts to your team so everyone drafts needs analyses, objectives, content, assessments and job aids the same way.",
            "Always start with the outcomes and the learners before you generate a single activity — AI makes a well-designed course faster, not a missing design.",
            "Keep the quality habit: verify every fact with a subject expert, check for bias, confirm alignment to the objectives, and stand behind everything before it reaches a learner.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the course kit for your own real, non-confidential training need, from needs analysis and objectives through to an assembled, aligned package.",
    "Introduce your prompt library and the analyse → design → develop → align → deliver workflow to your team so the practice sticks.",
    "Review each lab's detailed steps in this guide and re-create the course package in your own AI tools.",
]
LG_GLOSSARY = [
    ("Instructional design (ID)", "The systematic process of turning a learning need into an effective learning experience — analysing, designing, developing, implementing and evaluating learning."),
    ("Generative AI assistant", "A general-purpose chat tool (ChatGPT, Claude, Gemini) that generates text drafts and analysis from a prompt."),
    ("AI image tool", "A tool that generates images from a text prompt (built into ChatGPT, Gemini or Copilot, or a dedicated tool like Adobe Firefly or Canva), used here for visuals and job aids."),
    ("ChatGPT / Claude / Gemini", "The three widely-used chat assistants used in this course to analyse, write, structure and refine course material."),
    ("ADDIE", "A common instructional-design model with five phases — Analyse, Design, Develop, Implement, Evaluate — that structures the course-building process."),
    ("Backward design", "Designing a course from the intended outcomes backwards: define what learners must be able to do, then the assessment, then the content and activities."),
    ("Needs analysis", "The up-front study of the performance gap, the business need and the learners, that decides what a course must achieve and for whom."),
    ("Learner persona", "A believable, research-based profile of a representative learner group — their role, prior knowledge, motivation, context and constraints — used to keep design learner-centred."),
    ("Learning objective", "A clear, measurable statement of what a learner will be able to do after the learning, written with an observable action verb."),
    ("Bloom's taxonomy", "A framework of cognitive levels (remember, understand, apply, analyse, evaluate, create) whose action verbs are used to write objectives and pitch assessment at the right level."),
    ("Alignment", "The principle that content, activities and assessment all serve the stated learning objectives, with no gaps or orphans."),
    ("Curriculum map", "A high-level plan of a course — its modules, the objectives each covers, and the sequence — agreed before detailed development."),
    ("Lesson plan", "A detailed plan for a single lesson or session — its objective, timing, activities, materials and assessment."),
    ("Chunking", "Breaking content into small, digestible pieces so it is easier to learn and remember."),
    ("Learning activity", "Anything that has learners do something — a discussion, exercise, role-play or scenario — to apply and practise the content."),
    ("Scenario / branching scenario", "A realistic situation learners work through, sometimes with choices that branch to different outcomes, to practise decisions in a safe setting."),
    ("Case study", "An extended, realistic example that learners analyse to apply concepts to a real-world situation."),
    ("Formative vs summative", "A formative check gives feedback during learning; a summative check measures achievement of the objectives at the end."),
    ("Quiz item types", "Common question forms — multiple-choice, true/false, matching, short-answer — each suited to different objectives and cognitive levels."),
    ("Distractor", "An incorrect but plausible option in a multiple-choice question; good distractors reflect common misconceptions without giving the answer away."),
    ("Answer guide", "The record of the correct answer (and rationale) for each quiz item, used to score and review learners' responses."),
    ("Rubric", "A scoring guide that lists the criteria for a task and describes each performance level, so grading is consistent and expectations are clear."),
    ("Feedback", "Information given to a learner about their performance that helps them improve; AI can draft model feedback that you calibrate."),
    ("Storyboard", "A plan for an e-learning screen or video sequence showing, for each frame, the on-screen content, the narration and the visuals."),
    ("Narration script", "The spoken words for a video or e-learning module, written to be heard rather than read."),
    ("Job aid", "A concise, take-away reference — a checklist, quick-reference card or one-pager — that supports performance on the job after the course."),
    ("Accessibility", "Designing content so every learner can use it, including alt text for images, captions for media, plain language and support for assistive technology."),
    ("Alt text", "A short text description of an image that lets learners using a screen reader understand what the image shows."),
    ("Prompt", "The instruction you give the AI; a structured prompt with role, context, task, format and constraints produces a far better draft than a vague one."),
    ("Prompt library", "A saved, reusable set of prompt templates for the recurring ID tasks — needs analysis, objectives, outlines, content, quizzes, rubrics, job aids."),
    ("Generate–review–refine loop", "The core AI workflow — prompt, review the draft critically against objectives and audience, then refine with follow-up prompts and your own edits until it is right."),
    ("Human-in-the-loop", "Keeping a person responsible for reviewing, fact-checking, correcting and approving every AI output before it is used with learners."),
    ("Hallucination", "A confident but false or invented statement, fact or example from an AI, which is why every output must be fact-checked with a subject expert."),
    ("Bias check", "Reviewing content and examples for stereotypes or unfair assumptions so the material is inclusive and represents learners fairly."),
    ("Responsible AI use", "Using AI safely and ethically — protecting confidential data, verifying facts, checking for bias, respecting copyright, and being transparent about AI assistance."),
    ("Course package", "The assembled set of facilitator and learner materials — plans, content, activities, assessments, rubrics and job aids — ready to deliver a course."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C1176 Generative AI for Instructional Design courseware.", TRAINER),
]
