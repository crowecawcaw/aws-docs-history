# Batch load

Neptune Analytics supports a `CALL` procedure `neptune.load` to load data from Amazon S3, to insert new vertices,
edges, and properties, or to update single cardinality vertex property values. It executes as a mutation query and does
atomic writes. It uses the IAM credentials of the caller to access the data in Amazon S3. See
[Create your IAM role for Amazon S3 access](bulk-import-create-from-s3.md#create-iam-role-for-s3-access "bulk-import-create-from-s3.md#create-iam-role-for-s3-access") to set up the permissions.

## Request syntax

The signature of the `CALL` procedure is shown below:

```
CALL neptune.load(
  {
    source: "string",
    region: "us-east-1",
    format: "csv",
    failOnError: true,
    concurrency: 1
  }
)
```

- **source** (required) – An Amazon S3 URI prefix. All object names with matching
  prefixes are loaded. See [Neptune Database loader reference](../../../neptune/latest/userguide/load-api-reference-load.md#load-api-reference-load-parameters "../../../neptune/latest/userguide/load-api-reference-load.md#load-api-reference-load-parameters") for Amazon S3 URI prefix examples. The IAM user who signs the openCypher
  request must have permissions to list and download these objects, and must be authorized for
  `WriteDataViaQuery` and `DeleteDataViaQuery` actions. See
  [IAM role mapping](query-APIs-IAM-role-mappings.md "query-APIs-IAM-role-mappings.md") for more IAM authentication related details.
- **region** (required) – The AWS region where the Amazon S3 bucket is hosted.
  Currently, cross-region loads are not supported.
- **format** (required) – The data format of the Amazon S3 data to be loaded, valid options are
  `csv`, `opencypher`, `ntriples` or `parquet`. For more information,
  see [Data format for loading from Amazon S3 into Neptune Analytics](loading-data-formats.md "loading-data-formats.md").
- **ParquetType** (required if the format is `parquet`) - The data type of the
  Parquet format, with the only valid option being `columnar`. For more information, see
  [Using Parquet data](using-Parquet-data.md "using-Parquet-data.md").
- **blankNodeHanding**(must be provided when format is `ntriples`) - The
  method to handle blank nodes in the dataset. Currently, only `convertToIri` is supported,
  meaning blank nodes are converted to unique IRIs at load time.
  For more information, see [Handling RDF values](using-rdf-data.md#rdf-handling "using-rdf-data.md#rdf-handling").
- **failOnError** (optional) default: true – If set to `true`
  (the default), the load process halts whenever there is an error parsing or inserting data.
  If set to `false`, the load process continues and commits whatever data was successfully inserted.

The edge or relationship data should be loaded with `failOnError` set to `true`,
to avoid duplication of partially committed edges or relationships in subsequent loads.

- _concurrency_ (optional) default: 1 – This value controls the number of threads used to
  run the load process, up to the maximum available.

###### Note

Unlike bulk import, there is no need to pass the `role-arn` for batch load since the IAM credentials
of the signer of the openCypher query are used to download data from Amazon S3. The signer must have permissions to
download data from Amazon S3 with the trust relationship set up to assume the role, so that Neptune Analytics can assume the role
to load the data into the graph from files in Amazon S3.

## Response syntax

A sample response is shown below.

```
{
    "results": [
        {
            "totalRecords": 108070,
            "totalDuplicates": 46521,
            "totalTimeSpentMillis": 558,
            "numThreads": 16,
            "insertErrors": 0,
            "throughputRecordsPerSec": 193673,
            "loadId": "13a60c3b-754d-c49b-4c23-06b9dd5b346b"
        }
    ]
}
```

- `totalRecords`: The number of graph elements - vertex labels, edges, and properties - attempted
  for insertion.
- `totalDuplicates`: The count of duplicate graph elements - vertex labels or properties -
  encountered. These elements may have pre-existed before the load request or were duplicates within the
  input CSV files. Each edge is treated as new, so edges are excluded from this count.
- `totalTimeSpentMillis`: The total time taken for downloading, parsing, and inserting data
  from CSV files, excluding the request queue time.
- `numThreads`: The number of threads utilized for downloading and inserting data. This correlates
  with the provided `concurrency` parameter input, reflecting any caps applied.
- `insertErrors`: Errors faced during insertions, including parsing errors and Amazon S3 access issues.
  Error details are available in the CloudWatch logs. Refer to the [Troubleshooting](bulk-import-troubleshooting.md "bulk-import-troubleshooting.md")
  section of this document to understand troubleshooting insertErrors. Concurrent modification errors may
  also cause insert errors in batch loads attempting to modify a vertex property value being concurrently
  changed by another request.
- `throughputRecordsPerSec`: The total throughput in records per second.
- `loadId`: The loadId for searching errors and load summary. All batch information is published
  to CloudWatch logs under `/aws/neptune/import-task-logs/<graph-id>/<load-id>`.

###### Note

Around 2.5Gb of Amazon S3 files can be loaded in a single request on 128 m-NCU. Larger sized datasets could run into
`out of memory` errors. To workaround that, the Amazon S3 files can be split across multiple serial batch
load requests. The source argument takes a prefix, so files can be partitioned across requests by including
prefixes of file names. The limit scales linearly based on m-NCUs, so for example 5Gb of Amazon S3 files can be loaded
in a single request on 256 m-NCU. Also, if the dataset contains larger string values for example, then larger
volumes of data can also be ingested in a single request, since they would generate fewer number of graph
elements per byte of dataset. It is recommended to run tests with your data to determine the exact details
for this process.

###### Important

Duplicate edges get created if the same edge file content is loaded more than once. This could happen if, for example:

1. The same Amazon S3 source or file is accidentally included for load in more than one request that succeeded.
2. The edge data is first loaded with `failOnError` set to false and runs into partial errors,
   and the errors are fixed and the entire dataset is reloaded. All of the edges that were successfully
   inserted on the first request would get duplicated after the second request.
