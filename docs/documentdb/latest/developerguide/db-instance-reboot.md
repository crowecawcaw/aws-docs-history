# Rebooting an Amazon DocumentDB instance

Occasionally, you might need to reboot your Amazon DocumentDB instance,
usually for maintenance reasons. If you make certain changes,
such as changing the cluster parameter group that is associated
with a cluster, you must reboot the instances in the cluster for
the changes to take effect. You can reboot a specified instance
using the AWS Management Console or the AWS CLI.

Rebooting an instance restarts the database engine service.
Rebooting results in a momentary outage, during which the
instance status is set to `rebooting`. An Amazon DocumentDB
event is created when the reboot is completed.

Rebooting an instance doesn't result in a failover. To failover
an Amazon DocumentDB cluster, use the AWS Management Console or the AWS CLI operation
`failover-db-cluster`. For more information, see [Amazon DocumentDB Failover](failover.md "failover.md").

You can't reboot your instance if it isn't in the
_available_ state. Your database can be
unavailable for several reasons, such as a previously requested
modification, or a maintenance-window action. For more
information on instance states, see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").

Using the AWS Management Console
The following procedure reboots an instance that you
specify using the console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters** .

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the Clusters navigation box, you’ll see the column **Cluster Identifier**. Your instances are listed under clusters, similar to the screenshot below.

![Clusters table showing list of clusters under Cluster identifier column, with instances nested inside clusters.](images/choose-clusters.png) 4. Check the box to the left of the instance you wish to reboot. 5. Choose **Actions**, choose
**Reboot**, and then choose
**Reboot** to confirm your reboot.

It takes a few minutes for your instance to reboot. You can use the instance only when its status is _available_. You can monitor the instance's status using the console or the AWS CLI. For more information,
see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").

Using the AWS CLI
To reboot an Amazon DocumentDB instance, use the
`reboot-db-instance` operation with the
`--db-instance-identifier` parameter. This
parameter specifies the identifier for the instance to be
rebooted.

The following code reboots the instance `sample-instance`.

For Linux, macOS, or Unix:

```
aws docdb reboot-db-instance \
       --db-instance-identifier sample-instance
```

For Windows:

```
aws docdb reboot-db-instance ^
       --db-instance-identifier sample-instance
```

Output from this operation looks something like the
following.

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "sample-instance",
        "DBInstanceClass": "db.r5.large",
        "Engine": "docdb",
        "DBInstanceStatus": "rebooting",
        "Endpoint": {
            "Address": "sample-instance.node.us-east-1.docdb.amazonaws.com",
            "Port": 27017,
            "HostedZoneId": "ABCDEFGHIJKLM"
        },
        "InstanceCreateTime": "2020-03-27T08:05:56.314Z",
        "PreferredBackupWindow": "02:00-02:30",
        "BackupRetentionPeriod": 1,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abcd0123",
                "Status": "active"
            }
        ],
        "AvailabilityZone": "us-east-1c",
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-abcd0123",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-abcd0123",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-wxyz0123",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1b"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "sun:06:53-sun:07:23",
        "PendingModifiedValues": {},
        "EngineVersion": "3.6.0",
        "AutoMinorVersionUpgrade": true,
        "PubliclyAccessible": false,
        "DBClusterIdentifier": "sample-cluster",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/sample-key",
        "DbiResourceId": "db-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "CACertificateIdentifier": "rds-ca-2019",
        "PromotionTier": 1,
        "DBInstanceArn": "arn:aws:rds:us-east-1:<accountID>:db:sample-instance",
        "EnabledCloudwatchLogsExports": [
            "profiler"
        ]
    }
}

```

It takes a few minutes for your instance to reboot. You can use the instance only when its status is _available_. You can monitor the instance's
status using the console or AWS CLI. For more information, see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").
