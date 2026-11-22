

# Error codes for protected queries and jobs in AWS Clean Rooms

When a protected query or protected job fails, AWS Clean Rooms returns an error code. The code identifies the kind of failure. AWS Clean Rooms also returns a signal that indicates whether running the same request again might succeed.

Use the error code to handle failures in your application. The error code stays the same even if the wording of the error message changes.

You can find the error code in the following places:
+ The `error` object in the [GetProtectedQuery](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetProtectedQuery.html) and [GetProtectedJob](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetProtectedJob.html) responses. The `retryable` field in the `retry` object indicates whether running the same request again might succeed.
+ The `errorCode` field in the analysis log that AWS Clean Rooms delivers when the analysis finishes. For more information, see [Analysis logging in AWS Clean Rooms](query-logs.md).

The `errorMessage` field contains more detail about the specific failure.

The following table lists the error codes for protected queries and jobs, whether each is retryable, and what to do next. The Retryable column shows the `retryable` value. No (`false`) means that running the same request again, unchanged, isn't expected to succeed. You might still run the analysis again after you act on the error.


| Error code | Meaning | Retryable | Action | 
| --- | --- | --- | --- | 
| `MALFORMED_QUERY` | The query is not valid, such as a syntax error or an unsupported operation. | No | Fix the query, and then run the analysis again. | 
| `MALFORMED_SCRIPT` | The user script or its environment is not valid, such as a code error or a missing dependency. | No | Fix the user script, and then run the analysis again. | 
| `RESOURCE_NOT_FOUND` | A referenced resource doesn't exist. | No | Verify that the resource exists, or correct the reference. Then run the analysis again. | 
| `INVALID_RESOURCE` | A referenced resource exists, but you can't use it because its configuration, state, or data is not valid. | No | Fix the resource, and then run the analysis again. | 
| `RESOURCE_ACCESS_DENIED` | A required permission is missing for a data source or resource. | No | Grant the permission, and then run the analysis again. | 
| `INSUFFICIENT_COMPUTE` | The query or job exceeded the available compute (memory, disk, or time). | No | Try one or more of the following, and then run the analysis again:+  Reduce what the analysis processes, for example by using fewer joins or more selective filters. <br />+  Tune the Spark memory and parallelism properties for your analysis. For the properties that you can set, see [Querying configured tables using a SQL analysis template](use-analysis-template.md) and [Running a PySpark job on a configured table using a PySpark analysis template](run-jobs-with-analysis-template.md). For a SQL query, you can export its logs, analyze the failure, and then adjust properties to address the issue. For more information, see [Exporting query analysis logs](export-analysis-logs.md). <br />+  Use a larger worker type, more workers, or both.  | 
| `TRANSIENT_ERROR` | A temporary condition caused the failure, such as throttling or a network interruption. | Yes | Retry the analysis. If the issue persists, contact Support. | 
| `INTERNAL_ERROR` | AWS Clean Rooms encountered an unexpected error. | No | If the error persists, contact Support. | 
| `UNKNOWN_ERROR` | AWS Clean Rooms couldn't classify the failure. | No | If the error persists, contact Support. | 

For more information about running analyses, see [Running SQL queries](running-sql-queries.md) and [Running PySpark jobs](run-jobs.md).