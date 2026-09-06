

# Audio requirements
<a name="nielsen-wmark-requirements"></a>

## Supported audio
<a name="nielsen-wmark-supportedaudio"></a>

The audio must meet the following requirements:
+ Sample-rate frequency: 48 kHz (48000 samples per second).
+ Number of channels: Up to 8 audio channels.
+ Interleaved samples.
+ The audio must conform to one of the coding modes and channel layouts specified in the following table.

In the table, read across each row to identify the channel layout for the coding mode that is identified in the first cell.


|  Coding mode  | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 | Ch 7 | Ch 8 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Mono | Left |  |  |  |  |  |  |  | 
| Stereo | Stereo left | Stereo right |  |  |  |  |  |  | 
| 5.1 audio | Front left | Front right | Center | LFE | Surround left | Surround right |  |  | 
| 5.1 audio plus stereo | Front left | Front right | Center | LFE | Surround left | Surround right | Stereo left | Stereo right | 

## Recommended minimum bitrate
<a name="nielsen-min-bitrate"></a>

We recommend the minimum audio bitrates listed in the following table. If you set the audio bitrates lower than the recommended values, your watermarks might not be reliably detected.



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

