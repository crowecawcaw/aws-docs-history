

# Post-ads response
<a name="monetization-functions-hooks-post-ads"></a>

## When it fires
<a name="monetization-functions-hooks-post-ads-when"></a>

MediaTailor runs the function mapped to `POST_ADS_RESPONSE` after it receives and parses a response from the ADS, including resolution of VAST wrapper redirects. The function sees the parsed ads before MediaTailor selects ads to insert, so changes made here influence which ads fill the ad break.

The hook fires for all streaming protocols (HLS and DASH) and all playback modes (live, VOD, and pre-roll). It typically fires once per ad break. For ADS responses that cover multiple ad breaks at once (such as VMAP responses) and for prefetched ad responses, the hook fires when MediaTailor processes the response, and the `avail` input namespace is not present. Use `$exists(avail)` to check before accessing avail fields.

## Input
<a name="monetization-functions-hooks-post-ads-input"></a>

`event.*`, `session.*`, `adsRequest.*`, and `adsResponse.*`, plus `avail.*` when the response applies to a single ad break. For all available fields, see [Input field reference](monetization-functions-hooks.md#monetization-functions-hooks-input-ref).

## Output namespace allowed
<a name="monetization-functions-hooks-post-ads-output"></a>


| Namespace | Accepted types | How the output is used | 
| --- | --- | --- | 
| adsResponse.ads | Array of ad objects | Replaces the parsed ad list for this response. MediaTailor matches each returned ad to the original ads by adId and proceeds to ad selection with the returned list. | 
| temp.\* | Any | Temporary data for passing values between steps in an executor. Not persisted. | 

Write the modified ad list back to `adsResponse.ads`. You can:
+ **Filter** — return a subset of the original ads. Ads you omit are not considered for insertion, and the duration they occupied becomes available for other ads to fill.
+ **Reorder** — return the ads in a different order. Order affects which ads fill the ad break first.
+ **Modify** — change `durationSeconds`, `adSystem`, `adTitle`, `mediaFiles`, or `trackingEvents` on an ad. Ads returned unchanged keep all of their original VAST metadata.
+ **Inject** — add ads that were not in the original response. A new entry must include `adId`, `durationSeconds`, and `mediaFiles`. Ads fetched with a `VAST_REQUEST` function in the same hook invocation are an exception: appending such an ad by its `adId` is enough, because MediaTailor restores the ad's complete parsed VAST data. For more information, see [VAST request](monetization-functions-types-vast-request.md).

**Important**  
Always use a JSONata array constructor or array coercion when filtering. A filter expression such as `adsResponse.ads[adSystem != 'BLOCKED']` produces a single object when exactly one ad matches. It produces no value at all when zero ads match. In that case the output key is omitted and the filter has no effect. Wrap the expression in brackets or append `[]`:  

```
{
    "Output": {
        "adsResponse.ads": "{%adsResponse.ads[adSystem != 'BLOCKED'][]%}"
    }
}
```

The following rules apply to the returned ad list:
+ If two entries share an `adId`, the first occurrence wins.
+ Invalid entries are rejected individually. Valid entries in the same output still apply.
+ If an injected entry's `adId` collides with an ad from the ADS response, the original ad is used as the base and your field changes are applied on top of it.

## What this hook doesn't see
<a name="monetization-functions-hooks-post-ads-scope"></a>

This hook runs before ad selection, so it doesn't see ads that other MediaTailor features contribute later, and it can't determine which ads will ultimately be inserted, because transcode status and fill decisions happen afterward. For prefetched ads, the hook fires when MediaTailor processes the prefetch response itself. At a later ad break, those previously prefetched ads are merged after this hook runs, so the hook doesn't see them there. To act on the final ad set, use `PRE_MANIFEST_INSERTION`.

## Typical use cases
<a name="monetization-functions-hooks-post-ads-use-cases"></a>
+ Filter ads by metadata, such as removing ads from competing ad systems so they don't appear in the same ad break (competitive separation).
+ Fetch additional ads from a secondary ad server with a `VAST_REQUEST` function when the primary response is short, and append them to the ad list.
+ Reorder ads so that preferred ads fill the ad break first.
+ Modify tracking events or ad metadata before insertion.

## Failure behavior
<a name="monetization-functions-hooks-post-ads-failure"></a>

If a function attached to `POST_ADS_RESPONSE` fails for any reason, such as a timeout, an expression error, or invalid output, MediaTailor discards the function's output. The request proceeds with the original ADS response, as if no function were attached. If the serialized input exceeds the input size limit, MediaTailor skips the hook invocation entirely. For the limits that apply, see [Limits](monetization-functions-limits.md).