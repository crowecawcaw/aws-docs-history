

# Resetting channel history in AWS Elemental MediaPackage
<a name="channel-reset"></a>

These steps show how to reset a channel in MediaPackage. Resetting the channel history clears out previously ingested content from the channel. For information about when you might want to reset, see [Reset for AWS Elemental MediaPackage channels and endpoints](resetting.md).

You can use the MediaPackage console, MediaPackage API, or AWS CLI to edit a channel. This guide shows how to reset channel history using the MediaPackage console.

**To reset a channel (console)**

1. Stop the encoder. If you don't stop the encoder, all endpoints for the MediaPackage channel will stop working.

   In AWS Elemental MediaLive, stop the channel as described in [Starting, stopping, and pausing a channel](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html) in the MediaLive user guide.

1. In MediaPackage, access the channel group that the channel is associated with, as described in [Viewing channel group details in AWS Elemental MediaPackage](channel-group-view.md).

1. From the **Channels** list, select the channel that you want to reset and choose **Reset history**. 

1. Wait at least 30 seconds after MediaPackage channel reset to complete, then restart the encoder. 

   Refreshed content will then be available from the channel's endpoint. 