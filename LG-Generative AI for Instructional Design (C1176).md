# Generative AI for Instructional Design (C1176) — Learner Guide

**Course Code:** C1176  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 27 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Generative AI for Instructional Design  (50%)](#topic-01--getting-started-with-generative-ai-for-instructional-design--50)
  - [Lab 1 — Set Up Your AI Instructional-Design Toolkit](#lab-1--set-up-your-ai-instructional-design-toolkit)
  - [Lab 2 — Write Effective Prompts for Instructional Design](#lab-2--write-effective-prompts-for-instructional-design)
  - [Lab 3 — Analyse Learning Needs, Audience and Objectives with AI](#lab-3--analyse-learning-needs-audience-and-objectives-with-ai)
  - [Lab 4 — Structure the Course Curriculum with AI](#lab-4--structure-the-course-curriculum-with-ai)
  - [Lab 5 — Build the Lesson Plans and Learning Sequence with AI](#lab-5--build-the-lesson-plans-and-learning-sequence-with-ai)
- [Topic 02 — Creating Learning Content and Assessments with AI  (50%)](#topic-02--creating-learning-content-and-assessments-with-ai--50)
  - [Lab 6 — Generate Learning Content, Activities and Scenarios with AI](#lab-6--generate-learning-content-activities-and-scenarios-with-ai)
  - [Lab 7 — Create Quizzes, Assessments and Rubrics with AI](#lab-7--create-quizzes-assessments-and-rubrics-with-ai)
  - [Lab 8 — Produce Scripts, Visuals and Job Aids with AI](#lab-8--produce-scripts-visuals-and-job-aids-with-ai)
  - [Lab 9 — Align to Outcomes and Quality-Check the AI Output](#lab-9--align-to-outcomes-and-quality-check-the-ai-output)
  - [Lab 10 — Assemble, Review and Finalise the Course Package](#lab-10--assemble-review-and-finalise-the-course-package)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Generative AI for Instructional Design (C1176) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 10 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build a single, connected deliverable — the Meridian Service Excellence course kit, a short blended customer-service course for the new frontline staff of a fictional Singapore retail chain, Meridian Retail Group. You start in Lab 1 by setting up ChatGPT, Claude, Gemini and an AI image tool as an instructional-design toolkit, then in every lab you take the course one stage further — a reusable prompt library, a needs analysis with learner personas and measurable objectives, a curriculum map, sequenced lesson plans, learning content with activities and scenarios, quizzes, assessments and rubrics, scripts, visuals and job aids, an alignment and quality check, and finally an assembled, finished facilitator and learner package ready to deliver. A Meridian training brief with the context you need is supplied in labs/reference-pack/; you may substitute your own non-confidential course wherever you prefer.


## Course Learning Outcomes

- LO1: Explain how generative AI supports instructional design, and set up an AI toolkit — general chat assistants (ChatGPT, Claude, Gemini) and an AI image tool — for learning-design work.
- LO2: Write effective, structured prompts for instructional-design tasks and build a reusable prompt library.
- LO3: Use generative AI to analyse learning needs, profile the target learners, and write clear, measurable learning objectives.
- LO4: Use AI to structure a course — a curriculum map and module breakdown aligned to the objectives.
- LO5: Use AI to build lesson plans and sequence the learning into a coherent, timed flow.
- LO6: Generate engaging learning content, activities and scenarios with AI.
- LO7: Create quizzes, assessments and rubrics aligned to the learning objectives with AI.
- LO8: Produce learner-facing scripts, visuals and job aids with AI.
- LO9: Align every artifact to the learning outcomes and quality-check AI output for accuracy, bias and instructional soundness.
- LO10: Assemble, review and finalise the complete course package — facilitator and learner materials — ready to deliver.


## Before You Start — Preparation

**What you need**

- A laptop (Windows or Mac) with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection — every generative feature runs in the cloud.
- Access to at least one general chat assistant — ChatGPT (chat.openai.com), Claude (claude.ai) or Gemini (gemini.google.com); a free account for each is enough to follow the labs, and the trainer will confirm what is available.
- Access to an AI image tool for the visuals and job aids (the image generation built into ChatGPT, Gemini or Microsoft Copilot / Designer is enough; a dedicated tool such as Adobe Firefly or Canva also works).
- A signed-in account for each tool you will use, tested before Lab 1 with a simple 'hello' prompt so you know it responds, plus somewhere to keep your work (a documents folder or notes app).
- The supplied Meridian training brief (the organisation, the audience, the business need and the course constraints) in labs/reference-pack/ — or a few notes from your own non-confidential course to use instead.

**Verify your setup**

Before Lab 1, confirm you can sign in to at least one chat assistant and an AI image tool, send a simple prompt and get a reply, and that you have the Meridian training brief to hand. If anything is missing, tell the trainer.

```bash
Open chat.openai.com (ChatGPT) · claude.ai (Claude) · gemini.google.com (Gemini)  ·  sign in  ·  send "Hello, are you ready to help me design a training course?"  ·  confirm a reply  ·  run one test image in your image tool
```

**Conventions used in every lab**

- Placeholders such as <YOUR TOPIC>, <YOUR AUDIENCE> or <PASTE OBJECTIVES> are replaced with your own values before you send a prompt.
- Prompts to paste into ChatGPT, Claude or Gemini — or your image tool where a step says so — are shown in the 'Prompt to use' blocks; adapt the bracketed parts to your own course.
- Where a lab says 'any assistant', use whichever chat tool you prefer; the visual steps use an AI image tool, and the prompting and review skills work across all of them.
- Every lab ends with a 'Test it' step — an explicit check that the reviewed output meets the standard before you move on.
- Keep every reviewed output and prompt in one project folder (Meridian-Service-Course-Kit) so your course package stays together, consistent and aligned.


## Topic 01 — Getting Started with Generative AI for Instructional Design  (50%)

Introduction to instructional design and generative AI · Setting up AI tools for learning design · Analysing learning needs, audiences and objectives with AI · Structuring courses and lessons with AI

**Key concepts**

- Instructional design in one view — instructional design is the systematic process of turning a learning need into an effective learning experience: you analyse the audience and goals, define measurable objectives, design and develop content and assessment, then implement and evaluate — the ADDIE cycle, or a backward-design flow from outcomes to activities.
- Generative AI for instructional design — a generative AI assistant is a drafting and design partner across the whole ID workflow; it drafts needs analyses, objectives, course outlines, content, activities, assessments and job aids, turning days of design work into a fast first draft that you review and refine.
- What AI is good (and not good) at — AI is strong at drafting, structuring, rephrasing and generating options at speed; it does not know your real learners, your organisation's context or your subject-matter truth, so you supply the facts, the audience insight and the pedagogical judgement.
- Two anchors: outcomes and audience — every good design decision traces back to who the learners are and what they must be able to DO afterwards; you use AI to get sharp on both before you generate a single slide, activity or quiz.
- Popular GenAI tools — ChatGPT, Claude and Gemini all take a text prompt and return a draft; paired with an AI image tool they cover analysis, content, assessment and visuals. The prompting and review skills you learn here transfer across all of them.
- The generate–review–refine loop — every AI task follows the same loop: you prompt, the AI drafts, you review it critically against your objectives and audience, and you refine with follow-up prompts and your own edits until it is right. This loop drives every lab in the course.
- Prompting is the core skill — a good ID prompt gives the AI a role (an instructional designer), the context (audience, level, mode, constraints), the exact task, the format you want back and any constraints; a vague ask gives generic content, a structured ask gives usable content.
- A reusable prompt library — the same ID tasks recur for every course (needs analysis, objectives, outlines, content, quizzes, rubrics, job aids), so you save your best prompts as reusable templates you can run for any future course.
- Learning objectives and alignment — clear, measurable objectives written with observable action verbs (for example Bloom's taxonomy) are the backbone of a course; content, activities and assessment must all align to them, and AI helps you draft objectives and check that alignment.
- Human judgement, accuracy and ethics — AI drafts and suggests, but you verify every fact with a subject expert, check examples for bias and stereotypes, protect learner and organisational data, respect copyright, and own the instructional quality of everything you publish.


### Lab 1 — Set Up Your AI Instructional-Design Toolkit

Learning outcome: Sign in to ChatGPT, Claude, Gemini and an AI image tool, run your first instructional-design prompts, and learn the generate–review–refine loop that every later lab uses..

Goal: This lab gets you comfortable with the tools before any real design work begins. You open the chat assistants (ChatGPT, Claude and Gemini), confirm you are signed in, and run a simple instructional-design prompt so you see how each drafts learning content, then run the same prompt in a second assistant to feel how they differ. You open an AI image tool, sign in, and generate a quick throwaway visual so you can see what an image tool does for learning materials. You note what AI is genuinely good at for instructional design (a fast draft, structure, options) and where it needs you (your real learners, your subject-matter truth, your pedagogical judgement). By the end you understand the describe -> generate -> review -> refine loop that is the heart of every lab. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

Your AI instructional-design toolkit set up and tested — at least one chat assistant and an AI image tool signed in and responding — a first throwaway AI-generated draft and visual, and a clear, written understanding of the generate–review–refine loop and what AI can and cannot do for an instructional designer.   (Tools: ChatGPT, Claude, Gemini, an AI image tool, account sign-in, first prompts, comparing assistants, the generate–review–refine loop.)

**Step-by-step**

1. Create a project folder on your machine called 'Meridian-Service-Course-Kit' so every file and note you make today stays together. Open ChatGPT (chat.openai.com), Claude (claude.ai) and Gemini (gemini.google.com) in browser tabs and confirm you are signed in to at least one.
2. In one chat assistant, run a simple first prompt to see how it drafts learning content. Paste the prompt below and read the reply.

   ```bash
   You are an instructional designer. In five short bullet points, explain what makes a short workplace training course effective for new frontline retail staff. Keep each bullet to one sentence.
   ```

3. Run the exact same prompt in a second assistant and compare the two replies. Notice differences in tone, length and structure — the skill you learn transfers across all of them, so use whichever you prefer.

   ```bash
   You are an instructional designer. In five short bullet points, explain what makes a short workplace training course effective for new frontline retail staff. Keep each bullet to one sentence.
   ```

4. Open your AI image tool (image generation in ChatGPT or Gemini, Microsoft Copilot / Designer, or a tool like Adobe Firefly or Canva), sign in, and generate a quick throwaway visual so you can see what an image tool produces for learning materials. Paste the prompt below.

   ```bash
   A simple, friendly flat illustration of a retail associate warmly greeting a customer in a bright neighbourhood store, clean and modern, no text.
   ```

5. Look at what the image tool produced — a usable draft visual generated in seconds. Note that it is a fast starting point, not a finished course graphic. You will not keep this one; it is only to feel the tool.
6. In one line each, write what the AI did well (fast draft, structure, instant visual) and where it needs you (it does not know Meridian's real service standards, your learners, or your judgement). This good/not-good picture guides how you use AI all day.
7. Open the supplied Meridian training brief (labs/reference-pack/): the organisation, the audience, the business need and the course constraints. Skim it so you know the course you are about to design.
8. Save your notes into your Meridian-Service-Course-Kit folder. Write one line, in your own words, describing the generate -> review -> refine loop — you rely on it in every later lab.

**Test it**

You have signed in to at least one chat assistant and an AI image tool, run the same prompt in two assistants and compared them, generated a throwaway visual, written a one-line note on what AI is and is not good at for instructional design, skimmed the Meridian training brief, and described the generate–review–refine loop in your own words — all saved in your Meridian-Service-Course-Kit folder.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 2 — Write Effective Prompts for Instructional Design

Learning outcome: Turn a vague ask into a strong, structured prompt (role, context, task, format, constraints) for instructional-design tasks, and save a reusable prompt library for the work you repeat for every course..

Goal: A good result starts with a good prompt, not a lucky one. In this lab you read the Meridian training brief and write a deliberately vague prompt first, so you see how generic the result is. You then rebuild it with five clear parts — a role for the AI, the context (audience, level, mode, constraints), the exact task, the format you want back, and any constraints — and watch the draft become genuinely usable. You run small single-change edits to feel how each part matters, then save your best versions as a reusable prompt library with clearly marked slots, covering the tasks you repeat for every course: needs analysis, objectives, outline, content, activities, quizzes, rubrics and job aids. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

A structured instructional-design prompt built from role, context, task, format and constraints, plus a reusable prompt library with clearly marked slots for the recurring ID tasks, saved in your project folder.   (Tools: ChatGPT / Claude / Gemini, the structured prompt framework (role, context, task, format, constraints), prompt iteration, a reusable prompt library.)

**Step-by-step**

1. Open the Meridian training brief and note two things you will reuse in every prompt: who the learners are (new frontline retail associates in their first week) and the goal (deliver great customer service, including handling complaints).
2. Write a deliberately vague first prompt in any assistant and generate, so you can see the generic result. Paste the prompt below and read how unfocused the reply is.

   ```bash
   Write a customer service training course.
   ```

3. Rebuild the prompt with a role and the context, and regenerate. Paste the prompt below and compare it with the vague version.

   ```bash
   You are an experienced instructional designer. Context: Meridian Retail Group is onboarding new frontline retail associates, who are often first-time workers, and needs a short, practical, roughly three-hour blended course on delivering great customer service, including handling complaints and knowing when to escalate. Draft the high-level topics this course should cover.
   ```

4. Now add the exact task, the format you want back, and clear constraints, and regenerate. Paste the prompt below.

   ```bash
   As the same instructional designer, list the 4 to 6 modules this course should have. For each module give a short title and one line on what learners will be able to do after it. Present it as a numbered list, keep it practical and beginner-friendly, and do not invent Meridian-specific policies — leave clear placeholders where a real company policy is needed.
   ```

5. Put the vague result and the structured result side by side. Note in one line how much more usable the structured prompt was — this is the core lesson of the day.
6. Run two or three single-change edits to feel how each part steers the result — for example change the audience to 'experienced staff moving into a supervisor role', or change the mode to 'a self-paced e-learning module only' — and note which you would keep for Meridian.
7. Save a reusable prompt library in your project folder: templates for needs analysis, learning objectives, course outline, content, activities, quiz items, rubrics and job aids, each with clearly marked slots — [ROLE], [CONTEXT], [AUDIENCE], [TASK], [FORMAT], [CONSTRAINTS] — that you fill in for any future course.

**Test it**

You have compared a vague prompt with a structured one built from role, context, task, format and constraints, seen how much better the structured prompt performs, run single-change edits to feel each part, and saved a reusable prompt library with marked slots for the recurring instructional-design tasks in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 3 — Analyse Learning Needs, Audience and Objectives with AI

Learning outcome: Use AI to analyse the learning need, profile the target learners as personas, and write clear, measurable learning objectives — the foundation every later artifact must align to..

Goal: A good course rests on a clear need, a real understanding of the learners, and sharp objectives. In this lab you use a chat assistant to turn the Meridian training brief into a short needs analysis — the performance gap, the business need and what success looks like — then profile the learners as one or two personas (their role, prior knowledge, motivation and constraints). Crucially, you then write measurable learning objectives using observable action verbs (Bloom's taxonomy), and you check them: each objective must be observable, achievable in the time, and tied to the real on-the-job need — not a vague 'understand customer service'. You verify any factual claim against the brief and replace anything the AI invented with the brief's real context or a clear [VERIFY] placeholder. This foundation anchors every lab that follows. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

A short needs analysis (performance gap, business need, success measure), one or two learner personas, and a set of clear, measurable, Bloom-aligned learning objectives for the Meridian course — checked for observability and fit, and grounded in the supplied brief.   (Tools: ChatGPT / Claude / Gemini, needs / gap analysis, learner personas, writing measurable objectives, Bloom's taxonomy, verifying against the brief.)

**Step-by-step**

1. Open the Meridian training brief and note the business need (why the course exists) and the audience (new frontline retail associates in their first week).
2. Draft a short needs analysis with AI. Paste the prompt below, with the relevant brief details pasted in.

   ```bash
   You are an instructional designer. From this training brief: '[PASTE BRIEF DETAILS]', write a short needs analysis: the performance gap (what learners cannot yet do), the business need it serves, any constraints (time, mode, prior knowledge), and one clear measure of success. Keep it to a page; do not invent facts not in the brief — mark anything you would need to confirm.
   ```

3. Profile the learners as personas. Paste the prompt below.

   ```bash
   For the same course, create one or two learner personas for new frontline retail associates — often first-time workers. For each: a name and role, prior knowledge and confidence, what motivates them, their context and constraints, and what would make the training work for them. Keep them realistic and free of stereotypes.
   ```

4. Write measurable learning objectives. Paste the prompt below.

   ```bash
   Write 5 to 7 measurable learning objectives for this course, each starting 'By the end of this course, learners will be able to...' and using an observable action verb from Bloom's taxonomy (for example describe, demonstrate, apply, handle, decide). Make them achievable in a three-hour blended course and tied to the real on-the-job need. Avoid vague verbs like 'understand' or 'know'.
   ```

5. Pressure-test the objectives. Paste the prompt below and tighten any weak objective.

   ```bash
   Review these objectives for quality: is each one observable and measurable, achievable in the time, and tied to a real performance need? Flag any that are vague, too ambitious, or not assessable, and suggest a sharper version.
   ```

6. Verify against the brief: check every fact in the needs analysis and personas against the Meridian training brief, keep the brief's real context, and replace anything the AI invented with the brief's value or a clear [VERIFY] placeholder. Never carry an AI-invented fact into your design.
7. Save three things in your project folder: the needs analysis, the learner personas, and the final measurable objectives. These objectives are the spine every later lab must align to.

**Test it**

You have a short needs analysis, one or two realistic learner personas, and a set of clear, measurable, Bloom-aligned learning objectives — pressure-tested for observability and fit and verified against the supplied brief — saved in your project folder as the foundation for the course.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 4 — Structure the Course Curriculum with AI

Learning outcome: Turn the objectives into a curriculum map — the course's modules, the objectives each module covers, and a logical sequence — so the course has a clear structure before any content is written..

Goal: With the objectives set, you design the shape of the course. In this lab you use AI to turn your learning objectives into a curriculum map: the modules the course needs, which objective(s) each module covers, the key topics inside each, and a suggested time for each within the three-hour budget. You review it hard — checking every objective is covered by a module (no gaps) and every module serves an objective (no orphans), that the sequence builds logically from simple to complex, and that the total time is realistic. You use backward design thinking: each module exists to move learners toward an objective. This map is the blueprint you turn into detailed lesson plans in Lab 5 and fill with content in Topic 2. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

A curriculum map for the Meridian course — modules with their covered objectives, key topics and suggested timings within the three-hour budget — reviewed so every objective is covered, every module earns its place, and the sequence builds logically.   (Tools: ChatGPT / Claude / Gemini, curriculum mapping, backward design, sequencing, objective-to-module alignment, time budgeting.)

**Step-by-step**

1. Gather your inputs from Lab 3: the measurable learning objectives and the learner personas. The map must serve those objectives and those learners.
2. Generate the curriculum map. Paste the prompt below, with your objectives pasted in.

   ```bash
   You are an instructional designer using backward design. Using these learning objectives: '[PASTE OBJECTIVES]', design a curriculum map for a three-hour blended course. Give 4 to 6 modules; for each: a title, the objective(s) it addresses, the key topics inside it, the mode (workshop or e-learning), and a suggested time in minutes. Present it as a table and make the times add up to about three hours.
   ```

3. Check coverage and orphans. Paste the prompt below.

   ```bash
   Check this curriculum map against my objectives: is every objective covered by at least one module, and does every module clearly serve an objective? List any objective with no module (a gap) and any module that serves no objective (an orphan), and suggest fixes.
   ```

4. Check the sequence: confirm the modules build logically — foundational ideas (what great service is, knowing the customer) before harder skills (handling a complaint, escalation) — and reorder anything out of place so the learning flows.
5. Check the time budget: confirm the module timings add up to about three hours with room for a welcome and a wrap-up, and adjust any module that is over- or under-weighted for its objective.
6. Decide the blend: mark which modules are the facilitator-led workshop and which sit in the short e-learning module, so the structure matches the blended design in the brief.
7. Save the final curriculum map in your project folder. This is the blueprint — you turn it into detailed lesson plans in Lab 5 and fill it with content, activities and assessment in Topic 2.

**Test it**

You have a curriculum map of 4 to 6 modules, each mapped to the objective(s) it covers with key topics, mode and a time — with every objective covered, no orphan modules, a logical simple-to-complex sequence, and timings that add up to about three hours. Saved in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 5 — Build the Lesson Plans and Learning Sequence with AI

Learning outcome: Turn the curriculum map into detailed, timed lesson plans — each with its objective, a warm-up, content, an activity and a check — sequenced into a coherent flow ready to develop..

Goal: Now you take the curriculum map down to the level a facilitator can actually run. In this lab you prompt AI to expand each module into a lesson plan: the module's objective, a short opener or warm-up, the content to teach, at least one learning activity where learners do something, a quick check for understanding, the timing for each part, and the materials needed. You apply a simple, sound structure to every lesson (for example a hook, then teach, then practise, then check — an engagement-to-application flow) so learning is active, not a lecture. You review the plans for realistic timing and a smooth flow from lesson to lesson across the whole course. These lesson plans are the detailed spine you fill with real content, activities and assessment in Topic 2. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

A set of detailed, timed lesson plans for the Meridian course — each module with its objective, warm-up, content, at least one activity, a check for understanding, timings and materials — sequenced into one coherent flow, ready to develop in Topic 2.   (Tools: ChatGPT / Claude / Gemini, lesson planning, active-learning structure (hook–teach–practise–check), timing, sequencing lessons, materials lists.)

**Step-by-step**

1. Open your Lab 4 curriculum map — each module becomes a lesson plan in this lab.
2. Expand one module into a full lesson plan. Paste the prompt below, with that module's details pasted in.

   ```bash
   You are an instructional designer. Expand this module into a detailed lesson plan: '[PASTE ONE MODULE]'. Include the module's objective, a short warm-up or hook, the content to teach, at least one active learning activity where learners apply the content, a quick check for understanding, the timing in minutes for each part, and the materials or media needed. Use a hook -> teach -> practise -> check flow and keep it practical for a facilitator.
   ```

3. Generate the remaining lesson plans the same way, one per module, keeping the same structure so the whole course feels consistent and every lesson has an active element rather than pure lecture.
4. Check the timing. Paste the prompt below.

   ```bash
   Review these lesson plans for timing: do the parts within each lesson add up to the module's allotted time, and do all the lessons together fit a three-hour course with a welcome, a break and a wrap-up? Flag anything that will overrun and suggest what to trim.
   ```

5. Check the flow between lessons: confirm each lesson connects to the next, prior knowledge builds in the right order, and there are no abrupt jumps or repeated content across lessons.
6. Confirm active learning: make sure every lesson has at least one activity or discussion where learners do or say something, not just receive content — the point of the workshop is practice.
7. Save the full set of lesson plans in your project folder. This is the detailed spine of the course — you write its content and activities in Lab 6, its assessment in Lab 7, and its scripts, visuals and job aids in Lab 8.

**Test it**

You have a complete set of timed lesson plans, one per module, each with its objective, a warm-up, content, at least one active learning activity, a check for understanding, timings and materials — sequenced into one coherent, active, three-hour flow with realistic timing. Saved in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


## Topic 02 — Creating Learning Content and Assessments with AI  (50%)

Generating content, activities and scenarios · Creating quizzes, assessments and rubrics · Producing scripts, visuals and job aids · Aligning to outcomes and quality-checking AI output

**Key concepts**

- From structure to content — AI turns your objectives and outline into concrete learning content: clear explanations, relatable examples, analogies and the words a learner reads or hears, which you shape to your audience's level and context.
- Activities and scenarios — learning sticks when learners DO something; AI generates practice activities, discussion prompts, role-plays, branching scenarios and case studies that let learners apply the content rather than just read it.
- Writing for learning, not documents — AI helps you chunk content into digestible pieces, write in plain, active language at the right reading level, and keep a consistent, encouraging tone across the whole course.
- Assessment aligned to objectives — good assessment measures the stated objectives at the right level; AI drafts quiz questions, scenario questions and performance tasks, which you check for validity, fairness and alignment before use.
- Quizzes and question quality — AI writes multiple-choice, true/false, matching and short-answer items with plausible distractors and answer guides; you review each for exactly one correct answer, no giveaway cues, and a clear link to an objective.
- Rubrics and feedback — AI drafts clear, criteria-based rubrics and model feedback for open-ended tasks, so grading is consistent and learners know what good looks like; you calibrate the criteria and performance levels to your standard.
- Scripts, visuals and job aids — AI drafts narration scripts and storyboards for e-learning or video, image and slide prompts for visuals, and concise job aids, checklists and quick-reference guides that learners keep and use after the course.
- Media, plain language and accessibility — AI helps you write alt text, captions and plain-language versions and check that content is inclusive and accessible, so every learner — including those using assistive technology — can use the material.
- Aligning to outcomes — you map every piece of content, every activity and every assessment item back to a learning objective; AI runs an alignment check that surfaces gaps (an objective with no assessment) and orphans (content that serves no objective).
- Quality-checking AI output — every AI draft is reviewed for accuracy, currency, bias, reading level and instructional soundness before it reaches a learner; the designer, not the AI, is accountable for the quality of what is delivered.


### Lab 6 — Generate Learning Content, Activities and Scenarios with AI

Learning outcome: Turn the lesson plans into concrete learning content, active learning activities and a realistic scenario — chunked, written in plain language, and pitched at the learners' level..

Goal: With the lesson plans set, you develop the material learners actually work with. In this lab you feed a lesson plan to a chat assistant and have it draft the learning content: clear explanations, relatable examples and a simple model learners can use (for example a service-recovery method for handling complaints). You then generate active learning activities — a discussion prompt, a role-play, and a realistic branching scenario in which a customer complaint plays out and the learner chooses how to respond. You edit hard: you chunk long content into digestible pieces, rewrite it in plain, active, encouraging language at the learners' level, and check every example is realistic and free of bias. The result is developed content and activities ready to be assessed in Lab 7 and produced in Lab 8. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

Developed learning content for the Meridian course — clear, chunked explanations and examples plus a simple service model — with at least one discussion activity, one role-play and one realistic branching scenario, all in plain, active language pitched at the learners.   (Tools: ChatGPT / Claude / Gemini, content drafting, chunking, plain-language writing, activity design, role-plays, branching scenarios, bias check.)

**Step-by-step**

1. Open one lesson plan from Lab 5 — for example the complaint-handling lesson — as the input for this lab's content.
2. Draft the learning content for that lesson. Paste the prompt below, with the lesson plan pasted in.

   ```bash
   You are an instructional designer writing for new frontline retail staff who may be first-time workers. From this lesson plan: '[PASTE LESSON PLAN]', write the learning content: a clear explanation of the key idea, one or two relatable retail examples, and a simple step-by-step model learners can apply (for handling a complaint, use a short service-recovery method). Write in plain, warm, active language, and chunk it into short sections with headings.
   ```

3. Generate active learning activities. Paste the prompt below.

   ```bash
   For the same lesson, create three activities that get learners doing, not just reading: (1) a short discussion prompt, (2) a two-person role-play with a brief setup and roles, and (3) a realistic branching scenario where a customer makes a complaint and the learner chooses between three responses, with feedback for each choice. Keep them practical and set in a neighbourhood retail store.
   ```

4. Chunk and simplify. Paste the prompt below.

   ```bash
   Rewrite this content into short, digestible chunks with clear headings, plain language at about a secondary-school reading level, active voice, and a warm, encouraging tone. Cut jargon or explain it in one line.
   ```

5. Check realism and bias: read every example and the scenario, and confirm they are realistic for a Singapore neighbourhood store and free of stereotypes about customers or staff. Rewrite anything that feels unrealistic, unfair or that singles out any group.
6. Confirm alignment: check that this content and its activities actually serve the lesson's objective — cut anything interesting-but-off-objective, and add anything the objective needs that is missing.
7. Generate the content and activities for the remaining lessons the same way, keeping the tone and structure consistent across the whole course, then save it all in your project folder. This developed content is what you assess in Lab 7 and produce in Lab 8.

**Test it**

You have developed learning content for the lessons — clear, chunked, plain-language explanations with realistic, bias-checked examples and a simple model — plus a discussion activity, a role-play and a branching scenario per key lesson, each aligned to its objective. Saved and ready to assess.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 7 — Create Quizzes, Assessments and Rubrics with AI

Learning outcome: Create assessment that measures the objectives — quiz items with answer guides, a scenario-based performance task, and a rubric — all aligned to the learning objectives and checked for quality and fairness..

Goal: A course is only as good as the evidence that learners can do what it promised. In this lab you use AI to build assessment that measures your objectives. You generate a short quiz (multiple-choice, true/false and short-answer items) with an answer guide and a rationale for each item, then a scenario-based performance task where a learner handles a mock complaint. Crucially, you check quality: every quiz item must map to an objective, have exactly one defensible correct answer with plausible distractors and no giveaway cues, and sit at the right cognitive level. You then have AI draft a criteria-based rubric for the performance task — with clear criteria and performance levels — and you calibrate it to Meridian's standard. The result is aligned, fair assessment ready to slot into the package. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

A short quiz with an answer guide and rationales, a scenario-based performance task, and a criteria-based rubric for the Meridian course — every item mapped to an objective, checked for one correct answer, plausible distractors and the right level, and calibrated to standard.   (Tools: ChatGPT / Claude / Gemini, quiz-item writing, distractors and answer guides, scenario/performance tasks, rubric design, objective alignment, item-quality review.)

**Step-by-step**

1. Open your final learning objectives from Lab 3 — every assessment item must measure one of them.
2. Generate a short quiz aligned to the objectives. Paste the prompt below, with your objectives pasted in.

   ```bash
   You are an assessment writer. From these learning objectives: '[PASTE OBJECTIVES]', write a 6-question quiz for new retail staff: a mix of multiple-choice (four options), true/false and one short-answer item. For each item, note which objective it measures, give the correct answer, and add a one-line rationale. Make the wrong options plausible, not obvious.
   ```

3. Create a scenario-based performance task. Paste the prompt below.

   ```bash
   Write a short scenario-based performance task for the same course: a realistic customer-complaint situation an associate must handle, the instructions to the learner, and what a good response would include. Tie it explicitly to the complaint-handling and escalation objectives.
   ```

4. Quality-check the quiz items. Paste the prompt below and fix whatever it flags.

   ```bash
   Review this quiz for item quality: does each item map to an objective, does each multiple-choice item have exactly one defensible correct answer with plausible distractors and no giveaway cues (such as 'all of the above' or the longest option always being right), and is each at an appropriate difficulty? Flag and rewrite any weak item.
   ```

5. Build a rubric for the performance task. Paste the prompt below.

   ```bash
   Create a criteria-based rubric to assess the complaint-handling performance task. Use 3 to 4 criteria (for example: stayed calm and empathetic, understood the customer's need, applied the service-recovery steps, knew when to escalate) and 3 performance levels (for example: developing, proficient, strong) with a short descriptor for each cell. Present it as a table.
   ```

6. Calibrate the rubric to standard: adjust the criteria and level descriptors so 'proficient' really reflects what Meridian expects of a new associate — not too lenient, not unrealistic for a first week — and make sure the criteria match the performance task and the objectives.
7. Save the quiz with its answer guide, the performance task, and the rubric in your project folder, noting the objective each piece measures. This aligned assessment slots into the package in Lab 10.

**Test it**

You have a short quiz with an answer guide and rationales, a scenario-based performance task, and a calibrated criteria-based rubric — every item mapped to an objective, each multiple-choice item checked for one correct answer, plausible distractors and no giveaway cues, and the rubric matched to Meridian's standard. Saved in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 8 — Produce Scripts, Visuals and Job Aids with AI

Learning outcome: Produce the learner-facing media — a narration script and storyboard for the e-learning module, on-brand visuals, and take-away job aids — that make the course usable and support performance on the job..

Goal: Now you produce the material learners see, hear and keep. In this lab you use AI three ways. First, you draft a short narration script and a storyboard for the e-learning module — for each screen, the on-screen text, the narration and the visual — written to be heard, not read. Second, you use an AI image tool to create on-brand visuals for the key screens and slides (a greeting, a complaint being resolved), keeping the style consistent and writing alt text for each so the material is accessible. Third, you create the take-away job aids learners keep after the course — a one-page complaint-handling checklist and a quick-reference card of the service steps. You check every visual is appropriate and licence-clear and every job aid is genuinely usable at the counter. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

A narration script and storyboard for the e-learning module, a consistent set of on-brand visuals with alt text for the key screens, and take-away job aids (a complaint-handling checklist and a quick-reference card) — all produced and checked for consistency, accessibility and appropriateness.   (Tools: ChatGPT / Claude / Gemini, narration scripts and storyboards, AI image generation, image prompting, alt text and accessibility, job-aid and checklist design, licensing check.)

**Step-by-step**

1. Choose the lesson to turn into the short e-learning module — for example the complaint-handling lesson — and open its content from Lab 6.
2. Draft the narration script and storyboard. Paste the prompt below, with the lesson content pasted in.

   ```bash
   You are an e-learning developer. From this lesson content: '[PASTE CONTENT]', write a storyboard for a short e-learning module. For each screen give: the on-screen text (brief), the narration (written to be heard, warm and clear, a few sentences), and a note on the visual. Keep the whole module to about 6 to 8 screens and roughly three to four minutes of narration.
   ```

3. Generate an on-brand visual for a key screen. Paste the image prompt below into your image tool.

   ```bash
   A clean, friendly flat illustration of a retail associate calmly helping a customer who looks concerned, in a bright neighbourhood lifestyle store, warm and approachable style, simple shapes, no text and no real brand logos, suitable for a training e-learning screen.
   ```

4. Generate the other visuals the same way, keeping the style consistent (same look, colours and character style) so the module feels like one course. For each image, write one line of alt text describing what it shows, so learners using a screen reader can follow along.
5. Check appropriateness and licensing: no real company logos or identifiable real people, confirm your image tool's terms allow training use, and note where you will disclose that images are AI-generated. Replace anything you are unsure about.
6. Create the take-away job aids. Paste the prompt below.

   ```bash
   Create two take-away job aids for new retail associates: (1) a one-page complaint-handling checklist using the service-recovery steps from the course, and (2) a wallet-sized quick-reference card of the greeting-to-resolution steps. Keep them short, plain, action-first, and usable at the counter in the moment.
   ```

7. Review the job aids for real-world usability — could a nervous new associate actually glance at this mid-shift and know what to do? Tighten anything wordy, then save the script, storyboard, visuals with alt text, and job aids in your project folder.

**Test it**

You have a storyboard and narration script for a short e-learning module, a consistent set of on-brand, appropriate, licence-checked visuals each with alt text, and two usable take-away job aids (a complaint-handling checklist and a quick-reference card) — all saved in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 9 — Align to Outcomes and Quality-Check the AI Output

Learning outcome: Run a full alignment and quality pass — map every artifact to an objective, find gaps and orphans, and check all AI-generated material for accuracy, bias, reading level and instructional soundness before it reaches learners..

Goal: Before a course is delivered, it must be checked. In this lab you run two disciplined passes over everything you have built. First, alignment: you build an alignment matrix that maps every objective to the content, activity and assessment that serve it, using AI to surface gaps (an objective with no assessment) and orphans (content that serves no objective), and you fix them. Second, quality: you have AI review the material — but critically, not trustingly — for factual accuracy (which you confirm with a subject expert or the brief, never the AI alone), for bias and stereotypes, for reading level and plain language, and for accessibility. You compile a short quality-check report of what you found and fixed. This is where you take ownership of the instructional quality of the whole package. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

An alignment matrix mapping every objective to its content, activity and assessment (with gaps and orphans fixed), plus a completed quality-check pass and short report covering accuracy, bias, reading level and accessibility — so the whole package is aligned and ready to finalise.   (Tools: ChatGPT / Claude / Gemini, alignment matrices, gap and orphan analysis, fact-checking, bias and stereotype review, readability checks, accessibility review.)

**Step-by-step**

1. Gather every artifact you have built: objectives (Lab 3), curriculum map and lesson plans (Labs 4-5), content and activities (Lab 6), quiz, task and rubric (Lab 7), and script, visuals and job aids (Lab 8).
2. Build the alignment matrix. Paste the prompt below, with your objectives and a list of your artifacts pasted in.

   ```bash
   You are a quality reviewer. Here are my learning objectives: '[PASTE OBJECTIVES]', and my course artifacts: '[LIST CONTENT, ACTIVITIES, QUIZ ITEMS, TASK, JOB AIDS]'. Build an alignment matrix mapping each objective to the content, activity and assessment that serve it. Flag any objective with no assessment (a gap) and any artifact that serves no objective (an orphan).
   ```

3. Fix gaps and orphans: for every objective missing an assessment, add or reassign an item; for every orphan, either tie it to an objective or cut it. Re-run the check until every objective is covered and nothing is orphaned.
4. Run the accuracy and bias quality check. Paste the prompt below.

   ```bash
   Review all this course material for quality: flag any factual claim I must verify with a subject expert, any example or scenario that could carry a stereotype or unfair assumption, and anything that reads as too strong or absolute to defend. List each issue with the fix you recommend. Do not assume your own facts are correct — mark them for me to confirm.
   ```

5. Confirm the facts yourself: take every claim the AI flagged (and any Meridian policy or service standard) and confirm it against the supplied brief or a subject expert — never on the AI's word alone — and correct anything wrong. Resolve every [VERIFY] placeholder left from earlier labs.
6. Check readability and accessibility. Paste the prompt below, then apply the fixes.

   ```bash
   Check this learner-facing content for reading level and accessibility: is it plain language at about a secondary-school level, active voice, jargon explained; do all images have alt text; and is anything conveyed by colour or image alone that a learner might miss? List what to improve.
   ```

7. Compile a short quality-check report in your project folder: the alignment matrix, the issues found (accuracy, bias, readability, accessibility) and how each was fixed. The package is now aligned and quality-checked, ready to assemble in Lab 10.

**Test it**

You have an alignment matrix with every objective mapped to its content, activity and assessment and all gaps and orphans fixed, plus a completed quality-check covering accuracy (facts confirmed against the brief or an expert, no [VERIFY] left), bias, reading level and accessibility — captured in a short report in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


### Lab 10 — Assemble, Review and Finalise the Course Package

Learning outcome: Assemble every artifact into one consistent facilitator and learner package, run a final review, and finalise the Meridian Service Excellence course kit ready to deliver — end to end..

Goal: The last mile is assembly and handover. In this lab you bring every reviewed artifact together into one coherent course package: a facilitator guide (the lesson plans, timings, activity instructions, answer guide and rubric) and a learner set (the content, the e-learning module storyboard, the quiz, and the take-away job aids). You use AI to draft a course overview and a facilitator guide that stitches the lesson plans into a runnable flow, then you run a final consistency pass — one voice, consistent terms, correct objective numbering and no leftover placeholders. You do a final human review against the objectives one last time, confirm every fact is verified, and finalise and export the package. That completes the Meridian Service Excellence course kit — from a training request to a deliverable course — end to end. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, the connected course package you assemble across all 10 labs.

**What you'll build**

A finished, assembled course package — a facilitator guide (course overview, lesson plans, timings, activity instructions, answer guide and rubric) and a learner set (content, e-learning storyboard, quiz and job aids) — run through a final consistency and human review, with every fact verified and no placeholders left, exported and ready to deliver.   (Tools: ChatGPT / Claude / Gemini, package assembly, facilitator guide, course overview, consistency pass, final human review, exporting the package.)

**Step-by-step**

1. Lay out every reviewed artifact from Labs 3-9 in the order it belongs in the package: overview, objectives, lesson plans, content, activities, e-learning storyboard, quiz and answer guide, performance task and rubric, and job aids.
2. Draft the course overview and facilitator guide. Paste the prompt below, with your lesson plans and objectives pasted in.

   ```bash
   You are an instructional designer assembling a course package. Using these objectives and lesson plans: '[PASTE]', write (1) a one-page course overview — purpose, audience, objectives, duration and structure — and (2) a facilitator guide that stitches the lesson plans into a runnable three-hour flow, with timings, what the facilitator does at each step, and where the activities, quiz and job aids are used.
   ```

3. Run a final consistency pass. Paste the prompt below.

   ```bash
   Do a consistency pass across this whole course package: make the voice and tone consistent, standardise key terms (for example the name of the service-recovery method), check the objective numbering matches everywhere, and flag any leftover placeholder, [VERIFY] tag or 'TODO'. Return a list of what to fix.
   ```

4. Fix everything the consistency pass flagged, and resolve any last placeholder — nothing marked [VERIFY] or 'TODO' may remain in a package about to be delivered.
5. Do a final human review against the objectives: read the package once as a whole and confirm a new associate who completes it would genuinely be able to do each objective, the assessment fairly measures each, and the facilitator could run it in three hours. Adjust anything that fails this test.
6. Split the package into the two audiences: a facilitator guide (with the answer guide and rubric) and a learner set (without the answer guide), so each reader gets what they need.
7. Export and save the finished package (as documents or a PDF) in your project folder, with a short contents page. This complete, aligned, quality-checked Meridian Service Excellence course kit is the deliverable the whole course set out to build — and remember, you, not the AI, own its instructional quality.

**Test it**

You have assembled every reviewed artifact into one coherent package — a facilitator guide (overview, lesson plans, timings, activity instructions, answer guide and rubric) and a learner set (content, e-learning storyboard, quiz and job aids) — run a final consistency and human review against the objectives, verified every fact with no placeholders left, and exported the finished Meridian Service Excellence course kit ready to deliver.

> **Note:** Full commands and screenshots are in labs/lab-10-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential employee data, personal information, credentials or proprietary training material into a public AI tool. Use the supplied Meridian training brief rather than real client material, treat every AI output — especially facts, examples and assessment answers — as a first draft to be reviewed, fact-checked with a subject expert and checked for bias, and be transparent about AI assistance where appropriate before the course reaches real learners.

---


## Wrap-Up

You have taken one training course — the Meridian Service Excellence course kit — from a training request to a finished, aligned course package in a single day, using ChatGPT, Claude, Gemini and an AI image tool as drafting and design partners while keeping the outcomes, the learners and the instructional quality your own.

**What you built**

- An AI instructional-design toolkit — ChatGPT, Claude, Gemini and an AI image tool set up, plus a reusable ID prompt library.
- A clear foundation — a needs analysis, learner personas and clear, measurable learning objectives for the Meridian course.
- A structured design — a curriculum map, module breakdown and sequenced, timed lesson plans aligned to the objectives.
- Developed materials — learning content, activities and scenarios, quizzes, assessments and rubrics, and scripts, visuals and job aids.
- An aligned, finished package — an objective-by-artifact alignment check, a quality-check for accuracy and bias, and an assembled facilitator and learner package ready to deliver.

**What to do next**

- Rebuild a course for a real, non-confidential training need of your own using the same workflow and prompt library.
- Introduce your saved prompts to your team so everyone drafts needs analyses, objectives, content, assessments and job aids the same way.
- Always start with the outcomes and the learners before you generate a single activity — AI makes a well-designed course faster, not a missing design.
- Keep the quality habit: verify every fact with a subject expert, check for bias, confirm alignment to the objectives, and stand behind everything before it reaches a learner.

---


## Next Steps

- First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.
- Second pass: rebuild the course kit for your own real, non-confidential training need, from needs analysis and objectives through to an assembled, aligned package.
- Introduce your prompt library and the analyse → design → develop → align → deliver workflow to your team so the practice sticks.
- Review each lab's detailed steps in this guide and re-create the course package in your own AI tools.


## Glossary

- **Instructional design (ID)** — The systematic process of turning a learning need into an effective learning experience — analysing, designing, developing, implementing and evaluating learning.
- **Generative AI assistant** — A general-purpose chat tool (ChatGPT, Claude, Gemini) that generates text drafts and analysis from a prompt.
- **AI image tool** — A tool that generates images from a text prompt (built into ChatGPT, Gemini or Copilot, or a dedicated tool like Adobe Firefly or Canva), used here for visuals and job aids.
- **ChatGPT / Claude / Gemini** — The three widely-used chat assistants used in this course to analyse, write, structure and refine course material.
- **ADDIE** — A common instructional-design model with five phases — Analyse, Design, Develop, Implement, Evaluate — that structures the course-building process.
- **Backward design** — Designing a course from the intended outcomes backwards: define what learners must be able to do, then the assessment, then the content and activities.
- **Needs analysis** — The up-front study of the performance gap, the business need and the learners, that decides what a course must achieve and for whom.
- **Learner persona** — A believable, research-based profile of a representative learner group — their role, prior knowledge, motivation, context and constraints — used to keep design learner-centred.
- **Learning objective** — A clear, measurable statement of what a learner will be able to do after the learning, written with an observable action verb.
- **Bloom's taxonomy** — A framework of cognitive levels (remember, understand, apply, analyse, evaluate, create) whose action verbs are used to write objectives and pitch assessment at the right level.
- **Alignment** — The principle that content, activities and assessment all serve the stated learning objectives, with no gaps or orphans.
- **Curriculum map** — A high-level plan of a course — its modules, the objectives each covers, and the sequence — agreed before detailed development.
- **Lesson plan** — A detailed plan for a single lesson or session — its objective, timing, activities, materials and assessment.
- **Chunking** — Breaking content into small, digestible pieces so it is easier to learn and remember.
- **Learning activity** — Anything that has learners do something — a discussion, exercise, role-play or scenario — to apply and practise the content.
- **Scenario / branching scenario** — A realistic situation learners work through, sometimes with choices that branch to different outcomes, to practise decisions in a safe setting.
- **Case study** — An extended, realistic example that learners analyse to apply concepts to a real-world situation.
- **Formative vs summative** — A formative check gives feedback during learning; a summative check measures achievement of the objectives at the end.
- **Quiz item types** — Common question forms — multiple-choice, true/false, matching, short-answer — each suited to different objectives and cognitive levels.
- **Distractor** — An incorrect but plausible option in a multiple-choice question; good distractors reflect common misconceptions without giving the answer away.
- **Answer guide** — The record of the correct answer (and rationale) for each quiz item, used to score and review learners' responses.
- **Rubric** — A scoring guide that lists the criteria for a task and describes each performance level, so grading is consistent and expectations are clear.
- **Feedback** — Information given to a learner about their performance that helps them improve; AI can draft model feedback that you calibrate.
- **Storyboard** — A plan for an e-learning screen or video sequence showing, for each frame, the on-screen content, the narration and the visuals.
- **Narration script** — The spoken words for a video or e-learning module, written to be heard rather than read.
- **Job aid** — A concise, take-away reference — a checklist, quick-reference card or one-pager — that supports performance on the job after the course.
- **Accessibility** — Designing content so every learner can use it, including alt text for images, captions for media, plain language and support for assistive technology.
- **Alt text** — A short text description of an image that lets learners using a screen reader understand what the image shows.
- **Prompt** — The instruction you give the AI; a structured prompt with role, context, task, format and constraints produces a far better draft than a vague one.
- **Prompt library** — A saved, reusable set of prompt templates for the recurring ID tasks — needs analysis, objectives, outlines, content, quizzes, rubrics, job aids.
- **Generate–review–refine loop** — The core AI workflow — prompt, review the draft critically against objectives and audience, then refine with follow-up prompts and your own edits until it is right.
- **Human-in-the-loop** — Keeping a person responsible for reviewing, fact-checking, correcting and approving every AI output before it is used with learners.
- **Hallucination** — A confident but false or invented statement, fact or example from an AI, which is why every output must be fact-checked with a subject expert.
- **Bias check** — Reviewing content and examples for stereotypes or unfair assumptions so the material is inclusive and represents learners fairly.
- **Responsible AI use** — Using AI safely and ethically — protecting confidential data, verifying facts, checking for bias, respecting copyright, and being transparent about AI assistance.
- **Course package** — The assembled set of facilitator and learner materials — plans, content, activities, assessments, rubrics and job aids — ready to deliver a course.
