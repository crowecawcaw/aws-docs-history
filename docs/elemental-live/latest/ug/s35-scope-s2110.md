# SMPTE 2110 output

SMPTE 2110 output supports passthrough of the SCTE-35
messages. Therefore, workable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                                         |
| ------------------- | ----------------------------- | ------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled             | Yes or No                     | Not applicable      | Yes or No             | Turns on passthrough of SCTE-35 messages. In this case, you could also insert more SCTE-35 messages if desired. Elemental Live converts all these SCTE-35 messages to SCTE-104 messages in the ancillary data stream in the output.You could also implement blanking and blackout.             |
| Disabled            | No                            | Not applicable      | No                    | Doesn't include SCTE-104 messages in the output. Do not insert extra messages: they are simply get stripped out of the output. Do not implement blanking or blackout. Choose this option only if, in a downstream system, you do not want to replace video that was originally marked by cues. |
