

# Pause and resume a penetration test run

A penetration test run can take many hours. Pause a run to stop AWS Security Agent without losing its work, then resume the run later to continue from where it left off. A resumed run keeps the findings from its earlier attempts and continues from the testing it already did, instead of starting over.

Resume a run in any of these situations:
+ You paused the run.
+ The run failed for one of these reasons, and you corrected the problem:
  + AWS Security Agent couldn’t sign in to your application.
  + AWS Security Agent couldn’t reach an endpoint.
  + AWS Security Agent couldn’t use an AWS Identity and Access Management (IAM) role.
+ The run reached its maximum task hours, and you want to raise the limit and continue.

You can’t pause or resume a run that your continuous integration and continuous delivery (CI/CD) pipeline started. Your pipeline starts a new run for each change. For more information, see [Run penetration tests from your CI/CD pipeline](cicd-pentest.md).

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ Access to the AWS Security Agent web application
+ A penetration test run that is in progress, paused, or failed for one of the reasons listed above

## Pause a run
<a name="_pause_a_run"></a>

To pause a run that is in progress and keep its work:

1. Log in to the AWS Security Agent web application.

1. Open the penetration test run that you want to pause.

1. Choose **Pause run**.

A run’s status reports its progress through the pause:
+  **Pausing** – AWS Security Agent is saving the run’s progress.
+  **Paused** – AWS Security Agent saved the run’s progress and isn’t testing. You can resume the run.

A paused run keeps its findings, and you can review them and generate a report without resuming the run.

**Note**  
 **Pause run** is available after preflight checks finish. During preflight, AWS Security Agent is still setting up the run and has no testing progress to save.

## Resume a run
<a name="_resume_a_run"></a>

AWS Security Agent can resume a run when all of the following are true:
+ You created the run within the last 7 days. The 7 days count from when you created the run, not from when it paused.
+ The run paused, or failed for one of the reasons listed at the start of this topic.
+ The run saved its progress before it ended.
+ You have room in your quota for concurrent penetration test runs. A resumed run counts toward that quota, the same as a run you start. For more information, see [Service Quotas](quotas.md).

You don’t need to check these conditions yourself. AWS Security Agent offers **Resume run** only on a run whose status allows it. If a run saved no progress, it tells you why it can’t resume when you try.

You can’t resume a run that you stopped with **Stop run**. You also can’t resume a run that finished normally or a run that stopped because of an internal error. Create and run a new penetration test instead.

**Important**  
To keep a run’s progress so that you can continue it later, choose **Pause run** rather than **Stop run**. Only a paused run, or a run that failed for one of the reasons listed at the start of this topic, saves the progress a resumed run needs.

**Note**  
Both a run that finished normally and a run that reached its maximum task hours report a status of **Complete**. To tell them apart, open the run. A run that reached its limit shows a **Completed at task-hours budget** message.  
To resume a run that reached its maximum task hours, choose **Resume with overrides** and raise **Max task hours**. **Resume run** reuses the limit that the run already reached.

You can resume a run in three ways. All three continue the run from where it left off and keep its findings. They differ in which configuration the resumed run uses. In the **Penetration test runs** list, choosing **Resume run** opens the run without resuming it, so you always pick the mode from the run itself.

To resume a run:

1. Log in to the AWS Security Agent web application.

1. Open the penetration test run that you want to resume.

1. Choose one of the following:
   +  **Resume run** – Continues the run with the configuration it used before it paused or stopped.
   +  **Resume with pentest configuration** – Continues the run with the penetration test’s current configuration. Choose this after you change the penetration test itself, such as updating its credentials.
   +  **Resume with overrides** – Opens a page where you change the configuration before you resume. For more information, see [Resume a run with overrides](#resume-with-overrides).

The run status changes to **In progress**, and its **Version** increases by one. **Version** appears on the **Run overview** tab and counts the times you resumed the run. The run keeps the same run ID, so its findings, endpoints, task hours, and reports stay together under that one run.

## Resume a run with overrides
<a name="resume-with-overrides"></a>

Use **Resume with overrides** to change a run’s configuration before you continue it. The page opens with the configuration the run used before it paused or stopped, so you can see and change what the resumed run uses.

You can’t change a run’s test scope when you resume it, so the page doesn’t show the run’s target endpoints, repositories, or documents. To test a different scope, create a new penetration test.

You can change:
+  **Credentials** – Add or change the credentials the resumed run uses to sign in to your application.
+  **Network scope** – Change which URLs the run can and can’t reach, and the custom HTTP headers it sends.
+  **VPC configuration** – Change the virtual private cloud (VPC), subnets, and security groups the run uses.
+  **Max task hours** – Raise the limit for the resumed run, or choose **No limit** to remove it. A new limit must be at least 2 hours more than the task hours the run has already used.

**Clearing a field removes that setting from the resumed run**  
The page shows the whole configuration that the resumed run uses, not only the parts you change. If you clear a field, the resumed run runs without that setting. For example, if you remove every credential, the resumed run doesn’t sign in to your application.

After you make your changes, choose **Resume run**.

## Next steps
<a name="_next_steps"></a>

After you resume a run, consider these next steps:
+ Review the findings as the run continues to discover them. For more information, see [Review findings from a penetration test](review-penetration-findings.md).
+ To retest specific findings without resuming a run, see [Revalidate penetration test findings](revalidate-findings.md).
+ If a resumed run stops again for the same reason, see [Troubleshooting](troubleshooting.md).