# Setting up QVBR and rate

control mode

The Rate Control Mode fields in the Video section of each output on the Elemental Live
web interface let you control the quality and bitrate of the video.

When encoding visually complex video (such as high-motion sports events with brightly
dressed crowds in the background), there is always a trade-off between high video quality
and low bitrate. Higher video quality requires higher bitrate. There is less trade-off with
visually simple video such as cartoons.

Elemental Live offers several options that provide different balances of video quality
versus bitrate.

Do the following to set the rate control mode and bitrate for the output:

- In **Event** > **Streams** > **Video** > **Video Code**, choose **H.264**
- In **Event** > **Streams** > **Video** > **Advanced** > **Rate Control Mode for Video**, for
  **Codec settings**, select the desired option. For information about choosing the best option,
  see the sections below.
- Complete other fields, as appropriate:
  - If you select **QVBR**, complete **Max bitrate**, **Quality level**, **Buffer size**, and
    **Buffer fill percentage**.
  - If you select **VBR**, complete **Bitrate (average bitrate)**, **Max bitrate**, **Buffer size**, and **Buffer fill percentage**.
  - If you select **CBR**, complete **Bitrate**, **Buffer size**, and **Buffer fill percentage**.

###### Note

We do not recommend use of either the CQ or ABR options. The Statmux option only
applies if you have the Statmux option enabled on Elemental Live and only if you are
creating a "statmux output".

###### Quality-defined variable bitrate mode (QVBR)

With quality-defined variable bitrate mode (QVBR), you specify a maximum bitrate and
a quality level. Video quality will match the specified quality level except when it is
constrained by the maximum bitrate. This constraint occurs when the video is very
complex, so that it is not possible to reach the quality level without exceeding the
maximum bitrate.

We recommend this mode if you or your viewers pay for bandwidth, for example, if you are
delivering to a CDN or if your viewing users are on mobile networks.

When selecting QVBR, set the quality level and maximum bitrate for your most important
viewing devices. Set the buffer size to twice the maximum bitrate, and set the initial
buffer to 90%. Set the Buffer size to twice (2x) the Max bitrate and set the Buffer fill
percentage to 90%. The buffer contributes to a smooth playout.

The following table lists the recommended values for this mode:

| Viewing device | Quality level | Max bitrate            |
| -------------- | ------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary screen | 8 to 10       | 4,000,000 to 6,000,000 |
| PC or tablet   | 7             | 1,500,000 to 3,000,000 |
| Smartphone     | 6             | 1,000,000 to 1,500,000 | With this mode, the bitrate can change with each frame (in order to obtain at least the specified quality), but it cannot exceed the maximum bitrate. Elemental Live does not attempt to maintain an average bitrate. It always hits the maximum bitrate if that is necessary to obtain the specified quality. On the other hand, if the quality can be obtained with lower bitrates, Elemental Live does not use a higher bitrate. ###### Variable bitrate mode (VBR) With variable bitrate mode (VBR), you specify an average bitrate and a maximum bitrate. Video quality and bitrate vary, depending on the video complexity. Select VBR instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. If bitrate does not need to be constrained, then consider using QVBR. When selecting VBR, try to assess the expected complexity of the video, and set a suitable average bitrate. Set the maximum bitrate to accommodate expected spikes. Set the Buffer size to twice (2x) the Max bitrate and set the Buffer fill percentage to 90%. The buffer contributes to a smooth playout. With this mode, the bitrate can change with each frame (in order to obtain the best quality) but it cannot exceed the specified maximum bitrate. Elemental Live also ensures that as the channel progresses, the stream meets the specified average bitrate. This mode is useful when you expect short spikes in the complexity of the video. Elemental Live aims for the average bitrate but spikes to the maximum bitrate for a short time when necessary. ###### Constant bitrate mode (CBR) With constant bitrate mode (CBR), you specify a bitrate. Video quality varies, depending on the video complexity. Select CBR only if you distribute your assets to devices that cannot handle variable bitrates. But if it is acceptable for the bitrate to occasionally differ from a specified rate, then consider using VBR or QVBR instead. Over the duration of the channel, you might obtain both a lower bitrate and better quality with VBR or QVBR. When selecting CBR, set the bitrate to balance the video quality and the output bitrate. Set the Buffer size to twice (2x) the Max bitrate and set the Buffer fill percentage to 90%. The buffer contributes to a smooth playout. With this mode, the output always matches the specified bitrate. Sometimes that bitrate results in higher-quality video, and sometimes it results in lower-quality video. |
