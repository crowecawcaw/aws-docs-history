

# Server-side tracking with server-guided ad insertion (SGAI)
<a name="ad-reporting-server-side-sgai"></a>

When you use server-guided ad insertion (SGAI), server-side tracking uses a *sessionless beaconing* mechanism that differs from the stitched-mode approach described above. Instead of MediaTailor stitching ad segments into the content manifest (where it tracks `/v1/segment` requests), SGAI returns ad references as separate playlists in an asset list response with beacon metadata embedded in the ad URIs.

## How sessionless server-side beaconing works
<a name="ad-reporting-server-side-sgai-how-it-works"></a>

The following steps describe how server-side beaconing works for SGAI sessions:

1. **Session initialization**: The player requests the HLS multivariant playlist with `aws.insertionMode=GUIDED`. Server-side reporting is the default (no `aws.reportingMode` parameter is needed). Unlike stitched mode, the session initialization response does *not* include a `trackingUrl`.

1. **Cacheable manifest**: MediaTailor returns a cacheable manifest containing `EXT-X-DATERANGE` tags with `CLASS="com.apple.hls.interstitial"` and `X-ASSET-LIST` attributes pointing to the MediaTailor interstitial asset list endpoint.

1. **Asset list with beacon metadata**: When the player encounters an ad break, it fetches the asset list. MediaTailor returns a JSON response where each ad URI includes encrypted beacon metadata:

   ```
   {
     "ASSETS": [
       {
         "DURATION": 30.0,
         "URI": "https://cdn.example.com/ad/master.m3u8?awsBeaconData=<encrypted>&awsBeaconDomain=<MediaTailor-endpoint>&awsConfigurationName=<config-name>"
       }
     ]
   }
   ```

   When server-side reporting is active, the response does *not* include a `TRACKING` section. The ad URIs carry all beacon data.

1. **HLS variable substitution**: The player fetches the ad multivariant playlist. The ad manifest uses `#EXT-X-DEFINE:QUERYPARAM` directives to pass the beacon parameters from the URI query string into segment URLs via HLS variable substitution:

   ```
   #EXTM3U
   #EXT-X-DEFINE:QUERYPARAM="awsBeaconData"
   #EXT-X-DEFINE:QUERYPARAM="awsBeaconDomain"
   #EXT-X-DEFINE:QUERYPARAM="awsConfigurationName"
   #EXTINF:5.0,
   {$awsBeaconDomain}/segment/hash/{$awsConfigurationName}/{$awsBeaconData}/0/0?aws.segmentRelativePath=asset_00001.ts
   ```

   The player resolves the `{$awsBeaconData}`, `{$awsBeaconDomain}`, and `{$awsConfigurationName}` variables using the values from the ad manifest URI query string, and then requests each ad segment through MediaTailor.

1. **Beacon firing on segment request**: As the player requests each ad segment, the request routes through MediaTailor. The service decrypts the beacon data, determines the segment's position within the ad (impression, first quartile, midpoint, third quartile, or complete), and fires the appropriate VAST tracking beacon to the ad server. MediaTailor then redirects the player to the actual ad content segment.

## Player requirements for SGAI server-side beaconing
<a name="ad-reporting-server-side-sgai-requirements"></a>

To use server-side beaconing with SGAI, your player must meet the following requirements:
+ HLS version 11 or later
+ Support for `EXT-X-DATERANGE` with `CLASS` attribute for HLS Interstitials
+ Support for `#EXT-X-DEFINE:QUERYPARAM` variable substitution (RFC 8216bis). The player must percent-decode the query parameter values before substituting them into segment URLs.

**Note**  
SGAI server-side beaconing is currently supported for HLS only. DASH is not yet supported for SGAI server-side beaconing.

## Comparison with stitched-mode server-side tracking
<a name="ad-reporting-server-side-sgai-comparison"></a>

The following table summarizes how server-side tracking differs between stitched and server-guided ad insertion:


| Aspect | Stitched (SSAI) | Server-guided (SGAI) | 
| --- | --- | --- | 
| Manifest cacheability | Per-session, not cacheable | Cacheable, shared across viewers | 
| Ad segment routing | Through /v1/segment/ using the session ID | Through /v1/segment/ using an encrypted beacon data blob | 
| Session state for beacons | Stored per session in MediaTailor | Sessionless — all state is carried in the encrypted awsBeaconData parameter | 
| Tracking URL at session init | Returned in the session initialization response | Not provided — beacon data is embedded in ad URIs in each asset list response | 
| DASH support | Supported | Not yet supported | 

**Note**  
For live SGAI sessions, you can enable manifest-based ad prefetching using `aws.guidedPrefetchMode=MANIFEST`. This is separate from the schedule-based prefetch API used with stitched (SSAI) sessions. For details, see [Guided prefetch with manifest heartbeating](sgai-guided-prefetch.md).