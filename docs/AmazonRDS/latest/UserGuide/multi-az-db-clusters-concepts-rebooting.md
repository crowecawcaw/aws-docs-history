# Rebooting a Multi-AZ DB cluster and reader DB instances for Amazon RDS

You might need to reboot your Multi-AZ DB cluster, usually for maintenance reasons. For
example, if you make certain modifications or change the DB cluster parameter group
associated with a DB cluster, you reboot the DB cluster. Doing so causes the changes to take
effect.

If a DB cluster isn't using the latest changes to its associated DB cluster parameter group, the AWS Management Console shows the DB
cluster parameter group with a status of **pending-reboot**. The **pending-reboot** parameter
groups status doesn't result in an automatic reboot during the next maintenance window. To apply the latest parameter
changes to that DB cluster, manually reboot the DB cluster. For more information about parameter groups, see
[Parameter groups for Multi-AZ DB clusters](multi-az-db-clusters-concepts.md#multi-az-db-clusters-concepts-parameter-groups "multi-az-db-clusters-concepts.md#multi-az-db-clusters-concepts-parameter-groups").

Rebooting a DB cluster restarts the database engine service. Rebooting a DB cluster results in a momentary outage, during which
the DB cluster status is set to **rebooting**.

You can't reboot your DB cluster if it isn't in the **Available** state. Your database can be unavailable for
several reasons, such as an in-progress backup, a previously requested modification, or a maintenance-window action.

The time required to reboot your DB cluster depends on the crash recovery process, the
database activity at the time of reboot, and the behavior of your specific DB cluster. To
improve the reboot time, we recommend that you reduce database activity as much as possible
during the reboot process. Reducing database activity reduces rollback activity for
in-transit transactions.

###### Important

Multi-AZ DB clusters don't support reboot with a failover. When you reboot the writer
instance of a Multi-AZ DB cluster, it doesn't affect the reader DB instances in that DB cluster
and no failover occurs. When you reboot a reader DB instance, no failover occurs. To fail over a
Multi-AZ DB cluster, choose **Failover** in the console, call the AWS CLI command [`failover-db-cluster`](../../../cli/latest/reference/rds/failover-db-cluster.md "../../../cli/latest/reference/rds/failover-db-cluster.md"), or call the
API operation [`FailoverDBCluster`](../APIReference/API_FailoverDBCluster.md "../APIReference/API_FailoverDBCluster.md").

###### To reboot a DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose
   the Multi-AZ DB cluster that you want to reboot.
3. For **Actions**, choose **Reboot**.

The **Reboot DB cluster** page appears. 4. Choose **Reboot** to reboot your DB cluster.

Or choose **Cancel**.
To reboot a Multi-AZ DB cluster by using the AWS CLI, call the
[reboot-db-cluster](../../../cli/latest/reference/rds/reboot-db-cluster.md "../../../cli/latest/reference/rds/reboot-db-cluster.md") command.

```
aws rds reboot-db-cluster --db-cluster-identifier `mymultiazdbcluster`
```

To reboot a Multi-AZ DB cluster by using the Amazon RDS API, call the
[RebootDBCluster](../APIReference/API_RebootDBCluster.md "../APIReference/API_RebootDBCluster.md") operation.
