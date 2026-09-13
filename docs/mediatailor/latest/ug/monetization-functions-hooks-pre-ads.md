

# Pre-ads request
<a name="monetization-functions-hooks-pre-ads"></a>

## When it fires
<a name="monetization-functions-hooks-pre-ads-when"></a>

MediaTailor runs the function mapped to `PRE_ADS_REQUEST` once per ad break, immediately before sending the request to the ADS. The function runs each time an ad opportunity is encountered during manifest processing.

## Input
<a name="monetization-functions-hooks-pre-ads-input"></a>

All fields from `PRE_SESSION_INITIALIZATION`, plus `avail.*`, `scte.*`, `asset.*`, `inference.*`, and `adsRequest.*` (url, method, headers, body). For all available fields, see [Input field reference](monetization-functions-hooks.md#monetization-functions-hooks-input-ref).

## Elemental Inference contextual metadata variables (inference.\*)
<a name="monetization-functions-hooks-pre-ads-elemental-inference-vars"></a>

When your upstream encoder (such as AWS Elemental MediaLive) is configured for contextual metadata enrichment, it embeds Elemental Inference query parameters in SCTE-35 ad break markers. MediaTailor automatically parses these markers and exposes the following read-only variables in the `inference` namespace. These variables are the primary mechanism for dynamically configuring `AWS_SERVICE_REQUEST` functions that call Elemental Inference.

**Note**  
The `inference.*` variables are available only at the `PRE_ADS_REQUEST` hook. They are not available at `PRE_SESSION_INITIALIZATION`.


| Field | Type | Description | 
| --- | --- | --- | 
| inference.enriched | Boolean | true if Elemental Inference data was found and parsed successfully from the SCTE-35 marker. Check this before using other inference.\* fields. | 
| inference.feedId | String | The Elemental Inference feed identifier. | 
| inference.dataEndpoint | String | The data endpoint URL prefix for the Elemental Inference feed. Use this to construct the full GetMetadata URL. | 
| inference.pts | Long | The presentation timestamp (PTS) corresponding to the ad break signal. Used as the end of the query time window. | 
| inference.timescale | Long | The timescale for interpreting PTS values (for example, 90000 for 90 kHz). | 
| inference.region | String | The AWS Region extracted from the query URL. Use this as the TargetRegion for your AWS\_SERVICE\_REQUEST function. | 
| inference.previousBreakEndPts | Long | The PTS at which content resumed after the previous ad break. Use this as the start of the query time window to analyze only the content that played between breaks. Absent for the first ad break in a session. | 
| inference.parseError | Boolean | true if an Elemental Inference marker was found but could not be parsed. Indicates a configuration issue with the upstream encoder. | 

These variables are read-only. Functions cannot modify `inference.*` values.

When `inference.enriched` is `false` or absent, the remaining `inference.*` fields are not available. Your JSONata expressions must include fallback values to handle this case gracefully.

For how to use these variables in practice, see [Elemental Inference integration](monetization-functions-elemental-inference-integration.md).

## Output namespace allowed
<a name="monetization-functions-hooks-pre-ads-output"></a>


| Namespace | Accepted types | How the output is used | 
| --- | --- | --- | 
| player\_params.\* | Strings, numbers, booleans | Overrides session player parameters for this ad break. Available to the ADS request URL through [MediaTailor dynamic ad variables for ADS requests](variables.md). | 
| session.\* | Strings, numbers, booleans | Overrides session variables for this ad break. Available to the ADS request URL through dynamic variable substitution. | 
| avail.\* | Strings, numbers, booleans | Overrides avail variables for this ad break. Available to the ADS request URL through dynamic variable substitution. | 
| scte.\* | Strings, numbers, booleans | Overrides SCTE variables for this ad break. Available to the ADS request URL through dynamic variable substitution. | 
| asset.\* | Strings, numbers, booleans | Overrides asset metadata variables (from EXT-X-ASSET tags) for this ad break. Available to the ADS request URL through dynamic variable substitution. For more information, see [HLS supported ad markers](hls-ad-markers.md). | 
| adsRequest.\* | String | Overrides the ADS request for this ad break only. Supported fields: url, method, headers.<name>, body. The url value is treated as a template and supports [MediaTailor dynamic ad variables for ADS requests](variables.md) after the function runs. Not persisted. | 

**Note**  
All output from the `PRE_ADS_REQUEST` hook is a transient override. It applies only to the current ad break's ADS request and is not persisted to the session.

**Example — rewriting the ADS request:**

```
{
    "Output": {
        "adsRequest.url": "{%'https://ads.example.com/v1/vast?sid=' & session.id & '&genre=' & player_params.genre%}",
        "adsRequest.headers.X-Custom-Token": "{%player_params.auth_token%}"
    }
}
```

This replaces the ADS URL and adds a custom header for the current ad break.

## Typical use cases
<a name="monetization-functions-hooks-pre-ads-use-cases"></a>
+ Rewrite the ADS request URL to route traffic between different ad servers for A/B testing.
+ Append enrichment data (audience segments, identity tokens) to the ADS request URL or headers.
+ Conditionally modify ADS request parameters based on SCTE-35 signal data or avail index.
+ Query Elemental Inference for content classifications and brand safety signals to enable contextual ad targeting.

## Failure behavior
<a name="monetization-functions-hooks-pre-ads-failure"></a>

If a function attached to `PRE_ADS_REQUEST` fails for any reason, MediaTailor discards the function's output and proceeds as if no function were attached. The ADS request is sent using the original session and request parameters without modification.