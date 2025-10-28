# Scaling Amazon DocumentDB

clusters

Amazon DocumentDB enables you to scale the storage and compute in your
clusters based on your needs. This section describes how you can use
storage scaling, instance scaling, and read scaling to manage
performance and scaling for your Amazon DocumentDB clusters and instances.

###### Topics

- [Storage scaling](#db-cluster-manage-scaling-storage "#db-cluster-manage-scaling-storage")
- [Instance scaling](#db-cluster-manage-scaling-instance "#db-cluster-manage-scaling-instance")
- [Read scaling](#db-cluster-manage-scaling-reads "#db-cluster-manage-scaling-reads")
- [Write scaling](#db-cluster-manage-scaling-writes "#db-cluster-manage-scaling-writes")

## Storage scaling

Amazon DocumentDB storage automatically scales with the data in your cluster
volume. As your data grows, your cluster volume storage grows in 10
GiB increments, up to 128 TiB.

## Instance scaling

You can scale your Amazon DocumentDB cluster as needed by modifying the
instance class for each instance in the cluster. Amazon DocumentDB supports
several instance classes that are optimized for Amazon DocumentDB.

For more information, see [Modifying an Amazon DocumentDB instance](db-instance-modify.md "db-instance-modify.md").

## Read scaling

You can achieve read scaling for your Amazon DocumentDB cluster by creating up to 15 Amazon DocumentDB replicas in the cluster. Each Amazon DocumentDB replica returns the same data from the cluster volume with minimal replica lag—usually less than 100 milliseconds after the primary instance has written an update. As your read traffic increases, you can create additional Amazon DocumentDB replicas and connect to them directly to distribute the read load for your cluster. Amazon DocumentDB replicas don't have to be of the same instance class as the primary instance.

For more information, see [Adding an Amazon DocumentDB instance to a cluster](db-instance-add.md "db-instance-add.md").

To read scale with Amazon DocumentDB, we recommend that you connect to your cluster as a replica set and distribute reads to replica instances using the built-in read preference capabilities of your driver. For more information, please see [Connecting to Amazon DocumentDB as a replica set](connect-to-replica-set.md "connect-to-replica-set.md").

## Write scaling

You can scale write capacity on your Amazon DocumentDB cluster by increasing the size of your cluster’s primary instance. This section provides two methods for scaling your cluster’s primary instance based on your needs. The first option seeks to minimize application impact but requires more steps to complete. The second option optimizes for simplicity as it has fewer steps, but it comes with the tradeoff of having more potential impact to your application.

Depending on your application, you can choose what approach below is best for you. For more information about available instance sizes and costs, see the [Amazon DocumentDB Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/") page.

1. **Optimize for high availability and
   performance** — If you are connecting to your
   cluster in [replica set mode](connect-to-replica-set.md "connect-to-replica-set.md")
   (recommended), you can use the following process to minimize
   the impact to your application when scaling your primary
   instance. This method minimizes impact because it keeps your
   cluster at or above your high availability, and read scaling
   targets are added to the cluster as instances, instead of
   being updated in place.
   1. Add one or more replicas of the larger instance type
      to your cluster (see [Adding an Amazon DocumentDB instance to a cluster](db-instance-add.md "db-instance-add.md")).
      We recommend all replicas be of the same or larger
      instance type as the primary. This avoids an unintentional
      reduction in write performance from failing over to a
      smaller instance type. For most customers, this means
      temporarily doubling the number of instances in their
      cluster, then removing the smaller replicas after
      scaling is complete.
   2. Set the failover tier on all new replicas to priority
      zero, ensuring a replica of the smaller instance type has
      the highest failover priority. For more information, see [Controlling the failover target](failover.md#failover-target_control "failover.md#failover-target_control").
   3. Initiate a manual failover, which will promote one of
      the new replicas to be the primary instance. For more
      information, see [Testing failover](failover.md#failover-testing "failover.md#failover-testing").

   ###### Note

   This will incur ~30 seconds of downtime for your
   cluster. Please plan accordingly. 4. Remove all replicas of an instance type smaller than
   your new primary from the cluster. 5. Set the failover tier of all instances back to the
   same priority (usually, this means setting them back to
   1).As an example, suppose that you have a cluster that currently contains three `r5.large` instances (one primary and two replicas), and you want to scale to an `r5.xlarge` instance type. To do so, you would first add three `r5.xlarge` replica instances to your cluster and then set the failover tier of the new `r5.xlarge` replicas to zero. Next, you would initiate a manual failover (understanding that your application will experience ~30 seconds of downtime). Once the failover is complete, you would remove all three `r5.large` instances from your cluster, leaving the cluster scaled to `r5.xlarge` instances.

To help optimize costs, Amazon DocumentDB instances are billed in one
second increments, with a ten minute minimum charge following
a billable status change such as creating, modifying, or
deleting an instance. For more information, see [Cost optimization](best_practices.md#best_practices-cost_optimization "best_practices.md#best_practices-cost_optimization")
in the best practices documentation. 2. **Optimize for simplicity** — This approach optimizes for simplicity. It doesn’t expand and contract the cluster, but it might temporarily reduce your read capacity.

It is possible that changing the instance class of a replica will result in that instance not serving requests for a brief period of time, from a few seconds to less than 30 seconds. If you are connecting to your cluster in [replica set mode](connect-to-replica-set.md "connect-to-replica-set.md") (recommended), then this would reduce your read capacity by one replica (e.g., to 66% capacity in a 3-node cluster, or 75% capacity in a 4-node cluster, etc.) during the scaling operation.

    1. Scale one of the replica instances in your cluster.
     For more information, see [Managing instance classes](db-instance-classes.md "db-instance-classes.md").
    2. Wait until the instance is available (see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md")).



    ###### Note

    This will incur ~30 seconds of downtime for your
     cluster. Please plan accordingly.
    3. Continue executing steps 1 and 2 until all replicas instances have been scaled, one by one.
    4. Initiate a manual failover. This will promote one of the replicas to be the primary instance. For more information, see [Amazon DocumentDB Failover](failover.md "failover.md").


    ###### Note

    This will incur up to 30 seconds of downtime for your cluster, but often takes less time than that. Please plan accordingly.
    5. Scale the former primary (now a replica) instance.
