# Supported content

With SMPTE 2022-6, the video, audio, and ancillary data are muxed
into one feed. Compare this design to SMPTE 2110, where the content is
each in a separate essence.

The following table describes the content that Elemental Live
supports in SMPTE 2022-6 inputs.

| Type                                                               | Details                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Video                                                              | UncompressedResolutions –<br>SD<br>and<br>HDScan<br>types – Progressive and interlacedSampling<br>– 4:2:2Bit format – 10-bit                                                                                                                                                                                                                                                                          |
| Audio                                                              | PCM audioUncompressed Sample rates:<br>44.1kHz and 48.0 kHz                                                                                                                                                                                                                                                                                                                                           |
| Dolby Digital (AC3)Coding modes – 1.0, 1+1, 2.0,<br>3.2 (with LFE) |
| Dolby Digital Plus (EAC3)Coding modes – 1.0, 2.0,<br>3.2           |
| Ancillary data – Captions (optional)                               | EIA-608 embedded captionsCEA-708 embedded<br>captionsTeletext as OP42 teletext format.<br>SMPTE 2031 field is unchecked in<br>source.Teletext as OP47 teletext format<br>wrapped in a SMPTE-2031 envelope. SMPTE 2031 field is<br>checked in source. Teletext as OP47<br>teletext format, also known as SMPTE RDD-08 (compliant<br>with ITU-R BT.1120-7). SMPTE 2031 field is unchecked in<br>source. |
| Ancillary data – Ad avail messages (optional)                      | SCTE 104 messages. Elemental Live will automatically convert<br>these messages to SCTE 35 messages during ingest.                                                                                                                                                                                                                                                                                     |
