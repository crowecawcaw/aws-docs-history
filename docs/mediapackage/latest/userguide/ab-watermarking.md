

# A/B forensic watermarking in AWS Elemental MediaPackage
<a name="ab-watermarking"></a>

AWS Elemental MediaPackage supports A/B forensic watermarking workflows for CMAF ingest. In an A/B watermarking workflow, the upstream encoder produces two watermark variants of the content and, on each incoming segment, signals which watermark variant and bit position the segment carries. MediaPackage uses this signal to make watermark-aware segment-combining decisions so that watermark bit positions stay aligned in the output. This alignment lets a downstream content delivery network (CDN) derive the correct bit position for each output segment.

To use A/B watermarking with MediaPackage, your workflow must meet the channel requirement and the upstream encoder must send the WMPaceInfoIngest header, as described in the following sections.

You configure A/B watermarking on the upstream encoder. When you use AWS Elemental MediaLive as the encoder, MediaLive produces the A and B watermark variants and sends each variant to a separate MediaPackage destination that you pair. For information about enabling A/B watermarking and configuring the A and B destinations in MediaLive, see [Creating A/B forensic video watermarks](https://docs.aws.amazon.com/medialive/latest/ug/feature-ab-watermark.html) in the *AWS Elemental MediaLive User Guide*.

## Channel requirements
<a name="ab-watermarking-channel-requirements"></a>

**Important**  
A/B watermarking is supported only on CMAF ingest channels that use *epoch-locked* output locking mode, which is the default mode for CMAF channels. Watermark-aware segment combining depends on epoch-locked segment numbering to keep watermark bit positions aligned. Channels that use non-epoch-locked mode, and ingest types other than CMAF, don't support A/B watermarking. For more information about output locking modes, see [Output locking mode for CMAF channels](cmaf-ingest.md#output-locking-mode).

For watermark bit positions to remain aligned across combined segments, configure your workflow so that the origin endpoint segment duration is a whole-number multiple of the encoder output segment duration. Set the encoder's watermark poly period so that the encoder output segment duration multiplied by the poly period equals the origin endpoint segment duration. This produces one watermark bit position per output segment. For example, a 2-second encoder output segment duration with a poly period of 3 matches a 6-second origin endpoint segment duration, and MediaPackage combines three input segments into each output segment.

**Note**  
You can use SCTE-35 ad markers on channels that use A/B watermarking. MediaPackage continues to split segments at SCTE-35 markers, and epoch locking keeps the A and B variants aligned across those splits.

## How watermarking affects segment combining
<a name="ab-watermarking-manifest-behavior"></a>

When watermarking is active, MediaPackage keeps each output segment within a single watermark bit position. If the watermark variant or bit position changes between input segments, or the encoder marks a watermark aggregation boundary by using the `firstpart` or `lastpart` fields, MediaPackage ends the current output segment at that boundary instead of combining across it. As a result, most output segments match your configured segment duration, but an output segment can be shorter where a watermark boundary falls. This appears in your HLS and DASH manifests as an occasional shorter segment at those boundaries.

## WMPaceInfoIngest header
<a name="ab-watermarking-header"></a>

When A/B watermarking is active, the upstream encoder must include a `WMPaceInfoIngest` HTTP header on each incoming media segment. This header carries the watermark pacing information for the segment, following the [ETSI TS 104 002](https://www.etsi.org/deliver/etsi_ts/104000_104099/104002/01.01.01_60/ts_104002v010101p.pdf) specification. MediaPackage parses this header to determine how to combine segments while preserving watermark bit positions.

The value of the `WMPaceInfoIngest` header is a JSON object. All of the following fields are required, and the header value must not exceed 500 characters.


**WMPaceInfoIngest header fields**  

| Field | Type | Description | 
| --- | --- | --- | 
| version | Integer | The version of the watermark pacing information. The only supported value is 1. | 
| variant | Integer | An integer, assigned by the encoder, that identifies which watermark variant (for example, the A or B rendition) the segment belongs to. | 
| position | Integer | The forensic watermark bit position that the segment carries, as determined by the encoder. This is the watermark bit position, not the segment sequence number. Valid values are -1 through 32767, where -1 indicates that the segment isn't watermarked. | 
| firstpart | Boolean | Whether this segment is the first segment of a watermark aggregation group. | 
| lastpart | Boolean | Whether this segment is the last segment of a watermark aggregation group. | 

The following is an example `WMPaceInfoIngest` header value:

```
{"version":1,"variant":0,"position":1024,"firstpart":true,"lastpart":false}
```