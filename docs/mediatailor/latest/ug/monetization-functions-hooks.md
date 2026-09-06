

# Functions lifecycle hooks
<a name="monetization-functions-hooks"></a>

A lifecycle hook defines when MediaTailor runs your function during playback. This page is a complete reference for input fields, output namespaces, and the rules that govern data flow at each hook.

## Overview
<a name="monetization-functions-hooks-overview"></a>

MediaTailor supports two lifecycle hooks:
+ **`PRE_SESSION_INITIALIZATION`** fires once when a viewer starts a new session. Use it for one-time setup work such as fetching audience segments. At this point, no ad break has occurred, so ad break context is not available.
+ **`PRE_ADS_REQUEST`** fires before every ad decision server (ADS) request — once per ad break in the stream. Use it to customize the ADS request with targeting data, modify the ADS URL, or add headers.

The key difference is timing: `PRE_SESSION_INITIALIZATION` runs once and sets up data that persists for the entire session, while `PRE_ADS_REQUEST` runs repeatedly and can tailor each ADS request to the specific ad break.

## Input field reference
<a name="monetization-functions-hooks-input-ref"></a>


| Field | Type | PRE\_SESSION\_INITIALIZATION | PRE\_ADS\_REQUEST | 
| --- | --- | --- | --- | 
| session.id | Long | ✓ | ✓ | 
| session.uuid | String | ✓ | ✓ | 
| session.client\_ip | String | ✓ | ✓ | 
| session.user\_agent | String | ✓ | ✓ | 
| session.referer\* | String | ✓ | ✓ | 
| session.avail\_duration\_secs | Long | ✗ | ✓ | 
| session.avail\_duration\_ms | Long | ✗ | ✓ | 
| player\_params.\* | String | ✓ | ✓ | 
| event.id | String | ✓ | ✓ | 
| event.hook | String | ✓ | ✓ | 
| event.timestamp | String | ✓ | ✓ | 
| avail.index | Int | ✗ | ✓ | 
| avail.random | Long | ✗ | ✓ | 
| avail.source\_content\_time\_epoch\_ms | Long | ✗ | ✓ | 
| scte.event\_id | Int | ✗ | ✓ | 
| scte.avail\_num | Int | ✗ | ✓ | 
| scte.segmentation\_event\_id | Int | ✗ | ✓ | 
| scte.segmentation\_type\_id | Int | ✗ | ✓ | 
| scte.segmentation\_upid | String | ✗ | ✓ | 
| scte.segmentation\_upid.assetId | String | ✗ | ✓ | 
| scte.segmentation\_upid.cueData.key | String | ✗ | ✓ | 
| scte.segmentation\_upid.cueData.value | String | ✗ | ✓ | 
| scte.unique\_program\_id | Int | ✗ | ✓ | 
| scte.archive\_allowed\_flag | Boolean | ✗ | ✓ | 
| scte.delivery\_not\_restricted\_flag | Boolean | ✗ | ✓ | 
| scte.device\_restrictions | Int | ✗ | ✓ | 
| scte.no\_regional\_blackout\_flag | Boolean | ✗ | ✓ | 
| scte.segment\_num | Int | ✗ | ✓ | 
| scte.segments\_expected | Int | ✗ | ✓ | 
| scte.sub\_segment\_num | Int | ✗ | ✓ | 
| scte.sub\_segments\_expected | Int | ✗ | ✓ | 
| scte.avails\_expected | Long | ✗ | ✓ | 
| asset.\* | String | ✗ | ✓ | 
| adsRequest.url | String | ✗ | ✓ | 
| adsRequest.method | String | ✗ | ✓ | 
| adsRequest.headers.<key> | String | ✗ | ✓ | 
| adsRequest.body | String | ✗ | ✓ | 

\* `session.referer` is only present when a Referer header is included in the session initialization request. Use `$exists(session.referer)` to check before accessing.