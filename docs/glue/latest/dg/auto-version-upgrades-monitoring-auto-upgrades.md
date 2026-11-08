

# Monitoring auto upgrades
<a name="auto-version-upgrades-monitoring-auto-upgrades"></a>

You can follow an auto upgrade with the job, its job runs, the evaluation record, the summaries, and Amazon EventBridge events.

## Checking a job's auto upgrade status
<a name="auto-version-upgrades-checking-a-jobs-auto-upgrade-status"></a>

While the job is set to `auto`, `GetJob` returns `AutoUpgradeMetadata`. It shows the source version, the target version, the evaluation status, and the analysis ID. Use the analysis ID to approve or decline an upgrade and to get the summaries.

```
aws glue get-job \
  --job-name my-etl-job \
  --query 'Job.AutoUpgradeMetadata'
```

## Checking which version a run used
<a name="auto-version-upgrades-checking-which-version-a-run-used"></a>

`GlueVersion` in the `GetJobRun` response shows the version that a run actually used, such as `4.0`. It never shows `auto`. Use it to tell apart runs on the current version, upgraded runs, and retries.

```
aws glue get-job-run \
  --job-name my-etl-job \
  --run-id jr_0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef \
  --query 'JobRun.{Version:GlueVersion,State:JobRunState,Attempt:Attempt}'
```

## Getting evaluation details
<a name="auto-version-upgrades-getting-evaluation-details"></a>

`GetJobUpgradeAnalysis` returns the current status in `Status`.


| Status | Meaning | Runs execute on | 
| --- | --- | --- | 
| `OBSERVING` | Observation or the compatibility check is in progress | Current version | 
| `WAITING_FOR_CONSENT` | Waiting for you to approve or decline | Current version | 
| `UPGRADING` | Upgrade validation is in progress | Target version | 
| `SUCCEEDED` | The job now runs on the target version | Target version | 
| `FAILED` | The upgrade failed, and AWS Glue set the job back to its previous version | Previous version | 
| `STOPPED` | You declined, the request expired, you turned off auto upgrade, or you deleted the job | Current version | 

The following command gets an evaluation.

```
aws glue get-job-upgrade-analysis \
  --job-name my-etl-job \
  --analysis-id ja-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
```

To find the evaluations for a job, run the following command.

```
aws glue list-job-upgrade-analyses \
  --job-name my-etl-job \
  --filter '{"AnalysisType": "AUTO_UPGRADE"}'
```

## Downloading the summary reports
<a name="auto-version-upgrades-downloading-the-summary-reports"></a>

For what each report contains, see [Summary reports](auto-version-upgrades-how-an-auto-upgrade-evaluation-works.md#auto-version-upgrades-summary-reports). To download the reports, do one of the following:
+ **Console** – Choose the job, and then choose the **Upgrade Analysis** tab.
+ **AWS CLI** – Run the following command. The `AutoUpgradeEligibilitySummary` and `AutoUpgradeEvaluationSummary` fields hold download URLs. The URLs are valid for 1 hour. To get new ones, run the command again.

```
aws glue get-job-upgrade-analysis \
  --job-name my-etl-job \
  --analysis-id ja-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d \
  --query '{Eligibility:AutoUpgradeEligibilitySummary,Evaluation:AutoUpgradeEvaluationSummary}'
```

## Amazon EventBridge events
<a name="auto-version-upgrades-amazon-eventbridge-events"></a>

AWS Glue sends an event at each step of an auto upgrade. You can use these events to get notified, for example when an upgrade needs your approval. AWS Glue sends the events to the default event bus in your account. All events use the source `aws.glue-autoversion`. The detail type is `Auto Version Job State Change`. The `resources` field lists the job ARN. Delivery is best effort. Use `GetJobUpgradeAnalysis` as the source of truth.


| `detail.state` | Sent when | Additional fields | 
| --- | --- | --- | 
| `EVALUATION_STARTED` | An evaluation begins | `currentVersion`, `targetVersion`, `analysisId`, `entrypoint` (`OBSERVATION` or `DIRECT_UPGRADE`) | 
| `CONSENT_REQUIRED` | The eligibility summary is ready | `currentVersion`, `targetVersion`, `analysisId`, `consentDeadline` (epoch seconds) | 
| `CONSENT_EXPIRED` | No decision within 7 days | `currentVersion`, `targetVersion`, `analysisId` | 
| `POST_OBSERVING_FAILED` | The compatibility check blocked the upgrade after observation | `currentVersion`, `targetVersion`, `analysisId`, `failureReason` | 
| `UPGRADE_RUN_SUCCEEDED` | An upgraded run passed validation | `currentVersion`, `targetVersion`, `analysisId`, `jobRunId`, `upgradeProgress` (upgraded runs that passed, out of the number needed) | 
| `UPGRADE_RUN_FAILED` | An upgraded run failed or failed validation | `currentVersion`, `targetVersion`, `analysisId`, `jobRunId`, `failureReason` | 
| `UPGRADE_COMPLETED` | The upgrade succeeded | `currentVersion` (previous), `newVersion`, `analysisId`, `outcome` (`GRADUATED`) | 
| `UPGRADE_FAILED` | The upgrade failed and the job was set back to its previous version | `currentVersion`, `attemptedVersion`, `rollbackVersion`, `analysisId`, `outcome` (`FAILED`), `failureReason` | 
| `UPGRADE_STOPPED` | You turned off auto upgrade or deleted the job | `currentVersion`, `targetVersion`, `analysisId`, `stoppedReason` | 

The following event pattern matches approval requests. You can use it in a rule that sends them to an Amazon SNS topic.

```
{
  "source": ["aws.glue-autoversion"],
  "detail-type": ["Auto Version Job State Change"],
  "detail": { "state": ["CONSENT_REQUIRED"] }
}
```