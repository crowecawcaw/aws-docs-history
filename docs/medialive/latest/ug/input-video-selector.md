# Input settings—Video selector

This section lets you identify the video to extract from the input, and lets you
enable the optional color space feature.

1. In **Video selector**, choose **Video
   selector**. More fields appear.
2. Complete **Selector settings** as specified in the table
   after this procedure.

Keep in mind that there is no button to add more video selectors because
you can extract only one video asset from the input. 3. For all input types, complete **Color space** and
**Color space usage**, but only if you want to
configure the handling of color space. For more information, see [Handling complex color space conversions](color-space.md "color-space.md").
**Determining whether you need to create a video
selector**

When you planned the channel, you should have [identified the video](channel-map-output-source.md "channel-map-output-source.md") that you
need to extract from this input.

You must now determine if you need to create a _video
selector_, to identify the specific asset to extract from the input.
Some input types require selectors, some input types don't require them.

The following table specifies whether you need to create a video selector.

| Input type                        | Add a video selector?                                                      | How video is extracted                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CDI                               | No                                                                         | MediaLive extracts the first video that it encounters in the source<br>content.                                                                                                                                                                                                                                                                                                                                                |
| Elemental Link                    | No                                                                         | The input contains only one video asset. MediaLive extracts that<br>video.                                                                                                                                                                                                                                                                                                                                                     |
| HLS                               | No                                                                         | By default, MediaLive extracts the video asset with the highest<br>bandwidth. You can complete the **Bandwidth**<br>field (in **Input settings\*<br>• –<br>**Network input settings\*\*). MediaLive extracts<br>the highest bandwidth video that is below this limit.                                                                                                                                                          |
| MediaConnect                      | Yes, if the input contains an MPTS                                         | Enter the program or PID to extract. If you don't specify the<br>program or PID, MediaLive extracts the first video it finds.                                                                                                                                                                                                                                                                                                  |
| No, if the input contains an SPTS | The input contains only one video asset. MediaLive extracts that<br>video. |
| MediaConnect Router               | Yes, if the input contains an MPTS                                         | Enter the program or PID to extract. If you don't specify the<br>program or PID, MediaLive extracts the first video it finds.                                                                                                                                                                                                                                                                                                  |
| No, if the input contains an SPTS | The input contains only one video asset. MediaLive extracts that<br>video. |
| MP4                               | No                                                                         | The input contains only one video asset. MediaLive extracts that<br>video.                                                                                                                                                                                                                                                                                                                                                     |
| RTMP                              | No                                                                         | The input contains only one video asset. MediaLive extracts that<br>video.                                                                                                                                                                                                                                                                                                                                                     |
| RTP                               | Yes, if the input contains an MPTS                                         | Enter the program or PID to extract. If you don't specify the<br>program or PID, MediaLive extracts the first video it finds.                                                                                                                                                                                                                                                                                                  |
| No, if the input contains an SPTS | The input contains only one video asset. MediaLive extracts that<br>video. |
| SMPTE<br>2110                     | No                                                                         | When you [created the<br>input](setup-input-s2110-pull.md "setup-input-s2110-pull.md"), you identified the video stream to extract.<br>MediaLive automatically selects that video.If the input<br>includes more than one video stream and you didn't enter a media<br>index when you created the input, MediaLive automatically selects the<br>video from the SDP file that has the lowest media index (typically<br>index 0). |
| SRT<br>caller                     | Yes, if the input contains an MPTS                                         | Enter the program or PID to extract. If you don't specify the<br>program or PID, MediaLive extracts the first video it finds.                                                                                                                                                                                                                                                                                                  |
| No, if the input contains an SPTS | The input contains only one video asset. MediaLive extracts that<br>video. |
