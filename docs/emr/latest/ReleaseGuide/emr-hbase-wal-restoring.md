# Restoring from Amazon EMR WAL

Because the Amazon EMR WAL for your original cluster is retained for 30 days, you can
restore and reuse the WAL for a newly-created cluster within that 30-day period. When
you launch a new cluster from the same S3 root directory, Amazon EMR keeps the WAL instances from your
old cluster. If you terminate this new cluster, the 30-day clock restarts from the time
of when you terminate.

Use the following procedure to restore an existing WAL with a new cluster. This
process assumes that you created your original cluster with Amazon EMR WAL enabled.

1. Within 30 days of creating a WAL-enabled cluster, create a new cluster in the
   same AWS Region as the original cluster. The new cluster can be in the same AZ
   or in a different AZ within the same Region that the original cluster was
   created.

Configure the object properties to specify the storage mode and the root
directory location in Amazon S3. The Amazon S3 location that you specify should be in the
same Region as your EMR cluster, but only one active cluster can use the same
HBase root directory in S3 at a time.

For console steps to create a cluster, and a detailed
`create-cluster` example that uses the AWS CLI, see [Creating a cluster with HBase](emr-hbase-create.md "emr-hbase-create.md"). 2. To use the existing Amazon EMR WAL for the new cluster, set the
`hbase.emr.wal.enabled` property to `true`. The
following JSON snippet shows an example configuration object.

```
[
    {
        "Classification": "hbase-site",
        "Properties": {
            "hbase.rootdir": "s3://`amzn-s3-demo-bucket`/`MyHBaseStore`"
        }
    },
    {
        "Classification": "hbase",
        "Properties": {
            "hbase.emr.storageMode": "s3",
            "hbase.emr.wal.enabled": "true"
        }
    }
]
```
