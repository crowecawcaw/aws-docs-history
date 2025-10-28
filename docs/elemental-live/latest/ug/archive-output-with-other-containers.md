# Archive

output with other containers

Other archive outputs do not support passthrough of the
SCTE-35 messages or manifest decoration. Therefore, the only
workable option is the default behavior:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                      |
| ------------------- | ----------------------------- | ------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Not applicable      | No                            | Not applicable      | No                    | Removes SCTE-35 messages from the output. The manifest is not decorated. Do not implement blanking or blackout because, without SCTE-35 messages in the video stream and without manifest decoration, it is impossible to find these blanks and blackouts programmatically. |
