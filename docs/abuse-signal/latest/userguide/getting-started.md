

# Getting started with AWS Abuse Signal API

This tutorial shows you how to submit and track your first abuse report, and takes about 10 minutes to complete.

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Step 1: Choose a Region and endpoint](#getting-started-step1)
+ [Step 2: Submit a report](#getting-started-step2)
+ [Step 3: Track the report](#getting-started-step3)
+ [Step 4: List your reports](#getting-started-step4)
+ [Handling errors](#getting-started-handling-errors)
+ [Clean up](#getting-started-clean-up)
+ [Next steps](#getting-started-next-steps)

## Prerequisites
<a name="getting-started-prerequisites"></a>

AWS Abuse Signal API charges no additional fee, so this tutorial costs nothing to complete.

Before you begin, make sure that you have the following:
+ An AWS identity (IAM user, IAM role, or federated user) that can sign requests with SigV4 or SigV4a. For account setup, including securing your root user with multi-factor authentication (MFA) and creating an IAM identity with the required `abuse:` permissions, see [Setting up AWS Abuse Signal API](setting-up.md).
+ IAM permissions for the actions you intend to call: `abuse:CreateAbuseReport`, `abuse:GetAbuseReportStatus`, and `abuse:ListAbuseReportStatuses`. For example policies, see [AWS Abuse Signal API identity-based policy examples](security-iam-id-based-policy-examples.md).
+ A well-formed XARF report. See [Report format (XARF)](report-format.md).

**Note**  
Sign requests using the service signing name `abuse`. For multi-Region use, sign with SigV4a. For more information, see [Choosing SigV4 or SigV4a](regions-endpoints.md#regions-endpoints-signing).

## Step 1: Choose a Region and endpoint
<a name="getting-started-step1"></a>

Pick a supported Region and use its Regional endpoint. For example, in `us-east-1`:

```
https://abuse.us-east-1.amazonaws.com
```

For all Regions and for the IPv6 and AWS PrivateLink endpoint names, see [Regions and endpoints](regions-endpoints.md).

## Step 2: Submit a report
<a name="getting-started-step2"></a>

Call `CreateAbuseReport` with your XARF report under the `report.xarf` key. Optionally include a `correlationId` to cross-reference the submission in your own system, and a `clientToken` to make retries idempotent.

```
POST /v1/abuse HTTP/1.1
Host: abuse.us-east-1.amazonaws.com
Content-type: application/json
Authorization: AWS4-HMAC-SHA256 Credential=...

{
  "report": {
    "xarf": {
      "xarf_version": "4.0.0",
      "report_id": "550e8400-e29b-41d4-a716-446655440000",
      "timestamp": "2026-09-09T14:30:00Z",
      "category": "content",
      "type": "phishing",
      "reporter": {
        "org": "Example Corp",
        "contact": "abuse@example.com",
        "domain": "example.com"
      },
      "sender": {
        "org": "Unknown",
        "contact": "unknown@example.com",
        "domain": "example.com"
      },
      "source_identifier": "192.0.2.42",
      "url": "https://example.com/login",
      "tags": ["lifecycle:test"]
    }
  },
  "correlationId": "incident-2026-09-001",
  "clientToken": "EXAMPLE-TOKEN-0001"
}
```

A successful response confirms that AWS received your report. It doesn’t mean that AWS has reached an outcome.

```
HTTP/1.1 202 Accepted
Content-type: application/json

{
  "reportId": "rpt01J5K9XMBN3QWERTY12345",
  "correlationId": "incident-2026-09-001"
}
```

**Important**  
The `"tags": ["lifecycle:test"]` entry marks this as a test submission. Reports tagged `lifecycle:test` are for testing the API and aren’t processed as abuse reports. Omit the tag when you submit a genuine abuse report. For more information, see [Tagging test submissions](report-format.md#report-format-tags).

## Step 3: Track the report
<a name="getting-started-step3"></a>

Use the returned report ID with `GetAbuseReportStatus`:

```
GET /v1/abuse/rpt01J5K9XMBN3QWERTY12345 HTTP/1.1
Host: abuse.us-east-1.amazonaws.com
Authorization: AWS4-HMAC-SHA256 Credential=...
```

```
HTTP/1.1 200 OK
Content-type: application/json

{
  "reportId": "rpt01J5K9XMBN3QWERTY12345",
  "correlationId": "incident-2026-09-001",
  "status": "PROCESSING",
  "description": "Report has been received and is being processed.",
  "submittedAt": 1788964201,
  "lastUpdatedAt": 1788964204
}
```

Processing can take longer than this tutorial. When processing finishes, the status changes to `COMPLETED`, which is final, and the response includes a `reasonCode` that describes the outcome, as in the following example. Reports tagged `lifecycle:test` aren’t processed as abuse reports.

```
HTTP/1.1 200 OK
Content-type: application/json

{
  "reportId": "rpt01J5K9XMBN3QWERTY12345",
  "correlationId": "incident-2026-09-001",
  "status": "COMPLETED",
  "description": "Enforcement action was taken on the reported resource.",
  "reasonCode": "ACTIONED",
  "submittedAt": 1788964201,
  "lastUpdatedAt": 1789031700
}
```

The status advances from `QUEUED` to `PROCESSING` to `COMPLETED`. Immediately after submission, the status record might still be propagating. If your SDK supports waiters, use the `ReportProcessing` waiter, which succeeds when the report reaches `PROCESSING` or `COMPLETED`. For the full lifecycle and the resolution reason codes, see [Tracking status](submitting-reports.md#submitting-reports-tracking).

## Step 4: List your reports
<a name="getting-started-step4"></a>

Use `ListAbuseReportStatuses` to enumerate your submissions, optionally filtering by `correlationId` and paginating with `maxResults` (1–50) and `nextToken`:

```
GET /v1/abusestatuses?correlationId=incident-2026-09-001&maxResults=25 HTTP/1.1
Host: abuse.us-east-1.amazonaws.com
Authorization: AWS4-HMAC-SHA256 Credential=...
```

For more about pagination, see [Listing and pagination](submitting-reports.md#submitting-reports-listing).

## Handling errors
<a name="getting-started-handling-errors"></a>

The following table describes common errors and how to resolve them.


| Error | HTTP | What to do | 
| --- | --- | --- | 
|  `ValidationException`  | 400 | Inspect `fieldList`, fix the flagged fields, and resubmit. | 
|  `SubmissionRequirementException`  | 422 | Inspect `unmetRequirements`, change the report content to meet the requirement, and resubmit. The report is well-formed but doesn’t meet a submission requirement, such as the submission lookback window or a `source_identifier` restriction. See [Submission requirements and rejections](submitting-reports.md#submitting-reports-policy). | 
|  `AccessDeniedException`  | 403 | Verify your signature and your IAM permissions for the `abuse:` action. | 
|  `ResourceNotFoundException`  | 404 | Retry status reads briefly. The report ID does not exist yet, or it has not propagated. | 
|  `ConflictException`  | 409 | Use a new token, or resend the original payload. You reused a `clientToken` with a different payload. | 

## Clean up
<a name="getting-started-clean-up"></a>

You submitted a test report and tracked its status to `PROCESSING`. Reports tagged `lifecycle:test` aren’t processed as abuse reports. For a genuine report, the response includes a `reasonCode` such as `ACTIONED` when the report reaches `COMPLETED`.

You don’t need to clean up anything for this walkthrough. You can’t delete an abuse report after you submit it. You tagged this submission with `lifecycle:test` in Step 2, so the service treats it as a test report and deletes it shortly after submission.

Include the `lifecycle:test` tag on test submissions. Omit it only for genuine abuse reports. For more information, see [Tagging test submissions](report-format.md#report-format-tags).

## Next steps
<a name="getting-started-next-steps"></a>

Now that you have submitted and tracked your first abuse report, you can explore the full workflow and the API reference:
+  [Report format (XARF)](report-format.md) – Learn how to build valid XARF reports and attach evidence.
+  [Submitting reports](submitting-reports.md) – Learn about idempotency, status tracking, submission requirements, pagination, and retries.
+  [AWS Abuse Signal API Reference](https://docs.aws.amazon.com/abuse-signal/latest/APIReference/) – Look up the operations, parameters, and errors in detail.