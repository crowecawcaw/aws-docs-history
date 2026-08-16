# Exporting query analysis logs

AWS Clean Rooms runs SQL queries on Apache Spark. When a query fails or runs slowly, the Spark logs
for that query contain the execution detail you need to find the cause. They show which stage
failed, how work was distributed across tasks, how much memory was used, and where time was
spent.

A query runs across data contributed by several collaboration members. Raw Spark logs can
therefore reveal information about another member's data, such as table names, storage
locations, and data values. For that reason, AWS Clean Rooms does not give you the raw logs. Instead,
it produces a _redacted_ copy in which customer data and
member metadata are redacted. AWS Clean Rooms exports that copy to an Amazon S3 bucket that you own. You
then analyze the exported logs with the tooling of your choice, such as Spark History
Server.

###### Important

Exported logs are redacted. Data values are removed, and counts and sizes are reported
as approximations so that they do not reveal details about the data in the collaboration.
As a result, the exported logs do not match the logs that a Spark job produces outside of
AWS Clean Rooms. Before you interpret them, read [Understanding redacted logs](export-analysis-logs-contents.md "export-analysis-logs-contents.md").

## Prerequisites

Before you can export logs for a query, all of the following must be true:

- Your membership has the `CAN_EXPORT_QUERY_ANALYSIS_LOG` member
  ability. Every collaboration member must approve a change request to grant this
  ability. For more information, see [Update member abilities](change-requests.md#update-member-abilities-change-request "change-requests.md#update-member-abilities-change-request").
- You are the query runner or the payer of the query. Having the ability is not
  sufficient on its own: you can export logs only for queries that you ran or that
  you paid for.
- The query has reached a terminal state. You can export logs for a query with
  a status of `SUCCESS`, `FAILED`, `CANCELLED`, or
  `TIMED_OUT`. You can't export logs while a query is still
  running.

Log export isn't available for every query. For the cases that aren't supported, see
[Considerations and limitations](#export-analysis-logs-limitations "#export-analysis-logs-limitations").

You don't need to create an IAM role for log export. AWS Clean Rooms writes the exported logs
using your own identity, so it writes the logs only where your own permissions already
allow. As a least-privilege practice, grant write access only to the bucket and key
prefix that you use for exported logs.

###### Note

If the destination bucket uses SSE-KMS with a customer managed key, you must have
permission to use that key. If you don't, the export request fails
immediately.

## Exporting logs for a query

Log export is asynchronous. When you start an export, AWS Clean Rooms returns immediately with
an export ID and a status of `IN_PROGRESS`, then redacts and copies the logs
in the background.

Before starting the export, AWS Clean Rooms writes a zero-byte object named
`validationSuccess` to your destination bucket to confirm that it can write
there. If this check fails, the request fails immediately with a validation error instead
of failing later in the background.

Console

###### To export logs for a query (console)

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that contains the query.
4. Choose the **Analysis** tab.
5. Do either of the following:

   - In the table of queries, select the query, choose
     **Actions**, and then choose
     **Export query analysis logs**.
   - Choose the query to open its details page, and then choose
     **Export analysis logs**.

6. In the dialog box, choose the destination Amazon S3 bucket and,
   optionally, a key prefix.
7. Choose **Export**.

If the **Export query analysis logs** option is
unavailable, the console explains why. The following table lists the messages
and how to resolve them.

| Message                                                                      | Resolution                                                                                      |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Query must reach a terminal state before logs can be<br>exported.            | Wait for the query to finish running.                                                           |
| You don't have the ability to export query analysis<br>logs.                 | Ask a collaboration member to submit a change request<br>adding the ability to your membership. |
| Log export is not supported for queries that use<br>differential privacy.    | None. Log export isn't available for these<br>queries.                                          |
| Only the query runner or the payer of the query can<br>export analysis logs. | Ask the member who ran or paid for the query to export the<br>logs.                             |

The query details page includes an **Export history**
table listing each export and its status. Choose a failed export to see the
error, or choose **View destination** to open the exported
logs in Amazon S3.

API
**To export logs for a query (API)**

Call `StartAnalysisLogExport`, specifying the membership, the
protected query, and your destination.

```
`aws cleanrooms start-analysis-log-export \
 --membership-identifier `membership-id` \
 --analysis-id `protected-query-id` \
 --analysis-type PROTECTED_QUERY \
 --result-configuration '{
 "outputConfiguration": {
 "s3": {
 "bucket": "`amzn-s3-demo-bucket`",
 "keyPrefix": "`query-logs/`"
 }
 }
 }'`
```

The response returns an `analysisLogExport` object containing an
`analysisLogExportId` and a `status` of
`IN_PROGRESS`.

To check on an export, call `GetAnalysisLogExport` with the
membership identifier and the export identifier, and poll until the status is
`SUCCESS` or `FAILED`. When an export fails, the
response includes an `error` field with a code and a
message.

```
`aws cleanrooms get-analysis-log-export \
 --membership-identifier `membership-id` \
 --analysis-log-export-identifier `analysis-log-export-id``
```

To list the exports for a membership, call
`ListAnalysisLogExports`. You can filter the results by query
using `analysisIdentifier`, and by the status of the export using
`status`. The `status` filter accepts
`IN_PROGRESS`, `SUCCESS`, or `FAILED`, and
takes one value at a time. These are the statuses of the export itself, not of
the query whose logs you exported. The results are paginated.

```
`aws cleanrooms list-analysis-log-exports \
 --membership-identifier `membership-id` \
 --analysis-identifier `protected-query-id` \
 --status SUCCESS`
```

Only one export can be active at a time for a given query and destination. If you
start an export while another export for the same query and the same Amazon S3 destination is
still in progress, the request fails with a validation error. To export the same query
twice at once, use a different key prefix for the second export.

You export independently of other members. If you and another member both have the
ability and both ran or paid for the same query, each of you can export the logs to your
own destination.

## Where the exported logs are written

AWS Clean Rooms writes the exported logs under the bucket and key prefix that you specify, using
the following structure:

```
s3://`your-bucket`/`key-prefix`/collaboration=`collaboration-id`/analysis=`protected-query-id`/`analysis-log-export-id`/
```

Because the path includes the export ID, exporting the same query more than once
doesn't overwrite the logs from an earlier export.

An export contains the redacted Spark event log for the query. This log is a set of
structured JSON records covering jobs, stages, tasks, timings, and query plans. Spark
itself writes this event log format. You can process an export with any tool that
reads Spark event logs, including your own tooling. AWS Clean Rooms doesn't provide a viewer for
exported logs. Within the export directory, the records follow the layout that Spark uses
for a rolling event log. A directory named
`eventlog_v2_`protected-query-id`` holds one or
more `events_` files and an `appstatus_` file that records that
the application completed. The directory and file names use the
protected query ID rather than an internal AWS Clean Rooms identifier.

Spark History Server is one such tool. To view an export in Spark History Server,
point an instance at the `eventlog_v2_` directory for the query. For example, an export of query
`6ba7b810-9dad-11d1-80b4-00c04fd430c8` to the bucket
`amzn-s3-demo-bucket` with the key prefix `query-logs/` produces the
following.

```
s3://amzn-s3-demo-bucket/query-logs/
  collaboration=f47ac10b-58cc-4372-a567-0e02b2c3d479/
    analysis=6ba7b810-9dad-11d1-80b4-00c04fd430c8/
      a1b2c3d4-e5f6-7890-abcd-ef1234567890/
        eventlog_v2_6ba7b810-9dad-11d1-80b4-00c04fd430c8/
          events_1_6ba7b810-9dad-11d1-80b4-00c04fd430c8
          appstatus_6ba7b810-9dad-11d1-80b4-00c04fd430c8
```

In this example, set the Spark History Server log directory to the following. Pointing
at the `eventlog_v2_` directory renders only the query that you exported.
Reading the logs directly from Amazon S3 requires the S3A connector, so use the
`s3a://` scheme. The credentials that Spark History Server runs with need read
access to the bucket.

```
spark.history.fs.logDirectory s3a://amzn-s3-demo-bucket/query-logs/collaboration=f47ac10b-58cc-4372-a567-0e02b2c3d479/analysis=6ba7b810-9dad-11d1-80b4-00c04fd430c8/a1b2c3d4-e5f6-7890-abcd-ef1234567890/eventlog_v2_6ba7b810-9dad-11d1-80b4-00c04fd430c8/
```

Use Spark History Server version 3.5.0 or later. You are responsible for setting up and
running your own instance. For information about running a Spark History Server
instance, see [Viewing after the fact](https://spark.apache.org/docs/latest/monitoring.html#viewing-after-the-fact "https://spark.apache.org/docs/latest/monitoring.html#viewing-after-the-fact") on the Apache Spark website.

## Troubleshooting log export

The request fails because you don't have permission to export logs

Your membership doesn't have the
`CAN_EXPORT_QUERY_ANALYSIS_LOG` ability. A collaboration member
must submit a change request to add the ability, and all members must
approve it. For more information, see [Update member abilities](change-requests.md#update-member-abilities-change-request "change-requests.md#update-member-abilities-change-request").

The request fails because the bucket can't be written to

Verify that the bucket exists, that it's in the same AWS Region as the
collaboration, and that you have permission to write to it. If the bucket
policy denies `s3:PutObject`, or restricts writes to a specific
VPC endpoint, AWS Clean Rooms can't write to the bucket.

If the bucket uses SSE-KMS with a customer managed key, this error might
also mean that you don't have permission to use that key. Confirm that the key
policy allows you to call `kms:GenerateDataKey` and
`kms:Decrypt` through Amazon S3.

The export fails because the query never ran

The query reached a terminal state without running on Spark, so no logs
were produced. This happens when a query fails validation or is cancelled
before it starts. The export fails with an error code of
`LOGS_NOT_AVAILABLE` and a message reporting that no query
execution logs are available for the query. There is nothing to
export.

The request fails because the query ran before log export was available

Redacted logs are produced while a query runs. A query that ran before log
export became available in AWS Clean Rooms produced none, so there is nothing to
export. To get logs for the same analysis, run the query again and export the
logs for the new run.

The request fails because a quota was exceeded

You have reached the maximum number of exports that can be in progress at
the same time. Wait for an in-progress export to finish, then retry.

The export starts but then fails

The initial permission check confirms only that AWS Clean Rooms can write to your
bucket at the moment you start the export. If your permissions change, or if
the credentials used for the export are revoked while the export is running,
the export fails after it has started. Call
`GetAnalysisLogExport` to see the error, resolve the cause, and
start a new export.

The export fails and reports an internal error

An internal error might mean that no logs were produced for the query.
You can retry the export.

The exported logs appear incomplete

If the query ended because a process ran out of memory, some log output
might be missing, because logs held on a host that stops abruptly aren't
recovered. The logs that were already written are still exported.

There is a zero-byte `validationSuccess` object in the
bucket

AWS Clean Rooms writes this object at the key prefix that you specified, to verify
that it can write to your destination before starting an export. It's separate
from the exported logs, which are written under the export's own directory,
and you can delete it. End your key prefix with a slash so that this object is
created inside the prefix rather than beside it.

## Considerations and limitations

- You can export logs for SQL queries run after August 11, 2026. Log export
  doesn't support PySpark jobs.
- Log export isn't supported for queries that failed validation or were
  cancelled before reaching the `STARTED` status.
- Log export isn't supported for queries that use differential privacy. For more
  information, see [AWS Clean Rooms Differential Privacy](differential-privacy.md "differential-privacy.md").
- The destination bucket for log export must be in the same AWS Region as the
  collaboration. Cross-Region export isn't supported.
- Securing the destination bucket for log export is your responsibility. Block
  public access to the bucket, and enable server access logging if you need a
  record of who reads the exported logs.
- AWS Clean Rooms doesn't accept a AWS KMS key for log export. Exported logs are encrypted
  using the default encryption configuration of the destination Amazon S3 bucket. To
  encrypt them with a customer managed key, configure the bucket's default
  encryption to use that key before you export.
- Log export supports only queries that reached a terminal state:
  `SUCCESS`, `FAILED`, `CANCELLED`, or
  `TIMED_OUT`.
- You can't cancel an export after it starts.

For quotas that apply to log export, including the number of exports that can run at
the same time, see [Quotas for AWS Clean Rooms](quotas.md "quotas.md").
