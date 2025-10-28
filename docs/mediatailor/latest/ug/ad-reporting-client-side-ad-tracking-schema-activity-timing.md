# Ad-tracking

activity timing

With client-side reporting, the player must emit tracking events (beacons) with a level of
precision. Using the MediaTailor client-side tracking schema, you can ensure that, for every avail,
ad, companion, overlay, and tracking events, timing and duration information is present, and in
different forms.

Use the following MediaTailor key/value pairs for the player to accurately reconcile ad-event
activities, such as tracking events, with playback position:

- [startTime](ad-reporting-client-side-ad-tracking-schema.md#property-starttime "ad-reporting-client-side-ad-tracking-schema.md#property-starttime")
- [startTimeInSeconds](ad-reporting-client-side-ad-tracking-schema.md#property-starttimeinseconds "ad-reporting-client-side-ad-tracking-schema.md#property-starttimeinseconds")
- [adProgramDateTime](ad-reporting-client-side-ad-tracking-schema.md#property-adprogramdatetime "ad-reporting-client-side-ad-tracking-schema.md#property-adprogramdatetime")
- [adID](ad-reporting-client-side-ad-tracking-schema.md#property-adid "ad-reporting-client-side-ad-tracking-schema.md#property-adid")/[eventId](ad-reporting-client-side-ad-tracking-schema.md#property-eventid "ad-reporting-client-side-ad-tracking-schema.md#property-eventid")
  HLS and DASH implement the value of `startTime` and
  `startTimeInSeconds` differently:

- HLS - The `startTime` values are relative to the beginning of the playback
  session. The beginning of the playback session is defined as time zero. The ad's
  `startTime` is the sum of the cumulative values of all the `EXT-INF`
  segment durations leading up to the avail. The media-sequence number of the segment that the
  ad or tracking event falls on also corresponds to the `adId` or
  `eventId` in the client-side tracking response.
- DASH:
  - Live/dynamic manifests - The `startTime` values are relative to the
    `MPD@availabilityStartTime` of the DASH manifest. The
    `MPD@avaibilityStartTime` is a timing anchor for all MediaTailor sessions that
    consume the stream.
  - VOD/static manifests - The `startTime` values are relative to the
    beginning of the playback session. The beginning of the playback session is defined as
    time zero. Each ad inside the avail is contained inside its own `Period`
    element. The `Period` element has a `@start` attribute with a
    value that's the same as the `startTime` values in the client-side tracking
    payload. The `PeriodId` also corresponds to the `adId` or
    `eventId` in the client-side tracking response.

###### Example : HLS

In the following example, the MediaTailor session started, and the following manifest is the
first one served to the client:

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:6
#EXT-X-MEDIA-SEQUENCE:4603263
#EXT-X-DISCONTINUITY-SEQUENCE:0
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:23.295678Z
#EXTINF:4.010667,
https://123.cloudfront.net/out/v1/index_1_34.ts
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:27.306345Z
#EXTINF:4.010667,
https://123.cloudfront.net/out/v1/index_1_35.ts
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:31.317012Z
#EXTINF:4.010667,
https://123.cloudfront.net/out/v1/index_1_36.ts
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:35.327679Z
#EXTINF:4.010667,
https://123.cloudfront.net/out/v1/index_1_37.ts
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:39.338346Z
#EXTINF:2.538667,
https://123.cloudfront.net/out/v1/index_1_38.ts
#EXT-X-DISCONTINUITY
#EXT-X-KEY:METHOD=NONE
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:41.453Z
#EXTINF:2.0,
https://123.cloudfront.net/tm/asset_1080_4_8_00001.ts
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:43.453Z
#EXTINF:2.0,
https://123.cloudfront.net/tm/asset_1080_4_8_00002.ts
#EXT-X-PROGRAM-DATE-TIME:2023-05-03T21:24:45.453Z
#EXTINF:2.0,
https://123.cloudfront.net/tm/asset_1080_4_8_00003.ts
```

In the client-side tracking JSON payload, the following values apply:

- `startTime`: `"PT18.581355S"`
- `startTimeInSeconds`: `18.581`
- `availProgramDateTime`: `"2023-05-03T21:24:41.453Z"`
- `adId`: `4603269`

###### Example : DASH

In the following example, the MediaTailor session gets a midroll in the manifest. Note that the
`@start` attribute value of the second period, which is the ad period, has a
value that's relative to the `MPD@availabilityStartTime` value. This value is the
one that MediaTailor writes into the client-side tracking response `startTime` fields,
for all sessions.

```
<?xml version="1.0" encoding="UTF-8"?>
<MPD availabilityStartTime="2022-10-05T19:38:39.263Z" minBufferTime="PT10S" minimumUpdatePeriod="PT2S" profiles="urn:mpeg:dash:profile:isoff-live:2011" publishTime="2023-05-03T22:06:48.411Z" suggestedPresentationDelay="PT10S" timeShiftBufferDepth="PT1M30S" type="dynamic" xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:scte35="urn:scte:scte35:2013:xml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd">
    <BaseURL>https://123.channel-assembly.mediatailor.us-west-2.amazonaws.com/v1/channel/my-channel/</BaseURL>
    <Location>https://123.cloudfront.net/v1/dash/94063eadf7d8c56e9e2edd84fdf897826a70d0df/MediaTailor-Live-HLS-DASH/channel/channel1/dash.mpd?aws.sessionId=794a15e0-2a7f-4941-a537-9d71627984e5</Location>
    <Period id="1683151479166_1" start="PT5042H25M59.903S" xmlns="urn:mpeg:dash:schema:mpd:2011">
        <BaseURL>https://123.cloudfront.net/out/v1/f1a946be8efa45b0931ea35c9055fb74/ddb73bf548a44551a0059c346226445a/eaa5485198bf497284559efb8172425e/</BaseURL>
        <AdaptationSet ...>
            ...
        </AdaptationSet>
    </Period>
    <Period id="1683151599194_1_1" start="PT5042H27M59.931S">
        <BaseURL>https://123.cloudfront.net/tm/94063eadf7d8c56e9e2edd84fdf897826a70d0df/fpc5omz5wzd2rdepgieibp23ybyqyrme/</BaseURL>
        <AdaptationSet ...>
            ...
        </AdaptationSet>
    </Period>
</MPD>
```

In the client-side tracking JSON payload, the following values apply:

- `startTime`: `"PT5042H27M59.931S"`
- `startTimeInSeconds`: `18152879.931`
- `availProgramDateTime`: `null`
- `adId`: `1683151599194_1_1`
