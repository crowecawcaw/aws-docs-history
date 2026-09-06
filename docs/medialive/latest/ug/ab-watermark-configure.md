# Setting up A/B video watermarking

Before you begin, complete the [A/B
watermarking prerequisites](feature-ab-watermark.md#ab-watermark-prerequisites "feature-ab-watermark.md#ab-watermark-prerequisites"). This section assumes that you are familiar with
creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md"), and
that you have already set up the video encodes in a supported output group.

###### To set up A/B video watermarking

1. On the **Create channel** page of the MediaLive console, choose
   the CMAF Ingest or MediaPackage v2 output group.
2. In the output group settings, expand the **Watermarking**
   section. For **Watermarker**, choose
   **Irdeto AB Watermarker**. The watermarking settings apply
   to all outputs in the output group.
3. Complete the watermarking fields as described in the following
   table.

A/B watermarking fields| Area | Field | Description |
| --- | --- | --- |
| **Watermarking** | **Watermarker** | Choose *_Irdeto AB Watermarker_<br>• to enable<br>A/B forensic video watermarking for all video encodes in this<br>output group. |
| **Watermarking** | **License** | Enter the name of the AWS Secrets Manager secret that contains<br>the Irdeto license file. |
| **Watermarking** | **Operator Id** | Enter the vendor-provided operator ID. |
| **Watermarking** | **A/B Watermarking Profile** | Choose **Default**,<br>**Mezzanine**,<br>**HQ**,<br>**Robust**,<br>**Camcording**, or<br>**Custom**. If you choose<br>**Custom**, complete the custom profile<br>fields described below. |
| **Watermarking** | **Poly Period** | Enter a value from 1 through 1000. This number is the number<br>of segments per watermarking bit. The total duration of the<br>watermarking bit should be the LCM (least common multiple) of all<br>segment sizes emitted by the downstream packager. |
| **Watermarking** | **Watermark ID Length** | Choose *_512_<br>• (default) or<br>**2048**. This value is the number of<br>bits that compose the embedded watermark identifier. The value<br>must match the license. |
| **Watermarking** | **Alternate Destination<br>• Pipeline<br>0** | Configure the B-variant alternate destination for<br>pipeline 0. For CMAF Ingest output groups, enter the<br>destination URL. For MediaPackage v2 output groups, select<br>the region, channel group name, channel name, and endpoint<br>ID. The output group's regular A destination carries the A<br>variant; the B alternate destination carries the<br>corresponding B variant. |
| **Watermarking** | **Alternate Destination<br>• Pipeline<br>1** | Configure the B-variant alternate destination for<br>pipeline 1 using the same field type as pipeline 0. This<br>field appears only on standard (two-pipeline)<br>channels. |

If you chose **Custom** for the profile, complete the
following fields.

Custom profile fields| Area | Field | Description |
| --- | --- | --- |
| **Custom profile** | **Scene Cut** | Controls the number of frames after a scene cut during<br>which the watermarker embeds a mark. Higher values increase<br>robustness around scene changes at a potential quality<br>cost. |
| **Custom profile** | **Target PSNR** | Controls the target peak signal-to-noise ratio. Higher<br>values produce less-visible watermarks but might reduce<br>detection reliability. Lower values increase detection<br>robustness at a potential quality cost. |
| **Custom profile** | **Embedding Frequency** | Enter the maximum interval, in milliseconds, between<br>watermark embeddings. |

If the output group has an additional destination, it also gets a paired B
alternate destination. MediaLive currently supports at most one additional A/B
destination pair. Complete the following fields for the additional
destination.

    * **Additional Destinations Alternate Destinations - Pipeline
     0** — Configure the B-variant alternate for pipeline 0
     of the additional destination. For CMAF Ingest, enter a URL. For
     MediaPackage v2, select the structured destination fields.
    * **Additional Destinations Alternate Destinations - Pipeline
     1** — Configure the B-variant alternate for pipeline 1
     of the additional destination. This field appears only on standard
     (two-pipeline) channels.

###### Note

**Destination model:** The output group's
regular A destinations carry the A watermark variant. Each corresponding
paired B alternate destination carries the B variant. Standard channels
have two pipelines, so each destination role has a Pipeline 0 and a
Pipeline 1 field. Single-pipeline channels have only Pipeline 0. Configure
each B alternate destination as a distinct endpoint. The B alternate
destinations for the regular and additional destinations must be different
from each other. 4. Set the channel to use epoch locking. In the navigation pane, choose
**General settings**, then choose **Global
configuration**. Choose **Enable global
configuration**, and for **Output locking mode**,
choose **EPOCH\_LOCKING**. For more information, see [Configuring output locking and setting the mode](pipeline-locking-set-up.md#pipeline-locking-mode "pipeline-locking-set-up.md#pipeline-locking-mode").
