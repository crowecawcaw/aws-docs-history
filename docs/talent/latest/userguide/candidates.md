

# Candidates
<a name="candidates"></a>

The job candidates page shows all candidates for a specific job and their evaluation results. To open it, navigate to **Jobs** and choose a job.

**Note**  
ATS integrations are not available at launch. Support for ATS integrations is coming soon. For more information, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html) in the *Amazon Connect Talent Administrator Guide*.

**Topics**
+ [How candidate records are created](#candidates-record-created)
+ [The job candidates page](#candidates-page)
+ [Candidates who opted out](#candidates-opted-out)
+ [Review candidate results](review-candidate-results.md)
+ [Candidate experience](candidate-experience.md)

## How candidate records are created
<a name="candidates-record-created"></a>

Amazon Connect Talent creates a candidate record in two ways:
+ **From your ATS** – When a candidate application is created in your applicant tracking system for a job linked to an evaluation, Amazon Connect Talent automatically creates a candidate record.
+ **From a manual send** – When you manually send an evaluation to a candidate by email, Amazon Connect Talent checks whether a candidate record already exists for that email address and role. If one exists, the evaluation is sent to the existing candidate. If one doesn't exist, Amazon Connect Talent creates a new candidate record. Manually created candidate records are not synced back to your ATS.

Candidates appear on the job candidates page as soon as their record is created — you don't need to wait for them to complete the evaluation. Scores populate after the candidate completes their evaluation.

## The job candidates page
<a name="candidates-page"></a>

The job candidates page shows all candidates for a job.

### Candidate metrics
<a name="candidate-metrics"></a>

At the top of the page, the **Metrics** section shows the following candidate metrics:
+ **Evaluations sent** – Each evaluation sent counts once, including retakes.
+ **Evaluations completed** – Evaluations where the candidate finished every part. Opting out of one part still counts as completed.
+ **Evaluation completion rate** – Completed divided by sent, excluding full opt-outs.

The total candidate count appears at the top of the candidate list (for example, "Candidates (9)"). This is the number of candidate applications for a given job. If a candidate has multiple evaluations for the same job, they are only counted once. Candidates who opted out of their evaluation are included in this count.

### Candidate list
<a name="candidates-list"></a>

Below the metrics, the **Candidates** section lists all candidates with a total count (for example, "Candidates (9)"). Each candidate in the list shows the following:
+ **Candidate ID** – A unique identifier assigned by Amazon Connect Talent, shown as a clickable link. Choose the ID to open the candidate results page.
+ **Evaluation status** – The current status of the candidate's evaluation. Possible statuses include:
  + **Scheduled** – The evaluation invitation has been sent to the candidate, but the candidate hasn't started yet.
  + **In progress** – The candidate has started the evaluation but hasn't completed it yet.
  + **Score pending** – The candidate has completed the evaluation and Amazon Connect Talent is scoring the results. Scoring can take up to two hours. Once scoring finishes, the status changes to **Completed** and scores become available.
  + **Completed** – The candidate has completed their evaluation and the score is available.
  + **Opted out** – The candidate chose not to complete the evaluation. For more information, see [Candidates who opted out](#candidates-opted-out).
+ **Evaluation completed** – The date the candidate completed their evaluation.
+ **Evaluation** – The name of the evaluation the candidate was sent.
+ **Application status** – The candidate's current application status (**Active**, **Hired**, or **Rejected**). Amazon Connect Talent gets this status from your applicant tracking system.

Each candidate also shows scores for the parts of the evaluation that apply to them:
+ **Problem solving score** – The candidate's Problem solving assessment score, if the evaluation includes a Problem solving assessment.
+ **Work approach score** – The candidate's Work approach assessment score, if the evaluation includes a Work approach assessment.
+ **Interview score** – The candidate's overall AI-led interview score, if the evaluation includes an AI-led interview.

Scores appear only for the components included in the candidate's evaluation. For example, if an evaluation includes an AI-led interview and a Work approach assessment but no Problem solving assessment, only the interview score and Work approach score appear.

#### Candidates with multiple evaluations
<a name="candidates-multiple-evaluations"></a>

A candidate can have more than one evaluation for a job. This happens when:
+ The candidate was sent separate evaluations for the same role — for example, a first-round evaluation and a second-round evaluation.
+ The candidate's evaluation was resent — for example, because of a technical difficulty that required them to retake the evaluation.

When a candidate has multiple evaluations, each evaluation appears as a separate row in the candidate list with its own scores, evaluation status, and completion date. Evaluations are listed in order of completion date, with the most recently completed evaluation at the top.

### Search and filter candidates
<a name="candidates-search-filter"></a>

You can narrow the candidate list using the following controls:
+ **Search** – Search by candidate ID.
+ **Sort by** – Sort the list by interview score or other criteria.
+ **Filters** – Filter candidates by evaluation status, evaluation name, interview score, assessment score, or application status.

The page shows the number of matching candidates (for example, "9 Matching") and supports pagination.

### Change application status
<a name="candidates-change-status"></a>

To update a candidate's application status, select one or more candidates using the checkboxes and choose **Change status**.

**Note**  
Changing a candidate's application status in Amazon Connect Talent does not update the status in your applicant tracking system and does not notify the candidate.

## Candidates who opted out
<a name="candidates-opted-out"></a>

A candidate can choose not to complete the evaluation. There are two ways a candidate can opt out:
+ **Opt out of the entire evaluation** – The candidate declines the whole evaluation, including all assessments and the AI-led interview.
+ **Opt out of the AI-led interview only** – The candidate declines the AI-led interview but completes their assessments.

When a candidate opts out, Amazon Connect Talent shows the status "Opted out" in place of a score. The candidate's application status stays Active, so the candidate remains in your pipeline and you can follow up.

To find candidates who opted out, filter the candidate list. Set **Evaluation status** to **Opted out** or set **Interview score** to **Opted out**.

For more information about the candidate's experience when opting out, see [How a candidate opts out](candidate-experience.md#candidate-experience-opt-out). For more information about what you see on the candidate results page for an opted-out candidate, see [Review candidate results](review-candidate-results.md).