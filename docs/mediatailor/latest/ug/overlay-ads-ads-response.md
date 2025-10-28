# Ad Decision Server (ADS) response

The ADS response must contain one valid tracking event. At minimum, the tracking
event can be an `Impression` tracking event. The tracking event should
contain at least one `NonLinear` ad. This ad is the overlay ad, taking
the form of a static, HTML, or iFrame resource.

```
<vmap AdBreak breaktype="linear" breakId="csoverlay"
```

If the VAST response is a VMAP with `breakType` of `nonlinear`, the avail metadata is inside
the `nonLinearAvails` root object. If the VAST response is a VMAP with a `breakType` of `linear`,
or is a plain VAST response without VMAP, the avail metadata is inside the `avails` root
object.

The following VAST response is a wrapped VMAP response with a
`breakType` value of `linear`.

In addition to the wrapped VMAP response, MediaTailor also supports a wrapped VMAP
response with a `breakType` value of `nonlinear`, and a plain
VAST response.

```
<?xml version="1.0" encoding="utf-8"?>
<vmap:VMAP xmlns:vmap="http://www.iab.net/vmap-1.0" version="1.0">
  <vmap:AdBreak breakType="linear" breakId="csoverlay">
    <vmap:AdSource allowMultipleAds="true" followRedirects="true" id="1">
      <vmap:VASTAdData>
        <VAST xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="3.0" xsi:noNamespaceSchemaLocation="vast.xsd">
          <Ad sequence="1">
            <InLine>
              <AdSystem>2.0</AdSystem>
              <AdTitle>2</AdTitle>
              <Impression><![CDATA[`https://adserver.com/beacon=impression`]]></Impression>
              <Creatives>
                <Creative>
                  <NonLinearAds>
                    <NonLinear width="640" height="360" id="18">
                      <StaticResource creativeType="text/js_ref"><![CDATA[`https://client-side-ads.com/tags/static/ctv-generic/overlay001.json?iv_geo_country%3DUS%26`]]></StaticResource>
                    </NonLinear>
                  </NonLinearAds>
                </Creative>
              </Creatives>
            </InLine>
          </Ad>
        </VAST>
      </vmap:VASTAdData>
    </vmap:AdSource>
    <vmap:TrackingEvents>
      <vmap:Tracking event="breakStart"><![CDATA[`https://adserver.com/beacon=breakstartimpression`]]></vmap:Tracking>
      <vmap:Tracking event="breakEnd"><![CDATA[`https://adserver.com/beacon=breakendimpression`]]></vmap:Tracking>
    </vmap:TrackingEvents>
  </vmap:AdBreak>
</vmap:VMAP>
```

###### Example 1: DASH manifest source to MediaTailor

```
<?xml version="1.0" encoding="utf-8"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:scte35="urn:scte:scte35:2013:xml" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd" id="201" type="dynamic" publishTime="2022-11-07T19:59:05+00:00" minimumUpdatePeriod="PT2S" availabilityStartTime="2022-11-07T06:57:11.250000+00:00" minBufferTime="PT10S" suggestedPresentationDelay="PT20.000S" timeShiftBufferDepth="PT58.999S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
  <Period start="PT46827.601S" id="0" duration="PT88.321S">
  ...
  </Period>
  <Period start="PT46915.922S" id="45" duration="PT6.006S">
    <EventStream timescale="90000" schemeIdUri="urn:scte:scte35:2014:xml+bin">
    <Event duration="540000" id="144">
        <scte35:Signal>
            <scte35:Binary>`SCTE35-binary`</scte35:Binary>
        </scte35:Signal>
    </Event>
    </EventStream>
    ...
  </Period>
  <Period start="PT46921.928S" id="49">
  ...
  </Period>
</MPD>
```

###### Example 2: MediaTailor personalized DASH manifest containing an ad ID decoration

```
<?xml version="1.0" encoding="utf-8"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:scte35="urn:scte:scte35:2013:xml" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd" id="201" type="dynamic" publishTime="2022-11-07T19:59:05+00:00" minimumUpdatePeriod="PT2S" availabilityStartTime="2022-11-07T06:57:11.250000+00:00" minBufferTime="PT10S" suggestedPresentationDelay="PT20.000S" timeShiftBufferDepth="PT58.999S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
  <Period start="PT46827.601S" id="0" duration="PT88.321S">
  ...
  </Period>
  <Period start="PT46915.922S" id="45" duration="PT6.006S">
  <EventStream schemeIdUri="urn:sva:advertising-wg:ad-id-signaling" timescale="90000">
    <Event presentationTime="13500000" duration="1351350">
    <![CDATA[{"version": 1,"identifiers": [{"scheme": "urn:smpte:ul:060E2B34.01040101.01200900.00000000","value": "`adId`","ad_position": "`adId`", "ad_type":"overlay","creative_id": "`creativeId`","tracking_uri": "`trackingUri`"}]}]]></Event>
  </EventStream>
  ...
  </Period>
  <Period start="PT46921.928S" id="49">
  ...
  </Period>
</MPD>
```
