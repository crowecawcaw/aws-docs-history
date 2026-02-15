# Neptune data plane bulk loader APIs

**Bulk-load actions:**

- [StartLoaderJob (action)](#StartLoaderJob "#StartLoaderJob")
- [GetLoaderJobStatus (action)](#GetLoaderJobStatus "#GetLoaderJobStatus")
- [ListLoaderJobs (action)](#ListLoaderJobs "#ListLoaderJobs")
- [CancelLoaderJob (action)](#CancelLoaderJob "#CancelLoaderJob")
  **Bulk load structure:**

- [LoaderIdResult (structure)](#LoaderIdResult "#LoaderIdResult")

## StartLoaderJob (action)

        The AWS CLI name for this API is: `start-loader-job`.

Starts a Neptune bulk loader job to load data from an Amazon S3 bucket into
a Neptune DB instance. See [Using
the Amazon Neptune Bulk Loader to Ingest Data](bulk-load.md "bulk-load.md").

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:StartLoaderJob](iam-dp-actions.md#startloaderjob "iam-dp-actions.md#startloaderjob")
IAM action in that cluster.

**Request**

- **dependencies**  (in the CLI: `--dependencies`) –  a String, of type: `string` (a UTF-8 encoded string).

This is an optional parameter that can make a queued load request contingent
on the successful completion of one or more previous jobs in the queue.

Neptune can queue up as many as 64 load requests at a time, if their `queueRequest`
parameters are set to `"TRUE"`. The `dependencies`
parameter lets you make execution of such a queued request dependent on the successful
completion of one or more specified previous requests in the queue.

For example, if load `Job-A` and `Job-B` are
independent of each other, but load `Job-C` needs `Job-A`
and `Job-B` to be finished before it begins, proceed as follows:

    1. Submit `load-job-A` and `load-job-B` one after
     another in any order, and save their load-ids.
    2. Submit `load-job-C` with the load-ids of the two jobs in its
     `dependencies` field:

###### Example

```
  "dependencies" : ["(job_A_load_id)", "(job_B_load_id)"]
```

Because of the `dependencies` parameter, the bulk loader
will not start `Job-C` until `Job-A` and `Job-B`
have completed successfully. If either one of them fails, Job-C will not be executed,
and its status will be set to `LOAD_FAILED_BECAUSE_DEPENDENCY_NOT_SATISFIED`.

You can set up multiple levels of dependency in this way, so that the failure
of one job will cause all requests that are directly or indirectly dependent on
it to be cancelled.

- **failOnError**  (in the CLI: `--fail-on-error`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

**`failOnError`**  
–   A flag to toggle a complete stop on an error.

_Allowed values_: `"TRUE"`, `"FALSE"`.

_Default value_: `"TRUE"`.

When this parameter is set to `"FALSE"`, the loader tries
to load all the data in the location specified, skipping any entries with errors.

When this parameter is set to `"TRUE"`, the loader stops as
soon as it encounters an error. Data loaded up to that point persists.

- **format**  (in the CLI: `--format`) –  _Required:_ a Format, of type: `string` (a UTF-8 encoded string).

The format of the data. For more information about data formats for the
Neptune `Loader` command, see [Load
Data Formats](bulk-load-tutorial-format.md "bulk-load-tutorial-format.md").

###### Allowed values

    + **`csv`** for the [Gremlin
     CSV data format](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md").
    + **`opencypher`** for the
     [openCypher
     CSV data format](bulk-load-tutorial-format-opencypher.md "bulk-load-tutorial-format-opencypher.md").
    + **`ntriples`** for the
     [N-Triples RDF data format](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/").
    + **`nquads`** for the [N-Quads RDF data format](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/").
    + **`rdfxml`** for the [RDF\XML RDF data format](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/").
    + **`turtle`** for the [Turtle RDF data format](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/").

- **iamRoleArn**  (in the CLI: `--iam-role-arn`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for an IAM role to be assumed by the Neptune
DB instance for access to the S3 bucket. The IAM role ARN provided here should be
attached to the DB cluster (see [Adding
the IAM Role to an Amazon Neptune Cluster](bulk-load-tutorial-IAM-add-role-cluster.md "bulk-load-tutorial-IAM-add-role-cluster.md").

- **mode**  (in the CLI: `--mode`) –  a Mode, of type: `string` (a UTF-8 encoded string).

The load job mode.

_Allowed values_: `RESUME`, `NEW`,
`AUTO`.

_Default value_: `AUTO`.

######

    + `RESUME`   –   In RESUME mode, the loader
     looks for a previous load from this source, and if it finds one, resumes that load
     job. If no previous load job is found, the loader stops.


    The loader avoids reloading files that were successfully loaded in a previous
     job. It only tries to process failed files. If you dropped previously loaded data
     from your Neptune cluster, that data is not reloaded in this mode. If a previous
     load job loaded all files from the same source successfully, nothing is reloaded,
     and the loader returns success.
    + `NEW`   –   In NEW mode, the creates a new
     load request regardless of any previous loads. You can use this mode to reload
     all the data from a source after dropping previously loaded data from your Neptune
     cluster, or to load new data available at the same source.
    + `AUTO`   –   In AUTO mode, the loader looks
     for a previous load job from the same source, and if it finds one, resumes that job,
     just as in `RESUME` mode.


    If the loader doesn't find a previous load job from the same source, it loads
     all data from the source, just as in `NEW` mode.

- **parallelism**  (in the CLI: `--parallelism`) –  a Parallelism, of type: `string` (a UTF-8 encoded string).

The optional `parallelism` parameter can be set to reduce
the number of threads used by the bulk load process.

_Allowed values_:

    + `LOW` –   The number of threads used is the number
     of available vCPUs divided by 8.
    + `MEDIUM` –   The number of threads used is the
     number of available vCPUs divided by 2.
    + `HIGH` –   The number of threads used is the same
     as the number of available vCPUs.
    + `OVERSUBSCRIBE` –   The number of threads used
     is the number of available vCPUs multiplied by 2. If this value is used, the bulk
     loader takes up all available resources.


    This does not mean, however, that the `OVERSUBSCRIBE` setting
     results in 100% CPU utilization. Because the load operation is I/O bound, the
     highest CPU utilization to expect is in the 60% to 70% range.

_Default value_: `HIGH`

The `parallelism` setting can sometimes result in a deadlock
between threads when loading openCypher data. When this happens, Neptune returns
the `LOAD_DATA_DEADLOCK` error. You can generally fix the issue
by setting `parallelism` to a lower setting and retrying the load
command.

- **parserConfiguration**  (in the CLI: `--parser-configuration`) –  It is a map array of key-value pairs where:

    Each key is a a String, of type: `string` (a UTF-8 encoded string).

    Each value is a a String, of type: `string` (a UTF-8 encoded string).

**`parserConfiguration`**
  –   An optional object with additional parser configuration
values. Each of the child parameters is also optional:

######

    + **`namedGraphUri`**  
     –   The default graph for all RDF formats when no graph is specified
     (for non-quads formats and NQUAD entries with no graph).


    The default is `https://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`.
    + **`baseUri`**   –
       The base URI for RDF/XML and Turtle formats.


    The default is `https://aws.amazon.com/neptune/default`.
    + **`allowEmptyStrings`**
       –   Gremlin users need to be able to pass empty string values("")
     as node and edge properties when loading CSV data. If `allowEmptyStrings`
     is set to `false` (the default), such empty strings are treated as
     nulls and are not loaded.


    If `allowEmptyStrings` is set to `true`, the
     loader treats empty strings as valid property values and loads them accordingly.

- **queueRequest**  (in the CLI: `--queue-request`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

This is an optional flag parameter that indicates whether the load request
can be queued up or not.

You don't have to wait for one load job to complete before issuing the next
one, because Neptune can queue up as many as 64 jobs at a time, provided that their
`queueRequest` parameters are all set to `"TRUE"`.
The queue order of the jobs will be first-in-first-out (FIFO).

If the `queueRequest` parameter is omitted or set to `"FALSE"`,
the load request will fail if another load job is already running.

_Allowed values_: `"TRUE"`, `"FALSE"`.

_Default value_: `"FALSE"`.

- **s3BucketRegion**  (in the CLI: `--s-3-bucket-region`) –  _Required:_ a S3BucketRegion, of type: `string` (a UTF-8 encoded string).

The Amazon region of the S3 bucket. This must match the Amazon Region of
the DB cluster.

- **source**  (in the CLI: `--source`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The `source` parameter accepts an S3 URI that identifies
a single file, multiple files, a folder, or multiple folders. Neptune loads every
data file in any folder that is specified.

The URI can be in any of the following formats.

    + `s3://(bucket_name)/(object-key-name)`
    + `https://s3.amazonaws.com/(bucket_name)/(object-key-name)`
    + `https://s3.us-east-1.amazonaws.com/(bucket_name)/(object-key-name)`

The `object-key-name` element of the URI is equivalent to
the [prefix](../../../AmazonS3/latest/API/API_ListObjects.md#API_ListObjects_RequestParameters "../../../AmazonS3/latest/API/API_ListObjects.md#API_ListObjects_RequestParameters")
parameter in an S3 [ListObjects](../../../AmazonS3/latest/API/API_ListObjects.md "../../../AmazonS3/latest/API/API_ListObjects.md")
API call. It identifies all the objects in the specified S3 bucket whose names
begin with that prefix. That can be a single file or folder, or multiple files and/or
folders.

The specified folder or folders can contain multiple vertex files and
multiple edge files.

- **updateSingleCardinalityProperties**  (in the CLI: `--update-single-cardinality-properties`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

`updateSingleCardinalityProperties` is an optional parameter
that controls how the bulk loader treats a new value for single-cardinality vertex
or edge properties. This is not supported for loading openCypher data.

_Allowed values_: `"TRUE"`, `"FALSE"`.

_Default value_: `"FALSE"`.

By default, or when `updateSingleCardinalityProperties`
is explicitly set to `"FALSE"`, the loader treats a new value as an
error, because it violates single cardinality.

When `updateSingleCardinalityProperties` is set to `"TRUE"`,
on the other hand, the bulk loader replaces the existing value with the new one.
If multiple edge or single-cardinality vertex property values are provided
in the source file(s) being loaded, the final value at the end of the bulk load could
be any one of those new values. The loader only guarantees that the existing value
has been replaced by one of the new ones.

- **userProvidedEdgeIds**  (in the CLI: `--user-provided-edge-ids`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

This parameter is required only when loading openCypher data that contains
relationship IDs. It must be included and set to `True` when openCypher
relationship IDs are explicitly provided in the load data (recommended).

When `userProvidedEdgeIds` is absent or set to `True`,
an `:ID` column must be present in every relationship file in the
load.

When `userProvidedEdgeIds` is present and set to `False`,
relationship files in the load **must not**
contain an `:ID` column. Instead, the Neptune loader automatically
generates an ID for each relationship.

It's useful to provide relationship IDs explicitly so that the loader
can resume loading after error in the CSV data have been fixed, without having
to reload any relationships that have already been loaded. If relationship IDs
have not been explicitly assigned, the loader cannot resume a failed load if any
relationship file has had to be corrected, and must instead reload all the relationships.

**Response**

- **payload**   – _Required:_ It is a map array of key-value pairs where:

    Each key is a a String, of type: `string` (a UTF-8 encoded string).

    Each value is a a String, of type: `string` (a UTF-8 encoded string).

Contains a `loadId` name-value pair that provides an identifier
for the load operation.

- **status**   – _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP return code indicating the status of the load job.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [BulkLoadIdNotFoundException](data-api-dp-errors.md#BulkLoadIdNotFoundException "data-api-dp-errors.md#BulkLoadIdNotFoundException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [LoadUrlAccessDeniedException](data-api-dp-errors.md#LoadUrlAccessDeniedException "data-api-dp-errors.md#LoadUrlAccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [InternalFailureException](data-api-dp-errors.md#InternalFailureException "data-api-dp-errors.md#InternalFailureException")
- [S3Exception](data-api-dp-errors.md#S3Exception "data-api-dp-errors.md#S3Exception")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")

## GetLoaderJobStatus (action)

        The AWS CLI name for this API is: `get-loader-job-status`.

Gets status information about a specified load job. Neptune keeps track
of the most recent 1,024 bulk load jobs, and stores the last 10,000 error details
per job.

See [Neptune
Loader Get-Status API](load-api-reference-status.md "load-api-reference-status.md") for more information.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetLoaderJobStatus](iam-dp-actions.md#getloaderjobstatus "iam-dp-actions.md#getloaderjobstatus")
IAM action in that cluster..

**Request**

- **details**  (in the CLI: `--details`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Flag indicating whether or not to include details beyond the overall status
(`TRUE` or `FALSE`; the default is `FALSE`).

- **errors**  (in the CLI: `--errors`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Flag indicating whether or not to include a list of errors encountered
(`TRUE` or `FALSE`; the default is `FALSE`).

The list of errors is paged. The `page` and `errorsPerPage`
parameters allow you to page through all the errors.

- **errorsPerPage**  (in the CLI: `--errors-per-page`) –  a PositiveInteger, of type: `integer` (a signed 32-bit integer), at least 1 ?st?.

The number of errors returned in each page (a positive integer; the default
is `10`). Only valid when the `errors` parameter set
to `TRUE`.

- **loadId**  (in the CLI: `--load-id`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The load ID of the load job to get the status of.

- **page**  (in the CLI: `--page`) –  a PositiveInteger, of type: `integer` (a signed 32-bit integer), at least 1 ?st?.

The error page number (a positive integer; the default is `1`).
Only valid when the `errors` parameter is set to `TRUE`.

**Response**

- **payload**   – _Required:_ a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

Status information about the load job, in a layout that could look like
this:

###### Example

```
{
          "status" : "200 OK",
          "payload" : {
            "feedCount" : [
              {
                "LOAD_FAILED" : (number)
              }
            ],
            "overallStatus" : {
              "fullUri" : "s3://(bucket)/(key)",
              "runNumber" : (number),
              "retryNumber" : (number),
              "status" : "(string)",
              "totalTimeSpent" : (number),
              "startTime" : (number),
              "totalRecords" : (number),
              "totalDuplicates" : (number),
              "parsingErrors" : (number),
              "datatypeMismatchErrors" : (number),
              "insertErrors" : (number),
            },
            "failedFeeds" : [
              {
                "fullUri" : "s3://(bucket)/(key)",
                "runNumber" : (number),
                "retryNumber" : (number),
                "status" : "(string)",
                "totalTimeSpent" : (number),
                "startTime" : (number),
                "totalRecords" : (number),
                "totalDuplicates" : (number),
                "parsingErrors" : (number),
                "datatypeMismatchErrors" : (number),
                "insertErrors" : (number),
              }
            ],
            "errors" : {
              "startIndex" : (number),
              "endIndex" : (number),
              "loadId" : "(string),
              "errorLogs" : [ ]
            }
          }
        }
```

- **status**   – _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP response code for the request.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [BulkLoadIdNotFoundException](data-api-dp-errors.md#BulkLoadIdNotFoundException "data-api-dp-errors.md#BulkLoadIdNotFoundException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [LoadUrlAccessDeniedException](data-api-dp-errors.md#LoadUrlAccessDeniedException "data-api-dp-errors.md#LoadUrlAccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [InternalFailureException](data-api-dp-errors.md#InternalFailureException "data-api-dp-errors.md#InternalFailureException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")

## ListLoaderJobs (action)

        The AWS CLI name for this API is: `list-loader-jobs`.

Retrieves a list of the `loadIds` for all active loader jobs.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:ListLoaderJobs](iam-dp-actions.md#listloaderjobs "iam-dp-actions.md#listloaderjobs")
IAM action in that cluster..

**Request**

- **includeQueuedLoads**  (in the CLI: `--include-queued-loads`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

An optional parameter that can be used to exclude the load IDs of queued
load requests when requesting a list of load IDs by setting the parameter to `FALSE`.
The default value is `TRUE`.

- **limit**  (in the CLI: `--limit`) –  a ListLoaderJobsInputLimitInteger, of type: `integer` (a signed 32-bit integer), not less than 1 or more than 100 ?st?s.

The number of load IDs to list. Must be a positive integer greater than zero
and not more than `100` (which is the default).

**Response**

- **payload**   – _Required:_ A [LoaderIdResult](#LoaderIdResult "#LoaderIdResult") object.

The requested list of job IDs.

- **status**   – _Required:_ a String, of type: `string` (a UTF-8 encoded string).

Returns the status of the job list request.

###### Errors

- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [BulkLoadIdNotFoundException](data-api-dp-errors.md#BulkLoadIdNotFoundException "data-api-dp-errors.md#BulkLoadIdNotFoundException")
- [InternalFailureException](data-api-dp-errors.md#InternalFailureException "data-api-dp-errors.md#InternalFailureException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [LoadUrlAccessDeniedException](data-api-dp-errors.md#LoadUrlAccessDeniedException "data-api-dp-errors.md#LoadUrlAccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")

## CancelLoaderJob (action)

        The AWS CLI name for this API is: `cancel-loader-job`.

Cancels a specified load job. This is an HTTP `DELETE` request.
See [Neptune
Loader Get-Status API](load-api-reference-status.md "load-api-reference-status.md") for more information.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:CancelLoaderJob](iam-dp-actions.md#cancelloaderjob "iam-dp-actions.md#cancelloaderjob")
IAM action in that cluster..

**Request**

- **loadId**  (in the CLI: `--load-id`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the load job to be deleted.

**Response**

- **status**   – a String, of type: `string` (a UTF-8 encoded string).

The cancellation status.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [BulkLoadIdNotFoundException](data-api-dp-errors.md#BulkLoadIdNotFoundException "data-api-dp-errors.md#BulkLoadIdNotFoundException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [LoadUrlAccessDeniedException](data-api-dp-errors.md#LoadUrlAccessDeniedException "data-api-dp-errors.md#LoadUrlAccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [InternalFailureException](data-api-dp-errors.md#InternalFailureException "data-api-dp-errors.md#InternalFailureException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")

## _Bulk load structure:_

## LoaderIdResult (structure)

Contains a list of load IDs.

###### Fields

- **loadIds** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of load IDs.
