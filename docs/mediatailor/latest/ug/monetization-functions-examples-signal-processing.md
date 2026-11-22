

# Example 6: SCTE-35 signal processing

## Scenario
<a name="monetization-functions-examples-signal-processing-scenario"></a>

A broadcaster uses an external placement opportunity information system (POIS) to clean SCTE-35 signals before ad insertion. The broadcaster wants MediaTailor to do this work instead, in an HLS tag processor function on the post-origin response. The function must:
+ Keep only segmentation types 16 (Program Start), 17 (Program End), 32 (Chapter Start), 33 (Chapter End), 34 (Break Start), and 35 (Break End), and drop every other descriptor.
+ Remove any tag that is left with no descriptors.
+ Copy the UPID from a Program Start descriptor into later Break Start and Break End descriptors that have none.
+ Pass `splice_insert` commands through unchanged.

## Configuration
<a name="monetization-functions-examples-signal-processing-config"></a>

**Process SCTE-35 signals (HLS\_TAG\_PROCESSOR):**

```JSON
{
  "FunctionId": "scte35_signal_processor",
  "FunctionType": "HLS_TAG_PROCESSOR",
  "HlsTagProcessorConfiguration": {
    "Runtime": "JSONATA",
    "TagFilter": ["EXT-X-DATERANGE"],
    "Output": {
      "player_params.upid": "{% tag.attributes.scte35Cmd ? ($u := $decodeScte35(tag.attributes.scte35Cmd).descriptors[segmentation_type_id = 16 and $length(segmentation_upid) > 0][0].segmentation_upid; $u ? $u : player_params.upid) : player_params.upid %}",
      "tag": "{% (
        $payload := tag.attributes.scte35Cmd ? { 'field': 'scte35Cmd', 'binary': tag.attributes.scte35Cmd }
          : tag.attributes.scte35Out ? { 'field': 'scte35Out', 'binary': tag.attributes.scte35Out }
          : tag.attributes.scte35In ? { 'field': 'scte35In', 'binary': tag.attributes.scte35In } : null;
        $payload ? (
          $decoded := $decodeScte35($payload.binary);
          $decoded.splice_command.type = 'splice_insert' ? $passthroughTag(tag) : (
            $filtered := $decoded ~> |$| { 'descriptors': [descriptors[segmentation_type_id in [16,17,32,33,34,35]]] } |;
            $processed := player_params.upid ? $insertUpidIfEmpty($filtered, [34,35], player_params.upid) : $filtered;
            $patch := $payload.field = 'scte35Cmd' ? { 'attributes.scte35Cmd': $encodeScte35($processed) }
              : $payload.field = 'scte35Out' ? { 'attributes.scte35Out': $encodeScte35($processed) }
              : { 'attributes.scte35In': $encodeScte35($processed) };
            $count($processed.descriptors) > 0 ? $updateTag(tag, $patch) : $removeTag(tag)
          )
        ) : $passthroughTag(tag)
      ) %}"
    }
  }
}
```

**Note**  
The `player_params.upid` expression falls back to the stored value when a Program Start arrives without a UPID, so it never clears a UPID that is already stored.

The `tag` expression maps each requirement to one part:
+ **Keep selected segmentation types** — `$filtered` keeps only descriptors whose `segmentation_type_id` is in `[16,17,32,33,34,35]`.
+ **Remove empty tags** — `$count($processed.descriptors) > 0 ? $updateTag(tag, $patch) : $removeTag(tag)` removes a tag that has no descriptors left.
+ **Backfill the UPID** — the `player_params.upid` output stores the UPID from a Program Start (type 16) descriptor, and `$insertUpidIfEmpty($filtered, [34,35], player_params.upid)` writes it into Break Start and Break End descriptors that have none.
+ **Pass through splice\_insert** — `$decoded.splice_command.type = 'splice_insert' ? $passthroughTag(tag)` returns the tag unchanged.

## Function mapping
<a name="monetization-functions-examples-signal-processing-mapping"></a>

```JSON
{
    "FunctionMapping": {
        "POST_ORIGIN_RESPONSE": "scte35_signal_processor"
    }
}
```

## What happens when the function runs
<a name="monetization-functions-examples-signal-processing-runtime"></a>

1. A Program Start tag arrives. MediaTailor stores its UPID in `player_params.upid`.

1. A Break Start tag with no UPID arrives in a later manifest. The function filters its descriptors and inserts the stored UPID.

1. A tag that is left with only unwanted descriptors is removed.

1. A `splice_insert` tag passes through unchanged.

1. The ad decision server sees only the processed signals.

For more information, see [Post-origin response](monetization-functions-hooks-post-origin.md) and [HLS tag processor](monetization-functions-types-hls-tag-processor.md).