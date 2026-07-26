# Determining pending maintenance

Maintenance most often involves updates to the following resources in your cluster:

- Operating system (OS) of instances in the cluster
- Engine version of the cluster

For more information about Amazon DocumentDB maintenance, see [Maintaining Amazon DocumentDB](db-instance-maintain.md "db-instance-maintain.md").

Using the AWS Management Console
You can use the AWS Management Console to determine whether a cluster has
pending maintenance.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Menu button.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. Locate the **Maintenance** column to
determine whether a cluster has pending maintenance.

![Console screenshot showing Amazon DocumentDB cluster maintenance field.](images/docdb-cluster-pending-maintenance.png)

**None**
indicates that the cluster is
running the latest engine patch version and its instances have the latest OS updates.
**Available**
indicates that the cluster has pending maintenance, which
might mean that an engine upgrade or OS update is needed. 4. If your cluster has pending maintenance,
you can view the pending maintenance actions by choosing the cluster name
and selecting the **Maintenance & backups** tab.
The **Pending Maintenance** section lists the pending maintenance actions.

![The Amazon DocumentDB Maintenance and backups tab showing the system-update maintenance action for a cluster.](images/cluster-maint-3.png)

Using the AWS CLI
You can use the AWS CLI to determine whether a cluster has the
latest engine version and OS updates by using the `describe-pending-maintenance-actions`
operation with the following parameters.

###### Parameters

- `--resource-identifier`—Optional.
  The ARN for the resource (cluster). If this parameter is omitted,
  pending maintenance actions for all clusters are listed.
- `--region`—Optional. The AWS
  Region that you want to run this operation in, for example,
  `us-east-1`.

###### Example

For Linux, macOS, or Unix:

```
aws docdb describe-pending-maintenance-actions \
   --resource-identifier arn:aws:rds:`aa-example-1`:`111122223333`:cluster:`sample-cluster` \
   --region `aa-example-1`

```

For Windows:

```
aws docdb describe-pending-maintenance-actions ^
   --resource-identifier arn:aws:rds:`aa-example-1`:`111122223333`:cluster:`sample-cluster` ^
   --region `aa-example-1`

```

Output from this operation looks something like the following.

```
{
    "PendingMaintenanceActions": [
        {
            "ResourceIdentifier": "arn:aws:rds:aa-example-1:111122223333:cluster:sample-cluster",
            "PendingMaintenanceActionDetails": [
                {
                    "Description": "New feature",
                    "Action": "system-update",
                    "ForcedApplyDate": "2019-02-25T21:46:00Z",
                    "AutoAppliedAfterDate": "2019-02-25T07:41:00Z",
                    "CurrentApplyDate": "2019-02-25T07:41:00Z"
                }
            ]
        }
    ]
}

```

The following maintenance action types apply to Amazon DocumentDB clusters:

- `system-update` —
  Upgrade the engine patch for the Amazon DocumentDB cluster.

If your cluster has a pending engine patch upgrade available, continue with the steps at
[Performing a patch update to a cluster's engine version](db-cluster-version-upgrade.md "db-cluster-version-upgrade.md").

- `os-upgrade` —
  Update the operating systems of all the DB instances in the Amazon DocumentDB cluster, using rolling upgrades.

For more information, see
[Amazon DocumentDB operating system updates](db-instance-maintain.md#os-system-updates "db-instance-maintain.md#os-system-updates").
