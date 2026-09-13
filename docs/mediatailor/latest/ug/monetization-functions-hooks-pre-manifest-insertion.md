

# Pre-manifest insertion
<a name="monetization-functions-hooks-pre-manifest-insertion"></a>

## When it fires
<a name="monetization-functions-hooks-pmi-when"></a>

MediaTailor runs the function mapped to `PRE_MANIFEST_INSERTION` once per personalization pass. This happens at the end of ad break personalization, after ad selection, transcode checks, and fill policy, and immediately before MediaTailor writes the ads into the manifest. The function receives all newly personalized ad breaks from that pass in a single invocation, so you can implement cross-break logic.

The hook fires for all streaming protocols (HLS and DASH) and all playback modes (live, VOD, and pre-roll). Each ad break is personalized exactly once: the hook doesn't fire again when MediaTailor renders the same ad break in later manifest requests, and requests that personalize no new ad breaks don't invoke the hook.

## Input
<a name="monetization-functions-hooks-pmi-input"></a>

`event.*` and `session.*` (the same fields as `POST_ADS_RESPONSE`), plus `avails.*`, an array with one entry per newly personalized ad break, including each ad break's selected ads and skipped ads. For all available fields, see [Input field reference](monetization-functions-hooks.md#monetization-functions-hooks-input-ref).

## Output namespace allowed
<a name="monetization-functions-hooks-pmi-output"></a>


| Namespace | Accepted types | How the output is used | 
| --- | --- | --- | 
| avails.avails | Array of ad break objects | Replaces the ad list of each returned ad break. For each ad break, MediaTailor derives keep, reorder, and remove decisions from the returned ads array by matching adId. Entries with an unrecognized adId are treated as injections. | 
| temp.\* | Any | Temporary data for passing values between steps in an executor. Not persisted. | 

Return each ad break with the `ads` array you want inserted. Echo the ad objects you keep, omit the ones you remove, and reorder as needed. The same array-coercion rule as `POST_ADS_RESPONSE` applies: always wrap filter expressions in an array constructor, or an empty result silently leaves the ad break unchanged.

**Injecting an ad** — an entry whose `adId` is not in the original ad break is an injection. On injected entries, MediaTailor honors these fields: `adId`, `creativeUrl`, `durationSeconds`, `vastAdId`, `creativeId`, and `trackingEvents`. The field for specifying an injected creative is `creativeUrl`. Ads you read from the input expose their creative as `mediaUrl`. There are two ways to specify the creative:
+ **Explicit `creativeUrl`** — provide the URL of the creative to insert. If MediaTailor has already transcoded the creative, the injection succeeds immediately. Examples of already-transcoded creatives are a creative from an earlier ad break, or a `skippedAds[].creativeUrl` value whose `reason` is not transcode-related. If the creative is not yet transcoded, MediaTailor drops the injection for the current ad break rather than waiting, but the attempt initiates transcoding of the creative. Injecting the same URL into a later ad break succeeds after transcoding completes, the same way an untranscoded ad from your ADS is skipped at first and inserted in later ad breaks.
+ **`vastAdId` auto-hydration** — if your function chain includes a `VAST_REQUEST` call in the same hook invocation, inject with just the `vastAdId` of a parsed ad and omit `creativeUrl`. MediaTailor then selects the best media file from the ad's full media file list, using the same selection logic as the normal ad insertion path. It also registers new streaming creatives for transcoding so they are available in future ad breaks. If you provide both, `creativeUrl` wins. If neither matches, MediaTailor drops the injection. For more information, see [How parsed ads integrate with hook outputs](monetization-functions-types-vast-request.md#monetization-functions-types-vast-request-store).

The following rules apply:
+ At most 10 ads can be injected per invocation, across all ad breaks. MediaTailor drops injections beyond the limit.
+ If an ad break changed, MediaTailor reruns its fill policy with the normal duration tolerance. Ads that overflow the ad break are trimmed.
+ Ad breaks with `mutable` set to `false` (for example, overlay ad breaks, suppressed ad breaks, and live ad breaks the viewer joined mid-break) ignore modifications and render unchanged. This hook can't override avail suppression.
+ Injected ads go through the same variant-matching rules as ads from the ADS. An injected ad whose renditions don't match the stream is dropped.
+ Injections are idempotent (repeatable without duplicating results) across manifest requests. MediaTailor reconciles by creative identity, so an injected ad persists without duplicating.

## Typical use cases
<a name="monetization-functions-hooks-pmi-use-cases"></a>
+ Detect underfilled ad breaks with `fillRate` and inject house ads or promos fetched with a `VAST_REQUEST` function.
+ Remove or deduplicate ads across all ad breaks in the invocation, for example enforcing that a creative appears in only one ad break.
+ Remove a specific ad from the final ad set just before it is written to the manifest.
+ Re-insert an ad that was skipped earlier, using its `skippedAds[].creativeUrl`.

## Failure behavior
<a name="monetization-functions-hooks-pmi-failure"></a>

If a function attached to `PRE_MANIFEST_INSERTION` fails for any reason, such as a timeout, an expression error, or invalid output, MediaTailor discards the function's output. The originally selected ads are written into the manifest, as if no function were attached. If the serialized input exceeds the input size limit, MediaTailor skips the hook invocation entirely. For the limits that apply, see [Limits](monetization-functions-limits.md).