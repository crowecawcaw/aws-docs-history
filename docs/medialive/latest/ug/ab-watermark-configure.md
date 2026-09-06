

# Setting up A/B video watermarking
<a name="ab-watermark-configure"></a>

Before you begin, complete the [A/B watermarking prerequisites](feature-ab-watermark.md#ab-watermark-prerequisites). This section assumes that you are familiar with creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md), and that you have already set up the video encodes in a supported output group.

**To set up A/B video watermarking**

1. On the **Create channel** page of the MediaLive console, choose the CMAF Ingest or MediaPackage v2 output group.

1. In the output group settings, expand the **Watermarking** section. For **Watermarker**, choose **Irdeto AB Watermarker**. The watermarking settings apply to all outputs in the output group.

1. Complete the watermarking fields as described in the following table.  
**A/B watermarking fields**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/ab-watermark-configure.html)

   If you chose **Custom** for the profile, complete the following fields.  
**Custom profile fields**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/ab-watermark-configure.html)

   If the output group has an additional destination, it also gets a paired B alternate destination. MediaLive currently supports at most one additional A/B destination pair. Complete the following fields for the additional destination.
   + **Additional Destinations Alternate Destinations - Pipeline 0** — Configure the B-variant alternate for pipeline 0 of the additional destination. For CMAF Ingest, enter a URL. For MediaPackage v2, select the structured destination fields.
   + **Additional Destinations Alternate Destinations - Pipeline 1** — Configure the B-variant alternate for pipeline 1 of the additional destination. This field appears only on standard (two-pipeline) channels.
**Note**  
**Destination model:** The output group's regular A destinations carry the A watermark variant. Each corresponding paired B alternate destination carries the B variant. Standard channels have two pipelines, so each destination role has a Pipeline 0 and a Pipeline 1 field. Single-pipeline channels have only Pipeline 0. Configure each B alternate destination as a distinct endpoint. The B alternate destinations for the regular and additional destinations must be different from each other.

1. Set the channel to use epoch locking. In the navigation pane, choose **General settings**, then choose **Global configuration**. Choose **Enable global configuration**, and for **Output locking mode**, choose **EPOCH\_LOCKING**. For more information, see [Configuring output locking and setting the mode](pipeline-locking-set-up.md#pipeline-locking-mode).