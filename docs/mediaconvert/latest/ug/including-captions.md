

# Setting up input captions
<a name="including-captions"></a>

To include captions in your job, follow these steps in the order listed:

1. If your input captions are a timecode-based sidecar captions format, such as SCC or STL, [set the timecode source settings.](#set-the-timecode-source-settings)

1. [Gather required captions information.](#gather-required-captions-information)

1. [Create input captions selectors.](#create-input-caption-selectors)

1. [Set up captions in outputs.](set-up-captions-in-outputs.md)

For a full list of supported input and output captions, see [Captions reference tables](captions-support-tables.md).

For information about how to set up captions in your output, see [Setting up captions in outputs](set-up-captions-in-outputs.md).

**Tip**  
You can use Amazon Transcribe with MediaConvert to generate captions and include them in your output. For more information, see [AWS VOD captioning using Amazon Transcribe](https://github.com/aws-samples/aws-transcribe-captioning-tools) in *AWS Samples* on GitHub.

## Specifying the timecode source
<a name="set-the-timecode-source-settings"></a>

For your captions to correctly synchronize with your video, you must set up your input timeline to match the timecodes embedded in your captions file. MediaConvert establishes the input timeline based on the value you choose for the input **Timecode source** setting. For more information, see [Input timecode source and captions alignment](about-input-timecode-source-and-captions-alignment.md).

For instructions on adjusting the **Timecode source** setting, see [Adjusting the input timeline with the input timecode source](timecode-input.md).

## Gathering required captions information
<a name="gather-required-captions-information"></a>

Before you set up captions in your job, note the following information:
+ The *input captions format*. You must have this information ahead of time; MediaConvert does not read this from your input files.
+ The *tracks* from the input captions that you intend to use in any of your outputs.
+ The *output packages and files* that you intend to create with the job. For information about specifying the output package or file type, see [Creating outputs](output-settings.md).
+ The *output captions format* that you intend to use in each output.

  For supported output captions based on your input container, input captions format, and output container, see [Supported input captions, within video containers](captions-support-tables-by-container-type.md). 
+ The *output captions tracks* that you intend to include for each output. If you pass through teletext-to-teletext, all tracks in the input are available in the output. Otherwise, the tracks that you include in an output might be a subset of the tracks that are available in the input.

## Creating input captions selectors
<a name="create-input-caption-selectors"></a>

When you set up captions, you begin by creating captions selectors. Captions selectors identify a particular captions asset on the input and associate a label with it. The captions asset is either a single track or the set of all tracks contained in the input file, depending on your input captions format. For example, you might add **Captions selector 1** and associate the French captions with it. When you [set up an output to include captions](set-up-captions-in-outputs.md), you do so by specifying captions selectors. 

**To create input captions selectors**

1. On the **Create job** page, in the **Job** pane on the left, choose an input. 
**Note**  
In jobs with multiple inputs, each input must have the same number of captions selectors. For inputs that don't have captions, create empty captions selectors. For these selectors, for **Source**, choose **Null source**. Remove all captions selectors if no inputs have captions.

1. In the **Captions selectors** section, near the bottom of the page, choose **Add captions selector**. 

1. Under **Source**, choose the input captions format. 

1. For most formats, more fields appear. Specify the values for these fields as described in the topic that relates to your input captions format. Choose the appropriate topic from the list that follows this procedure.

1. Create more captions selectors as necessary. The number of captions selectors that you need depends on your input captions format. Choose the appropriate topic from the list that follows this procedure.