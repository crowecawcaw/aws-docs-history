

# DASH audio timeline pattern
<a name="dash-audio-timeline-pattern"></a>

In a DASH manifest, the `SegmentTimeline` element describes when each media segment is available and its duration. For audio tracks, the timescale mismatch between audio and video codecs means that audio segment durations don't always align evenly with video segment boundaries. This typically produces a repeating pattern of slightly different durations in the audio timeline. For example, an audio track might alternate between durations of 287232 and 288768 (at a timescale of 48000) in a predictable cycle.

Without patternization, the manifest must list every audio segment individually in the `SegmentTimeline`, using separate `S` elements for each duration change. As the time-shift buffer grows, the manifest grows linearly, which increases bandwidth usage and parsing time on playback devices.

When you enable the `PATTERNED` audio timeline setting, MediaPackage detects the repeating cycle of audio segment durations and represents it as a `Pattern` element in the manifest. Instead of listing each segment individually, the `SegmentTimeline` references the pattern by ID, and a single `S` element with a repeat count can describe many segments. Enabling this setting adds an `EssentialProperty` descriptor with the scheme `urn:mpeg:dash:pattern:2024` to the adaptation set. This descriptor signals to players that the manifest may contain patterned elements. The `EssentialProperty` is always present when the feature is enabled, but `Pattern` elements only appear when MediaPackage detects a qualifying repeating cycle in the audio segment durations. This follows the Segment Duration Patternization (SDP) specification from DASH-IF.

MediaPackage analyzes incoming audio segment durations and identifies repeating cycles (patterns of 2 to 6 segments). Once a pattern repeats at least twice, MediaPackage emits a `Pattern` element containing `P` sub-elements that describe the duration sequence. The `S` elements in the `SegmentTimeline` then reference this pattern using the `p` attribute (pattern ID) and the `pE` attribute (pattern entry point, indicating where in the cycle the segment begins).

If a segment arrives that doesn't match the expected pattern position, MediaPackage breaks from the pattern and represents that segment explicitly. Pattern detection then restarts. Similarly, when a discontinuity occurs (such as an input switch or stream restart), the pattern state resets and detection begins fresh on the new content.

**When to use each setting**  
Choose between the two `AudioTimelinePattern` values based on your playback environment:
+ `NONE` – The manifest uses an explicit per-segment timeline. Every audio segment duration is listed individually in the `SegmentTimeline`. Use this setting if your players don't support the DASH-IF SDP specification, or if you need maximum compatibility with older DASH clients.
+ `PATTERNED` – The manifest includes the `urn:mpeg:dash:pattern:2024` `EssentialProperty` descriptor, and may contain `Pattern` elements when MediaPackage detects repeating duration cycles in the audio segments. When patterns are present, manifest size is significantly reduced for long time-shift buffers. Use this setting when your players support this feature and you want to minimize manifest bandwidth.

**Caveats**  
Keep the following in mind when using audio timeline patterns:
+ This feature applies only to audio timelines. Video and subtitle timelines are not patternized.
+ When the `PATTERNED` setting is enabled, MediaPackage always includes the `EssentialProperty` descriptor `urn:mpeg:dash:pattern:2024` in the manifest, even if no pattern has been detected yet. If a player encounters this essential property, the manifest may contain `Pattern` elements. Players must support these elements to parse the manifest. Players that don't recognize it will reject the manifest. 
+ When a discontinuity occurs (for example, an input switch), the pattern resets. Segments around the discontinuity boundary are represented explicitly until a new pattern is detected.
+ Uniform durations (where every segment has the same duration) are not patternized because the standard `S@r` repeat count already provides optimal compression for that case.

**Example Unpatterned audio timeline**  
In this example, the audio `AdaptationSet` uses an explicit `SegmentTimeline` where every audio segment is listed individually. The durations alternate between 288768 and 287232, and the manifest grows linearly with the time-shift buffer:  

```
<AdaptationSet id="1084563256" contentType="audio" mimeType="audio/mp4" segmentAlignment="true" startWithSAP="1" bitstreamSwitching="true" lang="spa">
  <Role schemeIdUri="urn:mpeg:dash:role:2011" value="main"/>
  <Label>spa</Label>
  <SegmentTemplate timescale="48000" media="segment_$RepresentationID$_$Number$.mp4" initialization="segment_$RepresentationID$_295846802_init.mp4" startNumber="295918052" presentationTimeOffset="85206900240000">
    <SegmentTimeline>
      <S t="85224398928384" d="288768"/>
      <S t="85224399217152" d="287232"/>
      <S t="85224399504384" d="288768"/>
      <S t="85224399793152" d="287232"/>
      <S t="85224400080384" d="288768"/>
      <S t="85224400369152" d="287232"/>
      <!-- ...additional alternating S elements for each segment in the buffer... -->
      <S t="85224426577152" d="287232"/>
      <S t="85224426864384" d="288768"/>
      <S t="85224427153152" d="287232"/>
    </SegmentTimeline>
  </SegmentTemplate>
  <Representation id="audio-ac3-spa" bandwidth="128000" codecs="ac-3" audioSamplingRate="48000">
    <AudioChannelConfiguration schemeIdUri="tag:dolby.com,2014:dash:audio_channel_configuration:2011" value="A000"/>
  </Representation>
</AdaptationSet>
```

**Example Patterned audio timeline**  
The following example shows the same audio adaptation set with the `PATTERNED` setting enabled. The repeating duration cycle is defined once in a `Pattern` element, and a single `S` entry with a repeat count covers most of the timeline. A trailing `S` entry handles the final segment that doesn't complete a full pattern cycle:  

```
<AdaptationSet id="1084563256" contentType="audio" mimeType="audio/mp4" segmentAlignment="true" startWithSAP="1" bitstreamSwitching="true" lang="spa">
  <EssentialProperty schemeIdUri="urn:mpeg:dash:pattern:2024"/>
  <Role schemeIdUri="urn:mpeg:dash:role:2011" value="main"/>
  <Label>spa</Label>
  <SegmentTemplate timescale="48000" media="segment_$RepresentationID$_$Number$.mp4" initialization="segment_$RepresentationID$_295846802_init.mp4" startNumber="295918052" presentationTimeOffset="85206900240000">
    <Pattern id="008c49c1">
      <P d="287232"/>
      <P d="288768"/>
    </Pattern>
    <SegmentTimeline>
      <S t="85224398928384" r="49" p="008c49c1" pE="1"/>
      <S t="85224427153152" d="287232"/>
    </SegmentTimeline>
  </SegmentTemplate>
  <Representation id="audio-ac3-spa" bandwidth="128000" codecs="ac-3" audioSamplingRate="48000">
    <AudioChannelConfiguration schemeIdUri="tag:dolby.com,2014:dash:audio_channel_configuration:2011" value="A000"/>
  </Representation>
</AdaptationSet>
```

When you enable the `PATTERNED` setting, MediaPackage adds the `EssentialProperty` descriptor with `schemeIdUri="urn:mpeg:dash:pattern:2024"` at the `AdaptationSet` level. This descriptor signals to DASH players that the adaptation set may contain `Pattern` elements. You will never encounter pattern elements without this descriptor present, but the descriptor may be present without any pattern elements if no repeating cycle has been detected. Players that don't recognize this scheme are required by the DASH specification to ignore the adaptation set, which prevents misinterpretation of any `Pattern` elements that may be present. For this reason, only enable `PATTERNED` when your target players support `urn:mpeg:dash:pattern:2024`.

To configure the audio timeline pattern for a DASH endpoint, set the `AudioTimelinePattern` field in the [manifest configuration](endpoints-create.md#dash-manifest).