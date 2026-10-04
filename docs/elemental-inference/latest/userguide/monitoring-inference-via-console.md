

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

## Monitoring tab
<a name="monitor-console-monitoring-tab"></a>

The **Monitoring** tab is the first tab on the feed details page.

Until the feed has an association, it is not active. While the feed is not active, the **Monitoring** tab shows a message that prompts you to add an association so that you can monitor the feed.

To add an association from the feed details page, choose **Add association**.

When the feed is active or archived, the **Monitoring** tab shows the **Feed dashboard**. The dashboard is a set of Amazon CloudWatch graphs that show live data for the feed:
+ **PutMedia request count**
+ **PutMedia request latency**
+ **GetMetadata request latency**
+ **Feature processing latency** – One graph, with a line for each feature (event clipping, smart cropping, smart subtitling, and contextual metadata)

## Feed outputs tab
<a name="monitor-console-feed-outputs"></a>

In this tab, one panel appears for each feature that you have enabled in the channel. Each panel includes the following information:
+ The output status. For more information about status, see [Lifecycle of an AWS Elemental Inference workflow](monitor-inference-feed-lifecycle.md).
+ From association: A value of true means that the output was created using the `AssociateFeed` operation. 

  If your organization uses AWS Elemental MediaLive to set up Elemental Inference features in a channel, a value of true indicates that you used MediaLive to create the feed and the output.

### Preview metadata
<a name="monitor-console-preview-metadata"></a>

Each output card on the **Feed outputs** tab includes an expandable **Preview metadata** section. This section shows the metadata that the output has recently produced. Preview is available for smart cropping, event clipping, smart subtitling, and contextual metadata outputs.

The feed must be active to preview metadata. While the feed is not active, the console shows the message *Feed must be active to preview metadata.*

By default, the preview reads a window of the most recent metadata, just behind the live edge. To set how far back to read, choose a **Time range**: **Last 10 seconds** (the default), **Last 20 seconds**, or **Last 30 seconds**.

To read from a specific point on the media timeline instead, turn on **Use a fixed start PTS**. PTS (presentation timestamp) is the media-timeline position that metadata is stamped with. For more information, choose **What is PTS?** in the console. For example, use this option for video-on-demand content that starts near PTS 0. Enter a **Start PTS** value in timescale units. The window length control then changes to **Duration**.

You can also set the following options:
+ **Input** – The feed input to read from (0 or 1).
+ **Timescale** – The number of timescale units (ticks) per second used for PTS values. The default is 90000.

To load the metadata, choose **Apply**. Results appear as a **Table** or as **JSON**. The columns that appear depend on the output type.