# Migrating to Amazon DocumentDB serverless

###### Topics

- [Migrating existing DocumentDB clusters to serverless](#w5aac41c19b5 "#w5aac41c19b5")
- [Migrating from MongoDB to DocumentDB serverless](#w5aac41c19b7 "#w5aac41c19b7")

## Migrating existing DocumentDB clusters to serverless

### Upgrading a cluster’s engine version

If your provisioned cluster is running a lower engine version that does not support DocumentDB serverless, you need to first upgrade the cluster to a supported engine version.
For more information, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md "docdb-mvu.md").

### Migrating a provisioned cluster to DocumentDB serverless

To switch a provisioned cluster to use DocumentDB serverless, follow these steps:

1. Check if the provisioned cluster’s engine version needs to be upgraded to be used with DocumentDB serverless.
   See [Requirements and limitations for DocumentDB serverless](docdb-serverless-limitations.md "docdb-serverless-limitations.md").

###### Note

If the provisioned cluster is running an engine version that isn't available for DocumentDB serverless, upgrade the engine version of the cluster.
See [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md "docdb-mvu.md"). 2. Configure the scaling configuration for the cluster.
For details on choosing the scaling configuration, see [Choosing the scaling capacity range for a DocumentDB serverless cluster](docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing "docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing").
To modify the scaling configuration for a cluster, see [Viewing and modifying a cluster’s scaling capacity range configuration](docdb-serverless-managing.md#docdb-serverless-range-config "docdb-serverless-managing.md#docdb-serverless-range-config"). 3. Configure any other cluster properties to account for the DocumentDB serverless requirements and limitations from [Requirements and limitations for DocumentDB serverless](docdb-serverless-limitations.md "docdb-serverless-limitations.md"). 4. Add one or more DocumentDB serverless instances to the cluster. Follow the procedure in [Adding an Amazon DocumentDB serverless instance](docdb-serverless-create-cluster.md#docdb-serverless-adding-instance "docdb-serverless-create-cluster.md#docdb-serverless-adding-instance").

###### Note

In some cases, you might already have one or more provisioned reader instances in the cluster.
If so, you can choose to convert one of the readers to a DocumentDB serverless instance instead of creating a new instance.
To do so, follow the procedure in [Changing an instance's class](db-instance-classes.md#db-instance-class-changing "db-instance-classes.md#db-instance-class-changing"). 5. (Optional) Perform a failover operation to make a DocumentDB serverless instance the cluster writer.
See [Amazon DocumentDB Failover](failover.md "failover.md"). 6. (Optional) Convert any remaining provisioned Amazon DocumentDB instances to DocumentDB serverless instances (see [Changing an instance's class](db-instance-classes.md#db-instance-class-changing "db-instance-classes.md#db-instance-class-changing")) or remove them from the cluster (see [Deleting an Amazon DocumentDB instance](db-instance-delete.md "db-instance-delete.md")).

Using the AWS Management Console
The following AWS Management Console configuration example shows the migration process using an Amazon DocumentDB provisioned cluster that is running Amazon DocumentDB 5.0.0, which does not require an engine version upgrade to start using DocumentDB serverless.
The cluster is named `sample`, and starts with three provisioned instances named `sample`, `sample2`, and `sample3`.
In this example, these three instances will be replaced by three serverless instances.

1. Sign into the [AWS Management Console](../../../https:/console.aws.amazon.com/docdb/home.md "../../../https:/console.aws.amazon.com/docdb/home.md") and open the Amazon DocumentDB console.
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page.

The **Clusters** table appears. 3. In the **Clusters** table, select the checkbox of the cluster to which you want to add a serverless instance. 4. Choose **Actions**, and then choose **Add instances**. 5. In the **Add instances** dialog box, select **Serverless** in the **DB instance class** section for each new serverless instance you want to create. 6. For **Serverless capacity settings**, set the scaling configuration based on the capacity description in the dialog box. 7. (Optional) To add another instance, choose **Add instance**.
Continue adding instances until you have reached the desired number of new instances.

In this example, three new serverless instances are created. 8. Choose **Create**.

It takes several minutes to create an instance. You can use the console or the AWS CLI to view the instance's status.
For more information, see [Monitoring an Amazon DocumentDB Cluster's Status](monitoring_docdb-cluster_status.md "monitoring_docdb-cluster_status.md"). 9. Returning to the **Clusters** table, select the checkboxes of all three of the original provisioned instances. 10. Choose **Actions**, and then choose **Delete**.

During the deletion, a failover is automatically performed to promote one of the remaining instances to be the writer.
After a few minutes, the delete process is completed. The existing cluster now contains three DocumentDB serverless instances (as defined in the **Size** column).

Using the AWS CLI
The following AWS CLI configuration example shows the migration process using an Amazon DocumentDB provisioned cluster that is running Amazon DocumentDB 5.0.0, which does not require an engine version upgrade to start using DocumentDB serverless.
The cluster is named `sample`, and starts with three provisioned instances named `sample`, `sample2`, and `sample3`.
In this example, these three instances will be replaced by three serverless instances.
The cluster is named `sample-cluster`, and starts with two provisioned instances named `sample-provisioned-instance-1` and `sample-provisioned-instance-2`, a writer instance and a reader instance.

In the following example, replace each `user input placeholder` with your own information or configuration parameters.

Use the `aws docdb describe-db-clusters` operation to determine the status of a cluster. The following code finds the status of the cluster `sample-cluster` and outputs the results in a table:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier `sample-cluster` \
    --query 'DBClusters[*].DBClusterMembers' \
    --output table
```

```
--------------------------------------------------------------------------------------------------------
|                                          DescribeDBClusters                                          |
+--------------------------------+---------------------------------+------------------+----------------+
|  DBClusterParameterGroupStatus |      DBInstanceIdentifier       | IsClusterWriter  | PromotionTier  |
+--------------------------------+---------------------------------+------------------+----------------+
|  in-sync                       |  sample-provisioned-instance-2  |  False           |  1             |
|  in-sync                       |  sample-provisioned-instance-1  |  True            |  1             |
+--------------------------------+---------------------------------+------------------+----------------+
```

Add the scaling configuration for the cluster:

```
aws docdb modify-db-cluster \
    --db-cluster-identifier `sample-cluster` \
    --serverless-v2-scaling-configuration MinCapacity=`0.5`,MaxCapacity=`16`
```

Add the serverless instances.
In this example, new serverless instances named `sample-serverless-instance-1` and `sample-serverless-instance-2` are added:

```
aws docdb create-db-instance \
    --db-cluster-identifier `sample-cluster` \
    --db-instance-identifier `sample-serverless-instance-1` \
    --db-instance-class db.serverless \
    --engine docdb

aws docdb create-db-instance \
    --db-cluster-identifier `sample-cluster` \
    --db-instance-identifier `sample-serverless-instance-2` \
    --db-instance-class db.serverless \
    --engine docdb
```

Enter the following to wait for the serverless instances to be available before proceeding:

```
aws docdb wait db-instance-available \
    --db-instance-identifier sample-serverless-instance-1

aws docdb wait db-instance-available \
    --db-instance-identifier sample-serverless-instance-2
```

Perform a failover to make the new `sample-serverless-instance-1` instance the cluster writer:

```
aws docdb failover-db-cluster \
    --db-cluster-identifier `sample-cluster` \
    --target-db-instance-identifier `sample-serverless-instance-1`
```

The failover takes a few seconds to complete, after which sample-serverless-instance-1 becomes the cluster writer. Verify this with the following input:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier `sample-cluster` \
    --query 'DBClusters[*].DBClusterMembers' \
    --output table
```

```
--------------------------------------------------------------------------------------------------------
|                                          DescribeDBClusters                                          |
+--------------------------------+---------------------------------+------------------+----------------+
|  DBClusterParameterGroupStatus |      DBInstanceIdentifier       | IsClusterWriter  | PromotionTier  |
+--------------------------------+---------------------------------+------------------+----------------+
|  in-sync                       |  sample-provisioned-instance-2  |  False           |  1             |
|  in-sync                       |  sample-provisioned-instance-1  |  False           |  1             |
|  in-sync                       |  sample-serverless-instance-2   |  False           |  1             |
|  in-sync                       |  sample-serverless-instance-1   |  True            |  1             |
+--------------------------------+---------------------------------+------------------+----------------+
```

Finally, delete the original provisioned instances:

```
aws docdb delete-db-instance \
    --db-instance-identifier `sample-provisioned-instance-1`

aws docdb delete-db-instance \
    --db-instance-identifier `sample-provisioned-instance-2`
```

## Migrating from MongoDB to DocumentDB serverless

You can migrate your MongoDB databases to DocumentDB serverless, just as with provisioned Amazon DocumentDB.
For more information, see [Migrating to Amazon DocumentDB](docdb-migration.md "docdb-migration.md").
