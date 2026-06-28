# Working with the AWS DMS maintenance window

Every AWS DMS replication instance has a weekly maintenance window during which any
available system changes are applied. You can think of the maintenance window as an
opportunity to control when modifications and software patching occurs.

If AWS DMS determines that maintenance is required during a given week, the
maintenance occurs during the 30-minute maintenance window you chose when you
created the replication instance. AWS DMS completes most maintenance during the
30-minute maintenance window. However, a longer time might be required for larger
changes.

## Effect of maintenance on existing migration tasks

When an AWS DMS migration task is running on an instance, the following events
occur when a patch is applied:

- If the tables in the migration task are in the replicating ongoing changes phase (CDC),
  AWS DMS stops the task for a moment and then resumes it after the patch is applied. The
  migration then continues from where it was interrupted when the patch was applied.
- If AWS DMS is migrating a table as part of a **migrate existing data** or
  **migrate existing data and replicate ongoing changes** task, DMS stops and
  then restarts the migration for all tables that are in full load phase while the patch is
  applied. DMS also stops and resumes all tables that are in CDC phase while the patch
  is applied.

## Changing the maintenance window setting

You can change the maintenance window time frame using the AWS Management Console,
the AWS CLI, or the AWS DMS API.

You can change the maintenance window time frame using the AWS Management Console.

###### To change the preferred maintenance window using the console

1. Sign in to the AWS Management Console and open the AWS DMS console at
   [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose
   **Replication instances**.
3. Choose the replication instance you want to
   modify and choose **Modify**.
4. Expand the **Maintenance** tab and choose a date and time for your
   maintenance window.
5. Choose **Apply changes immediately**.
6. Choose **Modify**.
   To adjust the preferred maintenance window, use the AWS CLI [`modify-replication-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command with the
   following parameters.

- `--replication-instance-identifier`
- `--preferred-maintenance-window`

###### Example

The following AWS CLI example sets the maintenance window to Tuesdays from
4:00–4:30 a.m. UTC.

```
aws dms modify-replication-instance \
--replication-instance-identifier `myrepinstance` \
--preferred-maintenance-window `Tue:04:00-Tue:04:30`
```

To adjust the preferred maintenance window, use the AWS DMS API [`ModifyReplicationInstance`](../../../AmazonRDS/latest/APIReference/API_ModifyDBInstance.md "../../../AmazonRDS/latest/APIReference/API_ModifyDBInstance.md") action with the
following parameters.

- `ReplicationInstanceIdentifier =
 `myrepinstance``
- `PreferredMaintenanceWindow = `Tue:04:00-Tue:04:30``

###### Example

The following code example sets the maintenance window to Tuesdays from
4:00–4:30 a.m. UTC.

```
https://dms.us-west-2.amazonaws.com/
?Action=ModifyReplicationInstance
&DBInstanceIdentifier=myrepinstance
&PreferredMaintenanceWindow=Tue:04:00-Tue:04:30
&SignatureMethod=HmacSHA256
&SignatureVersion=4
&Version=2014-09-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/dms/aws4_request
&X-Amz-Date=20140425T192732Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=1dc9dd716f4855e9bdf188c70f1cf9f6251b070b68b81103b59ec70c3e7854b3
```
