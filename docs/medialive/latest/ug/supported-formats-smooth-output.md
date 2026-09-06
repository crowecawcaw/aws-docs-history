

# Captions formats supported in Microsoft Smooth outputs
<a name="supported-formats-smooth-output"></a>

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive in a Microsoft Smooth output, when you have this input container and captions type. 

**Note**  
You can also produce subtitles without a caption source in your input. Enable the Smart Subtitles feature, which uses AWS Elemental Inference to generate TTML subtitles from the audio. For more information, see [Smart Subtitles using Elemental Inference](elemental-inference-automatic-subtitling.md).



- **CDI container**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEBU-TT<br />SMPTE-TT<br />TTML
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inEBU-TT<br />SMPTE-TT<br />TTML

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inSMPTE-TT<br />TTML

- **MP4 container**
  - **Source caption input:** Ancillary / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML

- **RTMP container**
  - **Source caption input:** Embedded
  - **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML

- **MPEG-TS container (through MediaConnect or through the RTP or SRT protocols)**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** DVB-Sub / **Supported output captions:** SMPTE-TT
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML
  - **Source caption input:** SCTE-27 / **Supported output captions:** Burn-in<br />SMPTE-TT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inEBU-TT-D<br />SMPTE-TT<br />TTML

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inSMPTE-TT<br />TTML
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inSMPTE-TT<br />WebVTT

- **All input containers(Smart Subtitles generates subtitles from the source audio, not from captions in the source.)**
  - **Source caption input:** Smart Subtitles
  - **Supported output captions:** TTML

