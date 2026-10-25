

# Setting up with the MediaLive console
<a name="functions-medialive-console"></a>

1. In Elemental Inference, create the function, then create the feed with the function output and the access role. See [Creating a function](functions-create.md) and [Attaching a function to a feed](functions-attach.md). Make a note of the feed ARN, and leave the feed unassociated – a feed can be associated with only one resource.

1. In MediaLive, on the **Create channel** or **Edit channel** page, open **AWS Elemental Inference settings** and set **State** to **Enabled**.

1. Choose to select an existing feed, or to enter a feed ARN, and specify the feed that you created.
**Important**  
Don't let MediaLive create a new feed. A feed that MediaLive creates has neither your function output nor an access role.

1. If the function reads `media.transcript`, the feed needs audio. In the **Elemental Inference feed** section, for **Audio selector name**, choose the channel audio selector to send to the feed. The console selects the channel's first audio selector by default.

1. Save the channel. MediaLive associates the channel with the feed.

1. Start the channel. Media flows to Elemental Inference, and the function starts running on its trigger.

**Note**  
After a channel is saved with a feed, the feed selection is read-only. To use a different feed, disable the Elemental Inference settings, save the channel, then edit the channel again and select the new feed.