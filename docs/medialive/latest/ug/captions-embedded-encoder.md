

# Embedded captions encoding

You can produce embedded (CEA-608 or CEA-708) captions in an output in two ways. With encode mode, you can deliver embedded captions to players and devices that need them. This works even when the source has captions only in another format, such as Teletext.

*Passthrough mode*  
The source captions are embedded (or SCTE-20) captions. MediaLive passes the captions through to the embedded captions output. This is the original behavior for embedded captions.

*Encode mode*  
The source captions are in a non-embedded format. MediaLive generates new CEA-608 or CEA-708 embedded captions from that source.

The mode depends on the format of the source captions that feed the embedded captions output. You don't choose the mode directly.

## Encode mode sources
<a name="captions-embedded-encoder-sources"></a>

In encode mode, MediaLive can generate embedded captions from the following source formats:
+ Teletext
+ Smart Subtitles (the AWS Elemental Inference automatic subtitling feature)
+ WebVTT, from the subtitle renditions of an HLS input (see [Information for WebVTT](identify-captions-in-the-input.md#captions-webvtt-source))

MediaLive always handles embedded sources as passthrough, not encode. Other source formats, for example SCTE-20 and DVB-Sub, aren't supported as sources for embedded encode mode.

## Encode mode settings
<a name="captions-embedded-encoder-settings"></a>

In encode mode, you complete two fields on the embedded captions output. These fields map to the `EmbeddedMode` and `CaptionServiceChannel` members of the `EmbeddedDestinationSettings` in the MediaLive API.

**Embedded mode** (`EmbeddedMode`)  
This field specifies the embedded captions standard that MediaLive generates. Set the field to one of the following values:    
`EMBEDDED_608_ONLY`  
Generate CEA-608 captions only.  
`EMBEDDED_708_ONLY`  
Generate CEA-708 captions only.  
`EMBEDDED_608_AND_708`  
Generate both CEA-608 and CEA-708 captions.

**Caption service channel** (`CaptionServiceChannel`)  
An integer that identifies the caption channel. This value is both the CEA-608 caption channel and the CEA-708 service number. For example, a value of 1 means CC1 for CEA-608 and Service 1 for CEA-708. The valid range is 1 to 63, but the range that applies depends on the embedded mode. For the ranges, see [Valid channel ranges](#captions-embedded-encoder-ranges).

## Valid channel ranges
<a name="captions-embedded-encoder-ranges"></a>

The valid range for **Caption service channel** depends on the value of **Embedded mode**. CEA-608 has only four caption channels, so a value above 4 produces CEA-708 captions only.

The following table shows the valid caption service channel values for each embedded mode, and the captions that MediaLive generates.


| Embedded mode | Valid caption service channel | Result | 
| --- | --- | --- | 
| EMBEDDED\_608\_ONLY | 1–4 | MediaLive generates CEA-608 captions only. | 
| EMBEDDED\_708\_ONLY | 1–63 | MediaLive generates CEA-708 captions only. | 
| EMBEDDED\_608\_AND\_708 | 1–4 | MediaLive generates both CEA-608 and CEA-708 captions. | 
| EMBEDDED\_608\_AND\_708 | 5–63 | MediaLive generates CEA-708 captions only, because CEA-608 has only four caption channels. | 

## Encoding rules
<a name="captions-embedded-encoder-rules"></a>

The following rules apply when you set up embedded captions encoding:
+ You must specify `EmbeddedMode` and `CaptionServiceChannel` together. If you set one without the other, you get a validation error.
+ Don't set `EmbeddedMode` or `CaptionServiceChannel` for a passthrough (embedded source) configuration. If you set either field, you get a validation error.
+ Within the same output, each embedded captions encode must use a unique `CaptionServiceChannel` value.
+ Within the same output, all embedded captions encodes must use the same `EmbeddedMode` value.
+ An output can contain multiple embedded captions encodes only when they are all in encode mode. A passthrough embedded captions configuration is limited to one embedded captions encode per output.
+ Embedded captions are carried in the video elementary stream, so an embedded captions encode must be in an output that also contains video.
+ All inputs in the channel must use the same captions source type for the caption selectors that feed embedded encode mode. Input switching between different captions source types (for example, Teletext on one input and Smart Subtitles on another) into embedded encode mode isn't supported.