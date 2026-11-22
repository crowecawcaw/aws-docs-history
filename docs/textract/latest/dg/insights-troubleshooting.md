

# Troubleshooting

This page lists the API error responses Amazon Textract Insights returns and the common configuration pitfalls that cause them, with how to fix each.

## API error responses
<a name="insights-troubleshooting-errors"></a>

All APIs return standard AWS error responses. Which errors each operation can return is listed with that operation in the Amazon Textract Insights API Reference.


**API error responses**  

| **Error** | **Cause** | **Retry?** | 
| --- | --- | --- | 
| `ValidationException` | Invalid input, such as a schema that fails validation, a reused `ClientRequestToken` with different parameters, or deleting a blueprint that still has versions or is referenced by a project. Includes field-level details for schema errors. | No. Fix the request. | 
| `InvalidParameterException` | A parameter is malformed, such as a badly formed ARN, or a `ClientRequestToken` longer than 64 characters or containing characters other than letters, numbers, hyphens, and underscores. | No. Fix the request. | 
| `ResourceNotFoundException` | The project or blueprint does not exist. | No. | 
| `InvalidJobIdException` | `GetDocumentInsights` only. The job ARN is well formed but no such job exists. | No. | 
| `AccessDeniedException` | Insufficient permissions, or the resource belongs to another account. | No. | 
| `ConflictException` | A project or blueprint with that name already exists, or a concurrent update to the same resource conflicted. | For a concurrent update, yes. Re-read the resource, then retry. | 
| `LimitExceededException` | An account quota was reached, such as projects or blueprints per account, versions per blueprint, or concurrent jobs. | For concurrent jobs, retry after running jobs finish. The more pages you submit at once, the longer all jobs take. If you need more throughput, request a quota increase. | 
| `ServiceQuotaExceededException` | Tagging APIs only. The tag quota for the resource was reached. | No. | 
| `ThrottlingException` | Tagging APIs only. The request rate was too high. | Yes, with exponential backoff. | 
| `ProvisionedThroughputExceededException` | The request rate exceeded your throughput quota. | Yes, with exponential backoff. | 
| `InternalServerError` | Service error. | Yes, with exponential backoff. | 

When a job completes with `Status` `FAILED`, read `ErrorType` and `ErrorMessage` from `GetDocumentInsights` for the cause.

## Common pitfalls
<a name="insights-troubleshooting-pitfalls"></a>

The following configuration mistakes are common causes of the errors in the preceding table.

### Missing ExtractionConfiguration fields
<a name="insights-troubleshooting-extraction-config"></a>

`ExtractionConfiguration` is required on `CreateProject`, and it must include `BoundingBox`, a non-empty `Granularity.Types` list, and `OutputFormat`. Omitting any of them, or passing an empty `Granularity.Types`, fails with `ValidationException`. To keep extraction minimal when you only need custom extraction, pass:

```json
{"BoundingBox": {"State": "DISABLED"}, "Granularity": {"Types": ["PAGE"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}
```

Also note that on `UpdateProject`, a configuration block you include is replaced in full, so an included `ExtractionConfiguration` must still contain `BoundingBox`, `Granularity`, and `OutputFormat`.

### Inline object schema rejection
<a name="insights-troubleshooting-inline-object"></a>

In a blueprint schema, define tables and nested structures with `$defs` and `$ref`. An inline `type: object` is rejected with `ValidationException` ("Blueprint has invalid schema"). See [Blueprint schemas](insights-blueprint-schemas.md).

### Job fails with PageLimitExceeded or DocumentTooLargeException
<a name="insights-troubleshooting-page-limit"></a>

Page limits are checked after the job starts, so `StartDocumentInsights` succeeds and the job ends `FAILED`. Check `ErrorType`:
+ `PageLimitExceeded`. The file has more pages than the service accepts. Split the file before you submit it.
+ `DocumentTooLargeException` ("The input document size is too large to process."). Despite the wording, this error can come from a page-count limit rather than file size. For example, either custom extraction ran without splitting on a file over the no-splitting page limit, or figure captioning was enabled on a file over the figure-captioning page limit. Both return the same message. If the job used custom extraction without splitting, enable `SplitterConfiguration` first, because that limit is lower. If the error persists, turn off figure captioning or submit a shorter file.

For the page limits, see [Limits and quotas](insights-quotas.md).

### Bucket AWS Region mismatch
<a name="insights-troubleshooting-bucket-region"></a>

The input and output Amazon S3 buckets must be in the same AWS Region as the request. A bucket in another AWS Region causes the job to fail. Confirm the buckets and the `--region` you call with all match.

### Reading OutputConfiguration as a folder instead of job\_metadata.json
<a name="insights-troubleshooting-output-folder"></a>

On `SUCCEEDED`, `OutputConfiguration.S3Uri` points directly at the job's `job_metadata.json` file, not at a folder you have to list. Read that file first and follow its `extraction_path` and `custom_path` entries to each `result.json`, rather than enumerating Amazon S3 keys yourself. See [Output location and file structure](insights-output-location.md).

### Over-masking with PII detection
<a name="insights-troubleshooting-over-masking"></a>

Setting `PiiEntityTypes` to `ALL` can over-mask form boilerplate and unlabeled values. Narrow the list to the types you need, and validate redaction on representative documents. See [Detecting and redacting sensitive data](insights-detecting-redacting.md).

### Supplying ProjectArn and Blueprints
<a name="insights-troubleshooting-project-blueprints"></a>

`StartDocumentInsights` takes exactly one of `--project-arn` or `--blueprints`. Supplying neither returns `ValidationException`: Either `ProjectArn` or `Blueprints` must be provided. Inline blueprints produce custom extraction results only. See [Running jobs with inline blueprints](insights-inline-blueprints.md).

### Unsupported input type
<a name="insights-troubleshooting-input-type"></a>

Supported input file types are PDF, PNG, JPEG, and TIFF. See [Limits and quotas](insights-quotas.md).