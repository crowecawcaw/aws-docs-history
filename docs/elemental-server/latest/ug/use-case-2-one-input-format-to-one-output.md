

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# One Input Format to the Same Output Format, One Output
<a name="use-case-2-one-input-format-to-one-output"></a>

The input is set up with one format of captions and two or more languages. You want to maintain the format in the output. You want to produce only one type of output and include all the languages in that output.

## Example: Pass Through Embedded Captions to an HLS Output
<a name="example:-embedded-to-embedded-in-hls"></a>

The input has embedded captions in English and Spanish. You want to produce HLS output that includes embedded captions in both English and Spanish.

![Diagram showing input captions in Embedded English and French flowing to output captions and Output 1 HLS.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-one-1.png)


This example illustrates two important features of an embedded-to-embedded workflow. First, you do not create separate caption selectors; all of the languages are all automatically included. Secondly, if you are outputting to HLS, there is an opportunity to specify the languages and the order in which they appear.<a name="setup-2"></a>

# To set up a job for this example
<a name="setup-2"></a>

1. In the input, follow the procedure in [Creating Input Captions Selectors](create-input-caption-selectors.md) to create one caption selector for Embedded.  
![Caption Selector 1 interface with Embedded source selected and options for channel number and upconvert settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-one-2.png)

1. Create a stream (for example, Stream 1) and set up the video and audio. 

1. In that same stream, set up a captions tab as described in the topic [Setting Up Output Captions for All Formats Except Sidecar](setting-up-output-captions-not-sidecar.md). Create one captions tab only and specify the settings as follows:
   + **Caption Source**: Caption Selector 1.
   + **Destination Type**: Embedded. 
   + **Language**: Leave blank; with embedded captions, all the languages are included.  
![Stream 1 configuration showing caption source, destination type, language, and description fields.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-one-3.png)

1. In the HLS output group, create an output. In the Output section, set the Stream field in that output to Stream 1.   
![Output settings interface with Stream 1 selected and options for Name Modifier and Advanced settings.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-one-4.png)

1. Still in the Output Group section (not in the Output section), click **Advanced**. In Caption Languages, choose **Insert**. The CC Language fields appear:
   + Set up CC1 as English.
   + Set up CC2 as French.  
![Caption Languages form with dropdown menus for CC1 through CC4 language selection and description fields.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/example-one-to-one-5.png)

1. Save the job. 