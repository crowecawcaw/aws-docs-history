# Personalizing DASH manifests with ad metadata

MediaTailor personalizes the manifest with creatives returned by the Ad Decision Server
(ADS). For each ad, MediaTailor also includes an `EventStream` element that
spans the duration of the ad. The `Event` element format is similar to
that described in the section [Ad creative signaling in DASH and HLS](https://www.svta.org/document/draft-ad-creative-signaling-in-dash-and-hls/ "https://www.svta.org/document/draft-ad-creative-signaling-in-dash-and-hls/") in the 2023 version of the
_SVA technical publication_.

For underfilled ad breaks on configurations that have slate enabled, MediaTailor appends
the slate period to the end of the avail period, but without any
`EventStream` metadata

For each ad stitched into the personalized manifest, MediaTailor adds the creative
metadata, represented as a `CDATA` element within an `Event`
element.

###### Example Linear DASH origin (Inline SCTE attributes):

```
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:scte35="urn:scte:scte35:2013:xml" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd" id="201" type="dynamic" publishTime="2023-02-10T21:08:40+00:00" minimumUpdatePeriod="PT6S" availabilityStartTime="2023-02-09T22:47:05.865000+00:00" minBufferTime="PT10S" suggestedPresentationDelay="PT20.000S" timeShiftBufferDepth="PT88.999S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
  <Period start="PT80141.456S" id="104" duration="PT304.103S">
    <AdaptationSet id="1485523442" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1" bitstreamSwitching="true">
      <SegmentTemplate timescale="60000" media="index_video_$RepresentationID$_0_$Number$.mp4?m=1676062374" initialization="index_video_$RepresentationID$_0_init.mp4?m=1676062374" startNumber="151" presentationTimeOffset="4808487386">
        <SegmentTimeline>
          <S t="4824975858" d="360360" r="3"/>
          <S t="4826417298" d="316316"/>
        </SegmentTimeline>
      </SegmentTemplate>
      <Representation id="1" width="960" height="540" frameRate="30000/1001" bandwidth="1800000" codecs="avc1.4D401F"/>
      <Representation id="3" width="640" height="360" frameRate="30000/1001" bandwidth="1200000" codecs="avc1.4D401E"/>
      <Representation id="5" width="480" height="270" frameRate="30000/1001" bandwidth="800000" codecs="avc1.4D4015"/>
    </AdaptationSet>
    <AdaptationSet id="1377232898" mimeType="audio/mp4" segmentAlignment="0" lang="eng">
      <Label>eng</Label>
      <SegmentTemplate timescale="48000" media="index_audio_$RepresentationID$_0_$Number$.mp4?m=1676062374" initialization="index_audio_$RepresentationID$_0_init.mp4?m=1676062374" startNumber="151" presentationTimeOffset="3846790126">
        <SegmentTimeline>
          <S t="3859981294" d="287744"/>
          <S t="3860269038" d="288768"/>
          <S t="3860557806" d="287744"/>
          <S t="3860845550" d="288768"/>
          <S t="3861134318" d="252928"/>
        </SegmentTimeline>
        </SegmentTemplate>
        <Representation id="2" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
      <Representation id="4" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
      <Representation id="6" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
    </AdaptationSet>
    <SupplementalProperty schemeIdUri="urn:scte:dash:utc-time" value="2023-02-10T21:02:31.007Z"/>
  </Period>
  <Period start="PT80445.560S" id="155" duration="PT44.978S">
    <EventStream timescale="90000" schemeIdUri="urn:scte:scte35:2013:xml">
      <Event duration="4048044">
        <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="207000" tier="4095">
          <scte35:SpliceInsert spliceEventId="111" spliceEventCancelIndicator="false" outOfNetworkIndicator="true" spliceImmediateFlag="false" uniqueProgramId="1" availNum="1" availsExpected="1">
            <scte35:Program>
              <scte35:SpliceTime ptsTime="7239893422"/>
            </scte35:Program>
            <scte35:BreakDuration autoReturn="true" duration="4048044"/>
          </scte35:SpliceInsert>
        </scte35:SpliceInfoSection>
      </Event>
    </EventStream>
    <AdaptationSet id="1485523442" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1" bitstreamSwitching="true">
      <SegmentTemplate timescale="60000" media="index_video_$RepresentationID$_0_$Number$.mp4?m=1676062374" initialization="index_video_$RepresentationID$_0_init.mp4?m=1676062374" startNumber="156" presentationTimeOffset="4826733614">
        <SegmentTimeline>
          <S t="4826733614" d="284284"/>
          <S t="4827017898" d="360360" r="5"/>
          <S t="4829180058" d="252252"/>
        </SegmentTimeline>
      </SegmentTemplate>
      <Representation id="1" width="960" height="540" frameRate="30000/1001" bandwidth="1800000" codecs="avc1.4D401F"/>
      <Representation id="3" width="640" height="360" frameRate="30000/1001" bandwidth="1200000" codecs="avc1.4D401E"/>
      <Representation id="5" width="480" height="270" frameRate="30000/1001" bandwidth="800000" codecs="avc1.4D4015"/>
    </AdaptationSet>
    <AdaptationSet id="1377232898" mimeType="audio/mp4" segmentAlignment="0" lang="eng">
      <Label>eng</Label>
      <SegmentTemplate timescale="48000" media="index_audio_$RepresentationID$_0_$Number$.mp4?m=1676062374" initialization="index_audio_$RepresentationID$_0_init.mp4?m=1676062374" startNumber="156" presentationTimeOffset="3861387246">
        <SegmentTimeline>
          <S t="3861387246" d="227328"/>
          <S t="3861614574" d="288768"/>
          <S t="3861903342" d="287744"/>
          <S t="3862191086" d="288768"/>
          <S t="3862479854" d="287744"/>
          <S t="3862767598" d="288768"/>
          <S t="3863056366" d="287744"/>
          <S t="3863344110" d="202752"/>
        </SegmentTimeline>
      </SegmentTemplate>
      <Representation id="2" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
      <Representation id="4" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
      <Representation id="6" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
    </AdaptationSet>
    <SupplementalProperty schemeIdUri="urn:scte:dash:utc-time" value="2023-02-10T21:07:35.111Z"/>
  </Period>
  <Period start="PT80490.538S" id="163">
    <AdaptationSet id="1485523442" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1" bitstreamSwitching="true">
      <SegmentTemplate timescale="60000" media="index_video_$RepresentationID$_0_$Number$.mp4?m=1676062374" initialization="index_video_$RepresentationID$_0_init.mp4?m=1676062374" startNumber="164" presentationTimeOffset="4829432310">
        <SegmentTimeline>
          <S t="4829432310" d="348348"/>
          <S t="4829780658" d="360360" r="1"/>
        </SegmentTimeline>
      </SegmentTemplate>
      <Representation id="1" width="960" height="540" frameRate="30000/1001" bandwidth="1800000" codecs="avc1.4D401F"/>
      <Representation id="3" width="640" height="360" frameRate="30000/1001" bandwidth="1200000" codecs="avc1.4D401E"/>
      <Representation id="5" width="480" height="270" frameRate="30000/1001" bandwidth="800000" codecs="avc1.4D4015"/>
    </AdaptationSet>
    <AdaptationSet id="1377232898" mimeType="audio/mp4" segmentAlignment="0" lang="eng">
      <Label>eng</Label>
      <SegmentTemplate timescale="48000" media="index_audio_$RepresentationID$_0_$Number$.mp4?m=1676062374" initialization="index_audio_$RepresentationID$_0_init.mp4?m=1676062374" startNumber="164" presentationTimeOffset="3863546862">
        <SegmentTimeline>
          <S t="3863546862" d="278528"/>
          <S t="3863825390" d="287744"/>
          <S t="3864113134" d="288768"/>
        </SegmentTimeline>
      </SegmentTemplate>
      <Representation id="2" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
      <Representation id="4" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
      <Representation id="6" bandwidth="193007" audioSamplingRate="48000" codecs="mp4a.40.2">
        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
      </Representation>
    </AdaptationSet>
    <SupplementalProperty schemeIdUri="urn:scte:dash:utc-time" value="2023-02-10T21:08:20.090Z"/>
  </Period>
</MPD>
```

###### Example Linear DASH personalized manifest (with creative ad signaling):

```
<MPD availabilityStartTime="2023-02-09T22:47:05.865000+00:00" id="201" minBufferTime="PT10S" minimumUpdatePeriod="PT6S" profiles="urn:mpeg:dash:profile:isoff-live:2011" publishTime="2023-02-10T21:08:43+00:00" suggestedPresentationDelay="PT20.000S" timeShiftBufferDepth="PT88.999S" type="dynamic" xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:scte35="urn:scte:scte35:2013:xml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-DASH_schema_files/DASH-MPD.xsd">
    <BaseURL>https://d3fch9e2fcarly.cloudfront.net/out/v1/f9f38deca3f14fc4b5ab3cdbd76cfb9e/</BaseURL>
    <Location>https://777788889999.mediatailor.us-west-2.amazonaws.com/v1/dash/94063eadf7d8c56e9e2edd84fdf897826a70d0df/emt/out/v1/f9f38deca3f14fc4b5ab3cdbd76cfb9e/index.mpd?aws.sessionId=672ed481-4ffd-4270-936f-7c8403947f2e</Location>
    <Period duration="PT304.103S" id="104" start="PT80141.456S">
        <AdaptationSet bitstreamSwitching="true" id="1485523442" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
            <SegmentTemplate initialization="index_video_$RepresentationID$_0_init.mp4?m=1676062374" media="index_video_$RepresentationID$_0_$Number$.mp4?m=1676062374" presentationTimeOffset="4808487386" startNumber="151" timescale="60000">
                <SegmentTimeline>
                    <S d="360360" r="3" t="4824975858"/>
                    <S d="316316" t="4826417298"/>
                </SegmentTimeline>
            </SegmentTemplate>
            <Representation bandwidth="1800000" codecs="avc1.4D401F" frameRate="30000/1001" height="540" id="1" width="960"/>
            <Representation bandwidth="1200000" codecs="avc1.4D401E" frameRate="30000/1001" height="360" id="3" width="640"/>
            <Representation bandwidth="800000" codecs="avc1.4D4015" frameRate="30000/1001" height="270" id="5" width="480"/>
        </AdaptationSet>
        <AdaptationSet id="1377232898" lang="eng" mimeType="audio/mp4" segmentAlignment="0">
            <Label>eng</Label>
            <SegmentTemplate initialization="index_audio_$RepresentationID$_0_init.mp4?m=1676062374" media="index_audio_$RepresentationID$_0_$Number$.mp4?m=1676062374" presentationTimeOffset="3846790126" startNumber="151" timescale="48000">
                <SegmentTimeline>
                    <S d="287744" t="3859981294"/>
                    <S d="288768" t="3860269038"/>
                    <S d="287744" t="3860557806"/>
                    <S d="288768" t="3860845550"/>
                    <S d="252928" t="3861134318"/>
                </SegmentTimeline>
            </SegmentTemplate>
            <Representation audioSamplingRate="48000" bandwidth="193007" codecs="mp4a.40.2" id="2">
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
            <Representation audioSamplingRate="48000" bandwidth="193007" codecs="mp4a.40.2" id="4">
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
            <Representation audioSamplingRate="48000" bandwidth="193007" codecs="mp4a.40.2" id="6">
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
        </AdaptationSet>
        <SupplementalProperty schemeIdUri="urn:scte:dash:utc-time" value="2023-02-10T21:02:31.007Z"/>
    </Period>
    <Period id="155_1" start="PT22H20M45.56S">
        <BaseURL>https://777788889999.mediatailor.us-west-2.amazonaws.com/v1/dashsegment/94063eadf7d8c56e9e2edd84fdf897826a70d0df/emt/672ed481-4ffd-4270-936f-7c8403947f2e/155/155_1/</BaseURL>
        <EventStream schemeIdUri="urn:sva:advertising-wg:ad-id-signaling" timescale="90000">
            <Event presentationTime="xxxxx" duration="1351350">
                <![CDATA[{"version": 1,"identifiers": [{"scheme": "urn:smpte:ul:060E2B34.01040101.01200900.00000000","value": "155_1","ad_position": "155_1", "ad_type":"avail","creative_id": "123","tracking_uri": "../../../../v1/tracking/hashed-account-id/origin-id/session-id","custom_vast_data":"123abc"}]}]]>
            </Event>
        </EventStream>
        <AdaptationSet bitstreamSwitching="false" frameRate="30000/1001" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
            <SegmentTemplate startNumber="1" timescale="90000"/>
            <Representation bandwidth="1800000" codecs="avc1.64001f" height="540" id="1" width="960">
                <SegmentTemplate initialization="asset_540_1_2init.mp4" media="asset_540_1_2_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
            <Representation bandwidth="1200000" codecs="avc1.64001e" height="360" id="3" width="640">
                <SegmentTemplate initialization="asset_360_1_1init.mp4" media="asset_360_1_1_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
            <Representation bandwidth="800000" codecs="avc1.640015" height="270" id="5" width="480">
                <SegmentTemplate initialization="asset_270_0_0init.mp4" media="asset_270_0_0_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
        </AdaptationSet>
        <AdaptationSet lang="eng" mimeType="audio/mp4" segmentAlignment="0">
            <SegmentTemplate initialization="asset_audio_128_3init.mp4" media="asset_audio_128_3_$Number%09d$.mp4" startNumber="1" timescale="48000"/>
            <Label>eng</Label>
            <Representation audioSamplingRate="48000" bandwidth="128000" codecs="mp4a.40.2" id="6">
                <SegmentTemplate initialization="asset_audio_128_3init.mp4" media="asset_audio_128_3_$Number%09d$.mp4" startNumber="1" timescale="48000">
                    <SegmentTimeline>
                        <S d="98304" t="0"/>
                        <S d="96256" r="1" t="98304"/>
                        <S d="95232" t="290816"/>
                        <S d="96256" r="2" t="386048"/>
                        <S d="48128" t="674816"/>
                    </SegmentTimeline>
                </SegmentTemplate>
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
        </AdaptationSet>
    </Period>
    <Period id="155_2" start="PT22H21M0.575S">
        <BaseURL>https://777788889999.mediatailor.us-west-2.amazonaws.com/v1/dashsegment/94063eadf7d8c56e9e2edd84fdf897826a70d0df/emt/672ed481-4ffd-4270-936f-7c8403947f2e/155/155_2/</BaseURL>
        <EventStream schemeIdUri="urn:sva:advertising-wg:ad-id-signaling" timescale="90000">
            <Event presentationTime="0" duration="1351350">
                <![CDATA[{"version": 1,"identifiers": [{"scheme": "urn:smpte:ul:060E2B34.01040101.01200900.00000000","value": "155_2","ad_position": "155_2", "ad_type":"avail","creative_id": "234","tracking_uri": "../../../../v1/tracking/hashed-account-id/origin-id/session-id","custom_vast_data":"123abc"}]}]]>
            </Event>
        </EventStream>
        <AdaptationSet bitstreamSwitching="false" frameRate="30000/1001" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
            <SegmentTemplate startNumber="1" timescale="90000"/>
            <Representation bandwidth="1800000" codecs="avc1.64001f" height="540" id="1" width="960">
                <SegmentTemplate initialization="asset_540_1_2init.mp4" media="asset_540_1_2_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
            <Representation bandwidth="1200000" codecs="avc1.64001e" height="360" id="3" width="640">
                <SegmentTemplate initialization="asset_360_1_1init.mp4" media="asset_360_1_1_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
            <Representation bandwidth="800000" codecs="avc1.640015" height="270" id="5" width="480">
                <SegmentTemplate initialization="asset_270_0_0init.mp4" media="asset_270_0_0_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
        </AdaptationSet>
        <AdaptationSet lang="eng" mimeType="audio/mp4" segmentAlignment="0">
            <SegmentTemplate initialization="asset_audio_128_3init.mp4" media="asset_audio_128_3_$Number%09d$.mp4" startNumber="1" timescale="48000"/>
            <Label>eng</Label>
            <Representation audioSamplingRate="48000" bandwidth="128000" codecs="mp4a.40.2" id="6">
                <SegmentTemplate initialization="asset_audio_128_3init.mp4" media="asset_audio_128_3_$Number%09d$.mp4" startNumber="1" timescale="48000">
                    <SegmentTimeline>
                        <S d="98304" t="0"/>
                        <S d="96256" r="1" t="98304"/>
                        <S d="95232" t="290816"/>
                        <S d="96256" r="2" t="386048"/>
                        <S d="48128" t="674816"/>
                    </SegmentTimeline>
                </SegmentTemplate>
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
        </AdaptationSet>
    </Period>
    <Period id="155_3" start="PT22H21M15.59S">
        <BaseURL>https://777788889999.mediatailor.us-west-2.amazonaws.com/v1/dashsegment/94063eadf7d8c56e9e2edd84fdf897826a70d0df/emt/672ed481-4ffd-4270-936f-7c8403947f2e/155/155_3/</BaseURL>
        <EventStream schemeIdUri="urn:sva:advertising-wg:ad-id-signaling" timescale="90000">
            <Event presentationTime="0" duration="1351350">
                <![CDATA[{"version": 1,"identifiers": [{"scheme": "urn:smpte:ul:060E2B34.01040101.01200900.00000000","value": "155_3","ad_position": "155_3", "ad_type":"avail","creative_id": "345","tracking_uri": "../../../../v1/tracking/hashed-account-id/origin-id/session-id","custom_vast_data":"123abc"}]}]]>
            </Event>
        </EventStream>
        <AdaptationSet bitstreamSwitching="false" frameRate="30000/1001" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
            <SegmentTemplate startNumber="1" timescale="90000"/>
            <Representation bandwidth="1800000" codecs="avc1.64001f" height="540" id="1" width="960">
                <SegmentTemplate initialization="asset_540_1_2init.mp4" media="asset_540_1_2_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
            <Representation bandwidth="1200000" codecs="avc1.64001e" height="360" id="3" width="640">
                <SegmentTemplate initialization="asset_360_1_1init.mp4" media="asset_360_1_1_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
            <Representation bandwidth="800000" codecs="avc1.640015" height="270" id="5" width="480">
                <SegmentTemplate initialization="asset_270_0_0init.mp4" media="asset_270_0_0_$Number%09d$.mp4" startNumber="1" timescale="90000">
                    <SegmentTimeline>
                        <S d="180180" r="6" t="0"/>
                        <S d="90090" t="1261260"/>
                    </SegmentTimeline>
                </SegmentTemplate>
            </Representation>
        </AdaptationSet>
        <AdaptationSet lang="eng" mimeType="audio/mp4" segmentAlignment="0">
            <SegmentTemplate initialization="asset_audio_128_3init.mp4" media="asset_audio_128_3_$Number%09d$.mp4" startNumber="1" timescale="48000"/>
            <Label>eng</Label>
            <Representation audioSamplingRate="48000" bandwidth="128000" codecs="mp4a.40.2" id="6">
                <SegmentTemplate initialization="asset_audio_128_3init.mp4" media="asset_audio_128_3_$Number%09d$.mp4" startNumber="1" timescale="48000">
                    <SegmentTimeline>
                        <S d="98304" t="0"/>
                        <S d="96256" r="1" t="98304"/>
                        <S d="95232" t="290816"/>
                        <S d="96256" r="2" t="386048"/>
                        <S d="48128" t="674816"/>
                    </SegmentTimeline>
                </SegmentTemplate>
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
        </AdaptationSet>
    </Period>
    <Period id="163" start="PT80490.538S">
        <AdaptationSet bitstreamSwitching="true" id="1485523442" mimeType="video/mp4" segmentAlignment="true" startWithSAP="1" subsegmentAlignment="true" subsegmentStartsWithSAP="1">
            <SegmentTemplate initialization="index_video_$RepresentationID$_0_init.mp4?m=1676062374" media="index_video_$RepresentationID$_0_$Number$.mp4?m=1676062374" presentationTimeOffset="4829432310" startNumber="164" timescale="60000">
                <SegmentTimeline>
                    <S d="348348" t="4829432310"/>
                    <S d="360360" r="1" t="4829780658"/>
                </SegmentTimeline>
            </SegmentTemplate>
            <Representation bandwidth="1800000" codecs="avc1.4D401F" frameRate="30000/1001" height="540" id="1" width="960"/>
            <Representation bandwidth="1200000" codecs="avc1.4D401E" frameRate="30000/1001" height="360" id="3" width="640"/>
            <Representation bandwidth="800000" codecs="avc1.4D4015" frameRate="30000/1001" height="270" id="5" width="480"/>
        </AdaptationSet>
        <AdaptationSet id="1377232898" lang="eng" mimeType="audio/mp4" segmentAlignment="0">
            <Label>eng</Label>
            <SegmentTemplate initialization="index_audio_$RepresentationID$_0_init.mp4?m=1676062374" media="index_audio_$RepresentationID$_0_$Number$.mp4?m=1676062374" presentationTimeOffset="3863546862" startNumber="164" timescale="48000">
                <SegmentTimeline>
                    <S d="278528" t="3863546862"/>
                    <S d="287744" t="3863825390"/>
                    <S d="288768" t="3864113134"/>
                </SegmentTimeline>
            </SegmentTemplate>
            <Representation audioSamplingRate="48000" bandwidth="193007" codecs="mp4a.40.2" id="2">
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
            <Representation audioSamplingRate="48000" bandwidth="193007" codecs="mp4a.40.2" id="4">
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
            <Representation audioSamplingRate="48000" bandwidth="193007" codecs="mp4a.40.2" id="6">
                <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
            </Representation>
        </AdaptationSet>
        <SupplementalProperty schemeIdUri="urn:scte:dash:utc-time" value="2023-02-10T21:08:20.090Z"/>
    </Period>
</MPD>
```
