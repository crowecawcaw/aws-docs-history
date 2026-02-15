# Tutorial: Restoring a DB cluster from a DB cluster snapshot using the AWS CLI

In this tutorial, you restore a DB cluster from a DB cluster snapshot using the AWS CLI. Restoring a DB cluster from a snapshot using the AWS CLI has two steps:

1. [Restoring the DB cluster](#tut-restore-cluster.CLI.restore "#tut-restore-cluster.CLI.restore") using the [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md") command
2. [Creating the primary (writer) DB instance](#tut-restore-cluster.CLI.create "#tut-restore-cluster.CLI.create") using the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command

## Restoring the DB cluster

You use the `restore-db-cluster-from-snapshot` command. The following options are required:

- `--db-cluster-identifier` – The name of the restored DB cluster.
- `--snapshot-identifier` – The name of the DB snapshot to restore from.
- `--engine` – The database engine of the restored DB cluster. It must be compatible with the
  database engine of the source DB cluster.

The choices are the following:

    + `aurora-mysql` – Aurora MySQL 5.7 and 8.0 compatible.
    + `aurora-postgresql` – Aurora PostgreSQL compatible.

In this example, we use `aurora-mysql`.

- `--engine-version` – The version of the restored DB cluster. In this example, we use a MySQL-8.0
  compatible version.

The following example restores an Aurora MySQL 8.0–compatible DB cluster named `my-new-80-cluster` from a
DB cluster snapshot named `my-57-cluster-snapshot`.

###### To restore the DB cluster

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `my-new-80-cluster` \
    --snapshot-identifier `my-57-cluster-snapshot` \
    --engine aurora-mysql \
    --engine-version `8.0.mysql_aurora.3.02.0`
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-cluster-identifier `my-new-80-cluster` ^
    --snapshot-identifier `my-57-cluster-snapshot` ^
    --engine aurora-mysql ^
    --engine-version `8.0.mysql_aurora.3.02.0`
```

The output resembles the following.

```
{
    "DBCluster": {
        "AllocatedStorage": 1,
        "AvailabilityZones": [
            "eu-central-1b",
            "eu-central-1c",
            "eu-central-1a"
        ],
        "BackupRetentionPeriod": 14,
        "DatabaseName": "",
        "DBClusterIdentifier": "my-new-80-cluster",
        "DBClusterParameterGroup": "default.aurora-mysql8.0",
        "DBSubnetGroup": "default",
        "Status": "creating",
        "Endpoint": "my-new-80-cluster.cluster-############.eu-central-1.rds.amazonaws.com",
        "ReaderEndpoint": "my-new-80-cluster.cluster-ro-############.eu-central-1.rds.amazonaws.com",
        "MultiAZ": false,
        "Engine": "aurora-mysql",
        "EngineVersion": "8.0.mysql_aurora.3.02.0",
        "Port": 3306,
        "MasterUsername": "admin",
        "PreferredBackupWindow": "01:55-02:25",
        "PreferredMaintenanceWindow": "thu:21:14-thu:21:44",
        "ReadReplicaIdentifiers": [],
        "DBClusterMembers": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-########",
                "Status": "active"
            }
        ],
        "HostedZoneId": "Z1RLNU0EXAMPLE",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:eu-central-1:123456789012:key/#######-5ccc-49cc-8aaa-############",
        "DbClusterResourceId": "cluster-ZZ12345678ITSJUSTANEXAMPLE",
        "DBClusterArn": "arn:aws:rds:eu-central-1:123456789012:cluster:my-new-80-cluster",
        "AssociatedRoles": [],
        "IAMDatabaseAuthenticationEnabled": false,
        "ClusterCreateTime": "2022-07-05T20:45:42.171000+00:00",
        "EngineMode": "provisioned",
        "DeletionProtection": false,
        "HttpEndpointEnabled": false,
        "CopyTagsToSnapshot": false,
        "CrossAccountClone": false,
        "DomainMemberships": [],
        "TagList": []
    }
}
```

## Creating the primary (writer) DB instance

To create the primary (writer) DB instance, you use the
`create-db-instance` command. The following options are
required:

- `--db-cluster-identifier` – The name of the restored DB cluster.
- `--db-instance-identifier` – The name of the primary DB instance.
- `--db-instance-class` – The instance class of the
  primary DB instance. In this example, we use
  `db.t3.medium`.

###### Note

We recommend using the T DB instance classes only for development and test servers, or other non-production
servers. For more details on the T instance classes, see [DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

- `--engine` – The database engine of the primary DB instance. It must be the same database engine
  as the restored DB cluster uses.

The choices are the following:

    + `aurora-mysql` – Aurora MySQL 5.7 and 8.0 compatible.
    + `aurora-postgresql` – Aurora PostgreSQL compatible.

In this example, we use `aurora-mysql`.

The following example creates a primary (writer) DB instance named `my-new-80-cluster-instance` in the restored
Aurora MySQL 8.0–compatible DB cluster named `my-new-80-cluster`.

###### To create the primary DB instance

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-cluster-identifier my-new-80-cluster \
    --db-instance-identifier `my-new-80-cluster-instance` \
    --db-instance-class `db.t3.medium` \
    --engine aurora-mysql
```

For Windows:

```
aws rds create-db-instance ^
    --db-cluster-identifier my-new-80-cluster ^
    --db-instance-identifier `my-new-80-cluster-instance` ^
    --db-instance-class `db.t3.medium` ^
    --engine aurora-mysql
```

The output resembles the following.

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "my-new-80-cluster-instance",
        "DBInstanceClass": "db.t3.medium",
        "Engine": "aurora-mysql",
        "DBInstanceStatus": "creating",
        "MasterUsername": "admin",
        "AllocatedStorage": 1,
        "PreferredBackupWindow": "01:55-02:25",
        "BackupRetentionPeriod": 14,
        "DBSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-########",
                "Status": "active"
            }
        ],
        "DBParameterGroups": [
            {
                "DBParameterGroupName": "default.aurora-mysql8.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-2305ca49",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "eu-central-1a"
                    },
                    "SubnetOutpost": {},
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "eu-central-1b"
                    },
                    "SubnetOutpost": {},
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "eu-central-1c"
                    },
                    "SubnetOutpost": {},
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "sat:02:41-sat:03:11",
        "PendingModifiedValues": {},
        "MultiAZ": false,
        "EngineVersion": "8.0.mysql_aurora.3.02.0",
        "AutoMinorVersionUpgrade": true,
        "ReadReplicaDBInstanceIdentifiers": [],
        "LicenseModel": "general-public-license",
        "OptionGroupMemberships": [
            {
                "OptionGroupName": "default:aurora-mysql-8-0",
                "Status": "in-sync"
            }
        ],
        "PubliclyAccessible": false,
        "StorageType": "aurora",
        "DbInstancePort": 0,
        "DBClusterIdentifier": "my-new-80-cluster",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:eu-central-1:534026745191:key/#######-5ccc-49cc-8aaa-############",
        "DbiResourceId": "db-5C6UT5PU0YETANOTHEREXAMPLE",
        "CACertificateIdentifier": "rds-ca-2019",
        "DomainMemberships": [],
        "CopyTagsToSnapshot": false,
        "MonitoringInterval": 0,
        "PromotionTier": 1,
        "DBInstanceArn": "arn:aws:rds:eu-central-1:123456789012:db:my-new-80-cluster-instance",
        "IAMDatabaseAuthenticationEnabled": false,
        "PerformanceInsightsEnabled": false,
        "DeletionProtection": false,
        "AssociatedRoles": [],
        "TagList": []
    }
}
```
