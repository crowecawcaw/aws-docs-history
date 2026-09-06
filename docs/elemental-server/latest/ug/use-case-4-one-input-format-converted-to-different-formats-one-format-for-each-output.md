

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# One Input Format to Multiple Different Formats, One for Each Output
<a name="use-case-4-one-input-format-converted-to-different-formats-one-format-for-each-output"></a>

The input is set up with one format of captions and two or more languages. You want to produce several different types of output. In each output, you want to convert the captions to a different format but include all the languages.

## Example: Two SRT Tracks to TTML and WebVTT
<a name="example:-two-srt-tracks-to-ttml-and-webvtt"></a>

For example, the input has SRT captions in Czech and Polish. You want to produce a DASH output and an HLS output. In the DASH output, you want to convert the same Teletext captions to TTML and include both languages. In the HLS output, you want to convert the same SRT captions to WebVTT and include both languages. 

![Workflow showing input captions converted to TTML and WebVTT formats for DASH and HLS outputs.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-different-one-each-1.png)


This example illustrates an important feature of setting up streams. The two output captions are TTML and WebVTT. WebVTT cannot be associated with the DASH output, which means that the stream that holds the WebVTT captions cannot be associated with the DASH output. This means that you must create two separate streams – one for the video, audio and captions (TTML) for DASH, another for the video, audio and captions (WebVTT) for HLS.

It looks like this means that the video is being encoded twice – an expensive operation. But that is not true. So long as the video and audio are set up to be identical in both streams, the encoder only encodes the video and audio once in the job. The source captions are, of course, processed twice.<a name="setup-4"></a>

# To set up a job for this example
<a name="setup-4"></a>

1. In the input, follow the procedure in [Creating Input Captions Selectors](create-input-caption-selectors.md) to create two caption selectors:
   + One for Teletext Czech. Specify the page that holds the Czech captions.
   + One for Teletext Polish. Specify the page that holds the Polish captions.  
![Caption Selector interface showing two selectors with Source dropdown set to Teletext and Page Numbers 890 and 896.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-different-one-each-2.png)

1. Create a stream (for example, Stream 1) and set up the video and audio. This stream is associated with the DASH output.

1. Create a second stream (for example, Stream 2) and set up the video and audio in exactly the same way as Stream 1. This stream is associated with the HLS output.

1. Create one caption stream (for example, Stream 3) following the procedure for sidecar captions in the topic [Setting Up Output Captions in a Sidecar Format (SCC, SMI, SRT, TTML, WebVTT)](setting-up-output-captions-sidecar.md). Specify the captions settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: TTML. 
   + **Language**: Czech.
   + **Pass Style Information**: Set it as desired, but you must set both languages identically for all captions (TTML and Teletext).
   + **Use ID3 as Caption Content**: Leave unchecked. 

1. Create a second caption stream (for example, Stream 4) in the same way, specifying the captions settings as follows:
   + **Caption Source**: Caption Selector 2.
   + **Language**: Polish.
   + Other fields: same as the first caption stream. 

1. Create a third caption stream (for example, Stream 5) in the same way, specifying the captions settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: WebVTT. 
   + **Language**: Czech.
   + **Pass Style Information**: Set it as desired, but you must set both languages identically for all captions (TTML and Teletext).

1. Create a fourth caption stream (for example, Stream 6) in the same way, specifying the captions settings as follows:
   + **Caption Source**: Caption Selector 2.
   + **Language**: Polish.
   + Other fields: Same as the third caption stream.  
![Streams configuration interface showing six streams with video, audio, and caption settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-different-one-each-3.png)

1. In the DASH output group, create three outputs:
   + In the first output, set the Stream field in that output to Stream 1 (the first video/audio stream). 
   + In the second output, set the Stream field in that output to Stream 3.
   + In the third output, set the Stream field in that output to Stream 4.

   Although there are three outputs, they are all in the same output group, so the video/audio and two captions are kept together.   
![Three output streams showing Stream 1 with av modifier, Stream 3 with CZ modifier, and Stream 4 with POL modifier.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-different-one-each-4.png)

1. In the HLS output group, create three outputs:
   + In the first output, set the Stream field in that output to Stream 2 (the second video/audio stream). 
   + In the second output, set the Stream field in that output to Stream 5.
   + In the third output, set the Stream field in that output to Stream 6.

   Again, although there are three outputs, they are all in the same output group, so the video/audio and two captions are kept together.  
![Three output streams with name modifiers av, CZ, and POL configured in the Outputs section.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-different-one-each-5.png)