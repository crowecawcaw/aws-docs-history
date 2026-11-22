

# Quotas for AWS Abuse Signal API

Your AWS account has default quotas, formerly referred to as limits, for AWS Abuse Signal API. Unless otherwise noted, AWS enforces each quota per account. For the quotas in a single table, see [AWS Abuse Signal API endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/abuse-signal.html#abuse-signal_quotas) in the *AWS General Reference*.

**Topics**
+ [Request rate quotas](#quotas-throttling)
+ [Report and evidence size limits](#quotas-evidence)
+ [Requesting a quota increase](#quotas-increase)

## Request rate quotas
<a name="quotas-throttling"></a>

The API enforces per-account request rate limits. When you exceed your rate, the service returns `ThrottlingException` (HTTP 429) with a `Retry-After` header that advises when to retry. The default per-operation limits, measured in transactions per second (TPS), are as follows.


| Operation | Sustained (TPS per account) | Burst | Adjustable | 
| --- | --- | --- | --- | 
|  `CreateAbuseReport`  | 10 | 100 | Yes | 
|  `GetAbuseReportStatus`  | 50 | 100 | Yes | 
|  `ListAbuseReportStatuses`  | 10 | 50 | Yes | 

Use exponential backoff with jitter and honor the `Retry-After` header. The service keys throttling to your AWS account and the operation, so limits apply per account per operation. For retry guidance, see [Retries and backoff](submitting-reports.md#submitting-reports-retries).

## Report and evidence size limits
<a name="quotas-evidence"></a>

The following table lists the size limits for a single `CreateAbuseReport` request, including any embedded evidence.


| Limit | Value | 
| --- | --- | 
| Maximum decoded size per evidence item | 5 MB | 
| Maximum evidence items per report | 50 | 
| Maximum total request payload size | 5 MB | 

For more about embedded evidence, see [Embedded evidence](report-format.md#report-format-evidence).

## Requesting a quota increase
<a name="quotas-increase"></a>

AWS Abuse Signal API isn’t available in Service Quotas. To request an increase to an adjustable quota, create a [service quota increase case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase) in the AWS Support Center Console.