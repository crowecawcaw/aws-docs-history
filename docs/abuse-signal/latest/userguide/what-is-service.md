

# What is AWS Abuse Signal API?

The AWS Abuse Signal API is a programmatic interface that allows AWS customers, security researchers, and partner organizations to submit and track reports of suspected abuse of AWS resources.

You submit reports in the eXtended Abuse Reporting Format (XARF), an open standard for structured abuse reporting. For more information, see [XARF on the XARF website](https://xarf.org/docs/introduction/). Reports can cover a wide range of abuse categories, including spam, phishing, distributed denial of service (DDoS), malware distribution, and copyright infringement.

With the AWS Abuse Signal API, you can:
+  **Submit abuse reports** – Create structured abuse reports by using the XARF format, with full support for all XARF v4 report types.
+  **Track report status** – Monitor the processing status of submitted reports, from submission through resolution.
+  **List and filter reports** – Retrieve the status of all reports, with optional filtering by correlation ID.
+  **Retry submissions safely** – Safely retry report submissions without creating duplicates by using client tokens.

To use AWS Abuse Signal API, you need an AWS account and AWS Identity and Access Management (IAM) permissions for the `abuse:CreateAbuseReport`, `abuse:GetAbuseReportStatus`, and `abuse:ListAbuseReportStatuses` actions. For account and permission setup, see [Setting up AWS Abuse Signal API](setting-up.md). The service provides only a programmatic REST/JSON API and has no console, so you must sign HTTP requests with SigV4 or SigV4a, or use an AWS SDK or the AWS Command Line Interface (AWS CLI) that signs requests for you.

AWS Abuse Signal API has the following key characteristics:
+ Three public operations: `CreateAbuseReport`, `GetAbuseReportStatus`, and `ListAbuseReportStatuses` 
+ REST/JSON over HTTPS, authenticated with AWS Signature Version 4 (SigV4) or Signature Version 4A (SigV4a)

For the complete reference of operations, parameters, and errors, see the [AWS Abuse Signal API Reference](https://docs.aws.amazon.com/abuse-signal/latest/APIReference/).

**Topics**
+ [Are you a first-time AWS Abuse Signal API user?](#first-time-user)
+ [Features of AWS Abuse Signal API](#servicename-feature-overview)
+ [How AWS Abuse Signal API works](#how-it-works)
+ [What happens after you submit a report](#what-happens-after-submit)
+ [Your responsibilities](#your-responsibilities)
+ [Pricing for AWS Abuse Signal API](#pricing)
+ [Accessing AWS Abuse Signal API](#acessing-servicename)

## Are you a first-time AWS Abuse Signal API user?
<a name="first-time-user"></a>

If you are a first-time user of AWS Abuse Signal API, we recommend that you begin by reading the following sections:
+  [Getting started with AWS Abuse Signal API](getting-started.md) – Submit your first abuse report and track it to completion.
+  [Report format (XARF)](report-format.md) – Learn how the API consumes XARF reports.
+  [Submitting reports](submitting-reports.md) – Understand idempotency, status tracking, submission requirements, and retries.
+  [Regions and endpoints](regions-endpoints.md) – Choose an AWS Region and the endpoint to call.

## Features of AWS Abuse Signal API
<a name="servicename-feature-overview"></a>

AWS Abuse Signal API provides the following features:
+  **Standardized reporting** – Submit abuse reports in XARF, an open, machine-readable format. The service validates against the XARF v4 specification and automatically converts v3 reports to v4.
+  **Report ID on receipt** – When AWS receives your report, the API returns `HTTP 202 Accepted` and a report ID. This response confirms receipt only.
+  **Deduplicated, idempotent submissions** – Use a client-provided token or an auto-generated token derived from the payload so that your safe retries never create duplicate reports.
+  **Status tracking** – Track a report through its lifecycle (`QUEUED`, `PROCESSING`, `COMPLETED`) and read a high-level resolution reason code when it completes.
+  **Embedded evidence** – Attach base64-encoded evidence to substantiate a report, within defined size limits.
+  **Private connectivity** – Reach the API over the public internet or privately from your virtual private cloud (VPC) with AWS PrivateLink, using the same endpoint names.

## How AWS Abuse Signal API works
<a name="how-it-works"></a>

AWS Abuse Signal API uses a five-step workflow to handle abuse reports:

1.  **Submit a report.** Call `CreateAbuseReport` with a report in XARF format.

1.  **AWS checks the report.** If the report doesn’t meet the submission requirements, the API returns an error that explains what to fix.

1.  **AWS returns a report ID.** A successful response confirms that AWS received your report. If you retry with the same client token, the API returns the original report ID and doesn’t create a duplicate.

1.  **Check the status.** Use `GetAbuseReportStatus` or `ListAbuseReportStatuses` with the report ID. The status can be seen as `QUEUED` (received), `PROCESSING` (being processed), or `COMPLETED` (processed to completion).

1.  **Read the outcome.** When the report has been processed to completion, the status shows as `COMPLETED` and includes a reason code explaining the resolution. See [Resolution reason codes](submitting-reports.md#submitting-reports-reason-codes).

AWS Trust & Safety processes each report and decides how to respond, outside the API.

## What happens after you submit a report
<a name="what-happens-after-submit"></a>

AWS Trust & Safety handles reports submitted through the API under its standard abuse handling processes and policies. AWS customers are responsible for the content they host and the activities they conduct using AWS services. Many reports are resolved by the customer removing or disabling the reported content or activity. Where a customer is unable or unwilling to address prohibited content or activity, AWS may take suspension action to mitigate the abuse, with notice to the customer in accordance with the customer’s agreement with AWS. AWS doesn’t disclose customer information to reporters.

## Your responsibilities
<a name="your-responsibilities"></a>
+  **Submit well-formed XARF.** Conform to the XARF v4 schema and the evidence size limits so that reports pass validation.
+  **Sign requests correctly.** Use SigV4 or SigV4a with the `abuse` signing name, and maintain IAM permissions for the actions you call.
+  **Handle throttling and retries.** Use idempotency tokens for safe retries, back off on `429`, and honor the `Retry-After` header.
+  **Tag test traffic.** Use `lifecycle:test` for non-production submissions.
+  **Track by report ID.** Persist the returned report ID (and your own correlation ID) so that you can query status later.
+  **Protect sensitive data.** Include only the evidence necessary to substantiate a report.

## Pricing for AWS Abuse Signal API
<a name="pricing"></a>

AWS Abuse Signal API charges no additional fee, so you can submit and track abuse reports at no cost.

## Accessing AWS Abuse Signal API
<a name="acessing-servicename"></a>

You access AWS Abuse Signal API programmatically through its REST/JSON API over HTTPS. Sign every request with SigV4 or SigV4a using the `abuse` signing name. Most AWS SDKs and the AWS Command Line Interface (AWS CLI) sign requests for you. For the endpoint names to use in each Region, see [Regions and endpoints](regions-endpoints.md). For operation and parameter details, see the [AWS Abuse Signal API Reference](https://docs.aws.amazon.com/abuse-signal/latest/APIReference/).