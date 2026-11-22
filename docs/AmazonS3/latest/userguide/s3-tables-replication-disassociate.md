

# Disassociating a replica table from replication

Replica tables that S3 Tables replication maintains are read-only. To write to a replica table, you can disassociate it from replication. The table becomes a standalone table in place, like a table that you create with the `CreateTable` operation. It keeps the same table bucket, namespace, and name, and the data that was already replicated to it. You can read from it, write to it, and use it as the source of a new replication configuration.

For example, you can disassociate a replica table to keep writing to your data from another AWS Region during a Regional disruption, or to give another team or account its own writable copy of a production table.

You can disassociate a replica table by using the Amazon S3 console, the AWS CLI, the AWS SDKs, or the [DisassociateTableReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DisassociateTableReplication.html) API operation.

## What happens when you disassociate a replica table
<a name="s3-tables-replication-disassociate-what-happens"></a>

When you disassociate a replica table, the following changes occur:
+ **Replication to the table stops permanently** – S3 Tables replication stops copying updates from the source table to the table, including updates that it hadn't committed to the table yet. You can't associate the table with its source table again. On the source table, `GetTableReplicationStatus` returns `FAILED` for the disassociated destination, with the failure message `The destination table has been detached from replication and is no longer accepting replicated data`. For more information, see [Replication status values](s3-tables-replication-managing.md#s3-tables-replication-status-values).
+ **The table becomes a standalone table** – The `GetTable` response no longer includes the `managedByService` and `managedTableInformation` fields, and the `ListTables` response no longer includes the `managedByService` field for the table.
+ **Writes might not succeed right away** – It can take a few minutes before you can write to the table. During this time, write requests to the table might fail with an access denied (403) error. If this happens, retry the request.
+ **You can turn on compaction for the table** – While the table is a replica, it receives all table snapshots from the source table, including compacted snapshots, so compaction isn't supported on it. After you disassociate the table, you can turn on compaction by using the [PutTableMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableMaintenanceConfiguration.html) operation. For more information, see [Compaction](s3-tables-maintenance.md#s3-tables-maintenance-compaction).

## Before you disassociate a replica table
<a name="s3-tables-replication-disassociate-before"></a>

Before you disassociate a replica table, consider the following:
+ **You can disassociate only replica tables** – You can disassociate only a replica table that S3 Tables replication created in a destination table bucket. The request fails with a `BadRequestException` error if you specify a source table, a table that you created, or a table that you already disassociated.
+ **Check how current the replica is** – To find the last update that was replicated to the replica table, call `GetTableReplicationStatus` on the source table and check the `lastSuccessfulReplicatedUpdate` value for the destination. Later updates to the source table won't be in the table after you disassociate it. If you want the table to include all updates from the source, stop writing to the source table and wait until the replication status for the destination is `COMPLETED`. For more information, see [Monitoring replication status](s3-tables-replication-managing.md#s3-tables-replication-monitoring-status).
+ **Disassociate each table separately** – Each request disassociates one replica table. If the source table replicates to multiple destinations, the other replica tables keep replicating. If you replicate a table bucket by using a bucket-level replication configuration, disassociate each replica table that you want to write to.

### Required permissions
<a name="s3-tables-replication-disassociate-permissions"></a>

To disassociate a replica table, you must have the `s3tables:DisassociateTableReplication` permission on the replica table. To check the replication status before you disassociate, you also need the `s3tables:GetTableReplicationStatus` permission on the source table.

The following example identity-based policy grants permission to check the replication status of the tables in a source table bucket, and to disassociate and view the replica tables in a destination table bucket. To use this policy, replace the `{{user input placeholders}}` with your own information.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowCheckReplicationStatus",
      "Effect": "Allow",
      "Action": "s3tables:GetTableReplicationStatus",
      "Resource": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-source-table-bucket}}/table/*"
    },
    {
      "Sid": "AllowDisassociateReplicaTables",
      "Effect": "Allow",
      "Action": [
        "s3tables:DisassociateTableReplication",
        "s3tables:GetTable"
      ],
      "Resource": "arn:aws:s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-destination-table-bucket}}/table/*"
    }
  ]
}
```

## Using the S3 console
<a name="s3-tables-replication-disassociate-console"></a>

**Warning**  
Disassociation is a one-way operation. After you disassociate a replica table, you manage it as a standalone table. To replicate the table, use it as the source of a new replication configuration.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation pane, choose **Table buckets**.

1. In the **Table buckets** list, choose the name of the destination table bucket that contains the replica table.

1. Choose the **Tables** tab.

1. In the **Tables** list, choose the name of the replica table that you want to disassociate.

1. Choose the **Properties** tab.

1. In the **Replication properties** section, choose **Disassociate**.

1. In the **Disassociate replica table** dialog box, enter **confirm**, and then choose **Disassociate**.

## Using the AWS CLI
<a name="s3-tables-replication-disassociate-cli"></a>

**Warning**  
Disassociation is a one-way operation. After you disassociate a replica table, you manage it as a standalone table. To replicate the table, use it as the source of a new replication configuration.

To use the following AWS CLI example commands, replace the `{{user input placeholders}}` with your own information.

1. (Optional) To find the last update that was replicated to the replica table, run the following AWS CLI command to check the replication status of the source table.

   ```bash
   aws s3tables get-table-replication-status \
       --table-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-source-table-bucket}}/table/{{example-table-id}}
   ```

   In the response, find the destination for the replica table and check its `replicationStatus` and `lastSuccessfulReplicatedUpdate` values.

1. To disassociate the replica table, run the following AWS CLI command. Specify the ARN of the replica table in the destination table bucket.

   ```bash
   aws s3tables disassociate-table-replication \
       --table-arn arn:aws:s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-destination-table-bucket}}/table/{{example-replica-table-id}}
   ```

   If the request succeeds, the command returns no output.

1. (Optional) To confirm that the table is disassociated, run the following AWS CLI command. In the response, the `managedByService` and `managedTableInformation` fields no longer appear.

   ```bash
   aws s3tables get-table \
       --table-bucket-arn arn:aws:s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-destination-table-bucket}} \
       --namespace {{example_namespace}} \
       --name {{example_table}}
   ```

## Next steps
<a name="s3-tables-replication-disassociate-next-steps"></a>

After you disassociate a replica table, you can do the following:
+ Point your applications and query engines at the table in the destination table bucket. Because the table keeps the same namespace and name, you typically need to update only the Region or table bucket that your applications use.
+ Replicate the table by creating a replication configuration that uses it as the source. If the destination table bucket already contains a table with the same namespace and name, such as the original source table, delete or rename that table first. For more information, see [Setting up S3 Tables replication](s3-tables-replication-setting-up.md).