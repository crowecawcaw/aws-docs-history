

# Amazon DocumentDB in-place major version upgrade
<a name="docdb-mvu"></a>

You can perform an in-place major version upgrade (MVU) of your Amazon DocumentDB cluster while keeping the same endpoints, storage, and tags. Your applications continue to work without modifications. This feature is available at no additional cost in all AWS Regions where Amazon DocumentDB is available.

**Important**  
Your cluster is unavailable during the upgrade and reboots multiple times. Do not connect to, read from, or write to the cluster after starting the upgrade. Downtime varies depending on the number of collections, indexes, databases, and instances. Perform the upgrade during your maintenance window or low-utilization hours.  
Once upgraded, you cannot downgrade to a previous version. You can restore your pre-upgrade snapshot to a new cluster if needed.

**Topics**
+ [Supported upgrade paths](#mvu-upgrade-paths)
+ [Prerequisites](#mvu-prerequisites)
+ [Best practices](#mvu-best-practices)
+ [What changes after upgrading to Amazon DocumentDB 8.0](#mvu-50-to-80-differences)
+ [Post-upgrade considerations for clusters upgraded from 3.6 or 4.0](#mvu-36-to-50-differences)
+ [Performing the upgrade](#perform-an-mvu)
+ [Troubleshooting](#mvu-troubleshooting)

## Supported upgrade paths
<a name="mvu-upgrade-paths"></a>

The following table lists every supported in-place major version upgrade path. You can select any published minor version on the target major as the target engine version.


| Source major version | Target major version | Notes | 
| --- | --- | --- | 
| Amazon DocumentDB 3.6 | Amazon DocumentDB 5.0 (any published minor version) | See [Post-upgrade considerations for clusters upgraded from 3.6 or 4.0](#mvu-36-to-50-differences) for post-upgrade considerations. | 
| Amazon DocumentDB 3.6 | Amazon DocumentDB 8.0 (any published minor version) | See [Post-upgrade considerations for clusters upgraded from 3.6 or 4.0](#mvu-36-to-50-differences) and [What changes after upgrading to Amazon DocumentDB 8.0](#mvu-50-to-80-differences) for post-upgrade considerations. | 
| Amazon DocumentDB 4.0 | Amazon DocumentDB 5.0 (any published minor version) | See [Post-upgrade considerations for clusters upgraded from 3.6 or 4.0](#mvu-36-to-50-differences) for post-upgrade considerations. | 
| Amazon DocumentDB 4.0 | Amazon DocumentDB 8.0 (any published minor version) | See [Post-upgrade considerations for clusters upgraded from 3.6 or 4.0](#mvu-36-to-50-differences) and [What changes after upgrading to Amazon DocumentDB 8.0](#mvu-50-to-80-differences) for post-upgrade considerations. | 
| Amazon DocumentDB 5.0 (any published minor version) | Amazon DocumentDB 8.0 (any published minor version) | See [What changes after upgrading to Amazon DocumentDB 8.0](#mvu-50-to-80-differences) for feature changes. | 

To view the minor versions available in your AWS Region, use the AWS CLI command `aws docdb describe-db-engine-versions`. For a list of released minor versions, see [Release notes](release-notes.md).

**Note**  
Each MVU can target any published minor version on the destination major. For example, upgrading from Amazon DocumentDB 3.6 or 4.0 can go directly to the latest published 5.0 or 8.0 minor version; there is no requirement to first upgrade to the `.0` minor version and then apply a minor version upgrade.  
You can upgrade from Amazon DocumentDB 3.6 or 4.0 directly to 8.0 in a single MVU. Upgrading in stages through 5.0 (first to a 5.0 minor version, then to an 8.0 minor version) is also supported.

**Note**  
In-place MVU is not supported for global clusters or elastic clusters. To upgrade a global cluster, remove the secondary clusters, convert the primary to a regional cluster, perform the MVU, then recreate the global cluster by adding secondary clusters using the same names to retain your endpoints. You will incur I/O charges while the upgraded primary replicates data to the new secondaries. For detailed steps, see [Removing a cluster from an Amazon DocumentDB global cluster](global-clusters.manage.md#global-clusters.remove).

## Prerequisites
<a name="mvu-prerequisites"></a>

**Important**  
**Scale up burstable instances before upgrading.** If your cluster uses burstable instance types (for example, `db.t3.medium` or `db.t4g.medium`), scale up the primary instance to at least `db.r5.large` or `db.r6g.large` before initiating the upgrade. Burstable instances may not have sufficient CPU and memory to complete the upgrade process, which can result in upgrade failures and extended cluster unavailability. You can scale back down after the upgrade completes.  
**Scale up the serverless writer instance before upgrading.** If your cluster has a serverless writer instance, the maximum DCU in the `ServerlessV2ScalingConfiguration` must be set to 3 or higher before initiating the upgrade. Clusters with a maximum DCU below 3 cannot be upgraded because they do not have sufficient CPU or memory to complete the upgrade.  
**Check your partial indexes before upgrading (upgrade from Amazon DocumentDB 5.0 to 8.0).** Before starting the upgrade, review your partial indexes for a `partialFilterExpression` that uses the `$type` operator to match certain BSON types: specifically the `binData`, `bool`, `date`, `double`, `decimal`, and `array` type aliases, or a numeric type code such as `{ "$type" : 1 }`. Such partial indexes cause the upgrade to fail, even though the index works normally for reads and writes. Use `db.collection.getIndexes()` to review the `partialFilterExpression` of your partial indexes. Drop the affected partial index before starting the upgrade and recreate it after the upgrade completes. If you are unsure whether an index is affected, contact AWS support before upgrading.
+ **Instance type** — Amazon DocumentDB 4.0\+ does not support db.r4 instances. Modify any `db.r4.*` instances to `db.r5.*` instances or newer before upgrading. See [Modifying an Amazon DocumentDB instance](db-instance-modify.md) and [Supported instance classes by Region](db-instance-classes.md#db-instance-classes-by-region).
+ **OS patches** — Apply any pending OS maintenance actions on all instances before upgrading. See [Amazon DocumentDB operating system updates](db-instance-maintain.md#os-system-updates).
**Note**  
Pending cluster-level engine patches may hide instance OS patches. Apply engine patches first if needed. See [Performing a patch update to a cluster's engine version](db-cluster-version-upgrade.md).
+ **Index limits on burstable instances (t-family instances)** — If you have more than 3,000 indexes on burstable instances, scale up the primary to at least db.r5.large before upgrading. You can scale back down after the upgrade completes.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/docdb-mvu.html)
+ **Parameter group** — Have a custom cluster parameter group for the target version ready before upgrading. If one is not specified, the default parameter group for the target version will be used (for example, `default.docdb5.0` or `default.docdb8.0`).
+ **Manual snapshot** — Create a manual snapshot before upgrading. The upgrade process creates an automatic snapshot named `preupgrade-<name>-<version>-<timestamp>`, but always create your own backup. See [Creating a manual cluster snapshot](backup_restore-create_manual_cluster_snapshot.md).
**Note**  
The auto snapshot created by the upgrade process will not be automatically deleted after the in-place major version upgrade has completed. This snapshot will not incur any charges as long as it is within the retention period. You can choose to delete this snapshot once you have verified a successful upgrade of your cluster.  
![Image: the Snapshots navigation box showing a table of previously created snapshots.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/mvu-snapshot-2.png)

## Best practices
<a name="mvu-best-practices"></a>

### Before upgrade — testing with a clone
<a name="test-in-place-mvu"></a>

1. Use [Cloning a volume for an Amazon DocumentDB cluster](db-cluster-cloning.md) to create a clone of your cluster. You will not incur storage costs unless you modify data on the clone.

1. Match the instance count of the clone to the target cluster for a realistic time estimate.

1. Perform the MVU on the clone and fully test for functional differences.

1. Check if an upgrade is already scheduled by running [`describe-db-clusters`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-clusters.html) and looking for `PendingModifiedValues.EngineVersion`. If you have modified the cluster and selected to apply it in the next maintenance window, the schedule will not be visible in the console but you can view it in the AWS CLI:

   ```
   aws docdb describe-db-clusters \
     --region {{us-east-1}} \
     --db-cluster-identifier {{mydocdbcluster}}
   ```

   ```
   "PendingModifiedValues": {
       "EngineVersion": "5.0.0"
   },
   ```

1. If testing is successful, proceed with the upgrade on your production cluster.

### During the upgrade
<a name="during-in-place-mvu"></a>

You can monitor progress of your in-place major version upgrade by subscribing to cluster maintenance events. When the upgrade completes, you will receive the "Database cluster major version has been upgraded" event. This and other events occurring during the upgrade appear in the **Events and Tags** section of the cluster detail page in the Amazon DocumentDB console. The cluster status then changes from `upgrading` to `available`.

The following events are generated during the upgrade:

1. Database cluster engine major version upgrade started. Cluster remains online.

1. Upgrade preparation in progress: Starting online upgrade prechecks.

1. Upgrade preparation in progress: Completed online upgrade prechecks.

1. Taking database cluster offline while the primary instance completes the patch/upgrade process.

1. Upgrade preparation in progress: Starting offline upgrade prechecks.

1. Upgrade preparation in progress: Completed offline upgrade prechecks.

1. Upgrade in progress: Creating pre-upgrade snapshot [preupgrade-<cluster-name>-<version-from>-to-<version-to>-<timestamp>].

1. Upgrade in progress: Cloning volume.

1. Upgrade in progress: Upgrading writer.

1. Upgrade in progress: Upgrading readers.

1. Database cluster engine major version has been upgraded.

Events are visible in the console under the **Events** page:

![Image: the Events navigation box showing a table of upgrade events.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/mvu-events-2.png)


From the AWS CLI, you can run [`aws docdb describe-events`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-events.html) to monitor upgrade progress. To receive notifications automatically, use [`aws docdb create-event-subscription`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-event-subscription.html) to subscribe to events and route them to Amazon SNS for email, push messages, or other delivery methods. For more information, see [Subscribing to Amazon DocumentDB events](event-subscriptions.subscribe.md).

```
aws docdb describe-events 
  --source-identifier {{mydocdbcluster}} 
  --source-type db-cluster
```

The command returns output similar to the following:

```
{
    "Events": [
        {
            "SourceIdentifier": "mydocdbcluster",
            "SourceType": "db-cluster",
            "Message": "Database cluster engine version upgrade started.",
            "EventCategories": [
                "maintenance"
            ],
            "Date": "2023-07-11T23:20:32.444000+00:00",
            "SourceArn": "arn:aws:rds:us-east-1:xxxx:cluster:mycluster"
        }
    ]
}
```

### After the upgrade
<a name="after-in-place-mvu"></a>

**Warning**  
Immediately after the in-place major version upgrade, your Amazon DocumentDB cluster repopulates index metadata that the database engine uses to optimize query execution plans. Query performance returns to expected levels once this process completes. It typically finishes in a few minutes but can take up to two hours depending on the number of indexes on your cluster.  
Do not reboot, failover, or scale up/down your writer instance during this time, as it may disrupt the index metadata recalculation. Wait until you observe expected query performance before making such changes.  
Track progress via the following cluster events:  
Post-upgrade cluster status: Index metadata refresh process started
Post-upgrade cluster status: Index metadata refresh process completed in X seconds
Contact AWS support if the index metadata refresh process hasn't completed within three hours, or if you continue to experience performance issues after the process completes.

1. **Take a manual snapshot** of the upgraded cluster in case you need to restore to the post-upgrade state. The automatic snapshot process will resume as soon as the in-place major version upgrade completes.

1. **Tag clusters upgraded from 3.6.** Add a tag to differentiate clusters upgraded from 3.6. (see [Post-upgrade considerations for clusters upgraded from 3.6 or 4.0](#mvu-36-to-50-differences)).

1. **Update your driver.** To use new features (for example, collation, views, or Zstd compression in 8.0), upgrade to the corresponding MongoDB API version. For more information, see [What's new in Amazon DocumentDB 8.0](compatibility.md#compatibility-whatsnew-8).

1. **Test thoroughly.** Validate your application against the upgraded cluster.

## What changes after upgrading to Amazon DocumentDB 8.0
<a name="mvu-50-to-80-differences"></a>

After performing a major version upgrade to Amazon DocumentDB 8.0 (from Amazon DocumentDB 5.0, or directly from 3.6 or 4.0), the following features are enabled or changed:
+ **Collation.** Amazon DocumentDB 8.0 supports [collation](collation.md). After the upgrade, new collections and their indexes, and new indexes on existing collections, have collation enabled by default.
+ **Text index.** New text indexes are created using Text Index V2, which uses an updated text search parser for improved MongoDB compatibility. Existing text indexes are not affected.
+ **Query planner version.** If you did not have a custom parameter group, a new default parameter group is created for Amazon DocumentDB 8.0 with Planner Version 3 automatically selected. With query planner version 3, [views](views.md) are also available.
+ **Compression.** Amazon DocumentDB 8.0 supports dictionary-based document compression using the Zstd algorithm. After the upgrade, new collections are created with Zstd compression enabled by default. Existing collections from 5.0 retain their compression settings. To take advantage of Zstd compression on existing collections, you can modify their compression settings. For more information, see [Managing dictionary-based compression in Amazon DocumentDB 8.0](dict-compression.md).
+ **Index rebuild.** If you are upgrading from Amazon DocumentDB 5.0 to Amazon DocumentDB 8.0, no index rebuild is needed. If you are upgrading directly from Amazon DocumentDB 3.6 or 4.0 to 8.0, rebuild your indexes as described in [Post-upgrade considerations for clusters upgraded from 3.6 or 4.0](#mvu-36-to-50-differences).

**Important**  
Amazon DocumentDB 8.0 requires TLS 1.2 or higher. TLS 1.0 and TLS 1.1 are no longer supported.

**Note**  
For a full list of functional differences, see [Amazon DocumentDB compatibility with MongoDB](compatibility.md).

## Post-upgrade considerations for clusters upgraded from 3.6 or 4.0
<a name="mvu-36-to-50-differences"></a>
+ **Index rebuild.** An MVU retains original indexes. Amazon DocumentDB 5.0 and later have improved index maintenance and garbage collection, especially for low-cardinality indexes. After upgrading from 3.6 or 4.0 (to either 5.0 or 8.0), rebuild your indexes to ensure optimal query performance (optional, involves additional I/O). See [Index maintenance using `reIndex`](managing-indexes.md#reIndex).
+ **Subdocument numeric comparison (3.6 only).** Clusters upgraded from 3.6 inherit the 3.6 behavior where numeric types in subdocuments are not compared across types. For example, `{a: {b: NumberLong(1)}}` does not equal `{a: {b: 1}}` in 3.6, but they are equal in 4.0 and later. This behavior affects any clusters upgraded from 3.6.

## Performing the upgrade
<a name="perform-an-mvu"></a>

------
#### [ Using the AWS Management Console ]

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/docdb/home?region=us-east-1) and open the Amazon DocumentDB console.

1. In the **Clusters** table, select the source cluster, choose **Actions**, and then **Modify**.  
![Image: the Clusters navigation box showing a list of existing cluster links and their corresponding instance links.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/mvu-cluster-table-2.png)

1. In **Cluster specifications**, choose the target version (for example, **5.0.0** or **8.0.0**) from the **Engine version** dropdown.  
![Image: the Cluster specifications section of the Modify cluster dialog box showing the Cluster indentifier and Engine version fields.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/mvu-modify-cluster-2.png)

1. In **Cluster options**, select your cluster parameter group for the target engine version. You can use the default (for example, **default.docdb5.0** or **default.docdb8.0**) or a custom parameter group you created.  
![Image: the Cluster options section of the Modify cluster dialog box showing the Cluster parameter group field.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/mvu-param-group-2.png)

1. Choose **Continue**, select your scheduling preference (apply immediately or next maintenance window), then choose **Modify cluster**.  
![Image: the Modify cluster dialog box showing the summary and scheduling of modification for the selected cluster.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/mvu-mod-schedule-2.png)

1. Monitor the cluster status in the clusters table as it changes to **upgrading**:  
![Image: the Clusters navigation box highlighting the Status column for the cluster being upgraded.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/mvu-cluster-upgrading-2.png)

------
#### [ Using the AWS CLI ]

Use [`modify-db-cluster`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster.html) with the `--allow-major-version-upgrade` flag:

```
aws docdb modify-db-cluster \
  ‐‐db-cluster-identifier {{mydocdbcluster}} \
  ‐‐allow-major-version-upgrade \
  ‐‐engine-version {{8.0.0}} \
  ‐‐apply-immediately \
  ‐‐cluster-parameter-group {{mydocdbparametergroup}} \
  ‐‐region {{us-east-1}}
```

Replace each {{placeholder}} with your cluster's information.

------

## Troubleshooting
<a name="mvu-troubleshooting"></a>
+ **Pre-upgrade check failure.** Before the upgrade begins, Amazon DocumentDB runs pre-upgrade validation checks. The following are common causes of pre-check failures:
  + **The upgrade could not proceed because collection(s) have names with 58 or more characters** — Rename the affected collections to shorter names before retrying the upgrade.
  + **The upgrade could not proceed because the index count exceeds the limit for the instance type** — Upgrade to a larger instance type before retrying the upgrade. For index limits by instance type, see [Prerequisites](#mvu-prerequisites).
+ **Upgrade failure and rollback.** If the upgrade fails, it automatically attempts a rollback. A successful rollback generates the event: "Database cluster is in a state that cannot be upgraded." Your cluster returns to its pre-upgrade state and you can continue using it. Contact AWS support to troubleshoot before re-attempting.
+ **Post-upgrade performance.** Temporary performance degradation and high CPU utilization may occur while the index metadata refresh runs. If degradation persists beyond 3 hours, contact AWS support.

For additional assistance, contact [AWS Support](https://aws.amazon.com/support).