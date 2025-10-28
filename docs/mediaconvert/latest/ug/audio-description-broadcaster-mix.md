# Configuring a job for pre-mixed audio

descriptions

If you have an input that already has pre-mixed audio descriptions, and does not
contain an _audio description audio signal_ or an
_audio description data stream_, set
**Audio description broadcaster mix** to **Broadcaster
mixed AD**.

When you do, MediaConvert writes metadata in your output that signals to downstream
systems that it contains broadcaster mixed audio descriptions.

The following describes how to configure your job settings to write metadata
in your output signalling it contains pre-mixed audio descriptions.

To write broadcaster mixed audio description metadata in your output by using
the MediaConvert console:

1. Open the [Create
   job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page in the MediaConvert console.
2. Add an input that has pre-mixed audio description.
3. Add an output with at least one audio track.
4. In the output audio track, set **Audio description broadcaster
   mix** to **Broadcaster mixed AD**.
5. (Optional) If you enable Manual audio remixing, keep **Audio
   description audio channel** and **Audio description
   data channel** blank, as these channels will not be present
   in your input.
   The following is an excerpt of a job settings JSON that specifies pre-mixed
   audio descriptions for a stereo output:

```
{
  "Settings": {
    "Inputs": [],
    "OutputGroups": [
      {
        "Name": "File Group",
        "OutputGroupSettings": {
          "Type": "FILE_GROUP_SETTINGS",
          "FileGroupSettings": {}
        },
        "Outputs": [
          {
            "VideoDescription": {},
            "AudioDescriptions": [
              {
                "CodecSettings": {
                  "Codec": "AAC",
                  "AacSettings": {
                    "Bitrate": 96000,
                    "CodingMode": "CODING_MODE_2_0",
                    "SampleRate": 48000,
                    "AudioDescriptionBroadcasterMix": "BROADCASTER_MIXED_AD"
                  }
                }
              }
            ],
            "ContainerSettings": {
              "Container": "MP4",
              "Mp4Settings": {}
            }
          }
        ]
      }
    ]
  }
}
```
