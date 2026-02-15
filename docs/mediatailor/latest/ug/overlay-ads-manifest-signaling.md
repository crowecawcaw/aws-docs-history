# Manifest signaling

MediaTailor trigger overlay-ads support when it sees a specific SCTE-35 marker in the
manifest. The required signal is a splice command type 6, or time signal, that is a Provider
Overlay Advertisement Start signal. This signal has a segmentation type id of
`0x38`

The following example shows the `0x38` SCTE-35 marker in a JSON
object.

```
{
  "tableId": 252,
  "selectionSyntaxIndicator": false,
  "privateIndicator": false,
  "sectionLength": 53,
  "protocolVersion": 0,
  "encryptedPacket": false,
  "encryptedAlgorithm": 0,
  "ptsAdjustment": 0,
  "cwIndex": 0,
  "tier": 4095,
  "spliceCommandLength": 5,
  "spliceCommandType": 6,
  "spliceCommand": {
    "specified": true,
    "pts": 1800392
  },
  "descriptorLoopLength": 31,
  "descriptors": [
    {
      "spliceDescriptorTag": 2,
      "descriptorLength": 29,
      "indentifier": "CUEI",
      "segmentationEventId": 158389361,
      "segmentationEventCancelIndicator": false,
      "programSegmentationFlag": true,
      "segmentationDurationFlag": true,
      "deliveryNotRestrictedFlag": false,
      "webDeliveryAllowedFlag": true,
      "noRegionalBlackoutFlag": true,
      "archiveAllowedFlag": true,
      "deviceResctrictions": 3,
      "segmentationDuration": 1350000,
      "segmentationUpidType": 9,
      "segmentationUpidLength": 7,
      "segmentationUpid": {
        "0": 111,
        "1": 118,
        "2": 101,
        "3": 114,
        "4": 108,
        "5": 97,
        "6": 121
      },
      "segmentationTypeId": 56,
      "segmentNum": 1,
      "segmentsExpected": 0
    }
  ],
  "crc": 2510422713
}
```

The following example shows the SCTE-35 signal represented as a binary (base
32/hexadecimal) value:

```
0xfc303500000000000000fff00506fe001b78c8001f021d435545490970d4717fdf00000dbba009076f7665726c6179380100000084226c4f
```

The following examples shows the SCTE-35 marker in both HLS and DASH
manifests.

###### Example: HLS manifest

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:7
#EXT-X-MEDIA-SEQUENCE:419
#EXT-X-DISCONTINUITY-SEQUENCE:3
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:09.231Z
#EXTINF:6.02,
https://aws.cloudfront.net/media/asset1/index1_00007.ts
#EXT-X-DISCONTINUITY
#EXT-X-KEY:METHOD=NONE
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:15.251Z
#EXTINF:6.0,
https://aws.cloudfront.net/media/asset1/index1_00001.ts
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:21.251Z
#EXTINF:4.0,
https://aws.cloudfront.net/media/asset1/index1_00002.ts
#EXT-X-DISCONTINUITY
#EXT-X-DATERANGE:ID="1692073825251-30-1",START-DATE="2023-08-15T04:30:25.251Z",DURATION=10.0,PLANNED-DURATION=10.0,SCTE35-OUT=0xfc303500000000000000fff00506fe001b78c8001f021d435545490970d4717fdf00000dbba009076f7665726c6179380100000084226c4f
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:25.251Z
#EXTINF:2.0,
https://aws.cloudfront.net/media/asset1/index1_00003.ts
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:27.251Z
#EXTINF:6.0,
https://aws.cloudfront.net/media/asset1/index1_00004.ts
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:33.251Z
#EXTINF:2.0,
https://aws.cloudfront.net/media/asset1/index1_00005.ts
#EXT-X-DISCONTINUITY
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:35.251Z
#EXTINF:4.0,
https://aws.cloudfront.net/media/asset1/index1_00006.ts
#EXT-X-PROGRAM-DATE-TIME:2023-08-15T04:30:39.251Z
#EXTINF:6.02,
https://aws.cloudfront.net/media/asset1/index1_00007.ts
```

###### Example: DASH manifest

```
<?xml version="1.0"?>
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:scte35="urn:scte:scte35:2013:xml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" availabilityStartTime="2023-08-15T16:34:05.911Z" minBufferTime="PT30S" minimumUpdatePeriod="PT2S" profiles="urn:mpeg:dash:profile:isoff-live:2011" publishTime="2023-08-15T16:34:17.950Z" suggestedPresentationDelay="PT20S" timeShiftBufferDepth="PT1M30S" type="dynamic" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd">
  <Period xmlns="urn:mpeg:dash:schema:mpd:2011" id="1692117245944_1" start="PT0.033S">
    <BaseURL>https://aws.cloudfront.net/out/v1/abc/123/def/</BaseURL>
    <EventStream schemeIdUri="urn:scte:scte35:2013:xml" timescale="90000">
      <Event duration="900000">
        <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="0" tier="4095">
          <scte35:TimeSignal>
            <scte35:SpliceTime ptsTime="0"/>
          </scte35:TimeSignal>
          <scte35:SegmentationDescriptor segmentNum="0" segmentationDuration="900000" segmentationEventCancelIndicator="false" segmentationEventId="1" segmentationTypeId="56" segmentsExpected="0" subSegmentNum="0" subSegmentsExpected="0">
            <scte35:SegmentationUpid segmentationUpidFormat="hexBinary" segmentationUpidType="14">63736f7665726c6179</scte35:SegmentationUpid>
          </scte35:SegmentationDescriptor>
        </scte35:SpliceInfoSection>
      </Event>
    </EventStream>
    <AdaptationSet bitstreamSwitching="true" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
      <Representation bandwidth="3000000" codecs="avc1.4D4028" frameRate="30/1" height="1080" id="1" width="1920">
        <SegmentTemplate initialization="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_video_1_0_init.mp4" media="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_video_1_0_$Number$.mp4" presentationTimeOffset="0" startNumber="1" timescale="30000">
          <SegmentTimeline>
            <S d="60000" r="6" t="1000"/>
            <S d="30000" t="421000"/>
          </SegmentTimeline>
        </SegmentTemplate>
      </Representation>
      <Representation bandwidth="2499968" codecs="avc1.4D4028" frameRate="30/1" height="1080" id="2" width="1920">
        <SegmentTemplate initialization="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_video_2_0_init.mp4" media="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_video_2_0_$Number$.mp4" presentationTimeOffset="0" startNumber="1" timescale="30000">
          <SegmentTimeline>
            <S d="60000" r="6" t="1000"/>
            <S d="30000" t="421000"/>
          </SegmentTimeline>
        </SegmentTemplate>
      </Representation>
      <Representation bandwidth="2200000" codecs="avc1.4D401F" frameRate="30/1" height="720" id="3" width="1280">
        <SegmentTemplate initialization="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_video_3_0_init.mp4" media="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_video_3_0_$Number$.mp4" presentationTimeOffset="0" startNumber="1" timescale="30000">
          <SegmentTimeline>
            <S d="60000" r="6" t="1000"/>
            <S d="30000" t="421000"/>
          </SegmentTimeline>
        </SegmentTemplate>
      </Representation>
    </AdaptationSet>
    <AdaptationSet lang="eng" mimeType="audio/mp4" segmentAlignment="0">
      <Label>Alternate Audio</Label>
      <Representation audioSamplingRate="48000" bandwidth="128000" codecs="mp4a.40.2" id="9">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
        <SegmentTemplate initialization="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_audio_9_0_init.mp4" media="../cf684d31ec9e451ca98d2349989f6c0a/855c733eed20493ab3cc1100750bcf0b/index_audio_9_0_$Number$.mp4" presentationTimeOffset="0" startNumber="1" timescale="48000">
          <SegmentTimeline>
            <S d="98304" t="0"/>
            <S d="96256" t="98304"/>
            <S d="95232" t="194560"/>
            <S d="96256" r="2" t="289792"/>
            <S d="95232" t="578560"/>
            <S d="46080" t="673792"/>
          </SegmentTimeline>
        </SegmentTemplate>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```
