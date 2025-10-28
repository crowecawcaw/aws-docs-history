# Features of AWS Elemental MediaPackage

MediaPackage supports the following features:

**Accessibility support**

MediaPackage supports audio and subtitles accessibility signaling for HLS, CMAF,
and DASH VOD assets that are created from an HLS source.

- Audio accessibility signaling supports functionality like
  Descriptive Voice Services (DVS) to help make media accessible to
  people who are blind or visually impaired. For example, an audio
  track might be used to provide an audio description of the
  scene.
- Subtitles accessibility signaling helps make media accessible to
  people who are deaf or hard of hearing. For example, a subtitles
  track might be used to provide description of music and sound
  effects in the video.

To enable players to provide accessibility signaling, MediaPackage passes through
the `EXT-X-MEDIA` tag and attributes from the source
playlist.

###### Important

The `EXT-X-MEDIA` tag must include a
`CHARACTERISTICS` attribute with an appropriate value for
accessibility signalling to work.

- For audio accessibility, the value must be
  `public.accessibility.describes-video`.
- For subtitles accessibility, the value must include one or
  both of
  `public.accessibility.describes-music-and-sound`
  and
  `public.accessibility.transcribes-spoken-dialog`.

###### Example EXT-X-MEDIA tag with accessibility caption attribute

`#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="captions-group",NAME="accessibility-captions1",LANGUAGE="eng",
 CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound",AUTOSELECT=YES,DEFAULT=YES,URI="caption-accessibility-eng.m3u8"`

**Allow listing**

Allow listing is available with only live workflows in
MediaPackage.

MediaPackage supports restricting network access to the endpoint. To take
advantage of this feature, you must enter the allowed IP addresses on the
endpoint. For more information about adding allow listing information, see
[Access control settings fields](endpoints-hls-access-control.md "endpoints-hls-access-control.md").

**Audio**

MediaPackage supports multi-language audio inputs and the following audio
codecs:

- AAC stereo
- Dolby AC3 and E-AC3 (Dolby Digital and Dolby Digital+)

MediaPackage accepts these codecs from the input source and passes them
through to the output stream.

Be sure to order your inputs so that your preferred audio rendition is
listed first in the audio section of the parent manifest. When packaging
audio and subtitles or captions tracks, MediaPackage designates the first audio
track as `DEFAULT=YES` and `AUTO-SELECT=YES`. This
packaging overrides default and auto-select settings from the input.

###### Important

MediaPackage doesn't support audio-only inputs. The stream
configuration from the encoder must include at least one video
track.

**Captions**

Your embedded source captions can be CEA-608 captions, CEA-708 captions,
or both CEA-608 and CEA-708. MediaPackage will pass through these captions
in the media segments and parent manifest on HLS, CMAF, and DASH endpoints,
and generate the appropriate manifest signaling.

Be sure to order your inputs so that your preferred captions rendition is
listed first in the captions section of the parent manifest. When packaging
captions tracks, MediaPackage designates the first captions track as
`DEFAULT=YES` and `AUTO-SELECT=YES`. This
packaging overrides default and auto-select settings from the input.

###### Important

Your input HLS playlist must include captions signaling tags. If not
present, MediaPackage will not be able to generate the corresponding output manifest
signaling.

**CDN Authorization**

MediaPackage supports content delivery network (CDN) authorization. For information, see [CDN authorization in AWS Elemental MediaPackage](cdn-auth.md "cdn-auth.md").

**DRM**

MediaPackage supports content protection through digital rights
management (DRM). For information, see [Content encryption and DRM in AWS Elemental MediaPackage](using-encryption.md "using-encryption.md").

**HLS Rendition Groups**

MediaPackage supports rendition groups for incoming and outgoing HLS
content. For information about output rendition groups, see [Rendition groups reference in AWS Elemental MediaPackage](rendition-groups.md "rendition-groups.md").

**Live to VOD**

Use the harvest job resource to extract a live-to-VOD (video on demand)
asset from a live content stream. MediaPackage creates the asset and stores
it in an Amazon S3 bucket. You can use the VOD functionality in MediaPackage to
deliver the asset to end users.

**Input Redundancy**

Input redundancy is available with only live workflows in
MediaPackage.

MediaPackage creates two input URLs on every channel so that you can
create input redundancy by sending two identical streams to the same
channel. For information about how input redundancy works, see [Live input redundancy AWS Elemental MediaPackage processing
flow](what-is-flow-ir.md "what-is-flow-ir.md").

**Subtitles**

MediaPackage supports input WebVTT text-based subtitles. MediaPackage
translates the subtitles to the appropriate format based on the packager
that's used on the endpoint:

- For HLS and CMAF: WebVTT is passed through
- For DASH: subtitles are translated to EBU-TT
- For Microsoft Smooth Streaming: subtitles are translated to
  DFXP

Be sure to order your inputs so that your preferred subtitles rendition is
listed first in the subtitles section of the parent manifest. When packaging
subtitles tracks, MediaPackage designates the first subtitles track as
`DEFAULT=YES` and `AUTO-SELECT=YES`. This
packaging overrides default and auto-select settings from the input.

**Time-shift Viewing**

Time-shift viewing is available with only live workflows in
MediaPackage.

MediaPackage allows playback of a stream at a time earlier than the
current time. Start-over, catch-up TV, and time delay are all supported. For
more information about setting up time-shift capabilities, see [Time-shifted viewing reference in AWS Elemental MediaPackage](time-shifted.md "time-shifted.md").

**Video**

MediaPackage supports the input H.264 video codec and passes it through
to the output stream. CMAF endpoints in
MediaPackage also support H.265/HEVC and HDR-10, following the Apple
specification to applicable playback devices.

###### Important

MediaPackage requires at least one video track to be present in the
stream configuration from the encoder. The service doesn't support
audio-only ingest.
