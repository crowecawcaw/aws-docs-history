

# Audio requirements
<a name="supportedaudio"></a>

## Supported audio
<a name="nielsen-watermarks-input-audio"></a>

All the source audio in the MediaLive inputs must meet the following requirements:
+ Sample-rate frequency: 48 kHz (48000 samples per second).
+ Up to 8 audio channels, with interleaved samples.
+ The audio must conform to one of the coding modes and channel layouts specified in the following table.

In the table, read across each row to identify the channel layout for the coding mode that is identified in the first cell.


| Number of channels |  Coding mode  | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 | Ch 7 | Ch 8 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 1 | Mono | Left |  |  |  |  |  |  |  | 
| 2 | Stereo | Stereo left | Stereo right |  |  |  |  |  |  | 
| 6 | 5.1 audio | Front left | Front right | Center | LFE | Surround left | Surround right |  |  | 
| 8 | 5.1 audio plus stereo | Front left | Front right | Center | LFE | Surround left | Surround right | Stereo left | Stereo right | 

## Recommended minimum bitrates
<a name="nielsen-watermarks-input-audio-bitrate"></a>

We strongly recommend following the minimum audio bitrates listed in the following table. If you set the audio bitrates lower than the recommended values, your watermarks might not be reliably detected.



- ** Dolby Digital  **
  - **Coding mode:** Stereo / **Minimum bitrate (kbps):** 192
  - **Coding mode:** 5.1 / **Minimum bitrate (kbps):** 384

- **Dolby Digital Plus**
  - **Coding mode:** Stereo / **Minimum bitrate (kbps):** 192
  - **Coding mode:** 5.1 / **Minimum bitrate (kbps):** 192

- **AAC with the LC profile**
  - **Coding mode:** Stereo
  - **Minimum bitrate (kbps):** 128

- **AAC with the HEV1 profile**
  - **Coding mode:** 5.1
  - **Minimum bitrate (kbps):** 256

- ** MPEG-1, layer II **
  - **Coding mode:** Stereo
  - **Minimum bitrate (kbps):** 96

