

# How an auto upgrade evaluation works
<a name="auto-version-upgrades-how-an-auto-upgrade-evaluation-works"></a>

This section describes each phase of an auto upgrade.

## Phase 1: Observation
<a name="auto-version-upgrades-phase-1-observation"></a>

Your job keeps running on its current version, as usual. AWS Glue records metadata about each run. This includes write targets, output schema, summary stats, and run metrics. This metadata forms a baseline for later checks.

AWS Glue doesn't access your input or output data. For more information, see [Data handling](auto-version-upgrades-security-for-auto-upgrade.md#auto-version-upgrades-data-handling).

Observation continues until the job has enough successful runs to form a baseline. How long that takes depends on how often the job runs. If runs keep failing on the current version, the evaluation stops. Fix the job so that its runs succeed on its current version. Then set `GlueVersion` to `auto` again.

## Phase 2: Compatibility check and approval
<a name="auto-version-upgrades-phase-2-compatibility-check-and-approval"></a>

AWS Glue checks the job for known breaking changes in the target version. AWS Glue uses the metadata from observation. The check covers 3 areas:
+ **Configuration** – Spark settings and job arguments that the target version removes or changes.
+ **Code** – Changes in Spark, Python, Scala, and their libraries that affect your script.
+ **Dependencies** – Python modules, JAR files, and connectors that don't work on the target version.

What happens next depends on the result:
+ **If AWS Glue finds an issue that blocks the upgrade**, the evaluation ends. AWS Glue doesn't ask for approval. The job stays on its current version. The auto upgrade evaluation summary lists each issue with a suggested fix.
+ **Otherwise**, AWS Glue sends the eligibility summary and asks for your approval. The summary lists any warnings to review. For more information, see [Approving or declining an upgrade](auto-version-upgrades-managing-auto-upgrade.md#auto-version-upgrades-approving-or-declining-an-upgrade).

**Important**  
The compatibility check looks for known Spark migration issues. It also looks for Python and Scala language issues. It can't account for data that the observation runs didn't see. It also has a limited view of non-Spark code and your own libraries. A job that passes the check can still fail or act differently on the target version.

## Phase 3: Upgrade validation
<a name="auto-version-upgrades-phase-3-upgrade-validation"></a>

After you approve, the job runs on the target version. AWS Glue compares each upgraded run with the baseline from observation. The following table shows which differences fail the upgrade and which are warnings.


| Check | What AWS Glue compares | If different | 
| --- | --- | --- | 
| Run outcome | The upgraded run must succeed. | Fails the upgrade | 
| Write operations | The number, type, and order of the job's writes. | Fails the upgrade | 
| Output schema | Column names, data types, and null settings of each write. | Fails the upgrade | 
| Output format | The file format of each write, such as Parquet. | Warning | 
| Row and file counts | Rows and files written by each write. | Warning | 
| Completeness | The share of non-null values in each output column. | Warning | 
| Performance | Read and write speed, and run time. | Warning | 
| Cost | DPU-seconds and estimated cost of the run. | Warning | 

Warnings don't stop the upgrade. Review them in the auto upgrade evaluation summary. A change in row count can mean a real difference in the output. It can also mean that the input data changed between runs.

For jobs upgrading from AWS Glue 2.0, AWS Glue doesn't compare runs with a baseline. The upgraded runs must still succeed.

**Important**  
Validation compares metadata about your output, such as the schema and record counts, not the data values. An upgraded run can pass every check and still write different values. After the upgrade, check the output of the first upgraded runs.

After the required number of upgraded runs succeed and pass the checks, the upgrade completes.

## Phase 4: Completion
<a name="auto-version-upgrades-phase-4-completion"></a>

**When the upgrade succeeds** – From now on, the job runs on the target version. `GlueVersion` stays `auto`. AWS Glue sends the auto upgrade evaluation summary. When a newer version becomes the target, a new evaluation starts on a later run.

**When the upgrade fails** – AWS Glue does the following:
+ Sets the job back to its previous version, such as `4.0`. Auto upgrade is turned off, and later runs use that version.
+ Checks the job's code against the target version.
+ Sends the auto upgrade evaluation summary.

For how to try again, see [Upgrading a job after a failed evaluation](auto-version-upgrades-managing-auto-upgrade.md#auto-version-upgrades-upgrading-a-job-after-a-failed-evaluation).

## Why auto upgrade requires retries
<a name="auto-version-upgrades-why-auto-upgrade-requires-retries"></a>

When an upgraded run fails, AWS Glue retries it on the job's current version. So the run still writes its output. This retry is why auto upgrade needs `MaxRetries` of 1 or higher. The retry counts against the job's normal retry limit.

An upgraded run can fail in 2 ways. It can fail while it runs, or it can finish but fail the data validation checks. In both cases, AWS Glue marks the run `FAILED` and retries it on the current version. A run that fails the data validation checks shows the following message.

```
Auto upgrade output data validation failed, rolling back to previous version
```

## New jobs created with auto upgrade
<a name="auto-version-upgrades-new-jobs-created-with-auto-upgrade"></a>

A new job created with `GlueVersion` set to `auto` has no baseline and no version change to approve. AWS Glue skips observation, the compatibility check, and approval. It runs the job on the target version.

AWS Glue watches the job's first run. If that run succeeds, the evaluation is complete and the job stays on auto upgrade. If it fails, AWS Glue sets the job to the default AWS Glue version for new jobs. In both cases, AWS Glue sends the auto upgrade evaluation summary. The summary lists any issues and possible fixes.

When you update an existing job to `auto`, the evaluation moves through all 4 phases.

## Summary reports
<a name="auto-version-upgrades-summary-reports"></a>

AWS Glue sends you 2 summary reports during an evaluation. For how to download them, see [Downloading the summary reports](auto-version-upgrades-monitoring-auto-upgrades.md#auto-version-upgrades-downloading-the-summary-reports).

### Eligibility summary
<a name="auto-version-upgrades-eligibility-summary"></a>

AWS Glue sends the eligibility summary at the end of phase 2, when it requests your approval. The summary has the following sections.


| Section | What it tells you | 
| --- | --- | 
| Compatibility summary | Pass or fail for configuration, application code, and dependencies | 
| Warnings | Configuration and dependency warnings | 
| Write paths | Each path and table the job wrote to, with the write mode and format | 
| Approve or decline | Instructions for the console, AWS CLI, and SDK | 

The eligibility summary also shows the date and time that the approval request expires.

### Auto upgrade evaluation summary
<a name="auto-version-upgrades-auto-upgrade-evaluation-summary"></a>

AWS Glue sends the auto upgrade evaluation summary when the evaluation ends. If the upgrade succeeds, it shows the output data checks. If the evaluation fails, it lists the required changes. It also includes the compatibility check results, suggested fixes, and next steps.

The upgrade validation section of the auto upgrade evaluation summary has 3 parts:
+ A summary with pass, warn, or fail for correctness, performance, and cost
+ A table of checks with the expected range and each upgraded run's value
+ An appendix with job run IDs and detail for each operation and column