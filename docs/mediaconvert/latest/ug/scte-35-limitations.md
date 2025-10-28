# SCTE-35 limitations

Limitations to SCTE-35 support are as follows:

- You can either specify insertion points using ESAM XML or pass through SCTE-35
  messages from the input. You can't do both.
- AWS Elemental MediaConvert supports only time_signal messages, not splice_insert
  messages.
- The service inserts SCTE-35 messages only into the following outputs:
  - Outputs in **File group** output groups with
    **MPEG-2 Transport Stream** set for
    **Container**.

  Set the container for each output under **Output
  settings**, **Container**.
  - Outputs in **DASH ISO** output groups.
  - Outputs in **Apple HLS** output groups.
  - Outputs in **CMAF** output groups.

- The service forces Instantaneous Decoder Refresh (IDR) frames at the insertion
  points specified in your ESAM XML document for the following output codecs: MPEG-2,
  MPEG-4 AVC (H.264), or HEVC (H.265).

In the [MediaConvert console](https://console.aws.amazon.com/mediaconvert/ "https://console.aws.amazon.com/mediaconvert/"), go to **Encoding settings**,
**Video**, and then set the codec for each output in the
**Video codec** section.

- **DASH ISO** and **CMAF DASH** output groups
  only support single-period manifest outputs.
