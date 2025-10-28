# Configuring a job that mixes audio descriptions

When you mix audio descriptions, jobs have the following requirements:

**Input**

You need an input with an audio description audio signal on one audio
channel and an audio description data stream on another.

**Audio remixing**

To mix audio descriptions across multiple audio selectors, for example if
you have a sidecar audio file, enable **Manual audio
remixing** in your output.

Otherwise, to apply audio description mixing to a single input audio
selector, you can enable **Input remix controls** in your
input instead. Keep in mind that this mixing will not apply across multiple
audio selectors or across audio selector groups.

The following describes how to configure your job settings to mix audio
descriptions.

To mix audio descriptions in your output by using the MediaConvert
console:

1. Open the [Create
   job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page in the MediaConvert console.
2. Add an input that has an audio description audio signal and an audio
   description data stream.
3. Add an output with at least one audio track.
4. In the output audio track, expand **Advanced** and
   enable **Manual audio remixing**.
5. Enter the channel that has your audio description audio signal in
   **Audio description audio channel**.
6. Enter the channel that has your audio description data stream in
   **Audio description data channel**.
7. Specify the total number of **Input channels**. For
   example, if your input has four input channels including left, right,
   audio description audio signal, and audio description data stream,
   select **4** .
8. Specify the total number of **Output channels**. For
   example, for a stereo output select **2**.
9. Specify mixing levels under **Channel mapping**. For
   example, to mix an audio description audio signal from channel 3 across
   left and right channels in a stereo output, and to mute the data stream,
   enter the following:

| Channel mapping | Inputs  | Outputs |
| --------------- | ------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | L (0)   | R (1)   |
| 1               | **0**   | **-60** |
| 2               | **-60** | **0**   |
| 3               | **0**   | **0**   |
| 4               | **-60** | **-60** | ###### Note When played over speakers, audio description data streams sound like noise. Mute the data stream in your output by setting its channel mapping to **-60**, as shown in the previous channel mapping example table. The following is an excerpt of a job settings JSON that specifies audio description mixing for a stereo output. Note that the audio description audio signal is in input channel 3, and the audio description data stream is in input channel 4: `{ "Settings": { "Inputs": [], "OutputGroups": [ { "Name": "File Group", "OutputGroupSettings": { "Type": "FILE_GROUP_SETTINGS", "FileGroupSettings": {} }, "Outputs": [ { "VideoDescription": {}, "AudioDescriptions": [ { "CodecSettings": { "Codec": "AAC", "AacSettings": { "Bitrate": 96000, "CodingMode": "CODING_MODE_2_0", "SampleRate": 48000 } }, "AudioSourceName": "Audio Selector 1", "RemixSettings": { "ChannelMapping": { "OutputChannels": [ { "InputChannelsFineTune": [ 0, -60, 0, -60 ] }, { "InputChannelsFineTune": [ -60, 0, 0, -60 ] } ] }, "ChannelsIn": 4, "ChannelsOut": 2, "AudioDescriptionAudioChannel": 3, "AudioDescriptionDataChannel": 4 } } ], "ContainerSettings": { "Container": "MP4", "Mp4Settings": {} } } ] } ] } }` |
