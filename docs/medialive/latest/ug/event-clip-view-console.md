

# Viewing the event clipping setup
<a name="event-clip-view-console"></a>

You can view information about the Elemental Inference features in a channel. 

**Note**  
This section describes how to set up view event clipping information using the MediaLive console. To view information using an AWS API, use the `GetFeed` operation. For more information, see [ GetFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFeed) in the *AWS Elemental Inference API Reference*. 

You can view information about the Elemental Inference features in a channel. You can view information on the MediaLive console or the Elemental Inference console. 

## Viewing the setup on the MediaLive console
<a name="event-clip-eml-console-view"></a>

On the MediaLive console, in the left navigation bar, choose **Channels**, then choose the channel to view. In the tabs in the middle of the page, choose **AWS Elemental Inference**. Information appears, including the following:

**ID and ARN**

The ID and ARN of the Elemental Inference feed that is associated with the channel. 

The ID is identical to the last portion of the ARN of the feed. If you are interested in working with the feed using Elemental Inference directly, make a note of the ARN.

**Status of the feed**

These statuses are listed in lifetime order, from **CREATING** to **ARCHIVED**. Note the following:
+ A newly created feed typically transitions immediately from **CREATING** to **AVAILABLE** to **ACTIVE**. **ACTIVE** means that the feed is associated with the channel.
+ When MediaLive deletes a feed, its status changes to **DELETED**, then after a short period, it changes to **ARCHIVED**. There is no way to change the status of a feed that is **DELETED** or **ARCHIVED**. If you re-enable Elemental Inference features in a channel, MediaLive will create a new feed that has a new ID.

**Feature panels**

One panel appears for each Elemental Inference feature that you have enabled in the channel. Each panel includes the following information:
+ The type of feature.
+ The status of the feature, which will always be **ENABLED**. (If you disable the feature, the entire panel disappears, so you won't see **DISABLED**.)
+ Settings, which shows the value in the callback field.

## Viewing the setup using the Elemental Inference CLI
<a name="event-clip-inference-view-cli"></a>

To view information using an AWS API, use the `GetFeed` operation of Elemental Inference. For more information, see [ GetFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFeed) in the *AWS Elemental Inference API Reference*. 