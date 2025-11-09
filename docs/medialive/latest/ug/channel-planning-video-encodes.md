# Identify the video encodes

You must decide on the number of video encodes and their codecs. Follow this procedure for
each output group.

1. Determine the maximum number of encodes that are allowed in the output group. The
   following rules apply for each type of output group.

| Type of output group | Rule for video encodes                                                     |
| -------------------- | -------------------------------------------------------------------------- |
| Archive              | One or<br>more video<br>encodes.                                           |
| CMAF Ingest          | One or more video encodes. Typically, there are multiple video<br>encodes. |
| Frame Capture        | One video encode.                                                          |
| HLS or MediaPackage  | One or more video encodes. Typically, there are multiple video<br>encodes. |
| Microsoft Smooth     | One or more video encodes. Typically, there are multiple video<br>encodes. |
| RTMP                 | One video encode.                                                          |
| SRT                  | One or more video encodes.                                                 |
| UDP                  | One or<br>more video<br>encodes.                                           |

2. If the output group allows more than one video encode, decide how many you want. Keep
   in mind that you can create multiple output encodes from the single video source that
   MediaLive ingests.
3. Identify the codec or codecs for the video encodes.
   - For most types of output groups, the downstream system dictates the codec for each
     video encode, so you obtained this information when you identified the output encodes.
   - For an Archive output group, you decide which codec suits your purposes.

4. Identify the resolution and bitrate for each video encode. You might have obtained
   requirements or recommendations from your downstream system when you identified the output encodes.
5. Identify the frame rates for each video encode. If you are using more than one video
   encode, you can ensure compatibility by choosing output frame rates that are multiples of
   the lowest frame rate used.

Examples:

    * 29.97 and 59.94 frames per second are compatible frame rates.
    * 15, 30, and 60 frames per second are compatible frame rates.
    * 29.97 and 30 frames per second are *not*
     compatible frame rates.
    * 30 and 59.94 frames per second are *not*
     compatible frame rates.
