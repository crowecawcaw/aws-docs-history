

# Step 2: Design the workflow
<a name="s2110-out-design-workflow"></a>

Before you start to create the SMPTE 2110 output group, plan the contents, to make sure that you observe the rules for the number of video, audio, and ancillary data streams that you can include.

**Topics**
+ [Design the video](#2110-output-design-video)
+ [Design the audio](#2110-output-design-audio)
+ [Design the ancillary data](#2110-output-design-anc-data)

## Design the video
<a name="2110-output-design-video"></a>

Decide if you want the output video to be uncompressed or JPEG XS.

The output group can contain only one video output. This Elemental Live *output* represents one SMPTE 2110 *stream*. If you need multiple SMPTE 2110 streams, you must create one SMPTE 2110 output group for each.

## Design the audio
<a name="2110-output-design-audio"></a>

**Note**  
Pay attention to the terminology in this section because there is terminology from SMPTE 2110 and there is terminology from Elemental Live.   
A Elemental Live *output* is a SMPTE 2110 *stream*.   
A Elemental Live *stream* is a SMPTE 2110 *essence*.   
A Elemental Live *stream* contains *encodes*.

1. Decide how many audio outputs you need. This Live *output* represents one SMPTE 2110 *stream*. 

   Follow these guidelines:
   + You need a separate output for each variation of audio codec and bit depth/sample rate combination. For example:
     + One output for PCM audio, and one output for Dolby Digital.
     + One output for Dolby Digital Plus, and one output for Dolby Digital Passthrough.
     + One output for Dolby Digital with a bit depth of 24 and another output for Dolby Digital with a bit depth of 16.

     You don't need separate outputs for different channel configurations (PCM) or coding mode (Dolby Digital codecs). For example, in a PCM output, you can include one encode that is PCM 6-channel and one encode that is PCM 2-channel. 
   + All audio encodes that are in the same output must follow these rules:
     + They must have the same sample rate.
     + They must have the same bit depth.

     Therefore, for example, you need separate outputs if you want to produce one Dolby Digital 5.1 with 24-bit depth and another Dolby Digital 5.1 with 16-bit depth.

1. In each output, decide how many encodes you need. You need one encode for each PCM channel configuration or Dolby Digital coding-mode.

   For example, to include two PCM stereo channels (perhaps one English and one French), you need two encodes. 

   Or to include one Dolby Digital 5.1 and one Dolby Digital stereo pair, you need two encodes.

**Result of these decisions**

You will have a list of outputs, streams, and encodes. For example:
+ One PCM output containing one Elemental Live stream. The stream contains eight 2-channel encodes.
+ One Dolby Digital output containing one Elemental Live stream. The stream contains one encode, for 5.1 audio.

## Design the ancillary data
<a name="2110-output-design-anc-data"></a>

In the ancillary data, you configure the output to include or exclude embedded captions and SCTE 104 messages.

**Embedded captions**

1. If your input includes captions, you can convert those captions to embedded captions and include them in the ancillary data output. For detailed information about setting up captions, see [Setting up for captions](setting-up-for-captions.md).

1. If you decide to include embedded captions, identify the line where you want them to appear in the VANC (vertical ancillary data space) of the video stream. If you aren't sure which line to use, speak to the downstream system.

**SCTE 104 messages**

1. Decide if you want to include ad avail messages in the output. These messages can come from two sources:
   + SCTE 35 or SCTE 104 ad avail messages already present in the event input. When Elemental Live ingests the input, SCTE 104 messages are always converted to SCTE 35 messages. 
   + SCTE 35 messages that you insert when the event is running, using the API.

   In both cases, Elemental Live converts the messages to SCTE 104 messages in the SMPTE 2110 output. For general information about ad avail handling in Elemental Live, see [SCTE-35 and SCTE-104 message processing in Elemental Live](scte-message-processing.md).

1. If you decide to include ad avail messages, identify the line where you want them to appear in the VANC of the video stream.