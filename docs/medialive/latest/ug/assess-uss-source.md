# Assess video content

Consult the following table for information about how to assess video
source. Read across each row.

###### Note

You don't need to perform any assessment of the video being delivered
over CDI or from an AWS Elemental Link device. These sources are always acceptable to
MediaLive.

| Information to obtain                                                    | Verify the following                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The available video codecs or formats.                                   | Make sure that at least one of the video codecs is included in the list of video codecs<br>for the package format. See [Supported codecs by input type](inputs-supported-codecs-by-input-type.md "inputs-supported-codecs-by-input-type.md") . If<br>the content is available in more than one supported codec, decide which single video codec<br>you want to use. You can extract only one video asset from the source<br>content. |
| The maximum expected bitrate.                                            | Make sure that the bandwidth between the upstream system and MediaLive<br>is sufficient to handle the anticipated maximum bitrate of the source<br>content.If you are setting up standard channels (to implement<br>[pipeline redundancy](plan-redundancy.md "plan-redundancy.md")), make sure<br>that the bandwidth is double the anticipated maximum bitrate because<br>there are two pipelines.                                   |
| Whether the video characteristics change in the middle of the<br>stream. | For best results, verify that the video characteristics of the<br>video source don't change in the middle of the stream. For example, the<br>codec should not change. The frame rate should not<br>change.                                                                                                                                                                                                                           |
