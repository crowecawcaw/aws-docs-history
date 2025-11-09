# Neptune Loader Command

Loads data from an Amazon S3 bucket into a Neptune DB instance.

To load data, you must send an HTTP `POST` request to the
`https://`your-neptune-endpoint`:`port`/loader`
endpoint. The parameters for the `loader` request can be sent in
the `POST` body or as URL-encoded parameters.

###### Important

The MIME type must be `application/json`.

The Amazon S3 bucket must be in the same AWS Region as the cluster.

###### Note

You can load encrypted data from Amazon S3 if it was encrypted using the Amazon S3
`SSE-S3` mode. In that case, Neptune is able to impersonate your
credentials and issue `s3:getObject` calls on your behalf.

You can also load encrypted data from Amazon S3 that was encrypted using the
`SSE-KMS` mode, as long as your IAM role includes the necessary
permissions to access AWS KMS. Without proper AWS KMS permissions, the bulk
load operation fails and returns a `LOAD_FAILED` response.

Neptune does not currently support loading Amazon S3 data encrypted using the
`SSE-C` mode.

You don't have to wait for one load job to finish before you start another
one. Neptune can queue up as many as 64 jobs requests at a time, provided that
their `queueRequest` parameters are all set to `"TRUE"`.
The queue order of the jobs will be first-in-first-out (FIFO). If you don't want
a load job to be queued up, on the other hand, you can set its
`queueRequest` parameter to `"FALSE"` (the default), so that
the load job will fail if another one is already in progress.

You can use the `dependencies` parameter to queue up a job that
must only be run after specified previous jobs in the queue have completed
successfully. If you do that and any of those specified jobs fails, your job will
not be run and its status will be set to `LOAD_FAILED_BECAUSE_DEPENDENCY_NOT_SATISFIED`.

## Neptune Loader Request Syntax

```
{
  "source" : "`string`",
  "format" : "`string`",
  "iamRoleArn" : "`string`",
  "mode": "`NEW|RESUME|AUTO`",
  "region" : "`us-east-1`",
  "failOnError" : "`string`",
  "parallelism" : "`string`",
  "parserConfiguration" : {
    "baseUri" : "`http://base-uri-string`",
    "namedGraphUri" : "`http://named-graph-string`"
  },
  "updateSingleCardinalityProperties" : "`string`",
  "queueRequest" : "TRUE",
  "dependencies" : ["`load_A_id`", "`load_B_id`"]
}
```

###### edgeOnlyLoad Syntax

For an `edgeOnlyLoad`, the syntax would be:

```
{
"source" : "`string`",
"format" : "`string`",
"iamRoleArn" : "`string`",
"mode": "`NEW|RESUME|AUTO`",
"region" : "`us-east-1`",
"failOnError" : "`string`",
"parallelism" : "`string`",
"edgeOnlyLoad" : "`string`",
"parserConfiguration" : {
    "baseUri" : "`http://base-uri-string`",
    "namedGraphUri" : "`http://named-graph-string`"
},
"updateSingleCardinalityProperties" : "`string`",
"queueRequest" : "TRUE",
"dependencies" : ["`load_A_id`", "`load_B_id`"]
}
```

## Neptune Loader Request Parameters

- **`source`**   –   An Amazon S3 URI.

The `SOURCE` parameter accepts an Amazon S3 URI that identifies a single
file, multiple files, a folder, or multiple folders. Neptune loads every data file in any folder
that is specified.

The URI can be in any of the following formats.

    + `s3://`bucket_name`/`object-key-name``
    + `https://s3.amazonaws.com/`bucket_name`/`object-key-name``
    + `https://s3.us-east-1.amazonaws.com/`bucket_name`/`object-key-name``

The `object-key-name` element of the URI is equivalent to the [prefix](../../../AmazonS3/latest/API/API_ListObjects.md#API_ListObjects_RequestParameters "../../../AmazonS3/latest/API/API_ListObjects.md#API_ListObjects_RequestParameters")
parameter in an Amazon S3 [ListObjects](../../../AmazonS3/latest/API/API_ListObjects.md "../../../AmazonS3/latest/API/API_ListObjects.md")
API call. It identifies all the objects in the specified Amazon S3 bucket whose names begin with
that prefix. That can be a single file or folder, or multiple files and/or folders.

The specified folder or folders can contain multiple vertex files and multiple edge files.

For example, if you had the following folder structure and files in an Amazon S3 bucket named `bucket-name`:

```
s3://bucket-name/a/bc
s3://bucket-name/ab/c
s3://bucket-name/ade
s3://bucket-name/bcd
```

If the source parameter is specified as `s3://bucket-name/a`, the first three files will be loaded.

```
s3://bucket-name/a/bc
s3://bucket-name/ab/c
s3://bucket-name/ade
```

- **`format`**   –   The format of the
  data. For more information about data formats for the Neptune
  `Loader` command, see [Using the Amazon Neptune bulk loader to ingest data](bulk-load.md "bulk-load.md").

###### Allowed values

    + **`csv`** for the [Gremlin CSV data format](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md").
    + **`opencypher`** for the
     [openCypher CSV data format](bulk-load-tutorial-format-opencypher.md "bulk-load-tutorial-format-opencypher.md").
    + **`ntriples`** for the
     [N-Triples RDF data format](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/").
    + **`nquads`** for the
     [N-Quads RDF data format](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/").
    + **`rdfxml`** for the
     [RDF\XML RDF data format](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/").
    + **`turtle`** for the
     [Turtle RDF data format](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/").

- **`iamRoleArn`**   –   The Amazon Resource
  Name (ARN) for an IAM role to be assumed by the Neptune DB instance for
  access to the S3 bucket. For information about creating a role that has access to Amazon S3
  and then associating it with a Neptune cluster, see [Prerequisites: IAM Role and Amazon S3 Access](bulk-load-tutorial-IAM.md "bulk-load-tutorial-IAM.md").

Starting with [engine release 1.2.1.0.R3](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md"),
you can also chain multiple IAM roles if the Neptune DB instance and the Amazon S3 bucket
are located in different AWS Accounts. In this case, `iamRoleArn` contains
a comma-separated list of role ARNs, as described in [Chaining IAM roles in Amazon Neptune](bulk-load-tutorial-chain-roles.md "bulk-load-tutorial-chain-roles.md"). For example:

```
curl -X POST https://localhost:8182/loader \
  -H 'Content-Type: application/json' \
  -d '{
        "source" : "s3://`(the target bucket name)`/`(the target date file name)`",
        "iamRoleArn" : "arn:aws:iam::`(Account A ID)`:role/`(RoleA)`,arn:aws:iam::`(Account B ID)`:role/`(RoleB)`,arn:aws:iam::`(Account C ID)`:role/`(RoleC)`",
        "format" : "csv",
        "region" : "us-east-1"
      }'
```

- **`region`**   –   The `region`
  parameter must match the AWS Region of the cluster and the S3 bucket.

Amazon Neptune is available in the following Regions:

    + US East (N. Virginia):   `us-east-1`
    + US East (Ohio):   `us-east-2`
    + US West (N. California):   `us-west-1`
    + US West (Oregon):   `us-west-2`
    + Canada (Central):   `ca-central-1`
    + Canada West (Calgary):   `ca-west-1`
    + South America (São Paulo):   `sa-east-1`
    + Europe (Stockholm):   `eu-north-1`
    + Europe (Spain):   `eu-south-2`
    + Europe (Ireland):   `eu-west-1`
    + Europe (London):   `eu-west-2`
    + Europe (Paris):   `eu-west-3`
    + Europe (Frankfurt):   `eu-central-1`
    + Middle East (Bahrain):   `me-south-1`
    + Middle East (UAE):   `me-central-1`
    + Israel (Tel Aviv):   `il-central-1`
    + Africa (Cape Town):   `af-south-1`
    + Asia Pacific (Hong Kong):   `ap-east-1`
    + Asia Pacific (Tokyo):   `ap-northeast-1`
    + Asia Pacific (Seoul):   `ap-northeast-2`
    + Asia Pacific (Osaka):   `ap-northeast-3`
    + Asia Pacific (Singapore):   `ap-southeast-1`
    + Asia Pacific (Sydney):   `ap-southeast-2`
    + Asia Pacific (Jakarta):   `ap-southeast-3`
    + Asia Pacific (Melbourne):   `ap-southeast-4`
    + Asia Pacific (Malaysia):   `ap-southeast-5`
    + Asia Pacific (Mumbai):   `ap-south-1`
    + China (Beijing):   `cn-north-1`
    + China (Ningxia):   `cn-northwest-1`
    + AWS GovCloud (US-West):   `us-gov-west-1`
    + AWS GovCloud (US-East):   `us-gov-east-1`

- **`mode`**   –   The load job mode.

_Allowed values_: `RESUME`, `NEW`,
`AUTO`.

_Default value_: `AUTO`

######

    + `RESUME`   –   In RESUME mode,
     the loader looks for a previous load from this source, and if it finds
     one, resumes that load job. If no previous load job is found, the loader stops.


    The loader avoids reloading files that were successfully loaded in
     a previous job. It only tries to process failed files. If you dropped
     previously loaded data from your Neptune cluster, that data is not
     reloaded in this mode. If a previous load job loaded all files from the
     same source successfully, nothing is reloaded, and the loader returns
     success.
    + `NEW`   –   In NEW mode, the
     creates a new load request regardless of any previous loads. You
     can use this mode to reload all the data from a source after dropping
     previously loaded data from your Neptune cluster, or to load new data
     available at the same source.
    + `AUTO`   –   In AUTO mode,
     the loader looks for a previous load job from the same source, and if it
     finds one, resumes that job, just as in `RESUME` mode.


    If the loader doesn't find a previous load job from the same
     source, it loads all data from the source, just as in `NEW`
     mode.

- **`edgeOnlyLoad`**   –   A flag that
  controls file processing order during bulk loading.

_Allowed values_: `"TRUE"`, `"FALSE"`.

_Default value_: `"FALSE"`.

When this parameter is set to "FALSE", the loader automatically loads vertex files first, then edge
files afterwards. It does this by first scanning all files to determine their contents (vertices or edges).
When this parameter is set to "TRUE", the loader skips the initial scanning phase and immediately loads all
files in the order they appear. For more information see
[bulk load optimize](bulk-load-optimize.md "bulk-load-optimize.md").

- **`failOnError`**   –   A flag to toggle a
  complete stop on an error.

_Allowed values_: `"TRUE"`, `"FALSE"`.

_Default value_: `"TRUE"`.

When this parameter is set to `"FALSE"`, the loader tries to load all
the data in the location specified, skipping any entries with errors.

When this parameter is set to `"TRUE"`, the loader stops
as soon as it encounters an error. Data loaded up to that point persists.

- **`parallelism`**   –   This is an optional
  parameter that can be set to reduce the number of threads used by the
  bulk load process.

_Allowed values_:

    + `LOW` –   The number of threads used is the
     number of available vCPUs divided by 8.
    + `MEDIUM` –   The number of threads used is the
     number of available vCPUs divided by 2.
    + `HIGH` –   The number of threads used is the
     same as the number of available vCPUs.
    + `OVERSUBSCRIBE` –   The number of threads used is the
     number of available vCPUs multiplied by 2. If this value is used, the bulk loader takes up all
     available resources.


    This does not mean, however, that the `OVERSUBSCRIBE` setting
     results in 100% CPU utilization. Because the load operation is I/O bound, the
     highest CPU utilization to expect is in the 60% to 70% range.

_Default value_: `HIGH`

The `parallelism` setting can sometimes result in a deadlock
between threads when loading openCypher data. When this happens, Neptune returns the
`LOAD_DATA_DEADLOCK` error. You can generally fix the issue by setting
`parallelism` to a lower setting and retrying the load command.

- **`parserConfiguration`**  
  –   An optional object with additional parser configuration values.
  Each of the child parameters is also optional:

| Name                | Example Value                                               | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `namedGraphUri`     | `http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph` | The default graph for all RDF formats when no graph is specified (for non-quads<br>formats and NQUAD entries with no graph). The default is<br>`http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`                                                                                                                                                                           |
| `baseUri`           | `http://aws.amazon.com/neptune/default`                     | The base URI for RDF/XML and Turtle formats. The default is<br>`http://aws.amazon.com/neptune/default`.                                                                                                                                                                                                                                                                              |
| `allowEmptyStrings` | `true`                                                      | Gremlin users need to be able to pass empty string values("") as node<br>and edge properties when loading CSV data. If `allowEmptyStrings`<br>is set to `false` (the default), such empty strings are treated<br>as nulls and are not loaded.<br>If `allowEmptyStrings` is set to `true`,<br>the loader treats empty strings as valid property values and loads<br>them accordingly. |

For more information, see [SPARQL Default Graph and Named Graphs](feature-sparql-compliance.md#sparql-default-graph "feature-sparql-compliance.md#sparql-default-graph").

- **`updateSingleCardinalityProperties`**   –   This
  is an optional parameter that controls how the bulk loader treats a new
  value for single-cardinality vertex or edge properties. This is not supported for
  loading openCypher data (see [Loading openCypher data](#load-api-reference-load-parameters-opencypher "#load-api-reference-load-parameters-opencypher")).

_Allowed values_: `"TRUE"`, `"FALSE"`.

_Default value_: `"FALSE"`.

By default, or when `updateSingleCardinalityProperties` is explicitly
set to `"FALSE"`, the loader treats a new value as an error, because it
violates single cardinality.

When `updateSingleCardinalityProperties` is set to `"TRUE"`,
on the other hand, the bulk loader replaces the existing value with the new one.
If multiple edge or single-cardinality vertex property values are provided in the
source file(s) being loaded, the final value at the end of the bulk load could be
any one of those new values. The loader only guarantees that the existing value
has been replaced by one of the new ones.

- **`queueRequest`**   –   This is an optional flag parameter
  that indicates whether the load request can be queued up or not.

You don't have to wait for one load job to complete before issuing the next one,
because Neptune can queue up as many as 64 jobs at a time, provided that their
`queueRequest` parameters are all set to `"TRUE"`. The queue
order of the jobs will be first-in-first-out (FIFO).

If the `queueRequest` parameter is omitted or set to `"FALSE"`,
the load request will fail if another load job is already running.

_Allowed values_: `"TRUE"`, `"FALSE"`.

_Default value_: `"FALSE"`.

- **`dependencies`**   –   This is an optional parameter
  that can make a queued load request contingent on the successful completion of one or more
  previous jobs in the queue.

Neptune can queue up as many as 64 load requests at a time, if their
`queueRequest` parameters are set to `"TRUE"`. The
`dependencies` parameter lets you make execution of such a queued request
dependent on the successful completion of one or more specified previous requests
in the queue.

For example, if load `Job-A` and `Job-B` are independent
of each other, but load `Job-C` needs `Job-A` and `Job-B`
to be finished before it begins, proceed as follows:

    1. Submit `load-job-A` and `load-job-B` one after
     another in any order, and save their load-ids.
    2. Submit `load-job-C` with the load-ids of the
     two jobs in its `dependencies` field:

```
  "dependencies" : ["`job_A_load_id`", "`job_B_load_id`"]
```

Because of the `dependencies` parameter, the bulk loader will not start
`Job-C` until `Job-A` and `Job-B` have completed
successfully. If either one of them fails, Job-C will not be executed, and its
status will be set to `LOAD_FAILED_BECAUSE_DEPENDENCY_NOT_SATISFIED`.

You can set up multiple levels of dependency in this way, so that the failure of one job
will cause all requests that are directly or indirectly dependent on it to be cancelled.

- **`userProvidedEdgeIds`**   –  
  This parameter is required only when loading openCypher data that contains relationship
  IDs. It must be included and set to `True` when openCypher relationship IDs
  are explicitly provided in the load data (recommended).

When `userProvidedEdgeIds` is absent or set to `True`,
an `:ID` column must be present in every relationship file in the load.

When `userProvidedEdgeIds` is present and set to `False`,
relationship files in the load **must not** contain an
`:ID` column. Instead, the Neptune loader automatically generates an
ID for each relationship.

It's useful to provide relationship IDs explicitly so that the loader can resume
loading after error in the CSV data have been fixed, without having to reload any
relationships that have already been loaded. If relationship IDs have not been
explicitly assigned, the loader cannot resume a failed load if any relationship file
has had to be corrected, and must instead reload all the relationships.

- `accessKey`   –   **[deprecated]**
  An access key ID of an IAM role with access to the S3 bucket and data files.

The `iamRoleArn` parameter is recommended instead.
For information about creating a role that has access to Amazon S3 and then associating it
with a Neptune cluster, see [Prerequisites: IAM Role and Amazon S3 Access](bulk-load-tutorial-IAM.md "bulk-load-tutorial-IAM.md").

For more information, see [Access keys (access key ID and secret access key)](../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys").

- `secretKey`   –   **[deprecated]**
  The `iamRoleArn` parameter is recommended instead.
  For information about creating a role that has access to Amazon S3 and then associating it
  with a Neptune cluster, see [Prerequisites: IAM Role and Amazon S3 Access](bulk-load-tutorial-IAM.md "bulk-load-tutorial-IAM.md").

For more information, see [Access
keys (access key ID and secret access key)](../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys").

### Special considerations for loading openCypher data

- When loading openCypher data in CSV format, the format parameter must
  be set to `opencypher`.
- The `updateSingleCardinalityProperties` parameter is not
  supported for openCypher loads because all openCypher properties have single
  cardinality. The openCypher load format does not support arrays, and if an ID
  value appears more than once, it is treated as a duplicate or an insertion error
  (see below).
- The Neptune loader handles duplicates that it encounters in openCypher
  data as follows:
  - If the loader encounters multiple rows with the same node
    ID, they are merged using the following rule:
    - All the labels in the rows are added to the node.
    - For each property, only one of the property values is loaded.
      The selection of the one to load is non-deterministic.

  - If the loader encounters multiple rows with the same
    relationship ID, only one of them is loaded. The selection of the one
    to load is non-deterministric.
  - The loader never updates property values of an existing node
    or relationship in the database if it encounters load data having the ID
    of the existing node or relationship. However, it does load node labels
    and properties that are not present in the existing node or
    relationship.

- Although you don't have to assign IDs to relationships, it is
  usually a good idea (see the `userProvidedEdgeIds` parameter
  above). Without explicit relationship IDs, the loader must reload all
  relationships in case of an error in a relationship file, rather than
  resuming the load from where it failed.

Also, if the load data doesn't contain explicit relationship IDs,
the loader has no way of detecting duplicate relationships.

Here is an example of an openCypher load command:

```

curl -X POST https://`your-neptune-endpoint`:`port`/loader \
     -H 'Content-Type: application/json' \
     -d '
     {
       "source" : "s3://`bucket-name`/`object-key-name`",
       "format" : "**opencypher**",
       **"userProvidedEdgeIds": "TRUE"**,
       "iamRoleArn" : "arn:aws:iam::`account-id`:role/`role-name`",
       "region" : "`region`",
       "failOnError" : "FALSE",
       "parallelism" : "MEDIUM",
     }'
```

The loader response is the same as normal. For example:

```
{
  "status" : "200 OK",
  "payload" : {
    "loadId" : "`guid_as_string`"
  }
}
```

## Neptune Loader Response Syntax

```
{
    "status" : "200 OK",
    "payload" : {
        "loadId" : "`guid_as_string`"
    }
}
```

###### 200 OK

Successfully started load job returns a `200` code.
