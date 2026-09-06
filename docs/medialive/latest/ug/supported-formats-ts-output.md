

# Captions formats supported in UDP, SRT, MediaConnect Router, or multiplex outputs
<a name="supported-formats-ts-output"></a>

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive in an MPEG-TS streaming output or in an MPTS multiplex output, when you have this input container and captions type. 



- **CDI container**
  - **Source caption input:** ARIB / **Supported output captions:** ARIB
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20
  - **Source caption input:** Teletext / **Supported output captions:** Burn-in<br />DVB-Sub<br />Teletext

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inDVB-Sub<br />

- **MP4 container**
  - **Source caption input:** Ancillary / **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded

- **RTMP container**
  - **Source caption input:** Embedded
  - **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded

- **MPEG-TS container (through MediaConnect or through the RTP or SRT protocols)**
  - **Source caption input:** ARIB / **Supported output captions:** ARIB
  - **Source caption input:** DVB-Sub / **Supported output captions:** Burn-in<br />DVB-Sub
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-in<br />DVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** SCTE-27 / **Supported output captions:** None
  - **Source caption input:** Teletext / **Supported output captions:** Burn-in<br />DVB-Sub<br />Teletext

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Teletext / **Supported output captions:** Burn-in<br />DVB-Sub<br />Teletext<br />

- **All input containers(Smart Subtitles generates subtitles from the source audio, not from captions in the source.)**
  - **Source caption input:** Smart Subtitles
  - **Supported output captions:** None

