#

Deleting a replication instance

You can delete an AWS DMS replication instance when you are finished using it. If you
have migration tasks that use the replication instance, you must stop and delete the
tasks before deleting the replication instance.

If you close your AWS account, all AWS DMS resources and configurations associated
with your account are deleted after two days. These resources include all replication
instances, source and target endpoint configuration, replication tasks, and SSL
certificates. If after two days you decide to use AWS DMS again, you recreate the
resources you need.

If your replication instance meets all the criteria for deletion, and it stays in the
`DELETING` status for an extended period of time, contact support to troubleshoot the issue.

To delete a replication instance, use the AWS console.

###### To delete a replication instance using the AWS console

1. Sign in to the AWS Management Console and open the AWS DMS console at
   [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose **Replication instances**.
3. Choose
   the replication instance you want to delete.
4. Choose **Delete**.
5. In the dialog box, choose **Delete**.
   To delete a replication instance, use the AWS CLI [`delete-replication-instance`](../../../cli/latest/reference/dms/delete-replication-instance.md "../../../cli/latest/reference/dms/delete-replication-instance.md") command with the following
   parameter:

- `--replication-instance-arn`

###### Example delete

The following AWS CLI example deletes a replication instance.

```
aws dms delete-replication-instance \
--replication-instance-arn `arn of my rep instance`
```

To delete a replication instance, use the AWS DMS API [`DeleteReplicationInstance`](../APIReference/API_DeleteReplicationInstance.md "../APIReference/API_DeleteReplicationInstance.md") action with the
following parameters:

- `ReplicationInstanceArn = `arn of my rep
  instance``

###### Example delete

The following code example deletes a replication instance.

```
https://dms.us-west-2.amazonaws.com/
?Action=DeleteReplicationInstance
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
