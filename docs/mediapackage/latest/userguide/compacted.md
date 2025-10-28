# DASH manifest compactness

For some players, processing a manifest with duplicate data about each representation
(track) is difficult and slow. To reduce some of the burden, AWS Elemental MediaPackage compacts the manifest
by default. Compacting is achieved by moving some attributes from the
`Representation` object to the `AdaptationSet` object. This way,
rather than having the attributes defined for each representation in the manifest, they're
defined once at a higher level. The representations then inherit these attributes from the
adaptation set.

If you require an uncompacted manifest, you can set the [manifest compactness](endpoints-create.md#dash-manifest "endpoints-create.md#dash-manifest") on the DASH endpoint.

###### Example standard DVB-DASH manifest (compacted)

In this example, the `SegmentTemplate` objects and all of their elements
are collapsed into one and moved to the `AdaptationSet`. The playback device
understands that each representation in this adaptation set uses this same
template:

```
<MPD id="0" profiles="urn:dvb:dash:profile:dvb-dash:2014,urn:dvb:dash:profile:dvb-dash:isoff-ext-live:2014" type="dynamic" minimumUpdatePeriod="PT2S" minBufferTime="PT5S" timeShiftBufferDepth="PT1M0.002S" suggestedPresentationDelay="PT10S" availabilityStartTime="2024-01-01T00:00:00.000000+00:00" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:dvb="urn:dvb:dash-extensions:2014-1" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd" publishTime="2025-02-27T19:52:52.000491+00:00">
  <ProgramInformation lang="eng" moreInformationURL="https://dvb.org/?standard=dvb-mpeg-dash-profile-for-transport-of-iso-bmff-based-dvb-services-over-ip-based-networks">
    <Title>Test DVB-DASH Channel title</Title>
    <Source>Test DVB-DASH Channel source</Source>
    <Copyright>Test DVB-DASH Channel copyright</Copyright>
  </ProgramInformation>
  <BaseURL serviceLocation="slgroup" dvb:priority="1" dvb:weight="100">https://w2dorn.egress.pentest-stack.dev.v2.mediapackage.elemental.aws.a2z.com/out/v1/HippoPentest/HippoPentestCmaf/cmaf/</BaseURL>
  <BaseURL serviceLocation="slgroup" dvb:priority="10" dvb:weight="10">https://w2dorn.egress.pentest-stack.dev.v2.mediapackage.elemental.aws.a2z.com/out/v1/HippoPentest/HippoPentestCmaf/cmaf/</BaseURL>
  <Period id="1740685874005" start="PT10171H51M14.005S">
    <AdaptationSet id="107031859" contentType="video" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" bitstreamSwitching="true">
      <Role schemeIdUri="urn:mpeg:dash:role:2011" value="main"/>
      <SegmentTemplate timescale="60000" media="segment_$RepresentationID$_$Number$.mp4" initialization="segment_$RepresentationID$_145057156_init.mp4" startNumber="870342955" presentationTimeOffset="104441152310000">
        <SegmentTimeline>
          <S t="104441154540000" d="120000" r="29"/>
        </SegmentTimeline>
      </SegmentTemplate>
      <Representation id="h264_1080p30" bandwidth="4096000" codecs="avc1.4D4028" frameRate="30/1" width="1920" height="1080"/>
      <Representation id="h264_720p30" bandwidth="8000000" codecs="avc1.4D401F" frameRate="30/1" width="1280" height="720"/>
    </AdaptationSet>
.
.
.
  </Period>
  <UTCTiming schemeIdUri="urn:mpeg:dash:utc:http-iso:2014" value="https://time.akamai.com/?iso"/>
  <Metrics metrics="DVBErrors">
    <Reporting schemeIdUri="urn:dvb:dash:reporting:2014" value="1" dvb:reportingUrl="https://dvb.org" dvb:probability="1000"/>
    <Reporting schemeIdUri="urn:dvb:dash:reporting:2014" value="1" dvb:reportingUrl="https://dvb.org" dvb:probability="500"/>
  </Metrics>
</MPD>
```

###### Example full DASH manifest (uncompacted)

In the following example, the `SegmentTemplate` object and all of its
elements are listed in every `Representation.` If
`ContentProtection` is configured, those values are also listed in each
`Representation`. Each adaptation set in the manifest has this same
layout:

```
<AdaptationSet mimeType="video/mp4" segmentAlignment="true" subsegmentAlignment="true" startWithSAP="1" subsegmentStartsWithSAP="1" bitstreamSwitching="true">
   <Representation id="1" width="640" height="360" frameRate="30/1" bandwidth="749952" codecs="avc1.640029">
      <SegmentTemplate timescale="30000" media="index_video_1_0_$Number$.mp4?m=1543947824" initialization="index_video_1_0_init.mp4?m=1543947824" startNumber="1">
         <SegmentTimeline>
           <S t="62000" d="60000" r="9"/>
         </SegmentTimeline>
      </SegmentTemplate>
   </Representation>
   <Representation id="2" width="854" height="480" frameRate="30/1" bandwidth="1000000" codecs="avc1.640029">
      <SegmentTemplate timescale="30000" media="index_video_3_0_$Number$.mp4?m=1543947824" initialization="index_video_3_0_init.mp4?m=1543947824" startNumber="1">
         <SegmentTimeline>
           <S t="62000" d="60000" r="9"/>
         </SegmentTimeline>
      </SegmentTemplate>
   </Representation>
   <Representation id="3" width="1280" height="720" frameRate="30/1" bandwidth="2499968" codecs="avc1.640029">
      <SegmentTemplate timescale="30000" media="index_video_5_0_$Number$.mp4?m=1543947824" initialization="index_video_5_0_init.mp4?m=1543947824" startNumber="1">
         <SegmentTimeline>
           <S t="62000" d="60000" r="9"/>
         </SegmentTimeline>
      </SegmentTemplate>
   </Representation>
</AdaptationSet>
```
