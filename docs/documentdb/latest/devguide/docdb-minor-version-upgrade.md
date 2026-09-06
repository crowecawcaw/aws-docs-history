

# Amazon DocumentDB minor version upgrade
<a name="docdb-minor-version-upgrade"></a>

**Note**  
This topic covers *minor* version upgrades within the same major version (for example, upgrading from 5.0.0 to 5.0.1). For information about upgrading to a different major version, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md).

You can upgrade the minor engine version of your Amazon DocumentDB cluster (for example, from 5.0.0 to 5.0.1) by modifying the cluster. Minor version upgrades can be applied immediately or during the next maintenance window.

## Before performing a minor version upgrade
<a name="docdb-minor-version-upgrade-before"></a>

Before performing a minor version upgrade, the following actions may be helpful:
+ Perform the upgrade during a period of low traffic to reduce the impact of any brief downtime.
+ Verify the target minor version is a valid upgrade target for your current version by using the `describe-db-engine-versions` command.
+ For global clusters, secondary clusters must be upgraded before the primary cluster. For more information, see [Global clusters patching](db-instance-maintain.md#global-clusters-patching).

**Important**  
Upgrades are **one-way operations** — you cannot downgrade after upgrading.
Your cluster will experience brief downtime during the upgrade process.

## Performing a minor version upgrade
<a name="docdb-minor-version-upgrade-perform"></a>

------
#### [ Using the AWS Management Console ]

To perform a minor version upgrade using the AWS Management Console:

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/docdb/home?region=us-east-1) and open the Amazon DocumentDB console.

1. In the **Clusters** table, select the cluster you want to upgrade, choose **Actions**, and then choose **Modify**.

1. On the **Modify cluster** dialog, in the **Cluster specifications** section, choose the target minor version from the **Engine version** drop-down menu.

1. Scroll down and choose **Continue**.

1. In the **Scheduling of modifications** section, choose to apply the change immediately or during the next maintenance window.

   Then choose **Modify cluster**.

------
#### [ Using the AWS CLI ]

Use the [`modify-db-cluster`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster.html) command with the `--engine-version` parameter:

```
aws docdb modify-db-cluster \
    --db-cluster-identifier {{mydocdbcluster}} \
    --engine-version {{5.0.1}} \
    --apply-immediately \
    --region {{us-east-1}}
```

In the example above, replace each {{user input placeholder}} with your cluster's information.

**Note**  
To apply the upgrade during the next maintenance window instead of immediately, use `--no-apply-immediately` in place of `--apply-immediately`.

------

## Verifying the minor version upgrade
<a name="docdb-minor-version-upgrade-verify"></a>

After the upgrade completes, verify the engine version using the AWS CLI:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier {{mydocdbcluster}} \
    --query 'DBClusters[0].EngineVersion'
```

Output from this operation looks something like the following:

```
"5.0.1"
```