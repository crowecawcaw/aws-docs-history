# Identify the audio encodes

You must decide on the number of audio encodes. Follow this procedure for each output
group.

1. Determine the maximum number of encodes that are allowed in the output group. The
   following rules apply for each type of output group.

| Type of output group | Rule for audio encodes                                                   |
| -------------------- | ------------------------------------------------------------------------ |
| Archive              | Zero or more audio encodes.                                              |
| CMAF Ingest          | Zero or more audio encodes. Typically, there are multiple audio encodes. |
| Frame Capture        | Zero audio encodes.                                                      |
| HLS or MediaPackage  | Zero or more audio encodes. Typically, there are multiple audio encodes. |
| Microsoft Smooth     | Zero or more audio encodes. Typically, there are multiple audio encodes. |
| RTMP                 | Zero or one audio encodes.                                               |
| SRT                  | One or more audio encodes.                                               |
| UDP                  | One or more audio encodes.                                               |

2. If the output group allows more than one audio encode, decide how many you want. These
   guidelines apply:
   - Each different combination of output codec, coding mode, and language is one
     encode.

   MediaLive can produce a specific coding mode only if the source contains that coding
   mode or a higher mode. For example, MediaLive can create 1.0 from a 1.0 or a 2.0 source.
   It can't create 5.1 from a 2.0 source.
   - MediaLive can produce a specific language only if the source contains that language.
   - MediaLive can produce more than one encode for a given language.

   For example, you could choose to include Spanish in Dolby 5.1 and in AAC
   2.0.
   - There is no requirement for the count of encodes to be the same for all languages.
     For example, you could create two encodes for Spanish, and only one encode for the
     other languages.

3. Identify the bitrate for each audio encode. You might have obtained requirements or
   recommendations from your downstream system when you identified the output encodes.
