

# Review candidate results
<a name="review-candidate-results"></a>

After a candidate completes an evaluation, you can review the results on the candidate results page. There are two ways to open it:
+ **From Amazon Connect Talent** – On the job candidates page, choose a candidate ID to open their results. For more information about the job candidates page, see [Candidates](candidates.md).
+ **From your ATS** – When a candidate completes their evaluation, Amazon Connect Talent writes a completion event to your ATS that includes a link to the candidate's results. Choose this link to go directly to the candidate results page in Amazon Connect Talent.

**Note**  
After a candidate completes an evaluation, their results can take up to two hours to appear in Amazon Connect Talent.

**Note**  
ATS integrations are not available at launch. Support for ATS integrations is coming soon. For more information, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html) in the *Amazon Connect Talent Administrator Guide*.

## The candidate results page
<a name="rcr-page"></a>

At the top of the page, you see the candidate's unique identifier assigned by Amazon Connect Talent, evaluation status, and application status. You can also choose **Copy email** to copy the candidate's email address, or choose **Change status** to update the candidate's application status. The back arrow returns you to the job candidates page for the job.

**Note**  
The candidate identifier is unique to Amazon Connect Talent and does not match the identifier that your applicant tracking system uses for the same candidate. Changing a candidate's application status in Amazon Connect Talent does not update the status in your applicant tracking system and does not notify the candidate.

Results are organized into three sections: Overview, Assessments, and AI-led interview.

The sections that appear depend on what the evaluation includes. For example, if an evaluation doesn't include assessments, the Assessments section doesn't appear on the candidate results page. You see results only for the components that are part of the candidate's evaluation.

### Candidates with multiple evaluations
<a name="rcr-multiple-evaluations"></a>

When a candidate has completed more than one evaluation for a job, the candidate results page shows results for each evaluation separately. Each evaluation appears under its evaluation title with its own evaluation status and results, listed in order of completion date with the most recently completed evaluation at the top.

The Overview, Assessments, and AI-led interview sections group results by evaluation — so you can compare how the candidate performed across evaluations. Each evaluation's scores and narrative explanations are independent.

### Overview
<a name="rcr-overview"></a>

The Overview section gives you a high-level picture of how the candidate performed across the entire evaluation. Assessment results and AI-led interview results appear side by side, so you can quickly see where a candidate is strong and where they need development, without drilling into the details.

Start here to get a quick read on the candidate before you review the Assessments or AI-led interview sections for the full detail.

### Assessments
<a name="rcr-assessments"></a>

The Assessments section shows the full results for each assessment included in the evaluation. Each competency measured by the assessment has a score on the four-level assessment scale. These scores reflect how closely the candidate's responses match the behavioral patterns associated with success in that competency — they are not pass/fail judgments. For more information about the scale, see [How assessments work](assessments.md).

A High or Very High score means the candidate's responses aligned well with the behaviors expected for that competency. A Low or Moderate score means the candidate's responses were less aligned — it does not mean the candidate failed.

Use assessment results alongside interview results to build a fuller picture of the candidate. For more information about how assessments are selected and scored, see [How assessments work](assessments.md).

### AI-led interview
<a name="rcr-interview"></a>

The AI-led interview section shows the overall interview score and a card for each competency the interview measured.

#### Interview score
<a name="rcr-interview-score"></a>

Amazon Connect Talent scores each competency on a 1–5 scale. The overall interview score is the equal average of all competency scores, so every competency counts the same.

Each competency card includes a score (1–5) and a detailed narrative. The narrative describes what the candidate said, which strengths were observed, and where evidence was limited or absent, so you can understand *why* a candidate received a particular score, not just what the score is.

Expand a competency card to read the full narrative.

#### Not scored compared with a low score
<a name="rcr-not-enough-data"></a>

Amazon Connect Talent treats a low score and a lack of evidence as two different things. Understanding this distinction helps you read interview results correctly.
+ **A low score** – The candidate answered but did not demonstrate the behavior the rubric defines for that competency. The candidate had the opportunity to show the behavior and did not.
+ **Not scored** – The competency was not covered. For example, the interview ended early, was interrupted, or the candidate withdrew. Amazon Connect Talent reports "Not scored" for that competency, and for the overall score, instead of producing a partial or misleading number.

The difference matters: a low score tells you something about the candidate's demonstrated abilities. "Not scored" tells you nothing — the candidate didn't have the chance to demonstrate the competency.

When a competency shows "Not scored," the card displays a message explaining why and, where available, links to the related question in the interview playback. While scoring is still in progress after an interview, the score appears blank until scoring finishes — this does not mean "Not scored."

#### Interview playback
<a name="rcr-playback"></a>

The interview playback lets you go beyond the scores and read exactly what the candidate said. This is where you verify whether a score reflects your own reading of the evidence, understand the context behind a content flag, or prepare for a conversation with the candidate or hiring manager.

To open the playback, choose the interview playback link from the AI-led interview section on the candidate results page.

The playback page starts with an **At a glance** summary — the overall interview score and a per-competency narrative that explains what evidence was observed and what was not. Below that, the **Transcript** shows the full conversation, with interview questions on the left (each tagged with the competency it measures) and the candidate's responses on the right, synchronized with timestamps.

Every score Amazon Connect Talent assigns can be traced back to a specific moment in the transcript. If a competency score seems too high or too low, the playback gives you the evidence to understand why.

##### Provide feedback
<a name="rcr-feedback"></a>

At the top of the playback page, choose **Review evaluation** to provide detailed feedback on the evaluation, or use the thumbs up and thumbs down buttons to indicate whether the evaluation was helpful. Your feedback helps improve the quality of future evaluations.

#### Review flagged content
<a name="rcr-content-flags"></a>

Amazon Connect Talent monitors candidate responses during the AI-led interview and surfaces flags when something may need your attention. Flags appear on the candidate list, the candidate results page, and the interview playback page. Select a flag to see a summary of why the candidate was flagged.

Flags don't affect the candidate's competency scores.

There are two types of flags:

##### Content flags
<a name="rcr-content-flags-content"></a>

Content flags identify responses that contain language or content that may require your review. A content flag appears with one of the following labels:


| Flag | What it means | 
| --- | --- | 
| Discriminatory language | The candidate's response contains language that may be discriminatory. | 
| Demeaning language | The candidate's response contains language that may be demeaning toward others. | 
| Inappropriate content | The candidate's response contains content that may be sexually inappropriate. | 
| Violent language | The candidate's response contains language that references or promotes violence. | 
| Criminal references | The candidate's response contains references to criminal activity. | 

##### Fraud detection flags
<a name="rcr-fraud-flags"></a>

Fraud detection flags identify responses that may not be genuinely human-spoken. Amazon Connect Talent analyzes the candidate's responses for indicators of authentic speech — such as natural hesitations, self-corrections, and organically recalled details — and flags interviews where the responses may be AI-generated, scripted, or otherwise non-genuine.

##### What to do when a candidate is flagged
<a name="rcr-content-flags-action"></a>

All flags are informational. Amazon Connect Talent surfaces them for your awareness but does not take action on them. When you see a flag:

1. Review the flagged response in the interview playback to understand the context. Choose the linked question to go directly to the relevant moment in the transcript.

1. Select the flag to read the summary of why the candidate was flagged.

1. Use your judgment and your organization's policies to determine the appropriate next step.

1. Consult your HR or legal team if the flagged content raises concerns that go beyond the hiring decision.

**Important**  
Flags help you identify responses that may need additional review. Amazon Connect Talent does not recommend any specific action based on a flag — the decision on how to proceed is yours.

## Candidates who opted out
<a name="rcr-opted-out"></a>

What you see on the candidate results page depends on how the candidate opted out:
+ **Opted out of the AI-led interview only** – The AI-led interview section shows "Opted out," and the interview competencies show N/A. Any assessments the candidate already completed keep their scores.
+ **Opted out of the entire evaluation** – The score sections are hidden, and a banner shows that the candidate opted out of the evaluation.

Follow up with the candidate using your own process.

## How results sync with your ATS
<a name="rcr-ats"></a>

When a candidate completes their evaluation, Amazon Connect Talent writes a completion event back to your applicant tracking system (ATS). This keeps your ATS up to date without manual steps.

**Note**  
ATS result syncing is available for jobs synced from your ATS. Jobs created directly in Amazon Connect Talent do not sync results to an ATS. For more information about ATS integration, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html).

### What your ATS shows
<a name="rcr-ats-shows"></a>

After a candidate completes their evaluation, their application in your ATS shows:
+ The evaluation status as completed.
+ A link to review the candidate's results in Amazon Connect Talent.

Recruiters can choose this link to go directly to the candidate's results page in Amazon Connect Talent.

### Returning to your ATS
<a name="rcr-ats-return"></a>

The candidate results page in Amazon Connect Talent includes a link back to the candidate's record in your ATS. This lets you review results in Amazon Connect Talent and then return to your ATS to continue your hiring process, without needing to search for the candidate again.