# Including timecode metadata in the

output

You can set up a MediaLive channel to include timecode metadata in the individual output
encode. Timecode metadata is supported in any type of output group except Frame Capture.

The timecode is inserted according to the standard for the output encode:

- H.264 – The timecode is inserted in an SEI message of type pic_timing,
  in accordance with section D.1.2 of ISO/IEC 14496-10-2005
- H.265 – The timecode is inserted in an SEI message of type timecode, in
  accordance with section D.2.26 of ITU-T H.265
- MPEG – The timecode is inserted in each GOP header, in accordance with section
  6.2.2.6 of ISO/IEC 13818-2-2000 (R2006)

###### To include timecode metadata in the output

On the output side, in each video encode, you specify whether to include the
timecode. By default, the timecode is not included in the video encode.

1. On the **Create Channel** page, in the **Output
   groups** section, choose an output group, then choose an
   output.
2. Display the **Stream settings** section, and then choose the
   **Video** section. In **Codec settings**,
   choose the codec for this video encode. More fields appear.
3. Choose **Timecode**, then in **Timecode
   insertion**, choose an option:
   - **DISABLED** – This encode won't include
     timecode metadata.
   - **PIC_TIMING_SEI** (for
     AV1,
     H.264,
     or
     H.265) or
     **GOP_timecode**
     (MPEG) – This encode will include timecode metadata.
