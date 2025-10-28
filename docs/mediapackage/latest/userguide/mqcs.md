# Leveraging media quality scores with AWS Elemental MediaPackage

Streaming media quality is influenced by many factors. To ensure the highest quality
viewing experience, services in the video streaming workflow must have awareness of, and
ability to act on, indicators of quality down to the segment level in a stream. MediaPackage uses
media quality confidence score (MQCS) functionality to receive, act on, calculate, and
communicate quality scores of live streaming content. When adopted into your entire
workflow, MQCS provides an automated operation to ensure that you provide the optimum
viewing experience to your customers.

The following sections describe how MediaPackage leverages media quality scores from stream
inputs and through origin outputs to continuously monitor video quality, correct for errors
in the live streaming workflow, and help facilitate debugging through increased visibility.

MQCS is available with CMAF ingest, and is enabled by default. To adjust settings, select
the MQCS settings on your CMAF channels. For more information about channel settings, see
[Creating a channel in AWS Elemental MediaPackage](channels-create.md "channels-create.md").

## How MQCS works

The following is a high-level explanation of how MediaPackage uses quality scores from its
inputs and in its outputs. For a more detailed explanation about quality scores and how
to set up your quality-aware workflow, see the blog [Improve your viewers' live streaming experience with Media Quality-Aware Resiliency](https://aws.amazon.com/blogs/media/improve-your-viewers-live-streaming-experience-with-media-quality-aware-resiliency/ "https://aws.amazon.com/blogs/media/improve-your-viewers-live-streaming-experience-with-media-quality-aware-resiliency/").

### MQCS with inputs to MediaPackage

MQCS in input streams to MediaPackage builds on [live
input redundancy](what-is-flow-ir.md "what-is-flow-ir.md") functionality. With input redundancy, MediaPackage receives two
input streams to a channel. If the active stream is missing any segments, MediaPackage
automatically switches to the other stream. MediaPackage continually monitors the streams
and switches between them as needed based on segment availability.

With MQCS, the upstream encoder (MediaLive) calculates a quality score for the stream
at the ABR-level, based on the health of the source bitstream or elementary, error
recovery, and segment errors. The encoder communicates this score to MediaPackage. When the
input streams have identical health (segment availability and latency), MediaPackage
determines which stream to use for source content based on which has the highest
quality score. MediaPackage can effectively provide dynamic segment replacement as it
receives content from the encoder.

When both input streams have equal MQCS scores, you can configure MediaPackage to prefer
a specific input by setting the **Preferred input** option when
creating or updating your channel. This ensures consistent behavior when quality
scores are identical, which is particularly useful for cross-Region architectures
where multiple MediaPackage channels need to produce identical outputs.

The inputs are identified as follows:

- **Input 1** corresponds to the first ingest
  endpoint URL returned in the channel creation response
- **Input 2** corresponds to the second ingest
  endpoint URL returned in the channel creation response

You can also use MQCS to aid in [Cross-Region failover](cross-region-failover.md "cross-region-failover.md") when you enable MediaPackage to include
quality scores in responses to requests from downstream systems, such as CDNs
(CloudFront). The next section describes how MQCS works with outputs from MediaPackage.

### MQCS with outputs from MediaPackage

As MediaPackage receives streams from the encoder, it re-calculates the quality score for
each segment and track type. It also calculates an average quality score for all
segments in the media sequence. MediaPackage communicates this score through CMSD headers
in its responses to downstream systems, such as CDNs (CloudFront) and other
quality-monitoring systems.

Downstream systems can use the quality scores from MediaPackage to determine from which
origin to serve content, failing over between origins to provide the highest quality
viewing experience. CloudFront uses the quality scores as an input to its media
quality-aware resiliency functionality (MQAR). For information about MQAR, see [Media quality-aware resiliency](../../../AmazonCloudFront/latest/DeveloperGuide/media-quality-score.md "../../../AmazonCloudFront/latest/DeveloperGuide/media-quality-score.md") in the _Amazon CloudFront Developer Guide_.

## Requirements for using MQCS

Your workflow must meet these requirements to use MQCS:

- To enable CDN failover based on quality scores, you must have two identical
  channels in MediaPackage, with identical origin endpoints.
- Your CDN must support common media server data (CMSD) HTTP headers. If you're
  using CloudFront, see [Use
  real-time logs](../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md "../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md") in the _Amazon CloudFront Developer
  Guide_ for more information about CMSD and CMCD headers in logs.
- For resiliency against Region failures, you must set up cross-Region failover.
  For details and instructions, see the blog [Build a resilient cross-Region live streaming architecture in
  AWS](https://aws.amazon.com/blogs/media/build-a-resilient-cross-region-live-streaming-architecture-on-aws/ "https://aws.amazon.com/blogs/media/build-a-resilient-cross-region-live-streaming-architecture-on-aws/").
