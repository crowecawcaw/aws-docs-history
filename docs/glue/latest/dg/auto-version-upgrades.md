

# Automatic version upgrades for AWS Glue jobs
<a name="auto-version-upgrades"></a>

AWS Glue automatic version upgrades (auto upgrade) keep your AWS Glue for Apache Spark jobs on the latest stable AWS Glue version. Your jobs get new features, faster runs, and security fixes. You don't need a migration project.

To turn on auto upgrade, set the job's `GlueVersion` parameter to `auto`. AWS Glue observes the job's existing runs and analyzes the job script, configuration, and dependencies for compatibility with the latest stable version. AWS Glue doesn't modify your script or job settings.

If the job requires code or configuration changes, AWS Glue doesn't upgrade the job. Instead, the auto upgrade evaluation summary lists the required changes. If the job requires no changes, AWS Glue sends you an eligibility summary with the compatibility results and requests your approval to upgrade. After you approve, subsequent job runs use the latest stable version. If an upgraded job run fails, AWS Glue retries the run on the previous version and reverts the job to that version.

## How auto upgrade works
<a name="auto-version-upgrades-how-auto-upgrade-works"></a>

For an existing job, auto upgrade has 4 phases.

![Flow of an auto upgrade: observation, compatibility check and approval, upgrade validation, and completion. If a blocking issue is found, you decline, or an upgraded run fails, the job goes back to its previous version.](https://docs.aws.amazon.com/glue/latest/dg/images/auto-version-upgrades-flow.png)



| Phase | What AWS Glue does | What you do | 
| --- | --- | --- | 
| 1. Observation | The job runs on its current version. AWS Glue records a baseline from these runs. | No action required. | 
| 2. Compatibility check and approval | AWS Glue checks the job for known breaking changes. If none are found, you get an eligibility summary. | Review the summary. Approve or decline within 7 days. | 
| 3. Upgrade validation | The next job runs use the latest stable version. AWS Glue compares each run with the baseline. | Monitor the upgraded runs. | 
| 4. Completion | The job stays on the latest stable version. If a run failed, the job is back on its previous version. | Review the auto upgrade evaluation summary. | 

If you create a new job with `GlueVersion` set to `auto`, the job skips these phases. It runs on the latest stable version from the start.

Auto upgrade doesn't start extra job runs. There's no extra charge for auto upgrade. Each job run is billed at the normal rate.

## Before you start
<a name="auto-version-upgrades-before-you-start"></a>

Auto upgrade supports jobs that meet the following requirements:
+ The job is a Spark ETL job (`glueetl`) on AWS Glue 2.0 or later. Streaming, Python shell, and Ray jobs aren't supported.
+ The job's `MaxRetries` parameter is set to 1 or higher. Job run queuing is turned off. If an upgraded run fails, AWS Glue uses the retry to run it on the previous version.
+ The job is safe to retry. If a run fails partway, you have a way to make sure that the retry doesn't duplicate or corrupt the output, or to clean up any partial output. For example, the job overwrites its output on a retry.

## Get started
<a name="auto-version-upgrades-get-started"></a>

**To create a new job with auto upgrade**

1. Confirm that the job is safe to retry.

1. Create the job with the `GlueVersion` parameter set to `auto` and `MaxRetries` set to 1 or higher.

**To upgrade an existing job**

1. Confirm that the job is safe to retry and has `MaxRetries` set to 1 or higher.

1. Set the job's `GlueVersion` parameter to `auto`.

1. Keep running the job as usual.

1. When you get the eligibility summary, review it. Then approve the upgrade.

1. Monitor the upgraded runs. When the evaluation ends, review the auto upgrade evaluation summary.

**To assess and auto upgrade multiple jobs with an AI agent**

1. Install the [managing-glue-jobs skill](https://github.com/aws-samples/aws-glue-samples/blob/8d52b2c004d48b4d15c20cb1b0bd161da0c98a0d/utilities/skills/managing-glue-jobs/README.md) from the AWS Glue samples repository on the GitHub website.

1. To assess your jobs, enter a prompt such as the following. This step is read-only.

   ```
   Assess my Glue jobs in us-west-2 for auto upgrade. Use AWS profile my-profile.
   ```

1. To turn on auto upgrade and set up email notifications, enter a prompt such as the following.

   ```
   Proceed with the eligible jobs, and set up auto upgrade email notifications to data-team@example.com.
   ```

   This step sets `GlueVersion` to `auto` and creates the email resources. Your jobs keep running on their current version.

1. When you get an approval request, review it with the agent. Then approve it. For example:

   ```
   Which of my Glue jobs in us-west-2 are waiting for upgrade approval?
   ```

   ```
   Approve the upgrade for my-etl-job.
   ```
**Important**  
Approval is the only step that moves a job to the latest stable version. Before you approve, review the eligibility summary, and confirm that the job is safe to retry.

The agent asks you before it makes any change.

For console steps and sample AWS CLI commands, see [Turning on auto upgrade with the console or AWS CLI](auto-version-upgrades-turning-on-auto-upgrade-with-the-console-or-aws-cli.md). If you get an access error, see [IAM permissions for auto upgrade](auto-version-upgrades-iam-permissions-for-auto-upgrade.md).

## Considerations and limitations
<a name="auto-version-upgrades-considerations-and-limitations"></a>
+ **Regions** – Auto upgrade is available in the following AWS Regions:
  + US East (Ohio)
  + US West (Oregon)
  + Canada (Central)
  + South America (São Paulo)
  + Europe (Frankfurt)
  + Europe (Ireland)
  + Asia Pacific (Mumbai)
  + Asia Pacific (Singapore)
  + Asia Pacific (Tokyo)
+ **One evaluation at a time** – A job can have one evaluation at a time. A job that runs Upgrade with AI can't use auto upgrade.
+ **Jobs that run rarely** – Auto upgrade uses the job's own runs. So these jobs take longer.
+ **Changes during an evaluation** – Avoid changing the job's script or output during an evaluation. A change can make the baseline out of date, and the evaluation can then fail.