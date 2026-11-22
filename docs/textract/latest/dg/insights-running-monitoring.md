

# Running and monitoring Document Insights jobs

`StartDocumentInsights` submits a document for asynchronous processing and returns a `JobArn`. To find out when the job finishes, you can have Amazon Textract Insights send an event to Amazon EventBridge (recommended), or poll `GetDocumentInsights` with the job ARN until the job reaches a terminal status. This page covers both, and the fields you read along the way.

## Starting a job
<a name="insights-running-monitoring-starting"></a>

Supply the input document, the output prefix, and exactly one of a project ARN or inline blueprints:

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/invoice.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
```

The response contains only the job ARN:

```json
{ "JobArn": "arn:aws:textract:us-east-1:111122223333:job/abcd1234efgh" }
```
+ Supply exactly one of `--project-arn` (uses the project's configured capabilities) or `--blueprints` (inline blueprints, custom extraction results only — see [Running jobs with inline blueprints](insights-inline-blueprints.md)).
+ `OutputConfiguration.S3Uri` is a prefix. Per-job results are written beneath it under the job ID.
+ The input and output buckets must be in the same AWS Region as the request.
+ You can add `--encryption-configuration` for a customer managed AWS KMS key, `--client-request-token` for idempotency, and `--tags` to tag the job. See [Data protection and encryption](insights-data-protection.md) and [Tagging Amazon Textract Insights resources](insights-tagging.md).

## Monitoring with Amazon EventBridge (recommended)
<a name="insights-running-monitoring-eventbridge"></a>

When you enable notifications on a job, Amazon Textract Insights sends one event to EventBridge when the job finishes. You create an EventBridge rule that routes the event to a target such as an Amazon SQS queue, an AWS Lambda function, or an AWS Step Functions state machine, so your application reacts as soon as each job is done.

To enable notifications, pass `--notification-configuration` when you start the job:

```bash
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/invoice.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh" \
  --notification-configuration '{"EventBridgeConfiguration": {"EventBridgeEnabled": true}}'
```

We recommend EventBridge over polling for production workloads, and especially when you run many jobs at once:
+ **You learn about completion sooner.** The event typically arrives within seconds of the job finishing, instead of on your next poll.
+ **You make fewer API calls.** Polling calls count against the `GetDocumentInsights` requests-per-second quota (default 10, see [Limits and quotas](insights-quotas.md)), so polling many jobs at once can cause throttling. Events don't count against Amazon Textract Insights quotas.
+ **You don't need a long-running poller.** Your target runs only when a job finishes, so nothing has to keep track of every outstanding job ARN.

### How it works
<a name="insights-running-monitoring-eventbridge-how"></a>

1. You call `StartDocumentInsights` with `NotificationConfiguration.EventBridgeConfiguration.EventBridgeEnabled` set to `true`.

1. When the job reaches a terminal status, Amazon Textract Insights sends one event to the default event bus in the same AWS account and AWS Region as the job.

1. An EventBridge rule that matches the event delivers it to your target.

**Note**  
Notifications are opt-in for each job. If you omit `NotificationConfiguration`, or set `EventBridgeEnabled` to `false`, no event is sent. If no rule in your account matches the event, EventBridge discards it. Sending events doesn't require additional Amazon Textract Insights permissions. You need EventBridge permissions such as `events:PutRule` and `events:PutTargets` to create the rule, and the target must allow EventBridge to deliver to it.

### Event types
<a name="insights-running-monitoring-eventbridge-event-types"></a>

All events have the source `aws.textract`. The `detail-type` tells you how the job ended.


**Event types**  

| **`detail-type`** | **`detail.job_status`** | **Meaning** | 
| --- | --- | --- | 
| Document Insights Job Succeeded | `SUCCESS` | The job completed. Results are in the output location. | 
| Document Insights Job Failed With Client Error | `FAILED` | The job failed because of the request or its input. Fix the input before retrying. | 
| Document Insights Job Failed With Service Error | `ERROR` | The job failed because of an internal error. You can retry the job. | 

### Event example
<a name="insights-running-monitoring-eventbridge-example"></a>

```json
{
  "version": "0",
  "id": "972bb155-f584-821c-a9ab-680a793a3329",
  "detail-type": "Document Insights Job Succeeded",
  "source": "aws.textract",
  "account": "111122223333",
  "time": "2026-11-10T00:13:34Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "job_id": "abcd1234efgh",
    "job_status": "SUCCESS",
    "input_s3_object": {
      "s3_bucket": "amzn-s3-demo-bucket",
      "name": "documents/invoice.pdf"
    },
    "output_s3_location": {
      "s3_bucket": "amzn-s3-demo-destination-bucket",
      "name": "results/abcd1234efgh/0"
    },
    "error_message": "",
    "job_submission_time": "2026-11-10T00:13:24Z",
    "job_completion_time": "2026-11-10T00:13:34Z",
    "job_duration_in_seconds": 9
  }
}
```

### Event detail fields
<a name="insights-running-monitoring-eventbridge-fields"></a>

Each event's `detail` object carries the following fields:


**Event detail fields**  

| **Field** | **Description** | 
| --- | --- | 
| `job_id` | The job ID: the last segment of the `JobArn` that `StartDocumentInsights` returned. Use it to match the event to your job. The event's `resources` list is empty, so build the job ARN from `job_id`, `region`, and `account` if you need it. | 
| `job_status` | `SUCCESS`, `FAILED`, or `ERROR`. | 
| `input_s3_object`, `output_s3_location` | The bucket and key of the input document, and the bucket and key prefix where the job wrote its results. | 
| `error_message` | A description of the failure for failed jobs. Empty for successful jobs. | 
| `job_submission_time`, `job_completion_time`, `job_duration_in_seconds` | When the job was submitted and finished (ISO 8601 UTC, to the second), and how long it took. | 

### Route events to an Amazon SQS queue
<a name="insights-running-monitoring-eventbridge-sqs"></a>

Create a rule on the default event bus that matches all three detail types:

```bash
aws events put-rule \
  --region us-east-1 \
  --name document-insights-job-completed \
  --event-pattern '{
    "source": ["aws.textract"],
    "detail-type": [
      "Document Insights Job Succeeded",
      "Document Insights Job Failed With Client Error",
      "Document Insights Job Failed With Service Error"
    ]
  }'
```

Allow Amazon EventBridge to send to your queue for this rule only, then add the queue as the rule's target:

```bash
aws sqs set-queue-attributes \
  --region us-east-1 \
  --queue-url https://sqs.us-east-1.amazonaws.com/111122223333/document-insights-events \
  --attributes '{"Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"events.amazonaws.com\"},\"Action\":\"sqs:SendMessage\",\"Resource\":\"arn:aws:sqs:us-east-1:111122223333:document-insights-events\",\"Condition\":{\"ArnEquals\":{\"aws:SourceArn\":\"arn:aws:events:us-east-1:111122223333:rule/document-insights-job-completed\"}}}]}"}'
```

```bash
aws events put-targets \
  --region us-east-1 \
  --rule document-insights-job-completed \
  --targets Id=queue,Arn=arn:aws:sqs:us-east-1:111122223333:document-insights-events
```

**Note**  
With the preceding queue policy, Amazon EventBridge sends to the queue as the `events.amazonaws.com` service principal. If the queue uses server-side encryption, use Amazon SQS-managed encryption (SSE-SQS), or a customer managed AWS KMS key whose key policy allows `events.amazonaws.com` to call `kms:GenerateDataKey` and `kms:Decrypt`. The AWS managed key `alias/aws/sqs` doesn't grant the service principal access, and you can't change its key policy. For more information, see [Configure KMS permissions for AWS services](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.html) in the Amazon SQS Developer Guide.

For other targets, see [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the Amazon EventBridge User Guide.

### Best practices
<a name="insights-running-monitoring-eventbridge-best-practices"></a>

Follow these practices when you react to completion events:
+ **Match on job\_id and make your handler idempotent** – Store the job ARN when you start a job, and design for the same event arriving more than once.
+ **Reconcile jobs you don't hear about** – Event delivery isn't guaranteed. If you haven't received an event for a job by the time you expect it to finish, call `GetDocumentInsights` for that job instead of waiting indefinitely.
+ **Call GetDocumentInsights once, not in a loop** – The event's `output_s3_location` points inside the job's output folder, not at `job_metadata.json`. After a Document Insights Job Succeeded event, call `GetDocumentInsights` once: `OutputConfiguration.S3Uri` in the response is the location of the job's `job_metadata.json`, which lists the path of every `result.json` the job produced. See [Output location and file structure](insights-output-location.md).
+ **Retry service errors, fix client errors** – Retry after a Document Insights Job Failed With Service Error event. After a Document Insights Job Failed With Client Error event, read `error_message` and correct the request or input first.
+ **Polling suits one-off jobs** – Polling fits one-off jobs and scripts. For production workloads, prefer EventBridge. If you poll, back off between calls to stay within the `GetDocumentInsights` quota.

## Polling for completion
<a name="insights-running-monitoring-polling"></a>

Poll `GetDocumentInsights` with the `JobArn`:

```
aws textract get-document-insights \
  --region us-east-1 \
  --job-arn "arn:aws:textract:us-east-1:111122223333:job/abcd1234efgh"
```

The response reports the status, and either the output location or the error:

```json
{
  "Status": "SUCCEEDED",
  "OutputConfiguration": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/job_metadata.json" }
}
```

### Job statuses
<a name="insights-running-monitoring-statuses"></a>

The `Status` field reports one of the following values:


| **Status** | **Meaning** | **What to do** | 
| --- | --- | --- | 
| **`IN_PROGRESS`** | The job is still processing. | Wait, then poll again. | 
| **`SUCCEEDED`** | The job completed. | Read `job_metadata.json` at `OutputConfiguration.S3Uri` to locate each `result.json`. | 
| **`FAILED`** | The job failed. | Read `ErrorType` and `ErrorMessage`. | 

On `SUCCEEDED`, `OutputConfiguration.S3Uri` points at the job's `job_metadata.json`, which lists the S3 path of every `result.json` the job produced. See [Output location and file structure](insights-output-location.md).

On `FAILED`, the response includes `ErrorType` and `ErrorMessage` describing the failure.

## Start-and-poll loop (bash)
<a name="insights-running-monitoring-bash"></a>

The following Bash script starts a job and polls until it reaches a terminal status:

```bash
#!/usr/bin/env bash
set -euo pipefail

REGION="us-east-1"
PROJECT_ARN="arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
INPUT="s3://amzn-s3-demo-bucket/documents/invoice.pdf"
OUTPUT="s3://amzn-s3-demo-destination-bucket/results"

JOB_ARN=$(aws textract start-document-insights \
  --region "$REGION" \
  --input-configuration  "S3Uri=$INPUT" \
  --output-configuration "S3Uri=$OUTPUT" \
  --project-arn "$PROJECT_ARN" \
  --query JobArn --output text)

echo "Started $JOB_ARN"

while true; do
  STATUS=$(aws textract get-document-insights \
    --region "$REGION" --job-arn "$JOB_ARN" \
    --query Status --output text)
  echo "Status: $STATUS"
  case "$STATUS" in
    SUCCEEDED)
      aws textract get-document-insights \
        --region "$REGION" --job-arn "$JOB_ARN" \
        --query OutputConfiguration.S3Uri --output text
      break ;;
    FAILED)
      aws textract get-document-insights \
        --region "$REGION" --job-arn "$JOB_ARN" \
        --query '{ErrorType:ErrorType,ErrorMessage:ErrorMessage}'
      exit 1 ;;
    *)
      sleep 10 ;;
  esac
done
```

## Start-and-poll loop (Python, boto3)
<a name="insights-running-monitoring-python"></a>

The following Python script uses boto3 to combine the start and poll calls into a single loop:

```python
import time
import boto3

region = "us-east-1"
textract = boto3.client("textract", region_name=region)

response = textract.start_document_insights(
    InputConfiguration={"S3Uri": "s3://amzn-s3-demo-bucket/documents/invoice.pdf"},
    OutputConfiguration={"S3Uri": "s3://amzn-s3-demo-destination-bucket/results"},
    ProjectArn="arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh",
)
job_arn = response["JobArn"]
print(f"Started {job_arn}")

while True:
    result = textract.get_document_insights(JobArn=job_arn)
    status = result["Status"]
    print(f"Status: {status}")
    if status == "SUCCEEDED":
        print("Output:", result["OutputConfiguration"]["S3Uri"])
        break
    if status == "FAILED":
        print("ErrorType:", result.get("ErrorType"))
        print("ErrorMessage:", result.get("ErrorMessage"))
        break
    time.sleep(10)
```

## Idempotency
<a name="insights-running-monitoring-idempotency"></a>

Pass `ClientRequestToken` (`--client-request-token`) on `StartDocumentInsights` to make a submission idempotent. Retrying with the same token and the same parameters returns the original job rather than starting a duplicate. Use this to make client-side retries safe when a network error leaves you unsure whether a job was accepted.

## Error fields
<a name="insights-running-monitoring-errors"></a>

When `Status` is `FAILED`, read:
+ `ErrorType` — the error classification.
+ `ErrorMessage` — a human-readable description of what went wrong.

`GetDocumentInsights` returns `InvalidJobIdException` when the job ARN is well formed but no such job exists, `InvalidParameterException` when the job ARN is malformed, and `AccessDeniedException` when the job belongs to another account. For the full API error set and remediation, see [Troubleshooting](insights-troubleshooting.md) and the Amazon Textract Insights API Reference. 