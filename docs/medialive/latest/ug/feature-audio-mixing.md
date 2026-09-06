

# Audio channel mixing and remixing
<a name="feature-audio-mixing"></a>

AWS Elemental MediaLive provides a two-stage audio processing pipeline that you can use to combine audio from multiple sources and remap channels for your output. You can pre-mix multiple audio PIDs or tracks into a single combined stream, and then remix that stream into your desired output channel layout.

**Topics**
+ [About audio mixing in MediaLive](#audio-mixing-about)
+ [Pre-mixing audio from multiple PIDs](#audio-mixing-multi-pid)
+ [Pre-mixing audio from multiple tracks](#audio-mixing-multi-track)
+ [Remixing channels in the output](#audio-mixing-output-remix)
+ [Combining pre-mixing and output remixing](#audio-mixing-combined-example)

## About audio mixing in MediaLive
<a name="audio-mixing-about"></a>

MediaLive processes audio mixing in two stages. You can use either stage independently or combine both stages in the same channel.

Stage 1: Pre-mixing  
When your input contains multiple audio PIDs (in a transport stream) or multiple tracks, you can select multiple PIDs or tracks in a single audio selector. MediaLive independently processes each one—you can remix channels, adjust gain, and normalize loudness—before MediaLive interleaves the results into a combined audio stream.

Stage 2: Output remixing  
After pre-mixing (or for single-PID/track inputs), you can remap channels in the audio description by using `RemixSettings`. This produces the final channel layout, for example downmixing 5.1 surround to stereo.

**Note**  
Pre-mixing is optional. You can use output remixing alone if you only need to remap channels from a single audio source.

## Pre-mixing audio from multiple PIDs
<a name="audio-mixing-multi-pid"></a>

To pre-mix audio from multiple PIDs in a transport stream input, use `AudioPidSelection` with the `Pids` array. This replaces the legacy single `Pid` field.

Each entry in the `Pids` array is an `AudioPid` object with the following fields:
+ `Pid` (integer, 32–8190) — The PID value.
+ `PremixSettings` (optional) — An `AudioPreMixerSettings` object that controls how MediaLive processes this PID before interleaving.

The `AudioPreMixerSettings` object contains the following fields:
+ `Channels` (integer, 1–16) — Target channel count for this PID. If you specify this field, MediaLive remixes the audio to this channel count by using a default matrix.
+ `RemixSettings` — Fine-grained channel mapping. This is mutually exclusive with `Channels`—you cannot specify both. Uses the same structure as the output-level `RemixSettings`.
+ `GainDb` (number, -60 to \+60) — Gain adjustment in dB applied to this PID's audio.
+ `AudioNormalizationSettings` — Loudness normalization settings (algorithm, target LKFS, and so on).

The following constraints apply:
+ You must specify at least 2 PIDs when using `PremixSettings`.
+ You can specify a maximum of 16 PIDs per selector.
+ The total output channels across all PIDs with premix settings cannot exceed 16.

The following example shows two PIDs being pre-mixed. PID 101 contains stereo audio remixed to mono (1 channel) with -3 dB gain. PID 102 contains stereo audio kept as stereo (2 channels). The result is a 3-channel interleaved output.

```
{
  "AudioSelectors": {
    "my_mixed_audio": {
      "SelectorSettings": {
        "AudioPidSelection": {
          "Pids": [
            {
              "Pid": 101,
              "PremixSettings": {
                "Channels": 1,
                "GainDb": -3
              }
            },
            {
              "Pid": 102,
              "PremixSettings": {
                "Channels": 2
              }
            }
          ]
        }
      }
    }
  }
}
```

## Pre-mixing audio from multiple tracks
<a name="audio-mixing-multi-track"></a>

To pre-mix audio from multiple tracks, use `AudioTrackSelection` with the `Tracks` array. This works the same way as PID-based pre-mixing but uses track numbers instead of PID values.

Each entry in the `Tracks` array is an `AudioTrack` object with the following fields:
+ `Track` (integer, 1-based) — The track number.
+ `PremixSettings` (optional) — An `AudioPreMixerSettings` object. This uses the same structure and fields as described in the preceding PID section.

The same constraints apply: you must specify at least 2 tracks when using `PremixSettings`, and the total output channels cannot exceed 16.

The following example shows two tracks being pre-mixed. Track 1 contains stereo audio remixed to mono. Track 2 contains stereo audio kept as stereo.

```
{
  "AudioSelectors": {
    "my_mixed_tracks": {
      "SelectorSettings": {
        "AudioTrackSelection": {
          "Tracks": [
            {
              "Track": 1,
              "PremixSettings": {
                "Channels": 1,
                "GainDb": -3
              }
            },
            {
              "Track": 2,
              "PremixSettings": {
                "Channels": 2
              }
            }
          ]
        }
      }
    }
  }
}
```

## Remixing channels in the output
<a name="audio-mixing-output-remix"></a>

You can configure `RemixSettings` at the audio description level (output encode) to remap channels from the input stream into your desired output channel layout.

The `RemixSettings` object contains the following fields:
+ `ChannelsIn` (integer, 1–16) — Number of input channels to map from.
+ `ChannelsOut` (integer, 1–8) — Number of output channels to produce.
+ `ChannelMappings` (array) — One entry per output channel. Each entry contains:
  + `OutputChannel` (integer, 0-based index) — The output channel index.
  + `InputChannelLevels` (array) — Contribution from each input channel. Each entry contains:
    + `InputChannel` (integer, 0-based index) — The input channel index.
    + `Gain` (integer, -60 to \+6) — Gain in dB for this input channel's contribution.

The following example shows a 5.1 surround to stereo downmix. Input channels 0–5 represent the standard 5.1 layout (L, R, C, LFE, LS, RS). The output maps left-facing channels to output channel 0 and right-facing channels to output channel 1.

```
{
  "RemixSettings": {
    "ChannelsIn": 6,
    "ChannelsOut": 2,
    "ChannelMappings": [
      {
        "OutputChannel": 0,
        "InputChannelLevels": [
          {"InputChannel": 0, "Gain": 0},
          {"InputChannel": 2, "Gain": -3},
          {"InputChannel": 4, "Gain": -6}
        ]
      },
      {
        "OutputChannel": 1,
        "InputChannelLevels": [
          {"InputChannel": 1, "Gain": 0},
          {"InputChannel": 2, "Gain": -3},
          {"InputChannel": 5, "Gain": -6}
        ]
      }
    ]
  }
}
```

**Note**  
A gain value of -60 effectively mutes that input channel's contribution to the output.

## Combining pre-mixing and output remixing
<a name="audio-mixing-combined-example"></a>

You can use both stages together. First, pre-mix multiple PIDs or tracks into a combined stream. Then, apply `RemixSettings` on the audio description to produce the final output layout.

For example, consider two stereo PIDs that you pre-mix without channel reduction. MediaLive interleaves them into a 4-channel combined stream. You then configure `RemixSettings` on the audio description with `ChannelsIn` set to 4 and `ChannelsOut` set to 2. This produces a stereo output that blends content from both original PIDs.