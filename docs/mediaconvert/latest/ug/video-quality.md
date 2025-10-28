# Recommended encoding settings for video quality

When you create a job with AWS Elemental MediaConvert, the encoding settings that you choose affect video
quality, file size, and player compatibility.

You can configure your job to allow MediaConvert to automatically select the best encoding settings for video
quality, with a balanced output file size. Or, you can manually specify encoding settings to match your
output or delivery requirements.

This section introduces basic concepts, describes typical settings, and provides guidance for
choosing settings optimized for video quality.

###### Topics

- [Reference for GOP structure and frame types](#gop-structure "#gop-structure")
- [GOP size recommended setting](#gop-size-settings "#gop-size-settings")
- [B-frames between reference frames recommended setting](#reference-frames "#reference-frames")
- [Closed GOP cadence recommended setting](#closed-gop-cadence "#closed-gop-cadence")
- [Dynamic sub-GOP recommended setting](#dynamic-sub-gop "#dynamic-sub-gop")
- [GOP reference B-frames recommended setting](#gop-reference-b-frames "#gop-reference-b-frames")
- [Min I-Interval recommended setting](#min-i-interval "#min-i-interval")
- [Adaptive quantization recommended setting](#adaptive-quantization "#adaptive-quantization")

## Reference for GOP structure and frame types

When you create a job, the group of pictures (GOP) settings that you choose for your output
affect video quality and player compatibility. This section introduces basic GOP concepts,
describes typical GOP settings, and provides guidance for choosing settings optimized for video
quality.

A GOP is a specific arrangement of compressed video frame types. These frame types include
the following:

**I-Frames**

Intra-coded frames. Contain all of the information that a decoder uses decode the frame.
Typically, I-frames use the most number of bits within a video stream.

**IDR-Frames**

Instantaneous Decoder Refresh frames. Similar to I-frames, they contain all of the
information that a decoder uses to decode the frame. However, frames cannot reference any
frame that comes before an IDR-frame.

**P-Frames**

Predicted frames. Contain the differences between the current frame and one or more
frames before it. P-frames offer much better compression than I-frames and use fewer bits
within a video stream.

**B-Frames**

Bidirectional predicted frames. Contain the differences between the current frame and one
or more frames before or after it. B-frames offer the highest compression and take up the
fewest bits within a video stream.

A typical GOP starts with an IDR-frame and follows with a repeating pattern of B- and
P-frames. For example: `IDRBBPBBPBBPBB`

The following topics provide more information about individual GOP settings and recommend
settings that are optimized for video quality.

## GOP size recommended setting

GOP size is the number of frames in a GOP, and it defines the interval between IDR-frames.
For example, if a GOP starts with an IDR-frame and has a combination of 29 B and P-frames, the
GOP size is 30 frames.

A typical GOP size is 1–2 seconds long and corresponds to the video frame rate. For
example, if your output frame rate is 30 frames per second, a typical GOP size is 30 or 60
frames.

When you set your output video codec to `AVC (H.264)` or `HEVC
 (H.265)`, set **GOP mode control** to `Auto`. This allows
MediaConvert to select an optimal GOP size.

###### Note

Streaming video formats, including HLS, DASH, CMAF, and MSS, require the
fragment or segment length to be a multiple of the GOP size. For more information, see [Setting
the fragment length for streaming outputs](setting-the-fragment-length.md "setting-the-fragment-length.md"). When you
set GOP mode control to Auto for these video formats, MediaConvert automatically selects a
compatible and optimized GOP size that's relative to the fragment or segment length.

## B-frames between reference frames recommended setting

Defines the maximum number of B-frames that MediaConvert can use between reference
frames.

A typical value is 1 or 2 if **GOP reference B-Frames** is set to
`Disabled`, and 3–5 if **GOP reference B-frames** is set to
`Enabled`.

When you set your output video codec to `AVC (H.264)` or `HEVC
 (H.265)`, keep **B-frames between reference frames** blank. This allows
MediaConvert to select an optimal number of B-frames between reference frames.

## Closed GOP cadence recommended setting

**Closed GOP cadence** defines the number of GOPs a P- or B-frame is able
to reference across. A GOP can either be _open_ or _closed_. Open GOPs can have frames that reference a frame from a
different GOP, while closed GOPs have frames that reference only within the GOP itself.

When you set your output video codec to `AVC (H.264)` or `HEVC
 (H.265)`, keep **Closed GOP cadence** blank to allow MediaConvert to
select an optimal closed GOP cadence.

## Dynamic sub-GOP recommended setting

A dynamic sub-GOP can improve the subjective video quality of high-motion content. It does
this by allowing the number of B-frames to vary.

When you set your output video codec to `AVC (H.264)` or `HEVC
 (H.265)`, set **Dynamic sub-GOP** to `Adaptive`. This allows
MediaConvert to determine an optimal sub-GOP.

## GOP reference B-frames recommended setting

When you set your output video codec to `AVC (H.264)` or `HEVC
 (H.265)`, set **GOP reference B-frames** to `Enabled` to allow
B-frames to be referenced by other frame types. This improves the video quality of your output
relative to its bitrate.

## Min I-Interval recommended setting

Min I-Interval enforces a minimum number of frames between IDR-frames. This includes frames
that are created at the beginning of a GOP or by scene change detection. Use Min I-Interval to
improve video compression by varying GOP size when two IDR-frames would be created near each
other.

When you set your output video codec to `AVC (H.264)` or `HEVC
 (H.265)`, keep **Min I-Interval** blank. This allows MediaConvert to
select an optimal minimum I-interval.

## Adaptive quantization recommended setting

Adaptive quantization selects the strength applied to the different quantization modes that
MediaConvert uses, including flicker, spatial, and temporal quantization. MediaConvert uses
adaptive quantization to assign bits according to the complexity of your video.

When you set your output video codec to `AVC (H.264)`, `HEVC
 (H.265)`, or `XAVC`, set **Adaptive quantization** to
`Auto` to allow MediaConvert to select an optimal adaptive quantization.
