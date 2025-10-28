# DASH manifest types

Dynamic Adaptive Streaming over HTTP (DASH) uses a Media Presentation Description (MPD) manifest to deliver streaming content. Understanding the structure and components of DASH manifests is essential for configuring and troubleshooting MediaTailor workflows.

MPD (Media Presentation Description)

The MPD is the primary manifest file in DASH streaming that describes the structure and availability of media content. It contains information about periods, adaptation sets, representations, and segments that make up the streaming content.

This manifest type is also known by several other names in various contexts:

- DASH manifest
- DASH MPD
- Master manifest (when comparing to HLS)
- Presentation manifest

In MediaTailor workflows, the MPD is the entry point for playback requests and is where ad personalization begins.

###### Example MPD manifest example

```
<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd" profiles="urn:mpeg:dash:profile:isoff-live:2011" type="dynamic" minBufferTime="PT5.000S" maxSegmentDuration="PT2.005S" availabilityStartTime="2020-01-01T00:00:00Z" publishTime="2020-01-01T12:30:00Z" minimumUpdatePeriod="PT2.000S" timeShiftBufferDepth="PT5M">
  <Period id="1" start="PT0.000S">
    <AdaptationSet id="1" contentType="video" segmentAlignment="true" bitstreamSwitching="true" frameRate="30000/1001" maxWidth="1920" maxHeight="1080" par="16:9">
      <Representation id="1" mimeType="video/mp4" codecs="avc1.640028" width="1920" height="1080" bandwidth="5000000">
        <SegmentTemplate timescale="90000" initialization="init-stream$RepresentationID$.m4s" media="chunk-stream$RepresentationID$-$Number%05d$.m4s" startNumber="1" duration="180000"/>
      </Representation>
      <Representation id="2" mimeType="video/mp4" codecs="avc1.4d401f" width="1280" height="720" bandwidth="2800000">
        <SegmentTemplate timescale="90000" initialization="init-stream$RepresentationID$.m4s" media="chunk-stream$RepresentationID$-$Number%05d$.m4s" startNumber="1" duration="180000"/>
      </Representation>
      <Representation id="3" mimeType="video/mp4" codecs="avc1.4d401e" width="640" height="360" bandwidth="1100000">
        <SegmentTemplate timescale="90000" initialization="init-stream$RepresentationID$.m4s" media="chunk-stream$RepresentationID$-$Number%05d$.m4s" startNumber="1" duration="180000"/>
      </Representation>
    </AdaptationSet>
    <AdaptationSet id="2" contentType="audio" segmentAlignment="true" lang="eng">
      <Representation id="4" mimeType="audio/mp4" codecs="mp4a.40.2" audioSamplingRate="48000" bandwidth="128000">
        <SegmentTemplate timescale="48000" initialization="init-stream$RepresentationID$.m4s" media="chunk-stream$RepresentationID$-$Number%05d$.m4s" startNumber="1" duration="96000"/>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```

Period

A Period is a temporal section of a DASH presentation. Each Period contains one or more adaptation sets and represents a span of media time. In ad insertion workflows, separate Periods are typically used to delineate between content and ads.

This component is also known by several other names:

- Content segment
- Timeline section
- Program segment

In MediaTailor workflows, Periods are used to separate main content from ad content, with each ad typically represented by its own Period.

###### Example Period example

```
<Period id="ad-period-1" start="PT30.000S" duration="PT15.000S">
  <AdaptationSet id="1" contentType="video" segmentAlignment="true" bitstreamSwitching="true" frameRate="30000/1001" maxWidth="1920" maxHeight="1080" par="16:9">
    <Representation id="1" mimeType="video/mp4" codecs="avc1.640028" width="1920" height="1080" bandwidth="5000000">
      <SegmentTemplate timescale="90000" initialization="ad1/init-stream$RepresentationID$.m4s" media="ad1/chunk-stream$RepresentationID$-$Number%05d$.m4s" startNumber="1" duration="180000"/>
    </Representation>
  </AdaptationSet>
</Period>
```

AdaptationSet

An AdaptationSet groups a set of interchangeable encoded versions of one or several media content components. For example, one AdaptationSet might contain multiple video quality levels, while another might contain multiple audio language options.

This component is also known as:

- Media component group
- Stream set
- Track group

In MediaTailor workflows, AdaptationSets are preserved during ad insertion to maintain consistent media types between content and ads.

Representation

A Representation is a specific encoded version of the media content within an AdaptationSet. Each Representation typically differs in bitrate, resolution, or other encoding parameters, allowing clients to select the most appropriate version based on network conditions and device capabilities.

This component is also known as:

- Rendition (similar to HLS)
- Quality level
- Bitrate variant
- Stream variant

In MediaTailor workflows, Representations in ad Periods are matched as closely as possible to the Representations in content Periods to ensure a smooth viewing experience.

Segment

A Segment is a unit of media data that can be referenced individually by a URL. Segments contain the actual media content (video, audio, etc.) and are referenced within the MPD. There are two main types of segments in DASH:

- **Initialization Segment**: Contains initialization information for a Representation, such as codec parameters and timing information.
- **Media Segment**: Contains the actual media data for a specific time range within a Representation.

In MediaTailor workflows, segment URLs are often modified to point to the appropriate content or ad media files.

###### Note

DASH manifests are XML-based files that typically use the `.mpd` extension. The terminology for these files and their components may vary across different documentation and contexts, but the fundamental structure remains the same in the DASH streaming architecture.

When configuring MediaTailor, you provide the URL to the MPD manifest in your content origin. MediaTailor then handles the personalization of the manifest, typically by inserting additional Periods for ads according to your configuration.

For more information about DASH manifest specifications, see the [DASH Industry Forum Implementation Guidelines](https://dashif.org/docs/DASH-IF-IOP-v4.3.pdf "https://dashif.org/docs/DASH-IF-IOP-v4.3.pdf").
