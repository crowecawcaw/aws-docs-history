

# Managing Amazon DocumentDB serverless
<a name="docdb-serverless-managing"></a>

## Viewing and modifying a cluster’s scaling capacity range configuration
<a name="docdb-serverless-range-config"></a>

The `ServerlessV2ScalingConfiguration` argument specifies the scaling capacity range of your DocumentDB serverless instances. It consists of the minimum and maximum DocumentDB capacity unit (DCU) values that apply to all the DocumentDB serverless instances in the cluster.
+ **`MinCapacity`** — The minimum scaling capacity of any DocumentDB serverless instances in the cluster.
+ **`MaxCapacity`** — The maximum scaling capacity of any DocumentDB serverless instances in the cluster.

**Note**  
The following scaling configuration modifications require an instance restart to reflect the new `MinCapacity` and `MaxCapacity` values:  
Any changes to the `MaxCapacity` value
Changing the `MinCapacity` value to 1.0 or lower from a higher value
Changing the `MinCapacity` value to greater than 1.0 from a lower value

For more information on scaling configuration and how to select appropriate scaling capacity limits, see [Amazon DocumentDB serverless scaling configuration](docdb-serverless-scaling-config.md).

------
#### [ Using the AWS Management Console ]

The following AWS Management Console configuration example shows how to view and edit a DocumentDB serverless cluster's scaling configuration settings.

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/docdb/home?region=us-east-1) and open the Amazon DocumentDB console.

1. In the navigation pane, choose **Clusters**.
**Tip**  
If you don't see the navigation pane on the left side of your screen, choose the menu icon (![Menu button.](https://docs.aws.amazon.com/documentdb/latest/devguide/images/docdb-menu-icon.png)) in the upper-left corner of the page.

   The **Clusters** table appears.

1. In the **Clusters** table, select the checkbox of the cluster to which you want to modify the scaling capacity.

1. Choose **Actions**, and then choose **Modify**.

   The **Modify cluster** dialog box appears.

1. Locate the **Serverless capacity setting** section and set the scaling configuration (**Capacity range**) based on the capacity description in the dialog box.

   For more information about scaling and capacity ranges, see [Amazon DocumentDB serverless scaling configuration](docdb-serverless-scaling-config.md).

1. Choose **Continue**.

1. For **Scheduling of modifications**, choose **Apply immediately**.

1. Choose **Modify cluster**.

1. Once the modification has completed, each serverless instance should be rebooted. To minimize writer unavailability, perform the following sequence of operations:

   1. Reboot each serverless reader instance.

      1. Select the reader instance, choose **Actions**, and then **Reboot**.

      1. Wait for the instance status to return to **Available**.

   1. Perform a failover to a rebooted serverless instance.

      1. Select the cluster, choose **Actions**, and then **Failover**.

      1. Wait for the failover operation to complete.

   1. Reboot the remaining serverless instance.

      1. Select the remaining instance, choose **Actions**, and then **Reboot**.

      1. Wait for the instance status to return to **Available**.

------
#### [ Using the AWS CLI ]

The following AWS CLI configuration example shows the current scaling configuration.

In the following example, replace each {{user input placeholder}} with your own information or configuration parameters.

The cluster’s current scaling configuration can be viewed using the `describe-db-clusters` AWS CLI command:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier {{sample-cluster}} \
    --query 'DBClusters[0].ServerlessV2ScalingConfiguration'
```

The following is the output of this command:

```
{
    "MinCapacity": 0.5,
    "MaxCapacity": 16.0
}
```

The cluster’s scaling configuration can be modified using the `modify-db-cluster` command:

```
aws docdb modify-db-cluster \
    --db-cluster-identifier {{sample-cluster}} \
    --serverless-v2-scaling-configuration MinCapacity=0.5,MaxCapacity=32
```

Once complete, each serverless instance should be rebooted. To minimize writer unavailability, we can perform the following sequence of operations:

```
aws docdb reboot-db-instance \
    --db-instance-identifier {{sample-serverless-instance-reader}}

aws docdb wait db-instance-available \
    --db-instance-identifier {{sample-serverless-instance-reader}}

aws docdb failover-db-cluster \
   --db-cluster-identifier sample-cluster \
   --target-db-instance-identifier {{sample-serverless-instance-reader}}

aws docdb reboot-db-instance \
    --db-instance-identifier {{sample-serverless-instance-writer}}

aws docdb wait db-instance-available \
    --db-instance-identifier {{sample-serverless-instance-writer}}

aws docdb failover-db-cluster \
   --db-cluster-identifier sample-cluster \
   --target-db-instance-identifier {{sample-serverless-instance-writer}}
```

------

## Viewing and modifying the promotion tier of serverless readers
<a name="docdb-serverless-promo-tier"></a>

For clusters containing multiple DocumentDB serverless instances or a mixture of provisioned and serverless instances, pay attention to the promotion tier setting for each serverless instance. This setting controls more behavior for serverless instances than for provisioned instances.

For provisioned instances, the choice of tier 0–15 determines only the order in which Amazon DocumentDB chooses which reader instance to promote to the writer during a failover operation. However, for serverless instances, the tier number also determines whether the instance scales up to match the capacity of the writer instance or scales independently based on its own workload. Serverless reader instances in tier 0 or 1 are kept at a minimum capacity at least as high as the writer instance. That way, they are ready to take over from the writer instance in case of a failover. If the writer instance is a provisioned instance, Amazon DocumentDB estimates the equivalent DocumentDB serverless capacity. It uses that estimate as the minimum capacity for the serverless reader instance.

DocumentDB serverless reader instances in tiers 2–15 don't have the same constraint on their minimum capacity. When they are idle, they can scale down to the minimum DocumentDB capacity unit (DCU) value specified in the cluster's capacity range.

------
#### [ Using the AWS Management Console ]

The following AWS Management Console configuration example shows how to view and modify a DocumentDB serverless instance reader's promotional tier settings.

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/docdb/home?region=us-east-1) and open the Amazon DocumentDB console.

   The promotion tiers of each instance is displayed in the **Promotion tier** column in the AWS Management Console.

1. In the navigation pane, choose **Clusters**.
**Tip**  
If you don't see the navigation pane on the left side of your screen, choose the menu icon (![Menu button.](https://docs.aws.amazon.com/documentdb/latest/devguide/images/docdb-menu-icon.png)) in the upper-left corner of the page.

   The **Clusters** table appears.

1. In the **Clusters** table, select the checkbox of the instance to which you want to modify the promotion tier.

1. Choose **Actions**, and then choose **Modify**.

   The **Modify instance** dialog box appears.

1. Locate the **Failover** section and set the **Promotion tier** to the desired level.

1. Choose **Continue**.

1. For **Scheduling of modifications**, choose **Apply immediately**.

1. Choose **Modify instance**.

------
#### [ Using the AWS CLI ]

The following AWS CLI configuration example shows the current scaling configuration.

In the following example, replace each {{user input placeholder}} with your own information or configuration parameters.

The promotion tiers of all instances in a cluster can be viewed using the `describe-db-clusters` AWS CLI command:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier {{sample-cluster}} \
    --query 'DBClusters[0].DBClusterMembers' \
    --output table
```

The following is the output of this command:

```
--------------------------------------------------------------------------------------------------------
|                                          DescribeDBClusters                                          |
+--------------------------------+---------------------------------+------------------+----------------+
|  DBClusterParameterGroupStatus |      DBInstanceIdentifier       | IsClusterWriter  | PromotionTier  |
+--------------------------------+---------------------------------+------------------+----------------+
|  in-sync                       |  sample-serverless-instance-2   |  False           |  1             |
|  in-sync                       |  sample-serverless-instance-1   |  True            |  1             |
+--------------------------------+---------------------------------+------------------+----------------+
```

The promotion tier of a specific instance can be modified using the `modify-db-instance` command:

```
aws docdb modify-db-instance \
    --db-instance-identifier {{sample-serverless-instance-2}} \
    --promotion-tier {{3}}
```

------

## Checking and upgrading the platform version of a serverless cluster
<a name="docdb-serverless-platform-version"></a>

**Important**  
After you upgrade to a newer platform version, you can't downgrade to a previous version.

### Checking the platform version for an existing cluster
<a name="docdb-serverless-platform-version-checking"></a>

------
#### [ Using the AWS Management Console ]

The platform version is displayed on the **Configuration** tab of the cluster details page and the serverless instance details page.

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/docdb/home?region=us-east-1) and open the Amazon DocumentDB console.

1. In the navigation pane, choose **Clusters**.
**Tip**  
If you don't see the navigation pane on the left side of your screen, choose the menu icon (![Menu button.](https://docs.aws.amazon.com/documentdb/latest/devguide/images/docdb-menu-icon.png)) in the upper-left corner of the page.

1. In the list of clusters, choose the name of your serverless cluster.

1. Choose the **Configuration** tab. The **Platform version** field shows the platform version of the cluster.

------
#### [ Using the AWS CLI ]

You can use the `describe-db-clusters` AWS CLI command to check the platform version for an existing cluster.

In the following example, replace each {{user input placeholder}} with your own information or configuration parameters.

```
aws docdb describe-db-clusters \
    --db-cluster-identifier {{sample-cluster}} \
    --query 'DBClusters[0].ServerlessV2PlatformVersion'
```

The following is the output of this command:

```
"4"
```

------

### Checking the default platform version
<a name="docdb-serverless-platform-version-default"></a>

You can use the `describe-serverless-v2-platform-versions` AWS CLI command to check the details of a platform version, or to check the default platform version that you get when you create a new cluster.

```
aws docdb describe-serverless-v2-platform-versions \
    --engine docdb \
    --default-only
```

The following is the output of this command:

```
{
    "ServerlessV2PlatformVersions": [
        {
            "ServerlessV2PlatformVersion": "4",
            "ServerlessV2PlatformVersionDescription": "Version 4 offering scaling up to 256 DCUs, and performance improvement up to 35% compared to version 3",
            "Engine": "docdb",
            "ServerlessV2FeaturesSupport": {
                "MinCapacity": 0.5,
                "MaxCapacity": 256.0
            },
            "Status": "enabled",
            "IsDefault": true
        }
    ]
}
```

### Checking for pending platform version upgrades
<a name="docdb-serverless-platform-version-pending"></a>

You can use the `describe-pending-maintenance-actions` AWS CLI command to check whether there are any pending platform version upgrades for your DocumentDB serverless clusters. A pending platform version upgrade appears as the `serverless-platform-version-update` maintenance action.

To check for pending upgrades on a specific cluster, use the `--resource-identifier` parameter to specify the Amazon Resource Name (ARN) of your cluster:

```
aws docdb describe-pending-maintenance-actions \
    --resource-identifier arn:aws:rds:{{us-east-1}}:{{111122223333}}:cluster:{{sample-cluster}}
```

Output from this operation looks something like the following (JSON format).

```
{
    "PendingMaintenanceActions": [
        {
            "ResourceIdentifier": "arn:aws:rds:us-east-1:111122223333:cluster:sample-cluster",
            "PendingMaintenanceActionDetails": [
                {
                    "Action": "serverless-platform-version-update",
                    "Description": "Upgrade to platform version 4"
                }
            ]
        }
    ]
}
```

### Scheduling a platform version upgrade
<a name="docdb-serverless-platform-version-upgrading"></a>

To schedule when a pending platform version upgrade occurs, use the `apply-pending-maintenance-action` AWS CLI command after you identify the pending upgrade.

To schedule a platform version upgrade, specify the following parameters:
+ `--resource-identifier` — The ARN of your DocumentDB serverless cluster.
+ `--apply-action` — Use `serverless-platform-version-update` to specify a platform version upgrade.
+ `--opt-in-type` — Choose when to apply the upgrade. Use one of the following values:
  + `immediate` — Apply the upgrade immediately.
  + `next-maintenance` — Apply the upgrade during your next scheduled maintenance window.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb apply-pending-maintenance-action \
    --resource-identifier arn:aws:rds:{{us-east-1}}:{{111122223333}}:cluster:{{sample-cluster}} \
    --apply-action serverless-platform-version-update \
    --opt-in-type immediate
```
For Windows:  

```
aws docdb apply-pending-maintenance-action ^
    --resource-identifier arn:aws:rds:{{us-east-1}}:{{111122223333}}:cluster:{{sample-cluster}} ^
    --apply-action serverless-platform-version-update ^
    --opt-in-type immediate
```

For more information about maintenance actions, see [Maintaining Amazon DocumentDB](db-instance-maintain.md).