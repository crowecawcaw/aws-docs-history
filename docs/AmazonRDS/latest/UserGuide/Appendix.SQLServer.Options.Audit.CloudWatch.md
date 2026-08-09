# Configuring CloudWatch Log Stream

By default, Amazon RDS for SQL Server Audit delivers completed audit files to an Amazon S3 bucket.
You can also stream the audit logs to Amazon CloudWatch Logs — instead of Amazon S3, or in addition to it.

Streaming audit logs to Amazon CloudWatch Logs lets you:

- Store audit records in highly durable storage with a retention period you define.
- Search and filter audit log data, and build metric filters and CloudWatch alarms.
- Share log data between accounts and export it to Amazon S3.
- Stream data to , or process it in real time with .

## Enabling CloudWatch streaming

CloudWatch streaming is controlled by a single boolean setting,
`PUBLISH_TO_CLOUDWATCH`, on the `SQLSERVER_AUDIT` option.
Set it to `true` to stream audit logs to Amazon CloudWatch Logs, or `false` to stop.

###### Note

CloudWatch publishing does not require a customer IAM role. When
`PUBLISH_TO_CLOUDWATCH` is `true`, Amazon RDS manages delivery
of the audit logs to Amazon CloudWatch Logs for you — you don't need to create or attach any
IAM role or permissions for it. Because CloudWatch can be a standalone destination,
`IAM_ROLE_ARN` and `S3_BUCKET_ARN` are optional —
supply them only if you also want the S3 destination. At least one destination
(CloudWatch, S3, or both) must be configured.

### On a new option group

When you add the `SQLSERVER_AUDIT` option to an option group
(see [Adding SQL Server Audit to the DB instance options](Appendix.SQLServer.Options.Audit.Adding.md "Appendix.SQLServer.Options.Audit.Adding.md") for the full steps),
set the `PUBLISH_TO_CLOUDWATCH` setting to `true`.

### On an existing option group

###### To enable CloudWatch streaming on an existing option group

1. Open the Amazon RDS console, choose **Option groups**, and open the
   option group attached to your DB instance.
2. Choose **Modify option group**.
3. On the existing `SQLSERVER_AUDIT` option, set the
   `PUBLISH_TO_CLOUDWATCH` setting to `true`.
4. Save the changes, choosing whether to apply them immediately or during the
   next maintenance window.

Because a single option group can be shared by multiple DB instances, this change
affects every DB instance that uses that option group. To change only one instance,
use a separate option group for it.

After the option group is active you don't need to restart the DB instance —
audit logs begin streaming to Amazon CloudWatch Logs as soon as the change applies. To stop
streaming, set `PUBLISH_TO_CLOUDWATCH` back to `false`.

## Where the audit logs appear in CloudWatch

Amazon RDS publishes the SQL Server audit logs to an RDS-managed CloudWatch Logs log group named:

```
/aws/rds/instance/`db_instance_name`/sqlaudit
```

Within this log group, each node publishes to its own log stream, identified by the
node identifier. For Multi-AZ (Always On) instances, the primary and secondary each
write to a separate log stream in the same `sqlaudit` log group,
distinguished by their node identifier — so audit events from both replicas
are captured independently.

## Version availability

Streaming audit logs to CloudWatch is available on any engine version and edition
that supports SQL Server Audit — there is no additional version restriction
beyond the base SQL Server Audit support.
