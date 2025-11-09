# Managing Amazon DocumentDB serverless

## Viewing and modifying a cluster’s scaling capacity range configuration

The `ServerlessV2ScalingConfiguration` argument specifies the scaling capacity range of your DocumentDB serverless instances.
It consists of the minimum and maximum DocumentDB capacity unit (DCU) values that apply to all the DocumentDB serverless instances in the cluster.

- **`MinCapacity`** — The minimum scaling capacity of any DocumentDB serverless instances in the cluster.
- **`MaxCapacity`** — The maximum scaling capacity of any DocumentDB serverless instances in the cluster.

###### Note

The following scaling configuration modifications require an instance restart to reflect the new `MinCapacity` and `MaxCapacity` values:

- Any changes to the `MaxCapacity` value
- Changing the `MinCapacity` value to 1.0 or lower from a higher value
- Changing the `MinCapacity` value to greater than 1.0 from a lower value

For more information on scaling configuration and how to select appropriate scaling capacity limits, see [Amazon DocumentDB serverless scaling configuration](docdb-serverless-scaling-config.md "docdb-serverless-scaling-config.md").

Using the AWS Management Console
The following AWS Management Console configuration example shows how to view and edit a DocumentDB serverless cluster's scaling configuration settings.

1. Sign into the [AWS Management Console](../../../https:/console.aws.amazon.com/docdb/home.md "../../../https:/console.aws.amazon.com/docdb/home.md") and open the Amazon DocumentDB console.
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page.

The **Clusters** table appears. 3. In the **Clusters** table, select the checkbox of the cluster to which you want to modify the scaling capacity. 4. Choose **Actions**, and then choose **Modify**.

The **Modify cluster** dialog box appears. 5. Locate the **Serverless capacity setting** section and set the scaling configuration (**Capacity range**) based on the capacity description in the dialog box.

For more information about scaling and capacity ranges, see [Amazon DocumentDB serverless scaling configuration](docdb-serverless-scaling-config.md "docdb-serverless-scaling-config.md"). 6. Choose **Continue**. 7. For **Scheduling of modifications**, choose **Apply immediately**. 8. Choose **Modify cluster**. 9. Once the modification has completed, each serverless instance should be rebooted.
To minimize writer unavailability, perform the following sequence of operations:

    1. Reboot each serverless reader instance.


    	1. Select the reader instance, choose **Actions**, and then **Reboot**.
    	2. Wait for the instance status to return to **Available**.
    2. Perform a failover to a rebooted serverless instance.


    	1. Select the cluster, choose **Actions**, and then **Failover**.
    	2. Wait for the failover operation to complete.
    3. Reboot the remaining serverless instance.


    	1. Select the remaining instance, choose **Actions**, and then **Reboot**.
    	2. Wait for the instance status to return to **Available**.

Using the AWS CLI
The following AWS CLI configuration example shows the current scaling configuration.

In the following example, replace each `user input placeholder` with your own information or configuration parameters.

The cluster’s current scaling configuration can be viewed using the `describe-db-clusters` AWS CLI command:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier `sample-cluster` \
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
    --db-cluster-identifier `sample-cluster` \
    --serverless-v2-scaling-configuration MinCapacity=0.5,MaxCapacity=32
```

Once complete, each serverless instance should be rebooted.
To minimize writer unavailability, we can perform the following sequence of operations:

```
aws docdb reboot-db-instance \
    --db-instance-identifier `sample-serverless-instance-reader`

aws docdb wait db-instance-available \
    --db-instance-identifier `sample-serverless-instance-reader`

aws docdb failover-db-cluster \
   --db-cluster-identifier sample-cluster \
   --target-db-instance-identifier `sample-serverless-instance-reader`

aws docdb reboot-db-instance \
    --db-instance-identifier `sample-serverless-instance-writer`

aws docdb wait db-instance-available \
    --db-instance-identifier `sample-serverless-instance-writer`

aws docdb failover-db-cluster \
   --db-cluster-identifier sample-cluster \
   --target-db-instance-identifier `sample-serverless-instance-writer`
```

## Viewing and modifying the promotion tier of serverless readers

For clusters containing multiple DocumentDB serverless instances or a mixture of provisioned and serverless instances, pay attention to the promotion tier setting for each serverless instance.
This setting controls more behavior for serverless instances than for provisioned instances.

For provisioned instances, the choice of tier 0–15 determines only the order in which Amazon DocumentDB chooses which reader instance to promote to the writer during a failover operation.
However, for serverless instances, the tier number also determines whether the instance scales up to match the capacity of the writer instance or scales independently based on its own workload.
Serverless reader instances in tier 0 or 1 are kept at a minimum capacity at least as high as the writer instance.
That way, they are ready to take over from the writer instance in case of a failover.
If the writer instance is a provisioned instance, Amazon DocumentDB estimates the equivalent DocumentDB serverless capacity.
It uses that estimate as the minimum capacity for the serverless reader instance.

DocumentDB serverless reader instances in tiers 2–15 don't have the same constraint on their minimum capacity.
When they are idle, they can scale down to the minimum DocumentDB capacity unit (DCU) value specified in the cluster's capacity range.

Using the AWS Management Console
The following AWS Management Console configuration example shows how to view and modify a DocumentDB serverless instance reader's promotional tier settings.

1. Sign into the [AWS Management Console](../../../https:/console.aws.amazon.com/docdb/home.md "../../../https:/console.aws.amazon.com/docdb/home.md") and open the Amazon DocumentDB console.

The promotion tiers of each instance is displayed in the **Promotion tier** column in the AWS Management Console. 2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page.

The **Clusters** table appears. 3. In the **Clusters** table, select the checkbox of the instance to which you want to modify the promotion tier. 4. Choose **Actions**, and then choose **Modify**.

The **Modify instance** dialog box appears. 5. Locate the **Failover** section and set the **Promotion tier** to the desired level. 6. Choose **Continue**. 7. For **Scheduling of modifications**, choose **Apply immediately**. 8. Choose **Modify instance**.

Using the AWS CLI
The following AWS CLI configuration example shows the current scaling configuration.

In the following example, replace each `user input placeholder` with your own information or configuration parameters.

The promotion tiers of all instances in a cluster can be viewed using the `describe-db-clusters` AWS CLI command:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier `sample-cluster` \
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
    --db-instance-identifier `sample-serverless-instance-2` \
    --promotion-tier `3`
```
