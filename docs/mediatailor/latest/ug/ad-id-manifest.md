# Manifests and ad metadata insertion

During the ad stitching process, MediaTailor adds to the manifest the unique ID associated
with each creative being stitched. MediaTailor obtains the unique ID of the creative from the
`id` attribute value of that creative in the VAST response. If the
creative lacks an ID attribute value, MediaTailor will publish an empty value
(`id=""`).

MediaTailor uses an in-manifest metadata signal to decouple dependencies between the client
tracking API for ad creative metadata and timing/positioning within the overall
timeline. This decoupling reduces playback latency (especially in VOD scenarios), where
the player's user interface (UI) renders ad break positions in the timeline prior to
initializing playback.

The added metadata takes the following forms:

- For HLS manifests, the added metadata takes the form of `DATERANGE`
  tags for each ad in the avail period.
- For DASH manifests, the added metadata takes the form of an `Event`
  element within each ad period.
  The following JSON message body shows an example VAST response:

```
{
  "version": 1,
  "identifiers": [
    {
      "scheme": "urn:smpte:ul:060E2B34.01040101.01200900.00000000",
      "value": "`creativeId`",
      "ad_position": "`adId`",
      "ad_type": "`adType`",
      "tracking_uri": "`trackingUri`",
      "custom_vast_data":"`customVastData`"
    }
  ]
}
```

In the preceding example:

- `creativeId` is the `Id` attribute value
  of the `Creative` element for the ad
- `adId` is either the HLS sequence number associated
  with the beginning of the ad, or the DASH period ID of the ad
- `adType` is either `avail` or
  `overlay`, based on the VAST response
- `trackingUri` is the relative tracking endpoint for
  the MediaTailor session, in the format
  `../../../../tracking/`hashed-account-id`/`origin-id`/`session-id``
- `customVastData` is a value that MediaTailor extracts from
  the `creative_signaling` VAST extension. MediaTailor uses the contents of
  the CDATA node, if present. See the [Ad Decision Server (ADS) interactions](ad-id-ads-interactions.md "ad-id-ads-interactions.md") section for more details and a
  sample VAST response.
