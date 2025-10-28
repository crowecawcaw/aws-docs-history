# MediaTailor

DASH implicit session initialization

AWS Elemental MediaTailor creates a session for the client and redirects it with query parameters when
the client makes a manifest request without a session. The following example shows this
request format:

```
GET /v1/dash/`111122223333`/`originId`/index.mpd?manifest.test=123&other=456
```

MediaTailor creates a session for the client and redirects it with the query
parameters:

```
/v1/dash/`111122223333`/`originId`/index.mpd?sessionId=`session`&test=123
```

###### Parameter application in DASH

The DASH manifest response includes the query parameters in various locations,
including content segments, ad segments, and initialization URLs. MediaTailor applies
parameters to the following:

- DASH manifest Location elements
- SegmentTemplate initialization attributes
- SegmentTemplate media attributes
- Content segment URLs
- Ad segment URLs
  When the client makes the request, MediaTailor responds with a DASH manifest similar to the
  following example. The first period is a content period, so MediaTailor doesn't insert the
  manifest query parameter there. In the second period, which is an ad period, MediaTailor
  inserts the manifest query parameter into the `SegmentTemplate` element's
  `initialization` attribute and `media` attribute. The
  `Location` element also has the manifest query parameters.

```
<?xml version="1.0" encoding="UTF-8"?>
<MPD availabilityStartTime="2018-07-27T09:48:23.634000+00:00" id="201" minBufferTime="PT30S" minimumUpdatePeriod="PT15S" profiles="urn:mpeg:dash:profile:isoff-live:2011" publishTime="2023-02-14T23:37:43" suggestedPresentationDelay="PT25.000S" timeShiftBufferDepth="PT56.997S" type="dynamic" xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:scte35="urn:scte:scte35:2013:xml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd">
    <BaseURL>https://origin.com/contentSegments/</BaseURL>
    <Location>https://mediatailor.com/v1/dash/`111122223333`/`originId`/index.mpd?test=123&aws.sessionId=`session`</Location>
    <Period duration="PT29.963S" id="28737823" start="PT143732873.178S">
        <AdaptationSet bitstreamSwitching="true" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
            <Representation bandwidth="2200000" codecs="avc1.640029" frameRate="30000/1001" height="540" id="1" width="960">
                <SegmentTemplate initialization="index_video_7_0_init.mp4?m=1611174111" media="index_video_7_0_$Number$.mp4?m=1611174111" presentationTimeOffset="4311986195351" startNumber="28737828" timescale="30000">
                    <SegmentTimeline>
                        <S d="180180" t="4311986911066"/>
                        <S d="3003" t="4311987091246"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
        </AdaptationSet>
    </Period>
    <Period id="28737829_1" start="PT39925H48M23.141S">
        <BaseURL>https://mediatailor.com/v1/dashsegment/``111122223333``/`originId`/`session`/28737829/28737829_1/</BaseURL>
        <AdaptationSet bitstreamSwitching="false" frameRate="30000/1001" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
            <SegmentTemplate startNumber="1" timescale="90000"/>
            <Representation bandwidth="2200000" codecs="avc1.64001f" height="540" id="1" width="960">
                <SegmentTemplate initialization="asset_540_2_0init.mp4?test=123" media="asset_540_2_0_$Number%09d$.mp4?test=123" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="87087" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
        </AdaptationSet>
    </Period>
</MPD>
```
