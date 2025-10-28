# Identifying content in an MP4 source

The content in an MP4 source always consists of one video track, one or more audio tracks,
and optional captions.

Obtain identifying information from the content provider.

| Asset    | Details                                                                                               | Information to obtain                                                                      |
| -------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Video    | You don't need identifying information. MediaLive always extracts the single video asset.             | None                                                                                       |
| Audio    | The source might include multiple audio tracks, typically, one for each language.                     | Obtain the track numbers or three-character language codes of the languages that you want. |
| Captions | EmbeddedThe captions might be embedded in the video track or might be embedded in an ancillary track. | Obtain the languages in the channel numbers. For example, "channel 1 is French".           |
