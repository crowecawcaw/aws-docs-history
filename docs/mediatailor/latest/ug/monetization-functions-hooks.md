

# Functions lifecycle hooks
<a name="monetization-functions-hooks"></a>

A lifecycle hook defines when MediaTailor runs your function during playback. This page is a complete reference for input fields, output namespaces, and the rules that govern data flow at each hook.

## Overview
<a name="monetization-functions-hooks-overview"></a>

MediaTailor supports four lifecycle hooks:
+ **`PRE_SESSION_INITIALIZATION`** fires once when a viewer starts a new session. Use it for one-time setup work such as fetching audience segments. At this point, no ad break has occurred, so ad break context is not available.
+ **`PRE_ADS_REQUEST`** fires before every ad decision server (ADS) request — once per ad break in the stream. Use it to customize the ADS request with targeting data, modify the ADS URL, or add headers.
+ **`POST_ADS_RESPONSE`** fires after MediaTailor receives and parses the ADS response, including resolution of Video Ad Serving Template (VAST) wrapper redirects. Use it to filter, reorder, modify, or supplement the ads that the ADS returned, before MediaTailor selects ads to insert.
+ **`PRE_MANIFEST_INSERTION`** fires at the end of ad break personalization, after ad selection, transcode checks, and fill policy, immediately before MediaTailor writes ads into the manifest. Use it to inspect or modify the final ad set, including injecting additional ads into underfilled ad breaks.

The hooks differ in timing and scope. `PRE_SESSION_INITIALIZATION` runs once and sets up data that persists for the entire session. `PRE_ADS_REQUEST` and `POST_ADS_RESPONSE` run around each ADS interaction. `PRE_ADS_REQUEST` shapes the outgoing request, and `POST_ADS_RESPONSE` acts on the parsed response before ad selection. `PRE_MANIFEST_INSERTION` runs after selection is complete and sees the final ad set for all newly personalized ad breaks in a single invocation.

**Important**  
The `PRE_ADS_REQUEST`, `POST_ADS_RESPONSE`, and `PRE_MANIFEST_INSERTION` hooks share a combined execution budget of 2,000 ms for a single request. This budget is in addition to each hook's own 2,000 ms timeout. A hook's effective timeout is the smaller of its own timeout and the remaining budget. Time spent by an earlier hook reduces the time available to later hooks in the same request. If the remaining budget is exhausted before a hook starts, MediaTailor skips that hook and continues processing the request without it. `PRE_SESSION_INITIALIZATION` runs during session initialization and is not part of the combined budget. For more information, see [Limits](monetization-functions-limits.md).

**Note**  
In this documentation, an ad break is also called an *avail*. Input field names (such as `avail.availId` and `avails.avails`) and CloudWatch metrics use the `avail` form.

## Input field reference
<a name="monetization-functions-hooks-input-ref"></a>

The following table lists the input fields available at each lifecycle hook. In the Field column, `parent[].child` notation indicates a field of each element in the `parent` array.

**Note**  
The `POST_ADS_RESPONSE` and `PRE_MANIFEST_INSERTION` hooks expose session fields in camelCase (for example, `session.clientIp`), while the first two hooks use snake\_case (for example, `session.client_ip`). Player parameters are available through the `player_params` namespace at the first two hooks and as the `session.playerParams` object at the other two.


| Field | Type | PRE\_SESSION\_INITIALIZATION | PRE\_ADS\_REQUEST | POST\_ADS\_RESPONSE | PRE\_MANIFEST\_INSERTION | 
| --- | --- | --- | --- | --- | --- | 
| session.id | Long | ✓ | ✓ | ✓ | ✓ | 
| session.uuid | String | ✓ | ✓ | ✓ | ✓ | 
| session.client\_ip | String | ✓ | ✓ | ✗ | ✗ | 
| session.clientIp | String | ✗ | ✗ | ✓ | ✓ | 
| session.user\_agent | String | ✓ | ✓ | ✗ | ✗ | 
| session.userAgent | String | ✗ | ✗ | ✓ | ✓ | 
| session.referer\* | String | ✓ | ✓ | ✗ | ✗ | 
| session.avail\_duration\_secs | Long | ✗ | ✓ | ✗ | ✗ | 
| session.avail\_duration\_ms | Long | ✗ | ✓ | ✗ | ✗ | 
| session.streamingProtocol | String | ✗ | ✗ | ✓ | ✓ | 
| session.playerParams | Object | ✗ | ✗ | ✓ | ✓ | 
| player\_params.\* | String | ✓ | ✓ | ✗ | ✗ | 
| event.id | String | ✓ | ✓ | ✓ | ✓ | 
| event.hook | String | ✓ | ✓ | ✓ | ✓ | 
| event.timestamp | String | ✓ | ✓ | ✓ | ✓ | 
| avail.index | Int | ✗ | ✓ | ✗ | ✗ | 
| avail.random | Long | ✗ | ✓ | ✗ | ✗ | 
| avail.source\_content\_time\_epoch\_ms | Long | ✗ | ✓ | ✗ | ✗ | 
| avail.availId† | String | ✗ | ✗ | ✓ | ✗ | 
| avail.durationSeconds† | Number | ✗ | ✗ | ✓ | ✗ | 
| avail.startTime† | String | ✗ | ✗ | ✓ | ✗ | 
| scte.event\_id | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.avail\_num | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.segmentation\_event\_id | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.segmentation\_type\_id | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.segmentation\_upid | String | ✗ | ✓ | ✗ | ✗ | 
| scte.segmentation\_upid.assetId | String | ✗ | ✓ | ✗ | ✗ | 
| scte.segmentation\_upid.cueData.key | String | ✗ | ✓ | ✗ | ✗ | 
| scte.segmentation\_upid.cueData.value | String | ✗ | ✓ | ✗ | ✗ | 
| scte.unique\_program\_id | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.archive\_allowed\_flag | Boolean | ✗ | ✓ | ✗ | ✗ | 
| scte.delivery\_not\_restricted\_flag | Boolean | ✗ | ✓ | ✗ | ✗ | 
| scte.device\_restrictions | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.no\_regional\_blackout\_flag | Boolean | ✗ | ✓ | ✗ | ✗ | 
| scte.segment\_num | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.segments\_expected | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.sub\_segment\_num | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.sub\_segments\_expected | Int | ✗ | ✓ | ✗ | ✗ | 
| scte.avails\_expected | Long | ✗ | ✓ | ✗ | ✗ | 
| asset.\* | String | ✗ | ✓ | ✗ | ✗ | 
| inference.enriched | Boolean | ✗ | ✓ | ✗ | ✗ | 
| inference.feedId | String | ✗ | ✓ | ✗ | ✗ | 
| inference.dataEndpoint | String | ✗ | ✓ | ✗ | ✗ | 
| inference.pts | Long | ✗ | ✓ | ✗ | ✗ | 
| inference.timescale | Long | ✗ | ✓ | ✗ | ✗ | 
| inference.region | String | ✗ | ✓ | ✗ | ✗ | 
| inference.previousBreakEndPts | Long | ✗ | ✓ | ✗ | ✗ | 
| inference.parseError | Boolean | ✗ | ✓ | ✗ | ✗ | 
| adsRequest.url | String | ✗ | ✓ | ✓ | ✗ | 
| adsRequest.method | String | ✗ | ✓ | ✓ | ✗ | 
| adsRequest.headers.<key> | String | ✗ | ✓ | ✓ | ✗ | 
| adsRequest.body | String | ✗ | ✓ | ✗ | ✗ | 
| adsResponse.responseType | String | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads | Array | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].adId‡ | String | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].durationSeconds | Number | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].adSystem | String | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].adTitle | String | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].creativeId | String | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].sequence | Int | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].mediaFiles | Array | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].mediaFiles[].url | String | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].mediaFiles[].mimeType | String | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].mediaFiles[].width | Int | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].mediaFiles[].height | Int | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].mediaFiles[].bitrate | Int | ✗ | ✗ | ✓ | ✗ | 
| adsResponse.ads[].trackingEvents.<eventType> | Array of String | ✗ | ✗ | ✓ | ✗ | 
| avails.avails | Array | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].availId | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].durationSeconds | Number | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].startTime | Number | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].mediaProtocol | String (HLS \| DASH) | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].streamingMode | String (LIVE \| VOD) | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].fillDurationSeconds | Number | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].fillRate | Number (0–1) | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].mutable | Boolean | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads | Array | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].adId§ | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].vastAdId | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].creativeId | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].insertionUuid | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].sequenceInAvail | Int | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].durationSeconds | Number | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].adSystem¶ | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].adTitle¶ | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].mediaUrl | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].trackingEvents.<eventType> | Array of String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].ads[].mediaFiles | Array | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].skippedAds | Array | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].skippedAds[].adId | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].skippedAds[].vastAdId | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].skippedAds[].durationSeconds | Number | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].skippedAds[].creativeUrl | String | ✗ | ✗ | ✗ | ✓ | 
| avails.avails[].skippedAds[].reason | String | ✗ | ✗ | ✗ | ✓ | 

\* `session.referer` is only present when a Referer header is included in the session initialization request. Use `$exists(session.referer)` to check before accessing.

† The `avail` namespace is present only when the ADS response applies to a single ad break. It is not present for multi-break (VMAP) responses or prefetched responses. Use `$exists(avail)` to check before accessing.

‡ At `POST_ADS_RESPONSE`, `adId` is the `id` attribute of the VAST `<Ad>` element.

§ At `PRE_MANIFEST_INSERTION`, `adId` is an internal placement identifier. It is stable for an ad within its ad break, but it is not the VAST ad ID and is not comparable across ad breaks or across hooks. For identity checks that span ad breaks or hooks, use `vastAdId` (the `id` attribute of the VAST `<Ad>` element) or `creativeId`.

¶ On DASH VOD streams, `adTitle` and `adSystem` are `null` at this hook. Use `vastAdId` or `creativeId` in predicates there.