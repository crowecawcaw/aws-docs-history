# Adobe RTMP output

Adobe RTMP output does not support passthrough of the SCTE-35
messages but does support manifest decoration. Therefore, the
workable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect                                                                                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------------- | ------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Not applicable      | Yes or No                     | Enabled             | Yes or No             | Removes SCTE-35 messages from the video stream.<br>But instructions are included in the manifest. You<br>could insert extra messages: although they are not<br>included in the video stream of the output, they are<br>represented by instructions in the manifest. You<br>could also implement blanking and blackout. |
| Not applicable      | No                            | Disabled            | No                    | Removes SCTE-35 messages from the output. The<br>manifest is not decorated. Do not implement blanking<br>or blackout because, without SCTE-35 messages in the<br>video stream and without manifest decoration, it is<br>impossible to find these blanks and blackouts<br>programmatically.                             |
