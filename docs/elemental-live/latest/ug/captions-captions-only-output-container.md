# Supported source

captions and output captions in a captions-only output container

This table describes the caption formats that can be included on their
own in an output. With this option, _the container is always a raw
container that contains only the captions_ (video would be in
another container that may be a raw container or may be some other
type).

If you have one of the source caption formats listed in the first
column – regardless of the source container – you can convert it to an
external captions file and include it in a raw container that contains only
that captions file.

| Source input container | Source caption format                            | Supported output captions                   |
| ---------------------- | ------------------------------------------------ | ------------------------------------------- | ---------------- | ------------------------------------------------ |
| Any container          | SRT                                              | SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT |
| SMI                    | SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT      |                                             | TTML             | SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT      |
| SMPTE-TT               | SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT      |                                             | STL              | SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT      |
| Embedded               | SCC, SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT |                                             | SCC              | SCC, SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT |
| SCTE-20                | SCC, SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT |                                             | SCTE-20+Embedded | SCC, SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT |
| Embedded+SCTE-20       | SCC, SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT |                                             | Ancillary Data   | SCC, SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT |
| Teletext               | SMI, SMPTE-TT, SRT, TTML, EBU-TT-D, Web-VTT      |                                             | DVBSub           | SMPTE-TT                                         |
| SCTE-27                | SMPTE-TT                                         |
