# Working with cross-Region failover in

AWS Elemental MediaPackage

MediaPackage supports workflows where a CDN transparently fails over between multiple MediaPackage Live
v2 origins located in different AWS Regions. The failover functionality also works in a
single Region, but such a configuration doesn't protect against regional failures. The
purpose of such failover architectures is to force CDN requests to be forwarded to one or
more backup origins if the stream on the primary origin is not considered healthy. To be
transparent, the failover needs all the MediaPackage origins to produce symmetric streams. This
requirement can be satisfied through the combination of multiple requirements and
restrictions at different levels in the workflow as described in the following
sections.

## Requirements for cross-Region failover in

AWS Elemental MediaPackage

If your workflow respects these requirements and restrictions, origin failovers should
be seamless for your viewers and not generate live-stream-playback disruptions.

**Encoding**
The live encoders need to send aligned
ingest streams to all involved MediaPackage channels. This is achieved through the use of
epoch-locked CMAF ingest streamsets, where segmentation is using a regular cadence,
and the indexing of the segments is based on the epoch time. This can be configured
in MediaLive and AWS Elemental Live using the CMAF Ingest output group. For more details
about the configuration and the input timecode requirements, see [Creating CMAF Ingest Output Groups](../../../medialive/latest/ug/creating-cmafi-output-group.md "../../../medialive/latest/ug/creating-cmafi-output-group.md") in the _MediaLive user
guide_.

The encoding settings and CMAF Ingest output group settings must be
identical across multiple encoders. However, it’s possible to use
heterogeneous MediaLive channel types in different Regions, such as a standard
MediaLive channel in Region A and a single pipeline MediaLive channel in Region
B.

Your encoder configuration must also adhere to [Encoder restrictions for cross-Region failover](#cross-region-failover-rest "#cross-region-failover-rest").

**Packaging origination**

All involved MediaPackage
Live v2 channels and endpoints need to be configured with strictly identical
configuration settings, such as URL path, segmentation parameters, and encryption
parameters. The channel input type needs to be CMAF. If the channel input type is
HLS, the alignment of the output streams will not be guaranteed. Finally, the MediaPackage
channel that will act as the primary origin in the CDN origin group needs to include
a **Force endpoint error configuration** that will have MediaPackage
return 404 responses to the CDN in some problematic situations, like missing or
incomplete ingest, failed key rotations, or slate input (resulting from the upstream
encoder having lost its contribution source). For more information, see [Endpoint settings fields](endpoints-create.md#endpoints-settings "endpoints-create.md#endpoints-settings"). We recommend
to set the primary MediaPackage origin settings with aggressive **Force endpoint
error configuration** settings (at least Stale manifests, incomplete
manifest and Slate input). These settings should not be activated on the backup
MediaPackage origin, in order to maximize chances of a successful origin failover at the
CDN level.

**CDN**

The CDN distribution should be configured to
trigger origin failovers on network connection errors and 404 Not Found response
codes returned by the origin. Other 4xx/5xx response codes can also be used as
failover triggers, on top of the 404 code, to cover a wider range of problems that
are not related to the MediaPackage endpoint error configuration. For more information, see
[Optimize high availability with CloudFront origin failover](../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md "../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md").

## Encoder restrictions for cross-Region failover

Your encoder configuration, or re-configuration, must adhere to the following restrictions for cross-Region failover to work effectively.

- All video framerates in the CMAF output group need to be consistent.
  They should be either all fractional framerates, or all integer
  framerates, not a mix of the two. The combined use of framerates that
  are multiples of one another, like 25fps and 50fps or 29.97fps and
  59.94fps, is allowed.
- The transition from fractional framerates to integer framerates (or
  the other way around) across two encoding sessions is not allowed. The
  two framerates also need to be multiples of one another: 25fps to 50fps
  or 50fps to 25fps are allowed transitions, but 25fps to 30fps or 30fps
  to 25fps are not.
- The output segments sequence numbers should not go back in the past across two
  encoding sessions. The segment duration should not increase and the reference
  Epoch time should not change after the first encoding session.

If segment numbers go backward, MediaPackage sends a `409` error
response to the encoder. To recover from this state, see [Reset for channels and endpoints](resetting.md "resetting.md").

- The encoder output names must be identical across all Regions.
