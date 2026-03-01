# Find query output files in Amazon S3

Query output files are stored in sub-folders on Amazon S3 in the following path pattern
unless the query occurs in a workgroup whose configuration overrides client-side
settings. When workgroup configuration overrides client-side settings, the query uses
the results path specified by the workgroup.

```
`QueryResultsLocationInS3`/[`QueryName`|Unsaved`/yyyy/mm/dd`/]
```

- `QueryResultsLocationInS3` is the query result
  location specified either by workgroup settings or client-side settings. For
  more information, see [Specify a query result location](query-results-specify-location.md "query-results-specify-location.md") later in
  this document.
- The following sub-folders are created only for queries run from the console
  whose results path has not been overriden by workgroup configuration. Queries
  that run from the AWS CLI or using the Athena API are saved directly to the
  `QueryResultsLocationInS3`.

      + `QueryName` is the name of the query for
       which the results are saved. If the query ran but wasn't saved,
       `Unsaved` is used.
      + `yyyy/mm/dd` is the date that the query
       ran.

  Files associated with a `CREATE TABLE AS SELECT` query are stored in a
  `tables` sub-folder of the above pattern.

## Identify query output files

Files are saved to the query result location in Amazon S3 based on the name of the
query, the query ID, and the date that the query ran. Files for each query are named
using the `QueryID`, which is a unique identifier that
Athena assigns to each query when it runs.

The following file types are saved:

| File type                | File naming patterns                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Query results files**  | ``QueryID`.csv`<br>``QueryID`.txt`                   | DML query results files are saved in comma-separated values<br>(CSV) format.<br>DDL query results are saved as plain text files.<br>You can download results files from the console from the<br>**Results\*<br>• pane when using the console or<br>from the query **History\*\*. For more<br>information, see [Download query results files using the Athena console](saving-query-results.md "saving-query-results.md"). |
| **Query metadata files** | ``QueryID`.csv.metadata`<br>``QueryID`.txt.metadata` | DML and DDL query metadata files are saved in binary format<br>and are not human readable. The file extension corresponds to<br>the related query results file. Athena uses the metadata when<br>reading query results using the `GetQueryResults`<br>action. Although these files can be deleted, we do not recommend<br>it because important information about the query is lost.                                       |
| **Data manifest files**  | ``QueryID`-manifest.csv`                             | Data manifest files are generated to track files that Athena<br>creates in Amazon S3 data source locations when an [INSERT INTO](insert-into.md "insert-into.md") query<br>runs. If a query fails, the manifest also tracks files that the<br>query intended to write. The manifest is useful for identifying<br>orphaned files resulting from a failed query.                                                            |

To use the AWS CLI to identify the query output location and result files, run
the `aws athena get-query-execution` command, as in the following
example. Replace `abc1234d-5efg-67hi-jklm-89n0op12qr34`
with the query ID.

```
aws athena get-query-execution --query-execution-id `abc1234d-5efg-67hi-jklm-89n0op12qr34`
```

The command returns output similar to the following. For descriptions of each
output parameter, see [get-query-execution](../../../cli/latest/reference/athena/get-query-execution.md "../../../cli/latest/reference/athena/get-query-execution.md") in the
_AWS CLI Command Reference_.

```
{
    "QueryExecution": {
        "Status": {
            "SubmissionDateTime": 1565649050.175,
            "State": "SUCCEEDED",
            "CompletionDateTime": 1565649056.6229999
        },
        "Statistics": {
            "DataScannedInBytes": 5944497,
            "DataManifestLocation": "s3://amzn-s3-demo-bucket/athena-query-results-123456789012-us-west-1/MyInsertQuery/2019/08/12/abc1234d-5efg-67hi-jklm-89n0op12qr34-manifest.csv",
            "EngineExecutionTimeInMillis": 5209
        },
        "ResultConfiguration": {
            "EncryptionConfiguration": {
                "EncryptionOption": "SSE_S3"
            },
            "OutputLocation": "s3://amzn-s3-demo-bucket/athena-query-results-123456789012-us-west-1/MyInsertQuery/2019/08/12/abc1234d-5efg-67hi-jklm-89n0op12qr34"
        },
        "QueryExecutionId": "abc1234d-5efg-67hi-jklm-89n0op12qr34",
        "QueryExecutionContext": {},
        "Query": "INSERT INTO mydb.elb_log_backup SELECT * FROM mydb.elb_logs LIMIT 100",
        "StatementType": "DML",
        "WorkGroup": "primary"
    }
}

```
