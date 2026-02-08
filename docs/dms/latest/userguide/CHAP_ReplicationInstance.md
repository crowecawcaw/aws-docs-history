#

Rebooting a replication instance

You can reboot an AWS DMS replication instance to restart the replication engine. A
reboot results in a momentary outage for the replication instance, during which the
instance status is set to **Rebooting**. If the AWS DMS instance is
configured for Multi-AZ, the reboot can be conducted with a failover. An AWS DMS event is
created when the reboot is completed.

If your AWS DMS instance is a Multi-AZ deployment, you can force a planned failover from
one AWS Availability Zone to another when you reboot. When you force a planned failover of
your AWS DMS instance, AWS DMS closes out active connections on the current instance prior to
automatically switching to a standby instance in another Availability Zone. Rebooting with a
planned failover helps you simulate a planned failover event of an AWS DMS instance, such as
when scaling the replication instance class.

###### Note

After a reboot forces a failover from one Availability Zone to another, the
Availability Zone change might not be reflected for several minutes. This lag
appears in the AWS Management Console, and in calls to the AWS CLI and AWS DMS API.

If migration tasks are running on the replication instance when a reboot occurs,
no data loss occurs but the task stops, and the task status changes to an error state.

If the tables in the migration task are in the middle of a bulk load (full load phase)
and haven't yet started, they go into an error state. But tables that are complete
at that time, remain in a complete state. When a reboot happens during the full load phase,
we recommended that you perform either one of the steps below.

- Remove the tables that are in a complete state from the task, and restart the task
  with the remaining tables.
- Create a new task with tables in an error state, and with tables that are pending.
  If tables in the migration task are in the ongoing replication phase, the task resumes
  once the reboot is completed.

You can't reboot your AWS DMS replication instance if its status is not in the
**Available** state. Your AWS DMS instance can be unavailable for
several reasons, such as a previously requested modification or a maintenance-window
action. The time required to reboot an AWS DMS replication instance is typically small
(under 5 minutes).

To reboot a replication instance, use the AWS console.

###### To reboot a replication instance using the AWS console

1. Sign in to the AWS Management Console and open the AWS DMS console at
   [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose **Replication instances**.
3. Choose
   the replication instance you want to reboot.
4. Choose **Reboot**. The **Reboot replication instance**
   dialog box opens.
5. Select the check box for **Reboot with planned failover?** if you have
   configured your replication instance for Multi-AZ deployment and you want to fail over to another
   AWS Availability Zone.
6. Choose **Reboot**.
   To reboot a replication instance, use the AWS CLI [`reboot-replication-instance`](../../../cli/latest/reference/dms/reboot-replication-instance.md "../../../cli/latest/reference/dms/reboot-replication-instance.md") command with the following
   parameter:

- `--replication-instance-arn`

###### Example simple reboot

The following AWS CLI example reboots a replication instance.

```
aws dms reboot-replication-instance \
--replication-instance-arn `arn of my rep instance`
```

###### Example simple reboot with failover

The following AWS CLI example reboots a replication instance with failover.

```
aws dms reboot-replication-instance \
--replication-instance-arn `arn of my rep instance` \
--force-planned-failover

```

To reboot a replication instance, use the AWS DMS API [`RebootReplicationInstance`](../../../AmazonRDS/latest/APIReference/API_ModifyDBInstance.md "../../../AmazonRDS/latest/APIReference/API_ModifyDBInstance.md") action with the following
parameters:

- `ReplicationInstanceArn = `arn of my rep
  instance``

###### Example simple reboot

The following code example reboots a replication instance.

```
https://dms.us-west-2.amazonaws.com/
?Action=RebootReplicationInstance
&DBInstanceArn=`arn of my rep instance`
&SignatureMethod=HmacSHA256
&SignatureVersion=4
&Version=2014-09-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/dms/aws4_request
&X-Amz-Date=20140425T192732Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=1dc9dd716f4855e9bdf188c70f1cf9f6251b070b68b81103b59ec70c3e7854b3
```

###### Example simple reboot with failover

The following code example reboots a replication instance and fails over to
another AWS Availability Zone.

```
https://dms.us-west-2.amazonaws.com/
?Action=RebootReplicationInstance
&DBInstanceArn=`arn of my rep instance`
&ForcePlannedFailover=true
&SignatureMethod=HmacSHA256
&SignatureVersion=4
&Version=2014-09-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/dms/aws4_request
&X-Amz-Date=20140425T192732Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=1dc9dd716f4855e9bdf188c70f1cf9f6251b070b68b81103b59ec70c3e7854b3
```
