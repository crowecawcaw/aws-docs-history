

# Monitoring audit logging

If you haven't set up audit log delivery for a cluster, the cluster doesn't generate audit records. To get notified when this happens, create a CloudWatch alarm on the `AuditLogDeliveryNotConfigured` metric. For more information, see [CloudWatch metrics for audit logging](#audit-logging-monitoring-metrics).

Use [CloudWatch metrics](#audit-logging-monitoring-metrics) and the [delivery status](#audit-logging-troubleshooting) of your cluster to confirm that the cluster generates audit records and has a delivery source in each Region. If a change to audit settings fails, see [Error message reference](#audit-logging-error-reference).

## CloudWatch metrics for audit logging
<a name="audit-logging-monitoring-metrics"></a>

Use the following CloudWatch metrics to monitor audit logging for each cluster. Aurora DSQL publishes these metrics in the `AWS/AuroraDSQL` namespace with the `ClusterId` dimension.


| Metric name | Useful statistic | Description | 
| --- |--- |--- |
| AuditLogRecordsGenerated | Sum | The number of audit records that the cluster generated during the period. | 
| AuditLogRecordsByCategory | Sum | The number of audit records that the cluster generated for each statement class during the period. This metric also uses the Category dimension, whose value is the class of the records, such as READ, WRITE, or DDL. | 
| AuditLogMeteredBytes | Sum | The number of audit record bytes that Aurora DSQL metered for billing during the period. | 
| AuditLogDeliveryNotConfigured | Sum | The number of transactions that didn't generate audit records because audit log delivery isn't set up for the cluster. | 

For the other metrics that Aurora DSQL publishes, see [Monitoring Aurora DSQL with Amazon CloudWatch](cloudwatch-monitoring.md).

## Troubleshooting missing audit records
<a name="audit-logging-troubleshooting"></a>

If audit records don't arrive in your bucket after several minutes, follow these steps.

1. **Check the delivery status.** Run the following SQL query, and confirm that `has_delivery` is `t` for the Region of the cluster. If it's `f`, set up delivery for the cluster. For instructions on setting up delivery, see [Setting up audit log delivery](audit-logging-setup.md#audit-logging-set-up-delivery).

   ```sql
   SELECT * FROM sys.audit_delivery_status();
   ```

1. **Check the delivery.** Run the following AWS CLI command, and confirm that a delivery connects the delivery source of the cluster to your bucket. Replace {{region}} with the AWS Region of your cluster:

   ```bash
   aws logs describe-deliveries \
     --region {{region}}
   ```

1. **Check the audit settings.** Connect as the role that you want to audit, and run `SHOW dsql_audit.log;`. If the result is `none`, Aurora DSQL doesn't audit the role's statements. To change the setting, see [Configuring audit settings](audit-logging-configure.md).

1. **Check the metrics.** Check the `AuditLogRecordsGenerated` metric to confirm that the cluster generates audit records. If the `AuditLogDeliveryNotConfigured` metric is greater than `0`, delivery isn't set up.

1. **Check the bucket and key policies.** Confirm that the bucket still exists and that its bucket policy lets CloudWatch Logs write to it. Also confirm that the key policies of the AWS KMS keys of the bucket and the cluster allow log delivery, and that the keys are enabled. For more information, see [Data protection](audit-logging-iam.md#audit-logging-data-protection).

If audit records arrive but some fields contain `<not logged>`, see [Format details](audit-logging-records.md#audit-logging-format-details).

## Error message reference
<a name="audit-logging-error-reference"></a>

When a change to audit settings fails, the error message identifies the cause. For example, the following error occurs when a cluster doesn't have a delivery source:

```
ERROR:  cannot change audit configuration parameter "dsql_audit.log" while a region has no audit delivery
DETAIL:  No audit delivery exists in: us-east-2.
HINT:  Make sure audit delivery exists in all regions before setting audit parameters.
```

The following table describes each error message, its cause, and the steps to resolve it.


| Error message | Cause | How to resolve | 
| --- |--- |--- |
| cannot change audit configuration parameter "{{parameter}}" while a region has no audit delivery | One or more clusters in the cluster group don't have a delivery source. The DETAIL line lists their Regions. For example, you haven't set up delivery for a restored cluster, or someone deleted the delivery source of the cluster. If you set up delivery a few minutes ago, the change might not have taken effect yet. | Set up delivery for the cluster in each Region that the error lists. Run SELECT \* FROM sys.audit\_delivery\_status(); to confirm that has\_delivery is t for every Region. Then change the audit setting again. | 
| cannot change audit configuration parameter "{{parameter}}" while the cluster group's regions are unknown | Aurora DSQL can't determine the Regions of the cluster group. This error can occur while you set up a multi-Region cluster. | Finish peering the clusters, and wait until every cluster in the cluster group is in ACTIVE status. Then change the audit setting again. For more information, see [Configuring multi-Region clusters](configuring-multi-region-clusters.md). | 
| permission denied for function set\_audit\_config | The role that you connected as isn't a member of pg\_dsql\_audit\_admin. | Connect as admin or as a member of pg\_dsql\_audit\_admin. Alternatively, ask an administrator to grant pg\_dsql\_audit\_admin to your role. For more information, see [Audit administration roles](audit-logging-iam.md#audit-logging-roles). | 
| permission denied to set parameter "{{parameter}}" | Either the parameter isn't one of the audit settings that you can change, for example because the name is misspelled, or you ran SET for an audit setting as a role that isn't admin or a member of pg\_dsql\_audit\_admin. | Use one of the settings in [Audit settings](audit-logging-configure.md#audit-logging-settings). | 