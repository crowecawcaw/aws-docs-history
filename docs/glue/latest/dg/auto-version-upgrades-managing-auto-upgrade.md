

# Managing auto upgrade
<a name="auto-version-upgrades-managing-auto-upgrade"></a>

This section describes how to approve or decline an upgrade, how to disable auto upgrade, and how to upgrade a job after a failed evaluation.

## Approving or declining an upgrade
<a name="auto-version-upgrades-approving-or-declining-an-upgrade"></a>

When the check passes, AWS Glue sends the eligibility summary and asks for your approval. You have 7 days to approve or decline. The job keeps running on its current version until you decide.

### What each choice does
<a name="auto-version-upgrades-what-each-choice-does"></a>


| Choice | Result | 
| --- | --- | 
| Approve | The status changes to `UPGRADING`. The next run executes on the target version. | 
| Decline | The status changes to `STOPPED`. AWS Glue keeps the job on its current version and turns off auto upgrade. | 
| No response | After 7 days, the request expires and the status changes to `STOPPED`. The job stays set to `auto` and keeps running on its current version. Its next run starts a new evaluation. | 

You can repeat the same decision safely. You can't change a decision after AWS Glue records it.

### What to check before you approve
<a name="auto-version-upgrades-what-to-check-before-you-approve"></a>

After you approve, the job's next run uses the target version, with your real inputs and outputs. Upgraded runs are production runs, not test runs.

**Important**  
A failed upgraded run can still write data before it fails, including data with a changed schema. AWS Glue then retries the run on the current version. For targets written in `append` mode, the failed run and the retry can both add records.

Before you approve, check the following:

Write targets and cleanup  
For each write path in the eligibility summary, confirm that the target is overwritten by each run, or that you can remove data from a failed run.

Downstream consumers  
Jobs, crawlers, and dashboards that read the output might see data from a failed run. Confirm that they can handle this, or approve at a time when you can watch the first upgraded run.

Eligibility summary  
Make sure that the analysis is correct and that it lists every important write path. The list includes only paths written during observation, so code paths that didn't run, such as month-end branches, aren't included. For the limits of the check, see [Phase 2: Compatibility check and approval](auto-version-upgrades-how-an-auto-upgrade-evaluation-works.md#auto-version-upgrades-phase-2-compatibility-check-and-approval).

Warnings  
Review configuration and dependency warnings, especially settings that you rely on for performance or correctness.

Alarms  
A failed upgraded run appears in your run history even though AWS Glue retries it. Adjust alarms on failed runs if they would page your team.

### To approve or decline (console)
<a name="auto-version-upgrades-to-approve-or-decline-console"></a>

1. Open the [AWS Glue console](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **ETL jobs**.

1. Choose the job, and then choose the **Upgrade Analysis** tab.

1. Choose **Approve** or **Decline**.

### To approve or decline (AWS CLI)
<a name="auto-version-upgrades-to-approve-or-decline-aws-cli"></a>

Get the analysis ID from the `GetJob` response. For more information, see [Checking a job's auto upgrade status](auto-version-upgrades-monitoring-auto-upgrades.md#auto-version-upgrades-checking-a-jobs-auto-upgrade-status). Then run the following command. Use `--upgrade-consent DECLINE` to decline.

```
aws glue start-job-upgrade-analysis \
  --job-name my-etl-job \
  --analysis-id ja-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d \
  --upgrade-consent APPROVE
```

### To approve or decline (AWS SDK for Python (Boto3))
<a name="auto-version-upgrades-to-approve-or-decline-aws-sdk-for-python-boto3"></a>

```
import boto3

glue = boto3.client("glue", region_name="us-west-2")
glue.start_job_upgrade_analysis(
    JobName="my-etl-job",
    AnalysisId="ja-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    UpgradeConsent="APPROVE",  # or "DECLINE"
)
```

## Disabling auto upgrade
<a name="auto-version-upgrades-disabling-auto-upgrade"></a>

Set `GlueVersion` to a specific version, such as `4.0`. Any evaluation in progress stops, and the job's next run executes on the version you set. You can turn off auto upgrade safely at any phase.

```
aws glue update-job \
  --job-name my-etl-job \
  --job-update '{
    "Role": "arn:aws:iam::111122223333:role/MyGlueJobRole",
    "Command": {"Name": "glueetl", "ScriptLocation": "s3://amzn-s3-demo-bucket/scripts/my-etl-job.py"},
    "GlueVersion": "4.0",
    "MaxRetries": 1
  }'
```

## Upgrading a job after a failed evaluation
<a name="auto-version-upgrades-upgrading-a-job-after-a-failed-evaluation"></a>

When an evaluation fails, AWS Glue sets the job back to its previous version and turns off auto upgrade. Don't just set `GlueVersion` back to `auto`. The job would run on its previous version, where your fixes might not work. Instead, do the following:

1. Fix the issues in the auto upgrade evaluation summary, yourself or with Upgrade with AI. For more information, see [Generative AI upgrades for Apache Spark in AWS Glue](upgrade-analysis.md).

1. Set `GlueVersion` to the target version, and confirm that the job runs successfully.

1. Set `GlueVersion` to `auto`. The job is then ready to be evaluated when the next AWS Glue version is released.