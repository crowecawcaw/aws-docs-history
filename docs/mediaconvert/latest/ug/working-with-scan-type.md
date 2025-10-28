# Working with progressive and interlaced scan

types in AWS Elemental MediaConvert

_Progressive_ and _interlaced_ are two types of video display methods. Modern display devices
detect whether a video is interlaced or progressive and automatically play back the video
correctly. But, progressive video looks much better on modern screens.

To get the best results with using interlacing/deinterlacing and converting to and
from telecine, you must consider how your input video was recorded and what
transformations have been done to it. For example, when you apply deinterlacing to an
input that is not interlaced, your output video quality suffers.

###### Topics

- [Basic scan type vocabulary](#scan-type-vocabulary "#scan-type-vocabulary")
- [Settings for scan type
  conversion](#settings-for-scan-type-conversion "#settings-for-scan-type-conversion")
- [Converting the scan type of your
  video](converting-scan-type.md "converting-scan-type.md")
- [Valid settings combinations and requirements](valid-settings-combinations.md "valid-settings-combinations.md")

## Basic scan type vocabulary

Progressive video

_Progressive video_ includes all
lines in all frames. It looks better on modern screens because it
drastically reduces the amount of image flicker the viewer sees on the
screen. Devices displaying progressive video will re-draw all horizontal
lines in a frame. For example, a device running at 50 Hertz playing a
1080 progressive video re-draws 1080 lines (every line in the frame) 50
times per second.

Interlaced video

_Interlaced video_ uses a technique that doubles the
perceived frame rate of a video display without consuming extra bandwidth.
On older displays, most people won't notice decreased video quality with
interlaced video. Devices that support interlaced video re-draw every
_other_ horizontal line in a frame. For
example, a device running at 50 Hertz playing a 1080 interlaced video
redraws 540 lines (half of the lines in the frame) 50 times per second.

Field polarity for interlaced frames

Interlaced video contains two fields of a video frame, each one made
up of every other horizontal line the image.
_Field polarity_ in video distinguishes
between these two sets of lines. A set's polarity indicates whether the
top field comes first or bottom field comes first. In the following
illustration, the set with top field polarity is shown in blue and
contains the topmost line. The set with bottom field polarity is shown
in red and contains the second horizontal line from the top. The
complete frame contains both, with each set being refreshed
alternately.

![The illustration representing the complete frame is a square made up of alternating blue and red stripes. The top field square shows only the blue stripes, with white representing space between them. The first blue stripe is at the top of the square. The bottom field square shows only the red stripes. The first red stripe is one stripe's width below the top.](images/interlaced-field.PNG)

When you create interlaced outputs with MediaConvert, you can specify
which field polarity comes first with the setting **Interlace
mode**.

## Settings for scan type

conversion

To convert between interlaced to progressive video, specify the MediaConvert settings
covered in this topic. This topic offers conceptual information and guidance for
choosing values for the MediaConvert settings related to interlacing and deinterlacing.
For directions for specifying them, see the procedures in the topic [Configuring scan type conversion](converting-scan-type.md "converting-scan-type.md").

Valid values for some of these settings depend on what you choose for the other settings.
For a table that shows how to specify them together correctly, see [Requirements](valid-settings-combinations.md "valid-settings-combinations.md").

**Deinterlacer** preprocessor
`(Deinterlacer`)

Use this parent setting to enable and disable deinterlacing. If you simply enable the
deinterlacer without specifying any further deinterlacing settings, your job
will convert interlaced content to progressive. For the default
deinterlacing to work correctly, your input video must be interlaced and the
frames of your input video must not have metadata that tags them as
progressive.

**Deinterlace Control**
(`DeinterlacerControl`)

This setting is a child of the deinterlacer setting. You can
optionally use **Deinterlace control** to have
MediaConvert deinterlace all frames of your input video, including
those that are tagged as progressive. Only use this setting when you
know that this metadata in your input video is wrong.

**Deinterlace algorithm**
(`DeinterlaceAlgorithm)`

This setting is a child of the deinterlacer setting. You can
optionally use **Deinterlace algorithm** to specify the
way that MediaConvert does the deinterlacing to get the best quality for
your content. For sharper pictures, choose one of the motion adaptive
interpolation options (**Interpolate** or
**Interpolate ticker**). For smoother motion,
choose one of the blend options (**Blend** or
**Blend ticker**). When your source file includes
moving text, such as a scrolling headline at the bottom of the frame,
choose the ticker version of the algorithm.

**Deinterlace mode**
(`DeinterlacerMode`)

This setting is a child of the deinterlacer setting. You can
optionally use **Deinterlace mode** to modify how
MediaConvert applies deinterlacing.

Keep the default value, **Deinterlace**, to do
regular deinterlacing.

Choose **Inverse telecine** to convert hard telecine (29.97 fps,
interlaced) to progressive video at 23.976 fps. When you use inverse
telecine, you must still specify your output frame rate as 23.97.
MediaConvert doesn't automatically set this.

Choose **Adaptive** to have MediaConvert
automatically detect interlaced inputs and apply deinterlacing and
inverse telecine to them. Adaptive deinterlace mode is useful when you
use output presets, job templates, or custom programming to apply the
same job settings to transcode an entire library of assets.

###### Note

When you choose **Adaptive** for this setting,
MediaConvert automatically uses inverse telecine as
well.

**Interlace mode** (`interlaceMode`)

When you create interlaced video, from either progressive or
interlaced inputs, use this MediaConvert setting. The default value of
this setting is **Progressive**, so you can ignore this
setting unless you want an interlaced output.

###### Note

When you use an interlaced input and you keep the default setting,
**Progressive**, for **Interlace
mode**, you should also enable
**Deinterlace**. Otherwise, your progressive
output will have very poor video quality.

When you create interlaced outputs, use **Interlace
mode** to specify the [field polarity](#scan-type-vocabulary "#scan-type-vocabulary") of your outputs. You can either directly
specify the field that comes first, or you can set it to follow the
polarity of the source input. For jobs that have multiple inputs, the
output might have a mix of top and bottom field first, depending on the
polarity of the inputs.

When you set **Interlace mode** to follow the source
and your input is progressive, the output's field polarity depends on
which of the follow options you set. **Follow, top
field** results in an output that's top field first.
**Follow, bottom field** results in an output
that's bottom field first.

**Scan type** (`inputScanType`)

Use this setting only when your input is progressive segmented frame
(PsF). MediaConvert automatically detects progressive and interlaced
inputs. But it doesn't detect PsF. When your input is PsF, set
**Scan type** to **PsF** for
better preservation of quality when you do deinterlacing and frame rate
conversion.
