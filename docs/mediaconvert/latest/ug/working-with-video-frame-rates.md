# Working with frame rate conversion

The _frame rate_ of a video asset represents how
quickly video player devices play back the frames of a video, in frames per second
(fps). For example, films have a frame rate of 24 fps, NTSC television broadcasts are
29.97/59.94 fps, and PAL television broadcasts are 50/25 fps. If you keep the
MediaConvert default settings in your job, your output video will have the same frame
rate as your input video.

Some videos have a frame rate that varies over the duration of the video. For example,
some cameras automatically generate video that uses more frames for high-action
sequences and fewer frames for sequences with less motion. MediaConvert supports
variable frame rate (VFR) inputs, but creates only constant frame rate (CFR) outputs.
For more information, see [Variable frame rate inputs](using-variable-frame-rate-inputs.md "using-variable-frame-rate-inputs.md").

###### Topics

- [Settings for frame rate
  conversion](#settings-for-frame-rate-conversion "#settings-for-frame-rate-conversion")
- [Converting the frame rate of your video](converting-frame-rate.md "converting-frame-rate.md")
- [Using variable frame rate inputs
  in AWS Elemental MediaConvert](using-variable-frame-rate-inputs.md "using-variable-frame-rate-inputs.md")
- [Working with progressive and interlaced scan
  types in AWS Elemental MediaConvert](working-with-scan-type.md "working-with-scan-type.md")
- [Working with telecine in
  AWS Elemental MediaConvert](working-with-telecine-and-inverse-telecine.md "working-with-telecine-and-inverse-telecine.md")

## Settings for frame rate

conversion

To create outputs that have a different frame rate than your input, use these
MediaConvert settings:

**Frame rate** (`framerateControl`,
`framerateNumerator`,
`framerateDenominator`)

For frame rate conversion, specify a frame rate in your output encoding settings that's
different from your input video frame rate. MediaConvert will then create
an output that has the frame rate you specify, rather than the frame rate of
your input video.

Specifying your output frame rate directly in your JSON job
specification can be more complex than doing so in the MediaConvert console. For
details, see the procedure for using the API, CLI, and SDK in the topic
[Configuring frame rate conversion](converting-frame-rate.md "converting-frame-rate.md").

**Frame rate conversion algorithm**
(`framerateConversionAlgorithm`)

Choose how you want MediaConvert to increase or decrease the frame rate. The best choice for this setting depends on the
content of your video.

When you use **Drop duplicate**, MediaConvert copies or
deletes frames but doesn't alter them. This preserves the picture quality of
each individual frame, but might introduce stuttering in some conversions.
For numerically simple conversions, such as 60 fps to 30 fps, Drop duplicate
is often the best choice.

When you use **Interpolate**, MediaConvert blends frames
together to avoid the need to repeat or remove frames. This results in
smooth motion, but might introduce undesirable video artifacts. For
numerically complex conversions, Interpolate is likely to provide better
results than Drop duplicate.

When you use **FrameFormer**, MediaConvert uses the
InSync FrameFormer library. The conversion uses motion-compensated
interpolation based on the content of your input video. FrameFormer performs
various frame rate conversion techniques on a scene-by-scene basis and can
use different techniques on different regions of each frame. FrameFormer
does the conversion based on automatic detection of your source video's
underlying cadence, rather than relying on the frame rate reported in the
file's metadata.

**Feature limitations:**

- You can use FrameFormer with inputs that have resolutions up to 4K
  only. MediaConvert doesn't support FrameFormer conversion with 8K
  inputs.
- You can use FrameFormer only with jobs that you run through an
  on-demand queue. You can't use reserved queues with
  FrameFormer.

Using FrameFormer increases the transcoding time and incurs a significant
add-on cost. For more information, see the [MediaConvert pricing
page](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/").

Depending on the conversion, you might also use these settings:

**Slow PAL** (`slowPal`)

When you convert the frame rate from 23.976 or 24 frames per second (fps) to 25 fps, you
can optionally enable **Slow PAL** (slow phase alternating
line ). When you enable slow PAL, instead of duplicating frames to increase
the frame rate, MediaConvert relabels the video frames as 25 fps and
resamples your audio to keep it synchronized with the video. Slow PAL frame
rate conversion slightly reduces the duration of the video. Generally, you
use slow PAL to convert a cinema format for file-based playback or internet
streaming.

**Telecine** (`telecine`)

When you convert the frame rate from 23.976 frames per second (fps) to 29.97 fps, and
your output scan type is interlaced, you can optionally set
**Telecine** to **Hard** or
**Soft** to create a smoother picture. Generally, you
use telecine when you're preparing a video asset for broadcasting to set-top
boxes.

For more information, see [Telecine](working-with-telecine-and-inverse-telecine.md "working-with-telecine-and-inverse-telecine.md").

**Scan type** (`inputScanType`)

Use this setting only with progressive segmented frame (PsF) inputs. MediaConvert
automatically detects progressive and interlaced inputs. But it doesn't
detect PsF. When your input is PsF, set **Scan type** to
**PsF** for better preservation of quality when you do
deinterlacing and frame rate conversion.
