# MS Smooth output

MSS output does not support passthrough of the SCTE-35
messages but does support instructions in the sparse track.
Therefore, the workable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                                                          |
| ------------------- | ----------------------------- | ------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Not applicable      | Yes or No                     | Enabled             | Yes or No             | Removes SCTE-35 messages from the video stream. But instructions are included in the sparse track. You could insert extra messages: although they are not included in the video stream of the output, they are represented by instructions in the sparse track. You could also implement blanking and blackout. |
| Not applicable      | No                            | Disabled            | No                    | Removes SCTE-35 messages from the output. The sparse track does not include instructions. Do not implement blanking or blackout because, without SCTE-35 messages in the video stream and, without data in the sparse track, it is impossible to find these blanks and blackouts programmatically.              |
