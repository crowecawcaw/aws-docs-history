# Apple HLS output

Apple HLS output supports both passthrough of the SCTE-35
messages and manifest decoration. In fact, with HLS outputs,
passthrough and manifest decoration are either both enabled or
both disabled. Therefore, workable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | ----------------------------- | ------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled             | Yes or No                     | Enabled             | Yes or No             | Turns on passthrough of SCTE-35 messages and<br>manifest decoration. In this case, you could also<br>insert more SCTE-35 message if desired. You could<br>also implement blanking and blackout.                                                                                                                                                                              |
| Disabled            | No                            | Disabled            | No                    | Turns off passthrough in order to remove<br>SCTE-35 messages from the video stream. Turns off<br>manifest decoration. Do not insert extra messages:<br>they simply get stripped from the output. Do not<br>implement blanking or blackout.<br>Choose this option only if, in a downstream<br>system, you do not want to replace video that was<br>originally marked by cues. |
