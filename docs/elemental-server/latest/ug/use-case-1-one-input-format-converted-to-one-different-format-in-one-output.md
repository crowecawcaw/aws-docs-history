

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# One Input Format to a Different Output Format, One Output
<a name="use-case-1-one-input-format-converted-to-one-different-format-in-one-output"></a>

The input is set up with one format of captions and two or more languages. You want to convert the captions to a different format in the output. You want to produce only one type of output and include all the languages in that output.

## Example: Two SRT Tracks to Two TTML Tracks
<a name="example:-easy-workflow"></a>

The input has SRT captions in German and French. You want to convert the captions to TTML and include these captions in both languages in a DASH output. 

![Workflow diagram showing SRT German and French inputs converting to TTML outputs for DASH.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-easy-workflow-1.png)
<a name="setup-1"></a>

# To set up a job for this example
<a name="setup-1"></a>

1. In the input, follow the procedure in [Creating Input Captions Selectors](create-input-caption-selectors.md) to create two caption selectors:
   + One for the German SRT file.
   + One for the French SRT file.  
![Two caption selectors with source dropdown set to SRT and external caption file paths.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-easy-workflow-2.png)

1. Create a stream (for example, Stream 1) and set up the video and audio. 

1. Create one caption stream (for example, Stream 2) following the procedure for sidecar captions in the topic [Setting Up Output Captions in a Sidecar Format (SCC, SMI, SRT, TTML, WebVTT)](setting-up-output-captions-sidecar.md). Specify the captions settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: TTML. 
   + **Language**: German.
   + **Pass Style Information**: Set it as desired, but you must set both languages identically.
   + **Use ID3 as Caption Content**: Leave unchecked. 

1. Create another caption stream (for example, Stream 3) following the procedure for sidecar captions in the topic [Setting Up Output Captions in a Sidecar Format (SCC, SMI, SRT, TTML, WebVTT)](setting-up-output-captions-sidecar.md). Specify the captions settings as follows:
   + **Caption Source**: Caption Selector 2.
   + **Language**: French.
   + Other fields: same as the first caption stream.   
![Stream configuration interface showing video, audio, and caption settings for three streams.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-easy-workflow-3.png)

1. In the DASH output group, create three outputs:
   + In the first output, set the Stream field in that output to Stream 1. 
   + In the second output, set the Stream field in that output to Stream 2.
   + In the third output, set the Stream field in that output to Stream 3.

   Although there are three outputs, they are all in the same output group, so the video/audio and two captions are kept together.  
![Three output streams with name modifiers av, DE, and FR in a single output group.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-easy-workflow-4.png)