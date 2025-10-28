# Identifying content in an HLS source

The content in an HLS container is always a transport stream (TS) that contains only one
video rendition (program).

Obtain identifying information from the content provider.

| Asset    | Details                                                                                   | Information to obtain                                                                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Video    | You don't need identifying information. MediaLive always extracts the single video asset. |                                                                                                                                                                                                           |
| Audio    | The source might include multiple audio PIDs.                                             | Obtain the PIDs or three-character language codes of the languages that you want. We recommend that you obtain the PIDs for the audio assets. They are a more reliable way of identifying an audio asset. |
| Captions | Embedded                                                                                  | Obtain the languages in the channel numbers. For example, "channel 1 is French"                                                                                                                           |
