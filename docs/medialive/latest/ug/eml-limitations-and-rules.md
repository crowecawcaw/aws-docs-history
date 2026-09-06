

# MediaLive feature rules and limits
<a name="eml-limitations-and-rules"></a>

The following table provides a summary of many of the rules and constraints that apply to AWS Elemental MediaLive features. You can't change any of these constraints. 

MediaLive also includes quotas, which you can change. For more information about quotas, see [Quotas in MediaLive](limits.md). 

**Topics**
+ [Limits for inputs](#limits-inputs)
+ [Limits for outputs](#limits-outputs)
+ [Limits for other features](#limits-other-features)
+ [Limits for API requests](#limits-api)

## Limits for inputs
<a name="limits-inputs"></a>




- **Input number, push inputs**
  - You can attach 0 to 2 push inputs to a channel.

- **Input number, pull inputs**
  - You can attach up to 20 inputs to a channel. After you have counted the push inputs, the remainder can be pull inputs.

- **Input number, special rule for CDI inputs**
  - You can attach 0 or 1 regular CDI inputs to a channel. This input is a push input, so it counts towards the maximum number of push inputs in the channel. You can attach one set of partner CDI inputs to a channel. Attaching this set uses up the maximum number of push inputs in the channel. For information about these inputs, see [Creating CDI inputs as partner inputs](feature-cdi-partner.md).

- **Input number, special rule for Elemental Link inputs**
  - You can attach up to 2 Elemental Link inputs to a channel. Elemental Link inputs are push inputs, so each counts towards your maximum number of push inputs in the channel. +  You can attach these two Elemental Link inputs to one standard channel in order to implement [pipeline redundancy](plan-redundancy-mode.md). <br />+  You can include one or both of these Elemental Link inputs in a multiple-input channel, as part of an [input switching workflow](scheduled-input-switching.md). 

- **Input number, special rule for Elemental Link inputs per AWS Elemental Link hardware device**
  - You can create up to 4 inputs (Link inputs) from each AWS Elemental Link hardware device. You can then attach each input to a different channel.

- **Input number, special rule for SMPTE 2110 inputs**
  - You can attach 0 or 1 SMPTE 2110 inputs to a channel.

- **Input types – for dynamic inputs**
  - Only MP4 and Transport Stream (TS) file inputs that are stored in Amazon S3 or AWS Elemental MediaStore be set up as dynamic inputs.

- **Input types – in multiple-input channels**
  - You can attach multiple inputs to a channel, in order to implement input switching. You can't include an HLS input that is a VOD asset. For the definition of a VOD asset, see [Support for live and file sources](inputs-live-vs-file.md).
  - For the inputs that you attach in order to implement input switching, there are restrictions related to input types and Availability Zones:+  You can have multiple MediaConnect inputs attached to one channel, but all those inputs must be in the same two Availability Zones.  <br />+  You can have multiple VPC inputs attached to one channel, but all these inputs must be in the same two Availability Zones. VPC inputs include CDI inputs, RTP VPC inputs, and RTMP VPC inputs.  <br />+  If the channel has both MediaConnect inputs and VPC inputs, all these inputs must be in the same two Availability Zones. 

- **Input – audio and captions selectors**
  - Maximum of 32 audio and captions selectors (in any combination) in one channel.

- **Input – captions selectors for OCR conversion**
  - A maximum of 3 captions selectors that will use OCR conversion, per input.<br />A selector uses OCR conversion if the specified format is DVB-Sub or SCTE-27, and at least one output encode that uses the selector is a [WebVTT encode](output-sidecar-and-smptett-mss.md). If the selector is used in more than one WebVTT encode (for example, in two output groups), the selector counts only once towards the limit.



## Limits for outputs
<a name="limits-outputs"></a>




- **Output, types**
  - Maximum of one Archive output groups in a channel. Maximum of one MediaConnect Router output group in a channel.<br />Maximum of five outputs in a MediaConnect Router output group.<br />Maximum of 100 Mbps on a MediaConnect Router output.<br />MediaConnect Router output groups are not yet supported in opt-in regions.<br />For information about output types, see [Output types supported in MediaLive](outputs-supported-containers.md).

- **Output encodes, frame capture**
  - For frame capture encodes:+  Maximum of three frame capture encodes in a channel. The single encode in a Frame capture output group, and each (optional) [frame capture encode](#eml-limitations-and-rules) in an HLS output group both count towards this limit. <br />+  Maximum of three Frame capture outputs in each HLS output group. For information about output types, see [Output types supported in MediaLive](outputs-supported-containers.md). 

- **Output video encodes, UHD resolution, and input type**
  - A channel with a CDI input allows one UHD output encode (maximum).<br />The maximum number of *channels *with UHD is a quota that you can change, as described in [Quotas in MediaLive](limits.md). If you are using a CDI input, the maximum number of UHD *outputs* is a limitation. You can't change it.

- **Output video encodes, resolutions, and codecs**
  - Standard definition (SD) video is supported with all codecs. For information about supported output codecs, see [Supported codecs by output type](outputs-supported-codecs.md).
  - High definition (HD) video is supported with AV1, H.264, and H.265.
  - Ultra-high definition (UHD or 4K) video is supported with H.264 and H.265. AV1 supports only SD and HD resolutions.For information about output video resolutions, see [Supported codecs by output type](outputs-supported-codecs.md).

- **Output – audio encodes**
  - Maximum of 40 audio encodes in one channel.



## Limits for other features
<a name="limits-other-features"></a>




- **Color space, 3D LUT files in a channel**
  - Maximum of 8 files in each channel.For information about using 3D LUT files when converting color space, see [Getting ready to use 3D LUTs files with MediaLive](color-space-process-with-lut.md).

- **Image Overlays**
  - Maximum of eight different overlays (layers) active at one time in a channel. This means that the video can show up to eight different overlays at the same time.For information about image overlay, see [Working with image overlays](working-with-image-overlay.md).

- **Motion graphic overlay**
  - Maximum of one motion graphic overlay active at one time in a channel.For information about motion graphic overlay, see [Working with motion graphics overlays](feature-mgi.md).

- **Multiplexes **
  - Each multiplex produces only one MPTS. <br />For information about multiplex, see [Using MediaLive multiplex to create an MPTS](feature-multiplex.md).
  - All multiplex programs must include video.

- **Multiplexes, programs in a multiplex**
  - Maximum of 20 programs per multiplex. 
  - Each program in a multiplex is single use. It is attached only to one multiplex, and you can use it only for that multiplex.

- **Multiplexes, channels in a multiplex**
  - Each channel contains one and only one output group, of type multiplex. It can't contain any other type of output group.
  - Each channel is single use. You can attach it to only one program in the multiplex. You can use it only for that multiplex. 

- **Output locking feature**
  - Output locking is supported only with HLS and Microsoft Smooth. Although you enable the feature globally (for the entire channel), it only works with HLS output groups and Microsoft Smooth output groups.

- **Resiliency, [automatic input failover](automatic-input-failover.md)**
  - The automatic input failover feature applies to inputs, not to the entire channel.You can set up failover in only two, paired, inputs. The inputs must be push inputs. 

- **Resiliency, [pipeline redundancy](plan-redundancy-mode.md)**
  - The pipeline redundancy feature (channel class) applies to the channel and all its inputs. The following rules apply to the channels and inputs:+  Standard channel – You can attach only standard-class inputs. <br />+  Single-pipeline channel – You can attach single-class inputs (to omit support for pipeline redundancy) or standard-class inputs (to allow for easy upgrade of the channel at a later date).  

- **Schedule, maximum number of actions**
  - The schedule can contain a maximum of 1500 actions. You can't change this maximum.This maximum includes stale actions, actions that are in progress, and actions that aren't yet active. If you are near this maximum, you should delete stale actions.

- **Schedule and input switches**
  - The schedule can contain any number of scheduled input switching actions. For information about input switching, see [Setting up for input switching](scheduled-input-switching.md).
  - You can switch to a specific input as many times as you want. 



## Limits for API requests
<a name="limits-api"></a>

The following limits exist for API requests. For information about the current maximums (quotas) and about how to request an increase on any quota, see the [Service Quotas](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/medialive/quotas) console.




- **Frequency of API requests, not including requests to the [thumbnails](thumbnails.md) API**
  - Maximum 20 steady-state TPS (transactions per second). <br />This limit is not a quota that you can increase.
  - Maximum 40 burst.This limit is not a quota that you can increase.

- **Frequency of requests to the thumbnails API. For more information, see [Limit on thumbnails in MediaLive](thumbnail-limits.md)**
  - There is a maximum to the TPS for thumbnail requests.This limit is a quota that you can increase. For the current quota, and to request an increase on the quota, see the [Service Quotas](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/medialive/quotas) console.

