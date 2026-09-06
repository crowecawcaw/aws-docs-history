

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# One Input Format to the Same Output Format, Multiple Outputs
<a name="use-case-3-one-input-format-to-several-outputs"></a>

The input is set up with one format of captions and two or more languages. You want to maintain the format in the output. You want to produce several different types of outputs and include all the languages in all the outputs.

## Example: Pass Through Two TTML Tracks, Multiple Outputs
<a name="example:-two-outputs"></a>

The input has TTML captions in Spanish and Portuguese. You want to produce a DASH output and an MSS output. You want the DASH output to include the TTML captions in both Spanish and Portuguese and the MSS output to also include the TTML captions in both Spanish and Portuguese.

![Diagram showing input captions flowing to output captions, then to DASH and MSS outputs.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-several-1.png)
<a name="setup-3"></a>

# To set up a job for this example
<a name="setup-3"></a>

1. In the input, follow the procedure in [Creating Input Captions Selectors](create-input-caption-selectors.md) to create two caption selectors:
   + One for TTML Spanish.
   + One for TTML Portuguese.  
![Two caption selector rows showing source dropdown, external caption file path, browse button, and time delta fields.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-several-2.png)

1. Create a stream (for example, Stream 1) and set up the video and audio. 

1. Create a captions-only stream (for example, Stream 2) following the procedure for sidecar captions in the topic [Setting Up Output Captions in a Sidecar Format (SCC, SMI, SRT, TTML, WebVTT)](setting-up-output-captions-sidecar.md). Specify the captions settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: TTML. 
   + **Language**: Spanish.
   + **Pass Style Information**: Set it as desired, but you must set both languages identically.
   + **Use ID3 as Caption Content**: Leave unchecked. 

1. Create a second captions-only stream (for example, Stream 3), specifying the captions settings as follows:
   + **Caption Source**: Caption Selector 2.
   + **Language**: Portuguese.
   + Other fields: Same as the first caption stream.  
![Stream configuration interface showing three caption streams with language and destination settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-several-3.png)

1. In the DASH output group, create three outputs:
   + In the first output, set the Stream field in that output to Stream 1. 
   + In the second output, set the Stream field in that output to Stream 2.
   + In the third output, set the Stream field in that output to Stream 3.

   Although there are three outputs, they are all in the same output group, so the video/audio and two captions are kept together.   
![Three output streams with name modifiers av, ES, and PT shown in the Outputs interface.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-several-4.png)

1. In the MSS output group, create three outputs:
   + In the first output, set the Stream field in that output to Stream 1. 
   + In the second output, set the Stream field in that output to Stream 2.
   + In the third output, set the Stream field in that output to Stream 3.

   Notice that the streams in this output are also associated with the DASH output.  
![Three output streams with name modifiers ab, ES, and PT, each showing preset settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-several-5.png)

1. Save the job. 