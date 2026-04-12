# Setting up event clipping

You can set up event clipping in a new MediaLive channel that you are creating. Or you can
update an existing channel to include event clipping . You can set up event clipping and
other Elemental Inference features at the same time, in either a new channel or an existing channel.

This section describes how to set up event clipping using the MediaLive console. For
information about setting up using an AWS API, see [Elemental Inference features using AWS CLI](elemental-inference-cli.md "elemental-inference-cli.md").

###### Note

The information in this section assumes that you are familiar with the general
steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

You must enable event clipping in the channel.

1. If you plan to update an existing feed, make sure that you have room in the
   [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas") for Elemental Inference. The list of quotas is sorted
   alphabetically. Look for quotas that don't start with "Request rate for".

Keep in mind that each feature that you enable in a channel results in one
Elemental Inference output. 2. On the **Create channel** or **Edit channel
page**, choose **AWS Elemental Inference
settings**. Complete the fields as follows:

    * In **State**, choose **Enabled**.
     Sections for each Elemental Inference feature appear.
    * Expand the **Clip events** section. In
     **State**, choose **Enabled**.
    * In **Callback config**, you can enter a string that
     you want Elemental Inference to always include in the event clipping metadata for
     this output. This information is useful when you later work with Elemental Inference
     events in EventBridge. You will be able to filter events using this
     information, in order to find the events for one feed. The string might
     identify the sports event in the feed, for example.

3.  Save the channel. MediaLive calls the Elemental Inference `AssociateFeed` endpoint
    to perform these actions:

        * To create an event clipping output in the feed.
        * To associate the channel (the resource) with the feed, if this is the
         first Elemental Inference feature that you are setting up.

    You now have a usable feed: resource - feed - output.

You can start the channel. When the channel is running, MediaLive delivers the
source stream to Elemental Inference and then retrieves metadata from Elemental Inference. This metadata
provides information that you use to crop and scale the video. You use a
third-party solution to transform the video. (MediaLive can't crop the video.) For
more information, see [Creating an Elemental Inference workflow](../../../elemental-inference/latest/userguide/elemental-inference-configuration.md "../../../elemental-inference/latest/userguide/elemental-inference-configuration.md") in the _AWS Elemental Inference user
guide_.
