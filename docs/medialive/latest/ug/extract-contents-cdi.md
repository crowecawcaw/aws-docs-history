# Identifying content in a CDI source

The content in a CDI source always consists of uncompressed video, uncompressed audio, and
captions.

Obtain identifying information from the content provider.

| Asset    | Description                                                                                           | Information to obtain                                                                    |
| -------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Video    | You don't need identifying information. MediaLive always extracts the first video that it encounters. | None                                                                                     |
| Audio    | The source might include multiple audio tracks, typically one for each language.                      | Obtain the numbers and languages of the tracks. For example, "track 1 is French".        |
| Captions | ARIB                                                                                                  | You don't need any information. With ARIB captions, MediaLiveextracts all the languages. |
| Embedded | Obtain the languages in the channel numbers. For example, "channel 1 is French".                      |                                                                                          | Teletext | [If your plan for teletext captions](assess-uss-captions.md "assess-uss-captions.md") is to convert the captions to a different format, you must obtain the page numbers for the languages that you want to convert. If you plan to pass through the captions as Teletext in the output, you don't need any identifiers. |
