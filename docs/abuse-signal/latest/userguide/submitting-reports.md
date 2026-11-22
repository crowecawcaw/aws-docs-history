

# Submitting reports

AWS Abuse Signal API accepts abuse reports through an asynchronous API. This page covers the submission workflow in depth: idempotency, correlation IDs, tracking, pagination, and retry behavior. For a first end-to-end walkthrough, start with [Getting started with AWS Abuse Signal API](getting-started.md).

**Topics**
+ [The submission workflow](#submitting-reports-workflow)
+ [Tracking status](#submitting-reports-tracking)
+ [Idempotency in depth](#submitting-reports-idempotency)
+ [Correlation IDs](#submitting-reports-correlation-ids)
+ [Submission requirements and rejections](#submitting-reports-policy)
+ [Listing and pagination](#submitting-reports-listing)
+ [Retries and backoff](#submitting-reports-retries)

## The submission workflow
<a name="submitting-reports-workflow"></a>

1. Build a valid eXtended Abuse Reporting Format (XARF) report. See [Report format (XARF)](report-format.md).

1. Call `CreateAbuseReport` and receive `202 Accepted` with a report ID.

1. Persist the report ID and your `correlationId` so that you can track the report later.

1. Poll `GetAbuseReportStatus` to track the report, or enumerate your submissions with `ListAbuseReportStatuses`.

## Tracking status
<a name="submitting-reports-tracking"></a>

 `GetAbuseReportStatus` returns the current `status`, a human-readable `description`, and timestamps. When a report reaches the terminal `COMPLETED` status, it also carries a `reasonCode` describing the resolution outcome. Use `GetAbuseReportStatus` to read the current state for a given report ID.

A report progresses through the following states:

```
QUEUED -> PROCESSING -> COMPLETED
```


| Status | What it means | 
| --- | --- | 
|  `QUEUED`  | AWS has received your report and it is being queued for processing. Use the report ID to check the status of your report. | 
|  `QUEUED` (child sexual exploitation and abuse material reports) | AWS has received your report of suspected child sexual exploitation and abuse material.<br />Please also report this content directly to the National Center for Missing and Exploited Children’s (NCMEC) CyberTipline at the [CyberTipline website](https://report.cybertip.org/). Do not send images or copies of the material to AWS. | 
|  `PROCESSING`  | AWS has received your report and it is being processed. Use the report ID to check the status of your report. | 
|  `COMPLETED`  | The service processed the report successfully. The status also carries a `reasonCode` describing the resolution outcome. See [Resolution reason codes](#submitting-reports-reason-codes). | 

 `GetAbuseReportStatus` is a waitable operation. If your SDK supports waiters, use the `ReportProcessing` waiter. It polls until the report reaches `PROCESSING` or `COMPLETED`, because a report can move from `QUEUED` to `COMPLETED` before a poll observes `PROCESSING`. The waiter treats `ResourceNotFoundException` as a transient "not yet propagated" signal and retries, which is useful immediately after submission, when the status record might still be propagating. A successful wait confirms that the service has started processing the report, not that the report is resolved.

If you poll `GetAbuseReportStatus` yourself, wait 1–5 seconds between calls, retry on `ResourceNotFoundException`, and accept either `PROCESSING` or `COMPLETED`. `COMPLETED` is the only terminal status.

### Resolution reason codes
<a name="submitting-reports-reason-codes"></a>

A `COMPLETED` report carries a `reasonCode` that describes the resolution outcome:


| Reason code | What it means | 
| --- | --- | 
|  `ACTIONED`  | The content or activity you reported has been mitigated.<br />If you believe the reported content or activity persists, submit a new report containing the relevant URLs or most recent activity logs. | 
|  `NOT_RESOLVABLE_TO_AWS`  | AWS could not attribute the reported content or activity to AWS from the information provided.<br />If you’re able to provide additional information that may help us determine AWS as the origin, please submit a new report containing that information.<br />If no other information is available, you may use publicly available domain registration or network ownership information, including the [WHOIS website](https://www.whois.com/whois/) to identify and contact the relevant registrar or IP owner. | 
|  `REVIEWED_NO_AWS_ACTION`  | AWS has processed your report and isn’t taking further action at this time. If you have additional information, you can submit a new report that includes it. | 
|  `CONTENT_DOWN_OR_INACCESSIBLE`  | The reported content or activity was not accessible when AWS checked it. If it is accessible now, submit a new report with the current URL or activity logs, and say if it is visible only from certain locations or after signing in. | 
|  `NEED_MORE_INFORMATION`  | The report did not contain enough information to be processed. Required details vary by report type (for example, timestamps and IP/port data for activity reports, full headers for email spam, exact URLs for content reports).<br />Please submit a new report with as much information as possible. | 

## Idempotency in depth
<a name="submitting-reports-idempotency"></a>

Because `CreateAbuseReport` returns `202 Accepted` and the network can fail after the server has already accepted a report, retries are expected. Idempotency ensures that a retry does not create a duplicate. It works in one of two ways:
+  **Client-provided token (recommended).** Provide a `clientToken` (1–128 printable ASCII characters) that is unique per logical submission. Repeating the same token for the same principal returns the original report ID for 24 hours. This is the most predictable option and is recommended whenever your client can generate and remember a token.
+  **Auto-generated token (default).** If you omit `clientToken`, the service derives a token from a hash of the report payload and your principal, bucketed to a 5-minute window. Two identical payloads from the same principal within the same window collapse into one report. After the window, the service treats them as separate submissions.

**Important**  
Reusing a `clientToken` with a different payload returns `ConflictException` (HTTP 409) rather than silently overwriting or duplicating. Choose a new token whenever the report content changes.

## Correlation IDs
<a name="submitting-reports-correlation-ids"></a>

A `correlationId` (1–256 characters matching `^[a-zA-Z0-9-_]{1,256}$`) is your own reference for the submission. The service echoes it back in responses, and you can use it to filter results in `ListAbuseReportStatuses`. Correlation IDs are not unique keys. Multiple reports can share one, so use them to group related submissions (for example, all reports from a single incident).

## Submission requirements and rejections
<a name="submitting-reports-policy"></a>

A report can be rejected for two distinct reasons, and the HTTP status tells you which:
+  **Not well-formed** – The report fails the XARF schema or a field constraint. Returned as `ValidationException` (HTTP 400). Fix the structure or field values and resubmit.
+  **Well-formed but disallowed** – The report satisfies the schema but doesn’t meet a submission requirement. Returned as `SubmissionRequirementException` (HTTP 422). Retrying the same report does not succeed; you must change the report content.

A `SubmissionRequirementException` carries an `unmetRequirements` list. Each entry has a stable `code`, a `path` (a JSON Pointer to the offending member, or an empty string for the whole report), and a human-readable `message`. The service checks these requirements:


| Code | Applies to | What it means and how to fix | 
| --- | --- | --- | 
|  `rule.source_identifier.too_long`  |  `source_identifier`  | Longer than 253 bytes. This limit applies to every value, including URLs and IP addresses, and is checked before the format. If a URL exceeds the limit, supply only its hostname or IP address, and include the full URL in the report’s evidence. | 
|  `rule.source_identifier.forbidden_characters`  |  `source_identifier`  | Contains `{`, `}`, `*`, or a backtick, which are never valid in an address and are common in injection payloads. Remove them. | 
|  `rule.source_identifier.malformed`  |  `source_identifier`  | Not a valid IPv4 address, IPv6 address, URL, or domain name. Provide a well-formed identifier. | 
|  `rule.timestamp.unparseable`  |  `timestamp`  | Not a valid RFC 3339 date-time. Use a format such as `2026-09-22T12:00:00Z`. | 
|  `rule.timestamp.in_future`  |  `timestamp`  | Dated further ahead than the clock-skew tolerance (default 1 hour). Check the reporting host’s clock. | 
|  `rule.timestamp.too_old`  |  `timestamp`  | Earlier than the submission lookback window (default 90 days). For content that is still accessible, set the `timestamp` to the time you most recently observed it. | 
|  `rule.evidence.content_type_mismatch`  |  `evidence`  | The decoded `payload` of an evidence item doesn’t match its declared `content_type`. The entry’s `path` identifies the item, for example `/evidence/0`. Set `content_type` to the file’s actual type, or replace the payload with a file of the declared type. For the supported types, see [Embedded evidence](report-format.md#report-format-evidence). | 

## Listing and pagination
<a name="submitting-reports-listing"></a>

 `ListAbuseReportStatuses` returns up to `maxResults` items per page (1–50; a default page size applies when omitted). When more results exist, the response includes a `nextToken`. Pass it back on the next call to continue. You can also filter by `correlationId`. The service always scopes results to the caller’s own AWS account.

The following requests show the first and next pages. For a complete list request with authentication headers, see [Step 4: List your reports](getting-started.md#getting-started-step4).

```http
GET /v1/abusestatuses?maxResults=25 HTTP/1.1
Host: abuse.us-east-1.amazonaws.com
Authorization: AWS4-HMAC-SHA256 Credential=...
```

A successful call returns `200 OK` with a page of reports in the `reports` array. When more results exist, the response also includes a `nextToken`.

```json
{
  "reports": [
    {
      "reportId": "rpt01J5K9XMBN3QWERTY12345",
      "correlationId": "incident-2026-09-001",
      "status": "PROCESSING",
      "description": "Report has been received and is being processed."
    }
  ],
  "nextToken": "<token>"
}
```

To retrieve the next page, pass the token back in the `nextToken` query parameter:

```http
GET /v1/abusestatuses?maxResults=25&nextToken=<token> HTTP/1.1
Host: abuse.us-east-1.amazonaws.com
Authorization: AWS4-HMAC-SHA256 Credential=...
```

The pagination parameters are:
+  `maxResults` – The maximum number of reports to return per page (1–50).
+  `nextToken` – The pagination token returned by the previous call. Omit it on the first call.

## Retries and backoff
<a name="submitting-reports-retries"></a>
+ On `429 ThrottlingException` or `500 InternalServerException`, retry with exponential backoff and jitter, honoring the `Retry-After` header when present.
+ Always send the same `clientToken` on retries of the same logical submission so that the retry is idempotent.
+ Do not retry `400` (validation), `409` (conflict), or `422` (unmet submission requirement) without changing the request. These indicate a client-side issue to correct first.

For more information about the per-operation rate limits, see [Quotas for AWS Abuse Signal API](quotas.md).