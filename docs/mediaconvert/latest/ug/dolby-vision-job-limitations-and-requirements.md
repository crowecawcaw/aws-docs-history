# Dolby

Vision input format support and job setting requirements

The tables in this section describe Dolby Vision input format support
and job setting requirements for implementation with AWS Elemental MediaConvert.

The following table describes input format requirements for Dolby
Vision Profile 5 or Profile 8.1 outputs.

| Supported inputs with Dolby Vision metadata                                                                                                                                                              | Supported inputs without Dolby Vision metadata                                                             | Supported output Dolby Vision profile |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| IMF, MXF<br>• Video codec: JPEG 2000<br>• Input Dolby Vision metadata:<br>Frame-interleaved or XML file<br>QuickTime (.mov)<br>• Video codec: Apple ProRes<br>• Input Dolby Vision metadata: XML<br>file | HDR10<br>• Video codec: Any capable of carrying HDR10<br>SDR<br>• Video codec: Any capable of carrying SDR | Profile 5<br>Profile 8.1              |

The following table describes feature limitations and job requirements for
Dolby Vision outputs.

| Feature                                                                    | Job setting requirement                                                                 |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Maximum number of input videos or input clips<br>(For Profile 8.1 outputs) | One per job                                                                             |
| Input **Frame rate**                                                       | All inputs must have the same frame rate. Frame rate conversion is<br>not supported.    |
| Input **Image inserter**                                                   | Supported<br>(The brightness of your image will vary along with your video<br>content.) |
| Output **Frame rate**                                                      | **Follow source**                                                                       |
| Output **Image inserter**                                                  | **Disabled**                                                                            |
| Output **Video codec**                                                     | **HEVC (H.265)**                                                                        |
| Output **Color metadata**                                                  | **Insert**                                                                              |
| Output video **Resolution (w x h)**                                        | Maximum width: 4096Maximum height: 4096                                                 |
| Output video codec **Profile**                                             | **Main10/Main\*<br>• or<br>**Main10/High\*\*                                            |
| Captions **Destination type**                                              | Burn-in captions are not supported.                                                     |
| **Respond to AFD**                                                         | **None**                                                                                |
| \*_Color corrector_<br>• preprocessor                                      | **Disabled**                                                                            |
| \*_Timecode burn-in_<br>• preprocessor                                     | **Disabled**                                                                            |
| \*_Noise reducer_<br>• preprocessor                                        | **Disabled**                                                                            |
| **Motion image inserter**                                                  | **Disabled**                                                                            |
| \*_Queue_<br>• type                                                        | **On-demand queue**                                                                     |
