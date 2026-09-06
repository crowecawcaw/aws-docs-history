

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Gathering Required Captions Information
<a name="gather-required-captions-information"></a>

To choose an appropriate output captions format and to set up your captions in your job, you need the following information:
+ The *input video container*. You must have this information ahead of time; AWS Elemental Server does not read this from your input files. For a list of supported input containers and information about whether captions can be extracted from them, see [Reference: Supported Input Containers](supported-containers-input.md).
+ The *input captions format*. You must have this information ahead of time; AWS Elemental Server does not read this from your input files. For a list of supported input captions, see [Reference: Supported Captions Formats](supported-formats.md).
+ The *tracks* from the input captions that you intend to use in any of your outputs. Captions tracks often correspond to language, as in "a French captions track". You must have this information ahead of time; AWS Elemental Server does not read this from your input files.
+ The *output packages and standalone files* that you intend to create with the job.

  Captions are supported in every output container type. For a list of supported output containers, see the **Reference** tab of the documentation on the web interface of your appliance. To go to the documentation, choose the **Support** tab at the top of the interface.
+ The *output captions tracks* that you intend to include for each output. 

  In most cases, the tracks that you include in an output might be a subset of the tracks that are available in the input. If you pass through Teletext-to-Teletext, all tracks in the input are available in the output. In this situation, you can't choose only a subset of the input tracks.