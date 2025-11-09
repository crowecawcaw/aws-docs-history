# Audio settings requirements for different MXF profiles

This table shows the requirements for how you set up your output audio tracks in your
AWS Elemental MediaConvert job. The requirements are different for each MXF profile that you
choose.

###### Note

If you don't include any audio tracks in your output, then you must make sure that
there is no audio at all in your job settings.

- In your JSON job specification, this means removing the
  `AudioDescriptions` object entirely.
- In the MediaConvert console, this means that you must delete the **Audio 1** tab that MediaConvert inserts for you by default.
  Delete it by choosing it, and then choosing **Remove
  audio** in the upper right of the **Encoding settings** section.

| MXF profile       | Output audio requirements                                                                                                                                                                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generic OP1a      | Audio codec: Uncompressed WAV<br>Number of channels per track: 1, 2, 4, 6, or 8                                                                                                                                                                                                         |
| Sony XAVC (RDD32) | Audio codec: Uncompressed WAV<br>Number of channels per track: 1<br>Number of tracks per output: Any even number from 2 through 16<br>Bit depth: 24 bits<br>Sample rate: 48 kHz                                                                                                         |
| Sony XDCAM        | Audio codec: Uncompressed WAV<br>Number of channels per track: 1<br>Number of tracks per output: Any even number from 2 through 16, or<br>no audio at all<br>Bit depth: 16 bits or 24 bits; you must choose the same value for<br>all audio tracks in the output<br>Sample rate: 48 kHz |
| XDCAM RDD9        | Audio codec: Uncompressed WAV<br>Number of channels per track: 1<br>Number of tracks per output: 2, 4, or 8<br>Bit depth: 16 bits or 24 bits; you must choose the same value for<br>all audio tracks in the output<br>Sample rate: 48 kHz                                               |
| D10 (SMPTE-386)   | Audio codec: Uncompressed WAV<br>Number of channels per track: 4 or 8<br>Number of tracks per output: 1, or no audio at all<br>Bit depth: 16 bits or 24 bits; you must choose the same value for<br>all audio tracks in the output<br>Sample rate: 48 kHz                               |
