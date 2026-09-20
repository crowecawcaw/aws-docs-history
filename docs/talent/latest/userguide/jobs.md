

# Jobs
<a name="jobs"></a>

In Amazon Connect Talent, a job is a role you're hiring for. Each job has a title and description. You can create jobs directly in Amazon Connect Talent or connect them from an applicant tracking system (ATS). You then use those jobs to create evaluations. An evaluation defines the AI-led interviews and assessments that candidates complete as part of your hiring process.

**Note**  
ATS integrations are not available at launch. Support for ATS integrations is coming soon. For more information, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html) in the *Amazon Connect Talent Administrator Guide*.

**Topics**
+ [How jobs are used](#jobs-usage)
+ [Add a job](#jobs-create)
+ [View active jobs](#jobs-manage)
+ [View candidates for a job](#jobs-candidates)

## How jobs are used
<a name="jobs-usage"></a>

Jobs serve several purposes in Amazon Connect Talent:
+ **Competency selection** – When you create an evaluation, Amazon Connect Talent analyzes the job description and identifies key competencies for the role. These competencies drive which assessments are selected and which behavioral questions are generated for the AI-led interview. To learn more, see [Create an evaluation](managing-evaluations.md#create-candidate-evaluation).
+ **Candidate-facing job summary** – Amazon Connect Talent uses the job description to generate a summary that candidates see before they begin their evaluation. This summary is presented to the candidate along with the full job description, giving them context about the role they're being evaluated for. To learn more, see [Candidate experience](candidate-experience.md).
+ **Candidate applications** – For jobs synced from your ATS, Amazon Connect Talent pulls in the candidate applications associated with each job. When a candidate completes their evaluation, Amazon Connect Talent writes a completion event back to your ATS. The completion event appears on the candidate's application in your ATS and includes a link for the recruiter to review the candidate's results in Amazon Connect Talent. To learn more, see [Review candidate results](review-candidate-results.md).
+ **Application stages** – Amazon Connect Talent also syncs the application stages associated with each job from your ATS. Application stages are used to trigger sending evaluation invitations to candidates. To learn more, see [Sending evaluations to candidates](evaluations-send.md).

## Add a job
<a name="jobs-create"></a>

There are two ways to add a job to Amazon Connect Talent:
+ **Sync jobs from ATS** – When you add an ATS integration, Amazon Connect Talent automatically syncs active jobs from your ATS. For synced jobs, Amazon Connect Talent also pulls in the application stages associated with each job. Application stages are used to trigger sending evaluation invitations to candidates. To learn more, see [Sending evaluations to candidates](evaluations-send.md).
+ **Add a job manually** – Choose **Evaluations**, and then choose **Create evaluation**. In the evaluation creation flow, you can upload or describe your job. Manually created jobs are best suited for internal testing of evaluations. To learn more, see [How to test Amazon Connect Talent](getting-started-test.md).

In the first step of the evaluation creation workflow, you can search for synced jobs or jobs you created manually.

**Note**  
When you add your ATS integration, only jobs created in your ATS after the integration is established are synced into Amazon Connect Talent. Jobs that existed before the integration aren't synced.

**Important**  
You can't link a manually created job to an existing job in your ATS. Because of this, candidate applications from your ATS don't flow into manually created jobs. To evaluate candidates for a manually created job, you must send evaluation invitations manually, which creates new candidate records in Amazon Connect Talent. These records don't sync back to your ATS.

## View active jobs
<a name="jobs-manage"></a>

To view your jobs, choose the **Jobs** icon in the side navigation. The Jobs page lists your jobs in a searchable, sortable, paginated table. Tabs group the jobs:
+ **All** – Every job.
+ **Linked to candidate evaluations** – Jobs linked to an evaluation.
+ **Synced from ATS** – Jobs that come from a connected applicant tracking system.
+ **Uploaded** – Jobs created directly in Amazon Connect Talent.

## View candidates for a job
<a name="jobs-candidates"></a>

Choose a job to open the job candidates page, which shows all candidates for that role and their evaluation results. For more information, see [Candidates](candidates.md).