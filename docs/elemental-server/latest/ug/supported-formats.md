This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Reference: Supported Captions Formats

The following lists show supported input and output captions types. The table at the end of
this topic provides definitions for each of these captions types.

###### Note

Support for an input format and support for an output format doesn't mean that
AWS Elemental Server supports _conversion from_ a particular input
format to a particular output format. For that information, see the
**Reference** tab of the documentation on the web interface of your
appliance. To go to the documentation, choose the **Support** tab at the top of the
interface.

###### Supported Input Caption Formats

- Ancillary data
- ARIB
- DVB-Sub
- Embedded
- Embedded+SCTE-20
- SCC
- SCTE-20
- SCTE-27
- SMI
- SRT
- STL

###### Supported Output Caption Formats

- Ancillary+Embedded
- ARIB
- Burn-in
- CFF-TT
- DVB-Sub
- Embedded
- Embedded+SCTE-20
- RTMP CaptionInfo
- RTMP CuePoint
- SCC
- SCTE-20+Embedded
- SMI
- SRT
- Teletext
- TTML
- WebVTT

| Caption Format Descriptions | Caption                                                                                                                                                                                                                                                                                                                                 | Description |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Ancillary data              | From MXF input, data that is compliant with “SMPTE 291M: Ancillary Data Package and<br>Space Formatting” and is contained in ancillary data.<br>From QuickTime® input or for QuickTime output, data that is compliant with EIA-608<br>(also known as CEA-608) or CEA-708 (also known as EIA-708) and is contained in ancillary<br>data. |
| Ancillary+Embedded          | For QuickTime output only, the output combines captions in ancillary data and embedded<br>captions. The ancillary captions are compliant with EIA-608 (also known as CEA-608) or<br>CEA-708 (also known as EIA-708). The embedded captions are described below.                                                                         |
| ARIB                        | Captions that are compliant with the ARIB STD-B37 Version 2.4                                                                                                                                                                                                                                                                           |
| Burn-in                     | It is technically impossible for the encoder to read burn-in captions. Therefore, from<br>an input viewpoint, they cannot be considered to be captions.<br>Burn-in captions are captions that are converted into text and then overlaid on top of<br>the picture directly in the video stream.                                          |
| CFF-TT                      | Captions for Ultraviolet output.                                                                                                                                                                                                                                                                                                        |
| DVB-Sub                     | Captions that are compliant with ETSI EN 300 743.                                                                                                                                                                                                                                                                                       |
| Embedded                    | Captions that are compliant with the EIA-608 standard (also known as CEA-608 or<br>SMPTE-259M or “line 21 captions”) or the CEA-708 standard (also known as EIA-708).                                                                                                                                                                   |
| Embedded+SCTE-20            | Captions that have both embedded and SCTE-20 in the video. The embedded captions are<br>inserted before the SCTE-20 captions.                                                                                                                                                                                                           |
| RTMP CaptionInfo            | Captions that are compliant with the Adobe onCaptionInfo format.                                                                                                                                                                                                                                                                        |
| RTMP CuePoint               | Captions that are in the cuePoint format.                                                                                                                                                                                                                                                                                               |
| SCC                         | Captions that are in the Scenarist format, file extension .scc.                                                                                                                                                                                                                                                                         |
| SCTE-20                     | Captions that are compliant with the standard “SCTE 20 2012 Methods for Carriage of<br>CEA-608 Closed Captions and Non-Real Time Sampled Video.”                                                                                                                                                                                        |
| SCTE-20+Embedded            | Captions that are compliant with SCTE-43. The SCTE-20 captions are inserted in the<br>video before the Embedded captions.                                                                                                                                                                                                               |
| SCTE-27                     | Captions that are compliant with the standard “SCTE-27 (2011), Subtitling Methods for<br>Broadcast Cable.”                                                                                                                                                                                                                              |
| SMI                         | Captions in the Microsoft SAMI format.                                                                                                                                                                                                                                                                                                  |
| SRT                         | Captions in the SRT format.                                                                                                                                                                                                                                                                                                             |
| STL                         | Captions in the EBU STL format. Spruce STL format is not supported.                                                                                                                                                                                                                                                                     |
| Teletext                    | From TS input: Captions in the EBU Teletext format.<br>From MXF file input: Captions in the EBU Teletext format.<br>For output: Captions in the EBU Teletext format.                                                                                                                                                                    |
| TTML                        | Caption files that are compliant with the standard “Timed Text Markup Language 1<br>(TTML1) (Second Edition).”                                                                                                                                                                                                                          |
| WebVTT                      | Captions that are compliant with “webvtt: The Web Video Text Tracks Format” as defined<br>by the W3C organization.                                                                                                                                                                                                                      |
