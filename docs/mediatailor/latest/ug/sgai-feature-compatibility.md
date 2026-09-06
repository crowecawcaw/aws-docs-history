

# MediaTailor server-guided ad insertion feature compatibility matrix
<a name="sgai-feature-compatibility"></a>

AWS Elemental MediaTailor offers two ad insertion methods with different feature compatibility. Server-guided ad insertion works differently from server-side ad insertion, which affects compatibility with some MediaTailor features. Use this table to understand which features work with each ad insertion method.


**Feature compatibility by ad insertion method**  

| Feature | Server-side ad insertion (SSAI) | Server-guided ad insertion (SGAI) | 
| --- | --- | --- | 
| Ad prefetching | ✓ Supported | Not yet supported | 
| Ad suppression | ✓ Supported | Not applicable | 
| Pre-roll ad behavior | Controlled by MediaTailor configuration | Controlled by MediaTailor configuration | 
| Client-side ad tracking | Uses GetTracking API | Uses TRACKING section in asset list (GetTracking API is not used) | 
| Server-side ad tracking | ✓ Supported — beacons fire based on /v1/segment requests using the session ID | ✓ Supported (HLS only) — uses sessionless beaconing with encrypted beacon data embedded in ad URIs via \#EXT-X-DEFINE:QUERYPARAM. Requires HLS v11 or later. DASH is not yet supported. | 
| Ad-ID decoration | ✓ Supported | ✗ Not compatible | 

## Compatibility details
<a name="compatibility-details"></a>

### Ad prefetching
<a name="prefetch-compatibility"></a>

Ad prefetching isn't currently supported.

### Ad suppression
<a name="prefetch-compatibility"></a>

Ad suppression isn't supported with server-guided ad insertion methods because players only fetch ads they're going to play. 

### Pre-roll ad behavior
<a name="preroll-compatibility"></a>

Pre-roll ad timing works differently between insertion methods:
+ **Server-side ad insertion:** MediaTailor controls when pre-roll ads play based on configuration settings
+ **Server-guided ad insertion:** MediaTailor inserts pre-roll ads at the top of the manifest. Your player shows these ads first, then starts your content

### Ad tracking
<a name="tracking-compatibility"></a>

**Client-side tracking** uses different mechanisms depending on the ad insertion method:
+ **Server-side ad insertion (SSAI):** Uses the `GetTracking` API endpoint
+ **Server-guided ad insertion (SGAI):** MediaTailor provides tracking information in the `TRACKING` section of each asset list response. The `GetTracking` API endpoint is not used. The session initialization response does not include a `trackingUrl`.

**Server-side tracking** also differs between methods:
+ **Server-side ad insertion (SSAI):** MediaTailor fires beacons when the player fetches stitched ad segments through `/v1/segment/` using the session ID.
+ **Server-guided ad insertion (SGAI):** MediaTailor uses sessionless beaconing. MediaTailor embeds encrypted beacon data (`awsBeaconData`, `awsBeaconDomain`, `awsConfigurationName`) in the ad manifest URIs that it returns in the asset list. The ad manifest uses `#EXT-X-DEFINE:QUERYPARAM` tags so the player substitutes these values into segment URLs. When the player requests each ad segment, MediaTailor decrypts the data, fires the appropriate beacon, and redirects to the content segment. When server-side reporting is active, MediaTailor omits the `TRACKING` section from the asset list response. For details, see [Server-side tracking with server-guided ad insertion (SGAI)](ad-reporting-server-side-sgai.md).

### Ad-ID decoration
<a name="ad-id-compatibility"></a>

Ad-ID decoration is not compatible with server-guided ad insertion because the fields that populate X-AD-CREATIVE-SIGNALING headers are only known when the asset list is fetched, not when the manifest is written.