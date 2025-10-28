This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Using Dolby Atmos Encoding with

AWS Elemental Server

AWS Elemental Server can encode Dolby Digital Plus with Atmos channel-based, immersive
audio, Audio Descriptive Model Broadcast WAV files, or Dolby Atmos Master File.

###### Note

Understanding Dolby Atmos is required prerequisite knowledge for using this feature. Your
input audio channels must already be set up according the Dolby Atmos standard you are using as input.
For more information about Dolby Atmos, see the Dolby online
documentation.

## Input File

Requirements for Dolby Atmos Encoding

## Feature Restrictions

for Dolby Atmos Encoding

Note the following restrictions in the AWS Elemental Server implementation of Dolby
Atmos encoding:

- **Channel-based immersive:**
  AWS Elemental Server supports channel-based immersive (CBI) content.
- **Dolby Atmos Master File (DAMF):**
  AWS Elemental Server supports Dolby Atmos master file (DAMF). This is a collection of 3 files with the extensions, .atmos, .atmos.metadata, and .atmos.audio
- **Audio Descriptive Model Broadcast WAV Format (ADM BWF):**
  AWS Elemental Server supports ADM BWF. It is a single broadcast WAV file contains header data with the .atmos and .atmos.metadata information.
- **Output codec:** You can create Dolby Atmos
  audio outputs encoded with only the Dolby Digital Plus (EAC3) codec.
- **Output containers:** For file outputs, you
  can create Dolby Atmos audio in only in one of the video containers that
  supports Dolby Digital Plus: MPEG-4, MPEG-2 Transport Stream, or
  QuickTime.
- **Output packages:** For adaptive bitrate
  (ABR) outputs, you can create Dolby Atmos audio in any of the
  AWS Elemental Server output group types: CMAF, Apple HLS, DASH ISO, or
  Microsoft Smooth Streaming.

## Setting Up a Job for Dolby Atmos

Encoding

To encode 9.1.6 audio Dolby Atmos objects, provide 16 input channels of PCM audio, either in
individual .wav files or as tracks in a single container.

If you provide input audio as individual .wav files, you specify them in order in
your input. You specify them as **Audio selector 1**,
**Audio selector 2**, and so on, up to **Audio selector
16**. If you provide your audio as a single file containing 16 tracks,
you specify the file in your input as **Audio selector 1**, and
then you specify the tracks individually within that audio selector.

###### Important

Regardless of whether they are in separate files or a single file, you must
set up the channels in the following order: L, R, C, LFE, Ls, Rs, Lrs, Rrs, Lw,
Rw, Ltf, Rtf, Ltm, Rtm, Ltr, Rtr.

###### Summary Instructions for Individual .wav File Input

If your audio input is individual .wav files, do the following:

1. Create 16 separate input audio selectors, in this order: L, R, C, LFE, Ls,
   Rs, Lrs, Rrs, Lw, Rw, Ltf, Rtf, Ltm, Rtm, Ltr, Rtr.
2. Create a single audio selector group; include each of the 16 audio
   selectors.
3. Create one output stream with a single audio tab.
   1. For **Audio Codec**, choose **Dolby Digital Plus JOC (Atmos)**.
   2. For **Audio Source**, choose the audio selector group that you
      created.

###### Summary Instructions for Single, Multi-Track File Input

1. Create an input audio selector.
2. For **Selector Type**, choose
   **Track**.
3. For Track, specify your 16 channels with a comma-separated list of channel numbers.
   Specify them in this order: L, R, C, LFE, Ls, Rs, Lrs, Rrs, Lw, Rw, Ltf,
   Rtf, Ltm, Rtm, Ltr, Rtr.
4. Create one output stream with a single audio tab.
   1. For **Audio Codec**, choose **Dolby Digital Plus JOC (Atmos)**.
   2. For **Audio Source**, keep the default **Audio
      Selector 1**.

For more detailed instructions, see one of the following procedures:

[Procedure with separate audio input files](#proc-atmos-separate-input-files "#proc-atmos-separate-input-files")

[Procedure with a single audio input file](#proc-atmos-single-input-file "#proc-atmos-single-input-file")

###### To set up a Dolby Atmos job, with audio inputs as 16 individual .wav

files

1.  Set up your input audio selectors as follows:
    1. On the **Create New Job** page, in the **Input** section, under
       **Advanced**, find **Audio Selector
       1**.
    2. Choose the **External file** check box.
    3. For **External File**, provide the path and file name to the .wav file
       for your first channel. For **Audio Selector 1**,
       this channel must be L.

    ###### Important

    You must set up the channels in the following order: L, R, C,
    LFE, Ls, Rs, Lrs, Rrs, Lw, Rw, Ltf, Rtf, Ltm, Rtm, Ltr, Rtr.

    That is, if your input audio is in separate .wav files, **Audio Selector
    1** must point to the L channel, **Audio
    Selector 2** must point to the R channel, and so
    on. 4. At the top of the **Audio Selector** sections, choose **Add
    Audio Selector** to create **Audio Selector
    2**. 5. Under **Audio Selector 2**, choose **External
    file**. 6. Specify the path and file name to the .wav file for your second channel. For
    **Audio Selector 2**, this channel must be
    R. 7. Repeat the steps to create an audio selector for the rest of your
    16 channels. Choose the following channels for each selector:

        * **Audio Selector 3**: C
        * **Audio Selector 4**: LFE
        * **Audio Selector 5**: Ls
        * **Audio Selector 6**: Rs
        * **Audio Selector 7**: Lrs
        * **Audio Selector 8**: Rrs
        * **Audio Selector 9**: Lw
        * **Audio Selector 10**: Rw
        * **Audio Selector 11**: Ltf
        * **Audio Selector 12**: Rtf
        * **Audio Selector 13**: Ltm
        * **Audio Selector 14**: Rtm
        * **Audio Selector 15**: Ltr
        * **Audio Selector 16**: Rtr

2.  Create an input **Audio Selector Group** as follows:
    1. At the top of the **Audio Selector** sections, choose **Add
       Audio Selector Group**.
    2. For **Selector Group Name**, enter a descriptive name, such as
       `Dolby Atmos Audio Group`.
    3. All the audio selectors appear below **Selector Group Name**. Choose
       each audio selector that you created earlier in this
       procedure.

3.  In the bottom section of the **Create New Job** page, set up your output groups and outputs. Choose supported containers as
    listed in [Feature Restrictions
    for Dolby Atmos Encoding](#feature-restrictions-for-dolby-atmos-encoding "#feature-restrictions-for-dolby-atmos-encoding").
4.  Set up the **Audio 1** tab of **Stream
    1**.

###### Note

Avoid setting up multiple audio tabs within the stream. One audio tab represents the
entire Atmos audio content.

    1. For **Audio Codec**, choose **Dolby Digital Plus JOC (Atmos)**.


    For **Audio Source**, choose the audio selector group that you
     created earlier in this procedure, such as **Dolby Atmos
     Audio Group**.
    2. For the audio encoding settings, choose values that are suitable
     for your workflow. For more information, see the Dolby documentation
     for the Dolby Digital Plus Atmos encoding library.


    ###### Note

    AWS Elemental Server automatically performs audio normalization
     on Dolby Digital Plus Atmos outputs. Therefore, there is no
     **Dialnorm** setting under audio encoding
     settings.

###### To set up a Dolby Atmos job, with audio input as a single file with 16

tracks

1. Set up your input audio selector as follows:
2. 1. On the **Create New Job** page, in the **Input** section, under
      **Advanced**, find **Audio Selector
      1**.
   2. Choose the **External file** check box.
   3. For **External Audio File**, provide the path and
      file name to the .wav file.
   4. For **Selector Type**, choose
      **Track**.
   5. For **Track**, list your 16 PCM mono tracks in a
      comma-separated list. Specify them in the following order: L, R, C,
      LFE, Ls, Rs, Lrs, Rrs, Lw, Rw, Ltf, Rtf, Ltm, Rtm, Ltr, Rtr.
      - If the tracks of your input audio file are already in that
        order, then list them that way: `1, 2, 3, …
16`.
      - If the tracks of your input audio file are in a different order, list them according
        to the specified order. For example, if your L channel is in
        track 3, then list `3` first.

3. In the bottom section of the **Create New Job** page, set up your output groups and outputs.
4. Set up the **Audio 1** tab of **Stream
   1**.

###### Note

Don't set up multiple audio tabs within the stream. One audio tab
represents the entire Atmos audio content.

    1. For **Audio Codec**, choose **Dolby Digital Plus JOC (Atmos)**.


    For **Audio Source**, keep the default **Audio
     selector 1**.
    2. For the audio encoding settings, choose values that are suitable
     for your workflow. For more information, see the Dolby documentation
     for the Dolby Digital Plus Atmos encoding library.


    ###### Note

    AWS Elemental Server automatically performs audio normalization
     on Dolby Digital Plus Atmos outputs. Therefore, there is no
     **Dialnorm** setting under audio encoding
     settings.
