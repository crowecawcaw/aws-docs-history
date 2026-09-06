

# Supported caption formats
<a name="captions-supported-formats"></a>

<a name="table-captions-supported-formats"></a>

- **Ancillary data**
  - **Supported in input:** √
  - **Supported in output:**  
  - **Description:**  +  From MXF input, data that is compliant with “SMPTE 291M: Ancillary Data Package and Space Formatting” and that is contained in ancillary data. <br />+  From QuickTime input or for QuickTime output, data that is compliant with EIA-608 (also known as CEA-608) or CEA-708 (also known as EIA-708) and that is contained in ancillary data.  

- **Ancillary\+Embedded**
  - **Supported in input:**  
  - **Supported in output:** √
  - **Description:** For QuickTime output only, the output combines captions in ancillary data and embedded captions. The ancillary captions are compliant with EIA-608 (also known as CEA-608) or CEA-708 (also known as EIA-708). The embedded captions are described later in this table.

- **ARIB **
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Captions that are compliant with the ARIB STD-B37 Version 2.4.

- **Burn-in**
  - **Supported in input:** N/A
  - **Supported in output:** √
  - **Description:** From input: It is technically impossible for Elemental Live to read burn-in captions. Therefore, from an input viewpoint, they cannot be considered to be captions.<br />For output: Burn-in captions are captions that are converted into text and then overlaid on top of the picture directly in the video stream.

- **DVB-Sub**
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Captions that are compliant with ETSI EN 300 743.

- **EBU-TT-D**
  - **Supported in input:**  
  - **Supported in output:** √
  - **Description:** Captions that are compliant with EBU Tech 3380, EBU-TT-D Subtitling Distribution Format, 2018.

- **Embedded**
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Captions that are compliant with the EIA-608 standard (also known as CEA-608 or SMPTE-259M or “line 21 captions”) or the CEA-708 standard (also known as EIA-708).

- **Embedded\+SCTE-20**
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Captions that have both embedded and SCTE-20 in the video. The embedded captions are inserted before the SCTE-20 captions. 

- **RTMP CaptionInfo**
  - **Supported in input:**  
  - **Supported in output:** √
  - **Description:** Captions that are compliant with the Adobe onCaptionInfo format.

- **RTMP CuePoint **
  - **Supported in input:**  
  - **Supported in output:** √
  - **Description:** Captions that are in the cuePoint format.

- **SCC**
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Captions that are in the Scenarist format, file extension .scc. 

- **SCTE-20**
  - **Supported in input:** √
  - **Supported in output:**  
  - **Description:** Captions that are compliant with the standard “SCTE 20 2012 Methods for Carriage of CEA-608 Closed Captions and Non-Real Time Sampled Video.”

- **SCTE-20\+Embedded**
  - **Supported in input:**  
  - **Supported in output:** √
  - **Description:** Captions that are compliant with SCTE-43. The SCTE-20 captions are inserted in the video before the Embedded captions.

- **SCTE-27**
  - **Supported in input:** √
  - **Supported in output:**  
  - **Description:** Captions that are compliant with the standard “SCTE-27 (2011), Subtitling Methods for Broadcast Cable.”

- **SMI**
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Captions in the Microsoft SAMI format.

- **SMPTE-TT**
  - **Supported in input:**  
  - **Supported in output:** √
  - **Description:** Captions that are compliant with the standard “SMPTE ST 2052-1:2010.”

- **SRT**
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Captions in the SRT format.

- **STL **
  - **Supported in input:** √
  - **Supported in output:**  
  - **Description:** Captions in the EBU STL format. Spruce STL format is not supported.

- **Teletext **
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:**
    - From SDI input. Captions in:+  OP42 teletext format. SMPTE 2031 field is unchecked in source. <br />+   OP47 teletext format wrapped in a SMPTE-2031 envelope. SMPTE 2031 field is checked in source.  <br />+  OP47 teletext format, also known as SMPTE RDD-08 (compliant with ITU-R BT.1120-7). SMPTE 2031 field is unchecked in source. <br />From TS input: Captions in the EBU Teletext format.<br />From MXF file input: OP47 teletext format, also known as SMPTE RDD-08 (compliant with ITU-R BT.1120-7). SMPTE 2031 field is unchecked in source. 
    - For output: Captions in the EBU Teletext format.

- **TTML**
  - **Supported in input:** √
  - **Supported in output:** √
  - **Description:** Caption files that are compliant with the standard “Timed Text Markup Language 1 (TTML1) (Second Edition).”

- **WebVTT**
  - **Supported in input:**  
  - **Supported in output:** √
  - **Description:** Captions that are compliant with “webvtt: The Web Video Text Tracks Format” ([http://dev.w3.org/html5/webvtt/](https://dev.w3.org/html5/webvtt/)).

