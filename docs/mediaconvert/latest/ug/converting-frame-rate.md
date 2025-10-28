# Converting the frame rate of your video

After you know how you want to specify the relevant settings, use one of the following procedures to set up your job. For conceptual information and guidance about choosing the right values for these settings, see

[Settings for frame
rate conversion](working-with-video-frame-rates.md#settings-for-frame-rate-conversion "working-with-video-frame-rates.md#settings-for-frame-rate-conversion").

Console
To set up your transcoding job with frame rate conversion using the
MediaConvert console:

1. Determine the values that you want to set for frame rate
   conversion. For more information, see [Settings for frame
   rate conversion](working-with-video-frame-rates.md#settings-for-frame-rate-conversion "working-with-video-frame-rates.md#settings-for-frame-rate-conversion").
2. Set up your job inputs and outputs as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
3. On the **Create job** page, in the **Job** pane on the left, choose the output that you want to use frame rate
   conversion with.

###### Tip

To find a specific encoding setting on the MediaConvert console, use
your browser's search function. 4. In the **Encoding settings** section, for
**Frame rate**, choose the frame rate that
you want for your output. If the frame rate that you want isn't
listed, choose **Custom**. Then specify your
frame rate as a fraction in the fields to the right of
**Frame rate**. 5. For **Framerate conversion algorithm**,
choose the algorithm most suited to your content.

**Framerate conversion algorithm** isn't available on the
MediaConvert console until you choose your output frame
rate. 6. Optional. If your output is 25 fps and you want to use
**Slow PAL**, enable it. 7. Optional. If you're converting from 23.976 fps to 29.97 fps
and you want to do a telecine conversion, set
**Telecine** to **Hard**
or **Soft**.

**Telecine** isn't available on the MediaConvert console until you
set your output frame rate to 29.97.

API, SDK, or CLI
If you use the API, CLI, or an SDK, specify the relevant settings in your JSON
job specification and then submit it programmatically with your job. For more
information about submitting your job programmatically, see one of the
introductory topics of the _AWS Elemental MediaConvert API
Reference_:

- [Getting started with AWS Elemental MediaConvert using the AWS SDKs or the AWS
  CLI](../apireference/custom-endpoints.md "../apireference/custom-endpoints.md")
- [Getting started with AWS Elemental MediaConvert
  using the API](../apireference/getting-started.md "../apireference/getting-started.md")

To set up your transcoding job with frame rate conversion using the
API, SDK or AWS Command Line Interface (CLI):

1. Determine the values you want to set for frame rate
   conversion. For more information, see [Settings for frame
   rate conversion](working-with-video-frame-rates.md#settings-for-frame-rate-conversion "working-with-video-frame-rates.md#settings-for-frame-rate-conversion").
2. Use the MediaConvert console to generate your JSON job specification.
   We recommend this approach, because the console functions as an
   interactive validator against the MediaConvert job schema. Follow these
   steps to generate your JSON job specification using the console:
   1. Follow the previous procedure for the console.
   2. In the **Job** pane on the left, under **Job
      settings**, choose **Show job
      JSON**.

Find additional information, including where each setting belongs in the job
settings structure, in the _AWS Elemental MediaConvert API
Reference_. Links in this list go to information about the setting
in that document:

- **Frame rate control**
  (`framerateControl`)

Use the frame rate control setting to specify whether
MediaConvert uses the frame rate of your input sources or the
frame rate that you specify with the
`framerateNumerator` and
`framerateDenominator` settings.

###### Note

The default behavior for this setting is to follow source. Therefore, if you keep
this setting out of your JSON job specification, MediaConvert
ignores any values you provide for
`framerateNumerator` and
`framerateDenominator`.

    + AV1: `framerateControl`
    + AVC (H.264): `framerateControl`
    + HEVC (H.265): `framerateControl`
    + MPEG-2: `framerateControl`
    + Apple ProRes: `framerateControl`
    + VP8: `framerateControl`
    + VP9: `framerateControl`

- **Frame rate**
  (`framerateNumerator` and
  `framerateDenominator`)

In the MediaConvert job settings schema, frame rate is
represented as a fraction, to retain precision with irrational
numbers. Therefore, specify your frame rate value as
`framerateNumerator` divided by
`framerateDenominator`. For values for common
frame rates, see the table following this list of
settings.

Links to `framerateNumerator`

    + AV1: `framerateNumerator`
    + AVC (H.264): `framerateNumerator`
    + HEVC (H.265): `framerateNumerator`
    + MPEG-2: `framerateNumerator`
    + Apple ProRes: `framerateNumerator`
    + VP8: `framerateNumerator`
    + VP9: `framerateNumerator`

Links to `framerateDenominator`

    + AV1: `framerateDenominator`
    + AVC (H.264): `framerateDenominator`
    + HEVC (H.265): `framerateDenominator`
    + MPEG-2: `framerateDenominator`
    + Apple ProRes: `framerateDenominator`
    + VP8: `framerateDenominator`
    + VP9: `framerateDenominator`

- **Frame rate conversion algorithm**
  (`framerateConversionAlgorithm`)
  - AV1: `framerateConversionAlgorithm`
  - AVC (H.264): `framerateConversionAlgorithm`
  - HEVC (H.265): `framerateConversionAlgorithm`
  - MPEG-2: `framerateConversionAlgorithm`
  - Apple ProRes: `framerateConversionAlgorithm`
  - VP8: `framerateConversionAlgorithm`
  - VP9: `framerateConversionAlgorithm`

- **Slow PAL** (`slowPal`)
  - AVC (H.264): `slowPal`
  - HEVC (H.265): `slowPal`
  - MPEG-2: `slowPal`
  - Apple ProRes: `slowPal`

- **Telecine** (`telecine`)
  - AVC (H.264): `telecine`
  - HEVC (H.265): `telecine`
  - MPEG-2: `telecine`
  - Apple ProRes: `telecine`

  - **Scan type** (`InputScanType`)

| Common frame rate ratios | Frame rate common name | Value for framerateNumerator | Value for framerateDenominator |
| ------------------------ | ---------------------- | ---------------------------- | ------------------------------ |
| 23.976                   | 24,000                 | 1,001                        |
| 29.97                    | 30,000                 | 1,001                        |
| 59.94                    | 60,000                 | 1,001                        |
