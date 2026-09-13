

# EICM payload: Contextual metadata enrichment
<a name="scte35-enrichment-eicm"></a>

The `EICM` (Elemental Inference Contextual Metadata) feature payload carries the information that downstream consumers need to query AWS Elemental Inference for contextual metadata at ad-decision time.

For information about enabling this feature on your channel, see [Contextual metadata enrichment](elemental-inference-cm-enrichment.md).

This payload follows the 9-byte AWSE envelope header (for schema version 1). The `feature_id` in the envelope is `"EICM"`. See [AWSE UPID envelope](awse-scte35-format.md#scte35-enrichment-awse-envelope) for the envelope structure.

## EICM version 1 payload
<a name="scte35-enrichment-eicm-v1"></a>

The EICM payload begins with a `feature_version` byte that identifies the payload structure version. For version 1 (`feature_version = 0x01`), the remaining fields contain the Elemental Inference feed identifier, the data plane URL for `GetMetadata` queries, and the PTS on the conditioner timeline corresponding to the cue-out.

The fields appear in the order shown.


| Field | Size | Type | Description | 
| --- | --- | --- | --- | 
| feature\_version | 1 byte | uint8 | Identifies the version of the EICM payload structure. Currently, only 0x01 is valid; the fields for version 1 are described in the remaining rows of this table. A change to this value would indicate a structural change to the remaining fields. | 
| feed\_id\_length | 1 byte | uint8 | Length N of the feed\_id field. | 
| feed\_id | N bytes | ASCII | The Elemental Inference feed identifier (no NUL terminator). | 
| inference\_query\_url\_length | 1 byte | uint8 | Length M of the inference\_query\_url field. | 
| inference\_query\_url | M bytes | ASCII | The Elemental Inference data plane URL for GetMetadata queries (no NUL terminator, no trailing slash). | 
| inference\_query\_pts | 8 bytes | int64 BE | The PTS of the cue-out on the Elemental Inference conditioner timeline. | 
| inference\_query\_timescale | 4 bytes | uint32 BE | The timebase of inference\_query\_pts (for example, 90000). | 

The total EICM v1 payload size is `15 + N + M` bytes. This total includes one 1-byte version field, two 1-byte length fields, the two variable-length strings, one 8-byte PTS field, and one 4-byte timescale field. Combined with the 9-byte envelope header (for schema version 1), the full `segmentation_upid_length` is `24 + N + M`.

**Important**  
The `inference_query_pts` and `inference_query_timescale` values might differ from the PTS format that your output uses. Downstream systems must use these values only to query the Elemental Inference `GetMetadata` API.

## Downstream usage
<a name="scte35-enrichment-eicm-usage"></a>

Downstream consumers, such as ad-decision systems (for example, AWS Elemental MediaTailor), parse the EICM payload and use the fields to query Elemental Inference:

1. Locate the `segmentation_descriptor` with `segmentation_type_id = 0x01` and a UPID whose `format_identifier` is `"AWSE"`.

1. Verify `feature_id = "EICM"` and `feature_version = 0x01`.

1. Extract `feed_id`, `inference_query_url`, `inference_query_pts`, and `inference_query_timescale`.

1. Call the Elemental Inference `GetMetadata` API at the extracted URL, passing the feed ID and PTS value.