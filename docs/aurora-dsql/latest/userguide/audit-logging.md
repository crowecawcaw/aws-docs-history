

# Audit logging

With Amazon Aurora DSQL audit logging, you can record the SQL statements that run on your cluster and deliver the audit records to an Amazon Simple Storage Service (Amazon S3) bucket that you own. Each audit record contains details about a statement that ran. Audit records are delivered to your bucket as gzip-compressed files, with one JSON audit record on each line. For details, see [Understanding audit records](audit-logging-records.md).

## How it works
<a name="audit-logging-how-it-works"></a>

Audit logging has two parts. Aurora DSQL delivers audit records only when both parts are in place:
+ **Audit log delivery** – Determines where audit records go. For each cluster, you use [Amazon CloudWatch Vended Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) to deliver the cluster's audit records to an Amazon S3 bucket.
+ **Audit settings** – Determine which statements Aurora DSQL records. You use SQL to choose the classes of statements to audit for each database role.

You must set up audit log delivery before you can change audit settings. For instructions on setting up audit logging, see [Getting started with audit logging](audit-logging-setup.md).

Audit logging complements AWS CloudTrail. CloudTrail records Aurora DSQL API calls and connection attempts. Audit logs record the SQL statements that run on a connection. For more information about CloudTrail, see [Logging Aurora DSQL operations using AWS CloudTrail](logging-using-cloudtrail.md).

## Topics on this page
<a name="audit-logging-topics-on-page"></a>
+ [Multi-Region audit logging configuration](#audit-logging-multi-region)
+ [Audit logging for restored clusters](#audit-logging-restored-clusters)
+ [Pricing](#audit-logging-pricing)

## Related topics
<a name="audit-logging-related-topics"></a>
+ [Getting started with audit logging](audit-logging-setup.md)
+ [Configuring permissions](audit-logging-iam.md)
+ [Configuring audit settings](audit-logging-configure.md)
+ [Understanding audit records](audit-logging-records.md)
+ [Monitoring audit logging](audit-logging-monitoring.md)

## Multi-Region audit logging configuration
<a name="audit-logging-multi-region"></a>

In a multi-Region cluster, all clusters in the cluster group share the same audit settings, such as which classes of statements to audit. A change that you make on one cluster applies to every cluster in the same cluster group. Audit log delivery applies only to a single cluster, so set up delivery for the cluster in each AWS Region of the cluster group. If a Region doesn't have delivery, changes to audit settings fail, and the error lists the Regions without delivery. For more information about multi-Region clusters, see [Configuring multi-Region clusters](configuring-multi-region-clusters.md).

## Audit logging for restored clusters
<a name="audit-logging-restored-clusters"></a>

When you restore a backup to a new cluster, the new cluster has the audit settings of the backup, but not its audit log delivery. Set up delivery for the restored cluster. Until you do, audit records aren't generated for the restored cluster. The `AuditLogDeliveryNotConfigured` metric counts the affected transactions. For more information about restoring clusters, see [Restoring your backups](backup-aurora-dsql.md#restore-operations).

## Pricing
<a name="audit-logging-pricing"></a>

Audit logging will incur Aurora DSQL DPU charges, charges for log delivery through CloudWatch Logs, and charges for storing audit records in Amazon S3. On your monthly AWS bill, DPU charges appear under Aurora DSQL, CloudWatch Logs charges appear under CloudWatch, and storage charges appear under Amazon S3. For pricing information, see the [Aurora DSQL pricing](https://aws.amazon.com/rds/aurora/dsql/pricing/), [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/), and [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

We recommend that you audit only the classes of statements that can change data or permissions: `ddl`, `role`, and `write`. Auditing every statement, including reads, can produce a large volume of audit records and increase your log delivery and storage charges. For more information, see [Statement classes](audit-logging-configure.md#audit-logging-classes).