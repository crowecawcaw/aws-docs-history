# Best practices for integrating with DynamoDB

When integrating DynamoDB with other services, you should always follow the best practices for
using each individual service. However, there are some best practices specific to integration
that you should consider.

###### Topics

- [Creating a snapshot in DynamoDB](#bp-integration-snapshot "#bp-integration-snapshot")
- [Capturing data change in DynamoDB](#bp-integration-change-data-capture "#bp-integration-change-data-capture")

## Creating a snapshot in DynamoDB

- Generally, we recommend using [export to
  Amazon S3](S3DataExport.md "S3DataExport.md") to create snapshots for initial replication. It is both cost effective, and
  won't compete with your application's traffic for throughput. You can also consider a
  backup and restore to a new table followed by a scan operation. This will avoid competing
  for throughput with your application, but will generally be substantially less cost
  effective than an export.
- Always set a `StartTime` when doing an export. This makes it easy to
  determine where you'll start your change data capture (CDC) from.
- When using export to S3, set a lifecycle action on the S3 bucket. Typically, an
  expiration action set at 7 days is safe, but you should follow any guidelines that your
  company might have. Even if you explicitly delete your items after ingestion, this action
  can help catch issues, which helps reduce unnecessary costs and prevents policy
  violations.

## Capturing data change in DynamoDB

- If you need near real-time CDC, use [DynamoDB Streams](streamsmain.md "streamsmain.md")
  or [Amazon Kinesis Data Streams (KDS)](kds.md "kds.md"). When you're deciding which one to use,
  generally consider which is easiest to use with the downstream service. If you need to
  provide in-order event processing at a partition-key level, or if you have items that are
  exceptionally large, use DynamoDB Streams.
- If you don't need near real-time CDC, you can use [export to Amazon S3 with incremental exports](S3DataExport.md "S3DataExport.md") to
  export only the changes that have happened between two points in time.

If you used export to S3 for generating a snapshot, this can be especially helpful
because you can use similar code to process incremental exports. Typically, export to S3
is slightly cheaper than the previous streaming options, but cost is typically not the
main factor for which option to use.

- You can generally only have two simultaneous consumers of a DynamoDB stream. Consider
  this when planning your integration strategy.
- Don't use scans to detect changes. This might work on a small scale, but becomes
  impractical fairly quickly.
