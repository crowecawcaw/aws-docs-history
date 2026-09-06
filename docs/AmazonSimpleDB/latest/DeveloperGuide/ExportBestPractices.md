

# Best Practices for Domain Exports
<a name="ExportBestPractices"></a>

 Consider these best practices to ensure successful exports and efficient use of the export feature. 

## Plan for Asynchronous Processing
<a name="AsynchronousProcessing"></a>

 Domain exports are designed for migration and archival use cases, not real-time data access. Exports run asynchronously and may take time to complete depending on the size of your domain. Check the export status regularly using the `get-export` command rather than expecting immediate completion. 

## Consider Domain Lifecycle Management
<a name="DomainLifecycle"></a>

 Domain deletion is blocked while any export for that domain is in PENDING or IN\_PROGRESS status. If you plan to delete a domain, ensure all exports have completed (SUCCEEDED or FAILED status) before attempting deletion. You can use the `list-exports` command with a domain filter to check for active exports. 

## Understand Export Strategy
<a name="ExportStrategy"></a>

 All exports are full, non-incremental snapshots of your domain data. Every export contains the complete dataset, not just changes since the last export. Plan your export frequency accordingly, considering both storage costs and the time required to process full exports. 

## Stay Within Rate Quotas
<a name="RateQuotas"></a>

 Amazon SimpleDB enforces the following rate quotas for export operations: 
+  5 exports per domain within a rolling 24-hour window 
+  25 exports per AWS account within a rolling 24-hour window 

 Plan your export schedule to stay within these limits. If you need to export multiple domains, distribute the exports over time to avoid hitting the account-level quota. 

## Manage Cost Considerations
<a name="CostConsiderations"></a>

 Amazon SimpleDB does not charge for export operations, but Amazon S3 costs apply to the exported data: 
+  **Storage costs** - You pay for storing the exported data in Amazon S3 according to standard Amazon S3 pricing. 
+  **API call costs** - Amazon S3 charges for PUT requests made during the export process. 
+  **Data transfer costs** - Standard Amazon S3 data transfer pricing applies, especially for cross-Region exports. 

 The JSON format adds metadata overhead, so exported data size is larger than the raw Amazon SimpleDB data size. A domain approaching the 10 GB limit may export to well over 10 GB in Amazon S3. Repeated full exports can accumulate storage costs quickly, so consider implementing a lifecycle policy to archive or delete old exports. 

 For more information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/). 

## Follow Security Best Practices
<a name="SecurityBestPractices"></a>

 Exported data in Amazon S3 should be protected using the same security measures you apply to other sensitive data: 
+  Enable default encryption on your Amazon S3 bucket using SSE-S3 or SSE-KMS 
+  Configure bucket policies to restrict access to authorized users and services 
+  Enable Amazon S3 bucket versioning to protect against accidental deletion 
+  Use Amazon S3 access logging to track access to exported data 
+  Apply least-privilege IAM policies for users and roles that access exported data 

 For more information about Amazon S3 security, see [ Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) in the *Amazon S3 User Guide*. 

## Verify Data Integrity
<a name="DataIntegrityVerification"></a>

 After an export completes, verify the integrity and completeness of the exported data: 
+  Check the `totalItemCount` in `manifest-summary.json` against the expected number of items in your domain 
+  Verify the MD5 checksums in `manifest-file.json` for each data file after downloading 
+  Confirm that the sum of `dataFileItemCount` values in `manifest-file.json` matches the `totalItemCount` 

 These verification steps ensure that the export completed successfully and that no data was corrupted during the export or transfer process. 

## Handle Export Failures
<a name="FailureHandling"></a>

 If an export fails, Amazon SimpleDB does not automatically clean up partial data that may have been written to your Amazon S3 bucket. You are responsible for manually cleaning up any partial export data to avoid unnecessary storage costs. 

 When an export fails: 

1.  Use the `get-export` command to retrieve the `failureCode` and `failureMessage` 

1.  Address the underlying issue (such as insufficient permissions or bucket access problems) 

1.  Check your Amazon S3 bucket for partial export data and delete it if present 

1.  Start a new export after resolving the issue 