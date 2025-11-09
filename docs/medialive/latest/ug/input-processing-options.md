# Supported features by input type

SCTE 35 messages can appear only in the following types of MediaLive inputs:

- Elemental Link inputs
- HLS inputs
- MediaConnect inputs
- RTP inputs
- SMPTE 2110 inputs (SCTE 104 messages that are automatically converted to
  SCTE 35 messages)
- SRT Caller
- Transport Stream (TS) File inputs
- AWS CDI inputs
  The following table shows which inputs might include ad avail information and how
  MediaLive handles that information. To read the table, find an input in the first
  column, then read across in the row.

| Input                      | Interpret SCTE 35 messages in the<br>source<br>stream              | Interpret ad avail information in the input manifest |
| -------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------- |
| Elemental Link             | Yes                                                                | Not applicable                                       |
| HLS                        | Yes                                                                | Yes                                                  |
| MediaConnect               | Yes                                                                | Not applicable                                       |
| RTMP                       | No                                                                 | Not applicable                                       |
| RTP                        | Yes                                                                | Not applicable                                       |
| SMPTE 2110                 | Yes (interpret SCTE 104 messages in the ancillary data<br>packets) | Not applicable                                       |
| SRT Caller                 | Yes                                                                | No applicable                                        |
| Transport Stream (TS) file | Yes                                                                | Not applicable                                       |
| AWS CDI                    | Yes                                                                | Not applicable                                       |
