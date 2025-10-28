# Archive

output with MPEG-2 container

A transport stream (TS) in an MPEG-2 container supports
passthrough of the SCTE-35 messages, but it does not support
creation of a manifest. Therefore, usable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                                                                     |
| ------------------- | ----------------------------- | ------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled             | Yes or No                     | Not applicable      | Yes or No             | Turns on passthrough of SCTE-35 messages. In this case, you could also insert more SCTE-35 message if desired. You could also implement blanking and blackout.                                                                                                                                                             |
| Disabled            | No                            | Not applicable      | No                    | Turns off passthrough in order to remove SCTE-35 messages from the video stream. Do not insert extra messages: they simply get stripped out of the output. Do not implement blanking or blackout. Choose this option only if, in a downstream system, you do not want to replace video that was originally marked by cues. |
