

# Example 4: Testing APS directly (Postman / curl)
<a name="yield-optimization-examples-apstest"></a>

Use this example to test the APS endpoint directly outside of MediaTailor to verify that your Publisher ID and bid parameters produce a valid response. Paste this into Postman or use `curl` to confirm APS is returning bids before configuring your MediaTailor template.

## Endpoint
<a name="yield-optimization-examples-apstest-endpoint"></a>

```
POST https://emt-ortb-iad.stv.bid-na.ads.aps.amazon-adsystem.com/stv/ortb/ads
Content-Type: application/json
```

**Note**  
This is the `AMERICAS` region endpoint (`iad` = US East). For other regions, the hostname changes accordingly.

## Working bid request
<a name="yield-optimization-examples-apstest-request"></a>

Replace the placeholder values marked with `<YOUR_VALUE>` with your actual values. All other fields are valid working examples.

```
{
  "id": "test-request-001",
  "imp": [
    {
      "id": "test_imp_1",
      "video": {
        "mimes": ["video/mp4", "video/H264"],
        "minduration": 15,
        "maxduration": 30,
        "protocols": [1, 2, 3, 4, 5, 6, 7, 8],
        "w": 1920,
        "h": 1080,
        "placement": 1,
        "linearity": 1,
        "sequence": 1,
        "minbitrate": 240,
        "maxbitrate": 30000,
        "playbackmethod": [1],
        "delivery": [1, 2],
        "maxseq": 5,
        "poddur": 120,
        "podid": "1",
        "podseq": 0,
        "plcmt": 1
      },
      "tagid": "test_imp_1",
      "bidfloor": 1.5,
      "secure": 1
    }
  ],
  "app": {
    "id": "<YOUR_APP_ID>",
    "name": "<YOUR_APP_NAME>",
    "bundle": "<YOUR_APP_BUNDLE_ID>",
    "domain": "<YOUR_APP_DOMAIN>",
    "storeurl": "<YOUR_APP_STORE_URL>",
    "pagecat": ["IAB12"],
    "publisher": {
      "id": "<YOUR_APS_PUBLISHER_ID>"
    },
    "content": {
      "genre": "Sports",
      "cat": ["IAB12"],
      "prodq": 1,
      "context": 1,
      "contentrating": "TV-G",
      "livestream": 1,
      "language": "en"
    }
  },
  "device": {
    "ua": "Dalvik/5.36.0 (Linux; U; FIRE; en-US; Amazon Model/AFTHA004 OS/9)",
    "geo": {
      "country": "USA",
      "region": "LA",
      "metro": "622",
      "city": "Metairie",
      "zip": "70001"
    },
    "dnt": 0,
    "lmt": 0,
    "ip": "<YOUR_CLIENT_IP>",
    "devicetype": 3,
    "make": "Amazon",
    "model": "AFFT",
    "os": "Android",
    "osv": "5.0",
    "ifa": "<YOUR_CLIENT_IFA>"
  },
  "at": 1,
  "tmax": 1850,
  "source": {
    "tid": "test-transaction-001"
  },
  "regs": {
    "ext": {
      "gdpr": 0,
      "us_privacy": "1YNY"
    }
  }
}
```

## Field annotations
<a name="yield-optimization-examples-apstest-annotations"></a>

The table below explains what each field represents and how it maps to what MediaTailor would set in production:


| Field | Who sets it | Notes | 
| --- | --- | --- | 
| id | MediaTailor (hardcoded) | In production, auto-generated as {sessionId}\_{availId}. For testing, use any unique string. | 
| imp[0].video.minduration | MediaTailor (hardcoded) | Set from your MinimumUnfilledDuration config. Use 15 for testing. | 
| imp[0].video.maxduration | MediaTailor (hardcoded) | Calculated from unfilled break duration. Use 30 for testing. | 
| imp[0].video.maxseq | MediaTailor (hardcoded) | Calculated: floor(unfilled\_duration / 6). Use 5 for testing. | 
| imp[0].video.poddur | MediaTailor (hardcoded) | Unfilled break duration. Use 120 for testing. | 
| imp[0].video.mimes | Your template | Supported video formats. ["video/mp4"] is sufficient. | 
| imp[0].video.protocols | Your template | VAST protocol versions. [1,2,3,4,5,6,7,8] for maximum compatibility. | 
| imp[0].video.w / h | Your template | Video resolution. Match your stream output. | 
| imp[0].bidfloor | Your template | Minimum CPM. Lower = more bids returned. | 
| app.publisher.id | MediaTailor (hardcoded) | Your APS Publisher ID from console config. Replace with yours. | 
| app.bundle | Your template (mandatory) | Your app's bundle/ASIN. Replace with yours. | 
| app.storeurl | Your template (mandatory) | Your app store listing URL. Replace with yours. | 
| app.content.\* | Your template | Content metadata for targeting. Improves bid quality. | 
| device.ua | Your template (mandatory) | In production, from {{session.user\_agent}}. For testing, use a real device UA. | 
| device.ip | Your template (mandatory) | In production, from {{session.client\_ip}}. For testing, use a real US IP. | 
| device.geo.\* | Passed through | Optional geolocation. APS can also derive from IP. | 
| device.ifa | Your template | Device advertising ID. Improves targeting. | 
| regs.ext.us\_privacy | Your template | CCPA string. Use GPP (regs.gpp) in production for better fill. | 
| at | Passed through | Auction type. 1 = first price. | 
| tmax | Passed through | Max response wait time (ms). APS typically responds in <200ms. | 

## Expected response
<a name="yield-optimization-examples-apstest-response"></a>

A successful response (HTTP 200) returns a `seatbid` array with one or more bids. Each bid contains:
+ `price`: CPM bid price (for example, `5.00`).
+ `adm`: VAST XML containing the ad creative (Wrapper or InLine).
+ `adomain`: Advertiser domain (for example, `["landofrost.com"]`).
+ `dur`: Ad duration in seconds.
+ `cat`: IAB content category.
+ `ext.dsrc`: Demand source (for example, `"ADSP"` for Amazon DSP).

If you receive HTTP **204**, APS has no matching bids. This usually means:
+ The `publisher.id` is invalid or not active.
+ The `app.bundle` / `app.storeurl` don't match a registered app.
+ The `bidfloor` is too high for available demand.
+ The `device.ip` is outside APS coverage.

## curl example
<a name="yield-optimization-examples-apstest-curl"></a>

```
curl -X POST \
  'https://emt-ortb-iad.stv.bid-na.ads.aps.amazon-adsystem.com/stv/ortb/ads' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "test-request-001",
  "imp": [{"id": "test_imp_1", "video": {"mimes": ["video/mp4"], "minduration": 15, "maxduration": 30, "protocols": [1,2,3,4,5,6,7,8], "w": 1920, "h": 1080, "maxseq": 5, "poddur": 120, "podid": "1", "plcmt": 1}, "bidfloor": 1.5, "secure": 1}],
  "app": {"bundle": "<YOUR_BUNDLE>", "storeurl": "<YOUR_STORE_URL>", "publisher": {"id": "<YOUR_PUBLISHER_ID>"}, "content": {"genre": "Sports", "livestream": 1, "language": "en"}},
  "device": {"ua": "Dalvik/5.36.0 (Linux; U; FIRE; en-US; Amazon Model/AFTHA004 OS/9)", "ip": "98.172.189.170", "devicetype": 3, "make": "Amazon", "model": "AFFT", "os": "Android"},
  "at": 1, "tmax": 1850,
  "regs": {"ext": {"gdpr": 0, "us_privacy": "1YNY"}}
}'
```