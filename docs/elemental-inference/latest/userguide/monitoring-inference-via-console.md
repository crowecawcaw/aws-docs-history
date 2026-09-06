

# Monitoring AWS Elemental Inference on the console
<a name="monitoring-inference-via-console"></a>

You can monitor a feed using the Elemental Inference console.

1. On the Elemental Inference console, in the navigation pane, choose **Feeds**.

1. The **Feeds** page shows a list of your feeds. Each line in the list provides basic information about the feed, including its status. For information about statuses, see [Lifecycle of an AWS Elemental Inference workflow](monitor-inference-feed-lifecycle.md).

1. To view more details about a feed, choose the name of that feed. The **Feed details** page appears. Information appears, as described in the following sections.

## General details panel and feed association panel
<a name="monitor-console-gen-details"></a>

**Feed ID**

The ID of the Elemental Inference feed. The ID is identical to the last portion of the ARN of the feed. 

**ARN**

The ARN of the feed.

**Status of the feed**

These statuses are listed in lifetime order, from **CREATING** to **ARCHIVED**. Note the following:
+ A newly created feed typically transitions immediately from **CREATING** to **AVAILABLE** to **ACTIVE**. **ACTIVE** means that the feed is associated with its resource.
+ When Elemental Inference deletes a feed, its status changes to **DELETED**, then after a short period, it changes to **ARCHIVED**. There is no way to change the status of a feed that is **DELETED** or **ARCHIVED**. 

## Feed outputs tab
<a name="monitor-console-feed-outputs"></a>

In this tab, one panel appears for each feature that you have enabled in the channel. Each panel includes the following information:
+ The output status. For more information about status, see [Lifecycle of an AWS Elemental Inference workflow](monitor-inference-feed-lifecycle.md).
+ From association: A value of true means that the output was created using the `AssociateFeed` operation. 

  If your organization uses AWS Elemental MediaLive to set up Elemental Inference features in a channel, a value of true indicates that you used MediaLive to create the feed and the output.

### Preview metadata for smart crop
<a name="monitor-console-preview-smart-crop"></a>

This output tab also includes a viewer for historical smart cropping metadata. To retrieve metadata:

### Preview metadata for event clipping
<a name="monitor-console-preview-event-clip"></a>

This output tab also includes a viewer for historical event clipping metadata. 

