"""
Domain 2 — Creating Learning Content and Assessments with AI. Labs 6-10.

THE CONNECTED PROJECT CONTINUES — the same Meridian Service Excellence course kit,
now developed, assessed, produced, aligned and assembled.

Lab 6 generates the learning content, activities and scenarios; Lab 7 creates the
quizzes, assessments and rubrics; Lab 8 produces the scripts, visuals and job aids;
Lab 9 aligns every artifact to the outcomes and quality-checks the AI output; Lab
10 assembles, reviews and finalises the facilitator and learner package ready to
deliver. Use your own non-confidential course instead of Meridian wherever you
prefer.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Meridian Service Excellence course kit, "
 "the connected course package you assemble across all 10 labs."
)

DOMAIN2 = [
 dict(
 num=6, topic=2,
 title="Generate Learning Content, Activities and Scenarios with AI",
 objective="Turn the lesson plans into concrete learning content, active learning activities and a realistic scenario — chunked, written in plain language, and pitched at the learners' level.",
 desc="With the lesson plans set, you develop the material learners actually work with. In this lab you feed a "
 "lesson plan to a chat assistant and have it draft the learning content: clear explanations, relatable "
 "examples and a simple model learners can use (for example a service-recovery method for handling "
 "complaints). You then generate active learning activities — a discussion prompt, a role-play, and a "
 "realistic branching scenario in which a customer complaint plays out and the learner chooses how to respond. "
 "You edit hard: you chunk long content into digestible pieces, rewrite it in plain, active, encouraging "
 "language at the learners' level, and check every example is realistic and free of bias. The result is "
 "developed content and activities ready to be assessed in Lab 7 and produced in Lab 8. " + PROJECT_NOTE,
 build="Developed learning content for the Meridian course — clear, chunked explanations and examples plus a simple service model — with at least one discussion activity, one role-play and one realistic branching scenario, all in plain, active language pitched at the learners.",
 services="ChatGPT / Claude / Gemini, content drafting, chunking, plain-language writing, activity design, role-plays, branching scenarios, bias check",
 steps=[
 ("Open one lesson plan from Lab 5 — for example the complaint-handling lesson — as the input for this lab's content.", ""),
 ("Draft the learning content for that lesson. Paste the prompt below, with the lesson plan pasted in.",
  "You are an instructional designer writing for new frontline retail staff who may be first-time workers. From this lesson plan: '[PASTE LESSON PLAN]', write the learning content: a clear explanation of the key idea, one or two relatable retail examples, and a simple step-by-step model learners can apply (for handling a complaint, use a short service-recovery method). Write in plain, warm, active language, and chunk it into short sections with headings."),
 ("Generate active learning activities. Paste the prompt below.",
  "For the same lesson, create three activities that get learners doing, not just reading: (1) a short discussion prompt, (2) a two-person role-play with a brief setup and roles, and (3) a realistic branching scenario where a customer makes a complaint and the learner chooses between three responses, with feedback for each choice. Keep them practical and set in a neighbourhood retail store."),
 ("Chunk and simplify. Paste the prompt below.",
  "Rewrite this content into short, digestible chunks with clear headings, plain language at about a secondary-school reading level, active voice, and a warm, encouraging tone. Cut jargon or explain it in one line."),
 ("Check realism and bias: read every example and the scenario, and confirm they are realistic for a Singapore neighbourhood store and free of stereotypes about customers or staff. Rewrite anything that feels unrealistic, unfair or that singles out any group.", ""),
 ("Confirm alignment: check that this content and its activities actually serve the lesson's objective — cut anything interesting-but-off-objective, and add anything the objective needs that is missing.", ""),
 ("Generate the content and activities for the remaining lessons the same way, keeping the tone and structure consistent across the whole course, then save it all in your project folder. This developed content is what you assess in Lab 7 and produce in Lab 8.", ""),
 ],
 test="You have developed learning content for the lessons — clear, chunked, plain-language explanations with realistic, bias-checked examples and a simple model — plus a discussion activity, a role-play and a branching scenario per key lesson, each aligned to its objective. Saved and ready to assess.",
 ),
 dict(
 num=7, topic=2,
 title="Create Quizzes, Assessments and Rubrics with AI",
 objective="Create assessment that measures the objectives — quiz items with answer guides, a scenario-based performance task, and a rubric — all aligned to the learning objectives and checked for quality and fairness.",
 desc="A course is only as good as the evidence that learners can do what it promised. In this lab you use AI to "
 "build assessment that measures your objectives. You generate a short quiz (multiple-choice, true/false and "
 "short-answer items) with an answer guide and a rationale for each item, then a scenario-based performance task "
 "where a learner handles a mock complaint. Crucially, you check quality: every quiz item must map to an "
 "objective, have exactly one defensible correct answer with plausible distractors and no giveaway cues, and "
 "sit at the right cognitive level. You then have AI draft a criteria-based rubric for the performance task — "
 "with clear criteria and performance levels — and you calibrate it to Meridian's standard. The result is "
 "aligned, fair assessment ready to slot into the package. " + PROJECT_NOTE,
 build="A short quiz with an answer guide and rationales, a scenario-based performance task, and a criteria-based rubric for the Meridian course — every item mapped to an objective, checked for one correct answer, plausible distractors and the right level, and calibrated to standard.",
 services="ChatGPT / Claude / Gemini, quiz-item writing, distractors and answer guides, scenario/performance tasks, rubric design, objective alignment, item-quality review",
 steps=[
 ("Open your final learning objectives from Lab 3 — every assessment item must measure one of them.", ""),
 ("Generate a short quiz aligned to the objectives. Paste the prompt below, with your objectives pasted in.",
  "You are an assessment writer. From these learning objectives: '[PASTE OBJECTIVES]', write a 6-question quiz for new retail staff: a mix of multiple-choice (four options), true/false and one short-answer item. For each item, note which objective it measures, give the correct answer, and add a one-line rationale. Make the wrong options plausible, not obvious."),
 ("Create a scenario-based performance task. Paste the prompt below.",
  "Write a short scenario-based performance task for the same course: a realistic customer-complaint situation an associate must handle, the instructions to the learner, and what a good response would include. Tie it explicitly to the complaint-handling and escalation objectives."),
 ("Quality-check the quiz items. Paste the prompt below and fix whatever it flags.",
  "Review this quiz for item quality: does each item map to an objective, does each multiple-choice item have exactly one defensible correct answer with plausible distractors and no giveaway cues (such as 'all of the above' or the longest option always being right), and is each at an appropriate difficulty? Flag and rewrite any weak item."),
 ("Build a rubric for the performance task. Paste the prompt below.",
  "Create a criteria-based rubric to assess the complaint-handling performance task. Use 3 to 4 criteria (for example: stayed calm and empathetic, understood the customer's need, applied the service-recovery steps, knew when to escalate) and 3 performance levels (for example: developing, proficient, strong) with a short descriptor for each cell. Present it as a table."),
 ("Calibrate the rubric to standard: adjust the criteria and level descriptors so 'proficient' really reflects what Meridian expects of a new associate — not too lenient, not unrealistic for a first week — and make sure the criteria match the performance task and the objectives.", ""),
 ("Save the quiz with its answer guide, the performance task, and the rubric in your project folder, noting the objective each piece measures. This aligned assessment slots into the package in Lab 10.", ""),
 ],
 test="You have a short quiz with an answer guide and rationales, a scenario-based performance task, and a calibrated criteria-based rubric — every item mapped to an objective, each multiple-choice item checked for one correct answer, plausible distractors and no giveaway cues, and the rubric matched to Meridian's standard. Saved in your project folder.",
 ),
 dict(
 num=8, topic=2,
 title="Produce Scripts, Visuals and Job Aids with AI",
 objective="Produce the learner-facing media — a narration script and storyboard for the e-learning module, on-brand visuals, and take-away job aids — that make the course usable and support performance on the job.",
 desc="Now you produce the material learners see, hear and keep. In this lab you use AI three ways. First, you "
 "draft a short narration script and a storyboard for the e-learning module — for each screen, the on-screen "
 "text, the narration and the visual — written to be heard, not read. Second, you use an AI image tool to "
 "create on-brand visuals for the key screens and slides (a greeting, a complaint being resolved), keeping the "
 "style consistent and writing alt text for each so the material is accessible. Third, you create the "
 "take-away job aids learners keep after the course — a one-page complaint-handling checklist and a "
 "quick-reference card of the service steps. You check every visual is appropriate and licence-clear and every "
 "job aid is genuinely usable at the counter. " + PROJECT_NOTE,
 build="A narration script and storyboard for the e-learning module, a consistent set of on-brand visuals with alt text for the key screens, and take-away job aids (a complaint-handling checklist and a quick-reference card) — all produced and checked for consistency, accessibility and appropriateness.",
 services="ChatGPT / Claude / Gemini, narration scripts and storyboards, AI image generation, image prompting, alt text and accessibility, job-aid and checklist design, licensing check",
 steps=[
 ("Choose the lesson to turn into the short e-learning module — for example the complaint-handling lesson — and open its content from Lab 6.", ""),
 ("Draft the narration script and storyboard. Paste the prompt below, with the lesson content pasted in.",
  "You are an e-learning developer. From this lesson content: '[PASTE CONTENT]', write a storyboard for a short e-learning module. For each screen give: the on-screen text (brief), the narration (written to be heard, warm and clear, a few sentences), and a note on the visual. Keep the whole module to about 6 to 8 screens and roughly three to four minutes of narration."),
 ("Generate an on-brand visual for a key screen. Paste the image prompt below into your image tool.",
  "A clean, friendly flat illustration of a retail associate calmly helping a customer who looks concerned, in a bright neighbourhood lifestyle store, warm and approachable style, simple shapes, no text and no real brand logos, suitable for a training e-learning screen."),
 ("Generate the other visuals the same way, keeping the style consistent (same look, colours and character style) so the module feels like one course. For each image, write one line of alt text describing what it shows, so learners using a screen reader can follow along.", ""),
 ("Check appropriateness and licensing: no real company logos or identifiable real people, confirm your image tool's terms allow training use, and note where you will disclose that images are AI-generated. Replace anything you are unsure about.", ""),
 ("Create the take-away job aids. Paste the prompt below.",
  "Create two take-away job aids for new retail associates: (1) a one-page complaint-handling checklist using the service-recovery steps from the course, and (2) a wallet-sized quick-reference card of the greeting-to-resolution steps. Keep them short, plain, action-first, and usable at the counter in the moment."),
 ("Review the job aids for real-world usability — could a nervous new associate actually glance at this mid-shift and know what to do? Tighten anything wordy, then save the script, storyboard, visuals with alt text, and job aids in your project folder.", ""),
 ],
 test="You have a storyboard and narration script for a short e-learning module, a consistent set of on-brand, appropriate, licence-checked visuals each with alt text, and two usable take-away job aids (a complaint-handling checklist and a quick-reference card) — all saved in your project folder.",
 ),
 dict(
 num=9, topic=2,
 title="Align to Outcomes and Quality-Check the AI Output",
 objective="Run a full alignment and quality pass — map every artifact to an objective, find gaps and orphans, and check all AI-generated material for accuracy, bias, reading level and instructional soundness before it reaches learners.",
 desc="Before a course is delivered, it must be checked. In this lab you run two disciplined passes over "
 "everything you have built. First, alignment: you build an alignment matrix that maps every objective to the "
 "content, activity and assessment that serve it, using AI to surface gaps (an objective with no assessment) "
 "and orphans (content that serves no objective), and you fix them. Second, quality: you have AI review the "
 "material — but critically, not trustingly — for factual accuracy (which you confirm with a subject expert or "
 "the brief, never the AI alone), for bias and stereotypes, for reading level and plain language, and for "
 "accessibility. You compile a short quality-check report of what you found and fixed. This is where you take "
 "ownership of the instructional quality of the whole package. " + PROJECT_NOTE,
 build="An alignment matrix mapping every objective to its content, activity and assessment (with gaps and orphans fixed), plus a completed quality-check pass and short report covering accuracy, bias, reading level and accessibility — so the whole package is aligned and ready to finalise.",
 services="ChatGPT / Claude / Gemini, alignment matrices, gap and orphan analysis, fact-checking, bias and stereotype review, readability checks, accessibility review",
 steps=[
 ("Gather every artifact you have built: objectives (Lab 3), curriculum map and lesson plans (Labs 4-5), content and activities (Lab 6), quiz, task and rubric (Lab 7), and script, visuals and job aids (Lab 8).", ""),
 ("Build the alignment matrix. Paste the prompt below, with your objectives and a list of your artifacts pasted in.",
  "You are a quality reviewer. Here are my learning objectives: '[PASTE OBJECTIVES]', and my course artifacts: '[LIST CONTENT, ACTIVITIES, QUIZ ITEMS, TASK, JOB AIDS]'. Build an alignment matrix mapping each objective to the content, activity and assessment that serve it. Flag any objective with no assessment (a gap) and any artifact that serves no objective (an orphan)."),
 ("Fix gaps and orphans: for every objective missing an assessment, add or reassign an item; for every orphan, either tie it to an objective or cut it. Re-run the check until every objective is covered and nothing is orphaned.", ""),
 ("Run the accuracy and bias quality check. Paste the prompt below.",
  "Review all this course material for quality: flag any factual claim I must verify with a subject expert, any example or scenario that could carry a stereotype or unfair assumption, and anything that reads as too strong or absolute to defend. List each issue with the fix you recommend. Do not assume your own facts are correct — mark them for me to confirm."),
 ("Confirm the facts yourself: take every claim the AI flagged (and any Meridian policy or service standard) and confirm it against the supplied brief or a subject expert — never on the AI's word alone — and correct anything wrong. Resolve every [VERIFY] placeholder left from earlier labs.", ""),
 ("Check readability and accessibility. Paste the prompt below, then apply the fixes.",
  "Check this learner-facing content for reading level and accessibility: is it plain language at about a secondary-school level, active voice, jargon explained; do all images have alt text; and is anything conveyed by colour or image alone that a learner might miss? List what to improve."),
 ("Compile a short quality-check report in your project folder: the alignment matrix, the issues found (accuracy, bias, readability, accessibility) and how each was fixed. The package is now aligned and quality-checked, ready to assemble in Lab 10.", ""),
 ],
 test="You have an alignment matrix with every objective mapped to its content, activity and assessment and all gaps and orphans fixed, plus a completed quality-check covering accuracy (facts confirmed against the brief or an expert, no [VERIFY] left), bias, reading level and accessibility — captured in a short report in your project folder.",
 ),
 dict(
 num=10, topic=2,
 title="Assemble, Review and Finalise the Course Package",
 objective="Assemble every artifact into one consistent facilitator and learner package, run a final review, and finalise the Meridian Service Excellence course kit ready to deliver — end to end.",
 desc="The last mile is assembly and handover. In this lab you bring every reviewed artifact together into one "
 "coherent course package: a facilitator guide (the lesson plans, timings, activity instructions, answer guide "
 "and rubric) and a learner set (the content, the e-learning module storyboard, the quiz, and the take-away "
 "job aids). You use AI to draft a course overview and a facilitator guide that stitches the lesson plans into "
 "a runnable flow, then you run a final consistency pass — one voice, consistent terms, correct objective "
 "numbering and no leftover placeholders. You do a final human review against the objectives one last time, "
 "confirm every fact is verified, and finalise and export the package. That completes the Meridian Service "
 "Excellence course kit — from a training request to a deliverable course — end to end. " + PROJECT_NOTE,
 build="A finished, assembled course package — a facilitator guide (course overview, lesson plans, timings, activity instructions, answer guide and rubric) and a learner set (content, e-learning storyboard, quiz and job aids) — run through a final consistency and human review, with every fact verified and no placeholders left, exported and ready to deliver.",
 services="ChatGPT / Claude / Gemini, package assembly, facilitator guide, course overview, consistency pass, final human review, exporting the package",
 steps=[
 ("Lay out every reviewed artifact from Labs 3-9 in the order it belongs in the package: overview, objectives, lesson plans, content, activities, e-learning storyboard, quiz and answer guide, performance task and rubric, and job aids.", ""),
 ("Draft the course overview and facilitator guide. Paste the prompt below, with your lesson plans and objectives pasted in.",
  "You are an instructional designer assembling a course package. Using these objectives and lesson plans: '[PASTE]', write (1) a one-page course overview — purpose, audience, objectives, duration and structure — and (2) a facilitator guide that stitches the lesson plans into a runnable three-hour flow, with timings, what the facilitator does at each step, and where the activities, quiz and job aids are used."),
 ("Run a final consistency pass. Paste the prompt below.",
  "Do a consistency pass across this whole course package: make the voice and tone consistent, standardise key terms (for example the name of the service-recovery method), check the objective numbering matches everywhere, and flag any leftover placeholder, [VERIFY] tag or 'TODO'. Return a list of what to fix."),
 ("Fix everything the consistency pass flagged, and resolve any last placeholder — nothing marked [VERIFY] or 'TODO' may remain in a package about to be delivered.", ""),
 ("Do a final human review against the objectives: read the package once as a whole and confirm a new associate who completes it would genuinely be able to do each objective, the assessment fairly measures each, and the facilitator could run it in three hours. Adjust anything that fails this test.", ""),
 ("Split the package into the two audiences: a facilitator guide (with the answer guide and rubric) and a learner set (without the answer guide), so each reader gets what they need.", ""),
 ("Export and save the finished package (as documents or a PDF) in your project folder, with a short contents page. This complete, aligned, quality-checked Meridian Service Excellence course kit is the deliverable the whole course set out to build — and remember, you, not the AI, own its instructional quality.", ""),
 ],
 test="You have assembled every reviewed artifact into one coherent package — a facilitator guide (overview, lesson plans, timings, activity instructions, answer guide and rubric) and a learner set (content, e-learning storyboard, quiz and job aids) — run a final consistency and human review against the objectives, verified every fact with no placeholders left, and exported the finished Meridian Service Excellence course kit ready to deliver.",
 ),
]
