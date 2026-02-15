# Modifying an Amazon DocumentDB instance

You can modify your Amazon DocumentDB instance using either the AWS Management Console or the AWS CLI. To modify an instance, the instance must be in the _available_ state. You cannot modify an
instance that is stopped. If the cluster is stopped, first start
the cluster, wait for the instance to become _available_, and then make the desired modifications. For more information, see [Stopping and starting an
Amazon DocumentDB cluster](db-cluster-stop-start.md "db-cluster-stop-start.md").

Using the AWS Management Console
To modify a specific Amazon DocumentDB instance using the console,
complete the following steps.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters** .

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the Clusters navigation box, you’ll see the column **Cluster Identifier**. Your instances are listed under clusters, similar to the screenshot below.

![Clusters table showing list of clusters under Cluster identifier column, with instances nested inside clusters.](images/choose-clusters.png) 4. Check the box to the left of the instance you wish to modify. 5. Choose **Actions**, and then
choose **Modify**. 6. In the **Modify instance:
<instance-name>** pane, make the
changes that you want. You can make the following
changes:

    * **Instance
     specifications** — The
     instance identifier and class. Instance
     identifier naming constraints:




    	+ **Instance identifier** — Enter a name that is unique for all instances owned by your AWS account in the current region. The instance identifier must contain [1—63]
    	 alphanumeric characters or hyphens, have a letter as the first character, and cannot end with a hyphen or contain two consecutive hyphens.
    	+ **Instance class** — From the drop-down menu, select an instance class for your Amazon DocumentDB instance. For more information, see [Managing instance classes](db-instance-classes.md "db-instance-classes.md").
    * **Certificate
     authority** — Server
     certificate for this instance. For more
     information, see [Updating your Amazon DocumentDB TLS
     certificates](ca_cert_rotation.md "ca_cert_rotation.md").
    * **Failover**
     — During failover, the instance with
     the highest promotion tier will be promoted
     to primary. For more information, see [Amazon DocumentDB Failover](failover.md "failover.md").
    * **Maintenance**
     — The maintenance window in which
     pending modifications or patches are applied
     to instances in the cluster.

7. When you have finished, choose
   **Continue** to see a summary of
   your changes.
8. After verifying your changes, you can apply them
   immediately or during the next maintenance window
   under **Scheduling of modifications**.
   Choose **Modify instance** to save
   your changes. Alternatively, you can choose
   **Cancel** to discard your changes.

It takes a few minutes for your changes to be applied.
You can use the instance only when its status is
_available_. You can monitor the
instance's status using the console or AWS CLI. For more
information, see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").

Using the AWS CLI
To modify a specific Amazon DocumentDB instance using the AWS CLI, use
the `modify-db-instance` with the following
parameters. For more information, see [ModifyDBInstance](API_ModifyDBInstance.md "API_ModifyDBInstance.md").
The following code modifies the instance class to
`db.r5.large` for the instance
`sample-instance`.

###### Parameters

- `--db-instance-identifier`
  — Required. The identifier for the instance
  to be modified.
- `--db-instance-class` — Optional. The new compute and memory capacity of the instance; for example, `db.r5.large`. Not all instance classes are available in all AWS Regions. If you modify the instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless `ApplyImmediately` is specified as true for this request.
- `--apply-immediately`
  or `--no-apply-immediately`
  — Optional. Specifies whether this modification should be applied immediately or wait until the next maintenance window. If this parameter is omitted, the modification is performed during the next maintenance window.

###### Example

For Linux, macOS, or Unix:

```
aws docdb modify-db-instance \
       --db-instance-identifier sample-instance \
       --db-instance-class db.r5.large \
       --apply-immediately
```

For Windows:

```
aws docdb modify-db-instance ^
       --db-instance-identifier sample-instance ^
       --db-instance-class db.r5.large ^
       --apply-immediately
```

Output from this operation looks something like the
following.

```
{
    "DBInstances": [
        {
            "DBInstanceIdentifier": "sample-instance-1",
            "DBInstanceClass": "db.r5.large",
            "Engine": "docdb",
            "DBInstanceStatus": "modifying",
            "Endpoint": {
                "Address": "sample-instance-1.node.us-east-1.docdb.amazonaws.com",
                "Port": 27017,
                "HostedZoneId": "ABCDEFGHIJKLM"
            },
            "InstanceCreateTime": "2020-01-10T22:18:55.921Z",
            "PreferredBackupWindow": "02:00-02:30",
            "BackupRetentionPeriod": 1,
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-abcd0123",
                    "Status": "active"
                }
            ],
            "AvailabilityZone": "us-east-1a",
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
                        "SubnetIdentifier": "subnet-abcd0123",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1b"
                        },
                        "SubnetStatus": "Active"
                    }
                ]
            },
            "PreferredMaintenanceWindow": "sun:10:57-sun:11:27",
            `"PendingModifiedValues": {
 "DBInstanceClass": "db.r5.large"`
            },
            "EngineVersion": "3.6.0",
            "AutoMinorVersionUpgrade": true,
            "PubliclyAccessible": false,
            "DBClusterIdentifier": "sample-cluster",
            "StorageEncrypted": true,
            "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "DbiResourceId": "db-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "CACertificateIdentifier": "rds-ca-2019",
            "PromotionTier": 1,
            "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:sample-instance-1",
            "EnabledCloudwatchLogsExports": [
                "profiler"
            ]
        }
    ]
}
```

It takes a few minutes for your modifications to be applied.
You can use the instance only when its status is
_available_. You can monitor the instance's
status using the AWS Management Console or AWS CLI. For more information,
see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").
