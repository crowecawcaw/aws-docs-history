

# Setting up A/B video watermarking
<a name="ab-watermark-configure"></a>

Before you begin, complete the [A/B watermarking prerequisites](feature-ab-watermark.md#ab-watermark-prerequisites). This section assumes that you are familiar with creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md), and that you have already set up the video encodes in a supported output group.

**To set up A/B video watermarking**

1. On the **Create channel** page of the MediaLive console, choose the CMAF Ingest or MediaPackage v2 output group.

1. In the output group settings, expand the **Watermarking** section. For **Watermarker**, choose **Irdeto AB Watermarker**. The watermarking settings apply to all outputs in the output group.

1. Complete the watermarking fields as described in the following table.


**A/B watermarking fields**  

<table>
<thead>
  <tr><th>Area</th><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Watermarking</b></td><td><b>Watermarker</b></td><td>Choose <b>Irdeto AB Watermarker</b> to enable A/B forensic video watermarking for all video encodes in this output group.</td></tr>
  <tr><td><b>Watermarking</b></td><td><b>License</b></td><td>Enter the name of the AWS Secrets Manager secret that contains the Irdeto license file.</td></tr>
  <tr><td><b>Watermarking</b></td><td><b>Operator Id</b></td><td>Enter the vendor-provided operator ID.</td></tr>
  <tr><td><b>Watermarking</b></td><td><b>A/B Watermarking Profile</b></td><td>Choose <b>Default</b>, <b>Mezzanine</b>, <b>HQ</b>, <b>Robust</b>, <b>Camcording</b>, or <b>Custom</b>. If you choose <b>Custom</b>, complete the custom profile fields described below.</td></tr>
  <tr><td><b>Watermarking</b></td><td><b>Poly Period</b></td><td>Enter a value from 1 through 1000. This number is the number of segments per watermarking bit. The total duration of the watermarking bit should be the LCM (least common multiple) of all segment sizes emitted by the downstream packager.</td></tr>
  <tr><td><b>Watermarking</b></td><td><b>Watermark ID Length</b></td><td>Choose <b>512</b> (default) or <b>2048</b>. This value is the number of bits that compose the embedded watermark identifier. The value must match the license.</td></tr>
  <tr><td><b>Watermarking</b></td><td><b>Alternate Destination - Pipeline 0</b></td><td>Configure the B-variant alternate destination for pipeline 0. For CMAF Ingest output groups, enter the destination URL. For MediaPackage v2 output groups, select the region, channel group name, channel name, and endpoint ID. The output group's regular A destination carries the A variant; the B alternate destination carries the corresponding B variant.</td></tr>
  <tr><td><b>Watermarking</b></td><td><b>Alternate Destination - Pipeline 1</b></td><td>Configure the B-variant alternate destination for pipeline 1 using the same field type as pipeline 0. This field appears only on standard (two-pipeline) channels.</td></tr>
</tbody>
</table>


   If you chose **Custom** for the profile, complete the following fields.


**Custom profile fields**  

<table>
<thead>
  <tr><th>Area</th><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Custom profile</b></td><td><b>Scene Cut</b></td><td>Controls the number of frames after a scene cut during which the watermarker embeds a mark. Higher values increase robustness around scene changes at a potential quality cost.</td></tr>
  <tr><td><b>Custom profile</b></td><td><b>Target PSNR</b></td><td>Controls the target peak signal-to-noise ratio. Higher values produce less-visible watermarks but might reduce detection reliability. Lower values increase detection robustness at a potential quality cost.</td></tr>
  <tr><td><b>Custom profile</b></td><td><b>Embedding Frequency</b></td><td>Enter the maximum interval, in milliseconds, between watermark embeddings.</td></tr>
</tbody>
</table>


   If the output group has an additional destination, it also gets a paired B alternate destination. MediaLive currently supports at most one additional A/B destination pair. Complete the following fields for the additional destination.
   + **Additional Destinations Alternate Destinations - Pipeline 0** — Configure the B-variant alternate for pipeline 0 of the additional destination. For CMAF Ingest, enter a URL. For MediaPackage v2, select the structured destination fields.
   + **Additional Destinations Alternate Destinations - Pipeline 1** — Configure the B-variant alternate for pipeline 1 of the additional destination. This field appears only on standard (two-pipeline) channels.
**Note**  
**Destination model:** The output group's regular A destinations carry the A watermark variant. Each corresponding paired B alternate destination carries the B variant. Standard channels have two pipelines, so each destination role has a Pipeline 0 and a Pipeline 1 field. Single-pipeline channels have only Pipeline 0. Configure each B alternate destination as a distinct endpoint. The B alternate destinations for the regular and additional destinations must be different from each other.

1. Set the channel to use epoch locking. In the navigation pane, choose **General settings**, then choose **Global configuration**. Choose **Enable global configuration**, and for **Output locking mode**, choose **EPOCH\_LOCKING**. For more information, see [Configuring output locking and setting the mode](pipeline-locking-set-up.md#pipeline-locking-mode).