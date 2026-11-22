

# Post-origin response

## When it fires
<a name="monetization-functions-hooks-post-origin-when"></a>

MediaTailor runs the function mapped to `POST_ORIGIN_RESPONSE` after it fetches a manifest from the content origin, and before it parses ad markers and calls the ADS. The ADS and the player see the processed tags, not the origin tags.

The function runs once for each tag that matches its `TagFilter`. MediaTailor processes each tag at most once per playback session. Later manifest refreshes reuse the recorded result, and results for delivered tags don't change.

This hook supports HLS streams and `EXT-X-DATERANGE` tags.

This hook runs in the manifest-delivery path under its own CPU limit for each invocation, not the 2,000 ms combined budget that the request-path hooks share. For more information, see [Limits](monetization-functions-limits.md).

## Input
<a name="monetization-functions-hooks-post-origin-input"></a>

`event.*`, `mediaPlayList.*`, `tag`, `player_params.*`, and `temp.*`. For all available fields, see [Input field reference](monetization-functions-hooks.md#monetization-functions-hooks-input-ref).

## Media playlist and tag variables (mediaPlayList.\*, tag)
<a name="monetization-functions-hooks-post-origin-vars"></a>

The following read-only variables describe the media playlist and the tag being processed.


| Field | Type | Description | 
| --- | --- | --- | 
| event.streamFormat | String | Stream format. HLS. | 
| event.streamId | String | Stream identifier. | 
| event.playbackConfigName | String | Playback configuration name. | 
| event.lastProcessed | String | ISO 8601 time of the previous invocation for this session. Absent on the first invocation. | 
| mediaPlayList.targetDuration | Number | EXT-X-TARGETDURATION value. | 
| mediaPlayList.mediaSequenceNumber | Number | EXT-X-MEDIA-SEQUENCE value. | 
| mediaPlayList.startDate | String | Program date-time of the first segment. | 
| mediaPlayList.segments | Array | Segments in playlist order. | 
| mediaPlayList.segments[].uri | String | Segment URI. | 
| mediaPlayList.segments[].duration | Number | Segment duration in seconds. | 
| mediaPlayList.segments[].tags | Array | Tags attached to the segment. | 
| tag | Object | The tag being processed. Same shape as an element of segments[].tags. | 
| tag.name | String | Tag name, for example EXT-X-DATERANGE. | 
| tag.attributes.id | String | ID attribute. | 
| tag.attributes.startTime | String | START-DATE attribute. | 
| tag.attributes.classString | String | CLASS attribute. | 
| tag.attributes.endTime | String | END-DATE attribute. | 
| tag.attributes.duration | Number | DURATION attribute. | 
| tag.attributes.plannedDuration | Number | PLANNED-DURATION attribute. | 
| tag.attributes.scte35Cmd/scte35Out/scte35In | String | SCTE35-CMD, SCTE35-OUT, SCTE35-IN payloads. | 
| tag.clientDefinedAttributes | Object | X-\* attributes on the origin tag. Present even when empty. | 

Only `id` and `startTime` are always present. Other attributes appear only when the origin tag has them, so use `$exists()` to check before accessing. These variables are read-only.

## Output namespace allowed
<a name="monetization-functions-hooks-post-origin-output"></a>


| Namespace | Accepted types | How the output is used | 
| --- | --- | --- | 
| tag | Tag action (required) | Returned by $updateTag, $removeTag, or $passthroughTag. Determines how the tag appears in the manifest. | 
| player\_params.\* | Strings, numbers, booleans | Written after the tag is processed. A value persists for the player session and threads into later tags and manifest refreshes, so a value such as a UPID read from a Program Start signal is available to a later tag. It is also visible to subsequent hooks in the session (for example, PRE\_ADS\_REQUEST) and in ad decision server URL variables. Writes count toward the session player\_params size limit; a write that exceeds it is dropped and logged. | 
| temp.\* | Any JSON value | Scratch values for the current invocation. Not persisted. | 

## Supported function type
<a name="monetization-functions-hooks-post-origin-function-type"></a>

Use an `HLS_TAG_PROCESSOR` function at this hook. `HLS_TAG_PROCESSOR` is a helper function type that iterates through the media playlist for you, so you don't need to write your own manifest parser. For each tag that matches `TagFilter`, it evaluates your `Output` expressions and applies the transformation you return: update the tag, remove it, or pass it through unchanged. For configuration details, see [HLS tag processor](monetization-functions-types-hls-tag-processor.md).

The following example keeps only Program Start (16) and Program End (17) segmentation descriptors in each `EXT-X-DATERANGE` tag.

```JSON
{
  "FunctionId": "filter_descriptors",
  "FunctionType": "HLS_TAG_PROCESSOR",
  "HlsTagProcessorConfiguration": {
    "Runtime": "JSONATA",
    "TagFilter": ["EXT-X-DATERANGE"],
    "Output": {
      "tag": "{% tag.attributes.scte35Cmd ? $updateTag(tag, { 'attributes.scte35Cmd': tag.attributes.scte35Cmd ~> $decodeScte35 ~> |$| { 'descriptors': [descriptors[segmentation_type_id in [16,17]]] } | ~> $encodeScte35 }) : $passthroughTag(tag) %}"
    }
  }
}
```

## Typical use cases
<a name="monetization-functions-hooks-post-origin-use-cases"></a>
+ Remove SCTE-35 segmentation descriptors your ad workflow doesn't use, and remove tags left with none.
+ Copy the UPID from a Program Start signal into later Break Start and Break End signals that lack one.
+ Pass splice\_insert signals through unchanged while processing time\_signal messages.
+ Add, change, or remove custom `X-*` attributes on `EXT-X-DATERANGE` tags.
+ Start or end a regional blackout based on SCTE-35 signals.
+ Replace an external placement opportunity information system (POIS).

## Failure behavior
<a name="monetization-functions-hooks-post-origin-failure"></a>

If the function fails or exceeds a limit, MediaTailor still delivers the manifest. Tags already processed keep their results. Tags in the failed invocation pass through unchanged, and that result is final for the session. MediaTailor logs the failure to the customer log stream.

Each invocation is limited to 100 tags and 50 ms cumulative CPU. The cumulative modification size is limited to 25 KB per manifest window. For more information, see [Limits](monetization-functions-limits.md).