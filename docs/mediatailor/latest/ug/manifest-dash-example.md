# DASH MPD examples

The following sections provide examples of DASH origin MPDs and personalized MPDs.
Understanding these examples can help you configure and troubleshoot your MediaTailor
workflows.

For information about how query parameters are applied to DASH manifests and segments, see
[MediaTailor
DASH implicit session initialization](manifest-query-parameters-dash-implicit-session-initialization.md "manifest-query-parameters-dash-implicit-session-initialization.md").

## Understanding DASH MPD structure

Dynamic Adaptive Streaming over HTTP (DASH) uses a Media Presentation Description
(MPD) manifest to deliver streaming content. The MPD is an XML document that describes
the structure and availability of media content.

MPD (Media Presentation Description)

The MPD is the primary manifest file in DASH streaming that describes the
structure and availability of media content. It contains information about
periods, adaptation sets, representations, and segments that make up the
streaming content.

This manifest type is also known by several other names in various
contexts, including DASH manifest, DASH MPD, master manifest (when comparing
to HLS), or presentation manifest.

In MediaTailor workflows, the MPD is the entry point for playback requests and
is where ad personalization begins.

Period

A Period is a temporal section of a DASH presentation. Each Period
contains one or more adaptation sets and represents a span of media time. In
ad insertion workflows, separate Periods are typically used to delineate
between content and ads.

In MediaTailor workflows, Periods are used to separate main content from ad
content, with each ad typically represented by its own Period.

AdaptationSet

An AdaptationSet groups a set of interchangeable encoded versions of one
or several media content components. For example, one AdaptationSet might
contain multiple video quality levels, while another might contain multiple
audio language options.

In MediaTailor workflows, AdaptationSets are preserved during ad insertion to
maintain consistent media types between content and ads.

Representation

A Representation is a specific encoded version of the media content within
an AdaptationSet. Each Representation typically differs in bitrate,
resolution, or other encoding parameters, allowing clients to select the
most appropriate version based on network conditions and device
capabilities.

In MediaTailor workflows, Representations in ad Periods are matched as closely
as possible to the Representations in content Periods to ensure a smooth
viewing experience.

For more detailed information about DASH manifest types, see [DASH manifest types](dash-manifest-types.md "dash-manifest-types.md").

For information about DASH manifest structure and configuration in AWS Elemental MediaPackage, see the MediaPackage User Guide section on DASH overview.

## Live DASH MPD examples

This section provides examples of live DASH MPDs. Each example lists an MPD as
received from the origin server and after MediaTailor has personalized the MPD with
ads.

### DASH MPD splice insert

example

###### DASH origin MPD example for splice insert

The following example from an MPD shows an ad avail in a manifest received by
DASH from the content origin. This example uses the `SpliceInsert`
marker to indicate an ad avail.

```

<Period start="PT173402.036S" id="46041">
  <EventStream timescale="90000" schemeIdUri="urn:scte:scte35:2013:xml">
    <Event duration="9450000">
      <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="183265" tier="4095">
        <scte35:SpliceInsert spliceEventId="99" spliceEventCancelIndicator="false" outOfNetworkIndicator="true" spliceImmediateFlag="false" uniqueProgramId="1" availNum="1" availsExpected="1">
          <scte35:Program><scte35:SpliceTime ptsTime="7835775000"/></scte35:Program>
          <scte35:BreakDuration autoReturn="true" duration="9450000"/>
        </scte35:SpliceInsert>
        <scte35:SegmentationDescriptor segmentationEventId="99" segmentationEventCancelIndicator="false" segmentationDuration="9450000">
          <scte35:DeliveryRestrictions webDeliveryAllowedFlag="true" noRegionalBlackoutFlag="true" archiveAllowedFlag="true" deviceRestrictions="3"/>
          <scte35:SegmentationUpid segmentationUpidType="8" segmentationUpidLength="0"/>
          <scte35:SegmentationTypeID segmentationType="52"/>
          <scte35:SegmentNum segmentNum="1"/>
          <scte35:SegmentsExpected segmentsExpected="1"/>
        </scte35:SegmentationDescriptor>
      </scte35:SpliceInfoSection>
    </Event>
  </EventStream>
  <AdaptationSet mimeType="video/mp4" segmentAlignment="true" subsegmentAlignment="true" startWithSAP="1" subsegmentStartsWithSAP="1" bitstreamSwitching="true">
    <Representation id="1" width="960" height="540" frameRate="30000/1001" bandwidth="1000000" codecs="avc1.4D401F">
      <SegmentTemplate timescale="30000" media="index_video_1_0_$Number$.mp4?m=1528475245" initialization="index_video_1_0_init.mp4?m=1528475245" startNumber="178444" presentationTimeOffset="10395907501">
        <SegmentTimeline>
          <S t="10395907501" d="60060" r="29"/>
          <S t="10397709301" d="45045"/>
        </SegmentTimeline>
      </SegmentTemplate>
    </Representation>
  </AdaptationSet>
  <AdaptationSet mimeType="audio/mp4" segmentAlignment="0" lang="eng">
    <Representation id="2" bandwidth="96964" audioSamplingRate="48000" codecs="mp4a.40.2">
      <SegmentTemplate timescale="48000" media="index_audio_2_0_$Number$.mp4?m=1528475245" initialization="index_audio_2_0_init.mp4?m=1528475245" startNumber="178444" presentationTimeOffset="16633452001">
        <SegmentTimeline>
          <S t="16633452289" d="96256" r="3"/>
          <S t="16633837313" d="95232"/>
          <S t="16633932545" d="96256" r="4"/>
          <S t="16634413825" d="95232"/>
          <S t="16634509057" d="96256" r="5"/>
          <S t="16635086593" d="95232"/>
          <S t="16635181825" d="96256" r="4"/>
          <S t="16635663105" d="95232"/>
          <S t="16635758337" d="96256" r="5"/>
          <S t="16636335873" d="71680"/>
        </SegmentTimeline>
      </SegmentTemplate>
    </Representation>
  </AdaptationSet>
</Period>
```

In this origin MPD example:

- The `<EventStream>` element contains SCTE-35 markers that
  indicate ad avails
- The `<scte35:SpliceInsert>` element provides details
  about the ad avail
- The `<scte35:BreakDuration>` element specifies the
  duration of the ad break
- The `<AdaptationSet>` elements define the available video
  and audio streams

###### DASH personalized MPD example for splice insert

AWS Elemental MediaTailor personalizes the ad avails with advertising specifications.
The personalizations reflect the viewer data that is received from the player
and the advertising campaigns that are currently underway.

The following example shows an ad avail after AWS Elemental MediaTailor personalizes it.

```
<Period id="178443_1" start="PT96H15M30.25S">
  <BaseURL>http://111122223333.cloudfront.net/nbc_fallback_2/</BaseURL>
  <AdaptationSet bitstreamSwitching="false" frameRate="30/1" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
    <SegmentTemplate startNumber="1" timescale="90000"/>
    <Representation bandwidth="10000000" codecs="avc1.640028" height="1080" id="1" width="1920">
      <SegmentTemplate initialization="nbc_fallback_ad_2_1080p_10init.mp4" media="nbc_fallback_ad_2_1080p_10_$Number%09d$.mp4" startNumber="1" timescale="90000">
        <SegmentTimeline>
          <S d="180000" r="13" t="0"/>
          <S d="176940" t="2520000"/>
        </SegmentTimeline>
      </SegmentTemplate>
    </Representation>
    <Representation bandwidth="4000000" codecs="avc1.64001f" height="720" id="2" width="1280">
      <SegmentTemplate initialization="nbc_fallback_ad_2_720p_9init.mp4" media="nbc_fallback_ad_2_720p_9_$Number%09d$.mp4" startNumber="1" timescale="90000">
        <SegmentTimeline>
          <S d="180000" r="13" t="0"/>
          <S d="176940" t="2520000"/>
        </SegmentTimeline>
      </SegmentTemplate>
    </Representation>
  </AdaptationSet>
  <AdaptationSet mimeType="audio/mp4" segmentAlignment="0" lang="eng">
    <Representation id="8" bandwidth="128000" audioSamplingRate="48000" codecs="mp4a.40.2">
      <SegmentTemplate initialization="nbc_fallback_ad_2_audio_2init.mp4" media="nbc_fallback_ad_2_audio_2_$Number%09d$.mp4" startNumber="1" timescale="90000">
        <SegmentTimeline>
          <S d="180000" r="13" t="0"/>
          <S d="176940" t="2520000"/>
        </SegmentTimeline>
      </SegmentTemplate>
    </Representation>
  </AdaptationSet>
</Period>
```

In this personalized MPD example:

- MediaTailor has created a new Period for the ad content
- The `<BaseURL>` element points to the ad content
  location
- The `<AdaptationSet>` elements maintain similar structure
  to the content
- The `<Representation>` elements provide different quality
  levels for the ad content

### DASH MPD time signal

example

###### DASH origin MPD example for time signal

The following example from an MPD shows an ad avail in a manifest received by
DASH from the content origin. This example uses the `TimeSignal`
marker to indicate an ad avail.

```

<Period start="PT173402.036S" id="46041">
  <EventStream timescale="90000" schemeIdUri="urn:scte:scte35:2013:xml">
    <Event duration="9450000">
      <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="183265" tier="4095">
        <scte35:TimeSignal>
          <scte35:SpliceTime ptsTime="7835775000"/>
        </scte35:TimeSignal>
        <scte35:SegmentationDescriptor segmentationEventId="99" segmentationEventCancelIndicator="false" segmentationDuration="9450000">
          <scte35:DeliveryRestrictions webDeliveryAllowedFlag="true" noRegionalBlackoutFlag="true" archiveAllowedFlag="true" deviceRestrictions="3"/>
          <scte35:SegmentationUpid segmentationUpidType="8" segmentationUpidLength="0"/>
          <scte35:SegmentationTypeID segmentationType="52"/>
          <scte35:SegmentNum segmentNum="1"/>
          <scte35:SegmentsExpected segmentsExpected="1"/>
        </scte35:SegmentationDescriptor>
      </scte35:SpliceInfoSection>
    </Event>
  </EventStream>
  <AdaptationSet mimeType="video/mp4" segmentAlignment="true" subsegmentAlignment="true" startWithSAP="1" subsegmentStartsWithSAP="1" bitstreamSwitching="true">
    <Representation id="1" width="960" height="540" frameRate="30000/1001" bandwidth="1000000" codecs="avc1.4D401F">
      <SegmentTemplate timescale="30000" media="index_video_1_0_$Number$.mp4?m=1528475245" initialization="index_video_1_0_init.mp4?m=1528475245" startNumber="178444" presentationTimeOffset="10395907501">
        <SegmentTimeline>
          <S t="10395907501" d="60060" r="29"/>
          <S t="10397709301" d="45045"/>
        </SegmentTimeline>
      </SegmentTemplate>
    </Representation>
  </AdaptationSet>
</Period>
```

In this origin MPD example:

- The `<scte35:TimeSignal>` element is used instead of
  `<scte35:SpliceInsert>`
- The `<scte35:SegmentationDescriptor>` provides additional
  information about the ad avail

###### DASH personalized MPD example for time signal

AWS Elemental MediaTailor personalizes the ad avails with advertising specifications.
The personalizations reflect the viewer data that is received from the player
and the advertising campaigns that are currently underway.

The following example shows an ad avail after AWS Elemental MediaTailor personalizes it.

```
<Period id="178443_1" start="PT96H15M30.25S">
  <BaseURL>http://111122223333.cloudfront.net/nbc_fallback_2/</BaseURL>
  <AdaptationSet bitstreamSwitching="false" frameRate="30/1" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
    <SegmentTemplate startNumber="1" timescale="90000"/>
    <Representation bandwidth="10000000" codecs="avc1.640028" height="1080" id="1" width="1920">
      <SegmentTemplate initialization="nbc_fallback_ad_2_1080p_10init.mp4" media="nbc_fallback_ad_2_1080p_10_$Number%09d$.mp4" startNumber="1" timescale="90000">
        <SegmentTimeline>
          <S d="180000" r="13" t="0"/>
          <S d="176940" t="2520000"/>
        </SegmentTimeline>
      </SegmentTemplate>
    </Representation>
  </AdaptationSet>
</Period>
```

The personalized MPD for time signal is similar to the one for splice insert, with
MediaTailor creating a new Period for the ad content.

## VOD DASH MPD examples

This section provides examples of video on demand (VOD) DASH MPDs. Each example lists
an MPD as received from the origin server and after MediaTailor has personalized the MPD with
ads.

VOD DASH MPDs follow the same structure as live MPDs, but they typically have a
`type="static"` attribute in the MPD element and may contain multiple
Periods for different content segments.

For examples of VOD DASH MPDs, see the MediaTailor documentation on [DASH ad markers](dash-ad-markers.md "dash-ad-markers.md").

## Key differences in personalized

MPDs

When MediaTailor personalizes DASH MPDs, it makes several important changes:

Period handling

- New Periods are created for ad content
- Period start times are adjusted to maintain timeline
  continuity
- EventStream elements with SCTE-35 markers are processed and
  removed

AdaptationSet and Representation handling

- AdaptationSets in ad Periods are created to match content
  AdaptationSets
- Representations are created for different quality levels of the ad
  content
- SegmentTemplate elements are updated to point to ad content

Understanding these changes can help you troubleshoot issues in your MediaTailor workflows
and ensure proper configuration of your CDN and player.

## Related topics

For more information about DASH MPDs and MediaTailor, see the following topics:

- [DASH manifest types](dash-manifest-types.md "dash-manifest-types.md") -
  Detailed explanation of DASH manifest types
- [Using a CDN to optimize MediaTailor ad personalization and
  content delivery](integrating-cdn.md "integrating-cdn.md") -
  Information about using a CDN with MediaTailor
- [How MediaTailor ad insertion works](what-is-flow.md "what-is-flow.md") - Overview of how
  MediaTailor ad insertion works
- For comprehensive information about DASH manifest structure and MediaPackage configuration, see the MediaPackage User Guide section on DASH overview.
