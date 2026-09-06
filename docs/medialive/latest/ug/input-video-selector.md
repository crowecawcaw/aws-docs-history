

# Input settings—Video selector
<a name="input-video-selector"></a>

This section lets you identify the video to extract from the input, and lets you enable the optional color space feature. 

1. In **Video selector**, choose **Video selector**. More fields appear. 

1. Complete **Selector settings** as specified in the table after this procedure. 

   Keep in mind that there is no button to add more video selectors because you can extract only one video asset from the input.

1. For all input types, complete **Color space** and **Color space usage**, but only if you want to configure the handling of color space. For more information, see [Handling complex color space conversions](color-space.md).

**Determining whether you need to create a video selector**

When you planned the channel, you should have [identified the video](channel-map-output-source.md) that you need to extract from this input. 

You must now determine if you need to create a *video selector*, to identify the specific asset to extract from the input. Some input types require selectors, some input types don't require them.

The following table specifies whether you need to create a video selector. 



- **CDI**
  - **Add a video selector?:** No
  - **How video is extracted:** MediaLive extracts the first video that it encounters in the source content.

- **Elemental Link**
  - **Add a video selector?:** No
  - **How video is extracted:** The input contains only one video asset. MediaLive extracts that video. 

- **HLS**
  - **Add a video selector?:** No
  - **How video is extracted:** By default, MediaLive extracts the video asset with the highest bandwidth. You can complete the **Bandwidth** field (in **Input settings** – **Network input settings**). MediaLive extracts the highest bandwidth video that is below this limit.

- **MediaConnect**
  - **Add a video selector?:** Yes, if the input contains an MPTS / **How video is extracted:** Enter the program or PID to extract. If you don't specify the program or PID, MediaLive extracts the first video it finds.
  - **Add a video selector?:** No, if the input contains an SPTS / **How video is extracted:** The input contains only one video asset. MediaLive extracts that video. 

- **MediaConnect Router**
  - **Add a video selector?:** Yes, if the input contains an MPTS / **How video is extracted:** Enter the program or PID to extract. If you don't specify the program or PID, MediaLive extracts the first video it finds.
  - **Add a video selector?:** No, if the input contains an SPTS / **How video is extracted:** The input contains only one video asset. MediaLive extracts that video. 

- **MP4**
  - **Add a video selector?:** No
  - **How video is extracted:** The input contains only one video asset. MediaLive extracts that video. 

- **RTMP**
  - **Add a video selector?:** No
  - **How video is extracted:** The input contains only one video asset. MediaLive extracts that video. 

- **RTP**
  - **Add a video selector?:** Yes, if the input contains an MPTS / **How video is extracted:** Enter the program or PID to extract. If you don't specify the program or PID, MediaLive extracts the first video it finds.
  - **Add a video selector?:** No, if the input contains an SPTS / **How video is extracted:** The input contains only one video asset. MediaLive extracts that video. 

- **SMPTE 2110**
  - **Add a video selector?:** No
  - **How video is extracted:** When you [created the input](setup-input-s2110-pull.md), you identified the video stream to extract. MediaLive automatically selects that video.If the input includes more than one video stream and you didn't enter a media index when you created the input, MediaLive automatically selects the video from the SDP file that has the lowest media index (typically index 0).

- **SRT caller**
  - **Add a video selector?:** Yes, if the input contains an MPTS / **How video is extracted:** Enter the program or PID to extract. If you don't specify the program or PID, MediaLive extracts the first video it finds.
  - **Add a video selector?:** No, if the input contains an SPTS / **How video is extracted:** The input contains only one video asset. MediaLive extracts that video. 

