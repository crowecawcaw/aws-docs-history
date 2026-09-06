

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# One Captions Output Shared Across an Adaptive Bitrate (ABR) Package
<a name="use-case-5-one-captions-output-shared-by-multiple-video-streams"></a>

These examples show how to set up captions for streaming, adaptive bitrate (ABR) workflows. 

## Example: ABR Package with Embedded Output Captions
<a name="setup-for-embedded-caption-formats"></a>

In this example, there are three video/audio streams – one for low-resolution video, one for medium, and one for high. There is one output captions (English and Spanish embedded) that is associated with all three video/audio streams.

![Diagram showing input captions flowing to output captions and three video streams with audio.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/procedure-a-1.png)
<a name="setup-with-procedure-a-captions"></a>

# To set up a streaming output with captions that are not sidecar
<a name="setup-with-procedure-a-captions"></a>

Follow these steps if the captions are embedded in the video or are a captions object in the same stream as the video and audio.

1. In the input, follow the procedure in [Creating Input Captions Selectors](create-input-caption-selectors.md) to create one caption selector for Embedded.  
![Caption Selector 1 interface with Embedded source selected and options for channel number and upconvert settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/procedure-a-2.png)

1. Create a stream (for example, Stream 1) and set up the video and audio for low-resolution video.

1. In that same stream, set up a captions tab as described in the topic [Setting Up Output Captions for All Formats Except Sidecar](setting-up-output-captions-not-sidecar.md). Create one captions tab only and specify the settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: Embedded. 
   + **Language**: Leave blank; with embedded captions, all the languages are included.

1. Create a second stream (for example, Stream 2) and set up the video and audio for medium-resolution video.

1. Set up the second stream in the same way, specifying the captions settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: Embedded. 
   + **Language**: Leave blank; with embedded captions, all the languages are included.

1. Create a third stream (for example, Stream 3) and set up the video and audio for high-resolution video.

1. Set up the third stream in the same way, specifying the captions settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: Embedded. 
   + **Language**: Leave blank; with embedded captions, all the languages are included.  
![Three stream configurations showing caption source, destination type, and advanced settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/procedure-a-3.png)

1. In the MSS output group, create three outputs. 
   + In the first output, set the Stream field in that output to Stream 1. 
   + In the second output, set the Stream field in that output to Stream 2.
   + In the third output, set the Stream field in that output to Stream 3.  
![Three output streams with name modifiers low, medium, and high, each with preset set to None.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/procedure-a-4.png)

1. Save the job. 

## Example: ABR Package with Sidecar Output Captions
<a name="setup-for-other-caption-formats"></a>

For sidecar output formats, the setup is similar. The only real difference is that each stream may contain more than one captions tab – for example, one for English, one for Spanish, one for Portuguese.<a name="setup-with-procedure-b-captions"></a>

# To set up a streaming output with sidecar captions
<a name="setup-with-procedure-b-captions"></a>

Follow these steps if the captions are set up as sidecars – each captions track is in its own stream.

For example, there are three video/audio streams – one for low-resolution video, one for medium-resolution, and one for high-resolution. There are two output captions (English and Spanish SCC) that are associated with all three video/audio streams.

1. In the input, follow the procedure in [Creating Input Captions Selectors](create-input-caption-selectors.md) to create one caption selector for each language: 
   + **Caption Selector 1**: for SCC English.
   + **Caption Selector 2**: for SCC Spanish.

1. Create a stream (for example, Stream 1) and set up the video and audio for low-resolution video.

1. Create another stream (for example, Stream 2) and set up the video and audio for medium-resolution video.

1. Create another stream (for example, Stream 3) and set up the video and audio for high-resolution video.  
![Three stream configuration panels showing resolution, codec, and encoding settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/procedure-b-1.png)

1. Set up a captions-only stream (for example, Stream 4) for your first captions track following the procedure for sidecar captions in the topic [Setting Up Output Captions in a Sidecar Format (SCC, SMI, SRT, TTML, WebVTT)](setting-up-output-captions-sidecar.md). Specify the captions settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: SCC. 
   + **Language**: English
   + **Framerate**rate: As appropriate.

1. Set up another captions-only stream (for example, Stream 5) in the same way, specifying the captions settings as follows:
   + **Caption Source**: Caption Selector 2.
   + **Destination Type**: SCC. 
   + **Language**: Spanish
   + **Framerate**: As appropriate.  
![Caption configuration panels for Stream 4 and Stream 5 showing source selectors and language settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/procedure-b-2.png)

1. In the MSS output group, create five outputs. 
   + In the first output, set the Stream field in that output to Stream 1. 
   + In the second output, set the Stream field in that output to Stream 2.
   + In the third output, set the Stream field in that output to Stream 3.
   + In the fourth output, set the Stream field in that output to Stream 4.
   + In the fifth output, set the Stream field in that output to Stream 5.  
![Output streams configuration table showing five streams with name modifiers and settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/procedure-b-3.png)

1. Save the job. 