# Applying the service updates

You can start applying the service updates to your fleet from the time that
the updates have an **available** status. Service updates are cumulative. In other words, any
updates that you haven't applied yet are included with your latest update.

If a service update has auto-update enabled, you can choose to not take any action when it
becomes available. MemoryDB will schedule to apply the update during your clusters' maintenance window
after the **Auto-update start date**. You will receive related notifications for each stage of the update.

###### Note

You can apply only those service updates that have an
**available** or **scheduled** status.

For more information about reviewing and applying any
service-specific updates to applicable MemoryDB clusters, see [Applying the
service updates using the console](#applying-updates-console-APIReferenceconsole "#applying-updates-console-APIReferenceconsole").

When a new service update is available for one or more of your MemoryDB clusters, you
can use the MemoryDB console, API, or AWS CLI to apply the update. The following sections
explain the options that you can use to apply updates.

## Applying the

service updates using the console

To view the list of available service updates, along with other information, go to the **Service Updates** page in the console.

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. On the navigation pane, choose **Service Updates**.

Under **Service update details** you can view the following:

- **Service update name**: The unique name of the service update
- **Update description**: Detailed information about the service update
- **Auto-update start date**: If this attribute is set, MemoryDB will start scheduling your clusters to be
  auto-updated in the appropriate maintenance windows after this date.
  You will receive notifications in advance on the exact scheduled maintenance window, which might not be the immediate one
  after the **Auto-update start date**. You can still apply the update to your clusters any time you choose.
  If the attribute is not set, the service update is not auto-update enabled and MemoryDB will not update your clusters automatically.

In the **Cluster update status** section, you can view a list of clusters where the service update
has not been applied or has just been applied recently. For each cluster, you can view the following:

- **Cluster name**: The name of the cluster
- **Nodes updated:** The ratio of individual nodes within a specific cluster that were updated or remain available for the specific service update.
- **Update Type**: The type of the service update, which is one of **security-update** or **engine-update**
- **Status**: The status of the service update on the cluster, which is one of the following:

      + *available*: The update is available for the requisite cluster.
      + *in-progres*: The update is being applied to this cluster.
      + *scheduled*: The update date has been scheduled.
      + *complete*: The update has been successfully applied. Cluster with a complete status will be displayed for 7 days after its completion.

  If you chose any or all of the clusters with the **available** or **scheduled** status, and then chose **Apply now**, the update will start being applied on those clusters.
