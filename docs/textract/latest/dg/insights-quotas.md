

# Limits and quotas

Amazon Textract Insights has two kinds of limits:
+ **Quotas** are per-account, per-Region defaults. You can request an increase through Service Quotas.
+ **Limits** are fixed by the service and cannot be raised. A request that exceeds a request limit, such as a name length or the number of blueprints, is rejected. A document that exceeds a page limit is accepted, and the job then fails (see [Troubleshooting](insights-troubleshooting.md)).

## Quotas (adjustable)
<a name="insights-quotas-adjustable"></a>

The following quotas are per-account, per-Region defaults. You can request an increase for a quota through Service Quotas.


**Adjustable quotas**  

| **Quota** | **Default** | 
| --- | --- | 
| `StartDocumentInsights` requests per second | 10 | 
| `GetDocumentInsights` requests per second | 10 | 
| Concurrent extraction jobs | 20 | 
| Concurrent generative jobs | 20 | 
| Concurrent custom jobs | 20 | 
| Figures captioned per page | 5 | 
| Projects per account | 100 | 
| Blueprints per account | 350 | 
| Versions per blueprint | 10 | 

A job counts against its concurrent-job quota until it reaches a terminal status (`SUCCEEDED` or `FAILED`).

## Limits (fixed)
<a name="insights-quotas-limits"></a>

The following limits are fixed by the service and cannot be raised.

### Documents
<a name="insights-quotas-limits-documents"></a>

The following limits apply to each input document.


**Document limits**  

| **Limit** | **Value** | 
| --- | --- | 
| Supported file types | PDF, PNG, JPEG, TIFF. (DOC and DOCX are not supported.) | 
| Maximum file size | 500 MB | 
| Pages per document insights job | 3,000 | 
| Pages per document for custom extraction without splitting (`SplitterConfiguration` not enabled) | 20 | 
| Pages per document with figure captioning enabled (`GenerativeConfiguration.FigureCaption.State` is `ENABLED`) | 1,500 | 

### When a document exceeds a page limit
<a name="insights-quotas-page-limit-exceeded"></a>

Page limits are checked after the job starts, so `StartDocumentInsights` still returns a job ARN. The job then ends with `Status` `FAILED`, and `GetDocumentInsights` reports the cause in `ErrorType`:
+ More pages than the **Pages per document** limit: `PageLimitExceeded`, with `ErrorMessage` "The number of pages in the input document is too high."
+ Custom extraction without splitting on a file over its page limit: `DocumentTooLargeException`, with `ErrorMessage` "The input document size is too large to process."
+ Figure captioning enabled on a file over its page limit: `DocumentTooLargeException`, with the same `ErrorMessage`.

The two `DocumentTooLargeException` cases return the same message. To tell them apart, compare the file's page count with each limit and check which features the job had enabled.

Document summarization does not have its own page limit. Only the overall **Pages per document** limit applies.

To run custom extraction on a file longer than 20 pages, enable splitting so the file is divided into individual documents before blueprints are applied. For more information, see [Splitting multi-document files](insights-splitting.md).

### Projects and blueprints
<a name="insights-quotas-limits-projects"></a>

The following limits apply to projects and blueprints.


**Project and blueprint limits**  

| **Limit** | **Value** | 
| --- | --- | 
| Blueprints per project | 40 | 
| Blueprints per job when passed inline | 10 | 
| `FallbackBlueprints` entries per project | 1 | 
| Blueprint schema size | 100,000 characters | 
| Leaf fields per blueprint | 100 | 
| List leaf fields per blueprint | 30 | 
| Field name and custom type name | 1–60 characters; can't contain `/` | 
| Field description | Up to 600 characters | 
| `ProjectName`, `BlueprintName` | 1–128 characters, `[a-zA-Z0-9-_]+` | 
| `ProjectDescription` | Up to 300 characters | 

For blueprint structure rules (nesting, lists, enum), see [Blueprint schema best practice](insights-blueprint-schema-best-practice.md).

### Requests and tags
<a name="insights-quotas-limits-requests"></a>

The following limits apply to request tokens and resource tags.


**Request and tag limits**  

| **Limit** | **Value** | 
| --- | --- | 
| `ClientRequestToken` | 1–64 characters, `[a-zA-Z0-9-_]+` | 
| Tags per resource | 50 | 
| Tag key | 1–128 characters; can't begin with `aws:` | 
| Tag value | 0–256 characters | 

## Requesting a quota increase
<a name="insights-quotas-increase"></a>

Request an increase in Service Quotas for the specific quota and AWS Region you need. Limits in the "Limits (fixed)" section cannot be raised.