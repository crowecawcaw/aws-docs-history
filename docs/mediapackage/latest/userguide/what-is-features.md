# Supported features of AWS Elemental MediaPackage

MediaPackage supports the following features.

**Audio**

MediaPackage supports multi-language audio inputs and the following audio
codecs:

- AAC stereo
- Dolby AC3 and E-AC3 (Dolby Digital and Dolby Digital+)

MediaPackage accepts these codecs from the input source and passes them through
to the output stream.

Be sure to order your inputs so that your preferred audio rendition is
listed first in the audio section of the parent manifest. When packaging
audio and subtitles or captions tracks, MediaPackage designates the first audio
track as `DEFAULT=YES` and `AUTO-SELECT=YES`. This
packaging overrides default and auto-select settings from the input.

###### Important

MediaPackage doesn't support audio-only inputs. The stream configuration from
the encoder must include at least one video track.

**Captions**

Your embedded source captions can be CEA-608 captions, CEA-708 captions,
or both CEA-608 and CEA-708. MediaPackage will pass through these captions
in the media segments on TS and CMAF origin endpoints, and generate the
appropriate manifest signaling.

Be sure to order your inputs so that your preferred captions rendition is
listed first in the captions section of the parent manifest. When packaging
captions tracks, MediaPackage designates the first captions track as
`DEFAULT=YES` and `AUTO-SELECT=YES`. This
packaging overrides default and auto-select settings from the input.

###### Important

Your input HLS playlist must include captions signaling tags. If not
present, MediaPackage will not be able to generate the corresponding output
manifest signaling.

**DRM**

MediaPackage supports content protection through digital rights management (DRM).
For information, see [Content encryption and DRM in AWS Elemental MediaPackage](using-encryption.md "using-encryption.md").

**HLS Rendition Groups**

MediaPackage supports rendition groups for incoming and outgoing HLS content. For
information about output rendition groups, see [AWS Elemental MediaPackage rendition groups reference](rendition-groups.md "rendition-groups.md").

**Input Redundancy**

Input redundancy is available with only live workflows in MediaPackage.

MediaPackage creates two ingest URLs on every channel group so that you can
create input redundancy by sending two identical streams to the same
channel. For information about how input redundancy works, see [Live input redundancy AWS Elemental MediaPackage processing
flow](what-is-flow-ir.md "what-is-flow-ir.md").

**Low-latency streaming**

MediaPackage supports Apple low-latency HLS, which is a technology aimed at
reducing the delay between the time content is captured and the time it is
displayed on the viewer's screen. The goal is to achieve minimal end-to-end
delay (or "glass-to-glass" delay) by using techniques such as parallel
delivery and reduced buffering. This technology enables a more seamless and
immersive real-time viewing experience for users, particularly in
applications such as live video streaming, teleconferencing, and online
gaming.

**Subtitles**

MediaPackage supports input WebVTT text-based subtitles and passes through the
subtitles.

Be sure to order your inputs so that your preferred subtitles rendition is
listed first in the subtitles section of the parent manifest. When packaging
subtitles tracks, MediaPackage designates the first subtitles track as
`DEFAULT=YES` and `AUTO-SELECT=YES`. This
packaging overrides default and auto-select settings from the input.

**Time-shift Viewing**

Time-shift viewing is available with only live workflows in MediaPackage.

MediaPackage supports playback of a stream at a time earlier than the current
time. Start-over, catch-up TV, and time delay are all supported. For more
information about setting up time-shift capabilities, see [Time-shifted viewing with AWS Elemental MediaPackage](time-shifted.md "time-shifted.md").

**Video**

MediaPackage supports the input H.264 video codec and passes it through to the
output stream. CMAF endpoints in MediaPackage also support H.265/HEVC and HDR-10,
following the Apple specification to applicable playback devices.

###### Important

MediaPackage requires at least one video track to be present in the stream
configuration from the encoder. The service doesn't support audio-only
ingest.
