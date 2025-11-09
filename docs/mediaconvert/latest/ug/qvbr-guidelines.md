# Configuring quality-defined variable bitrate

mode

When you use QVBR, you can specify the quality level for your output and the maximum
peak bitrate. For reasonable values of those settings, the encoder chooses how many
bits to use for each part of the video. When you apply the same settings to several
assets, your job outputs for simpler assets (such as cartoons) have smaller file sizes
than your outputs for visually complex assets (such as high-motion sports with brightly
dressed crowds in the background).

This section provides information about the QVBR settings. The following table
provides a set of recommended values to get started with. Specify your values for these
settings when you create your outputs, as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md"). For more information about each setting,
choose a topic from the list that follows the table.

| Resolution | Width | Height | QVBR quality level | Max bitrate |
| ---------- | ----- | ------ | ------------------ | ----------- |
| 1080p      | 1920  | 1080   | 9                  | 6000000     |
| 720p       | 1280  | 720    | 8                  | 4000000     |
| 720p       | 1280  | 720    | 7                  | 2000000     |
| 480p       | 852   | 480    | 7                  | 1000000     |
| 360p       | 640   | 360    | 7                  | 700000      |
| 288p       | 512   | 288    | 7                  | 350000      |

With all resolutions, don't specify a value for **Max average
bitrate** unless you need to guarantee a total file size cap. When you
specify a maximum average bitrate, it reduces the benefit that QVBR provides in video
quality to file size ratio. To use **Max average bitrate**, you have to
first set **Quality tuning level** to **Multi-pass
HQ**.

If you aren't using **Max average bitrate**, and you don't need
multi-pass encoding for other reasons, set **Quality tuning level** to
**Single-pass HQ**.

###### Note

Multi-pass encoding is a professional tier feature. For more information about
MediaConvert pricing tiers, see [MediaConvert pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/").

## Setting QVBR quality tuning level

### Default QVBR quality level

You can keep the QVBR quality level blank to let the encoder automatically
determine the appropriate quality level based on the input video frames. When
you choose the default option, the encoder produces a more consistent quality
across the entire video instead of a specified target quality level. If you
choose this option, you can’t maintain a differentiated quality level based on
the intended viewing device (for example, large-screen TV, PC or tablet, or
smartphone). The encoder determines the appropriate quality level for you, based
on the characteristics of your input video, to maintain a consistent video
quality.

### Custom QVBR quality level

You can specify the **QVBR quality level** on a scale between
1 and 10. The encoder determines the right number of bits to use for each part
of the video to maintain the video quality that you specify.

The best value for an output depends on how the output will be viewed. In
general, set **QVBR quality level** as shown in the following
table.

| Intended viewing device | Recommended QVBR quality level for 720p/1080p |
| ----------------------- | --------------------------------------------- |
| Large-screen TV         | 8 or 9                                        |
| PC or tablet            | 7                                             |
| Smartphone              | 6                                             |

The following graph shows how changing the quality level affects the bitrate
that the encoder uses for different parts of the video. While the lines for both
level 7 and level 9 spike and drop in the same places, the encoder uses more
bits total when the quality is set higher.

![Both lines vary over time. The line that shows QVBR level 7 is shifted below the line for QVBR level 9.](images/RateCtlModeChart2.png)
