

# Managing evaluations
<a name="managing-evaluations"></a>

This page covers how to create, edit, and publish evaluations in Amazon Connect Talent.

**Note**  
ATS integrations are not available at launch. Support for ATS integrations is coming soon. For more information, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html) in the *Amazon Connect Talent Administrator Guide*.

## Create an evaluation
<a name="create-candidate-evaluation"></a>

A candidate evaluation is an AI-generated set of assessments and behavioral AI-led interview questions tailored to a specific job. Amazon Connect Talent analyzes the job description and your knowledge base, identifies key competencies, and produces a structured evaluation for you to review before publishing.

### Prerequisites
<a name="create-eval-prerequisites"></a>

Before you create a candidate evaluation, verify that you have the following:
+ An Amazon Connect Talent instance
+ Permissions to create evaluations. For more information about the permissions required to create evaluations, see the [Amazon Connect Talent Administrator Guide](https://docs.aws.amazon.com/talent/latest/adminguide/manage-security-profiles.html).
+ An ATS integration, if you want to send evaluations to candidates automatically. To set up your integration, see the [Amazon Connect Talent Administrator Guide](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html). If you are testing Amazon Connect Talent with internal users, an ATS integration is not required. To learn more, see [How to test Amazon Connect Talent](getting-started-test.md).

### To start creating an evaluation
<a name="create-eval-start"></a>

You can start creating an evaluation from the home page or the Evaluations page.
+ On the home page, choose **Create** in the **Recently created evaluations** section.
+ Or navigate to **Evaluations** in the sidebar and choose **Create evaluation**.

### Select a job
<a name="create-eval-select-job"></a>

In this step, you select the job you want to build the evaluation for. Amazon Connect Talent uses the job description to identify competencies and generate the evaluation. You have two options:
+ **Search for an existing job** – Use the search box or browse the **Most recently added** cards. Each card displays the job title, description, creation date, and last updated date.
+ **Upload or describe a job** – Choose **Upload or describe** to provide a job description directly. Use this option if you don't have a job in the system yet.

For more information about adding jobs to Amazon Connect Talent, see [Add a job](jobs.md#jobs-create).

### Wait for AI generation
<a name="create-eval-generation"></a>

After you select a job, Amazon Connect Talent generates the evaluation. A loading screen appears with a status indicator while Amazon Connect Talent analyzes the job and builds a tailored evaluation. Do not navigate away from this page during generation. This process takes approximately 90 seconds.

### Review the generated evaluation
<a name="create-eval-review"></a>

When generation completes, Amazon Connect Talent displays the message "Your evaluation is ready to publish." You can publish the evaluation, save it as a draft, or make edits. The page contains the following sections:
+ **Overview** – The job used to build the evaluation, the five key competencies selected for the job, and the evaluation language. Choose a competency to see why Amazon Connect Talent selected it for the role.
+ **Assessments** – Science-backed assessments tailored to the job, with an estimated duration for candidates (for example, \~8 mins). Each assessment shows what it measures, the competencies it evaluates, and how many of the job's competencies it covers. Amazon Connect Talent selects assessments based on the job's competencies, so not every evaluation includes assessments. For more information, see [How assessments work](assessments.md).
+ **AI-led interview** – Behavioral questions with dynamic follow-ups, with an estimated duration for candidates (for example, \~30 mins). Each question displays the competency it measures and shows how many of the job's competencies the interview covers. Every evaluation includes an AI-led interview by default, but you can remove it during editing. For more information, see [How AI-led interviews work](ai-led-interviews.md).

The estimated durations help you understand the total time commitment candidates need to complete the evaluation.

## Edit the evaluation
<a name="edit-evaluation"></a>

Before you publish an evaluation, you can adjust its AI-led interview questions, assessments, and language. After you publish an evaluation, it becomes read-only.

**Important**  
You can't edit an evaluation after you publish it. A published evaluation is read-only. You can edit an evaluation only during creation or while it is saved as a draft. If you want a colleague to review the evaluation before publishing, save it as a draft and share the draft with them.

### Edit AI-led interview questions
<a name="edit-eval-interview"></a>

1. Choose **Edit** next to **AI-led interview**.

1. Review the list of questions. Each question displays the question text and associated competency.

1. Choose the options menu on a question to access editing options:
   + **Rewrite** – Enter guidance and Amazon Connect Talent rewrites the question using AI. You can also paste in existing interview questions your organization uses. Amazon Connect Talent may make slight adjustments to optimize the question for an AI-led interview format.
   + **Remove** – Removes the question.

1. To add a question, choose **Add question**, select a competency, and optionally enter guidance to direct the AI. The competency list shows up to 15 competencies that Amazon Connect Talent identifies for the job, including competencies that are not among the five shown during evaluation creation.

1. Choose **Save**, then choose **Back to overview**.

You can restore a removed question while you work. Each interview module starts with a default set of questions, and Amazon Connect Talent estimates the interview duration from the number of questions.

**Important**  
AI-led interviews have a maximum duration of 30 minutes, at which point the interview ends. The interviewer informs the candidate that the interview is ending. If the candidate has not answered all of the questions, this does not negatively affect their score. Amazon Connect Talent scores only competencies for which the candidate provided a response. To learn more about how scoring works, see [How scoring works](how-scoring-works.md).

### Edit assessments
<a name="edit-eval-assessments"></a>

Amazon Connect Talent selects assessments based on the job's competencies. Because assessments are competency-driven, not every evaluation includes them – Amazon Connect Talent adds assessments only when the job's competencies match what an assessment measures. The following assessment types are available:


| Assessment type | Description | 
| --- | --- | 
| Work approach | Measures how a candidate approaches their work. | 
| Problem solving | Measures how a candidate works through problems. | 

Each assessment displays the following details:
+ What this measures
+ The competencies it evaluates
+ Customized terms (Problem solving only)
+ Mobile preview

#### To edit customized terms
<a name="edit-eval-terms"></a>

For Problem solving assessments, you can customize the terms used in scenarios. The assessment displays a table of generic terms and their customized equivalents.

1. Choose the edit icon next to the term you want to change.

1. In the dialog, review the **Generic Term** field (read-only) and enter a new value in the **Customized Term** field.

1. Choose **Update**.

Amazon Connect Talent checks each customized term for relevance and reverts values it cannot use.

#### To remove assessments
<a name="edit-eval-remove"></a>

You can remove individual assessments or all assessments at once.
+ To remove an individual assessment, choose the options menu for the assessment and choose **Remove**.
+ To remove all assessments, choose **Remove all assessments**.

### Set the evaluation language
<a name="evaluations-language"></a>

You can set or change the evaluation language from the Overview section. Amazon Connect Talent uses this language for all assessment and interview questions, and conducts the AI-led interview in that language.

**Note**  
If your knowledge base includes competencies written in a specific language, and those competencies are selected for an evaluation, changing the evaluation language does not translate those competencies. This only affects what recruiters see — the candidate experience is fully localized in the selected language regardless of the language used in your knowledge base.

Amazon Connect Talent supports the following languages for the candidate evaluation:


| Language | Locale | 
| --- | --- | 
| English (United States) | en-US | 
| English (Australia) | en-AU | 
| English (United Kingdom) | en-GB | 
| Portuguese (Brazil) | pt-BR | 
| French (France) | fr-FR | 
| Italian (Italy) | it-IT | 
| German (Germany) | de-DE | 
| Spanish (United States) | es-US | 

**Note**  
When you change the language, Amazon Connect Talent regenerates the evaluation. This replaces the current AI-led interview questions and assessments with new content in the selected language.

### Manage draft content
<a name="edit-eval-drafts"></a>

When you save an evaluation as a draft, you retain the full editing capabilities you had during creation. You can locate your draft evaluations in two ways:
+ Navigate to **Evaluations** in the sidebar and check the **Status** column for drafts.
+ Recently created drafts also appear on your home page in the **Drafts you haven't finished yet** card.

To open a draft for editing:

1. In the sidebar, choose **Evaluations**, or locate your recently created draft on the home page.

1. Choose the draft evaluation you want to edit. The **Edit** control isn't available for a published evaluation.

1. Choose **Edit** on the assessments, AI-led interview, or language section to make changes.

## Publish an evaluation
<a name="evaluations-publish"></a>

When you publish an evaluation, Amazon Connect Talent assembles the final evaluation from the selected competencies, questions, and scoring rubrics.

You can publish an evaluation only when it includes at least one assessment or one interview question.

1. Choose **Publish**.

1. You are prompted to **Choose where this evaluation runs**. Select the open job this evaluation should be used for from the list of active jobs synced from your ATS, and choose the application stage at which candidates receive their evaluation invitation. For more information, see [Sending evaluations to candidates](evaluations-send.md).

1. In the dialog, edit the evaluation name. The name is pre-filled with the job title.

1. Choose **Publish** to finalize.

Amazon Connect Talent returns you to the home page. The evaluation appears in the **Recently created evaluations** table. After you publish, the entire evaluation is read-only and cannot be edited.