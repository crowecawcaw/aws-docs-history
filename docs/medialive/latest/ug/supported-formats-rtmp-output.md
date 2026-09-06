

# Captions formats supported in RTMP outputs
<a name="supported-formats-rtmp-output"></a>

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive in an RTMP output, when you have this input container and captions type. 



- **CDI container**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbeddedRTMP CaptionInfo
  - **Source caption input:** Teletext / **Supported output captions:** None

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** SCTE-20 / **Supported output captions:** Embedded

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** Teletext / **Supported output captions:** None

- **MP4 container**
  - **Source caption input:** Ancillary / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo

- **RTMP container**
  - **Source caption input:** Embedded
  - **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo

- **MPEG-TS container (through MediaConnect or through the RTP or SRT protocols)**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** DVB-Sub / **Supported output captions:** Burn-in
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** SCTE-20 / **Supported output captions:** EmbeddedRTMP CaptionInfo
  - **Source caption input:** SCTE-27 / **Supported output captions:** Burn-in
  - **Source caption input:** Teletext / **Supported output captions:** None

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inRTMP CaptionInfo<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Teletext / **Supported output captions:** None

- **All input containers(Smart Subtitles generates subtitles from the source audio, not from captions in the source.)**
  - **Source caption input:** Smart Subtitles
  - **Supported output captions:** None

