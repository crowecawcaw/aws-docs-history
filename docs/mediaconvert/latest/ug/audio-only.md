# Creating audio-only outputs

You can use AWS Elemental MediaConvert to create outputs that contain only audio, without video.
With audio-only outputs, MediaConvert supports a more limited number of codec and container
combinations for input and output files.

The restrictions and procedures in this chapter apply to outputs that don't have video
in the container. This includes the following:

- Outputs in **File** output groups that don't have video
  included
- Streaming **HLS** output groups that contain only audio
  outputs
- Streaming **DASH** output groups that contain only audio outputs
  When you set up streaming output packages that contain audio, video, and captions, you
  create separate outputs for each element inside the output package. These are not
  audio-only outputs as described in this chapter. For more information about setting up
  streaming outputs, see [Creating outputs
  in ABR streaming output groups](setting-up-a-job.md#create-outputs-in-abr-streaming-output-groups "setting-up-a-job.md#create-outputs-in-abr-streaming-output-groups").

You set up an audio-only output in the same way that you set up an output that
contains video, except that you don't include video or captions.

MediaConvert generates the following files for audio-only outputs:

- **File** output groups: One separate audio-only file for
  each output.
- **HLS** output groups: A single rendition in the ABR
  stack for each output.
- **DASH ISO** output groups: A single rendition in the ABR
  stack for each output.

###### Note

For AAC streaming outputs, the initial segment is longer in duration than the others. This is because, with AAC, the initial segment must contain silent AAC pre-roll samples before the audible part of the segment. MediaConvert accounts for these extra samples in the timestamps, so the audio plays back correctly.

###### To create an audio-only output (console)

1. To confirm that MediaConvert supports your input files, consult the input
   table in [Supported output formats for audio-only workflows](audio-only-output.md "audio-only-output.md").
2. Set up your job as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md"), but with the following
   differences:
   - Remove the **Video** tab in the **Encoding
     settings** section of your output.
   - Choose a supported output container and audio codec from the output
     table in [Supported output formats for audio-only workflows](audio-only-output.md "audio-only-output.md").
   - Include only one group of audio settings per output. That is, don't
     choose **Add audio** to create an **Audio
     2** tab under **Encoding
     settings**.

3. If your outputs are in an **HLS** output group, choose a
   container for the audio-only output.

Under **Output settings**, in the **Audio**
section, for **Container for audio-only output**, choose
**MPEG-2 Transport Stream** to create a file in an MPEG2-TS
container. Keep the default value **Automatic** to create a raw
audio-only file with no container.

###### To create an audio-only output (API, SDK, and AWS CLI)

1. To confirm that MediaConvert supports your input files, consult the input
   table in [Supported output formats for audio-only workflows](audio-only-output.md "audio-only-output.md").
2. Set up your JSON job specification. Either manually edit your JSON file, or
   use the console to generate it as follows:
   1. Follow the previous procedure for the console.
   2. In the **Job** pane on the left, under **Job
      settings**, choose **Show job
      JSON**.The JSON job specification for audio-only jobs differs from standard jobs as
      follows:
   - Exclude each instance of `VideoDescription` and its
     children from the `Outputs` portion of your job JSON.
   - For each output, include only one child group of audio settings under
     `AudioDescriptions`.
   - For audio-only outputs in an **HLS** output group,
     specify a container for the audio-only output. Under
     `Outputs`, `OutputSettings`,
     `HlsSettings` include the property
     `HlsAudioOnlyContainer`. Set it to `M2TS` to
     create a file in an MPEG2-TS container. Set it to `AUTOMATIC`
     to create a raw audio-only file with no container.
     `AUTOMATIC` is the default behavior.

###### Topics

- [Supported output formats for audio-only workflows](audio-only-output.md "audio-only-output.md")
- [Audio-only job settings limitations](feature-limitations-for-audio-only.md "feature-limitations-for-audio-only.md")
