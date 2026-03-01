# Monitoring replication with metrics, event notifications, and statuses

You can monitor your live replication configurations and your S3 Batch Replication jobs
through the following mechanisms:

- **S3 Replication metrics** – When you enable
  S3 Replication metrics, Amazon CloudWatch emits metrics that you can use to track bytes pending, operations
  pending, and replication latency at the replication rule level. You can view
  S3 Replication metrics through the Amazon S3 console and the Amazon CloudWatch console. In the Amazon S3 console, you
  can view these metrics in the source bucket's **Metrics** tab. For more
  information about S3 Replication metrics, see [Using S3 Replication metrics](repl-metrics.md "repl-metrics.md").
- **S3 Storage Lens metrics** – In addition to
  S3 Replication metrics, you can use the replication-related Data Protection metrics provided by
  S3 Storage Lens dashboards. For example, if you use the free metrics in S3 Storage Lens, you can see
  metrics such as the total number of bytes that are replicated from the source bucket or the
  count of replicated objects from the source bucket.

To audit your overall replication stance, you can enable advanced metrics in S3 Storage Lens.
With advanced metrics in S3 Storage Lens, you can see how many replication rules you have of
various types, including the count of replication rules with a replication destination
that's not valid.

For more information about working with replication metrics in S3 Storage Lens, see [Viewing replication metrics in S3 Storage Lens dashboards](viewing-replication-metrics-storage-lens.md "viewing-replication-metrics-storage-lens.md").

- **S3 Event Notifications** – S3 Event Notifications
  can notify you at the object level in instances when objects don't replicate to their
  destination AWS Region or when objects aren't replicated within certain thresholds. S3
  Event Notifications provides the following replication event types:
  `s3:Replication:OperationFailedReplication`,
  `s3:Replication:OperationMissedThreshold`,
  `s3:Replication:OperationReplicatedAfterThreshold`, and
  `s3:Replication:OperationNotTracked`.

Amazon S3 events are available through Amazon Simple Queue Service (Amazon SQS), Amazon Simple Notification Service (Amazon SNS), or AWS Lambda.
For more information, see [Receiving replication failure events with Amazon S3 Event Notifications](replication-metrics-events.md "replication-metrics-events.md").

- **Replication status values** – You can also
  retrieve the replication status of your objects. The replication status can help you
  determine the current state of an object that's being replicated. The replication status of
  a source object will return either `PENDING`, `COMPLETED`, or
  `FAILED`. The replication status of a replica will return `REPLICA`.

You can also use replication status values when you're creating S3 Batch Replication
jobs. For example, you can use these status values to replicate objects that have either
never been replicated or that have failed replication.

For more information about retrieving the replication status of your objects, see [Getting replication status information](replication-status.md "replication-status.md"). For more information about using these values with
Batch Replication, see [Filters for a Batch Replication job](s3-batch-replication-batch.md#batch-replication-filters "s3-batch-replication-batch.md#batch-replication-filters").

###### Topics

- [Using S3 Replication metrics](repl-metrics.md "repl-metrics.md")
- [Viewing replication metrics in S3 Storage Lens dashboards](viewing-replication-metrics-storage-lens.md "viewing-replication-metrics-storage-lens.md")
- [Receiving replication failure events with Amazon S3 Event Notifications](replication-metrics-events.md "replication-metrics-events.md")
- [Getting replication status information](replication-status.md "replication-status.md")
