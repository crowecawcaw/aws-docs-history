# Managing the service updates

MemoryDB service updates are released on a regular basis. If you have one or more
qualifying clusters for those service updates, you receive notifications through email,
SNS, the Personal Health Dashboard (PHD), and Amazon CloudWatch events when the updates are released. The updates are also
displayed on the **Service Updates** page on the MemoryDB console. By
using this dashboard, you can view all the service updates and their status for your
MemoryDB fleet.

You control when to apply an update before an auto-update starts. We strongly recommend that you apply any updates of type **security-update**
as soon as possible to ensure that your MemoryDB are always up-to-date with current security patches.

The following sections explore these options in detail.

###### Topics

- [Amazon MemoryDB Managed maintenance and service updates overview](#managing-updates-maintenance "#managing-updates-maintenance")

## Amazon MemoryDB Managed maintenance and service updates overview

We frequently upgrade our MemoryDB fleet, with patches and upgrades being applied to instances seamlessly. We do this in one of the two ways:

1. Continuous managed maintenance.
2. Service updates.

These maintenance and service updates are required to apply upgrades that strengthen security, reliability, and operational performance.

Continuous managed maintenance happens from time to time and directly in your maintenance windows without requiring any action from your end. It's important to note that maintenance windows are mandatory for all customers, and you don't have the option to opt out. We strongly recommend avoiding any critical or important activities during these established maintenance windows. Additionally, please be aware that critical updates cannot be skipped to ensure the security and optimal performance of the system.

Service updates give you flexibility to apply them on your own. They are timed and may be moved into the maintenance window to be applied by us after their due date lapses.

You can manage updates by applying them at your earliest convenience or by replacing nodes, as updates are automatically applied on replacement. There will be no update activity during incoming maintenance windows if the updates have been applied to all nodes before them.

### Service updates

[Service updates in MemoryDB](service-updates.md "service-updates.md") enable you to apply certain service updates at your discretion. These updates can be of the following types: security patches or minor software updates. These updates help strengthen security, reliability, and operational performance of your clusters.

The value of these service updates is that you can control when to apply the update (e.g., you can delay applying service updates when there is an important business event that requires 24x7 availability of MemoryDB clusters).

If you have one or more qualifying clusters for those service updates, you receive notifications through email, the [Amazon SNS](mdbevents.md "mdbevents.md"), the [AWS Health Dashboard](../../../health/latest/ug/getting-started-health-dashboard.md "../../../health/latest/ug/getting-started-health-dashboard.md"), and [Amazon CloudWatch Events](monitoring-cloudwatch.md "monitoring-cloudwatch.md") events when the updates are released. The updates are also displayed on the **Service Updates** page on the MemoryDB console. By using this dashboard, you can view all the service updates and their status for your MemoryDB fleet.

You control when to apply an update before an auto-update starts. We strongly recommend that you apply any updates of type security-update as soon as possible to ensure that your MemoryDB are always up-to-date with current security patches.

Your cluster may be part of different service updates. Most of the updates do not require you to apply them separately. Applying one update to your cluster will mark the other updates as completed wherever applicable. You may need to apply multiple updates to the same cluster separately if the status does not change to “completed” automatically.

#### Service updates impact and downtime

When you or Amazon MemoryDB applies a service update to one or more MemoryDB clusters, the update is applied to no more than one node at a time within each shard until all selected clusters are updated. The nodes being updated will experience downtime of few seconds, while the rest of the cluster will continue to serve traffic.

- There will be no change in the cluster configuration.
- You will see a delay in your CloudWatch metrics that catch up as soon as possible.

**How does a node replacement impact my application?** - For MemoryDB nodes, the replacement process is designed to guarantee durability and availability. For single node MemoryDB clusters, MemoryDB dynamically spins up a replica, restores data from our durability components, and then fails over to it. For replication groups consisting of multiple nodes, MemoryDB replaces the existing replicas and syncs data from our durability components to the new replicas. MemoryDB is only Multi-AZ when there are more than 1 node so in this scenario, replacing the primary triggers a failover to a read replica. The planned node replacements complete while the cluster serves incoming write requests. If there is only one node, MemoryDB replaces the primary and then syncs the data from our durability components. The primary node is unavailable during this time, leading to longer write interruption.

**What best practices should I follow for a smooth replacement experience and minimize data loss?**

- In MemoryDB, data is highly durable, and data loss is not expected even in
  single node implementations. It is however recommended to implement Multi-AZ and
  backup strategies to minimize chances of loss in the unlikely event of failure.
  For a smooth replacement experience, we try to replace just enough nodes from
  the same cluster at a time to keep the cluster stable. You can provision primary
  and read replicas in different availability zones by enabling Multi-AZ. In this
  case, when a node is replaced, the primary role will failover to a replica in
  the shard. This shard will now serve traffic, and the data will be restored from
  its durability components. If your configuration includes only one primary and
  one single replica per shard, we recommend adding additional replicas prior to
  the patching. This will prevent reduced availability during the patching
  process. We recommend scheduling the replacement during a period with low
  incoming write traffic.

**What client configuration best practices should I follow to minimize application interruption during maintenance?** - In MemoryDB, the cluster mode configuration is always enabled, which provides the best availability during managed or unmanaged operations. The individual node endpoints of the replica nodes can be used for all the read operations. In MemoryDB, auto-failover is always enabled in the cluster, meaning the primary node may change. Therefore, the application should confirm the role of the node and update all the read endpoints to ensure that you aren't causing a major load on the primary. Similarly, avoid overloading the replicas with read requests during maintenance windows. One way to achieve this is to ensure that you have at least two read replicas to avoid any read interruption during maintenance.

It's important to test client applications to confirm that they comply with the Redis/Valkey Cluster protocol, and requests can be redirected across nodes properly. It is advisable to implement back-off and retry strategies to avoid overloading MemoryDB nodes during maintenance and replacement activities.

**Rescheduling** - You can defer the service update by changing the [maintenance window](maintenance-window.md "maintenance-window.md"). The scheduled update will only be applied to the cluster if the scheduled date matches the cluster's maintenance window. Once you change the maintenance window and the scheduled date has passed, the service update will be rescheduled to the newly specified window in the following weeks. You will receive a new notification one week before the new date has been reached.

Security at AWS is a shared responsibility. We strongly recommend that you apply the update at the earliest.

**Opting out of service updates** - You can determine if you can opt out of a service update by verifying the value of “Auto-update start date” attribute. If the value of “Auto-update start date” attribute of a service update is set, MemoryDB will schedule the service update to any remaining clusters for the upcoming maintenance window, and it is not possible to opt out. Still, if you apply the service update to the remaining clusters prior to the maintenance window, MemoryDB will not reapply the service update during the maintenance window. For more information, see [Applying the service updates](applying-updates.md "applying-updates.md").

**Why can’t the service updates be directly applied by MemoryDB during maintenance windows?** - Please note that the purpose of service updates is to give you flexibility on when to apply them. Clusters that are not participating in the MemoryDB-supported [compliance](memorydb-compliance.md "memorydb-compliance.md") programs can choose to not apply these updates, or apply them at a reduced frequency throughout the year. It is recommended however to apply the updates to remain compliant with regulations. This is true only when the value of “Auto-update start date” attribute of a service update is not present. For more information, see [Compliance validation for MemoryDB](memorydb-compliance.md "memorydb-compliance.md").

**How are updates applied in the maintenance window different from the service updates?** - Updates applied via continuous managed maintenance are directly scheduled in your maintenance windows without any action needed from your side. Service updates are timed and give you control on when you want to apply by the “Auto-update start date”. If they are still not applied by then, MemoryDB may schedule these updates in your maintenance window.

### Continuous Managed Maintenance Updates

These updates are mandatory and applied directly in your maintenance windows without any action needed from your side. These updates are separate than those offered by service updates.

#### Continuous maintenance impact and downtime

**How long does a node replacement take?** - A replacement typically completes within 30 minutes. The replacement may take longer in certain instance configurations and traffic patterns.

**How does a node replacement impact my application?** - Continuous Managed Maintenance Updates are applied in the same way as “Service updates”, through node replacement. Please refer to the Service updates impact and downtime section above for details.

**How do I manage node replacements on my own?** - You have the option to manage these replacements yourself at any time before the scheduled node replacement window. If you choose to manage the replacement yourself, you can take various actions depending on your use case.

- [Replace a node in cluster with one or more shards](nodes.md "nodes.md"): You can either use [backup and restore](snapshots-restoring.md "snapshots-restoring.md") or scale-out followed by a scale-in to [replace the nodes](cluster-resharding-online.md "cluster-resharding-online.md").
- [Change your maintenance window](maintenance-window.md "maintenance-window.md"): Also, you can change your cluster’s maintenance window. For changing your maintenance window to a more convenient time later, you can use [UpdateCluster API](clusters.md "clusters.md"), [update-cluster CLI](../../../cli/latest/reference/memorydb/update-cluster.md "../../../cli/latest/reference/memorydb/update-cluster.md") or click on [Modify](clusters.md "clusters.md") in the MemoryDB Management Console. Once you change your maintenance window, MemoryDB will schedule your node for maintenance during the newly specified window.

To see how this works in practice, let's say it's currently Thursday 11/09 at 1500 and the next maintenance window is Friday, 11/10, at 1700. Here are 3 scenarios:

    + You change your maintenance window to Friday at 1600 (after the current date time and before the next scheduled maintenance window). The node will be replaced on Friday, 11/10, at 1600.
    + You change your maintenance window to Saturday at 1600 (after the current date time and after the next scheduled maintenance window). The node will be replaced on Saturday, 11/11, at 1600.
    + You change your maintenance window to Wednesday at 1600 (earlier in the week than the current date time). The node will be replaced next Wednesday, 11/15, at 1600.

For more information, see [Managing maintenance](maintenance-window.md "maintenance-window.md").

Please note that the nodes in different clusters from different regions can be replaced at the same time providing that your maintenance window for these clusters is configured to be the same.

**How do I find out about upcoming scheduled replacements?** - You should get health notification on the AWS health Dashboard. Also you can find the status of different services upgrades with DescribeServiceUpdates API. Please note that we put all the efforts to proactively notify customers about foreseeable replacements. However, in exceptional cases like unpredictable failures, there may be unannounced replacements.

**Can I change the scheduled maintenance at a more suitable time?** - Yes, you can defer the scheduled maintenance to a more suitable time by changing the [maintenance window](../APIReference/API_DescribeServiceUpdates.md "../APIReference/API_DescribeServiceUpdates.md").

**Why are you doing these node replacements?** - These replacements are needed to apply mandatory software updates to your underlying host. The updates help strengthen our security, reliability, and operational performance.

**Do these replacements affect my nodes in Multiple Availability Zones and clusters from different regions at the same time?** - Replacements can run in multiple Availability Zones or regions in parallel, depending on the maintenance window for clusters.
