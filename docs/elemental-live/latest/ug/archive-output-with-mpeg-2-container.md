# Archive

output with MPEG-2 container

A transport stream (TS) in an MPEG-2 container supports
passthrough of the SCTE-35 messages, but it does not support
creation of a manifest. Therefore, usable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                                                                                          |
| ------------------- | ----------------------------- | ------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled             | Yes or No                     | Not applicable      | Yes or No             | Turns on passthrough of SCTE-35 messages. In this<br>case, you could also insert more SCTE-35 message if<br>desired. You could also implement blanking and<br>blackout.                                                                                                                                                                         |
| Disabled            | No                            | Not applicable      | No                    | Turns off passthrough in order to remove<br>SCTE-35 messages from the video stream. Do not<br>insert extra messages: they simply get stripped<br>out of the output. Do not implement blanking or<br>blackout.<br>Choose this option only if, in a downstream<br>system, you do not want to replace video that was<br>originally marked by cues. |
