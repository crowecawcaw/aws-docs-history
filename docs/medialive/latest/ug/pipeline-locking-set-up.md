# Setting up for locking

Pipeline
locking is enabled by default in a standard channel. You can disable it. If you decide
to keep it enabled,
you
should configure the mode to use in a specific channel. And you should configure the
output groups to ensure that MediaLive can successfully lock the pipelines.

###### Note

All the procedures in this section assume that you are familiar with the general
steps for creating a channel, as described [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

## Configuring

output locking and
setting
the mode

You can configure the channel
as
follows:

- Locking disabled
- Locking
  enabled in
  pipeline
  locking
  mode: lock the two pipelines to each other
- Locking
  enabled in
  epoch
  locking
  mode: lock the pipelines using the Unix epoch as the
  reference.

###### Configure the pipeline locking mode

1. In the channel that you are
   creating
   or editing, in the navigation pane, choose
   **General settings**. Then choose **Global
   configuration**.
2. Choose **Enable global configuration**.
3. In **Output locking mode**,
   choose
   **DISABLED**. Or choose the
   mode—**PIPELINE_LOCKING** or
   **EPOCH_LOCKING**. For details about the options,
   choose the **Info** link next to the field.

## Setting up an HLS, MediaPackage, or

Microsoft Smooth output group

In an HLS output group or Microsoft Smooth output group, you must set up the
framerate for each video encode.

###### Set up for pipeline locking

1. In the channel that you are creating, in the navigation pane, choose the
   HLS or Microsoft Smooth output group. If necessary, create the outputs and
   video encodes in each output.
2. In each output that contains a video encode, choose the video encode. In
   the **Codec settings** field, choose the codec. More fields
   appear.
3. Choose the **Frame rate** section and set the following
   fields:
   - **Framerate control**: We recommend you choose
     **Specified**. The option
     **Initialize_from_source** doesn't work well
     with pipeline locking.
   - **Framerate numerator** and **Framerate
     denominator**: Set the desired resolution for the
     output. Make sure that the conversion from input framerate to output
     framerate meets [the
     requirements](pipeline-locking-verify-input.md "pipeline-locking-verify-input.md").

4. Repeat, to setup of the frame rate in the video encode in every
   output.

## Setting up a UDP output group

In a UDP output group, you must obtain information about segmentation markers, and
set up the segmentation markers for framerate for each video encode.

###### Set up for pipeline locking

1. You need information about the how to configure segmentation in the
   outputs. This information is contained in fields on the **Create
   channel** page on the console. To display the fields, in the
   navigation pane choose **Archive group**. Then choose an
   output and choose **Network settings**. Choose the
   **Info** link next to each of the following fields:
   - **Segmentation markers**
   - **Segmentation time**
   - **EBP lookahead msec**
   - **Fragment time**
   - **Segmentation style**
   - **EBP placement**
   - **EBP audio interval**

2. Speak to your contact at the downstream system to obtain recommended
   values for these fields.
3. In the channel that you are creating, in the navigation pane, choose the
   Archive output group. If necessary, create the outputs. Then in the
   **Output settings**, choose **Network
   settings**. More fields appear.
4. Choose **Container settings** and set values for the
   segmentation fields listed in step 1. It's possible that some of the fields
   don't apply to the segmentation markers you choose.
5. If necessary, create the video encode in the output, then choose the video
   encode. In the **Codec settings** field, choose the codec.
   More fields appear.
6. Choose the **Frame rate** section and set the following
   fields:
   - **Framerate control**: We recommend you choose
     **Specified**. The option
     **Initialize_from_source** doesn't work well
     with pipeline locking.
   - **Framerate numerator** and **Framerate
     denominator**: Set the desired framerate for the
     output. Make sure that the conversion from input framerate to output
     framerate meets [the
     requirements](pipeline-locking-verify-input.md "pipeline-locking-verify-input.md").
