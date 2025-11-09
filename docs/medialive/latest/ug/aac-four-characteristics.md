# Supported sampling rate and bitrate for AAC

output

This section explains how to set the following four properties of the AAC audio codec when
you are setting up an audio encode in MediaLive:

- Profile
- Coding mode
- Sample rate
- Bitrate
  In the console, these properties are in four fields in the
  **Codec configuration** section for the AAC codec.
  To get here, go to the **Create channel** page and
  choose the appropriate output in the output group. In **Output
  settings**, go to the **Audio** section.
  In Codec settings, choose Aac, then expand
  **Codec configuration**. To review the step where
  you complete these fields, see [Set up the audio encodes](creating-a-channel-step7.md "creating-a-channel-step7.md").

###### Note

You can set all four fields. Or you can leave all the fields with
their defaults.

If you change only one or two fields, you might create a
combination that is not valid. See the tables in the following
sections to verify that the combination you have created is
valid.

###### To set these four fields

1. Choose a **Coding mode**.
2. Choose a **Profile** that is valid with that
   profile. See the tables that follow this procedure.
3. Choose a **Sample rate** that is valid for
   that combination of profile and coding mode.
4. Choose a **Bitrate** that falls within the
   range that is supported for that sample rate.

## Coding mode 1.0

In this table, read down the rows to find the profile that you
want. Then read across to find a valid combination of sample rate
and bitrate.

| Profile | Sample rate (Hz) | Minimum valid bitrate (bits/sec) | Maximum valid bitrate (bits/sec) |
| ------- | ---------------- | -------------------------------- | -------------------------------- |
| HEv1    | 22050            | 8000                             | 12000                            |
| 24000   | 8000             | 12000                            |
| 32000   | 12000            | 64000                            |
| 44100   | 18000            | 64000                            |
| 48000   | 18000            | 64000                            |
| LC      | 8000             | 8000                             | 14000                            |
| 12000   | 8000             | 14000                            |
| 16000   | 8000             | 28000                            |
| 22050   | 24000            | 28000                            |
| 24000   | 24000            | 28000                            |
| 32000   | 32000            | 192000                           |
| 44100   | 56000            | 256000                           |
| 48000   | 56000            | 288000                           |
| 88200   | 288000           | 288000                           |
| 96000   | 128000           | 288000                           |

## Coding mode 1+1

In this table, read down the rows to find the profile that you
want. Then read across to find a valid combination of sample rate
and bitrate.

| Profile | Sample rate (Hz) | Minimum valid bitrate (bits/sec) | Maximum valid bitrate (bits/sec) |
| ------- | ---------------- | -------------------------------- | -------------------------------- |
| HEv1    | 32000            | 24000                            | 128000                           |
| 44100   | 40000            | 192000                           |
| 48000   | 40000            | 192000                           |
| 96000   | 224000           | 256000                           |
| LC      | 8000             | 16000                            | 28000                            |
| 12000   | 16000            | 28000                            |
| 16000   | 16000            | 56000                            |
| 22050   | 48000            | 56000                            |
| 24000   | 48000            | 56000                            |
| 32000   | 64000            | 384000                           |
| 44100   | 112000           | 512000                           |
| 48000   | 112000           | 576000                           |
| 88200   | 256000           | 576000                           |
| 96000   | 256000           | 576000                           |

## Coding mode 2.0

In this table, read down the rows to find the profile that you
want. Then read across to find a valid combination of sample rate
and bitrate.

| Profile | Sample rate (Hz) | Minimum valid bitrate (bits/sec) | Maximum valid bitrate (bits/sec) |
| ------- | ---------------- | -------------------------------- | -------------------------------- |
| HEv1    | 32000            | 16000                            | 128000                           |
| 44100   | 16000            | 96000                            |
| 48000   | 16000            | 128000                           |
| 96000   | 96000            | 128000                           |
| HEv2    | 22050            | 8000                             | 12000                            |
| 24000   | 8000             | 12000                            |
| 32000   | 12000            | 64000                            |
| 44100   | 20000            | 64000                            |
| 48000   | 20000            | 64000                            |
| LC      | 8000             | 16000                            | 20000                            |
| 12000   | 16000            | 20000                            |
| 16000   | 16000            | 32000                            |
| 22050   | 32000            | 32000                            |
| 24000   | 32000            | 32000                            |
| 32000   | 40000            | 384000                           |
| 44100   | 96000            | 512000                           |
| 48000   | 64000            | 576000                           |
| 88200   | 576000           | 576000                           |
| 96000   | 256000           | 576000                           |

## Coding mode 5.1

In this table, read down the rows to find the profile that you
want. Then read across to find a valid combination of sample rate
and bitrate.

| Profile | Sample rate (Hz) | Minimum valid bitrate (bits/sec) | Maximum valid bitrate (bits/sec) |
| ------- | ---------------- | -------------------------------- | -------------------------------- |
| HEv1    | 32000            | 64000                            | 320000                           |
| 44100   | 64000            | 224000                           |
| 48000   | 64000            | 320000                           |
| 96000   | 240000           | 320000                           |
| LC      | 32000            | 160000                           | 768000                           |
| 44100   | 256000           | 640000                           |
| 48000   | 256000           | 768000                           |
| 96000   | 640000           | 768000                           |

## Coding mode

ad receiver mix

Choose this coding mode if you have an AD (audio description)
audio track that you want to include in the output.

In this table, read down the rows to find the profile that you
want. Then read across to find a valid combination of sample rate
and bitrate.

| Profile | Sample rate (Hz) | Minimum valid bitrate (bits/sec) | Maximum valid bitrate (bits/sec) |
| ------- | ---------------- | -------------------------------- | -------------------------------- |
| HEv1    | 22050            | 8000                             | 12000                            |
| HEv1    | 24000            | 8000                             | 12000                            |
| 32000   | 12000            | 64000                            |
| 44100   | 20000            | 64000                            |
| 48000   | 20000            | 64000                            |
| LC      | 8000             | 8000                             | 14000                            |
| 12000   | 8000             | 14000                            |
| 16000   | 8000             | 28000                            |
| 22050   | 24000            | 28000                            |
| 24000   | 24000            | 28000                            |
| 32000   | 32000            | 192000                           |
| 44100   | 56000            | 256000                           |
| 48000   | 56000            | 288000                           |
| 88200   | 288000           | 288000                           |
| 96000   | 128000           | 288000                           |
