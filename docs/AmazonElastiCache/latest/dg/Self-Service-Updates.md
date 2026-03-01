# Service updates in ElastiCache

ElastiCache automatically monitors your fleet of caches, clusters, and nodes to apply service
updates as they become available. Service updates for serverless caches are automatically
and transparently applied. For node-based clusters, you set up a predefined maintenance window.
Critical security updates will automatically be applied in these maintenance windows. All other
updates will be available via a self-service update.

With self-service updates, you control when and which updates are applied to your node-based clusters. You can also
monitor the progress of these updates to your selected ElastiCache cluster in real time.

###### Topics

- [Managing service updates for node-based clusters](#managing-updates "#managing-updates")

## Managing service updates for node-based clusters

ElastiCache service updates for node-based clusters are released on a regular basis. If you have one or more
qualifying node-based clusters for those service updates, you receive notifications through email,
SNS, the Personal Health Dashboard (PHD), and Amazon CloudWatch events when the updates are released. The updates are also
displayed on the **Service Updates** page on the ElastiCache console. By
using this dashboard, you can view all the service updates and their status for your
ElastiCache fleet. Service updates for serverless caches are transparently applied and cannot be managed via
**Service Updates**.

You control when to apply an update before an auto-update starts. There are three types of service updates:

- **security-update**: Includes the latest security patches. We strongly recommend that you apply security updates as soon as possible to ensure that your ElastiCache clusters are always up-to-date with the latest security patches.
- **engine-update**: Includes patches or minor engine version updates related to performance or stability optimizations for your current engine version.
- **engine-major-version-update**: Includes a major version or engine type change, typically due to your current engine version reaching its end of life. We recommend that you carefully review the version compatibility notes from the [Engine versions and upgrading in ElastiCache](engine-versions.md "engine-versions.md") before applying such updates.

The following sections explore these options in detail.

### Applying the service updates

You can start applying the service updates to your fleet from the time that
the updates have an **available** status. Service updates are cumulative. In other words, any
updates that you haven't applied yet are included with your latest update.

If a service update has auto-update enabled, you can choose to note any action when it
becomes available. ElastiCache will schedule to apply the update during one of your clusters' upcoming maintenance windows
after the **Auto-update start date**. You will receive related notifications for each stage of the update.

###### Note

You can apply only those service updates that have an
**available** or **scheduled** status.

For more information about reviewing and applying any
service-specific updates to applicable ElastiCache clusters, see [Applying the service updates using the console](#applying-updates-console-APIReferenceconsole "#applying-updates-console-APIReferenceconsole").

When a new service update is available for one or more of your ElastiCache clusters, you
can use the ElastiCache console, API, or AWS CLI to apply the update. The following sections
explain the options that you can use to apply updates.

#### Applying the service updates using the console

To view the list of available service updates, along with other information, go to the **Service Updates** page in the console.

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. On the navigation pane, choose **Service Updates**.
3. Under **Service updates** you can view the following:
   - **Service update name**: The unique name of the service update
   - **Update type**: The type of the service update, which is one of **security-update** or **engine-update**
   - **Update severity**: The priority of
     applying the update:
     - **critical:** We recommend
       that you apply this update immediately (within 14 days or
       less).
     - **important:** We recommend
       that you apply this update as soon as your business flow
       allows (within 30 days or less).
     - **medium:** We recommend that
       you apply this update as soon as you can (within 60 days or
       less).
     - **low:** We recommend that
       you apply this update as soon as you can (within 90 days or
       less).

   - **Engine version**: If the update type is engine-update, the engine version that is being updated.
   - **Release Date**: When the update is
     released and available to apply on your clusters.
   - **Recommended Apply By Date**: ElastiCache
     guidance date to apply the updates by.
   - **Status**: The status of the update,
     which is one of the following:
     - **available:** The update is
       available for requisite clusters.
     - **complete:** The update has
       been applied.
     - **cancelled:** The update has
       been canceled and is no longer necessary.
     - **expired:** The update is no
       longer available to apply.

4. Choose an individual update (not the button to its left) to view details of the service update.

In the **Cluster update status** section, you can view a list of clusters where the service update
has not been applied or has just been applied recently. For each cluster, you can view the following:

    * **Cluster name**: The name of the cluster
    * **Nodes updated:** The ratio of individual nodes within a specific cluster that were updated or remain available for the specific service update.
    * **Update Type**: The type of the service update, which is one of **security-update** or **engine-update**
    * **Status**: The status of the service update on the cluster, which is one of the following:




    	+ *available*: The update is available for the requisite cluster.
    	+ *in-progress*: The update is being applied to this cluster.
    	+ *scheduled*: The update date has been scheduled.
    	+ *complete*: The update has been successfully applied. Cluster with a complete status will be displayed for 7 days after its completion.
    If you chose any or all of the clusters with the **available** or **scheduled** status, and then chose **Apply now**, the update will start being applied on those clusters.

#### Applying the service updates using the AWS CLI

After you receive notification that service updates are available, you can
inspect and apply them using the AWS CLI:

- To retrieve a description of the service updates that are available,
  run the following command:

`aws elasticache describe-service-updates --service-update-status available`

For more information, see [describe-service-updates](../../../cli/latest/reference/elasticache/describe-service-updates.md "../../../cli/latest/reference/elasticache/describe-service-updates.md").

- To apply a service update on a list of clusters, run the following command:

`aws elasticache batch-apply-update-action --service-update ServiceUpdateNameToApply=sample-service-update --cluster-names cluster-1 cluster2`

For more information, see [batch-apply-update-action](../../../cli/latest/reference/elasticache/batch-apply-update-action.md "../../../cli/latest/reference/elasticache/batch-apply-update-action.md").

### Verifying you have the latest Service Update Applied using the AWS console

You can verify your ElastiCache for Redis OSS clusters are running the latest service update by following these steps:

1. Choose an applicable cluster on the **Redis OSS Clusters** page
2. Choose **Service updates** in the navigation pane to see the applicable service updates for
   that cluster, if any.

If the console displays a list of service updates, you can select the service update and choose
**Apply now**.

![Service updates console screenshot 1.](images/service-updates-1.png)

If the console displays “No service updates found”, it means the ElastiCache for Redis OSS cluster
already has the latest service update applied.

![Service updates console screenshot 2.](images/service-updates-2.png)

### Stopping the service updates

You can stop updates to clusters if needed. For example, you might want to
stop updates if you have an unexpected surge to your clusters that are
undergoing updates. Or you might want to stop updates if they're taking too long and
interrupting your business flow at a peak time.

The [Stopping](../APIReference/API_BatchStopUpdateAction.md "../APIReference/API_BatchStopUpdateAction.md") operation immediately interrupts all updates to those clusters
and any nodes that are yet to be updated. It continues to completion any nodes that
have an **in progress** status. However, it ceases updates to other
nodes in the same cluster that have an **update available** status
and reverts them to a **Stopping** status.

When the **Stopping** workflow is complete, the nodes that have a
**Stopping** status change to a **Stopped**
status. Depending on the workflow of the update, some clusters won't have any nodes
updated. Other clusters might include some nodes that are updated and others that
still have an **update available** status.

You can return later to finish the update process as your business flows permit.
In this case, choose the applicable clusters that you want to complete updates on,
and then choose **Apply Now**. For more information, see [Applying the service updates](#applying-updates "#applying-updates").

#### Using the console

You can interrupt a service update using the ElastiCache console. The following
demonstrates how to do this:

- After a service update has progressed on a selected cluster, the
  ElastiCache console displays the **View/Stop Update** tab at
  the top of the ElastiCache dashboard.
- To interrupt the update, choose **Stop
  Update**.
- When you stop the update, choose the cluster and examine the
  status. It reverts to a **Stopping** status and eventually a **Stopped** status.

#### Using the AWS CLI

You can interrupt a service update using the AWS CLI. The following code example
shows how to do this.

For a replication group, do the following:

`aws elasticache batch-stop-update-action --service-update-name
 `sample-service-update`--replication-group-ids
`my-replication-group-1
my-replication-group-2``

For a cluster, do the following:

`aws elasticache batch-stop-update-action --service-update-name
 `sample-service-update`--cache-cluster-ids
`my-cache-cluster-1
my-cache-cluster-2``

For more information, see [BatchStopUpdateAction](../APIReference/API_BatchStopUpdateAction.md "../APIReference/API_BatchStopUpdateAction.md").
