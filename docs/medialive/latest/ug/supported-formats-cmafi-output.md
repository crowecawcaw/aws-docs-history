

# Captions formats supported in CMAF Ingest outputs
<a name="supported-formats-cmafi-output"></a>

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive when you have this input container and captions type, and produce these outputs:
+ CMAF Ingest output
+ MediaPackage output with a CMAF Ingest container

**Note**  
You can also produce subtitles without a caption source in your input. Enable the Smart Subtitles feature, which uses AWS Elemental Inference to generate TTML or WebVTT subtitles from the audio. For more information, see [Smart Subtitles using Elemental Inference](elemental-inference-automatic-subtitling.md).



- **CDI container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-in<br />TTML<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** TTML<br />WebVTT

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inTTML<br />WebVTT
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-in<br />TTML<br />WebVTT

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inTTML<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inTTML<br />WebVTT

- **MP4 container**
  - **Source caption input:** Ancillary / **Supported output captions:** Burn-inTTML<br />WebVTT
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inTTML<br />WebVTT

- **RTMP container**
  - **Source caption input:** Embedded
  - **Supported output captions:** Burn-inTTML<br />WebVTT

- **MPEG-TS container (through MediaConnect or through the RTP or SRT protocols)**
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inTTML<br />WebVTT
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inTTML<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inTTML<br />WebVTT

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inTTML<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inTTML<br />WebVTT

- **All input containers(Smart Subtitles generates subtitles from the source audio, not from captions in the source.)**
  - **Source caption input:** Smart Subtitles
  - **Supported output captions:** TTML<br />WebVTT

