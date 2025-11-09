# Audio requirements

## Supported

audio

The audio must meet the following requirements:

- Sample-rate frequency: 48 kHz (48000 samples per second).
- Number of channels: Up to 8 audio channels.
- Interleaved samples.
- The audio must conform to one of the coding modes and channel layouts
  specified in the following table.

In the table, read across each row to identify the channel layout for
the coding mode that is identified in the first cell.

| Coding mode           | Ch 1        | Ch 2         | Ch 3   | Ch 4 | Ch 5          | Ch 6           | Ch 7        | Ch 8         |
| --------------------- | ----------- | ------------ | ------ | ---- | ------------- | -------------- | ----------- | ------------ |
| Mono                  | Left        |              |        |      |               |                |             |              |
| Stereo                | Stereo left | Stereo right |        |      |               |                |             |              |
| 5.1 audio             | Front left  | Front right  | Center | LFE  | Surround left | Surround right |             |              |
| 5.1 audio plus stereo | Front left  | Front right  | Center | LFE  | Surround left | Surround right | Stereo left | Stereo right |

## Recommended minimum bitrate

We recommend the minimum audio bitrates listed in the following table.
If you set the audio bitrates lower than the recommended values, your
watermarks might not be reliably detected.

| Codec                     | Coding mode | Minimum bitrate (kbps) |
| ------------------------- | ----------- | ---------------------- |
| Dolby Digital             | Stereo      | 192                    |
| 5.1                       | 384         |
| Dolby Digital Plus        | Stereo      | 192                    |
| 5.1                       | 192         |
| AAC with the LC profile   | Stereo      | 128                    |
| AAC with the HEV1 profile | 5.1         | 256                    |
| MPEG-1, layer II          | Stereo      | 96                     |
