

# Lifecycle of an AWS Elemental Inference workflow
<a name="monitor-inference-feed-lifecycle"></a>

When you use Elemental Inference, you create a feed, include one or more outputs, and associate a resource. Each output represents one Elemental Inference feature, such as smart crop. Each resource represents the source media that works with the feed.

## Lifecycle and status of a feed
<a name="monitor-inference-feed-status"></a>

The typical lifecycle of a feed is as follows:

CREATING -> AVAILABLE -> ACTIVE -> ARCHIVED -> DELETING -> DELETED

All of these statuses are one-way. Most importantly, you can't unarchive a feed. Typically the status changes as follows:
+ CREATING to AVAILABLE. This is always the initial transtion. 

  AVAILABLE means that the feed doesn't have a resource associated with it.
+ AVAILABLE to ACTIVE. After you associate the resource, the feed becomes ACTIVE. 

  ACTIVE means that you can stream media to the feed, using `PutMedia`.

  ACTIVE doesn't mean that you've called PutMedia and the feed is processing the media. Elemental Inference doesn't monitor streaming because each PutMedia call occurs in milliseconds, which means it is impossible to track in a meaningful way.
+ ACTIVE to ARCHIVED. When you no longer need the feed, you can archive it in one of these ways:
  + On the console, display the feed details and choose **Archive**. 
  + On the CLI, use the `DisassociateFeed` operation, which indirectly sets the status to ARCHIVED.

  When the feed is ARCHIVED, you can't use it any more. Your quota for feeds decreases by 1.
+ When you are ready, delete the feed. The feed will disappear from the array of lists, so you won't actually see it with a DELETED status.

## Status of a resource
<a name="monitor-inference-status-resource"></a>

A resource doesn't have a status. Keep in mind that the resource is really just a way of identifying that the feed is intended for a specific source media.

## Status of an output
<a name="monitor-inference-status-output"></a>

Related to the feed status, the output also has a status:
+ ENABLED means that Elemental Inference will generate metadata for the output when it is processing the source media. 
+ DISABLED means that it won't generate new metadata.

If you create an output using the console, its initial status is ENABLED. If you create it using the CLI, you choose the initial status.

You can change the output status when a feed is any of the statuses before ARCHIVED. You can change the status at any time, including when the source media is being streamed to the feed (in other words, you've called PutMedia).

You can't change the status of the output after the feed is ARCHIVED. There is never any need to do this.

## Lifecycle of metadata
<a name="monitor-inference-metadata-lifecycle"></a>

Elemental Inference produces metadata for a feature type (for example, smart crop) when media is being streamed to the feed and the output for that feature is ENABLED.

Elemental Inference retains metadata for 7 days, for both ENABLED and DISABLED outputs.

It continually discards data that is older than 7 days, for both ENABLED and DISABLED outputs.