

# Batch runs in HealthOmics
<a name="workflows-batch"></a>

AWS HealthOmics batch runs let you submit multiple runs in a single API request. Each run in the batch shares a common base configuration but can have different inputs and run-specific parameters. Batch runs reduce submission overhead and simplify lifecycle management for large-scale workflow processing.

With batch runs, you can:
+ Submit up to 100,000 runs in a single **StartRunBatch** call, with a shared configuration defined once and applied across all runs.
+ Apply per-run parameter overrides for individual samples, including name, output URI, parameters, priority, and tags.
+ Track overall batch status and individual run submission progress through **GetBatch** and **ListRunsInBatch**.
+ Cancel all runs in a batch using **CancelRunBatch**.
+ Delete all runs in a batch using **DeleteRunBatch**.
+ Delete batch metadata with **DeleteBatch**.

**Topics**
+ [Batch run concepts](#batch-concepts)
+ [Prerequisites](#batch-prerequisites)
+ [IAM permissions for batch operations](#batch-iam-permissions)
+ [Getting started: Submit your first batch](#batch-getting-started)
+ [Starting a batch run](#batch-starting)
+ [Monitoring batch progress](#batch-monitoring)
+ [Handling failed runs](#batch-handling-failures)
+ [Canceling a batch](#batch-canceling)
+ [Deleting batch runs](#batch-deleting-runs)
+ [Deleting batch metadata](#batch-deleting-metadata)
+ [EventBridge events for batches](#batch-eventbridge)
+ [Limitations and considerations](#batch-limitations)

## Batch run concepts
<a name="batch-concepts"></a>
+ **Batch** — A collection of workflow runs that share common configuration, managed as a single resource with its own Amazon Resource Name (ARN) and lifecycle status.
+ **Default run setting** (`defaultRunSetting`) — Workflow parameters shared across all runs in the batch, such as workflow ID, IAM role, output URI, and common parameters.
+ **Run-specific setting** (`inlineSettings` or `s3UriSettings`) — Per-run configurations that override or merge with the default run setting. Each entry must include a unique `runSettingId`.
+ **Run setting ID** (`runSettingId`) — A required, customer-provided unique identifier for each run configuration within a batch. After submission, use **ListRunsInBatch** to map each `runSettingId` to the HealthOmics-generated `runId`, allowing you to trace which run was created from which input configuration.
+ **Batch status** — The overall state of the batch operation. Possible values:
  + `CREATING` — Batch is being created.
  + `PENDING` — Batch has been created; run configurations are being validated asynchronously.
  + `SUBMITTING` — Validation complete; individual runs are being submitted.
  + `INPROGRESS` — All run submissions have been attempted; runs are executing.
  + `STOPPING` — A cancel request has been received; runs are being stopped.
  + `CANCELLED` — The batch was cancelled.
  + `PROCESSED` — All runs have reached a terminal state (completed, failed, or cancelled).
  + `FAILED` — The batch itself failed before runs could be created. See [Batch-level failures](#batch-level-failures) for details.
  + `RUNS_DELETING` — Runs in the batch are being deleted.
  + `RUNS_DELETE_FAILED` — Some or all runs in the batch failed to delete.
  + `RUNS_DELETED` — All runs in the batch have been deleted.
+ **Submission status** — The submission outcome for an individual run within the batch. Possible values:
  + `SUCCESS` — Run was successfully submitted.
  + `FAILED` — Run submission failed (for example, due to a validation error).
  + `CANCEL_SUCCESS` — Run was successfully cancelled.
  + `CANCEL_FAILED` — Run cancellation failed.
  + `DELETE_SUCCESS` — Run was successfully deleted.
  + `DELETE_FAILED` — Run deletion failed.

## Prerequisites
<a name="batch-prerequisites"></a>

Before starting a batch run, ensure you have:
+ An active HealthOmics private workflow. Batch runs are not supported with Ready2Run workflows.
+ An IAM service role with permissions to run HealthOmics workflows and access your Amazon S3 buckets. For details, see [Service roles for AWS HealthOmics](permissions-service.md).
+ Amazon S3 locations for input data and output results.
+ Run-specific parameters for each sample or experimental configuration.

## IAM permissions for batch operations
<a name="batch-iam-permissions"></a>

Your IAM identity must have permissions for both the batch operation and the underlying individual run operation. The following example policy grants permissions for all batch operations:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowBatchOperations",
      "Effect": "Allow",
      "Action": [
        "omics:StartRunBatch",
        "omics:GetBatch",
        "omics:ListBatch",
        "omics:ListRunsInBatch",
        "omics:CancelRunBatch",
        "omics:DeleteRunBatch",
        "omics:DeleteBatch"
      ],
      "Resource": "arn:aws:omics:*:{{123456789012}}:runBatch/*"
    },
    {
      "Sid": "AllowRunCreation",
      "Effect": "Allow",
      "Action": "omics:StartRun",
      "Resource": [
        "arn:aws:omics:*:{{123456789012}}:run/*",
        "arn:aws:omics:*:{{123456789012}}:workflow/*",
        "arn:aws:omics:*:{{123456789012}}:runGroup/*"
      ]
    },
    {
      "Sid": "AllowListOperations",
      "Effect": "Allow",
      "Action": [
        "omics:ListBatch",
        "omics:ListRunsInBatch"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowPassRole",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::{{123456789012}}:role/{{OmicsRole}}",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "omics.amazonaws.com"
        }
      }
    }
  ]
}
```

**Note**  
**StartRunBatch** requires dual authorization: `omics:StartRunBatch` on the batch resource and `omics:StartRun` on the run, workflow, and run group resources. Both permissions must be granted for the batch to succeed.

The IAM service role passed in `roleArn` (used by HealthOmics to execute the runs) requires the same permissions as it does for individual **StartRun** calls. For details, see [Service roles for AWS HealthOmics](permissions-service.md).

### Tagging and tag-based access control
<a name="batch-tagging"></a>

Batch runs support tags at two levels:
+ **Batch tags** (tags on the **StartRunBatch** request) — Applied to the batch resource. Tag-based access control (TBAC) is fully enforced for batch tags.
+ **Run tags** (`runTags` in `defaultRunSetting` and per-run `runTags`) — Applied to individual run resources. These tags are merged using the same precedence rules as parameters.

If you use tag-based access control policies, ensure your IAM policy includes `omics:TagResource` with the appropriate `aws:RequestTag` and `aws:TagKeys` conditions.

**Example: Restrict batch creation to non-production environments**

The following policy allows users to create batches and runs, but denies tagging any resource with `environment=production`:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowBatchAndRunCreation",
      "Effect": "Allow",
      "Action": [
        "omics:StartRunBatch",
        "omics:StartRun"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowTaggingNonProd",
      "Effect": "Allow",
      "Action": "omics:TagResource",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/environment": ["dev", "test"]
        }
      }
    },
    {
      "Sid": "DenyProductionTags",
      "Effect": "Deny",
      "Action": "omics:TagResource",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/environment": "production"
        }
      }
    }
  ]
}
```

With this policy:
+ `tags: {"environment": "dev"}` on the batch → Allowed
+ `tags: {"environment": "production"}` on the batch → Denied (403)
+ `runTags: {"environment": "production"}` in `defaultRunSetting` → Denied for individual runs during asynchronous creation

## Getting started: Submit your first batch
<a name="batch-getting-started"></a>

The following example walks through submitting a small batch of two runs, checking progress, and reviewing results.

**Step 1: Submit the batch**

```
aws omics start-run-batch \
  --batch-name "my-first-batch" \
  --default-run-setting '{
    "workflowId": "1234567",
    "roleArn": "arn:aws:iam::{{123456789012}}:role/{{OmicsRole}}",
    "outputUri": "s3://{{my-bucket}}/output/",
    "storageType": "DYNAMIC",
    "parameters": {"referenceUri": "s3://{{my-bucket}}/reference.fasta"}
  }' \
  --batch-run-settings '{
    "inlineSettings": [
      {
        "runSettingId": "sample-A",
        "parameters": {"inputUri": "s3://{{my-bucket}}/sampleA.fastq"}
      },
      {
        "runSettingId": "sample-B",
        "parameters": {"inputUri": "s3://{{my-bucket}}/sampleB.fastq"}
      }
    ]
  }'
```

The response returns a batch ID you use for all subsequent operations:

```
{
  "id": "7123456",
  "arn": "arn:aws:omics:us-west-2:123456789012:runBatch/7123456",
  "status": "CREATING"
}
```

**Step 2: Check batch progress**

```
aws omics get-batch --batch-id {{7123456}}
```

Watch the `status` field progress from `CREATING` → `PENDING` → `SUBMITTING` → `INPROGRESS` → `PROCESSED`. The `submissionSummary` shows how many runs were submitted successfully, and `runSummary` shows execution progress.

**Step 3: Review individual runs**

```
aws omics list-runs-in-batch --batch-id {{7123456}}
```

Each entry maps your `runSettingId` (e.g., `sample-A`) to the HealthOmics-generated `runId`, so you can trace results back to your input samples.

**Step 4: Check for failed submissions**

```
aws omics list-runs-in-batch --batch-id {{7123456}} --submission-status FAILED
```

If any runs failed to submit, the response includes `submissionFailureReason` and `submissionFailureMessage` to help you diagnose the issue.

## Starting a batch run
<a name="batch-starting"></a>

Use **StartRunBatch** to submit multiple runs with a single request. The request includes:
+ `defaultRunSetting` — Shared configuration for all runs in the batch. This includes fields such as `workflowId`, `roleArn`, `outputUri`, `parameters`, `scratchStorageMode`, and `engineSettings`. For Nextflow workflows, use `engineSettings` to specify profiles that apply to all runs in the batch. For more information, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings).
+ `batchRunSettings` — The individual run configurations, provided as one of:
  + `inlineSettings` — An array of up to 100 run-specific configurations provided directly in the request body. Each inline setting can include `engineSettings` to override the default profile for individual runs.
  + `s3UriSettings` — An Amazon S3 URI pointing to a JSON file containing the run configurations. Required for batches with more than 100 runs, and supports up to 100,000 runs.

You can also provide the following fields:
+ `batchName` — An optional human-readable name for the batch.
+ `requestId` — An idempotency token to prevent duplicate batch submissions.
+ `tags` — Tags to associate with the batch resource itself.

### Submit small batches with inline run configurations
<a name="batch-inline-settings"></a>

Provide an array of run-specific configurations directly in the request body using `inlineSettings`. Each entry must include a unique `runSettingId` (required). The `runSettingId` is your key for correlating results — when you call **ListRunsInBatch**, each entry maps your `runSettingId` to the HealthOmics-generated `runId` and `runArn`.

You can include up to 100 entries with inline configurations.

```
{
  "batchName": "genomics-cohort-analysis",
  "requestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "tags": {
    "project": "genomics-study",
    "environment": "production"
  },
  "defaultRunSetting": {
    "workflowId": "1234567",
    "roleArn": "arn:aws:iam::{{123456789012}}:role/{{OmicsRole}}",
    "outputUri": "s3://{{my-bucket}}/output/",
    "parameters": {
      "referenceUri": "s3://{{my-bucket}}/reference/genome.fasta"
    },
    "runTags": {
      "analysis-type": "germline"
    }
  },
  "batchRunSettings": {
    "inlineSettings": [
      {
        "runSettingId": "sample-001",
        "name": "Sample-001-Analysis",
        "parameters": {
          "inputUri": "s3://{{my-bucket}}/input/sample-001.fastq",
          "sampleName": "sample-001"
        },
        "runTags": {
          "patient-id": "patient001"
        }
      },
      {
        "runSettingId": "sample-002",
        "name": "Sample-002-Analysis",
        "outputUri": "s3://{{my-bucket}}/output/special/",
        "parameters": {
          "inputUri": "s3://{{my-bucket}}/input/sample-002.fastq",
          "sampleName": "sample-002"
        },
        "runTags": {
          "patient-id": "patient002"
        }
      }
    ]
  }
}
```

**CLI**

```
aws omics start-run-batch \
  --batch-name "genomics-cohort-analysis" \
  --request-id "a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  --default-run-setting '{
    "workflowId": "1234567",
    "roleArn": "arn:aws:iam::{{123456789012}}:role/{{OmicsRole}}",
    "outputUri": "s3://{{my-bucket}}/output/",
    "storageType": "DYNAMIC",
    "parameters": {"referenceUri": "s3://{{my-bucket}}/reference.fasta"}
  }' \
  --batch-run-settings '{
    "inlineSettings": [
      {
        "runSettingId": "sample-001",
        "name": "Run-001",
        "parameters": {"inputUri": "s3://{{my-bucket}}/input1.fastq"}
      },
      {
        "runSettingId": "sample-002",
        "name": "Run-002",
        "parameters": {"inputUri": "s3://{{my-bucket}}/input2.fastq"}
      }
    ]
  }'
```

### Submit large batches with run configurations in S3
<a name="batch-s3-settings"></a>

For batches with more than 100 runs, store your run configurations in a JSON file in Amazon S3 and provide the URI using `s3UriSettings`. The JSON file must contain an array of run-specific setting objects, each with a unique `runSettingId`. The file can contain up to 100,000 entries.

The S3 file format is the same as the `inlineSettings` array:

```
[
  {
    "runSettingId": "sample-001",
    "name": "Sample-001-Analysis",
    "parameters": {
      "inputUri": "s3://{{my-bucket}}/input/sample-001.fastq",
      "sampleName": "sample-001"
    }
  },
  {
    "runSettingId": "sample-002",
    "name": "Sample-002-Analysis",
    "parameters": {
      "inputUri": "s3://{{my-bucket}}/input/sample-002.fastq",
      "sampleName": "sample-002"
    }
  }
]
```

**API request**

```
{
  "defaultRunSetting": {
    "workflowId": "1234567",
    "roleArn": "arn:aws:iam::{{123456789012}}:role/{{OmicsRole}}",
    "outputUri": "s3://{{my-bucket}}/output/",
    "parameters": {
      "referenceUri": "s3://{{my-bucket}}/reference/genome.fasta"
    }
  },
  "batchRunSettings": {
    "s3UriSettings": "s3://{{my-bucket}}/configs/run-configs.json"
  }
}
```

**CLI**

```
aws omics start-run-batch \
  --default-run-setting '{
    "workflowId": "1234567",
    "roleArn": "arn:aws:iam::{{123456789012}}:role/{{OmicsRole}}",
    "outputUri": "s3://{{my-bucket}}/output/",
    "parameters": {"referenceUri": "s3://{{my-bucket}}/reference.fasta"}
  }' \
  --batch-run-settings '{"s3UriSettings": "s3://{{my-bucket}}/configs/run-configs.json"}'
```

**Important**  
The IAM service role specified in `roleArn` must have read access to the Amazon S3 object specified in `s3UriSettings`. HealthOmics validates access to the Amazon S3 file during the synchronous API call and records the file's ETag. If the file is modified after submission, the batch fails during asynchronous processing.

### Response
<a name="batch-response"></a>

A successful request returns a batch ID and initial status:

```
{
  "id": "7123456",
  "arn": "arn:aws:omics:us-west-2:123456789012:runBatch/7123456",
  "status": "CREATING",
  "uuid": "96c57683-74bf-9d6d-ae7e-f09b097db14a",
  "tags": {
    "project": "genomics-study",
    "environment": "production"
  }
}
```

If synchronous validation fails (for example, an invalid workflow ID or inaccessible Amazon S3 URI), the API returns an error before any runs are submitted.

### Parameter reference
<a name="batch-parameter-reference"></a>

The following table shows which **StartRun** fields can be set per run and which apply only at the batch level. For full field descriptions, see the **StartRun** API reference.


| Field | Batch-level (`defaultRunSetting`) | Per-run configurable (`inlineSettings`) | 
| --- | --- | --- | 
| workflowId | Yes | No | 
| workflowType | Yes | No | 
| workflowVersionName | Yes | No | 
| workflowOwnerId | Yes | No | 
| roleArn | Yes | No | 
| storageCapacity | Yes | No | 
| storageType | Yes | No | 
| runGroupId | Yes | No | 
| logLevel | Yes | No | 
| cacheBehavior | Yes | No | 
| cacheId | Yes | No | 
| retentionMode | Yes | No | 
| networkingMode | Yes | No | 
| configurationName | Yes | No | 
| name | Yes | Yes | 
| outputUri | Yes | Yes | 
| parameters | Yes | Yes (merged) | 
| priority | Yes | Yes | 
| runTags | Yes | Yes (merged) | 
| outputBucketOwnerId | Yes | Yes | 

**Note**  
The `runId` (for individual re-runs) field is not supported as an input to **StartRunBatch**. Each batch submission always creates new runs, and each run will receive a `runId`. See [Rerun a run in HealthOmics](rerun-a-run.md) for retrying individual runs.

### Parameter merging
<a name="batch-parameter-merging"></a>

Parameters from `defaultRunSetting` are merged with the run-specific parameters provided in `inlineSettings` or through an S3 URI. Run-specific values take precedence when keys overlap.

**Example:**


| Source | Parameters | 
| --- | --- | 
| defaultRunSetting | {"referenceUri": "s3://bucket/ref.fasta", "version": "v1"} | 
| inlineSettings entry | {"inputUri": "s3://bucket/sample.fastq", "version": "v2"} | 
| Merged result | {"referenceUri": "s3://bucket/ref.fasta", "inputUri": "s3://bucket/sample.fastq", "version": "v2"} | 

The same merging behavior applies to `runTags`. Tags specified in the per-run configuration override tags with the same key from `defaultRunSetting.runTags`, and new keys are added.

**Tag merging example:**


| Source | Tags | 
| --- | --- | 
| defaultRunSetting.runTags | {"project": "cancer-research", "pipeline-version": "v2.1"} | 
| inlineSettings[].runTags | {"patient-id": "patient001", "pipeline-version": "v3.0"} | 
| Merged result (applied to run) | {"project": "cancer-research", "patient-id": "patient001", "pipeline-version": "v3.0"} | 

**Note**  
Batch-level tags (on the **StartRunBatch** request) are applied only to the batch resource itself. They are not inherited by individual runs. Run-level tags are controlled through `defaultRunSetting.runTags` and per-run `runTags`.

### Gradual submission
<a name="batch-gradual-submission"></a>

**StartRunBatch** validates common fields synchronously and returns immediately with a batch ID and status `CREATING`. Runs in a batch are submitted gradually and asynchronously at a controlled rate according to your throughput quotas.

For the full list of HealthOmics quotas, see [HealthOmics service quotas](service-quotas.md).

The batch transitions through the following states during normal processing:

1. `CREATING` — Batch is being created.

1. `PENDING` — Batch created, run configurations being validated.

1. `SUBMITTING` — Validation complete, individual runs being submitted.

1. `INPROGRESS` — All run submissions attempted, runs are executing.

1. `PROCESSED` — All runs have reached a terminal state.

**Important**  
Batch run submission shares the same **StartRun** throughput quota as direct **StartRun** API calls. If you call **StartRun** directly while a large batch is being processed, both the batch submissions and your direct calls compete for the same capacity. This can cause batch runs to fail with `ThrottlingException` (rate exceeded) or your direct **StartRun** calls to be throttled. The same applies to **CancelRun** and **DeleteRun** — these share throughput quotas with **CancelRunBatch** and **DeleteRunBatch** respectively.

## Monitoring batch progress
<a name="batch-monitoring"></a>

### Get batch status
<a name="batch-get-status"></a>

Use **GetBatch** to retrieve overall status and submission progress for a batch.

```
aws omics get-batch --batch-id {{7123456}}
```

The response includes:
+ `status` — Overall batch state.
+ `submissionSummary` — Counts of successful and failed submissions for start, cancel, and delete operations.
+ `runSummary` — Counts of runs in each execution state. Possible values: `PENDING`, `STARTING`, `RUNNING`, `STOPPING`, `COMPLETED`, `DELETED`, `CANCELLED`, or `FAILED`
+ Timestamps for lifecycle events — `creationTime`, `submittedTime`, `processedTime`, `failedTime`.

**Example response:**

```
{
  "id": "7123456",
  "arn": "arn:aws:omics:us-west-2:123456789012:runBatch/7123456",
  "uuid": "96c57683-74bf-9d6d-ae7e-f09b097db14a",
  "name": "genomics-cohort-analysis",
  "status": "INPROGRESS",
  "totalRuns": 96,
  "defaultRunSetting": {
    "workflowId": "1234567",
    "roleArn": "arn:aws:iam::123456789012:role/OmicsRole",
    "outputUri": "s3://my-bucket/output/"
  },
  "submissionSummary": {
    "successfulStartSubmissionCount": 94,
    "failedStartSubmissionCount": 2,
    "pendingStartSubmissionCount": 0
  },
  "runSummary": {
    "pendingRunCount": 10,
    "startingRunCount": 5,
    "runningRunCount": 50,
    "stoppingRunCount": 0,
    "completedRunCount": 29,
    "failedRunCount": 0,
    "cancelledRunCount": 0,
    "deletedRunCount": 0
  },
  "creationTime": "2025-03-15T10:00:00Z",
  "submittedTime": "2025-03-15T10:05:00Z",
  "tags": {
    "project": "genomics-study"
  }
}
```

**Note**  
Run execution summaries are eventually consistent and may lag behind actual run states. Final counts are reconciled when the batch reaches `PROCESSED` status.

### List runs in a batch
<a name="batch-list-runs"></a>

Use **ListRunsInBatch** to retrieve detailed information for individual runs within a batch. Results are paginated.

```
aws omics list-runs-in-batch --batch-id {{7123456}}
```

You can filter results using one of the following query parameters. Only one filter per call is supported.


| Filter | Description | 
| --- | --- | 
| submissionStatus | Filter by submission status: SUCCESS, FAILED, CANCEL\_SUCCESS, CANCEL\_FAILED, DELETE\_SUCCESS, or DELETE\_FAILED. | 
| runSettingId | Retrieve the run for a specific run setting ID. | 
| runId | Retrieve the run for a specific run ID. | 

**Example: List failed submissions**

```
aws omics list-runs-in-batch --batch-id {{7123456}} --submission-status FAILED
```

Each result includes:
+ `runSettingId` — The customer-provided identifier for the run configuration.
+ `runId` — The HealthOmics-generated run identifier (empty if submission failed).
+ `runArn` — The full ARN of the run.
+ `submissionStatus` — The submission outcome (`SUCCESS`, `FAILED`, `CANCEL_SUCCESS`, `CANCEL_FAILED`, `DELETE_SUCCESS`, or `DELETE_FAILED`).
+ `submissionFailureReason` and `submissionFailureMessage` — Details if submission failed.

**Note**  
`runSettingId` is the customer-specified identifier you provided in the run configuration. `runId` is the HealthOmics-generated identifier assigned after successful submission. If submission failed, `runId` is empty.

### List batches
<a name="batch-list-batches"></a>

Use **ListBatch** to retrieve all batch resources in your account. Results are paginated.

```
aws omics list-batch
```

You can filter results using the following query parameters:


| Filter | Description | 
| --- | --- | 
| status | Filter by batch status. | 
| name | Filter by batch name. | 
| runGroupId | Filter by run group ID. | 

## Handling failed runs
<a name="batch-handling-failures"></a>

There are two distinct types of failures in batch processing. Understanding the difference is critical for troubleshooting.

### Batch-level failures
<a name="batch-level-failures"></a>

A batch-level failure means the batch itself failed — no runs were created (or only some were created before the failure). The batch status is `FAILED`.

Call **GetBatch** and check the `failureReason` field. Common failure reasons include:


| Failure category | Example `failureReason` message | Action | 
| --- | --- | --- | 
| Validation error | "Batch has 100001 runs but 100000 runs is the max.", "Expected 50 unique runSettingIds but there were 49", "Invalid JSON format in run configurations" | Fix the configuration and submit a new batch. These errors are not retryable. | 
| S3 configuration changed | "Expected s3UriConfigs etag: \\"abc123\\" but was: \\"def456\\". s3UriConfigs have changed since calling StartRunBatch" | Do not modify the S3 file after submission. Resubmit with the current file. | 
| Transient service error | "There was a transient error in the service. Retry the batch." | Retry by submitting the same batch again. Use the same requestId for idempotency. | 

**Example: Batch failed due to validation**

```
aws omics get-batch --batch-id {{7123456}}
```

```
{
  "id": "7123456",
  "arn": "arn:aws:omics:us-west-2:123456789012:runBatch/7123456",
  "status": "FAILED",
  "failureReason": "Batch has 100001 runs but 100000 runs is the max.",
  "failedTime": "2025-03-15T10:01:00Z"
}
```

### Run-level failures
<a name="batch-run-level-failures"></a>

A run-level failure means the batch itself succeeded (status is `INPROGRESS` or `PROCESSED`), but individual runs failed to submit. The batch continues processing other runs — it does not stop on the first failure.

**1. Check the submission summary**

```
aws omics get-batch --batch-id {{7123456}}
```

Look at `submissionSummary.failedStartSubmissionCount`. If this is greater than zero, some runs failed during submission.

**2. List failed submissions**

```
aws omics list-runs-in-batch --batch-id {{7123456}} --submission-status FAILED
```

Each failed entry includes:
+ `runSettingId` — Which run configuration failed.
+ `submissionFailureReason` — The error category.
+ `submissionFailureMessage` — A detailed error message.

**3. Submission failure reasons**

The following table lists the possible values for `submissionFailureReason` on individual runs:


| `submissionFailureReason` | Meaning | Retryable? | 
| --- | --- | --- | 
| ValidationException | Run parameters are invalid — for example, parameters don't match the workflow definition, invalid S3 URI format, or constraint violations. | No — fix the configuration. | 
| AccessDeniedException | The IAM service role lacks permissions to access required resources (S3 inputs, KMS keys, CloudWatch Logs, ECR images). | No — update the role policy. | 
| ResourceNotFoundException | A referenced resource (workflow, run group, or run cache) doesn't exist or is not in an active state. | No — verify resource IDs. | 
| ServiceQuotaExceededException | The account has reached the maximum number of active runs or another service quota. | Wait for runs to complete, or request a quota increase. | 
| ConflictException | A conflicting operation is in progress — for example, a duplicate run creation attempt. | Typically resolves on its own. | 
| ThrottlingException | The request was throttled due to API rate limits. | The service retries automatically. If it persists after retries, reduce concurrent batch submissions. | 
| RequestTimeoutException | The request timed out during processing. | The service retries automatically. If it persists, check for downstream issues. | 
| InternalServerException | An unexpected service error occurred. | The service retries automatically. If it persists after retries, contact AWS Support. | 

**Note**  
HealthOmics automatically retries transient errors (`ThrottlingException`, `RequestTimeoutException`, `InternalServerException`) for each run. A run is marked as `FAILED` only after all retry attempts are exhausted. Non-retryable errors (`ValidationException`, `AccessDeniedException`, `ResourceNotFoundException`) fail immediately without retries.

**4. Resubmit failed runs**

Create a new batch containing only the corrected run configurations. Use the same `defaultRunSetting` and include only the `runSettingId` entries that failed. There is no built-in retry mechanism for failed runs — you must submit a new batch.

## Canceling a batch
<a name="batch-canceling"></a>

Use **CancelRunBatch** to cancel a batch in progress. The cancel operation:
+ Prevents not-yet-submitted and pending runs from starting
+ Submits **CancelRun** requests for runs that have already started.

```
aws omics cancel-run-batch --batch-id {{7123456}}
```

**Important**  
Cancel is only allowed on batches in `PENDING`, `SUBMITTING`, or `INPROGRESS` state.
Only one cancel or delete operation per batch is allowed at a time.
Cancel operations are non-atomic and may be partially successful. Use **GetBatch** to review `successfulCancelSubmissionCount` and `failedCancelSubmissionCount` in the `submissionSummary`.

## Deleting batch runs
<a name="batch-deleting-runs"></a>

Use **DeleteRunBatch** to delete the individual runs within a batch.

```
aws omics delete-run-batch --batch-id {{7123456}}
```

**Important**  
Delete is only allowed on batches in `PROCESSED` or `CANCELLED` state.
Only one cancel or delete operation per batch is allowed at a time.
Delete operations are non-atomic and may be partially successful. Use **GetBatch** to review `successfulDeleteSubmissionCount` and `failedDeleteSubmissionCount` in the `submissionSummary`.

## Deleting batch metadata
<a name="batch-deleting-metadata"></a>

Use **DeleteBatch** to remove the batch resource and its associated metadata. This is a separate operation from **DeleteRunBatch**.

```
aws omics delete-batch --batch-id {{7123456}}
```

**Important**  
**DeleteBatch** requires the batch to be in a terminal state (`PROCESSED`, `FAILED`, `CANCELLED`, `RUNS_DELETE_FAILED`, or `RUNS_DELETED`).
**DeleteBatch** does not delete the individual runs. Use **DeleteRunBatch** first if you want to remove the runs as well.
After **DeleteBatch** completes, the batch metadata is no longer accessible. You cannot call **GetBatch**, **ListRunsInBatch**, **DeleteRunBatch**, or **CancelRunBatch** on a deleted batch.

## EventBridge events for batches
<a name="batch-eventbridge"></a>

HealthOmics sends events to Amazon EventBridge whenever a batch changes status. You can use these events to automate workflows—for example, to trigger a notification when a batch completes or fails, or to start a downstream pipeline when all runs finish.

Batch events use the same event bus and source as other HealthOmics events. For general setup instructions, see [Using EventBridge with AWS HealthOmics](eventbridge.md).

### Event detail-type
<a name="batch-event-detail-type"></a>


| Event name | Emitted when | 
| --- | --- | 
| RunBatch Status Change | The batch transitions to a new status (CREATING, PENDING, SUBMITTING, INPROGRESS, STOPPING, CANCELLED, PROCESSED, FAILED, RUNS\_DELETING, RUNS\_DELETED) | 

### Event detail fields
<a name="batch-event-detail-fields"></a>

The `detail` object in a batch event includes the following fields:


| Field | Type | Description | 
| --- | --- | --- | 
| omicsVersion | String | Event schema version (currently 1.0.0). | 
| arn | String | The batch ARN. | 
| batchId | String | The batch identifier. | 
| status | String | The new batch status. | 
| uuid | String | The batch UUID. | 
| batchName | String | The batch name (if provided). | 
| totalRuns | String | Total number of runs in the batch. | 
| failureReason | String | Failure reason (present only when status is FAILED). | 
| failureMessage | String | Detailed failure message (present only when status is FAILED). | 
| successfulStartSubmissionCount | String | Number of runs successfully submitted. | 
| failedStartSubmissionCount | String | Number of runs that failed to submit. | 
| pendingStartSubmissionCount | String | Number of runs still pending submission. | 
| pendingRunCount | String | Number of runs in pending state. | 
| startingRunCount | String | Number of runs starting. | 
| runningRunCount | String | Number of runs currently running. | 
| stoppingRunCount | String | Number of runs being stopped. | 
| completedRunCount | String | Number of completed runs. | 
| failedRunCount | String | Number of failed runs. | 
| cancelledRunCount | String | Number of cancelled runs. | 
| deletedRunCount | String | Number of deleted runs. | 
| workflowId | String | The workflow identifier. | 
| workflowArn | String | The workflow ARN. | 
| workflowVersionArn | String | The workflow version ARN (if applicable). | 
| workflowOwnerId | String | The workflow owner account ID (for shared workflows). | 
| runCache | String | The run cache ARN (if applicable). | 
| runCacheBehavior | String | The run cache behavior (if applicable). | 

### Event examples
<a name="batch-event-examples"></a>

**Example: Batch completed event**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-example11111",
  "detail-type": "RunBatch Status Change",
  "source": "aws.omics",
  "account": "123456789012",
  "time": "2025-03-15T12:30:00Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:omics:us-west-2:123456789012:runBatch/7123456"
  ],
  "detail": {
    "omicsVersion": "1.0.0",
    "arn": "arn:aws:omics:us-west-2:123456789012:runBatch/7123456",
    "batchId": "7123456",
    "status": "PROCESSED",
    "uuid": "96c57683-74bf-9d6d-ae7e-f09b097db14a",
    "batchName": "genomics-cohort-analysis",
    "totalRuns": "96",
    "successfulStartSubmissionCount": "94",
    "failedStartSubmissionCount": "2",
    "pendingStartSubmissionCount": "0",
    "completedRunCount": "90",
    "failedRunCount": "4",
    "cancelledRunCount": "0",
    "workflowId": "1234567"
  }
}
```

**Example: Batch failed event**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-example22222",
  "detail-type": "RunBatch Status Change",
  "source": "aws.omics",
  "account": "123456789012",
  "time": "2025-03-15T10:01:00Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:omics:us-west-2:123456789012:runBatch/7123456"
  ],
  "detail": {
    "omicsVersion": "1.0.0",
    "arn": "arn:aws:omics:us-west-2:123456789012:runBatch/7123456",
    "batchId": "7123456",
    "status": "FAILED",
    "failureReason": "VALIDATION_EXCEPTION",
    "failureMessage": "Expected 100 unique runSettingIds but there were 99"
  }
}
```

**Example: EventBridge rule for batch completion**

The following event pattern matches when any batch reaches a terminal state:

```
{
  "source": ["aws.omics"],
  "detail-type": ["RunBatch Status Change"],
  "detail": {
    "status": ["PROCESSED", "FAILED", "CANCELLED"]
  }
}
```

## Limitations and considerations
<a name="batch-limitations"></a>
+ **Shared throughput quotas** — Batch operations share the same per-account quotas as their individual API counterparts. **StartRunBatch** consumes **StartRun** service quotas. **CancelRunBatch** consumes **CancelRun** quotas, and **DeleteRunBatch** consumes **DeleteRun** quotas. Avoid calling individual run APIs while a large batch is in progress, as this can cause submission failures.
+ **Gradual submission** — Runs in a batch are submitted gradually and asynchronously according to your throughput quotas.
+ **Non-atomic operations** — **StartRunBatch**, **CancelRunBatch**, and **DeleteRunBatch** can all be partially successful. Always check submission summaries to identify runs that need retry.
+ **Eventual consistency** — Run execution status counts in **GetBatch** may lag behind actual run states. Final counts are accurate once the batch reaches `PROCESSED`.
+ **Single filter per list call** — **ListRunsInBatch** and **ListBatch** support only one filter per API call.
+ **Re-run not supported** — The `runId` (re-run) field is not supported in **StartRunBatch**. Each batch submission always creates new runs.
+ **Ready2Run workflows** — Batch runs are not supported with Ready2Run workflows.
+ **Inline configuration limit** — Inline configurations (`inlineSettings`) support up to 100 entries. For larger batches, use `s3UriSettings`. This limit is not adjustable.
+ **S3 configuration file** — The S3 configuration file must be a JSON array of run setting objects. The maximum file size is 6 GB, supporting up to 100,000 run configurations.
+ **S3 file immutability** — Do not modify the S3 configuration file after submitting the batch. HealthOmics validates the file's entity tag (ETag) during submission and fails the batch if the file has changed.