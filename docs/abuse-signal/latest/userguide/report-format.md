

# Report format (XARF)

With AWS Abuse Signal API, you can submit reports in XARF (eXtended Abuse Reporting Format), an open, machine-readable standard for abuse reports. For more information, see [XARF on the XARF website](https://xarf.org/docs/introduction/). You submit the XARF object under the `report.xarf` key of a `CreateAbuseReport` request.

**Note**  
This page summarizes how the API consumes XARF. The authoritative definition of every field and report type is the XARF specification. The API validates submissions against the XARF v4 JSON Schema.

**Topics**
+ [Version support and conversion](#report-format-versions)
+ [Report structure](#report-format-structure)
+ [Embedded evidence](#report-format-evidence)
+ [Tagging test submissions](#report-format-tags)
+ [Validation failures](#report-format-validation)

## Version support and conversion
<a name="report-format-versions"></a>

The service validates against XARF v4. If you submit a v3 report, the service automatically converts it to v4 before validation, so existing v3 producers continue to work. New integrations should emit v4 directly.

## Report structure
<a name="report-format-structure"></a>

Every report declares a `category` and a `type` and includes reporter and sender details, a source identifier, and a timestamp. The exact required and recommended fields depend on the report type. A minimal content/phishing report looks like the following:

```json
{
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
  "url": "https://example.com/login"
}
```

**Note**  
The `report_id` field inside the XARF document is the reporter’s own identifier for the report. It is distinct from the `reportId` that the API returns, which is the AWS-assigned identifier you use to track processing status.

## Embedded evidence
<a name="report-format-evidence"></a>

**Important**  
Never include images, video, or copies of child sexual abuse or child sexual exploitation material in a report, in any field and for any report type. Send URLs, hash values, and reference identifiers only.

A report can include an `evidence` array. Each evidence item carries a declared `content_type`, an optional `description`, a base64-encoded `payload`, and an optional `hash`. The service validates evidence as follows:
+ The service base64-decodes and MIME-parses the payload.
+ The service verifies the declared `content_type` against the actual decoded bytes (content-type sniffing) and rejects a mismatch.
+ If you declare a `hash`, use the format `algorithm:hexvalue`, where `algorithm` is `sha256`, `sha1`, or `md5` (for example, `sha256:9f86d081…​`). The service computes the digest of the decoded payload and rejects the evidence item if the hash doesn’t match, the algorithm isn’t supported, or the hex value is malformed. This follows the XARF hash convention; for the full evidence schema, see [the XARF v4 specification on the XARF website](https://xarf.org/docs/specification/).

The service accepts the following `content_type` values. The declared type must match the decoded bytes; any other value, or a value that is not a valid MIME type, is rejected.


| Content type | Accepted when | 
| --- | --- | 
|  `text/plain`  | The payload is valid UTF-8. | 
|  `application/json`  | The payload parses as JSON. | 
|  `application/xml`  | The payload is valid UTF-8 and its first non-whitespace character is `<`. | 
|  `text/html`  | The payload is valid UTF-8 and its first non-whitespace character is `<`. | 
|  `application/rtf` (or `text/rtf`) | The payload begins with the RTF magic number. | 
|  `image/png`  | The payload has the PNG magic number and ends with the `IEND` marker. | 
|  `image/jpeg`  | The payload begins with the JPEG start-of-image marker. | 
|  `application/pdf`  | The payload begins with `%PDF-` and ends with `%%EOF`. | 

Regardless of the declared `content_type`, the service rejects any payload that contains a ZIP archive (reported as `application/zip`). An archive appended to an otherwise-allowed file would bypass the content-type check, so the service blocks it.

Evidence is subject to the following size limits:


| Limit | Value | 
| --- | --- | 
| Maximum decoded size per evidence item | 5 MB | 
| Maximum evidence items per report | 50 | 
| Maximum total request payload size | 5 MB | 

**Important**  
A single `CreateAbuseReport` request must not exceed 5 MB in total size. Because evidence is base64-encoded in the request body (which adds roughly 33 percent overhead), keep the combined size of your report and any embedded evidence within this limit. Reference large artifacts (for example, by URL or hash) rather than embedding them.

## Tagging test submissions
<a name="report-format-tags"></a>

Use the XARF `tags` array with the `lifecycle:test` tag to mark non-production submissions that you send while testing your integration:


| Tag | Use for | 
| --- | --- | 
|  `lifecycle:test`  | Test submissions sent while developing or validating your integration. | 

Reports with the `lifecycle:test` tag are for testing the API and are not processed as abuse reports. The service deletes them shortly after submission. This `lifecycle:` convention is specific to AWS Abuse Signal API and is not part of the XARF standard. Any untagged reports will be processed as live submissions.

**Note**  
The `aws:` tag namespace is reserved for use by AWS. If you include any tag that begins with the `aws:` prefix, the service strips it from your report during processing. Use your own tag names outside the reserved `aws:` namespace, and don’t rely on `aws:`-prefixed tags.

## Validation failures
<a name="report-format-validation"></a>

If a report fails schema or evidence validation, the API returns `ValidationException` (HTTP 400) with a `fieldList` that names each failing field (as a JSON path) and the reason. Correct the flagged fields and resubmit.

Reports that are well-formed but don’t meet a submission requirement return `SubmissionRequirementException` (HTTP 422) instead. For more information, see [Submission requirements and rejections](submitting-reports.md#submitting-reports-policy).