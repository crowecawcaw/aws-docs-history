# Step 3: Create SMPTE 2110 output group

In a SMPTE 2110 output group, you create one output for the single video, for each
audio, and for the single (optional) ancillary data stream.

###### Topics

- [General procedure](#2110-output-general-procedure "#2110-output-general-procedure")
- [Set up the video stream](#2110-output-video "#2110-output-video")
- [Set up the audio stream](#2110-output-audio "#2110-output-audio")
- [Set up the ancillary data stream](#2110-output-anc-data "#2110-output-anc-data")

## General procedure

Follow this procedure to create an SMPTE 2110 output. This procedure applies if your
organization uses NMOS IS-04 and IS-05, and if it doesn't.

###### Note

Pay attention to the terminology in this section because there is terminology from
SMPTE 2110 and there is terminology from Elemental Live.

An Elemental Live _output_ is a SMPTE 2110
_stream_.

A Elemental Live _stream_ is a SMPTE 2110
_essence_.

A Elemental Live _stream_ contains _encodes_.

###### To configure a SMPTE 2110 output

To create a SMPTE 2110 output on the web interface, you create one SMPTE 2110
output group that contains one output for video, one output for audio, and
(optionally) one output for ancillary data. The video output contains one stream that
contains one video.

1. On the web interface for the event, scroll down to the **Additional
   Global Configuration** section.

Open the section and choose **Low
Latency
Mode**. We recommend that you enable this field for
any event that includes SMPTE 2110 outputs. 2. Scroll down to the **Output Groups** section and choose the
**SMPTE 2110** tab. 3. In the output group section, complete the **NMOS Control**
field:

    * Check this field if your organization has an NMOS registry.
    * Otherwise, leave the field unchecked.

4. Choose **Add Output** on the far right of the page. A new
   output section appears, with a reference to one Elemental Live stream. For
   example, _Stream 1_. Assume that this stream is
   for video.
5. Choose **Add Output** again for each audio output you want to
   include. You should have identified the output you need when you [designed the audio output](s2110-out-design-workflow.md#2110-output-design-audio "s2110-out-design-workflow.md#2110-output-design-audio"). Each time
   you add an output, a new output section appears, with a reference to one Elemental
   Live _stream_. For example, _Stream 2_.
6. Optionally, choose **Add Output** again to create an output
   for ancillary data. A new output section appears, with a reference to one
   Elemental Live stream. For example, _Stream 3_.

Scroll down to the **Streams** section. There is one Elemental
Live stream for each output you created. 7. To set up the video stream (for example, Stream 1), hover over **Audio
1** and click **x**. The stream now contains only a
video stream. 8. To set up each audio stream (for example, Stream 2), hover over
**Video** and click **x**. The stream now
contains only an audio stream. If you scroll back up to the output that references
this stream, you'll see that there is now an **Audio Settings**
section. 9. To set up the ancillary data stream (for example, Stream 3), hover over
**Audio 1** and click **x**. Then click
**Caption +**. The stream now contains a video stream and a
captions stream. If you scroll back up to the output that references this stream,
you'll see that there is now an **Ancillary Data Settings**
section. 10. To set up the content of the video, audio, and ancillary data streams, see the
sections [Set up the video stream](#2110-output-video "#2110-output-video"), [Set up the audio stream](#2110-output-audio "#2110-output-audio"),
and [Set up the ancillary data stream](#2110-output-anc-data "#2110-output-anc-data"). 11. When you save the event, Elemental Live creates an SDP file for each output you
included in the output group. The files are stored on your appliance at this
location:

`http://locahost/<filename>`

For information about the file name, see [Step 4: Download and post the SDP file](locate-sdp.md "locate-sdp.md"). 12. Follow the appropriate step with the SDP files:

    * If you enabled NMOS in the output group, Elemental Live automatically
     sends the SDP file to your registry, and your registry processes the
     information in each file. You don't need to do anything with the
     files.
    * If you didn't enable NMOS, you can download this file so that you can
     make it available to the downstream system for this output. See [Step 4: Download and post the SDP file](locate-sdp.md "locate-sdp.md").


    You must put the files on an HTTP server that is accessible to the
     downstream system.

## Set up the video stream

Follow this procedure to set up the video stream.

###### To set up the video stream

1.  Complete the **Outputs** section:
    - **RTP Payload Type** – Enter a
      number for the type. For example, `96` for a
      video stream. If you aren't sure what number to enter,
      speak to the administrator of the downstream
      system.

    This number will appear in the **m= line** in the SDP
    file.
    - **Primary Destination** and **Secondary
      Destination** – These fields appear only if the **NMOS
      Control** field is unchecked. Complete the two fields in one of
      these ways:

          + If you are not implementing seamless protection switching, complete
           only the primary destination.
          + If you are implementing seamless protection switching, complete
           both destinations fields, one interface for the primary stream, the
           other for the secondary stream.

      Enter the unicast or multicast address to deliver the video stream to.
      For example:

    `rtp://239.x.x.x:5000`

    This information will appear in the SDP file.
    - **Interface** – complete these two fields in one of
      these ways:
      - If you are not implementing seamless protection switching, complete
        only **Interface**.
      - If you are implementing seamless protection switching, complete
        both **Interface** fields, one interface for the
        primary stream, the other for the secondary stream.

2.  Complete the **Streams** section for the
    video (for example, Stream 1):

        * **Video Codec** – Choose the codec that you identified
         when you [designed the
         video](s2110-out-design-workflow.md#2110-output-design-video "s2110-out-design-workflow.md#2110-output-design-video").
        * **Interlace Mode** – Choose
         **Progressive** or
         **Interlaced**.
        * **FourCC** (Uncompressed only) – Choose **s210
         (10-bit 4:2:2 packed)**.
        * **Compression Ratio** (JPEG XS only) – Choose the
         compression that the downstream system has requested.
        * **Resolution - Width** – Enter a value that meets one of
         the following conditions:




        	+ A value between 352 and 1152. The value must be divisible by 4.
        	+ A value between 1160 and 2048. The value must be divisible by 8.
        	+ A value between 2054 and 4096. The value must be divisible by
        	 16.
        * **Resolution - Height** – Enter a value that meets one
         of the following conditions:




        	+ If **Interlace Mode** is Progressive – a value of
        	 240 or more. The value must be divisible by 4.


        	If **Interlace Mode** is Interlaced – a value of
        	 240 or more. The value must be divisible by 8.


        * Complete other fields according to your preference.

    Many of the fields in this section appear in the `a=ftmp` line in
    the SDP file.

## Set up the audio stream

###### To set up the audio stream

Follow this procedure to set up each audio stream.

1. Complete the **Outputs** section in the same way that you
   completed the section for the video. Make sure that you enter an RTP payload type
   that is unique in this SMPTE 2110 output group.

For information about the packet time, see the information after this procedure. 2. Add more encodes to each stream, according to [your design](s2110-out-design-workflow.md#2110-output-design-audio "s2110-out-design-workflow.md#2110-output-design-audio"). For example, if your
design includes an output that must contain four stereo PCM channels, you need
four encodes in the stream. 3. Complete the **Streams** section for the
video (for example, Stream 1):

    * **Audio Source** – Choose the input selector that
     identifies the source for this audio. You previously set up this selector in
     the Input section of the event.
    * **Audio Codec** – Choose the codec you identified for
     this stream when you designed the audio. Choose the same audio codec for all
     the encodes in this Elemental Live stream.


    * **Channels** (PCM only) – Set the number of channels you
     identified for this audio when you designed the audio.
    * **Coding Mode** (Dolby Digital and Dolby Digital Plus) –
     Choose the mode you identified for this audio when you designed the
     audio.
    * **Sample Rate** (PCM only) – See the information after
     this procedure.
    * **Bit Depth** – Choose a value. Choose the same value
     for all the encodes in this Elemental Live stream.
    * Complete other fields according to your preference. For Dolby Digital and
     Dolby Digital Plus, some of the remaining fields relate to Dolby metadata.
     For more information, see [Working with Dolby metadata](dolby-metadata.md "dolby-metadata.md").

Many of the fields in this section appear in the `a=ftmp` line in
the SDP file.

**Setting the sample rate and packet rate for PCM
audio**

Complete the **Sample Packet** (in the stream section) and the
**Packet Time** field (in the output section). Follow this
procedure:

- Identify the number of audio channels in all the encodes in this Elemental Live
  stream.
- Choose a sample rate and a packet time that both fall within the limits for the
  number of channels, as specified in the following table.
- Set the same sample rate for every encode in the Elemental Live stream.

| Number of audio channels | Maximum sample rate (Hz) | Maximum packet time (microseconds) |
| ------------------------ | ------------------------ | ---------------------------------- |
| Up to 4                  | 96,000                   | 1000                               |
| Up to 8                  | 48,000                   | 1000                               |
| Up to 32                 | 96,000                   | 125                                |
| Up to 64                 | 48,000                   | 125                                |

**Setting the packet rate for any of the Dolby
codecs**

Complete the **Packet Time** field (in the output section). Follow
this procedure:

- Identify the number of audio tracks in all the encodes in this Elemental Live
  stream.
- Choose a packet time that falls within the limits for the number of tracks, as
  specified in the following table.

| Number of audio tracks | Packet time (microseconds)     |
| ---------------------- | ------------------------------ |
| Up to 3                | 125 or 1000. We recommend 1000 |
| Up to 24               | 125                            |

Note that the sample rate is always 48,000 Hz.

## Set up the ancillary data stream

###### To set up the ancillary data stream

You set up the ancillary data stream to include embedded captions. You can
optionally configure how you want to handle ad avails. These ad avails might be in
the source and/or might be ad avails that you insert using the API.

1. Complete the **Outputs** section in the same way that you
   completed the section for the video. Make sure you enter an RTP payload type that
   is unique in this SMPTE 2110 output group.
2. Complete the video stream for this output so that it is identical to the video
   that you set up in the video output. In our example, the video stream in this
   ancillary data output is stream 3, and the video in the video output is stream 1.
3. If you want to pass through ad avails, complete these fields in the
   **Outputs** section:
   - **Enable SCTE 35 Passthrough** – Set the check box to
     checked.
   - **SCTE 104 messages line number** – Enter the line
     number that you identified when you [designed the ancillary
     data](s2110-out-design-workflow.md#2110-output-design-anc-data "s2110-out-design-workflow.md#2110-output-design-anc-data").

4. If you want include embedded captions in the output, follow this
   procedure:
   - Make sure that you have set up the event so that the captions in the
     input are converted to embedded captions in the output (or that the embedded
     source captions are passed through). For information about setting up
     captions, see [Setting up for captions](setting-up-for-captions.md "setting-up-for-captions.md").
   - In the **Outputs** section for the ancillary data, for
     **CEA-608-E captions line number**, enter the line
     number that you identified when you [designed the ancillary
     data](s2110-out-design-workflow.md#2110-output-design-anc-data "s2110-out-design-workflow.md#2110-output-design-anc-data").
