

# Troubleshooting auto upgrade
<a name="auto-version-upgrades-troubleshooting-auto-upgrade"></a>

To find why an evaluation failed, read the auto upgrade evaluation summary. You can also read `ErrorMessage` in the `GetJobUpgradeAnalysis` response. Or read `failureReason` in the event. To fix a job and upgrade it, see [Upgrading a job after a failed evaluation](auto-version-upgrades-managing-auto-upgrade.md#auto-version-upgrades-upgrading-a-job-after-a-failed-evaluation).


| Failure reason | What it means | What to do | 
| --- | --- | --- | 
| `Pre-upgrade eligibility check failed: breaking changes detected` | The check found a change that breaks the job. | Fix the issues. | 
| `The upgrade was blocked by HIGH-confidence Spark migration findings in the job script.` | The check found code that will break. | Fix the issues. | 
| `dependency change(s) required` | A library or JAR must change. | Fix the issues. | 
| `The job execution role cannot use the KMS key in --auto-upgrade-metadata-kms-key-arn...` | The job role can't use your key. | Grant the role `kms:GenerateDataKey` and `kms:Decrypt`. | 
| `Auto upgrade validation could not be completed because one or more observation runs failed at runtime.` | The job failed on its current version. | Fix the job so that it runs on its current version. Then set `GlueVersion` to `auto` again. | 
| `Auto upgrade validation encountered an error on an observation run (<run-id>). <details>` | The job role can't access something the check needs. Or another error will likely repeat. | Fix the cause in the details. For access errors, see [Permissions for the job role](auto-version-upgrades-iam-permissions-for-auto-upgrade.md#auto-version-upgrades-permissions-for-the-job-role). | 
| `Upgraded run failed: <error>` | The job failed on the target version. | Fix the issues. | 
| `Auto upgrade validation failed. Data mismatch detected in upgraded run(s).` | The writes or schema didn't match the baseline. | Find the changed writes or columns in the summary appendix. Fix the issues. | 
| `Upgrade consent was declined.` | You declined the upgrade. | No action needed. To try again, set `GlueVersion` to `auto`. | 
| `[Action required: Unable to update job version: <details>]` | AWS Glue couldn't set the job back to its old version. | Set `GlueVersion` to that version yourself. | 
| `An active upgrade-with-ai analysis (analysisId=<analysis-id>) already exists for this job. Cannot enroll in auto upgrade.` | Upgrade with AI is running on the job. | Wait for it to finish or stop it. | 
| `Assessment encountered an internal error.` | AWS Glue couldn't finish the check. | To retry, set `GlueVersion` to `auto` again. If it fails again, contact AWS Support. | 

## Related topics
<a name="auto-version-upgrades-related-topics"></a>
+ [Generative AI upgrades for Apache Spark in AWS Glue](upgrade-analysis.md)
+ [Migrating AWS Glue for Spark jobs to AWS Glue version 6.0](migrating-version-60.md)
+ [Migrating AWS Glue for Spark jobs to AWS Glue version 5.1](migrating-version-51.md)
+ [Configuring job properties for Spark jobs in AWS Glue](add-job.md) (job run queuing)
+ [AWS Glue pricing](https://aws.amazon.com/glue/pricing/)