

# Get started

To build and assign a training plan with Team Skills Planner, complete the following steps:

1. Sign in to [AWS Skill Builder](https://skillbuilder.aws/) as a Learning Administrator.

1. In the top navigation bar on the AWS Skill Builder Admin page, choose the **Team Skills Planner** tab.

1. Choose **Create your first goal** or **Create goal**.

1. Describe your goal in the chat box, or upload documents that describe it.

1. Review the proposed roles and job tasks, then choose **Save**.

1. (Optional) Choose **Set a baseline**, send the link to your team, and review the results when it closes.

1. Review the training recommendations and refine the plan.

1. Assign the plan, self-paced or as a cohort, and track progress.

 **Expected result**: Your goal appears on the Team Skills Planner tab with its roles, training plan, and assigned learners. Learners receive an email message about their assigned training.

## Create a goal
<a name="team-skills-planner-create-a-goal"></a>

After choosing **Create goal**, upload documents on what your team is working toward or describe your priorities in the chat box.

Choose **Upload documents** and upload one or more documents, such as an IT strategy, account plan, or meeting notes. Supported formats are PDF, DOCX, TXT, and JSON. You can upload up to five files, up to 25 MB each. Team Skills Planner proposes goals from what’s in them. Team Skills Planner can propose one or more goals. If the documents describe a single coherent commitment, it proposes one goal. If the documents describe several, it can propose multiple goals, each with its own roles and job tasks. It also checks for overlap with your existing Team Skills Planner goals.

Choose **Describe in chat** and then enter what your organization needs to achieve. For example:
+ "Our product team is building a generative AI assistant into our customer app on Amazon Bedrock, launching in Q2. The team is 40 engineers, 5 engineering managers, and 3 product managers."
+ "We’re migrating 200 on-premises applications to AWS over the next 18 months. The team is 12 solutions architects and 30 cloud operations engineers."

Team Skills Planner asks follow-up questions to shape the goal with you, as well as shape the compliance and data-handling focus of the plan.

**Note**  
Don’t include personal information in chat or uploads. Use is subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

## Review and refine roles and job tasks
<a name="team-skills-planner-review-and-refine"></a>

Team Skills Planner proposes a goal with a name, description, and the reasoning behind it, along with the roles involved.

Each proposed goal includes a **Why explanation**, and the AI assistant explains why it proposed each role, for example, "architects owning portfolio-level migration approaches and resilient target designs." It also notes what it left out and any information missing from your input. You can ask the AI assistant for a plain-language walkthrough of why certain job tasks were included and others left out.

Team Skills Planner proposes roles from its library and the job tasks that are relevant to your team’s goal. Remove any role your organization doesn’t need, ask the AI assistant to add one, and adjust each role’s job tasks so they match how your organization works.

On the Review and Refine page, Team Skills Planner pre-selects the job tasks most aligned with your goal and each role’s focus. Each role shows how many job tasks are included (for example, 30 of 86) and the estimated training hours.

You can edit directly or ask the AI assistant to make changes, for example:
+ "Why did you include these job tasks for Implementation and Integration?"
+ "Add job tasks on resilience and disaster recovery for the Solutions Architect role."

Changes the AI assistant makes stay unsaved until you choose **Save**.
+  **Including or excluding a domain** — Select or clear a domain to include or exclude all its job tasks for that role.
+  **Including or excluding individual job tasks** — Expand a domain to add omitted job tasks, include the complete job task set, or remove job tasks that aren’t relevant. You can also edit or remove a role, or ask the assistant to add one.

## Save the goal
<a name="team-skills-planner-save-the-goal"></a>

Choose **Save** or **Save and continue** to create the goal. Next, you can choose **Set a baseline** or go straight to training recommendations. After a baseline starts, you can’t edit the goal, its roles, or its job tasks.

## Run a baseline assessment
<a name="team-skills-planner-run-a-baseline"></a>

A baseline is a short, goal-focused skill check against the job tasks you selected for each role. It shows where your team stands, so recommendations close real gaps rather than assumed ones. The baseline is *optional*. It’s most useful when proficiency is uncertain, experience varies across a role, the team is taking on a new goal, or leaders need evidence of which job tasks require training. You might skip it if you have recent, trusted proficiency data, or if the same mandatory training goes to everyone.

 **How the baseline is built** 

A baseline measures the team, not each individual. Each respondent answers a short set of questions, and different respondents receive questions on different job tasks. Together, the team’s answers cover the role’s selected job tasks. This keeps each learner’s time short while still measuring the full scope of the role.

 **Send a baseline to a team** 

Share a single baseline link with your team. Each learner opens the link, enters an alias, chooses the role closest to their work, and answers a short, timed set of questions for that role. The questions test product knowledge in a short, game-like format, and each question takes about one minute. Ask learners to choose an alias that isn’t their name or email address. Some questions can have more than one correct answer. Learners don’t need to create or sign in to a Skill Builder account. The baseline link doesn’t grant access to the planning experience.

 **How many people to invite** 

Each respondent answers a short set of questions, and the questions are spread across the role’s job tasks. A job task needs at least one answer to be measured, and more answers give a stronger evidence level. A role with more job tasks needs more respondents. If only a few people are in a role, include fewer job tasks before you start the baseline, or treat the results as a light signal.

 **When the baseline closes** 

Learners can respond until the baseline closes. If you close a baseline early, the results show this note: "This baseline was closed early. Results may be partial — not everyone may have had time to respond."

 **How results are scored** 

Results show how many of the selected job tasks the group can do for each role and domain, and a team level for the role, such as Beginner. For example, a Machine Learning Engineer group might cover 14 of 80 job tasks, 18 percent, across four domains.

 **Interpret group-level results** 

Results are aggregated by role and domain. Individual learner answers and scores aren’t shown. For each role you see the number of respondents, job tasks met per domain, the strongest and weakest domains, and where most of the training plan focuses. A chart shows the team’s current position against each domain.

 **Baseline evidence levels** 

Each result shows how much evidence supports it:
+  **Strong** — Enough responses to treat the result as a reliable read.
+  **Moderate** — Use the result as a directional read.
+  **Limited** — Few responses, so treat the result as a light signal.
+  **Not measured** — No respondent answered questions on this job task.

 **Choose what goes into the plan** 

For each job task, the results show how many respondents passed, the evidence level, and whether the job task is included in the plan. Team Skills Planner takes out job tasks the group has already covered with strong evidence, so the team doesn’t repeat training it doesn’t need. Job tasks with limited evidence, or that weren’t measured, stay in.

You can choose to include or remove any job task in the plan under the **Include In Plan** column. Changes you make are marked your change, and you can choose **Restore recommendations** to go back to the suggested selection. This changes what the training plan covers. It doesn’t change the role’s job tasks, which stay locked after the baseline starts.

## Review training recommendations
<a name="team-skills-planner-review-recommendations"></a>

For each role, Team Skills Planner recommends training from the full AWS Training and Certification catalog, targeting job tasks the baseline shows aren’t yet covered, or the full saved scope if no baseline ran. Training is grouped into training areas, and the plan explains why it was built that way (Why this plan).

The plan summary shows the number of training areas, courses, total Digital Training hours, and total Classroom Training days. Each item shows:
+  **Format** — The type of training, such as Digital Training, AWS Builder Lab, AWS SimuLearn, or Classroom Training.
+  **Access** — Free, Subscription (requires AWS Skill Builder Team Subscription), or Purchase required (AWS Classroom Training is purchased separately).
+  **Duration** — Estimated hours or days.

 **Refining the plan** 

Everything is pre-selected, and you can keep editing until you assign learners. Ask the AI assistant or use the quick options to choose learning formats (including Blended, which lets Team Skills Planner choose the mix), filter by access type, or add skill validation such as microcredentials. For example:
+ "Prioritize immersive and self-paced Digital Training."
+ "Add skill validation, such as microcredentials, for each role."

The AI assistant suggests training to add, grouped by training area. Choose **Add** for an item or **Apply all** for a training area, then choose **Confirm changes**. Nothing already in the plan is removed, so remove any items you don’t need.
+  **Explore options** — Choose **Explore options** in a training area to see alternative training, or to add specific courses you want your team to take.
+  **Swap or remove items** — Replace or remove individual items, then choose **Save plan**.
+  **Understand access types** — Access tags on each item show whether it’s free, requires a Team Subscription, or must be purchased. Team Skills Planner doesn’t check how many seats are available in your subscription. Use the access-type filter to limit recommendations to training your organization can already access and confirm seat availability before you assign.

## Assign training
<a name="team-skills-planner-assign-training"></a>

Choose a delivery model that fits the goal and team: **self-paced** or **cohort**.
+  **Self-paced** — Learners work through the plan on their own schedule.
+  **Cohort** — The team moves through the plan together on a shared timeline that can include scheduled sessions such as AWS Classroom Training. Each cohort has an end date.

Choose self-paced when learners have different schedules or starting points. Choose cohort delivery when roles must be ready at the same time or on a deadline (for example, a migration wave), or when the plan includes classroom training.

You choose the delivery model for each role, so one goal can use both. For example, put technical roles in a cohort to move through the content together, and give other roles a self-paced plan.

 **Save the plan**, then **select the learners** to assign it to.

 **Set up a cohort.** For each role you want to run as a cohort, choose **Team-based cohort** as the learning format. Enter the estimated effort in hours per week, and Team Skills Planner calculates how long the cohort runs.

The recommended training becomes the cohort agenda, and pinned activities stay available for the whole cohort. You can turn on leaderboards to rank participants by the points they earn. You’re set as the cohort administrator automatically.

 **Seat and subscription considerations before assigning** 
+ Team Skills Planner doesn’t check seat availability. Confirm you have enough seats before you assign.
+ Cohort delivery requires an AWS Skill Builder Team Subscription, and each learner in a cohort needs Team Subscription access.
+ Items tagged Subscription require Team Subscription access; AWS Classroom Training is purchased separately.
+ Access requirements can vary by training type and organization setup. Discuss subscription, learner access, and purchasing options with your AWS Training representative.