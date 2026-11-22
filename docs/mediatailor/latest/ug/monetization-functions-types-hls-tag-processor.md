

# HLS tag processor

## When to use
<a name="monetization-functions-types-hls-tag-processor-when"></a>

Use `HLS_TAG_PROCESSOR` to filter, rewrite, or remove HLS tags in the origin manifest before MediaTailor parses ad markers and calls the ad decision server (ADS).

This type is valid only at the `POST_ORIGIN_RESPONSE` lifecycle hook. For when the hook fires and the input it provides, see [Post-origin response](monetization-functions-hooks-post-origin.md). You can use it to process `EXT-X-DATERANGE` tags in HLS streams.

## Configuration fields
<a name="monetization-functions-types-hls-tag-processor-fields"></a>

An `HLS_TAG_PROCESSOR` function has the following fields:


| Field | Required | Description | 
| --- | --- | --- | 
| Runtime | Yes | The expression language. Set this to JSONATA. | 
| TagFilter | Yes | Tag names that trigger evaluation. Accepts ["EXT-X-DATERANGE"]. | 
| RunCondition | No | Expression evaluated for each tag that matches TagFilter. The Output block runs only when it returns true. | 
| Output.tag | Yes | Expression that returns exactly one tag action: $updateTag, $removeTag, or $passthroughTag. | 
| Output.player\_params.<name> | No | Expression whose result is written to player\_params.<name> after the tag is processed. | 
| Output.temp.<name> | No | Scratch value for the current invocation. | 

```JSON
{
    "FunctionId": "myTagProcessor",
    "FunctionType": "HLS_TAG_PROCESSOR",
    "HlsTagProcessorConfiguration": {
        "Runtime": "JSONATA",
        "TagFilter": ["EXT-X-DATERANGE"],
        "RunCondition": "{%$exists(tag.attributes.scte35Cmd)%}",
        "Output": {
            "tag": "{%$passthroughTag(tag)%}",
            "player_params.<name>": "{%<expression>%}"
        }
    }
}
```

Replace `<name>` with the player parameter name, and `<expression>` with the JSONata expression whose result is written to it.

## How tags are processed
<a name="monetization-functions-types-hls-tag-processor-processing"></a>

MediaTailor walks the segments in playlist order. For each tag that matches `TagFilter` and passes `RunCondition`, MediaTailor binds the tag to the variable `tag` and evaluates `Output`.

Each tag identity (its `ID` attribute) is evaluated at most once for each playback session. On later manifest refreshes, MediaTailor replays the recorded result. Results for delivered tags are final.

## Run conditions and billing
<a name="monetization-functions-types-hls-tag-processor-run-conditions"></a>

You're billed only for evaluations where `RunCondition` returns `true`. Use `RunCondition` to skip tags you don't change.

For example, the following condition evaluates a tag only when it carries a segmentation descriptor of type 16, 17, or 18:

```JSON
{
    "RunCondition": "{% $count($decodeScte35(tag.attributes.scte35Cmd).descriptors[segmentation_type_id in [16,17,18]]) > 0 %}"
}
```

## Tag actions
<a name="monetization-functions-types-hls-tag-processor-actions"></a>

The `Output.tag` expression must return exactly one tag action.


| Function | Result | 
| --- | --- | 
| $updateTag(tag, patch) | Emits the tag with patch applied. | 
| $removeTag(tag) | Removes the tag from the manifest. | 
| $passthroughTag(tag) | Emits the tag unchanged. | 

The `patch` argument of `$updateTag` maps paths to new values. The following paths are supported.


| Path | Effect | 
| --- | --- | 
| attributes.scte35Cmd, attributes.scte35Out, attributes.scte35In | Replaces the SCTE-35 payload. Use $encodeScte35 to build the value. | 
| clientDefinedAttributes.X-<name> | Adds or overwrites a custom attribute. null removes it. | 
| blackoutConfiguration | Attaches a blackout start or end command: $startBlackout(...), $endBlackout(), or null. For more information, see [Blackout](monetization-functions-blackout.md). | 

For the SCTE-35 helpers (`$decodeScte35`, `$encodeScte35`, `$insertUpidIfEmpty`, and `$replaceUpid`), see [HLS tag processor functions (9)](monetization-functions-jsonata.md#monetization-functions-jsonata-allowed-tag-processor).

## HLS specification compliance
<a name="monetization-functions-types-hls-tag-processor-compliance"></a>

MediaTailor rejects changes that would make the manifest violate RFC 8216. In that case, MediaTailor emits the tag unchanged and logs the rejection to the customer log stream.

Same-`ID` `EXT-X-DATERANGE` tags form one date range, so the following rules apply:
+ If you change an attribute on a tag after MediaTailor delivered its pair, MediaTailor rejects the change.
+ If you remove one tag of a pair, MediaTailor removes both tags.
+ If you change an attribute on the first tag (OUT), MediaTailor copies the change to the second tag (IN).

## Composing with a concurrent executor
<a name="monetization-functions-types-hls-tag-processor-composition"></a>

You can combine HLS tag processors in a `CONCURRENT_EXECUTOR` only when their `TagFilter` sets don't overlap. MediaTailor rejects the playback configuration mapping if two children can match the same tag.

Each tag goes to the child whose filter matches it. Other tags pass through. For more information, see [Concurrent executor](monetization-functions-types-concurrent-executor.md).

## Example: Remove unused descriptors
<a name="monetization-functions-types-hls-tag-processor-example"></a>

The following function keeps only Program Start (16) and Program End (17) segmentation descriptors. If a tag has no descriptors left after filtering, the function removes it. The `RunCondition` limits billing to tags that carry a matching descriptor.

```JSON
{
    "FunctionId": "removeUnusedDescriptors",
    "FunctionType": "HLS_TAG_PROCESSOR",
    "HlsTagProcessorConfiguration": {
        "Runtime": "JSONATA",
        "TagFilter": ["EXT-X-DATERANGE"],
        "RunCondition": "{% $count($decodeScte35(tag.attributes.scte35Cmd).descriptors[segmentation_type_id in [16,17]]) > 0 %}",
        "Output": {
            "tag": "{% tag.attributes.scte35Cmd ? ($count($decodeScte35(tag.attributes.scte35Cmd).descriptors[segmentation_type_id in [16,17]]) > 0 ? $updateTag(tag, { 'attributes.scte35Cmd': tag.attributes.scte35Cmd ~> $decodeScte35 ~> |$| { 'descriptors': [descriptors[segmentation_type_id in [16,17]]] } | ~> $encodeScte35 }) : $removeTag(tag)) : $passthroughTag(tag) %}"
        }
    }
}
```

The `tag` expression guards on `tag.attributes.scte35Cmd`. Tags with no SCTE-35 payload pass through unchanged.