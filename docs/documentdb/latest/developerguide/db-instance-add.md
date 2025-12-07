# Adding an Amazon DocumentDB instance to a cluster

Using the AWS Management Console
Use the following procedure to create an instance for your
cluster using the Amazon DocumentDB console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](/images/documentdb/latest/developerguide/images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. To choose the cluster that you want to add an
instance to, select the button to the left of the
cluster's name. 4. Choose **Actions**, and then
choose **Add instances**. 5. In the **Add instance to: <cluster-name>**
page, repeat the following steps for each instance
that you want to add to the cluster. You can have up
to 15.

    1. **Instance identifier**— You can either enter a unique identifier for this instance or allow Amazon DocumentDB to provide the instance identifier based on the cluster identifier.


    Instance naming constraints:




    	* Length is [1—63] letters,
    	 numbers, or hyphens.
    	* First character must be a letter.
    	* Cannot end with a hyphen or contain two consecutive hyphens.
    	* Must be unique for all instances
    	 across Amazon RDS, Neptune, and Amazon DocumentDB
    	 per AWS account, per Region.
    2. **Instance class** — From the drop-down list, choose the instance type you want for this instance.
    3. **Promotion tier** — From the drop-down list, choose the promotion tier for your instance or choose *No preference* to allow Amazon DocumentDB to set the promotion tier for your instance. Lower numbers mean higher priority. For more information, see [Controlling the failover target](failover.md#failover-target_control "failover.md#failover-target_control").
    4. To add more instances, choose
     **Add additional instances** and repeat steps a, b, and c.

6. Finish the operation.
   - To add the instances to your cluster,
     choose **Create**.
   - To cancel the operation, choose
     **Cancel**.

It takes several minutes to create an instance. You can use the console or AWS CLI to view the instance's status. For more information, see [Monitoring an instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").

Using the AWS CLI
Use the `create-db-instance` AWS CLI operation
with the following parameters to create the primary instance
for your cluster.

- `--db-instance-class`
  — Required. The compute and memory capacity of the instance, for example, `db.m4.large`. Not all instance classes are available in all AWS Regions.
- `--db-instance-identifier`
  — Required. A string that
  identifies the instance.

Instance Naming Constraints:

    + Length is [1—63] letters,
     numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain
     two consecutive hyphens.
    + Must be unique for all instances
     across Amazon RDS, Neptune, and Amazon DocumentDB per AWS account, per Region.

- `--engine`
  — Required. Must be `docdb`.
- `--availability-zone`
  — Optional. The Availability Zone that you
  want this instance to be created in. Use this
  parameter to locate your instances in different
  Availability Zones to increase fault tolerance. For
  more information, see [Amazon DocumentDB High availability and replication](replication.md "replication.md").
- `--promotion-tier`
  — Optional. The failover priority tier for
  this instance. Must be between 0 and 15 with lower
  numbers being higher priority. For more information,
  see [Controlling the failover target](failover.md#failover-target_control "failover.md#failover-target_control").

1. **First, determine what
   Availability Zones you can create your instance in.**

If you want to specify the Availability Zone before
you create your instance, run the following command
to determine which Availability Zones are available
for your Amazon DocumentDB cluster.

For Linux, macOS, or Unix:

```
aws docdb describe-db-clusters \
       --query 'DBClusters[*].[DBClusterIdentifier,AvailabilityZones[*]]'
```

For Windows:

```
aws docdb describe-db-clusters ^
       --query 'DBClusters[*].[DBClusterIdentifier,AvailabilityZones[*]]'
```

Output from this operation looks something like the following.

```
[
    [
        "sample-cluster",
        [
            "us-east-1c",
            "us-east-1b",
            "us-east-1a"
        ]
    ]
]

```

2. **Second, determine what
   instance classes you can create in your Region.**

To determine which instance classes are available
to you in your Region, run the following command.
From the output, choose an instance class for the
instance you want to add to your Amazon DocumentDB cluster.

For Linux, macOS, or Unix:

```
aws docdb describe-orderable-db-instance-options \
        --engine docdb \
        --query 'OrderableDBInstanceOptions[*].DBInstanceClass'
```

For Windows:

```
aws docdb describe-orderable-db-instance-options ^
        --engine docdb ^
        --query 'OrderableDBInstanceOptions[*].DBInstanceClass'
```

Output from this operation looks something like the
following.

```
[
    "db.r5.16xlarge",
    "db.r5.2xlarge",
    "db.r5.4xlarge",
    "db.r5.8xlarge",
    "db.r5.large",
    "db.r5.xlarge"
]
```

3. **Finally, add an instance to
   your Amazon DocumentDB cluster.**

To add an instance to your Amazon DocumentDB cluster, run
the following command..

For Linux, macOS, or Unix:

```
aws docdb create-db-instance \
       --db-cluster-identifier sample-cluster \
       --db-instance-identifier sample-instance-2 \
       --availability-zone us-east-1b \
       --promotion-tier 2 \
       --db-instance-class db.r5.xlarge \
       --engine docdb
```

For Windows:

```
aws docdb create-db-instance ^
       --db-cluster-identifier sample-cluster ^
       --db-instance-identifier sample-instance-2 ^
       --availability-zone us-east-1b ^
       --promotion-tier 2 ^
       --db-instance-class db.r5.xlarge ^
       --engine docdb
```

Output from this operation looks something like the
following.

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "sample-instance-2",
        "DBInstanceClass": "db.r5.xlarge",
        "Engine": "docdb",
        "DBInstanceStatus": "creating",
        "PreferredBackupWindow": "02:00-02:30",
        "BackupRetentionPeriod": 1,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abcd0123",
                "Status": "active"
            }
        ],
        "AvailabilityZone": "us-east-1b",
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-6242c31a",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-abcd0123",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-wxyz0123",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2b"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "sun:11:35-sun:12:05",
        "PendingModifiedValues": {},
        "EngineVersion": "3.6.0",
        "AutoMinorVersionUpgrade": true,
        "PubliclyAccessible": false,
        "DBClusterIdentifier": "sample-cluster",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/sample-key",
        "DbiResourceId": "db-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "CACertificateIdentifier": "rds-ca-2019",
        "PromotionTier": 2,
        "DBInstanceArn": "arn:aws:rds:us-east-1:<accountID>:db:sample-instance-2"
    }
}

```

It takes several minutes to create the instance. You can
use the console or AWS CLI to view the instance's status. For
more information, see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").
