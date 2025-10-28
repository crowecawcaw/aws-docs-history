# Working with VOD sources

A VOD source represents a single piece of content, such as a video or an episode of a
podcast, that you add to your source location. You add one or more VOD sources to your
source location, and then associate each VOD source with a program after you create your
channel.

Each VOD source must have at least one _package
configuration_. A package configuration specifies a package format,
manifest location, and source group for your VOD source. When you create your channel,
you use the package configuration's source groups to create the corresponding outputs on
your channel. For example, if your source is packaged in two different formats—HLS and
DASH—then you'd create two package configurations, one for DASH and one for HLS. Then,
you would create two channel outputs, one for each package configuration. Each channel
output provides an endpoint that's used for playback requests. So, using the preceding
example, the channel would provide an endpoint for HLS playback requests and an endpoint
for DASH playback requests.

If you would like the offsets of ad markers in your manifest to be detected
automatically, each ad marker must appear at the same offset across all package
configurations and have a duration of zero. For HLS, MediaTailor will detect `DATERANGE`
and `EXT-X-CUE-OUT` tags. For DASH, HLS will detect the first Event tag within each
`EventStream` tag.

In the following example, an ad break opportunity will be detected at an offset of
12000ms because of the `DATERANGE` tag with a duration of 0.0. The first
`DATERANGE` tag at an offset of 0ms will not be detected because it has a
duration of 10.0.

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:6
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-DATERANGE:ID="1001",START-DATE="2021-09-16T23:51:05.249Z",DURATION=10.0,SCTE35-OUT=0xFC302500000003289800FFF01405000003E97FEFFE1D381BD8FE000DBBA00001010100000FD2B275
#EXTINF:6.000,
../../../719f911124e0495cbb067c91c1d6c298/1785a16ca14d4c2884781f25333f6766/index_1_0.ts
#EXTINF:6.000,
../../../719f911124e0495cbb067c91c1d6c298/1785a16ca14d4c2884781f25333f6766/index_1_1.ts
#EXT-X-DATERANGE:ID="1001",START-DATE="2021-09-16T23:51:05.249Z",DURATION=0.0,SCTE35-OUT=0xFC302500000003289800FFF01405000003E97FEFFE1D381BD8FE000DBBA00001010100000FD2B275
#EXTINF:6.000,
../../../719f911124e0495cbb067c91c1d6c298/1785a16ca14d4c2884781f25333f6766/index_1_2.ts
```

In the following example, an ad break opportunity will be detected at an offset of 0ms
because the `EXT-X-CUE-OUT` tag has a duration of 0 and is followed immediately by an
`EXT-X-CUE-IN` tag. The second `EXT-X-CUE-OUT`/`EXT-X-CUE-IN` pair will not be detected
because it has a duration of 10.

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:6
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-CUE-OUT:0
#EXT-X-CUE-IN
#EXTINF:6.000,
../../../719f911124e0495cbb067c91c1d6c298/1785a16ca14d4c2884781f25333f6766/index_1_0.ts
#EXTINF:6.000,
../../../719f911124e0495cbb067c91c1d6c298/1785a16ca14d4c2884781f25333f6766/index_1_1.ts
#EXT-X-CUE-OUT:10
...
#EXT-X-CUE-IN
#EXTINF:6.000,
../../../719f911124e0495cbb067c91c1d6c298/1785a16ca14d4c2884781f25333f6766/index_1_2.ts
```

In the following example, an ad break opportunity will be detected at an offset of 0ms
because the first Event in the `EventStream` occurs in the period starting at PT0.000S.
The second `Event` in the `EventStream` will not be detected.

```
<Period start="PT0.000S" id="9912561" duration="PT29.433S">
<EventStream timescale="90000" schemeIdUri="urn:scte:scte35:2013:xml">
<Event duration="0">
  <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="1241950593" tier="4095">
    <scte35:SpliceInsert spliceEventId="99" spliceEventCancelIndicator="false" outOfNetworkIndicator="true" spliceImmediateFlag="false" uniqueProgramId="1" availNum="1" availsExpected="1">
      <scte35:Program><scte35:SpliceTime ptsTime="3552273000"/></scte35:Program>
      <scte35:BreakDuration autoReturn="true" duration="2700000"/>
    </scte35:SpliceInsert>
  </scte35:SpliceInfoSection>
</Event>
<Event duration="0">
  <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="1241950593" tier="4095">
    <scte35:SpliceInsert spliceEventId="99" spliceEventCancelIndicator="false" outOfNetworkIndicator="true" spliceImmediateFlag="false" uniqueProgramId="1" availNum="1" availsExpected="1">
      <scte35:Program><scte35:SpliceTime ptsTime="3552273000"/></scte35:Program>
      <scte35:BreakDuration autoReturn="true" duration="2700000"/>
    </scte35:SpliceInsert>
  </scte35:SpliceInfoSection>
</Event>
</EventStream>
  ...
</Period>
```
