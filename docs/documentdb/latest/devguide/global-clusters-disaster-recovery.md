

# Disaster recovery and Amazon DocumentDB global clusters
<a name="global-clusters-disaster-recovery"></a>

**Topics**
+ [Performing a managed failover for an Amazon DocumentDB global cluster](#managed-failover)
+ [Performing a manual failover for an Amazon DocumentDB global cluster](#manual-failover)
+ [Performing a switchover for an Amazon DocumentDB global cluster](#global-cluster-switchover)
+ [Unblocking a global cluster switchover or failover](#unblocking-gc-so-fo)
+ [Managing RPOs for Amazon DocumentDB global clusters](#global-clusters-manage-recovery)

By using a global cluster, you can recover from disasters such as Region failures quickly. Recovery from disaster is typically measured using values for RTO and RPO.
+ **Recovery time objective (RTO)** — The time it takes a system to return to a working state after a disaster. In other words, RTO measures downtime. For a global cluster, RTO in minutes.
+ **Recovery point objective (RPO)** — The amount of data that can be lost (measured in time). For a global cluster, RPO is typically measured in seconds. 
+ To recover from an unplanned outage, you can perform a cross-Region failover to one of the secondaries in your global cluster. When your global cluster has multiple secondary Regions, make sure that you detach all the secondary Regions that you wish to promote as primaries. Then, you promote one of those secondary Regions to be the new primary AWS Region. Finally, you create new clusters in each of the other secondary Regions and attach those clusters to your global cluster.

## Performing a managed failover for an Amazon DocumentDB global cluster
<a name="managed-failover"></a>

This approach is intended for business continuity in the event of a true Regional disaster or complete service-level outage.

During a managed failover, your primary cluster is failed over to your choice of secondary Region while your Amazon DocumentDB global cluster's existing replication topology is maintained. The chosen secondary cluster promotes one of its read-only nodes to full writer status. This step allows the cluster to assume the role of primary cluster. Your database is unavailable for a short time while this cluster is assuming its new role. Data that wasn't replicated from the old primary to the chosen secondary cluster may be missing when this secondary becomes the new primary. The old primary volume makes a best effort attempt to take a snapshot before synchronizing with the new primary so unreplicated data is preserved on the snapshot.

**Note**  
You can only perform a managed cross-Region cluster failover on an Amazon DocumentDB global cluster if the primary and all secondary clusters have the same engine versions. If your engine versions are incompatible, you can perform the failover manually by following the steps in [Performing a manual failover for an Amazon DocumentDB global cluster](#manual-failover).  
If the Region's engine versions do not match, the failover will be blocked. Check for any pending upgrades and apply them to ensure all Region's engine versions match and the global cluster failover is unblocked. For more information, see [Unblocking a global cluster switchover or failover](#unblocking-gc-so-fo).

To minimize data loss, do the following before using this feature:
+ Take applications offline to prevent writes from being sent to the primary cluster of the Amazon DocumentDB global cluster.
+ Check lag times for all Amazon DocumentDB secondary clusters. Choosing the secondary Region with the least replication lag can minimize data loss with the current failed primary Region. Check lag times for all Amazon DocumentDB secondary clusters in the global cluster by viewing the `GlobalClusterReplicationLag` metric in Amazon CloudWatch. These metrics show you how far behind (in milliseconds) replication to a secondary cluster is to the primary cluster.

  For more information about CloudWatch metrics for Amazon DocumentDB, see [Amazon DocumentDB metrics](cloud_watch.md#cloud_watch-metrics_list).

During a managed failover, the chosen secondary cluster is promoted to its new role as primary. However, it doesn't inherit the various configuration options of the primary cluster. A mismatch in configuration can lead to performance issues, workload incompatibilities, and other anomalous behavior. To avoid such issues, resolve differences between your Amazon DocumentDB global clusters for the following:
+ **Configure an Amazon DocumentDB cluster parameter group for the new primary, if necessary** — You can configure your Amazon DocumentDB cluster parameter groups independently for each cluster in your Amazon DocumentDB global cluster. Therefore, when you promote a secondary cluster to take over the primary role, the parameter group from the secondary might be configured differently than for the primary. If so, modify the promoted secondary cluster's parameter group to conform to your primary cluster's settings. To learn how, see [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md).
+ **Configure monitoring tools and options, such as Amazon CloudWatch events and alarms** — Configure the promoted cluster with the same logging ability, alarms, and so on as needed for the global cluster. As with parameter groups, configuration for these features isn't inherited from the primary during the failover process. Some CloudWatch metrics, such as replication lag, are only available for secondary Regions. Thus, a failover changes how to view those metrics and set alarms on them, and could require changes to any predefined dashboards. For more information about Amazon DocumentDB clusters and monitoring, see [Monitoring and logging in Amazon DocumentDB](monitoring_docdb.md).

Typically, the chosen secondary cluster assumes the primary role within a minute. As soon as the new primary Region's writer node is available, you can connect your applications to it and resume your workloads. After Amazon DocumentDB promotes the new primary cluster, it automatically rebuilds all additional secondary Region clusters.

Because Amazon DocumentDB global clusters use asynchronous replication, the replication lag in each secondary Region can vary. Amazon DocumentDB rebuilds these secondary Regions to have the exact same point-in-time data as the new primary Region cluster. The duration of the complete rebuilding task can take a few minutes to several hours, depending on the size of the storage volume and the distance between the Regions. When the secondary Region clusters finish rebuilding from the new primary Region, they become available for read access. As soon as the new primary writer is promoted and available, the new primary Region's cluster can handle read and write operations for the Amazon DocumentDB global cluster.

To restore the global cluster's original topology, Amazon DocumentDB monitors the availability of the old primary Region. As soon as that Region is healthy and available again, Amazon DocumentDB automatically adds it back to the global cluster as a secondary Region. Before creating the new storage volume in the old primary Region, Amazon DocumentDB tries to take a snapshot of the old storage volume at the point of failure. It does this so that you can use it to recover any of the missing data. If this operation is successful, Amazon DocumentDB places this snapshot named "rds:docdb-unplanned-global-failover-name-of-old-primary-DB-cluster-timestamp" in the snapshot section of the AWS Management Console. You can also see this snapshot listed in the information returned by the `DescribeDBClusterSnapshots` API operation.

**Note**  
The snapshot of the old storage volume is a system snapshot that's subject to the backup retention period configured on the old primary cluster. To preserve this snapshot outside of the retention period, you can copy it to save it as a manual snapshot. To learn more about copying snapshots, including pricing, see [Copying a cluster snapshot](backup_restore-copy_cluster_snapshot.md#backup_restore-copy_a_cluster_snapshot).

After the original topology is restored, you can fail back your global cluster to the original primary Region by performing a switchover operation when it makes the most sense for your business and workload. To do so, follow the steps in [Performing a switchover for an Amazon DocumentDB global cluster](#global-cluster-switchover).

You can fail over your Amazon DocumentDB global cluster using the AWS Management Console, the AWS CLI, or the Amazon DocumentDB API.

------
#### [ Using the AWS Management Console ]

**Perform a managed failover on your Amazon DocumentDB global cluster**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Clusters**.

1. Find and choose the Amazon DocumentDB global cluster you want to fail over.  
![Image: Cluster table with global cluster selected.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/failover-cluster-table.png)

1. Choose **Switchover or Failover** from the **Actions** menu.

1. On the dialog box that appears, choose **Failover**, then choose the secondary cluster from the **New primary cluster** field drop down list.  
![Image: Global cluster switchover or failover dialog box.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/switch-fail-confirm.png)

1. Type "confirm" in the last field. Then choose **Confirm**.

   The status of the primary cluster changes to "**Failing-over**". This condition should take approximately one minute. During this time, the status of the new primary cluster shows "**Modifying...**". Once the new primary is promoted, it will show "**Available**" and will be able to serve read and write transactions. The secondary Regions including the old primary will show "**Resyncing...**" while it resynchronizes to the new primary. Similar to the new primary, it will only be able to serve transaction once the status changes to "**Available**".

1. When complete, the original primary cluster becomes the secondary cluster. The selected secondary cluster becomes the primary cluster.  
![Image: Cluster table showing new primary cluster.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/failover-complete.png)

------
#### [ Using the AWS CLI ]

**Perform a managed failover on your Amazon DocumentDB global cluster**

Run the [`failover-global-cluster`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/failover-global-cluster.html) CLI command to fail over your Amazon DocumentDB global cluster. With the command, pass values for the following options:
+ `--region`
+ `--global-cluster-identifier`
+ `--target-db-cluster-identifier`
+ `--allow-data-loss`

In the following examples, replace each {{user input placeholder}} with your cluster's information.

For Linux, macOS, or Unix:

```
aws docdb failover-global-cluster \
   --region {{region_of_selected_secondary}} \
   --global-cluster-identifier {{global_cluster_id}} \
   --target-db-cluster-identifier {{arn_of_secondary_to_promote}} \
   --allow-data-loss
```

For Windows:

```
aws docdb failover-global-cluster ^
   --region {{region_of_selected_secondary}} ^
   --global-cluster-identifier {{global_cluster_id}} ^
   --target-db-cluster-identifier {{arn_of_secondary_to_promote}} ^
   --allow-data-loss
```

------

## Performing a manual failover for an Amazon DocumentDB global cluster
<a name="manual-failover"></a>

If an entire cluster in one AWS Region becomes unavailable, you can promote another cluster in the global cluster to have read/write capability.

You can manually activate the global cluster failover mechanism if a cluster in a different AWS Region is a better choice to be the primary cluster. For example, you might increase the capacity of one of the secondary clusters and then promote it to be the primary cluster. Or the balance of activity among the AWS Regions might change, so that switching the primary cluster to a different AWS Region might give lower latency for write operations.

The following procedure outlines what to do to promote one of the secondary clusters in an Amazon DocumentDB global cluster.

To promote a secondary cluster:

1. Stop issuing DML statements and other write operations to the primary cluster in the AWS Region with the outage.

1. Identify a cluster from a secondary AWS Region to use as a new primary cluster. If you have two (or more) secondary AWS Regions in your global cluster, choose the secondary cluster that has the least lag time.

1. Detach your chosen secondary cluster from the global cluster.

   Removing a secondary cluster from a global cluster immediately stops the replication from the primary to this secondary and promotes it to standalone provisioned cluster with full read/write capabilities. Any other secondary cluster associated with the primary cluster in the Region with the outage are still available and can accept calls from your application. They also consume resources. Since you are recreating the global cluster, to avoid split-brain and other issues, remove the other secondary clusters before creating the new global cluster in the steps that follow.

   For detailed steps for detaching, see [Removing a cluster from an Amazon DocumentDB global cluster](global-clusters.manage.md#global-clusters.remove).

1. This cluster becomes the primary cluster of a new global cluster when you start adding Regions to it, in the next step.

1. Add an AWS Region to the cluster. When you do this, the replication process from primary to secondary begins.

1. Add more AWS Regions as needed to re-create the topology needed to support your application. Make sure that application writes are sent to the correct cluster before, during, and after making changes such as these, to avoid data inconsistencies among the clusters in the global cluster (split-brain issues).

1. When the outage is resolved and you're ready to assign your original AWS Region as the primary cluster again, perform the same steps in reverse.

1. Remove one of the secondary clusters from the global cluster. This will enable it to serve read/write traffic. 

1. Redirect all the write traffic to the primary cluster in the original AWS Region.

1. Add an AWS Region to set up one or more secondary clusters in the same AWS Region as before.

Amazon DocumentDB global clusters can be managed using AWS SDKs, enabling you to create solutions to automate global cluster failover process for Disaster Recovery and Business Continuity Planning use cases. One such solution is made available for our customers under Apache 2.0 licensing and can be accessed from our tools repository [here](https://github.com/awslabs/amazon-documentdb-tools/tree/master/global-clusters-automation). This solution leverages Amazon Route 53 for endpoint management and provides AWS Lambda functions that can be triggered based appropriate events.

## Performing a switchover for an Amazon DocumentDB global cluster
<a name="global-cluster-switchover"></a>

By using switchovers, you can change the Region of your primary cluster on a routine basis. This approach is intended for controlled scenarios, such as operational maintenance and other planned operational procedures.

There are three common use cases for using switchovers:
+ For "regional rotation" requirements imposed on specific industries. For example, financial service regulations might want tier-0 systems to switch to a different Region for several months to ensure that disaster recovery procedures are regularly exercised.
+ For multi-Region "follow-the-sun" applications. For example, a business might want to provide lower latency writes in different Regions based on business hours across different time zones.
+ As a zero-data-loss method to fail back to the original primary Region after a failover.

**Note**  
Switchovers are designed to be used on a healthy Amazon DocumentDB global cluster. To recover from an unplanned outage, follow the appropriate procedure in [Performing a manual failover for an Amazon DocumentDB global cluster](#manual-failover).  
To perform a switchover, all secondary Regions must be running the exact same engine version as the primary. If the Region's engine versions do not match, the switchover will be blocked. Check for any pending upgrades and apply them to ensure all Region's engine versions match and the global cluster switchover is unblocked. For more information, see [Unblocking a global cluster switchover or failover](#unblocking-gc-so-fo).

During a switchover, Amazon DocumentDB switches over your primary cluster to your chosen secondary Region while it maintains your global cluster's existing replication topology. Before it starts the switchover process, Amazon DocumentDB waits for all secondary Region clusters to be fully synchronized with the primary Region cluster. Then, the DB cluster in the primary Region becomes read-only and the chosen secondary cluster promotes one of its read-only nodes to full writer status. Promoting this node to a writer allows that secondary cluster to assume the role of primary cluster. Because all secondary clusters were synchronized with the primary at the beginning of the process, the new primary continues operations for the Amazon DocumentDB global cluster without losing any data. Your database is unavailable for a short time while the primary and selected secondary clusters are assuming their new roles.

To optimize application availability, do the following before using this feature:
+ Perform this operation during nonpeak hours or at another time when writes to the primary cluster are minimal.
+ Take applications offline to prevent writes from being sent to the primary cluster of the Amazon DocumentDB global cluster.
+ Check lag times for all Amazon DocumentDB secondary clusters in the global cluster by viewing the `GlobalClusterReplicationLag` metric in Amazon CloudWatch. This metric shows you how far behind (in milliseconds) replication to a secondary cluster is to the primary cluster. This value is directly proportional to the time it takes for Amazon DocumentDB to complete the switchover. Therefore, the larger the lag value, the longer the switchover will take.

  For more information about CloudWatch metrics for Amazon DocumentDB, see [Amazon DocumentDB metrics](cloud_watch.md#cloud_watch-metrics_list).

During a switchover, the chosen secondary DB cluster is promoted to its new role as primary. However, it doesn't inherit the various configuration options of the primary DB cluster. A mismatch in configuration can lead to performance issues, workload incompatibilities, and other anomalous behavior. To avoid such issues, resolve differences between your Amazon DocumentDB global clusters for the following:
+ **Configure Amazon DocumentDB DB cluster parameter group for the new primary, if necessary** — You can configure your Amazon DocumentDB cluster parameter groups independently for each cluster in your Amazon DocumentDB global cluster. That means that when you promote a secondary DB cluster to take over the primary role, the parameter group from the secondary might be configured differently than for the primary. If so, modify the promoted secondary DB cluster's parameter group to conform to your primary cluster's settings. To learn how, see [Managing Amazon DocumentDB cluster parameter groups](cluster_parameter_groups.md).
+ **Configure monitoring tools and options, such as Amazon CloudWatch Events and alarms** — Configure the promoted cluster with the same logging ability, alarms, and so on as needed for the global cluster. As with parameter groups, configuration for these features isn't inherited from the primary during the switchover process. Some CloudWatch metrics, such as replication lag, are only available for primary Regions. Thus, a switchover changes how to view those metrics and set alarms on them, and could require changes to any predefined dashboards. For more information, see [Monitoring and logging in Amazon DocumentDB](monitoring_docdb.md).

**Note**  
Typically, the role switchover can take up to several minutes.

When the switchover process completes, the promoted Amazon DocumentDB cluster can handle write operations for the global cluster.

You can switch over your Amazon DocumentDB global cluster using the AWS Management Console or the AWS CLI:

------
#### [ Using the AWS Management Console ]

**Perform a switchover on your Amazon DocumentDB global cluster**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Clusters**.

1. Find and select the Amazon DocumentDB global cluster you want to switch over.  
![Image: Cluster table with global cluster selected.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/switchover-cluster-table.png)

1. Choose **Switchover or Failover** from the **Actions **menu.

1. On the dialog box that appears, choose **Switchover**, then choose the secondary cluster from the **New primary cluster** field drop down list.  
![Image: Cluster switch over dialog with secondary cluster selected.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/switch-fail-confirm-2.png)

1. Choose **Confirm**.

   The status of the primary cluster changes to "**Switching-over**". This condition should take approximately three minutes. During this time, the status of all regional clusters show "**Modifying...**". Once the Regions are synchronized and the new primary is promoted, it will show "**Available**" for all status fields and will be able to serve transactions.

1. When complete, the original primary cluster becomes the secondary cluster. The selected secondary cluster becomes the primary cluster.  
![Image: Cluster table showing new primary cluster.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/failover-complete.png)

------
#### [ Using the AWS CLI ]

**Perform a switchover on your Amazon DocumentDB global cluster**

Run the [`switchover-global-cluster`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/switchover-global-cluster.html) CLI command to switch over your Amazon DocumentDB global cluster. With the command, pass values for the following options:
+ `--region`
+ `--global-cluster-identifier`
+ `--target-db-cluster-identifier`

In the following examples, replace each {{user input placeholder}} with your cluster's information.

For Linux, macOS, or Unix:

```
aws docdb switchover-global-cluster \
   --region {{region_of_primary}} \
   --global-cluster-identifier {{global_cluster_id}} \
   --target-db-cluster-identifier {{arn_of_secondary_to_promote}}
```

For Windows:

```
aws docdb switchover-global-cluster ^
   --region {{region_of_primary}} ^
   --global-cluster-identifier {{global_cluster_id}} ^
   --target-db-cluster-identifier {{arn_of_secondary_to_promote}}
```

------

## Unblocking a global cluster switchover or failover
<a name="unblocking-gc-so-fo"></a>

Global cluster switchovers and failovers are blocked when not all regional clusters in the global cluster are on the same engine version. If the versions don't match, you might see this error when calling a switchover or failover: The target DB cluster specified is running an engine version with a different patch level than the source DB cluster. Routinely apply the latest engine versions to keep your global clusters in a healthy state.

To resolve this error, update all secondary Regions first, and then the primary Region to the same engine version by applying any pending maintenance action items. To view pending maintenance action items, and to apply any needed changes to correct the issue, perform the instructions in one of the following tabs:

------
#### [ Using the AWS Management Console ]

To unblock a global cluster switchover or failover, you must determine if there are any pending maintenance actions for your clusters and apply them. Follow these steps to view and apply maintenance actions:

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Clusters**.

1. In the **Clusters** table, locate your global cluster in the **Cluster identifier** column. Under your global cluster, take note of each secondary cluster and the primary cluster for the given global cluster, and perform the following steps for each.

1. For each secondary cluster:

   1. If an update is available for your cluster, it is indicated as **Available**, **Required**, or **Next Window** in the **Maintenance** column.

   1. To take an action, choose the cluster to show it's details, then choose **Maintenance & backups**. The **Pending Maintenance** items appear.

   1. Under **Description**, if it indicates that a "New maintenance update is available", select it and then choose **Apply now**.

1. For your primary cluster:

   1. If an update is available for your cluster, it is indicated as **Available**, **Required**, or **Next Window** in the **Maintenance** column.

   1. To take an action, choose the cluster to show it's details, then choose **Maintenance & backups**. The **Pending Maintenance** items appear.

   1. Under **Description**, if it indicates that a "New maintenance update is available", select it and then choose **Apply now**.

------
#### [ Using the AWS CLI ]

To unblock a global cluster switchover or failover, you must determine if there are any pending maintenance actions for the cluster and apply them. Follow these steps to view and apply maintenance actions first on the secondary clusters then on the primary cluster for your global cluster:

1. Run the following on each secondary Region's regional cluster first and then for the primary Regions regional cluster.

1. Run the [`describe-pending-maintenance-actions`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-pending-maintenance-actions.html) CLI command with the `--resource-identifier` option to determine if any maintenance actions are available for your Amazon DocumentDB regional cluster.

   In the following examples, replace each {{user input placeholder}} with your cluster's information.

   For Linux, macOS, or Unix:

   ```
   aws docdb describe-pending-maintenance-action \
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}}
   ```

   For Windows:

   ```
   aws docdb describe-pending-maintenance-action ^
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}}
   ```

   The result looks similar to this:

   ```
   {
       "PendingMaintenanceActions": [
           {
               "ResourceIdentifier": "arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15",
               "PendingMaintenanceActionDetails": [
                   {
                       "Action": "system-update",
                       "CurrentApplyDate": "2025-04-11T03:01:00Z",
                       "Description": "db-version-upgrade",
                       "ForcedApplyDate": "2025-06-18T03:01:00Z",
                       "AutoAppliedAfterDate": "2025-05-11T03:01:00Z"
                       "OptInStatus": "pending"
                   }
               ]
           }
       ]
   }
   ```

1. If a maintenance action is needed, run the [`apply-pending-maintenance-action`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/apply-pending-maintenance-action.html) CLI command with the following options:
   + `--resource-identifier`
   + `--apply-action`
   + `--opt-in-type`
   + `--region`

   In the following examples, replace each {{user input placeholder}} with your cluster's information.

   For Linux, macOS, or Unix:

   ```
   aws docdb apply-pending-maintenance-action \
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}} \
      --apply-action {{system-update}} \
      --opt-in-type {{immediate}} \
      --region {{us-east-1}}
   ```

   For Windows:

   ```
   aws docdb apply-pending-maintenance-action ^
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}} ^
      --apply-action {{system-update}} ^
      --opt-in-type immediate ^
      --region {{us-east-1}}
   ```

1. Once the maintenance action has completed, run the [`describe-pending-maintenance-actions`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-pending-maintenance-actions.html) command again to ensure that there are no other actions pending for your cluster.

   The result you want is:

   ```
   {
       "PendingMaintenanceActions": []
   }
   ```

------
#### [ Using the Amazon DocumentDB API ]

To unblock a global cluster switchover or failover, you must determine if there are any pending maintenance actions for the cluster and apply them. Use the following APIs to view and apply maintenance actions:

1. Run the following on each secondary Region's regional cluster first and then for the primary Regions regional cluster.

1. Call the [PendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/APIReference/API_PendingMaintenanceAction.html) API to determine if any maintenance actions are available for your Amazon DocumentDB global cluster.

1. Apply any changes by calling the [ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/APIReference/API_ApplyPendingMaintenanceAction.html) API.

------

Switchovers and failovers are also blocked when the target secondary cluster has a scheduled change that hasn't been applied yet, such as a modification or maintenance action you requested for the next maintenance window. In this case, you might see this error when calling a switchover or failover: You can't fail over to the cluster with ARN {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}} because it's being modified or because modifications are pending. Try again when the cluster becomes available. To unblock the operation, remove the scheduled change on the target cluster. The steps depend on the type of change. After the scheduled change is removed and the cluster status returns to `available`, retry the switchover or failover.

You can't cancel a scheduled maintenance action (undo an opt-in) from the AWS Management Console, so use the AWS CLI.

------
#### [ Using the AWS CLI ]

1. Run the [describe-pending-maintenance-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-pending-maintenance-actions.html) CLI command with the `--resource-identifier` option, and look for a maintenance action whose `OptInStatus` is `next-maintenance`.

   In the following examples, replace each {{user input placeholder}} with your cluster's information.

   For Linux, macOS, or Unix:

   ```
   aws docdb describe-pending-maintenance-actions \
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}} \
      --region {{us-east-1}}
   ```

   For Windows:

   ```
   aws docdb describe-pending-maintenance-actions ^
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}} ^
      --region {{us-east-1}}
   ```

   The result looks similar to the following. Note the `Action` value (`os-upgrade` in this example), which you use in the next step.

   ```
   {
       "PendingMaintenanceActions": [
           {
               "ResourceIdentifier": "arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15",
               "PendingMaintenanceActionDetails": [
                   {
                       "Action": "os-upgrade",
                       "OptInStatus": "next-maintenance",
                       "CurrentApplyDate": "2026-09-02T03:02:00Z",
                       "Description": "New Operating System update is available"
                   }
               ]
           }
       ]
   }
   ```

1. Cancel the scheduled action by running the [apply-pending-maintenance-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/apply-pending-maintenance-action.html) CLI command with `--opt-in-type undo-opt-in`, passing the `Action` value from the previous step to `--apply-action`.

   For Linux, macOS, or Unix:

   ```
   aws docdb apply-pending-maintenance-action \
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}} \
      --apply-action {{os-upgrade}} \
      --opt-in-type undo-opt-in \
      --region {{us-east-1}}
   ```

   For Windows:

   ```
   aws docdb apply-pending-maintenance-action ^
      --resource-identifier {{arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15}} ^
      --apply-action {{os-upgrade}} ^
      --opt-in-type undo-opt-in ^
      --region {{us-east-1}}
   ```

   In the response, the maintenance action no longer has an `OptInStatus`, which confirms the scheduled opt-in was cancelled.

   ```
   {
       "ResourcePendingMaintenanceActions": {
           "ResourceIdentifier": "arn:aws:rds:us-east-1:001234567890:cluster:docdb-2025-03-27-19-21-15",
           "PendingMaintenanceActionDetails": [
               {
                   "Action": "os-upgrade",
                   "Description": "New Operating System update is available"
               }
           ]
       }
   }
   ```

------

------
#### [ Using the AWS CLI ]

1. Check for scheduled modifications by running the [describe-db-clusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-clusters.html) CLI command and inspecting the `PendingModifiedValues` output field.
**Note**  
Use the Amazon RDS CLI (`aws rds`) for this command, not the Amazon DocumentDB CLI (`aws docdb`), because the Amazon DocumentDB `describe-db-clusters` API doesn't return a cluster-level `PendingModifiedValues` field.

   In the following examples, replace each {{user input placeholder}} with your cluster's information.

   For Linux, macOS, or Unix:

   ```
   aws rds describe-db-clusters \
      --db-cluster-identifier {{docdb-2025-03-27-19-21-15}} \
      --query 'DBClusters[0].PendingModifiedValues' \
      --region {{us-east-1}}
   ```

   For Windows:

   ```
   aws rds describe-db-clusters ^
      --db-cluster-identifier {{docdb-2025-03-27-19-21-15}} ^
      --query "DBClusters[0].PendingModifiedValues" ^
      --region {{us-east-1}}
   ```

   The result shows the scheduled changes. In this example, a change to the cluster's name (`DBClusterIdentifier`) is pending, from `docdb-2025-03-27-19-21-15` to `docdb-new-name`.

   ```
   {
       "DBClusterIdentifier": "docdb-new-name"
   }
   ```

1. Revert the change by running the [modify-db-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster.html) CLI command with `--apply-immediately`, setting the modified value back to its original value. This example reverts the pending name change by setting `--new-db-cluster-identifier` back to the cluster's current name.

   For Linux, macOS, or Unix:

   ```
   aws docdb modify-db-cluster \
      --db-cluster-identifier {{docdb-2025-03-27-19-21-15}} \
      --new-db-cluster-identifier {{docdb-2025-03-27-19-21-15}} \
      --apply-immediately \
      --region {{us-east-1}}
   ```

   For Windows:

   ```
   aws docdb modify-db-cluster ^
      --db-cluster-identifier {{docdb-2025-03-27-19-21-15}} ^
      --new-db-cluster-identifier {{docdb-2025-03-27-19-21-15}} ^
      --apply-immediately ^
      --region {{us-east-1}}
   ```

------

## Managing RPOs for Amazon DocumentDB global clusters
<a name="global-clusters-manage-recovery"></a>

 With a Amazon DocumentDB global cluster, you can manage the recovery point objective (RPO) by using the `global_db_rpo` parameter. RPO represents the maximum amount of data that can be lost in the event of an outage. 

 When you set an RPO for your Amazon DocumentDB global cluster, Amazon DocumentDB monitors the *RPO lag time* of all secondary clusters. This monitoring ensures that at least one secondary cluster stays within the target RPO window. 

 The RPO setting controls how Amazon DocumentDB manages write transactions on the primary cluster to limit potential data loss if a failover occurs. Amazon DocumentDB evaluates RPO and RPO lag times to commit (or block) transactions on the primary as follows: 
+  Commits the transaction if at least one secondary DB cluster has an RPO lag time less than the RPO. 
+  Blocks the transaction if all secondary DB clusters have RPO lag times that are larger than the RPO. 

 In other words, if all secondary clusters are behind the target RPO, Amazon DocumentDB pauses transactions on the primary cluster. Amazon DocumentDB resumes and commits paused transactions as soon as the lag time of at least one secondary DB cluster drops below the RPO. The result is that no transactions can commit until the RPO is met. 

 The `global_db_rpo` parameter is dynamic. If you decide that you don't want all write transactions to stall until the lag decreases sufficiently, you can reset it quickly. In this case, Amazon DocumentDB applies the change after a short delay. 

**Important**  
 In a global database with only two AWS Regions, we recommend keeping the `global_db_rpo` parameter's default value in the secondary Region's parameter group. Otherwise, performing a failover due to a loss of the primary AWS Region could cause Amazon DocumentDB to pause transactions. Instead, wait until Amazon DocumentDB completes rebuilding the cluster in the old failed AWS Region before changing this parameter to enforce a maximum RPO. 

**Topics**
+ [Setting the recovery point objective](#global-clusters-set-rpo)
+ [Viewing the recovery point objective](#global-clusters-view-rpo)
+ [Disabling the recovery point objective](#global-clusters-disable-rpo)

### Setting the recovery point objective
<a name="global-clusters-set-rpo"></a>

 The `global_db_rpo` parameter controls the RPO setting for a Amazon DocumentDB database. Valid values range from 20 seconds to 2,147,483,647 seconds (68 years). Choose a realistic value to meet your business need. For example, you might want to allow up to 10 minutes for your RPO, in which case you set the value to 600. 

 You can set this value for your Amazon DocumentDB global cluster by using the AWS Management Console, the AWS CLI, or the Amazon DocumentDB API. 

------
#### [ Using the AWS Management Console ]

**To set the RPO**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1.  Choose the primary cluster of your Amazon DocumentDB global cluster and open the **Configuration** tab to find its DB cluster parameter group. 

    Parameter groups can't be edited directly. Instead, you do the following: 
   +  Create a custom DB cluster parameter group using the appropriate default parameter group as the starting point. 
   +  On your custom DB cluster parameter group, set the value of the **global\_db\_rpo** parameter to meet your use case. Valid values range from 20 seconds up to the maximum integer value of 2,147,483,647 (68 years). 
   +  Apply the modified DB cluster parameter group to your Amazon DocumentDB DB cluster. 

 For more information about modifying DB cluster parameter groups, see [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md). 

------
#### [ Using the AWS CLI ]

 To set the `global_db_rpo` parameter, use the [modify-db-cluster-parameter-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster-parameter-group.html) CLI command. In the command, specify the name of your primary cluster's parameter group and values for the RPO parameter. 

 The following example sets the RPO to 600 seconds (10 minutes) for the primary DB cluster's parameter group named `my_custom_global_parameter_group`. 

For Linux, macOS, or Unix:

```
aws docdb modify-db-cluster-parameter-group \
    --db-cluster-parameter-group-name {{my_custom_global_parameter_group}} \
    --parameters "ParameterName=global_db_rpo,ParameterValue={{600}},ApplyMethod=immediate"
```

For Windows:

```
aws docdb modify-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name {{my_custom_global_parameter_group}} ^
    --parameters "ParameterName=global_db_rpo,ParameterValue={{600}},ApplyMethod=immediate"
```

------
#### [ Using the Amazon DocumentDB API ]

 To modify the `global_db_rpo` parameter, use the [ModifyDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBClusterParameterGroup.html) API operation. 

------

### Viewing the recovery point objective
<a name="global-clusters-view-rpo"></a>

 The recovery point objective (RPO) of a global cluster is stored in the `global_db_rpo` parameter for each DB cluster. 

 You can use the CLI to view the `global_db_rpo` parameter for a Amazon DocumentDB DB cluster. Use the `--query` option to return only the `global_db_rpo` parameter from the parameter group. 

For Linux, macOS, or Unix:

```
aws docdb describe-db-cluster-parameters \
    --db-cluster-parameter-group-name {{my_custom_global_parameter_group}} \
    --query "Parameters[?ParameterName=='global_db_rpo']"
```

For Windows:

```
aws docdb describe-db-cluster-parameters ^
    --db-cluster-parameter-group-name {{my_custom_global_parameter_group}} ^
    --query "Parameters[?ParameterName=='global_db_rpo']"
```

 The command returns output similar to the following. 

```
[
    {
        "ParameterName": "global_db_rpo",
        "Description": "(s) Recovery point objective threshold, in seconds, that blocks user commits when it is violated.",
        "Source": "engine-default",
        "ApplyType": "dynamic",
        "DataType": "integer",
        "AllowedValues": "20-2147483647",
        "IsModifiable": true,
        "ApplyMethod": "immediate"
    }
]
```

 For more information about viewing parameters of the cluster parameter group, see [Managing Amazon DocumentDB cluster parameter groups](cluster_parameter_groups.md). 

### Disabling the recovery point objective
<a name="global-clusters-disable-rpo"></a>

 To disable the RPO, reset the `global_db_rpo` parameter. You can reset parameters using the AWS Management Console, the AWS CLI, or the Amazon DocumentDB API. 

------
#### [ Using the AWS Management Console ]

**To disable the RPO**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Parameter groups**.

1. In the list, choose your primary DB cluster parameter group.

1. Choose the radio button next to the **global\_db\_rpo** parameter.

1. Choose **Reset to default** and confirm it.

 For more information about how to reset a parameter with the console, see [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md). 

------
#### [ Using the AWS CLI ]

 To reset the `global_db_rpo` parameter, use the [reset-db-cluster-parameter-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/reset-db-cluster-parameter-group.html) command. 

For Linux, macOS, or Unix:

```
aws docdb reset-db-cluster-parameter-group \
    --db-cluster-parameter-group-name {{my_custom_global_parameter_group}} \
    --parameters "ParameterName=global_db_rpo,ApplyMethod=immediate"
```

For Windows:

```
aws docdb reset-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name {{my_custom_global_parameter_group}} ^
    --parameters "ParameterName=global_db_rpo,ApplyMethod=immediate"
```

------
#### [ Using the Amazon DocumentDB API ]

 To reset the `global_db_rpo` parameter, use the [ResetDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ResetDBClusterParameterGroup.html) API operation. 

------