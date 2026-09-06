

# Captions formats supported in HLS or MediaPackage outputs
<a name="supported-formats-hls-output"></a>

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive when you have this input container and captions type, and produce these outputs:
+ HLS output 
+ MediaPackage output with an HLS container

**Note**  
You can also produce subtitles without a caption source in your input. Enable the Smart Subtitles feature, which uses AWS Elemental Inference to generate subtitles from the audio. For more information, see [Smart Subtitles using Elemental Inference](elemental-inference-automatic-subtitling.md).



- **CDI container**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Teletext

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />WebVTT

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inWebVTT

- **MP4 container**
  - **Source caption input:** Ancillary / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />WebVTT

- **RTMP container**
  - **Source caption input:** Embedded
  - **Supported output captions:** Burn-inEmbedded<br />WebVTT

- **MPEG-TS container (through MediaConnect or through the RTP or SRT protocols)**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** DVB-Sub / **Supported output captions:** Burn-inWebVTT
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** SCTE-27 / **Supported output captions:** Burn-inWebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inWebVTT

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inWebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-inWebVTT

- **All input containers(Smart Subtitles generates subtitles from the source audio, not from captions in the source.)**
  - **Source caption input:** Smart Subtitles
  - **Supported output captions:** WebVTT

