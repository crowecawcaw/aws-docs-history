

# Identify the video encodes
<a name="channel-planning-video-encodes"></a>

You must decide on the number of video encodes and their codecs. Follow this procedure for each output group. 

1. Determine the maximum number of encodes that are allowed in the output group. The following rules apply for each type of output group.



<table>
<thead>
  <tr><th>Type of output group</th><th>Rule for video encodes</th></tr>
</thead>
<tbody>
  <tr><td>Archive</td><td>One or more video encodes.</td></tr>
  <tr><td>CMAF Ingest</td><td>One or more video encodes. Typically, there are multiple video encodes.</td></tr>
  <tr><td>Frame Capture</td><td>One video encode.</td></tr>
  <tr><td>HLS or MediaPackage</td><td>One or more video encodes. Typically, there are multiple video encodes.</td></tr>
  <tr><td>Microsoft Smooth</td><td>One or more video encodes. Typically, there are multiple video encodes.</td></tr>
  <tr><td>RTMP</td><td>One video encode.</td></tr>
  <tr><td>SRT</td><td>One or more video encodes.</td></tr>
  <tr><td>UDP</td><td>One or more video encodes. </td></tr>
</tbody>
</table>


1. If the output group allows more than one video encode, decide how many you want. Keep in mind that you can create multiple output encodes from the single video source that MediaLive ingests.

1. Identify the codec or codecs for the video encodes. 
   + For most types of output groups, the downstream system dictates the codec for each video encode, so you obtained this information when you [identified the output encodes](#channel-planning-video-encodes). 
   + For an Archive output group, you decide which codec suits your purposes.

1. Identify the resolution and bitrate for each video encode. You might have obtained requirements or recommendations from your downstream system when you [identified the output encodes](#channel-planning-video-encodes).

1. Identify the frame rates for each video encode. If you are using more than one video encode, you can ensure compatibility by choosing output frame rates that are multiples of the lowest frame rate used. 

   Examples:
   + 29.97 and 59.94 frames per second are compatible frame rates.
   + 15, 30, and 60 frames per second are compatible frame rates.
   + 29.97 and 30 frames per second are *not* compatible frame rates.
   + 30 and 59.94 frames per second are *not* compatible frame rates. 

    

If the output group will participate in Dynamic Multiview, the video encodes can be configured by following the instructions in [Setting Up Dynamic Multiview Outputs (Console)](dynamic-multiview-console.md).