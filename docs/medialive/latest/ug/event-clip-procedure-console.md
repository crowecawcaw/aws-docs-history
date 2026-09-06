# Setting up event clipping

You can set up event clipping in a new MediaLive channel that you are creating. Or you can
update an existing channel to include event clipping . You can set up event clipping and
other Elemental Inference features at the same time, in either a new channel or an existing channel.

This section describes how to set up event clipping using the MediaLive console. For
information about setting up using an AWS API, see [Elemental Inference features using AWS CLI](elemental-inference-cli.md "elemental-inference-cli.md").

###### Note

The information in this section assumes that you are familiar with the general
steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

To use event clipping, the Elemental Inference feed associated with your channel must have a
clipping output configured. You manage feed outputs in the Elemental Inference console.

1. In the Elemental Inference console, create or update your feed to include a clipping
   output. (Optional) Configure callback metadata on the output. For more
   information, see [Creating an Elemental Inference workflow](../../../elemental-inference/latest/userguide/elemental-inference-configuration.md "../../../elemental-inference/latest/userguide/elemental-inference-configuration.md") in the _AWS Elemental Inference user
   guide_.
2. On the MediaLive **Create channel** or **Edit channel** page, navigate to the **Elemental Inference settings** section.
3. For **Elemental Inference feed**, select the feed that
   contains the clipping output. If you created or updated the feed, choose
   **Refresh** to see it in the list.
4. Under **Event clipping**, verify that the clipping output
   from the feed is detected. The section displays a status indicator when the
   feed includes a clipping output.
5. Save the channel. When the channel is running, MediaLive delivers the source
   stream to Elemental Inference and retrieves metadata from Elemental Inference. You can then use Elemental Inference
   APIs or EventBridge rules to trigger event clips.
