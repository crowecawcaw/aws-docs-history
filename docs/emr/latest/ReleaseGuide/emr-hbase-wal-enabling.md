# Enabling Amazon EMR WAL

Use the following steps to enable writing to the Amazon EMR WAL when you create a cluster
with the AWS Command Line Interface.

###### Note

You can't enable Amazon EMR WAL for a cluster that is already running, and you can't
launch two clusters with the same S3 root directory. For more information, see [Considerations and Regions for Amazon EMR
WAL](emr-hbase-wal-considerations.md "emr-hbase-wal-considerations.md").

1. Before you can create an Amazon EMR WAL enabled cluster, you must add the required
   permissions to the instance profile that you plan to use with your cluster. For
   more information, see [Required permissions for Amazon EMR WAL](emr-hbase-wal-permissions.md "emr-hbase-wal-permissions.md").
2. Create a cluster from the AWS CLI. Use the `--configurations` option
   to provide a JSON configuration object that specifies the
   `hbase.emr.wal.enabled` property, as shown in the example
   below.
   - Specify the storage mode and the root directory location in Amazon S3. The
     Amazon S3 location that you specify should be in the same Region as your
     EMR cluster, but only one active cluster can use the same HBase root
     directory in S3 at a time.
   - Create your cluster with the instance groups configuration. You can't
     use Amazon EMR WAL with the instance fleets configuration. For more
     information on creating clusters with instance groups, see [Configure uniform instance groups](../ManagementGuide/emr-uniform-instance-group.md "../ManagementGuide/emr-uniform-instance-group.md") in the _Amazon EMR
     Management Guide_.
   - For console steps to create a cluster, and a detailed
     `create-cluster` example that uses the AWS CLI, see [Creating a
     cluster with HBase](emr-hbase-create.md "emr-hbase-create.md").

3. To enable WAL for the new cluster, set the `hbase.emr.wal.enabled`
   property to `true`. The following command contains a JSON snippet
   with an example configuration object.

```
aws emr create-cluster --name "`hbasewal`" --release-label `emr-6.x.y` \
--applications Name=HBase --use-default-roles --ec2-attributes KeyName=`myKey` \
--instance-type `m6i.xlarge` --instance-count `1` --configurations hbase.json
$cat hbase.json
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

When HBase is online on the newly created cluster, HBase will automatically write WAL
data to the Amazon EMR WAL and use the Amazon EMR WAL for recovery purposes.

###### Example 1: Creating an EMR cluster that uses Amazon EMR WAL

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

###### Example 2: Creating an EMR cluster with a custom WAL workspace

```
[
    {
        "Classification": "hbase-site",
        "Properties": {
            "hbase.rootdir": "s3://`amzn-s3-demo-bucket`/`MyHBaseStore`",
            "emr.wal.workspace": "`customWorkspaceName`"
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
