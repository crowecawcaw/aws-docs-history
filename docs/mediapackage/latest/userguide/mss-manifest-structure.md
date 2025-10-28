# MSS manifest structure in AWS Elemental MediaPackage

This topic explains the structure and components of Microsoft Smooth Streaming (MSS)
manifests in AWS Elemental MediaPackage. Understanding the manifest structure helps you troubleshoot playback
issues and optimize your MSS streaming workflow. For step-by-step instructions on creating
MSS endpoints, see [Create an MSS manifest](endpoints-create.md#endpoints-ism "endpoints-create.md#endpoints-ism"). For
information about encrypting MSS content, see [MSS encryption and DRM in AWS Elemental MediaPackage](mss-encryption.md "mss-encryption.md").

An MSS manifest is an XML document that describes the available media streams, their
qualities, and how to access the media fragments. The main components of an MSS manifest
include:

- **SmoothStreamingMedia**: The root element containing
  metadata about the presentation, including version, timescale, and whether the
  content is live.
- **Protection**: Contains DRM information when content
  is encrypted.
- **StreamIndex**: Defines a media stream (video,
  audio, or text) and its properties.
- **QualityLevel**: Defines the available bitrates and
  encoding parameters for a stream.
- **c**: Represents a fragment (segment) with
  attributes for duration (d), timestamp (t), and repeat count (r).
  MSS manifests use the MIME type `text/xml` and are accessed using URLs that end with `.ism/Manifest` rather than `.html`.

## MSS manifest examples

Here's an example of an MSS manifest with the Full layout:

```

<?xml version="1.0" encoding="utf-8"?>
<SmoothStreamingMedia MajorVersion="2" MinorVersion="2" TimeScale="10000000"
                      CanSeek="TRUE" CanPause="TRUE" IsLive="TRUE"
                      LookaheadCount="2" DVRWindowLength="600000000" Duration="0">
  <Protection>
    <ProtectionHeader SystemID="9a04f079-9840-4286-ab92-e65be0885f95">
      TG9yZW0gaXBzdW0=
    </ProtectionHeader>
  </Protection>
  <StreamIndex Type="video" Name="video" Subtype="" Chunks="30" TimeScale="10000000"
              Url="QualityLevels({bitrate})/Fragments(v={start time})" QualityLevels="2">
    <QualityLevel Index="0" Bitrate="8000000"
                CodecPrivateData="00000001274D401FA9180A00B7602200000300020000030079CD8001E848003D09DEF701F08041380000000128FEBC80"
                FourCC="H264" MaxWidth="1280" MaxHeight="720"/>
    <QualityLevel Index="1" Bitrate="307200"
                CodecPrivateData="00000001274D401FA9180A00B7602200000300020000030079CD8001E848003D09DEF701F08041380000000128FEBC80"
                FourCC="H264" MaxWidth="720" MaxHeight="480"/>
    <c d="20000000" t="3414723000000"/>
    <c d="20000000"/>
    <c d="20000000"/>
    <c d="20000000"/>
  </StreamIndex>
  <StreamIndex Type="audio" Name="eng_1" Language="eng" Subtype="" Chunks="30"
              TimeScale="10000000" Url="QualityLevels({bitrate})/Fragments(a_9_0={start time})">
    <QualityLevel Index="0" Bitrate="129941" CodecPrivateData="1190" FourCC="AACL"
                AudioTag="255" Channels="2" SamplingRate="48000" BitsPerSample="16" PacketSize="4"/>
    <c d="20053333" t="3414723040000"/>
    <c d="20053333"/>
    <c d="20053334"/>
    <c d="19840000"/>
  </StreamIndex>
</SmoothStreamingMedia>

```

When using the Compact manifest layout, MediaPackage uses the FragmentRepeat (r) attribute to
indicate repeated segments with the same duration, significantly reducing manifest size.
Here's an example of a compact manifest:

```

<SmoothStreamingMedia MajorVersion="2" MinorVersion="2" TimeScale="10000000"
                      Duration="6000" IsLive="FALSE">
  <StreamIndex Type="video" Timescale="10000000" Name="video" Chunks="1"
              QualityLevels="1" Url="http://example.com/video/{bitrate}/{start time}">
    <QualityLevel Index="0" Bitrate="5000000" MaxWidth="1920" MaxHeight="1080"
                CodecPrivateData="00000001674D401F965405A03C59722C4840000003004000000CA3C60CA80000000168EE3C80"
                FourCC="H264" NALUnitLengthField="4"/>
    <c d="2000" t="0" r="3"/>
  </StreamIndex>
  <StreamIndex Type="audio" Timescale="10000000" Name="audio" Chunks="1"
              QualityLevels="1" Url="http://example.com/audio/{bitrate}/{start time}">
    <QualityLevel Index="0" Bitrate="128000" CodecPrivateData="1190"
                SamplingRate="44100" Channels="2" BitsPerSample="16"
                PacketSize="4" AudioTag="255" FourCC="AACL"/>
    <c d="2000" t="0" r="1"/>
  </StreamIndex>
</SmoothStreamingMedia>

```

Notice that in the compact format, the `r="3"` attribute indicates that the
segment with duration 2000 repeats 3 times, which is more efficient than listing each
segment separately.

For more information about configuring manifest layouts when creating MSS endpoints,
see [Create an MSS manifest](endpoints-create.md#endpoints-ism "endpoints-create.md#endpoints-ism"). To understand how
these manifest formats affect playback on legacy devices, see [Testing MSS playback in AWS Elemental MediaPackage](mss-testing-playback.md "mss-testing-playback.md").

## Key manifest attributes

Key attributes in the MSS manifest that you should understand:

TimeScale

Defines the timescale used for timestamps in the manifest. In the example
above, 10000000 means that time values are in units of 1/10,000,000 seconds
(0.1 microseconds).

IsLive

Indicates whether the content is live (TRUE) or video-on-demand
(FALSE).

LookaheadCount

The number of fragments that must be available before the current fragment
is made available in the manifest.

DVRWindowLength

The duration of the DVR window in TimeScale units. In the example above,
600000000 units at a timescale of 10000000 equals 60 seconds.

FourCC

Four-character code that identifies the codec used for the stream. Common
values are "H264" for video and "AACL" for audio.

For information about how these attributes affect playback behavior, see [Troubleshooting MSS endpoints in AWS Elemental MediaPackage](mss-troubleshooting.md "mss-troubleshooting.md"). To learn how to
configure these attributes when creating MSS endpoints, see [Create an MSS manifest](endpoints-create.md#endpoints-ism "endpoints-create.md#endpoints-ism").

## MSS segment structure

MSS segments are based on the ISO Base Media File Format (ISOBMFF). Unlike CMAF
segments used for DASH and HLS, MSS requires ISM segments which include specific boxes
for MSS playback:

- **Tfxd UUID Box**: Encapsulates the absolute
  timestamp and duration of a fragment in a live presentation.
- **Tfrf UUID Box**: Encapsulates the absolute
  timestamp and duration for one or more subsequent fragments of the same track in
  a live presentation (used for lookahead).
- **Senc UUID Box**: Contains the sample-specific
  encryption data, including the initialization vectors needed for decryption when
  content is protected.

MSS segments don't have a sequence number like HLS segments. Instead, the player
determines the next segment by taking the sum of the previous segment's presentation
timestamp and duration.

If you encounter issues with MSS segment playback or availability, see [Troubleshooting MSS endpoints in AWS Elemental MediaPackage](mss-troubleshooting.md "mss-troubleshooting.md") for common
problems and solutions.

For information about creating MSS endpoints, see [Create an MSS manifest](endpoints-create.md#endpoints-ism "endpoints-create.md#endpoints-ism").
