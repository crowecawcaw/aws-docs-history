

# AWSE SCTE-35 format
<a name="awse-scte35-format"></a>

AWSE is a `format_identifier` value used in the SCTE-35 MPU UPID structure. Some AWS Elemental MediaLive features use this format to carry additional information in SCTE-35 `splice_info_section` messages.

This page describes the binary format of AWSE descriptors, including the versioned envelope structure and registered feature payloads.

## Features using the AWSE `format_identifier`
<a name="scte35-enrichment-operations"></a>

The following table lists the MediaLive features that append AWSE descriptors to SCTE-35 messages.


| Operation | Enabled by | Feature ID | Description | 
| --- | --- | --- | --- | 
| Append Elemental Inference query parameters | [Contextual metadata enrichment](elemental-inference-cm-enrichment.md) | EICM (Elemental Inference Contextual Metadata) | Embeds the Elemental Inference feed identifier, data plane URL, and a conditioner-timeline PTS into a Content Identification descriptor so that downstream systems can query the Elemental Inference GetMetadata API. See [EICM payload: Contextual metadata enrichment](scte35-enrichment-eicm.md). | 

## AWSE format specification
<a name="scte35-enrichment-awse-format"></a>

The AWSE `format_identifier` provides a versioned, extensible envelope. This envelope identifies the feature that produced the descriptor and carries a feature-specific payload. The following sections describe the outer descriptor structure, the envelope fields, and the registered feature identifiers.

### Segmentation descriptor structure
<a name="scte35-enrichment-awse-descriptor"></a>

Each AWSE descriptor follows the SCTE 35 `segmentation_descriptor()` syntax:

```
segmentation_descriptor {
    splice_descriptor_tag           = 0x02
    descriptor_length               = 15 + segmentation_upid_length
    identifier                      = 0x43554549 ('CUEI')
    segmentation_event_id           = <unique per splice_info_section>
    segmentation_event_cancel_indicator = 0
    program_segmentation_flag       = 1
    segmentation_duration_flag      = 0
    delivery_not_restricted_flag    = 1
    segmentation_upid_type          = 0x0C (MPU)
    segmentation_upid_length        = <varies by feature>
    segmentation_upid               = <AWSE format_identifier + envelope — see AWSE UPID envelope>
    segmentation_type_id            = 0x01 (Content Identification)
    segment_num                     = 0
    segments_expected               = 0
}
```

The `segmentation_upid_type` is always `0x0C` (MPU). The `segmentation_type_id` is always `0x01` (Content Identification). The `segmentation_upid` begins with the `format_identifier` value `"AWSE"`, followed by the envelope fields described in [AWSE UPID envelope](#scte35-enrichment-awse-envelope).

### AWSE UPID envelope
<a name="scte35-enrichment-awse-envelope"></a>

The `segmentation_upid` begins with a fixed envelope header. This header identifies the `format_identifier`, schema version, and feature. Depending on the feature, a feature-specific payload might or might not follow. Parsers use the `feature_id` to determine how to interpret the remaining bytes (if any).

The fields appear in the order shown.


| Field | Size | Type | Description | 
| --- | --- | --- | --- | 
| format\_identifier | 4 bytes | ASCII | "AWSE" — the SCTE-35 MPU format\_identifier value that identifies this UPID as an AWS Elemental payload. | 
| schema\_version | 1 byte | uint8 | Version of the AWSE envelope schema. Currently 0x01. A change to this value indicates a structural change to the envelope itself (including its size). | 
| feature\_id | 4 bytes | ASCII | Identifies which MediaLive feature produced this descriptor. Determines how to interpret any remaining bytes. See [Feature identifiers](#scte35-enrichment-awse-feature-ids). | 
| (feature-specific payload) | variable | — | Any additional fields required by the feature\_id you chose. Whether this payload is present, and its structure, depends entirely on the feature. See the feature's payload reference for details. | 

For schema version 1, the envelope header is 9 bytes (4 \+ 1 \+ 4). A feature-specific payload might or might not follow the `feature_id`, depending on the feature. When a payload is present, its length is `segmentation_upid_length - 9`. The feature defines the payload structure entirely; see the feature's payload reference for details.

Parsers that do not recognize a `feature_id` should skip the descriptor gracefully.

### Feature identifiers
<a name="scte35-enrichment-awse-feature-ids"></a>

The following table lists the registered `feature_id` values.


| Feature ID | Feature | Payload reference | 
| --- | --- | --- | 
| EICM | Contextual metadata enrichment (AWS Elemental Inference) | [EICM payload: Contextual metadata enrichment](scte35-enrichment-eicm.md) | 