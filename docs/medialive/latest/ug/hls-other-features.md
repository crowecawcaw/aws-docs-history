# Fields for other HLS

features

###### Topics

- [Fields for
  connection retries](#hls-reconnection-fields "#hls-reconnection-fields")
- [Fields for
  contents of manifests](#hls-manifest-contents "#hls-manifest-contents")
- [Fields for
  segments](#hls-segment-fields "#hls-segment-fields")
- [Fields for
  resiliency](#hls-resiliency "#hls-resiliency")
- [Fields for DRM](#hls-drm "#hls-drm")
- [Fields for SCTE-35 ad
  avails](#hls-ad-markers "#hls-ad-markers")
- [Fields for
  captions](#hls-captions "#hls-captions")
- [Fields for ID3
  metadata](#hls-id3 "#hls-id3")

## Fields for

connection retries

The following fields in the **Output group – HLS
settings – CDN settings** section configure the
behavior for reconnecting to the downstream system:

- **Connection retry
  interval**
- **Num retries**
- **Filecache duration**
- **Restart delay**

For details about a field, choose the
**Info** link next to the field in the
MediaLive console.

## Fields for

contents of manifests

The following fields in the **HLS output group
– Manifests and Segments** section
configure the information to include in the HLS child
manifests:

- **Output selection**
- **Mode**
- **Stream inf
  resolution**
- **Manifest duration
  format**
- **Num segments**
- **I-frame only playlists**
  – This field is used to implement
  trick-play via I-frames. For more information,
  see [Trick-play track via
  I-frames](trick-play-i-frames.md "trick-play-i-frames.md").
- **Program date time (PDT)**
  – This field is used to include or exclude
  the `EXT-X-PROGRAM-DATE-TIME` tag in
  manifest files. The tag information helps
  downstream players to synchronize the stream to
  the source that's selected in the **PDT
  clock** field.
- **Program date time (PDT)
  period** – This field is used
  to set the time interval for insertion of
  `EXT-X-PROGRAM-DATE-TIME` tags,
  in seconds.
- **Program date time (PDT)
  clock** – This field is used
  to select the time source of the PDT. Output
  timecode or UTC time can be selected.
- **Client cache**
- **Timestamp delta
  microseconds**
- **Codec
  specification**
- **Manifest
  compression**

For details about a field, choose the
**Info** link next to the field in
the MediaLive console.

## Fields for

segments

The following fields configure media segments in the
output.

- The following fields in the **HLS
  output group – Manifests and
  Segments** section:
  - **TS file
    mode**
  - **Segment
    length**
  - **Keep
    segments**
  - **Min segment
    length**

- **HLS outputs** –
  **Output settings** –
  **H.265 Packaging type**.
  This field applies only to fMP4 outputs. MediaLive
  ignores the value in this field for other types.

For details about a field, choose the
**Info** link next to the field.

## Fields for

resiliency

The following field relates to implementing resiliency
in an HLS output.

- **HLS output group** –
  **HLS Settings** section
  – **Input loss
  action**

Optionally change the value of **Input loss
action**.

**Setting up for most downstream
systems**

If you're sending this HLS output to a downstream system other than
AWS Elemental MediaPackage, choose the **Info** link to decide which option to
choose. For more information, see [Handling loss of video input](feature-input-loss.md "feature-input-loss.md").

**Setting up for
MediaPackage**

If you're sending this HLS output to AWS Elemental MediaPackage, set
this field to match how you set the [channel class](channel-class.md "channel-class.md"):

- If the channel is a standard channel (to
  support input redundancy on MediaPackage), set this
  field to **PAUSE_OUTPUT**.

With this setup, if MediaLive stops producing
output on one pipeline, MediaPackage detects the lack
of content on its current input and switches to
the other input. Content loss is minimized.

(If you set this field to
**EMIT_OUTPUT**, MediaLive
sends filler frames to MediaPackage. MediaPackage doesn't
consider filler frames to be lost content, and
therefore doesn't switch to its other
input.)

- If the channel is a single-pipeline channel,
  set this field to
  **EMIT_OUTPUT**.

With this setup, if the pipeline fails in
MediaLive then MediaPackage continues delivering to its own
downstream system (although the content will be
filler frames).

(If you set this field to
**PAUSE_OUTPUT**, MediaPackage
stops updating its endpoint, which might cause
problems at the downstream system.)

## Fields for DRM

Complete the **DRM** section only if
you are setting up for DRM using a static key to encrypt
the output.

- In **Key provider** settings,
  choose **Static key**.
- Complete the other fields as appropriate. For
  details about a field, choose the
  **Info** link next to the
  field.

In a static key setup, you enter an encryption key in
this section (along with other configuration data) and
then give that key to the other party (for example, by
sending it in an email). A static key is not really a
DRM solution and is not highly secure.

MediaLive supports only a static key as an encryption
option. To use a DRM solution with a key provider, you
must deliver the output to AWS Elemental MediaPackage, by creating a[MediaPackage output group](creating-mediapackage-output-group.md "creating-mediapackage-output-group.md") instead of an HLS
output group. You then encrypt the video using MediaPackage.
For more information, see the AWS Elemental MediaPackage User Guide.

## Fields for SCTE-35 ad

avails

Complete the **Ad markers** section if you plan to
include SCTE-35 messages in the output and to decorate the HLS manifest. See
[Processing SCTE 35 messages](scte-35-message-processing.md "scte-35-message-processing.md") and specifically [Enabling passthrough for HLS
outputs](scte-35-passthrough-or-removal.md#procedure-to-enable-passthrough-hls "scte-35-passthrough-or-removal.md#procedure-to-enable-passthrough-hls").

## Fields for

captions

The following fields relate to embedded captions in an
HLS output. If your plan includes creating at least one
embedded captions encode in this HLS output, then the
following fields apply:

- In the **Captions** section,
  the **Caption language
  setting**.

You can optionally set up the HLS manifest to
include information about the languages of the
embedded captions.

- **HLS settings** section
  – **Caption language
  mappings**

You can optionally set up the HLS manifest to
include information about each CC (caption
channel) number and language.

For detailed instructions about both these fields, see
[Language information in HLS manifests](set-up-the-hls-manifest.md "set-up-the-hls-manifest.md").

## Fields for ID3

metadata

Complete the **ID3** section if you
want to insert timed ID3 metadata or ID3 segment tags
into all the outputs in this output group. For detailed
instructions, see [Inserting ID3 timed metadata when creating the MediaLive
channel](insert-timed-metadata.md "insert-timed-metadata.md").
