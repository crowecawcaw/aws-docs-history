

# ORTB field reference
<a name="yield-optimization-ortb-reference"></a>

This page is a complete reference for every field in the OpenRTB bid request. Fields are categorized by how MediaTailor handles them and whether APS requires or recommends them for optimal ad fill.

For the full OpenRTB 2.6 specification, see the [IAB OpenRTB 2.6 spec](https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md).

## Field categories
<a name="yield-optimization-ortb-reference-categories"></a>


| Category | Meaning | Your action | 
| --- | --- | --- | 
| Mandatory | Must be present in your template. MediaTailor throws an error if missing. | You must provide these. | 
| Hardcoded by EMT | MediaTailor always sets these using values from your console configuration or the current avail context. Your template values are overridden. | Do not set these in your template. | 
| APS Recommended | Not strictly required by MediaTailor, but APS recommends these for better ad fill and targeting. Missing recommended fields may result in lower fill rates or no-bid responses. | Strongly recommended. | 
| Optional | Included in the bid request only if you provide them. No default value. | Provide if relevant to your use case. | 

## `app` object
<a name="yield-optimization-ortb-reference-app"></a>


| Field | Category | Notes | 
| --- | --- | --- | 
| app | Mandatory | The app object must exist in your template. | 
| app.bundle | Mandatory | Your app's bundle ID (for example, G15147002586). Must not be empty. | 
| app.storeurl | Mandatory | App store URL (for example, https://apps.apple.com/us/app/yourapp/id123). | 
| app.publisher.id | Hardcoded by EMT | Always set to your PublisherId from the console configuration. | 
| app.content | Mandatory (object) | MediaTailor sends an empty Content object if you omit this. Provide content metadata for better targeting. | 
| app.name | APS Recommended | App name for identification. | 
| app.id | APS Recommended | Your app identifier in APS. | 
| app.domain | APS Recommended | App domain. | 
| app.content.genre | APS Recommended | Content genre (for example, "Sport", "News"). | 
| app.content.contentrating | APS Recommended | Content rating (for example, "TV-G", "TV-14"). | 
| app.content.language | APS Recommended | Content language (ISO-639-1). | 
| app.content.id | APS Recommended | Content identifier. | 
| app.content.title | APS Recommended | Content title. | 
| app.content.episode | APS Recommended | Episode number. | 
| app.content.len | APS Recommended | Content length in seconds. | 
| app.cat | Optional | Content categories (IAB taxonomy). | 
| app.sectioncat | Optional | Section categories. | 
| app.pagecat | Optional | Page categories. | 
| app.ver | Optional | App version. | 
| app.privacypolicy | Optional | 1 = has privacy policy. | 
| app.paid | Optional | 1 = paid app. | 
| app.keywords | Optional | Comma-separated keywords. | 
| app.kwarray | Optional | Keywords as array. | 
| app.inventorypartnerdomain | Optional | Inventory partner domain. | 
| app.ext | Optional | Extension object (pass-through). | 

## `device` object
<a name="yield-optimization-ortb-reference-device"></a>


| Field | Category | Notes | 
| --- | --- | --- | 
| device | Mandatory | The device object must exist in your template. | 
| device.ua | Mandatory | User agent string. Must not be empty. Use {{session.user\_agent}}. | 
| device.ip | Mandatory | IPv4 address. Must not be empty. Use {{session.client\_ip}}. | 
| device.lmt | Optional (default: 0) | Limit Ad Tracking flag. 0 = tracking allowed, 1 = tracking limited. If not provided in your template, defaults to 0. | 
| device.devicetype | Hardcoded by EMT (default: 3) | MediaTailor sets 3 (Connected TV) if not provided. Your value is used if present. | 
| device.make | APS Recommended | Device manufacturer (for example, "Samsung", "Apple"). | 
| device.model | APS Recommended | Device model (for example, "Tizen TV", "iPhone"). | 
| device.os | APS Recommended | Operating system (for example, "Tizen", "iOS"). | 
| device.osv | APS Recommended | OS version. | 
| device.h | APS Recommended | Screen height in pixels. | 
| device.w | APS Recommended | Screen width in pixels. | 
| device.language | APS Recommended | Device language (ISO-639-1). | 
| device.ifa | APS Recommended | Device advertising ID. Not all devices have one (for example, web browsers). | 
| device.dnt | APS Recommended | Do Not Track flag. | 
| device.geo | Optional | Geo object with country, lat, lon. | 
| device.sua | Optional | Structured User Agent (UA-CH). | 
| device.ipv6 | Optional | IPv6 address. | 
| device.hwv | Optional | Hardware version. | 
| device.connectiontype | Optional | Connection type (WiFi, cellular, and so on). | 
| device.carrier | Optional | Carrier name. | 
| device.mccmnc | Optional | Mobile country/network code. | 
| device.ext | Optional | Extension object (pass-through). | 

## `imp` (impression) object
<a name="yield-optimization-ortb-reference-imp"></a>

Your template must contain exactly **one** `imp` object in an array.


| Field | Category | Notes | 
| --- | --- | --- | 
| imp[0].video | Mandatory | The video object must exist. | 
| imp[0].video.mimes | Mandatory | Supported MIME types (for example, ["video/mp4"]). | 
| imp[0].video.protocols | Optional | Supported VAST protocols. If omitted, MediaTailor uses hardcoded fallback [1, 2, 3, 4, 5, 6, 7, 8]. See the protocol enum reference below. | 
| imp[0].video.minduration | Hardcoded by EMT | Set to your MinimumUnfilledDuration from the console. | 
| imp[0].video.maxduration | Hardcoded by EMT | Set to the actual unfilled duration (seconds). | 
| imp[0].video.maxseq | Hardcoded by EMT | Calculated: floor(unfilled\_duration / 6). APS recommends either maxseq or poddur to return multiple ads. | 
| imp[0].video.poddur | Hardcoded by EMT | Set to the unfilled duration (seconds). | 
| imp[0].video.startdelay | Optional | Start delay. 0 = pre-roll, -1 = generic mid-roll, -2 = post-roll, > 0 = mid-roll offset in seconds. Use -1 for live mid-roll breaks. Hardcoded fallback: 6. | 
| imp[0].video.w | APS Recommended | Video width in pixels. | 
| imp[0].video.h | APS Recommended | Video height in pixels. | 
| imp[0].video.plcmt | APS Recommended | Placement type (1 = in-stream). | 
| imp[0].video.podid | APS Recommended | Pod identifier. | 
| imp[0].video.slotinpod | APS Recommended | Slot position in pod. | 
| imp[0].video.ext.slotId | Optional (default: "default\_slot\_id") | Your APS slot ID from the APS console. The default works but providing your actual slot ID allows APS to apply slot-specific targeting and floor pricing. | 
| imp[0].bidfloor | Optional (default: 1.0) | Minimum bid price in CPM. | 
| imp[0].secure | Optional (default: 1) | 1 = requires HTTPS creative URLs. | 
| imp[0].id | Optional | Impression ID. Auto-generated if not provided. | 
| imp[0].tagid | Optional | Tag/placement ID. | 
| imp[0].bidfloorcur | Optional | Bid floor currency (default USD). | 
| imp[0].ssai | Optional | SSAI indicator. | 
| imp[0].exp | Optional | Expiration time for the impression. | 
| imp[0].rqddurs | Optional | Requested durations array. | 
| imp[0].mincpmpersec | Optional | Minimum CPM per second. | 
| imp[0].pmp | Optional | Private marketplace object. | 
| imp[0].ext | Optional | Extension object (pass-through). | 

### Protocol enum reference
<a name="yield-optimization-ortb-reference-protocol-enum"></a>


| Value | Protocol | 
| --- | --- | 
| 1 | VAST 1.0 | 
| 2 | VAST 2.0 | 
| 3 | VAST 3.0 | 
| 4 | VAST 1.0 Wrapper | 
| 5 | VAST 2.0 Wrapper | 
| 6 | VAST 3.0 Wrapper | 
| 7 | VAST 4.0 | 
| 8 | VAST 4.0 Wrapper | 
| 9\+ | DAAST | 

## Top-level fields
<a name="yield-optimization-ortb-reference-top-level"></a>


| Field | Category | Notes | 
| --- | --- | --- | 
| id | Hardcoded by EMT | Auto-generated: {sessionId}\_{availId} format (for example, abc123-def456\_78901). Useful for correlating bid requests with session logs. | 
| cur | Optional (default: ["USD"]) | Allowed currencies. | 
| ext.integrationType | Hardcoded by EMT | Always set to "EMT". | 
| bcat | Optional | Blocked ad categories (IAB taxonomy). Your template value is sent as-is to APS. | 
| badv | Optional | Blocked advertiser domains. | 
| bapp | Optional | Blocked app bundle IDs. | 
| test | Optional | Test mode flag. | 
| at | Optional | Auction type. | 
| tmax | Optional | Maximum time (ms) to wait for bid response. | 
| wseat | Optional | Allowed buyer seats. | 
| bseat | Optional | Blocked buyer seats. | 
| wlang | Optional | Allowed creative languages. | 
| source | Optional | Source object for supply chain. | 
| ext | Optional | Your custom extension fields are merged with EMT's integrationType. | 

## `user` object
<a name="yield-optimization-ortb-reference-user"></a>


| Field | Category | Notes | 
| --- | --- | --- | 
| user | APS Recommended (EU) | Required for EU traffic with GDPR consent. | 
| user.consent | APS Recommended (EU) | GDPR consent string (TCF). | 
| user.id | Optional | User ID. | 
| user.buyeruid | Optional | Buyer-specific user ID. | 
| user.eids | Optional | Extended identifiers (LiveRamp, UID2, and so on). | 
| user.data | Optional | User data segments. | 
| user.ext | Optional | Extension object. | 

## `regs` object
<a name="yield-optimization-ortb-reference-regs"></a>


| Field | Category | Notes | 
| --- | --- | --- | 
| regs | APS Recommended | Include for regulatory compliance. | 
| regs.coppa | APS Recommended (US) | COPPA flag (1 = child-directed). | 
| regs.us\_privacy | APS Recommended (US) | US Privacy / CCPA string. | 
| regs.gdpr | APS Recommended (EU) | GDPR applies (1 = yes). | 
| regs.gpp | APS Recommended | Global Privacy Platform string. Preferred over us\_privacy for US audiences, results in better fill rates. See [Best practices](yield-optimization-best-practices.md). | 
| regs.gpp\_sid | APS Recommended | GPP section IDs (for example, [7] for US National). Required when gpp is present. | 
| regs.ext | Optional | Extension object. | 

## Next steps
<a name="yield-optimization-ortb-reference-next-steps"></a>
+ For copy-paste templates, see [Example templates](yield-optimization-examples.md).
+ For recommendations on maximizing fill rates, see [Best practices](yield-optimization-best-practices.md).