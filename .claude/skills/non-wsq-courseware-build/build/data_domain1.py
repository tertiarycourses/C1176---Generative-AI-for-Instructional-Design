"""
Domain 1 — Getting Started with Generative AI for Instructional Design. Labs 1-5.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course takes one connected deliverable — the Meridian Service
Excellence course kit, a short blended customer-service course for the new
frontline staff of a fictional Singapore retail chain, Meridian Retail Group —
one stage further. Lab 1 sets up the AI instructional-design toolkit; Lab 2 builds
a reusable prompt library; Lab 3 analyses the learning need, profiles the learners
and writes measurable objectives; Lab 4 structures the course into a curriculum
map; Lab 5 turns it into sequenced, timed lesson plans. A Meridian training brief
with the context you need is supplied; use your own non-confidential course instead
wherever you prefer.
"""

SCENARIO = (
 "Meridian Retail Group is a fictional Singapore chain of neighbourhood lifestyle stores. It is onboarding a "
 "wave of new frontline retail associates and needs a short, practical course — 'Delivering Great Customer "
 "Service at Meridian' — a roughly three-hour blended course (a facilitator-led workshop plus a short "
 "e-learning module and take-away job aids) that new associates complete in their first week. You are the "
 "instructional designer building it. The course must turn nervous new hires into associates who can greet "
 "customers warmly, understand a customer's need, handle a complaint calmly using a simple service recovery "
 "method, and know when to escalate. Across this course you take that course from a training request to a "
 "finished, aligned course package — the Meridian Service Excellence course kit — using ChatGPT, Claude, "
 "Gemini and an AI image tool. Use this scenario only if you cannot use a real, non-confidential course of "
 "your own; your own topic is always welcome."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, "
 "the connected course package you assemble across all 10 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Set Up Your AI Instructional-Design Toolkit",
 objective="Sign in to ChatGPT, Claude, Gemini and an AI image tool, run your first instructional-design prompts, and learn the generate–review–refine loop that every later lab uses.",
 desc="This lab gets you comfortable with the tools before any real design work begins. You open the chat "
 "assistants (ChatGPT, Claude and Gemini), confirm you are signed in, and run a simple instructional-design "
 "prompt so you see how each drafts learning content, then run the same prompt in a second assistant to feel "
 "how they differ. You open an AI image tool, sign in, and generate a quick throwaway visual so you can see "
 "what an image tool does for learning materials. You note what AI is genuinely good at for instructional "
 "design (a fast draft, structure, options) and where it needs you (your real learners, your subject-matter "
 "truth, your pedagogical judgement). By the end you understand the describe -> generate -> review -> refine "
 "loop that is the heart of every lab. " + PROJECT_NOTE,
 build="Your AI instructional-design toolkit set up and tested — at least one chat assistant and an AI image tool signed in and responding — a first throwaway AI-generated draft and visual, and a clear, written understanding of the generate–review–refine loop and what AI can and cannot do for an instructional designer.",
 services="ChatGPT, Claude, Gemini, an AI image tool, account sign-in, first prompts, comparing assistants, the generate–review–refine loop",
 steps=[
 ("Create a project folder on your machine called 'Meridian-Service-Course-Kit' so every file and note you make today stays together. Open ChatGPT (chat.openai.com), Claude (claude.ai) and Gemini (gemini.google.com) in browser tabs and confirm you are signed in to at least one.", ""),
 ("In one chat assistant, run a simple first prompt to see how it drafts learning content. Paste the prompt below and read the reply.",
  "You are an instructional designer. In five short bullet points, explain what makes a short workplace training course effective for new frontline retail staff. Keep each bullet to one sentence."),
 ("Run the exact same prompt in a second assistant and compare the two replies. Notice differences in tone, length and structure — the skill you learn transfers across all of them, so use whichever you prefer.",
  "You are an instructional designer. In five short bullet points, explain what makes a short workplace training course effective for new frontline retail staff. Keep each bullet to one sentence."),
 ("Open your AI image tool (image generation in ChatGPT or Gemini, Microsoft Copilot / Designer, or a tool like Adobe Firefly or Canva), sign in, and generate a quick throwaway visual so you can see what an image tool produces for learning materials. Paste the prompt below.",
  "A simple, friendly flat illustration of a retail associate warmly greeting a customer in a bright neighbourhood store, clean and modern, no text."),
 ("Look at what the image tool produced — a usable draft visual generated in seconds. Note that it is a fast starting point, not a finished course graphic. You will not keep this one; it is only to feel the tool.", ""),
 ("In one line each, write what the AI did well (fast draft, structure, instant visual) and where it needs you (it does not know Meridian's real service standards, your learners, or your judgement). This good/not-good picture guides how you use AI all day.", ""),
 ("Open the supplied Meridian training brief (labs/reference-pack/): the organisation, the audience, the business need and the course constraints. Skim it so you know the course you are about to design.", ""),
 ("Save your notes into your Meridian-Service-Course-Kit folder. Write one line, in your own words, describing the generate -> review -> refine loop — you rely on it in every later lab.", ""),
 ],
 test="You have signed in to at least one chat assistant and an AI image tool, run the same prompt in two assistants and compared them, generated a throwaway visual, written a one-line note on what AI is and is not good at for instructional design, skimmed the Meridian training brief, and described the generate–review–refine loop in your own words — all saved in your Meridian-Service-Course-Kit folder.",
 ),
 dict(
 num=2, topic=1,
 title="Write Effective Prompts for Instructional Design",
 objective="Turn a vague ask into a strong, structured prompt (role, context, task, format, constraints) for instructional-design tasks, and save a reusable prompt library for the work you repeat for every course.",
 desc="A good result starts with a good prompt, not a lucky one. In this lab you read the Meridian training "
 "brief and write a deliberately vague prompt first, so you see how generic the result is. You then rebuild it "
 "with five clear parts — a role for the AI, the context (audience, level, mode, constraints), the exact task, "
 "the format you want back, and any constraints — and watch the draft become genuinely usable. You run small "
 "single-change edits to feel how each part matters, then save your best versions as a reusable prompt library "
 "with clearly marked slots, covering the tasks you repeat for every course: needs analysis, objectives, "
 "outline, content, activities, quizzes, rubrics and job aids. " + PROJECT_NOTE,
 build="A structured instructional-design prompt built from role, context, task, format and constraints, plus a reusable prompt library with clearly marked slots for the recurring ID tasks, saved in your project folder.",
 services="ChatGPT / Claude / Gemini, the structured prompt framework (role, context, task, format, constraints), prompt iteration, a reusable prompt library",
 steps=[
 ("Open the Meridian training brief and note two things you will reuse in every prompt: who the learners are (new frontline retail associates in their first week) and the goal (deliver great customer service, including handling complaints).", ""),
 ("Write a deliberately vague first prompt in any assistant and generate, so you can see the generic result. Paste the prompt below and read how unfocused the reply is.",
  "Write a customer service training course."),
 ("Rebuild the prompt with a role and the context, and regenerate. Paste the prompt below and compare it with the vague version.",
  "You are an experienced instructional designer. Context: Meridian Retail Group is onboarding new frontline retail associates, who are often first-time workers, and needs a short, practical, roughly three-hour blended course on delivering great customer service, including handling complaints and knowing when to escalate. Draft the high-level topics this course should cover."),
 ("Now add the exact task, the format you want back, and clear constraints, and regenerate. Paste the prompt below.",
  "As the same instructional designer, list the 4 to 6 modules this course should have. For each module give a short title and one line on what learners will be able to do after it. Present it as a numbered list, keep it practical and beginner-friendly, and do not invent Meridian-specific policies — leave clear placeholders where a real company policy is needed."),
 ("Put the vague result and the structured result side by side. Note in one line how much more usable the structured prompt was — this is the core lesson of the day.", ""),
 ("Run two or three single-change edits to feel how each part steers the result — for example change the audience to 'experienced staff moving into a supervisor role', or change the mode to 'a self-paced e-learning module only' — and note which you would keep for Meridian.", ""),
 ("Save a reusable prompt library in your project folder: templates for needs analysis, learning objectives, course outline, content, activities, quiz items, rubrics and job aids, each with clearly marked slots — [ROLE], [CONTEXT], [AUDIENCE], [TASK], [FORMAT], [CONSTRAINTS] — that you fill in for any future course.", ""),
 ],
 test="You have compared a vague prompt with a structured one built from role, context, task, format and constraints, seen how much better the structured prompt performs, run single-change edits to feel each part, and saved a reusable prompt library with marked slots for the recurring instructional-design tasks in your project folder.",
 ),
 dict(
 num=3, topic=1,
 title="Analyse Learning Needs, Audience and Objectives with AI",
 objective="Use AI to analyse the learning need, profile the target learners as personas, and write clear, measurable learning objectives — the foundation every later artifact must align to.",
 desc="A good course rests on a clear need, a real understanding of the learners, and sharp objectives. In this "
 "lab you use a chat assistant to turn the Meridian training brief into a short needs analysis — the "
 "performance gap, the business need and what success looks like — then profile the learners as one or two "
 "personas (their role, prior knowledge, motivation and constraints). Crucially, you then write measurable "
 "learning objectives using observable action verbs (Bloom's taxonomy), and you check them: each objective "
 "must be observable, achievable in the time, and tied to the real on-the-job need — not a vague 'understand "
 "customer service'. You verify any factual claim against the brief and replace anything the AI invented with "
 "the brief's real context or a clear [VERIFY] placeholder. This foundation anchors every lab that follows. " + PROJECT_NOTE,
 build="A short needs analysis (performance gap, business need, success measure), one or two learner personas, and a set of clear, measurable, Bloom-aligned learning objectives for the Meridian course — checked for observability and fit, and grounded in the supplied brief.",
 services="ChatGPT / Claude / Gemini, needs / gap analysis, learner personas, writing measurable objectives, Bloom's taxonomy, verifying against the brief",
 steps=[
 ("Open the Meridian training brief and note the business need (why the course exists) and the audience (new frontline retail associates in their first week).", ""),
 ("Draft a short needs analysis with AI. Paste the prompt below, with the relevant brief details pasted in.",
  "You are an instructional designer. From this training brief: '[PASTE BRIEF DETAILS]', write a short needs analysis: the performance gap (what learners cannot yet do), the business need it serves, any constraints (time, mode, prior knowledge), and one clear measure of success. Keep it to a page; do not invent facts not in the brief — mark anything you would need to confirm."),
 ("Profile the learners as personas. Paste the prompt below.",
  "For the same course, create one or two learner personas for new frontline retail associates — often first-time workers. For each: a name and role, prior knowledge and confidence, what motivates them, their context and constraints, and what would make the training work for them. Keep them realistic and free of stereotypes."),
 ("Write measurable learning objectives. Paste the prompt below.",
  "Write 5 to 7 measurable learning objectives for this course, each starting 'By the end of this course, learners will be able to...' and using an observable action verb from Bloom's taxonomy (for example describe, demonstrate, apply, handle, decide). Make them achievable in a three-hour blended course and tied to the real on-the-job need. Avoid vague verbs like 'understand' or 'know'."),
 ("Pressure-test the objectives. Paste the prompt below and tighten any weak objective.",
  "Review these objectives for quality: is each one observable and measurable, achievable in the time, and tied to a real performance need? Flag any that are vague, too ambitious, or not assessable, and suggest a sharper version."),
 ("Verify against the brief: check every fact in the needs analysis and personas against the Meridian training brief, keep the brief's real context, and replace anything the AI invented with the brief's value or a clear [VERIFY] placeholder. Never carry an AI-invented fact into your design.", ""),
 ("Save three things in your project folder: the needs analysis, the learner personas, and the final measurable objectives. These objectives are the spine every later lab must align to.", ""),
 ],
 test="You have a short needs analysis, one or two realistic learner personas, and a set of clear, measurable, Bloom-aligned learning objectives — pressure-tested for observability and fit and verified against the supplied brief — saved in your project folder as the foundation for the course.",
 ),
 dict(
 num=4, topic=1,
 title="Structure the Course Curriculum with AI",
 objective="Turn the objectives into a curriculum map — the course's modules, the objectives each module covers, and a logical sequence — so the course has a clear structure before any content is written.",
 desc="With the objectives set, you design the shape of the course. In this lab you use AI to turn your "
 "learning objectives into a curriculum map: the modules the course needs, which objective(s) each module "
 "covers, the key topics inside each, and a suggested time for each within the three-hour budget. You review "
 "it hard — checking every objective is covered by a module (no gaps) and every module serves an objective (no "
 "orphans), that the sequence builds logically from simple to complex, and that the total time is realistic. "
 "You use backward design thinking: each module exists to move learners toward an objective. This map is the "
 "blueprint you turn into detailed lesson plans in Lab 5 and fill with content in Topic 2. " + PROJECT_NOTE,
 build="A curriculum map for the Meridian course — modules with their covered objectives, key topics and suggested timings within the three-hour budget — reviewed so every objective is covered, every module earns its place, and the sequence builds logically.",
 services="ChatGPT / Claude / Gemini, curriculum mapping, backward design, sequencing, objective-to-module alignment, time budgeting",
 steps=[
 ("Gather your inputs from Lab 3: the measurable learning objectives and the learner personas. The map must serve those objectives and those learners.", ""),
 ("Generate the curriculum map. Paste the prompt below, with your objectives pasted in.",
  "You are an instructional designer using backward design. Using these learning objectives: '[PASTE OBJECTIVES]', design a curriculum map for a three-hour blended course. Give 4 to 6 modules; for each: a title, the objective(s) it addresses, the key topics inside it, the mode (workshop or e-learning), and a suggested time in minutes. Present it as a table and make the times add up to about three hours."),
 ("Check coverage and orphans. Paste the prompt below.",
  "Check this curriculum map against my objectives: is every objective covered by at least one module, and does every module clearly serve an objective? List any objective with no module (a gap) and any module that serves no objective (an orphan), and suggest fixes."),
 ("Check the sequence: confirm the modules build logically — foundational ideas (what great service is, knowing the customer) before harder skills (handling a complaint, escalation) — and reorder anything out of place so the learning flows.", ""),
 ("Check the time budget: confirm the module timings add up to about three hours with room for a welcome and a wrap-up, and adjust any module that is over- or under-weighted for its objective.", ""),
 ("Decide the blend: mark which modules are the facilitator-led workshop and which sit in the short e-learning module, so the structure matches the blended design in the brief.", ""),
 ("Save the final curriculum map in your project folder. This is the blueprint — you turn it into detailed lesson plans in Lab 5 and fill it with content, activities and assessment in Topic 2.", ""),
 ],
 test="You have a curriculum map of 4 to 6 modules, each mapped to the objective(s) it covers with key topics, mode and a time — with every objective covered, no orphan modules, a logical simple-to-complex sequence, and timings that add up to about three hours. Saved in your project folder.",
 ),
 dict(
 num=5, topic=1,
 title="Build the Lesson Plans and Learning Sequence with AI",
 objective="Turn the curriculum map into detailed, timed lesson plans — each with its objective, a warm-up, content, an activity and a check — sequenced into a coherent flow ready to develop.",
 desc="Now you take the curriculum map down to the level a facilitator can actually run. In this lab you prompt "
 "AI to expand each module into a lesson plan: the module's objective, a short opener or warm-up, the content "
 "to teach, at least one learning activity where learners do something, a quick check for understanding, the "
 "timing for each part, and the materials needed. You apply a simple, sound structure to every lesson (for "
 "example a hook, then teach, then practise, then check — an engagement-to-application flow) so learning is "
 "active, not a lecture. You review the plans for realistic timing and a smooth flow from lesson to lesson "
 "across the whole course. These lesson plans are the detailed spine you fill with real content, activities "
 "and assessment in Topic 2. " + PROJECT_NOTE,
 build="A set of detailed, timed lesson plans for the Meridian course — each module with its objective, warm-up, content, at least one activity, a check for understanding, timings and materials — sequenced into one coherent flow, ready to develop in Topic 2.",
 services="ChatGPT / Claude / Gemini, lesson planning, active-learning structure (hook–teach–practise–check), timing, sequencing lessons, materials lists",
 steps=[
 ("Open your Lab 4 curriculum map — each module becomes a lesson plan in this lab.", ""),
 ("Expand one module into a full lesson plan. Paste the prompt below, with that module's details pasted in.",
  "You are an instructional designer. Expand this module into a detailed lesson plan: '[PASTE ONE MODULE]'. Include the module's objective, a short warm-up or hook, the content to teach, at least one active learning activity where learners apply the content, a quick check for understanding, the timing in minutes for each part, and the materials or media needed. Use a hook -> teach -> practise -> check flow and keep it practical for a facilitator."),
 ("Generate the remaining lesson plans the same way, one per module, keeping the same structure so the whole course feels consistent and every lesson has an active element rather than pure lecture.", ""),
 ("Check the timing. Paste the prompt below.",
  "Review these lesson plans for timing: do the parts within each lesson add up to the module's allotted time, and do all the lessons together fit a three-hour course with a welcome, a break and a wrap-up? Flag anything that will overrun and suggest what to trim."),
 ("Check the flow between lessons: confirm each lesson connects to the next, prior knowledge builds in the right order, and there are no abrupt jumps or repeated content across lessons.", ""),
 ("Confirm active learning: make sure every lesson has at least one activity or discussion where learners do or say something, not just receive content — the point of the workshop is practice.", ""),
 ("Save the full set of lesson plans in your project folder. This is the detailed spine of the course — you write its content and activities in Lab 6, its assessment in Lab 7, and its scripts, visuals and job aids in Lab 8.", ""),
 ],
 test="You have a complete set of timed lesson plans, one per module, each with its objective, a warm-up, content, at least one active learning activity, a check for understanding, timings and materials — sequenced into one coherent, active, three-hour flow with realistic timing. Saved in your project folder.",
 ),
]
