# Managing S3 Tables replication

After you configure S3 Tables replication, you can monitor replica status to verify what's
replicated. You can check replication status in the Amazon S3 console on the source table's
**Management** tab, or by using the AWS CLI. For more information, see [Setting up S3 Tables replication](s3-tables-replication-setting-up.md "s3-tables-replication-setting-up.md").This topic explains how to monitor replication and understand the different status values
that indicate whether replication is completed, in progress, or has failed.

## Monitoring replication

status

Replication jobs run continuously for your replicated tables. You can query the status of
replication with the GetTableReplicationStatus API or view it in the Amazon S3 console.

### To get the status of replication by using

the AWS CLI

The following example gets the replication status using the GetTableReplicationStatus
API.

```

aws s3tables get-table-replication-status \
    --table-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/`sales-data`

```

Expected output:

```

{
  "sourceTableARN": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/`sales-data`",
  "destinations": [
    {
      "replicationStatus": "COMPLETED",
      "destinationBucketARN": "arn:aws:s3tables:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`",
      "destinationTableARN": "arn:aws:s3tables:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/`sales-data`",
      "lastSuccessfulReplicatedUpdate": {
        "metadataLocation": "`latest_table_metadata.json`",
        "timestamp": "`2025-11-15T14:30:00Z`"
      }
    },
    {
      "replicationStatus": "PENDING",
      "destinationBucketARN": "arn:aws:s3tables:`eu-west-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket-eu-bucket`",
      "destinationTableARN": "arn:aws:s3tables:`eu-west-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket-eu-bucket`/table/`sales-data`",
      "lastSuccessfulReplicatedUpdate": {
        "metadataLocation": "`latest_table_metadata.json`",
        "timestamp": "`2025-11-15T14:25:00Z`"
      }
    }
  ]
}

```

For more information, see [get-table-replication-status](../../../cli/latest/reference/s3tables/get-table-replication-status.md "../../../cli/latest/reference/s3tables/get-table-replication-status.md") in the _AWS CLI Command
Reference_.

### Understanding the

response

The response contains the following elements:

- sourceTableARN – The ARN of the source table
  being replicated.
- destinations – An array of destination status
  objects, one for each configured replication destination. Each destination object
  contains:
  - replicationStatus – The current
    replication status for this destination (COMPLETED, PENDING, or FAILED).
  - destinationBucketARN – The ARN of the
    destination table bucket.
  - destinationTableARN – The ARN of the
    replica table in the destination bucket.
  - lastSuccessfulReplicatedUpdate –
    Information about the most recent successful replication:
    - metadataLocation – The Iceberg
      metadata file name that was last successfully replicated. Compare this with the
      source table's current metadata location to determine if replication is up to
      date.
    - timestamp – The time when this
      metadata file was replicated to the destination.

  - failureMessage (only present when status is
    FAILED) – A detailed error message describing why replication failed.

### Replication status values

Replication can have three possible statuses for each destination:

- COMPLETED – All source table snapshots have
  been successfully replicated to the destination. The source table's latest metadata
  location matches the last replicated metadata location.
- PENDING – Replication is in progress or new
  commits are waiting to be replicated. The source table's latest metadata location
  differs from the last replicated metadata location.
- FAILED – The last replication job for this
  table failed. No new updates are being replicated.
