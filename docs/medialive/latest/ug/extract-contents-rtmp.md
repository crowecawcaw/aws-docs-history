# Identifying content in an RTMP source

This procedure applies to both RTMP push and pull inputs from the internet, and to RTMP
inputs from Amazon Virtual Private Cloud. The content in an RTMP input always consists of one video, one audio, and
optional captions.

Obtain identifying information from the content provider.

| Asset    | Details                                                                                                  | Information to obtain                                                             |
| -------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Video    | You don't need identifying information. MediaLive always extracts the single video<br>asset.             | None                                                                              |
| Audio    | You don't need identifying information. MediaLive always extracts the single audio<br>asset              | Obtain the numbers and languages of the tracks. For example, "track 1 is French". |
| Captions | EmbeddedThe captions might be embedded in the video track or might be embedded in<br>an ancillary track. | Obtain the languages in the channel numbers. For example, "channel 1 is French".  |
