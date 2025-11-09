# Summary of encode rules for output groups

This table summarizes the rules for encodes for each output group. In the first column,
find the output group that
you want, then read across the row.

| Type of output group | Rule for video encodes                                                  | Rule for audio encodes                                                   | Rule for captions encodes                                                                                                                                    |
| -------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Archive              | One or more<br>video<br>encodes.                                        | Zero or more audio encodes.                                              | Zero or more captions encodes. The captions are either embedded or object-style<br>captions.                                                                 |
| CMAF<br>Ingest       | One or more video encodes. Typically, there are multiple video encodes. | Zero or more audio encodes. Typically, there are multiple audio encodes. | Zero or more captions encodes. Typically, there are caption languages to match<br>the audio languages. The captions<br>are embedded<br>or sidecar captions.  |
| Frame Capture        | One video encode.                                                       | Zero audio encodes.                                                      | Zero captions encodes.                                                                                                                                       |
| HLS or MediaPackage  | One or more video encodes. Typically, there are multiple video encodes. | Zero or more audio encodes. Typically, there are multiple audio encodes. | Zero or more captions encodes. Typically, there are caption languages to match<br>the audio languages. The captions are either embedded or sidecar captions. |
| Microsoft Smooth     | One or more video encodes. Typically, there are multiple video encodes. | Zero or more audio encodes. Typically, there are multiple audio encodes. | Zero or more captions encodes. Typically, there are caption languages to match<br>the audio languages. The captions are always sidecar captions.             |
| RTMP                 | One video encode.                                                       | Zero or one audio encodes.                                               | Zero or one caption encodes. The captions are either embedded or object-style<br>captions.                                                                   |
| SRT caller           | One or more video encodes.                                              | One or more audio encodes.                                               | Zero or more captions encodes. The captions are either embedded or object-style<br>captions.                                                                 |
| UDP                  | One or more<br>video<br>encodes.                                        | One or more audio encodes.                                               | Zero<br>or more captions encodes. The captions are either embedded or object-style<br>captions.                                                              |

Some output groups also support audio-only outputs. See [Setting up the output](audio-only-outputs-and-outputgroups.md "audio-only-outputs-and-outputgroups.md").

Some output groups also support outputs that contain JPEG files, to support trick play
according to the Roku specification. See [Trick-play track via the Image
Media Playlist specification](trick-play-roku.md "trick-play-roku.md").
