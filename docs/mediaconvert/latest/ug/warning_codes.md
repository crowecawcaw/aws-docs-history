# Warning codes

AWS Elemental MediaConvert returns warning codes when transcoding jobs run into problems that
do not prevent the job from completing. You can use Amazon EventBridge to track the warning codes
that the service returns. For more information, see [Using EventBridge with AWS Elemental MediaConvert](eventbridge_events.md "eventbridge_events.md").

The following provides detailed information about warning codes and messages that MediaConvert
returns, their possible causes, and solutions. To find information about a warning, you
can quickly find the warning code using the following links. Details for each warning are
available after the table.

**Warning codes**

[100000](#100000 "#100000") | [220000](#220000 "#220000") | [230001](#230001 "#230001") | [230002](#230002 "#230002") | [230004](#230004 "#230004") | [230005](#230005 "#230005") | [230006](#230006 "#230006") | [230007](#230007 "#230007") | [230008](#230008 "#230008") | [240000](#240000 "#240000") | [240001](#240001 "#240001") | [240003](#240003 "#240003") | [250001](#250001 "#250001") | [250002](#250002 "#250002") | [250003](#250003 "#250003") | [260000](#260000 "#260000") | [270000](#270000 "#270000")

The following is a list of warning codes and troubleshooting steps:

**100000 | Queue hop warning**

What this means: Your job waited in its original submission queue for longer than the wait time that you specified, but it couldn't move to its new destination queue. This could be because the destination queue no longer exists or has been modified.

You control hop behavior, including `Wait minutes` and the
`Destination queue`, under the **Job management Queue
hopping** settings.

Recommended actions:

- Check whether your destination queue still exists.
- No immediate action is required, but your job might take longer than expected to complete.

For more information, see `HopDestination` in the [API Reference](../apireference/jobs.md#jobs-model-hopdestination "../apireference/jobs.md#jobs-model-hopdestination").

Warning message:

**`Your job couldn't hop from its original submission queue to its
 destination queue.`**

**220000 | Input incomplete warning**

What this means: Your input file is missing data and your output's
duration might be shorter than you expect.

Recommended actions:

- Check your input for missing content.
- Verify that your file was completely uploaded to Amazon S3.
- Try re-uploading the file if necessary.

Warning message:

**`Your input file is truncated.`**

**230001 | Input color metadata warning**

What this means: MediaConvert could not follow your input's color space because
your input has missing or incomplete color metadata. Color metadata includes
color primaries, transfer function, and matrix coefficients.

Your output might have missing or inaccurate color metadata which can
cause players to inaccurately display the video contents. If you specified
`Color space conversion` in the output `Color
 corrector`, note that MediaConvert could not convert the color space and
might have written inaccurate color metadata.

Recommended actions:

- Manually specify your input's `Color space` and set
  `Color space usage` to `Force`.
- Check your output for color accuracy issues.

For more information, see `ColorSpace` in the [API Reference](../apireference/jobs.md#jobs-model-colorspace "../apireference/jobs.md#jobs-model-colorspace").

Warning message:

**`Your input's color metadata is missing or
 incomplete.`**

**230002 | Audio duration correction warning**

What this means: There is something wrong with the `'stts'` time-to-sample table in your input file container's audio track, and MediaConvert can't apply audio duration correction.

Recommended actions:

- Check your output for any audio video synchronization issues.

For more information about audio duration correction, see the [API Reference](../apireference/jobs.md#jobs-model-audiodurationcorrection "../apireference/jobs.md#jobs-model-audiodurationcorrection").

Warning message:

**`MediaConvert can't apply audio duration correction to your
 input.`**

**230004 | Input media header warning**

What this means: The `'mdhd'` media header atom in your input is incomplete or is missing data. MediaConvert expects the `'mdhd'` atom to be 32 bytes or 20 bytes.

MediaConvert might not read your input correctly, which could affect the quality or
accuracy of your output.

Recommended actions:

- Check the accuracy and quality of your output, including the total file duration and any language codes.

Warning message:

**`Your input is missing information in its `'mdhd'`
 media header atom.`**

**230005 | Input color sample range warning**

What this means: MediaConvert could not follow your input's color sample range because your input has missing or incomplete color sample range metadata.

Your output might have missing or inaccurate color sample range metadata
which can cause players to inaccurately display the video contents. If you
specified `Color space conversion` or `Sample range
 conversion` in the output `Color corrector`, note that
your output's sample range might be inaccurate.

Recommended actions:

- Manually specify your input's `Sample range`.
- Check your output for color accuracy issues.

For more information, see `SampleRange` in the [API Reference](../apireference/jobs.md#jobs-model-inputsamplerange "../apireference/jobs.md#jobs-model-inputsamplerange").

Warning message:

**`MediaConvert can't find color sample range metadata in your
 input.`**

**230006 | Input audio warning**

What this means: There's something wrong with your input's file structure or audio stream. The file might be corrupted or use non-standard encoding settings.

Your output might be missing audio content that MediaConvert couldn't
decode.

Recommended actions:

- Check your input for corruption or other audio encoding issues.
- Verify that your output contains all expected audio content.

Warning message:

**`MediaConvert can't decode a portion of your input
 audio.`**

**230007 | Input fragmented MP4 warning**

What this means: When your input is a fragmented MP4, each MOOF fragment (Movie Fragment Box) should increment sequentially. Your input has fragments that are out of order, which might cause playback issues.

Recommended actions:

- Check your output for any discontinuities or playback issues.

Warning message:

**`Your fragmented MP4 input has MOOF fragments that are out of
 order.`**

**230008 | Input MP4 decode warning**

What this means: Your MP4 input might have corrupt `NAL` units in the `AVC1` atom, and MediaConvert couldn't decode all of the video stream.

Recommended actions:

- Check your video output for issues, including problems with color, missing scene information, or gray frames.

Warning message:

**`MediaConvert can't decode a portion of your MP4 input's video
 stream.`**

**240000 | Output audio silence warning**

What this means: Your input audio track has missing, corrupt, or unexpected data. MediaConvert had to add silence to maintain proper synchronization.

Recommended actions:

- Check your output for any audio video synchronization issues.
- Verify that the audio quality meets your expectations.

Warning message:

**`MediaConvert added at least 100 milliseconds of audio silence to keep
 audio and video in sync.`**

**240001 | Output dropped audio warning**

What this means: Your input audio and video tracks were not properly synchronized. MediaConvert had to remove some audio content to maintain proper synchronization.

Recommended actions:

- Check your output for any audio video synchronization issues.
- Verify that no important audio content was lost.

Warning message:

**`MediaConvert dropped at least 100 milliseconds of audio to align audio
 and video.`**

**240003 | Output HDR10+ limited range warning**

What this means: You specified a full range HDR10+ output, but MediaConvert could only write it with a limited range because of technical constraints.

Recommended actions:

- Specify how MediaConvert converts the color sample range by using the
  Color corrector preprocessor. Set Sample range conversion to Limited
  range squeeze or Limited range clip.
- Check your output for any color accuracy issues.

Warning message:

**`MediaConvert converted your full range input into a limited range
 HDR10+ output.`**

**250001 | Input caption font warning**

What this means: You submitted an input caption with a font that MediaConvert doesn't support. MediaConvert will use a generic font instead.

Recommended actions:

- Check your output captions to ensure they display correctly with the generic font.
- If font appearance is critical, consider modifying your input captions to use a supported font.

Warning message:

**`Your input captions have an unsupported
 font.`**

**250002 | Input Dolby CBI bitrate
warning**

What this means: You submitted a Dolby CBI input with a bitrate that MediaConvert doesn't support. MediaConvert will automatically increase it to a supported bitrate.

Recommended actions:

- Check that the application generating your DOLBY CBI input is current and up to date.
- Verify that the audio quality in your output meets your expectations.

Warning message:

**`Your Dolby CBI input has an unsupported
 bitrate.`**

**250003 | Output Saliency aware encoding warning**

What this means: MediaConvert only applies Saliency aware encoding to outputs
that are 720p or higher in resolution that use Single Pass HQ or Multi Pass
HQ Quality tuning levels.

Use Saliency aware encoding to improve the perceptual video quality of
your output by allocating more encoding bits to the prominent or noticeable
parts of your content. You might receive this warning message for jobs that
specify Saliency aware encoding within an Automated ABR output, or for jobs
that use certain Presets or Templates.

Note that this warning is informational only, and no action is required if
the output quality meets your needs.

Recommended actions:

- Ensure your outputs are 720p or higher in resolution.
- Use Single Pass HQ or Multi Pass HQ Quality tuning levels.

Warning message:

**`MediaConvert can't apply Saliency aware encoding to one or more of
 your outputs.`**

**260000 | Video decoder buffer underflow warning**

What this means: The bitrate you specified for your output transport stream container is too low. It's less than the combined maximum bitrate of all output streams. This causes video decoder buffer underflow.

Recommended actions:

- Increase the container's bitrate to accommodate all the streams within it.
- Alternatively, decrease the bitrate for the video, audio, and data streams.
- Consider enabling the "Prevent buffer underflow" setting, although this can result in reduced output video quality whenever MediaConvert prevents decoder buffer underflows.

Warning message:

**`Your output transport stream exceeded the bitrate that you
 specified.`**

**270000 | Amazon S3 throttle warning**

What this means: While MediaConvert was writing your output files to your destination bucket, it was throttled by Amazon S3. This happens when you exceed your request rate limit to Amazon S3.

Recommended actions:

- Check for any other applications that are making simultaneous requests to the same Amazon S3 bucket and consider limiting them.
- Your job might stall or take longer than expected to complete, but no immediate action is required.
- For frequent issues, consider contacting Support about increasing your Amazon S3 request rate limits.

For more information, see [Troubleshooting Amazon S3](../../../AmazonS3/latest/userguide/troubleshooting.md "../../../AmazonS3/latest/userguide/troubleshooting.md").

Warning message:

**`MediaConvert received a `503 Slow Down` error code from
 Amazon S3 while writing your output to your destination
 bucket.`**
