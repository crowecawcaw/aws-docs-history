# DASH output

DASH ISO output does not support passthrough of the SCTE-35
messages or manifest decoration. Therefore, the only workable
option is the default behavior:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                                     |
| ------------------- | ----------------------------- | ------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Not applicable      | No                            | Not applicable      | No                    | Removes SCTE-35 messages from the output. The<br>manifest is not decorated. Do not implement<br>blanking or blackout because, without SCTE-35<br>messages in the video stream and without manifest<br>decoration, it is impossible to find these blanks<br>and blackouts programmatically. |
