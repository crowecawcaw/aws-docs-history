# Converting to Dolby Digital Plus with

Atmos

The following handling is supported:

- Encoding an audio output as Dolby Digital Plus with Atmos. The
  audio source must be a source that contains up to 16
  channels.
- Passthrough of a source audio that is already Dolby Digital Plus
  with Atmos.
  Elemental Live doesn't support transcoding (re-encoding) an audio source
  that is Dolby Digital Plus with Atmos.

Conversion to Dolby Digital Plus with Atmos requires the Advanced Audio
Pack. For information about purchasing this package, see [Purchasing
and
licensing an add-on package](ref-licenses-purchase.md "ref-licenses-purchase.md"). Note that passthrough of Dolby
Digital Plus with Atmos doesn't require a license.

## Supported sources

The source must have these characteristics:

- To convert to Dolby Digital Plus with Atmos, the audio input
  can be any source that has these characteristics:
  - Up to 16 channels in the following order:

  `L R C LFE Ls Rs Lb Rb Tfl Tfr Tsl Tsr Tbl Tbr Lw
 Rw`
  - If the source has fewer than 16 channels, Elemental Live
    extracts all the channels and then pads the output by
    inserting silence in the higher-numbered channels. For
    example, if the source has two channels, Elemental Live puts
    those channels in L and R, then inserts silence in the
    remaining channels.

  - If the source doesn't have the channels in the specified
    order, the results might be wrong on the downstream player.
    For example, the sound of rain falling might come out of
    the left speaker instead of a ceiling speaker.
  - A sampling rate of 48000 hz.

- To pass through Dolby Digital Plus with Atmos, the audio can
  be any coding mode and any sampling rate that Dolby Digital Plus
  supports.

For information about the types of inputs that support Dolby Digital
Plus and Dolby Digital Plus with Atmos, see [Reference: Supported live
inputs](ref-inputs-and-codecs.md "ref-inputs-and-codecs.md").

## Supported

outputs

**Audio encoding**

The Elemental Live implementation of Dolby Digital Plus with Atmos supports
the following coding modes in the output:

- 5.1.4 coding mode
- 7.1.4 coding mode
- 9.1.6 coding mode

Within each coding mode, the speaker channels are arranged as shown
in the following table.

| Coding mode               | Channel arrangement                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5.1.4                     | `L R C LFE Ls Rs Tfl Tfr Tbl Tbr`                                                                                                                              |
| 7.1.4                     | `L R C LFE Ls Rs Lb Rb Tfl Tfr Tbl Tbr`                                                                                                                        |
| 9.1.6                     | `L R C LFE Ls Rs Lb Rb Tfl Tfr Tsl Tsr Tbl Tbr Lw Rw`                                                                                                          | The abbreviations are the standard Dolby abbreviations: Left, Right, Center, LFE, Left surround, Right surround, Left rear surround, Right rear surround, Left back, Right back, Top front left, Top front right, Top side left, Top side right, Top back left, Top back right, Left wide, and Right wide. **Supported output groups** For information about the types of outputs that support Dolby Digital Plus with Atmos and Dolby Digital Plus with Atmos (as passthrough), see [Reference: Supported outputs](ref-outputs-and-codecs.md "ref-outputs-and-codecs.md"). ## Setting up the event Follow this procedure to produce Dolby Digital Plus with Atmos in one or more outputs. ###### Note The information in this section assumes that you are familiar with the general steps for creating an event. ###### To set up the input Follow this procedure if the source audio is Dolby Digital Plus, to convert the audio to Dolby Digital Plus with Atmos. 1. In the event in Elemental Live, go to the input that contains the Dolby Digital Plus audio that you want to transcode or pass through. 2. Choose **Advanced**, then choose **Add Audio Selector**. 3. Complete the fields to extract the Dolby Digital Plus audio. ###### To set up the output if the source audio is Dolby Digital Plus 1. In the event, go to the output group where you want to add the audio. Or create a new group. 2. Create the output where you want to add the audio encode. 3. In the **Streams** settings section for the output, choose the **Audio** section**.** Complete the fields as follows. |
| Field                     | Description                                                                                                                                                    |
| ---                       | ---                                                                                                                                                            |
| **Audio Source**          | Choose the audio selector that you set up in the input.                                                                                                        |
| **Audio Codec**           | Choose Dolby Digital Plus with Atmos.                                                                                                                          |
| **Coding mode**           | Choose the coding mode you want. For more information, see [Supported outputs](#dolby-atmos-output-supported-outputs "#dolby-atmos-output-supported-outputs"). |
| **Bitrate**               | Choose a value that is applicable to the coding mode. For information, choose the **?** icon above the field.                                                  |
| **Dialnorm**              | Complete these fields to specify values for the metadata. For information about a field, click the question mark icon above the field in Elemental Live.       |
| **DRC Line Mode Profile** |                                                                                                                                                                | **DRC RF Mode Profile**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Surround Trim**         |                                                                                                                                                                | **Height Trim**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 4. Complete the fields in the **Advanced** section as desired. Ignore **ARIB Dynamic Audio**, it doesn’t apply. ###### To pass through Dolby Digital Plus with Atmos from the input to the output Follow this procedure if the source audio is already Dolby Digital Plus with Atmos. 1. In the event, go to the output group where you want to add the audio. Or create a new group. 2. Create the output where you want to add the audio encode. 3. In the **Streams** settings section for the output, choose the **Audio** section**.** 4. Set these fields: <br>• **Audio Source**: Set to the audio selector that you set up in the input. <br>• **Audio Codec**: Set to Dolby Digital Plus Passthrough. With this setup, all audio sources in all the inputs will be passed through, both Dolby Digital Plus with Atmos and other audio. ###### Important Don't set **Audio Codec** to **Dolby Digital Plus with Atmos**. That isn't the correct value for passing through. If you choose this option, the output might have silent audio. ### Sample HLS manifest If you include Dolby Digital Plus with Atmos in an HLS output group, the audio line in the HLS manifest looks like this example: `#EXTM3U #EXT-X-VERSION:4 #EXT-X-INDEPENDENT-SEGMENTS #EXT-X-STREAM-INF:BANDWIDTH=2208800,AVERAGE-BANDWIDTH=2142800,CODECS="avc1.64001f,ec-3",RESOLUTION=1280x720,FRAME-RATE=30.000,AUDIO="program_audio_0" index_video.m3u8 #EXT-X-MEDIA:TYPE=AUDIO,LANGUAGE="eng",NAME="English",AUTOSELECT=YES,DEFAULT=YES,CHANNELS="12/JOC",GROUP-ID="program_audio_0",URI="index_audio.m3u8"` The `Channels` attribute in the last line is significant for Dolby Digital Plus with Atmos: <br>• 12/JOC indicates that the coding mode is 5.1.4 or 7.1.4 and the codec is Dolby Digital with Atmos. <br>• 16/JOC indicates that the coding mode is 9.1.6 and the codec is Dolby Digital with Atmos. |
