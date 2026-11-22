

# Example 7: Regional blackout

## Scenario
<a name="monetization-functions-examples-blackout-scenario"></a>

A sports network can't show a game to viewers in one region. The player sends `player_params.in_blackout_region=true` for those viewers. The origin marks the program with SCTE-35 Program Start (16) and Program End (17) or Program Early Termination (18). Viewers in the region see a slate for the program, and everyone else sees the game.

## Configuration
<a name="monetization-functions-examples-blackout-config"></a>

**Black out the program (HLS\_TAG\_PROCESSOR):**

```JSON
{
  "FunctionId": "hls_regional_blackout",
  "FunctionType": "HLS_TAG_PROCESSOR",
  "HlsTagProcessorConfiguration": {
    "Runtime": "JSONATA",
    "TagFilter": ["EXT-X-DATERANGE"],
    "RunCondition": "{% tag.attributes.scte35Cmd and $count($decodeScte35(tag.attributes.scte35Cmd).descriptors[segmentation_type_id in [16, 17, 18]]) > 0 %}",
    "Output": {
      "tag": "{% (
        $d := $decodeScte35(tag.attributes.scte35Cmd);
        $starts := $count($d.descriptors[segmentation_type_id = 16]) > 0;
        $ends := $count($d.descriptors[segmentation_type_id in [17, 18]]) > 0;
        $cmd := player_params.in_blackout_region and $starts ? $startBlackout('https://example.com/slates/regional.mp4', 14400)
          : $ends ? $endBlackout() : null;
        $cmd ? $updateTag(tag, { 'blackoutConfiguration': $cmd }) : $passthroughTag(tag)
      ) %}"
    }
  }
}
```

The `RunCondition` limits evaluation, and billing, to tags that carry program boundary descriptors.

**Cover viewers who join mid-program (optional, HTTP\_REQUEST):**

Viewers who join mid-program never see the Program Start tag. To cover them, add a `PRE_SESSION_INITIALIZATION` `HTTP_REQUEST` function that asks your entitlement service whether a blackout is active.

```JSON
{
  "FunctionId": "session_blackout_entitlement",
  "FunctionType": "HTTP_REQUEST",
  "HttpRequestConfiguration": {
    "Runtime": "JSONATA",
    "MethodType": "GET",
    "Url": "{% 'https://entitlement.example.com/v1/blackout?sessionId=' & $encodeUrlComponent(session.uuid) %}",
    "RequestTimeoutMilliseconds": 1000,
    "Output": {
      "aws.blackoutOperation": "{% response.body.operation = 'start' ? 'BLACKOUT_ON_INIT' : 'NONE' %}",
      "aws.blackoutSlateUrl": "{% response.body.slateUrl %}",
      "aws.blackoutMaxDurationSecs": "{% response.body.maxDurationSeconds %}"
    }
  }
}
```

The response shape in the output expressions is an example. Match the field names to the response your entitlement service returns.

## Function mapping
<a name="monetization-functions-examples-blackout-mapping"></a>

```JSON
{
    "FunctionMapping": {
        "POST_ORIGIN_RESPONSE": "hls_regional_blackout",
        "PRE_SESSION_INITIALIZATION": "session_blackout_entitlement"
    }
}
```

The `PRE_SESSION_INITIALIZATION` mapping is optional. Include it only when you add the `session_blackout_entitlement` function.

## What happens when the function runs
<a name="monetization-functions-examples-blackout-runtime"></a>
+ Viewer in the region, already watching: the Program Start tag starts the blackout and the viewer sees the slate. The Program End or Program Early Termination tag ends it.
+ Viewer in the region who joins mid-program: the session function starts the blackout at session start. The Program End tag ends it.
+ Viewer outside the region: tags pass through, and no blackout starts.
+ If neither an end tag nor the max duration (here 4 hours) arrives, the blackout ends at the max duration. The maximum allowed is 12 hours.

For more information, see [Post-origin response](monetization-functions-hooks-post-origin.md), [Pre-session initialization](monetization-functions-hooks-pre-session.md), [HLS tag processor](monetization-functions-types-hls-tag-processor.md), and [Blackout](monetization-functions-blackout.md).