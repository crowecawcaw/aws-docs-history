This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Image Processing – Scan Type – Secondary Fields

## Description

The scan type of the input can be converted to a different scan type: progressive,
interlaced, hard telecine, or soft telecine. You can configure to leave the scan type as is or
to convert from one incoming type (or a mix of incoming scan types) to another single type.
Configuring for scan type conversion involves setting fields in specific ways.

**Force Deinterlace**

The field applies only when the Deinterlacer Preprocessor is turned on. It deals with
issues of badly tagged frames.

- When the **Deinterlace Mode** is Adaptive, set **Force Mode** to Off.
- When the **Deinterlace Mode** is Deinterlace, use **Force Mode** as follows:
  - **Off**: The processor does not convert frames that are
    tagged in metadata as "progressive." It only converts those that are tagged as some other
    type.
  - **On**: The processor converts every frame to
    "progressive" – even those that are already tagged as "progressive." Turn **Force** **Mode** on only if the input
    frames are incorrectly marked as "progressive." Do not turn otherwise; processing frames
    that are already tagged as "progressive" degrade video quality.

- When the **Deinterlace Mode** is Inverse Telecine, use
  **Force Mode** as follows:
  - Off: The processor monitors presence/absence of the hard telecine field repeat
    cadence and applies only to hard telecine to progressive conversion on frames that have a
    distinct cadence.
  - On: The processor still monitors for hard telecine cadence and adapts to cadence,
    but all frames are converted from hard telecine to progressive using the last detected
    cadence.

**Deinterlace Algorithm**

The field applies only when the Deinterlacer Preprocessor is turned on and when the
**Deinterlace Mode** is set to **Deinterlace**
or **Adaptive**. Set it to the desired value:

- Motion adaptive interpolation: Provides for better spatial quality (i.e. produces
  sharper images).
- Motion adaptive blend: Provides for better temporal quality (i.e. produces smoother
  motion).
- Low latency interpolation: Performs interpolated line-doubling to allow for lower
  latency applications.

## Location of Fields

| Location of Field on Web Interface                                       | Location of Tag in XML                                                       |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Streams > Advanced >Preprocessors > Deinterlacer > Deinterlace Algorithm | stream_assembly/video_description/video_preprocessors/deinterlacer/algorithm |
| Streams > Advanced >Preprocessors > Deinterlacer > Force Mode            | stream_assembly/video_description/video_preprocessors/deinterlacer/force     |
