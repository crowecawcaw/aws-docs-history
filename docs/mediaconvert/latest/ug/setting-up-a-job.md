# Tutorial: Configuring job settings

This page provides step-by-step guidance on how to configure a job in MediaConvert.

To configure a job, you define input files for the service to transcode, and you specify
the source for each video, audio, and captions media element. That source might be a
specific part of the primary input file, or it might be a separate file. Next, you specify
the types of output files and packages that you want AWS Elemental MediaConvert to generate from the
input. You also specify the detailed encoding settings to produce the quality and type of
output that you want.

This tutorial shows how to configure jobs in MediaConvert to transcode media files into different
formats.

###### Topics

- [Optional step: Pause
  queues](#optional-pause-the-queue "#optional-pause-the-queue")
- [Step 1: Specify input
  files](#specify-input-settings "#specify-input-settings")
- [Step 2: Create input
  selectors](#create-selectors "#create-selectors")
- [Step 3: Create output groups](#specify-output-groups "#specify-output-groups")
- [Step 4: Create outputs](#create-outputs "#create-outputs")
- [Step 5: Specify global job
  settings](#specify-global-job-settings "#specify-global-job-settings")

## Optional step: Pause queues

If you're a new customer or you're experimenting with the MediaConvert console, you
can pause your queues to avoid accidentally starting a job before you're ready. For more
information about queues, see [Queues](working-with-queues.md "working-with-queues.md").

To pause or reactivate an on-demand queue using the AWS Management Console

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home/#/queues/list "https://console.aws.amazon.com/mediaconvert/home/#/queues/list") page in the MediaConvert console.
2. On the **Queues** page, choose the name of the queue that you
   want to pause or reactivate.
3. On the queue’s page, choose the **Edit queue** button.
4. On the **Edit queue** page, for **Status**,
   choose **Paused** or **Active**.
5. Choose **Save queue**.

## Step 1: Specify input files

The first part of setting up a MediaConvert job is specifying the location of your input file
or files.

###### To specify the location of your input

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert "https://console.aws.amazon.com/mediaconvert").
2. On the **Create job** page, in the **Job** pane on the left, choose **Input 1**.
3. In the **Input 1** pane, provide the URI to your video

input file
that is stored in Amazon S3 or on an HTTP(S) server. For Amazon S3 inputs, you can specify
the URI directly or choose **Browse** to select from your Amazon S3
buckets. For HTTP(S)
inputs, provide the URL to your input video file. For more information,
see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

###### Note

If your input audio or captions are in a separate file, don't create
separate inputs for them. You specify these files later in this procedure,
within your audio and captions selectors. 4. To join more than one input file into a single asset (input stitching), add
another input to the job. To do so, in the **Job** pane, in the
**Inputs** section, choose **Add**.

For jobs that have multiple input files, MediaConvert creates outputs by
concatenating the inputs in the order that you specify them in the job. You can
include up to 150 inputs in your job.

###### Tip

You can transcode portions of your inputs. For more information, see [Input settings](specifying-inputs.md "specifying-inputs.md").

## Step 2: Create input selectors for video, audio, and

captions

Next, create input selectors to flag the video, audio, and captions elements from your
input that you will use in your outputs. This labels each input element so that you can
point to it when you set up your outputs. When you set up input selectors, you also
provide the service with information about where to find the data and how to interpret
it.

###### To

set up your input selectors

1. In the **Video selector** section, specify values for the
   fields that are applicable to your job.

You don't need to create a video selector because MediaConvert automatically creates
a video selector when you begin setting up a job. However, the service doesn't
automatically detect information about the video source. You can provide this
information in the **Video selector** fields. If you keep these
settings in their default state, you will create a valid job.
For more information about individual settings, choose the **Info** link next to each setting.

###### Note

MediaConvert doesn't support inputs with multiple video streams, such as
Quad 4k. Each input can have only one video selector.
Therefore, there is no **Add video selector** button on the
console. 2. In the **Audio selectors** section, under **Audio
selector 1**, specify information about your primary audio asset.
You don't need to create an audio selector 1 because the service automatically
creates the first audio selector when you set up a job.

###### Note

An _audio asset_ is often dialogue,
background sound, and music together in one track. Tracks often consist of
multiple channels. For example, Dolby 5.1 sound has six
channels per track.

    1. For **Selector type**, choose the way that your audio
     assets are identified. Often, this is by track. If you are using an HLS
     input, and would like to select an alternate audio rendition, see [Alternate HLS audio
     rendition requirements](using-alternate-audio-renditions.md "using-alternate-audio-renditions.md").
    2. Provide the identifier (that is, track number, PID, or language code)
     for your primary audio asset. Your primary audio asset is likely to be
     track 1.


    ###### Note

    For
     most use cases, you associate one input track per
     input selector. If your use case requires combining multiple tracks
     into one track, or multiple tracks into one rendition of a streaming
     package, combine multiple input tracks in one audio selector by
     typing a comma-separated list.
     For more information about combining tracks, see
     [Setting up audio tracks and audio
     selectors](more-about-audio-tracks-selectors.md "more-about-audio-tracks-selectors.md").
    3. If your audio is in a separate file from your video, choose the
     **External file** slider switch element and provide
     the URI to your audio
    input file
     that is stored in Amazon S3 or on an HTTP(S) server. For Amazon S3 inputs, you can specify
     the URI directly or choose **Browse** to select from your Amazon S3
     buckets. For HTTP(S)
     inputs, provide the URL to your input video file. For more information,
     see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

3. If you have
   additional
   audio assets, such as multiple language tracks, choose **Add audio
   selector**. Then provide information about the next asset that is
   described in the preceding step of this procedure.
4. In the **Captions selectors** section,
   choose
   **Add captions selector**. This creates
   input captions selectors for any sets of captions that you
   plan to use in an output. For more information about setting up captions for
   your job, see [Setting up input captions](including-captions.md "including-captions.md").

## Step 3: Create output groups

After specifying your input, you create output groups. The choices that you make when you
set up output groups affect the types of assets that your job produces and which devices
can play them.

You can use MediaConvert to create media assets that fall broadly into two categories:

- **ABR streaming packages**. You can create
  adaptive bitrate (ABR) packages so that end viewers can download the asset
  gradually while they watch. Depending on how you set up your outputs, the end
  viewer's device can adapt to changes in the available bandwidth by downloading
  higher or lower-quality segments. ABR packages are also called ABR
  _stacks_, because they are made up of a
  stack
  of video, audio, and captions components. Each component in the stack or package
  is called a _rendition_.
- **Standalone files**. You might create these
  files and host them in a location where end viewers download the entire file all
  at once and then view it. You might also create standalone files and then send
  them to downstream systems for packaging and distribution.

###### To create an output group

1. In the **Job** pane, in the **Output
   groups** section, choose **Add**.
2. Choose an output group type, and then choose **Select**.

Create one file output group for all the standalone files that you intend to
create. Create one ABR streaming output group for each ABR streaming package
that you intend to create. For guidance on which ABR streaming output groups to
include in your job, see [Choosing your ABR streaming
output groups](choosing-your-streaming-output-groups.md "choosing-your-streaming-output-groups.md"). 3. Optionally, for **Custom group name**, enter a name for your
group. Any name that you provide here appears in the **Output
groups** section of the console but does not affect your
outputs. 4. For **Destination**, specify the URI for the Amazon S3 location
where the transcoding service will store your output files. You can specify the
URI directly or choose **Browse** to select from your Amazon S3
buckets.

###### Note

You can optionally append a basename to your destination URI. To create
the file name of your final asset, the transcoding service uses this
basename and any name modifier that you provide in the individual output
settings.

If you don't provide a basename with your URI, the transcoding service
generates a basename from the input 1 file name, minus the extension. 5. Specify the values for any additional settings that apply to the entire output
group. These settings vary depending on the type of output group that you
select. For more information about individual settings, choose the **Info** link next to each setting.

## Step 4: Create outputs

After you create output groups, set up your outputs in each group. The number of
outputs for each output group depends on the output group type, as follows:

- For **File** output groups, include all elements of the media
  asset in one output. This includes any audio or captions that you provide in a
  separate file.
- For ABR streaming output groups—**CMAF**,
  **Apple HLS**, **DASH ISO**, and
  **Microsoft Smooth Streaming**—create a separate
  output for each media element. That is, one output per video resolution, one
  output per audio track, and one output per captions language.

Choose from one of the following procedures that correspond to the output group types that
you created in [Step 3: Create output groups](#specify-output-groups "#specify-output-groups").

For each ABR streaming output group that you set up in [Step 3: Create output groups](#specify-output-groups "#specify-output-groups"),
create and set up an output for each media element that you want in the ABR
streaming package.

#### Creating video ABR streaming

outputs

For each video output that you include in your output group, MediaConvert creates
one video rendition, or set of segmented video files.
Multiple
video renditions in a streaming package, of varying resolutions and video
quality, allow the end viewer's device to adapt the quality of video to the
available bandwidth.

###### Note

Although
the job has only one video _input_
selector, ABR streaming output groups often have several video _outputs_ per output group.

###### To create and set up video ABR streaming outputs

1. On the **Create job** page, in the **Job** pane on the left,
   under **Output Groups**, below the
   **CMAF**, **Apple HLS**,
   **DASH ISO**, or **Microsoft Smooth
   Streaming** output group that you want add outputs to,
   choose **Output 1**.

When you create an output group, MediaConvert automatically
populates the output group with output 1. You don't need to
explicitly create the first output. 2. In the **Output settings** pane, for
**Name modifier**, enter a value.

MediaConvert appends the name modifier to the file names that it
creates for this output. Enter a name modifier that will make it
easy to identify which files came from which output, such as
`-video-hi-res`. 3. If one of the predefined groups of settings listed under
**Preset** is suitable for your workflow,
choose it from the list. If you use a preset, skip the next step of
this procedure. 4. Specify your video settings as follows:

    1. In the **Output settings** section,
     specify values for any remaining general settings. Depending
     on the output group type, these settings might include
     transport stream settings or other container settings.
     For more information about individual settings, choose the **Info** link next to each setting.
    2. In the **Stream settings** section,
     specify values for video encoding. The video settings are
     selected by default, so you don't need to explicitly choose
     this group of settings.


    There is only one input video selector per job, so you
     don't need to explicitly choose it when you set up your
     video outputs.For more information about individual settings, choose the

**Info** links on the console. 5. If your output includes a group of audio settings by default,
delete it as follows:

    1. In the **Stream settings** section,
     choose **Audio 1**.
    2. Choose **Remove audio**.

6. If you want multiple video renditions in your ABR streaming
   package, repeat the preceding steps of this procedure. This will
   create an additional video output for
   each
   one.

#### Creating audio ABR streaming

outputs

For each audio output that you include in your output group, MediaConvert creates
one audio rendition, or set of segmented video files. The most common reason
to include multiple audio renditions is to provide multiple language
options. If you provide only one language, you
probably
need only one audio output.

###### Note

For AAC streaming outputs, the initial segment is longer in duration than the others. This is because, with AAC, the initial segment must contain silent AAC pre-roll samples before the audible part of the segment. MediaConvert accounts for these extra samples in the timestamps, so the audio plays back correctly.

###### To create and set up audio ABR streaming outputs

1. If you're working in a CMAF output group, skip this step. The
   first audio output is created for you.

Create an output for your first audio track. Usually an audio
track corresponds to one language.

    1. In the **Job** pane, choose the output
     group that you're working in.
    2. In the **Outputs** pane, choose
     **Add output**.
    3. Choose the output that you just created.
    4. If your output includes a group of video settings by
     default, choose **Remove video** to delete
     it. This k the **Audio 1** group of
     settings displayed.

2. In the **Output settings** pane, for
   **Name modifier**, enter a value.

MediaConvert appends the name modifier to the file names that it
creates for this output. Enter a name modifier that will make it
easy to identify which files came from which output, such as
`-audio-english`. 3. If one of the predefined groups of settings listed under
**Preset** is suitable for your workflow,
choose it from the list. If you use a preset, skip the next step of
this procedure. 4. Specify your audio settings as follows:

    1. In the **Output settings** section,
     specify values for any remaining general settings.
     For more information about individual settings, choose the **Info** link next to each setting.
    2. Under **Stream settings**, for
     **Audio source**, choose one of the
     audio selectors that you created in [Step 2: Create input selectors for video, audio, and
     captions](#create-selectors "#create-selectors").
    3. In the **Stream settings** section,
     specify values for audio encoding. For more information about individual settings, choose the **Info** link next to each setting.

5. If you have additional audio assets to include in the ABR
   streaming package, create an output for each of them as
   follows:
   1. In the **Job** pane, choose the output
      group that you're working in.
   2. In the **Outputs** pane, choose
      **Add output**.
   3. Choose the output that you just created.
   4. If your output includes a group of video settings by
      default, choose **Remove video** to delete
      it. This keeps the **Audio 1** group of
      settings displayed.
   5. Set up the output as described in steps 2 through 4 of
      this procedure.

#### Creating captions for ABR

streaming outputs

Setting up captions can be complex. For detailed information, see [Setting up input captions](including-captions.md "including-captions.md"). For
basic instructions, complete the following procedure.

###### To create and set up captions for ABR streaming outputs

1. Create an output for your first set of captions. Usually a set of
   captions corresponds to one language.
   1. In the **Job** pane, choose the output
      group that you're working in.
   2. In the **Outputs** pane, choose
      **Add output**.
   3. Choose the output that you just created.
   4. If your output includes groups of video and audio settings
      by default, choose **Remove video** and
      **Remove audio** to delete them.
   5. Choose **Add captions** to display a set
      of captions settings.

2. In the **Output settings** pane, for
   **Name modifier**, enter a value.

MediaConvert appends the name modifier to the file names that it
creates for this output. Enter a name modifier that will make it
easy to identify which files came from which output, such as
`-captions-english`. 3. Specify your captions settings as follows:

    1. In the **Output settings** section,
     specify values for any remaining general settings.
     For more information about individual settings, choose the **Info** link next to each setting.
    2. Under **Stream settings**, for
     **Captions source**, choose one of the
     captions selectors that you created in [Step 2: Create input selectors for video, audio, and
     captions](#create-selectors "#create-selectors").
    3. In the **Stream settings** section,
     specify values for the remaining captions settings.

#### Creating additional

manifests

By default, MediaConvert generates a single multivariant playlist for each of your
CMAF, DASH ISO, Apple HLS,
and Microsoft Smooth Streamingoutput groups. This default
manifest references all the outputs in the output group.

Optionally, you can create additional multivariant playlists that reference
only a subset of the outputs in your output group. For example, you might
want to create a manifest that doesn't include HDR outputs, for viewers who
don't have a subscription that includes HDR.

###### Note

For CMAF output groups, if you keep the default enabled value for
**Write HLS manifest** and **Write DASH
manifest**, MediaConvert creates additional manifests in
both of those formats. If you disable either of those settings,
MediaConvert doesn't create additional manifests in that format.

###### To create an additional manifest

1. On the **Create job** page, in the **Job** pane on the left, choose the output group that you want to create the
   additional manifest for.
2. In the **Additional manifests** section on the
   right, choose **Add manifest**.
3. For **Manifest name modifier**, enter the text
   that you want to be at the end of the manifest file name, before the
   extension. This setting is required, because it gives each manifest
   a different file name.
4. For **Select outputs**, choose the outputs that
   you want the manifest to refer to.
5. Repeat these steps to create up to 10 additional manifests. Each
   additional manifest must have a different value for
   **Manifest name modifier**.

With File output groups, each asset that the service creates corresponds to one output,
rather than one output group. Each asset contains all video, audio, and captions
elements. Therefore, it's simplest to set up by first creating the output, and
then setting up all the output selectors.

#### Create file outputs

If you created a file output group in [Step 3: Create output groups](#specify-output-groups "#specify-output-groups"), create and set up an output in
the file output group for each standalone file that you intend to
create.

###### To create an output in a file output group

1. When you create an output group, MediaConvert automatically populates the
   output group with output 1, so you don't need to explicitly create
   it. If you are creating only one standalone file, skip the rest of
   this procedure.
2. If you want to create more than one standalone file, create
   additional outputs as follows:
   1. On the **Create job** page, in the **Job** pane on the left, under **Output Groups**,
      choose **File group**.
   2. In the **Outputs** pane, choose
      **Add output**.

#### Set up output

selectors in file outputs

Next, for each file output that you just created, set up output selectors.

###### To set up output selectors in a file output

1. On the **Create job** page, in the **Job** pane on the left, under **Output Groups**, under
   **File group**, choose **Output
   1**.
2. In the **Output settings** pane, for
   **Name modifier**, enter a value.

MediaConvert appends the name modifier to the file names that it
creates for this output. Enter a name modifier that identifies which
files came from which output, such as
`-standalone-hi-res`. 3. If one of the predefined groups of settings listed under
**Preset** is suitable for your workflow,
choose it from the list. If you use a preset, skip step 4 of this
procedure.

Output
presets can contain up to one set each of video, audio, and captions
settings. Therefore, if your standalone output file contains more
than one audio or captions asset, you can't use a preset. If you
can't use presets in your output, but you want to use the preset
settings as a starting point, choose the preset, then choose
**No preset** from the
**Preset** dropdown list. This prepopulates
your output with the same settings that are in the
preset. 4. Specify your output settings as follows:

    1. In the **Output settings** section,
     specify values for any remaining general settings. These
     settings vary depending on the container that you choose.
     For more information about individual settings, choose the **Info** link next to each setting.
    2. In the **Stream settings** section,
     specify values for video encoding. For more information about individual settings, choose the **Info** link next to each setting.


    ###### Note

    The video settings tab is selected
     by default, so you don't need to explicitly choose this
     group of settings. There is only one input video
     selector per job, so you don't need to explicitly choose
     it when you set up your video outputs.
    3. Choose **Audio 1** to display the group
     of encoding settings for the first audio asset.
     **Audio
     1** is located on the left side of the
     **Stream settings** pane, below
     **Video**.
    4. Under **Stream settings**, for
     **Audio source**, choose one of the
     audio selectors that you created in [Step 2: Create input selectors for video, audio, and
     captions](#create-selectors "#create-selectors").
    5. In the **Stream settings** section,
     specify values for audio encoding. For more information about individual settings, choose the **Info** link next to each setting.
    6. To include captions in the output, choose **Add
     captions**. This displays a group of captions
     settings. For more information about setting up captions,
     see [Setting up input captions](including-captions.md "including-captions.md").

## Step 5: Specify global job

settings

Global job settings apply to every output that the job creates.

If your job incorporates audio or captions provided in a separate file from your
input, or if you use the graphic overlay (image inserter) feature, it is especially
important to get these settings right.

There
are three distinct groups of timecode settings. Global job timecode configuration is one
of those three. For more information about the different sets of timecode settings and
how MediaConvert manages timecodes, see [Setting up timecodes](setting-up-timecode.md "setting-up-timecode.md").

###### To specify global job settings

1. In the **Job** pane, in the **Job settings**
   section, choose **AWS integration**.
2. For **IAM role**, choose an IAM role that has permissions
   to access the Amazon S3 buckets that hold your input and output files. The IAM role
   must have a trusted relationship with MediaConvert. For information about creating this
   role, see [Setting up IAM permissions](iam-role.md "iam-role.md") .
3. Optionally, specify job-wide timecode settings in the **Timecode
   configuration** pane.
4. Specify values for the other job settings and enable global processors.
   For more information about individual settings, choose the **Info** link next to each setting.
