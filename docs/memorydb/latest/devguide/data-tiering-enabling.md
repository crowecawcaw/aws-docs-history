

# Using data tiering
<a name="data-tiering-enabling"></a>

## Using data tiering using the AWS Management Console
<a name="data-tiering-enabling-console"></a>

When creating a cluster, you use data tiering by selecting a node type from the r6gd family, such as *db.r6gd.xlarge*. Selecting that node type automatically enables data tiering. 

For more information on creating a cluster, see [Step 2: Create a cluster](getting-started.md#getting-started.createcluster).

## Enabling data tiering using the AWS CLI
<a name="data-tiering-enabling-cli"></a>

When creating a cluster using the AWS CLI, you use data tiering by selecting a node type from the r6gd family, such as *db.r6gd.xlarge* and setting the `--data-tiering` parameter. 

You cannot opt out of data tiering when selecting a node type from the r6gd family. If you set the `--no-data-tiering` parameter, the operation will fail.

For Linux, macOS, or Unix:

```
aws memorydb create-cluster \
   --cluster-name my-cluster \
   --node-type db.r6gd.xlarge \
   --engine valkey  \
   --acl-name my-acl \
   --subnet-group my-sg \
   --data-tiering
```

For Windows:

```
aws memorydb create-cluster ^
   --cluster-name my-cluster ^
   --node-type db.r6gd.xlarge ^
   --engine valkey ^
   --acl-name my-acl ^
   --subnet-group my-sg
   --data-tiering
```

After running this operation, you will see a response similar to the following:

```
{
    "Cluster": {
        "Name": "my-cluster",
        "Status": "creating",
        "NumberOfShards": 1,
        "AvailabilityMode": "MultiAZ",
        "ClusterEndpoint": {
            "Port": 6379
        },
        "NodeType": "db.r6gd.xlarge",
        "EngineVersion": "7.2",
        "EnginePatchVersion": "7.2.6",
        "Engine": "valkey"
        "ParameterGroupName": "default.memorydb-valkey7",
        "ParameterGroupStatus": "in-sync",
        "SubnetGroupName": "my-sg",
        "TLSEnabled": true,
        "ARN": "arn:aws:memorydb:us-east-1:xxxxxxxxxxxxxx:cluster/my-cluster",
        "SnapshotRetentionLimit": 0,
        "MaintenanceWindow": "wed:03:00-wed:04:00",
        "SnapshotWindow": "04:30-05:30",        
        "ACLName": "my-acl",
        "DataTiering":"true",
        "AutoMinorVersionUpgrade": true
    }
}
```