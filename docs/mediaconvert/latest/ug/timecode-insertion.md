# Inserting timecode metadata

The **Timecode insertion** setting determines whether a given
output has timecodes embedded in its metadata. MediaConvert automatically puts this
information in the appropriate place, depending on the output codec. For MPEG-2
and QuickTime codecs, such as Apple ProRes, the service inserts the timecodes in
the video I-frame metadata. For H.265 (HEVC) and H.264 (AVC), the service
inserts the timecodes in the supplemental enhancement information (SEI) picture
timing message.

###### To include timecode metadata in an output (console)

1. On the **Create job** page, in the **Job** pane on the left, choose an output.
2. Under **Stream settings**, **Timecode
   insertion**, choose **Insert** to include
   timecode metadata. Choose **Disabled** to omit timecode
   metadata.

###### To include timecode metadata in an output (API, SDK, and AWS CLI)

- In your JSON job specification, set a value for [TimecodeInsertion](../apireference/jobs.md#jobs-prop-videodescription-timecodeinsertion "../apireference/jobs.md#jobs-prop-videodescription-timecodeinsertion"), located in `Settings`,
  `OutputGroups`, `Outputs`,
  `VideoDescription`.

Use `PIC_TIMING_SEI` to include timecode metadata. Use
`DISABLED` to omit timecode metadata.
