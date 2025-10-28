# Handle data delivery failures

Each Amazon Data Firehose destination has its own data delivery failure handling.

When you setup a Firehose stream, for many destinations such as OpenSearch, Splunk, and HTTP endpoints, you also setup an
S3 bucket where data that fails to be delivered can be backed up. For more information about how Firehose backs up data in
case of failed deliveries, see the relevant destination sections on this page. For more information about how to grant access to S3 buckets where data that fails to
be delivered can be backed up, see [Grant Firehose Access to an Amazon S3 Destination](controlling-access.md#using-iam-s3 "controlling-access.md#using-iam-s3").
When Firehose (a) fails to deliver data to the stream destination, and (b) fails to write data to the backup S3 bucket for failed deliveries, it effectively pauses stream delivery until such time that data can either be delivered to the destination or written to the backup S3 location.

## Amazon S3

Data delivery to your S3 bucket might fail for various reasons. For
example, the bucket might not exist anymore, the IAM role that Amazon Data Firehose assumes
might not have access to the bucket, the network failed, or similar events. Under
these conditions, Amazon Data Firehose keeps retrying for up to 24 hours until the delivery
succeeds. The maximum data storage time of Amazon Data Firehose is 24 hours. If data delivery
fails for more than 24 hours, your data is lost.

Data delivery to your
S3 bucket can fail for various reasons, such as:

- The bucket no longer exists.
- The IAM role assumed by Amazon Data Firehose lacks access to the bucket.
- Network issues.
- S3 errors, such as HTTP 500s or other API failures.
  In these cases, Amazon Data Firehose will retry delivery:

- **DirectPut sources:** Retries continue for
  up to 24 hours.
- **Kinesis Data Streams or Amazon MSK sources:** Retries continue
  indefinitely, up to the retention policy defined on the stream.
  Amazon Data Firehose delivers failed records to a S3 error bucket only when Lambda processing or parquet
  conversion fails. Other failure scenarios will result in continuous retry attempts
  to S3 until the retention period is reached. When Firehose successfully delivers
  records to S3, it creates an S3 object file, and in cases of partial record
  failures, it automatically retries delivery and updates the same S3 object file with
  the successfully processed records.

## Amazon Redshift

For an Amazon Redshift destination, you can specify a retry duration (0–7200
seconds) when creating a Firehose stream.

Data delivery to your Amazon Redshift provisioned cluster or Amazon Redshift Serverless
workgroup might fail for several reasons. For example, you might have an
incorrect cluster configuration of your Firehose stream, a cluster or
workgroup under maintenance, or a network failure. Under these conditions,
Amazon Data Firehose retries for the specified time duration and skips that particular
batch of Amazon S3 objects. The skipped objects' information is delivered to your
S3 bucket as a manifest file in the `errors/` folder, which you
can use for manual backfill. For information about how to COPY data manually
with manifest files, see [Using a Manifest to Specify Data Files](../../../redshift/latest/dg/loading-data-files-using-manifest.md "../../../redshift/latest/dg/loading-data-files-using-manifest.md").

## Amazon OpenSearch Service and OpenSearch

Serverless

For the OpenSearch Service and OpenSearch Serverless destination, you can
specify a retry duration (0–7200 seconds) during Firehose stream
creation.

Data delivery to your OpenSearch Service cluster or OpenSearch Serverless
collection might fail for several reasons. For example, you might have an
incorrect OpenSearch Service cluster or OpenSearch Serverless collection
configuration of your Firehose stream, an OpenSearch Service cluster or
OpenSearch Serverless collection under maintenance, a network failure, or
similar events. Under these conditions, Amazon Data Firehose retries for the specified time
duration and then skips that particular index request. The skipped documents
are delivered to your S3 bucket in the
`AmazonOpenSearchService_failed/` folder, which you can use
for manual backfill.

For OpenSearch Service, each document has the following JSON
format:

```
{
    "attemptsMade": "(number of index requests attempted)",
    "arrivalTimestamp": "(the time when the document was received by Firehose)",
    "errorCode": "(http error code returned by OpenSearch Service)",
    "errorMessage": "(error message returned by OpenSearch Service)",
    "attemptEndingTimestamp": "(the time when Firehose stopped attempting index request)",
    "esDocumentId": "(intended OpenSearch Service document ID)",
    "esIndexName": "(intended OpenSearch Service index name)",
    "esTypeName": "(intended OpenSearch Service type name)",
    "rawData": "(base64-encoded document data)"
}
```

For OpenSearch Serverless, each document has the following JSON
format:

```

{
    "attemptsMade": "(number of index requests attempted)",
    "arrivalTimestamp": "(the time when the document was received by Firehose)",
    "errorCode": "(http error code returned by OpenSearch Serverless)",
    "errorMessage": "(error message returned by OpenSearch Serverless)",
    "attemptEndingTimestamp": "(the time when Firehose stopped attempting index request)",
    "osDocumentId": "(intended OpenSearch Serverless document ID)",
    "osIndexName": "(intended OpenSearch Serverless index name)",
    "rawData": "(base64-encoded document data)"
}

```

## Splunk

When Amazon Data Firehose sends data to Splunk, it waits for an acknowledgment from
Splunk. If an error occurs, or the acknowledgment doesn’t arrive within the
acknowledgment timeout period, Amazon Data Firehose starts the retry duration counter. It
keeps retrying until the retry duration expires. After that, Amazon Data Firehose considers
it a data delivery failure and backs up the data to your Amazon S3 bucket.

Every time Amazon Data Firehose sends data to Splunk, whether it's the initial attempt or
a retry, it restarts the acknowledgement timeout counter. It then waits for
an acknowledgement to arrive from Splunk. Even if the retry duration
expires, Amazon Data Firehose still waits for the acknowledgment until it receives it or
the acknowledgement timeout is reached. If the acknowledgment times out,
Amazon Data Firehose checks to determine whether there's time left in the retry counter. If
there is time left, it retries again and repeats the logic until it receives
an acknowledgment or determines that the retry time has expired.

A failure to receive an acknowledgement isn't the only type of data
delivery error that can occur. For information about the other types of data
delivery errors, see [Splunk Data Delivery Errors](monitoring-with-cloudwatch-logs.md#monitoring-splunk-errors "monitoring-with-cloudwatch-logs.md#monitoring-splunk-errors"). Any data delivery error triggers
the retry logic if your retry duration is greater than 0.

The following is an example error record.

```
{
  "attemptsMade": 0,
  "arrivalTimestamp": 1506035354675,
  "errorCode": "Splunk.AckTimeout",
  "errorMessage": "Did not receive an acknowledgement from HEC before the HEC acknowledgement timeout expired. Despite the acknowledgement timeout, it's possible the data was indexed successfully in Splunk. Amazon Data Firehose backs up in Amazon S3 data for which the acknowledgement timeout expired.",
  "attemptEndingTimestamp": 13626284715507,
  "rawData": "MiAyNTE2MjAyNzIyMDkgZW5pLTA1ZjMyMmQ1IDIxOC45Mi4xODguMjE0IDE3Mi4xNi4xLjE2NyAyNTIzMyAxNDMzIDYgMSA0MCAxNTA2MDM0NzM0IDE1MDYwMzQ3OTQgUkVKRUNUIE9LCg==",
  "EventId": "49577193928114147339600778471082492393164139877200035842.0"
}
```

## HTTP endpoint destination

When Amazon Data Firehose sends data to an HTTP endpoint destination, it waits for a
response from this destination. If an error occurs, or the response doesn’t
arrive within the response timeout period, Amazon Data Firehose starts the retry duration
counter. It keeps retrying until the retry duration expires. After that,
Amazon Data Firehose considers it a data delivery failure and backs up the data to your
Amazon S3 bucket.

Every time Amazon Data Firehose sends data to an HTTP endpoint destination, whether it's
the initial attempt or a retry, it restarts the response timeout counter. It
then waits for a response to arrive from the HTTP endpoint destination. Even
if the retry duration expires, Amazon Data Firehose still waits for the response until it
receives it or the response timeout is reached. If the response times out,
Amazon Data Firehose checks to determine whether there's time left in the retry counter. If
there is time left, it retries again and repeats the logic until it receives
a response or determines that the retry time has expired.

A failure to receive a response isn't the only type of data delivery error
that can occur. For information about the other types of data delivery
errors, see [HTTP Endpoint Data Delivery Errors](monitoring-with-cloudwatch-logs.md#monitoring-http-errors "monitoring-with-cloudwatch-logs.md#monitoring-http-errors")

The following is an example error record.

```
{
	"attemptsMade":5,
	"arrivalTimestamp":1594265943615,
	"errorCode":"HttpEndpoint.DestinationException",
	"errorMessage":"Received the following response from the endpoint destination. {"requestId": "109777ac-8f9b-4082-8e8d-b4f12b5fc17b", "timestamp": 1594266081268, "errorMessage": "Unauthorized"}",
	"attemptEndingTimestamp":1594266081318,
	"rawData":"c2FtcGxlIHJhdyBkYXRh",
	"subsequenceNumber":0,
	"dataId":"49607357361271740811418664280693044274821622880012337186.0"
}
```

## Snowflake

For Snowflake destination, when you create a Firehose stream, you can specify
an optional retry duration (0-7200 seconds). The default value for retry
duration is 60 seconds.

Data delivery to your Snowflake table might fail for several reasons like
an incorrect Snowflake destination configuration, Snowflake outage, a
network failure, etc. The retry policy doesn’t apply to non-retriable
errors. For example, if Snowflake rejects your JSON payload because it had
an extra column that's missing in the table, Firehose doesn’t attempt to
deliver it again. Instead, it creates a back up for all the insert failures
due to JSON payload issues to your S3 error bucket.

Similarly, if delivery fails due to an incorrect role, table, or database,
Firehose doesn’t retry and writes the data to your S3 bucket. Retry duration
only applies to failure due to a Snowflake service issue, transient network
glitches, etc. Under these conditions, Firehose retries for the specified time
duration before delivering them to S3. The failed records are delivered in
snowflake-failed/ folder, which you can use for manual backfill.

The following is an example JSON for each record that you deliver to S3.

```
{
    "attemptsMade": 3,
    "arrivalTimestamp": 1594265943615,
    "errorCode": "Snowflake.InvalidColumns",
    "errorMessage": "Snowpipe Streaming does not support columns of type AUTOINCREMENT, IDENTITY, GEO, or columns with a default value or collation",
    "attemptEndingTimestamp": 1712937865543,
    "rawData": "c2FtcGxlIHJhdyBkYXRh"
}
```
