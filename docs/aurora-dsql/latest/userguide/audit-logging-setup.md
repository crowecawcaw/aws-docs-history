

# Getting started with audit logging

In this guide, you set up audit log delivery for an Aurora DSQL cluster, choose which statements to audit, and confirm that audit records arrive in your Amazon S3 bucket.

## Prerequisites
<a name="audit-logging-prerequisites"></a>

Before you begin, confirm the following:
+ You've created an Aurora DSQL cluster, and the cluster has finished creating. For a multi-Region cluster, you've also finished setting up the multi-Region configuration. For instructions, see [Step 1: Create an Aurora DSQL single-Region cluster](getting-started.md#getting-started-create-cluster) or [Create a multi-Region cluster](getting-started.md#getting-started-multi-region).
+ You've created an Amazon S3 bucket to receive the audit records. Consider a bucket that you use only for audit logs, so that you can control who can access the records and how long you keep them. For more information, see [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and [Bucket policies for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) in the *Amazon S3 User Guide*.
+ Your IAM identity has the permissions listed in [Caller permissions](audit-logging-iam.md#audit-logging-permissions). To run the AWS CLI examples in this guide, install the AWS CLI and configure it with credentials for that identity.
+ You can connect to the cluster as a database role that can change audit settings, such as the built-in `admin` role. For more information, see [Audit administration roles](audit-logging-iam.md#audit-logging-roles).

## Setting up audit log delivery
<a name="audit-logging-set-up-delivery"></a>

In this step, you connect your cluster to your Amazon S3 bucket. You register the cluster as a delivery source and the bucket as a delivery destination, and then create a delivery that connects them. For a multi-Region cluster, set up delivery for the cluster in each AWS Region. For more information, see [Multi-Region audit logging configuration](audit-logging.md#audit-logging-multi-region).

------
#### [ Console ]

**To set up audit log delivery (console)**

1. Open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql).

1. In the navigation pane, choose **Clusters**, and then choose the ID of the cluster.

1. Choose the **Cluster settings** tab.

1. In the **Audit logging** section, choose **Enable**.

1. On the **Manage audit logging** page, specify the Amazon S3 bucket for the audit records.

1. On the **Manage audit logging** page, turn on delivery.

   Delivery can take a few minutes to start. After delivery starts, the **Audit logging** section on the **Cluster settings** tab shows **Enabled**.

To change the object path or choose the record fields, use the AWS CLI.

If the page shows an access denied error, make sure that your identity has the permissions in [Caller permissions](audit-logging-iam.md#audit-logging-permissions). If audit records don't arrive, see [Troubleshooting missing audit records](audit-logging-monitoring.md#audit-logging-troubleshooting).

------
#### [ CLI ]

In the following commands, replace {{region}} with the Region of your cluster, {{111122223333}} with your AWS account ID, {{cluster-id}} with the ID of your cluster, and {{amzn-s3-demo-destination-bucket}} with the name of your bucket. You can choose any names for the delivery source and the delivery destination.

**Register the cluster as a delivery source**  
Run the following AWS CLI command to register the cluster as a delivery source with the `AUDIT_LOGS` log type:

```bash
aws logs put-delivery-source \
  --name {{my-cluster-audit-logs}} \
  --resource-arn arn:aws:dsql:{{region}}:{{111122223333}}:cluster/{{cluster-id}} \
  --log-type AUDIT_LOGS \
  --region {{region}}
```

**Register the bucket as a delivery destination**  
Run the following AWS CLI command to register the Amazon S3 bucket as a delivery destination with the `json` output format:

```bash
aws logs put-delivery-destination \
  --name {{my-audit-log-destination}} \
  --output-format json \
  --delivery-destination-configuration destinationResourceArn=arn:aws:s3:::{{amzn-s3-demo-destination-bucket}} \
  --region {{region}}
```

Record the delivery destination ARN from the output. You need it in the next command. The ARN has the format `arn:aws:logs:{{region}}:{{111122223333}}:delivery-destination:{{my-audit-log-destination}}`.

**Create the delivery**  
Run the following AWS CLI command to connect the delivery source to the delivery destination:

```bash
aws logs create-delivery \
  --delivery-source-name {{my-cluster-audit-logs}} \
  --delivery-destination-arn arn:aws:logs:{{region}}:{{111122223333}}:delivery-destination:{{my-audit-log-destination}} \
  --region {{region}}
```

If the bucket policy doesn't already let CloudWatch Logs deliver logs to the bucket, CloudWatch Logs adds the required statement to the bucket policy. If a command fails with an access denied error, make sure that your identity has the permissions listed in [Caller permissions](audit-logging-iam.md#audit-logging-permissions). If audit records don't arrive, see [Troubleshooting missing audit records](audit-logging-monitoring.md#audit-logging-troubleshooting).

**Customize the object path and fields**  
By default, CloudWatch Logs delivers your audit records under `AWSLogs/{{111122223333}}/dsql/{{region}}/{{yyyy}}/{{MM}}/{{dd}}/{{HH}}/` in the bucket. To change the object path, use the `--s3-delivery-configuration` option of `create-delivery` or `update-delivery-configuration`. For more information, see [Amazon S3 object key format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html#AWS-logs-infrastructure-V2-S3-object-key) in the *Amazon CloudWatch Logs User Guide*.

To deliver only some of the fields of each audit record, use the `--record-fields` option of `create-delivery` or `update-delivery-configuration` with the fields in [Record fields](audit-logging-records.md#audit-logging-record-format). For example, the following command creates a delivery that includes only the fields that show who ran which command. In `DDL` and `FUNCTION` records, these fields also show the object of the command:

```bash
aws logs create-delivery \
  --delivery-source-name {{my-cluster-audit-logs}} \
  --delivery-destination-arn arn:aws:logs:{{region}}:{{111122223333}}:delivery-destination:{{my-audit-log-destination}} \
  --record-fields resource_arn event_timestamp iam_arn session_user class command object_type object_name \
  --region {{region}}
```

------

**Confirm that delivery is set up**  
Connect to your cluster and run the following SQL query. The query returns one row for each AWS Region of the cluster:

```sql
SELECT * FROM sys.audit_delivery_status();
```

The `has_delivery` column shows `t` (true) for each Region where the cluster has a delivery source, and `f` (false) for each Region where it doesn't. Audit records reach your bucket only when a delivery also connects the delivery source to a delivery destination. After you set up delivery, it can take a few minutes for the query to show the change.

The following example output shows a cluster that has a delivery source:

```
  region   | has_delivery
-----------+--------------
 us-east-1 | t
(1 row)
```

The following example output shows a cluster that doesn't have a delivery source. If the query shows `f` for a Region, set up delivery for the cluster in that Region.

```
  region   | has_delivery
-----------+--------------
 us-east-1 | f
(1 row)
```

## Creating an audit administrator role
<a name="audit-logging-setup-admin"></a>

This step is optional. By default, the built-in `admin` role can change audit settings. If your compliance requirements call for separation of duties, create a dedicated audit administrator role before you continue. For instructions on creating the role, see [Audit administration roles](audit-logging-iam.md#audit-logging-roles).

To also audit roles that you create later, such as roles that a database administrator creates, we recommend that you set a cluster-wide baseline with `ALTER SYSTEM`. For more information, see [Setting a cluster-wide baseline](audit-logging-configure.md#audit-logging-cluster-wide).

## Setting up audit logging
<a name="audit-logging-setup-configure"></a>

If you created an audit administrator role in the previous step, connect to your cluster as that role. Otherwise, connect as `admin`.

Then choose what to audit for each database role. The following SQL example audits the DDL statements, role and privilege changes, and writes of the `admin` role:

```sql
SELECT sys.set_audit_config('admin', 'dsql_audit.log', 'ddl,role,write');
```

To also record the number of rows that each statement read or changed, turn on `dsql_audit.log_rows` for the role:

```sql
SELECT sys.set_audit_config('admin', 'dsql_audit.log_rows', 'on');
```

To audit other roles, run the same statements with their names. Changes to audit settings apply to new connections, and can take a few minutes to apply. For all audit settings, see [Configuring audit settings](audit-logging-configure.md).

**Confirm your audit settings**  
Run the following SQL query to list the audit settings that you set for each role:

```sql
SELECT r.rolname, s.setconfig
FROM pg_db_role_setting s
JOIN pg_roles r ON r.oid = s.setrole;
```

The following example output shows the audit settings from the previous examples:

```
 rolname |                        setconfig
---------+----------------------------------------------------------
 admin   | {"dsql_audit.log=ddl,role,write",dsql_audit.log_rows=on}
(1 row)
```

To see the audit settings that apply to your connection, reconnect to your cluster as `admin`, and then run the following command. If the output doesn't show your changes, wait a few minutes and reconnect.

```sql
SHOW dsql_audit.log;
```

The following example output shows the setting from the previous examples. If the output is `none`, Aurora DSQL doesn't audit the statements of your connection.

```
 dsql_audit.log
----------------
 ddl,role,write
(1 row)
```

## Verifying that audit records arrive
<a name="audit-logging-setup-verify"></a>

Reconnect to your cluster as `admin`, and run a statement that your audit settings cover. For example, the following SQL statements create and drop a table, which generates `DDL` records:

```sql
CREATE TABLE audit_test (id int PRIMARY KEY);
DROP TABLE audit_test;
```

To verify that the audit records arrived, run the following AWS CLI command to list the audit log files in your bucket. Replace {{amzn-s3-demo-destination-bucket}} with the name of your bucket, and {{111122223333}} with your AWS account ID. It can take several minutes for records to arrive. If the output doesn't include any files, wait a few minutes and run the command again.

```bash
aws s3 ls s3://{{amzn-s3-demo-destination-bucket}}/AWSLogs/{{111122223333}}/dsql/ --recursive
```

To print the audit records of a file, run the following AWS CLI command. Replace {{object-key}} with the key of a file from the output of the previous command:

```bash
aws s3 cp s3://{{amzn-s3-demo-destination-bucket}}/{{object-key}} - | gunzip
```

Each line of the output is one audit record in JSON format. For an example record and descriptions of the fields, see [Understanding audit records](audit-logging-records.md). If records don't arrive, see [Troubleshooting missing audit records](audit-logging-monitoring.md#audit-logging-troubleshooting).

## Cleaning up
<a name="audit-logging-setup-clean-up"></a>

If you set up audit logging only to try it, turn it off to avoid ongoing charges.

First, connect to your cluster as `admin`, and reset the audit settings that you chose in [Setting up audit logging](#audit-logging-setup-configure). Reset them before you delete the delivery, because Aurora DSQL accepts changes to audit settings only while delivery is set up:

```sql
SELECT sys.reset_audit_config('admin', 'dsql_audit.log');
SELECT sys.reset_audit_config('admin', 'dsql_audit.log_rows');
```

Then run the following AWS CLI command to find the ID of the delivery. Replace {{region}} with the AWS Region of your cluster:

```bash
aws logs describe-deliveries \
  --region {{region}}
```

Run the following AWS CLI commands to delete the delivery, the delivery source, and the delivery destination. Replace {{delivery-id}} with the ID of the delivery from the output of the previous command:

```bash
aws logs delete-delivery \
  --id {{delivery-id}} \
  --region {{region}}

aws logs delete-delivery-source \
  --name {{my-cluster-audit-logs}} \
  --region {{region}}

aws logs delete-delivery-destination \
  --name {{my-audit-log-destination}} \
  --region {{region}}
```

To avoid charges for storing the audit records, delete the audit log files from your bucket. If you created the bucket only for this guide, you can delete the bucket.

## Managing audit log delivery
<a name="audit-logging-manage"></a>

**Listing deliveries**  
To list the deliveries in a Region, run the following AWS CLI command. Replace {{region}} with the AWS Region of your cluster:

```bash
aws logs describe-deliveries \
  --region {{region}}
```

The output includes the ID and the delivery source name of each delivery. You need the ID to delete a delivery.

**Turning off audit logging**  
To stop auditing statements, reset the audit settings. Reset them before you delete the delivery, because Aurora DSQL accepts changes to audit settings only while delivery is set up. Reset the settings of each role that you audit. The following SQL example resets the `dsql_audit.log` setting of the {{app\_user}} role:

```sql
SELECT sys.reset_audit_config('{{app_user}}', 'dsql_audit.log');
```

To stop delivering audit records, run the following AWS CLI commands to delete the delivery and the delivery source. Replace {{delivery-id}} with the ID of the delivery from the output of `describe-deliveries`, {{my-cluster-audit-logs}} with the name of the delivery source, and {{region}} with the AWS Region of your cluster:

```bash
aws logs delete-delivery \
  --id {{delivery-id}} \
  --region {{region}}

aws logs delete-delivery-source \
  --name {{my-cluster-audit-logs}} \
  --region {{region}}
```

**Deleting a cluster**  
When you delete a cluster, Aurora DSQL stops generating its audit records. Delete the delivery and the delivery source of the cluster, because they remain in CloudWatch Logs after you delete the cluster.