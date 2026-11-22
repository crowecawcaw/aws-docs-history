

# Captions formats supported in HLS or MediaPackage outputs

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive when you have this input container and captions type, and produce these outputs:
+ HLS output 
+ MediaPackage output with an HLS container

**Note**  
You can also produce subtitles without a caption source in your input. Enable the Smart Subtitles feature, which uses AWS Elemental Inference to generate WebVTT subtitles from the audio. MediaLive can also encode those subtitles as embedded CEA-608 or CEA-708 captions. For more information, see [Smart Subtitles using Elemental Inference](elemental-inference-automatic-subtitling.md) and [Embedded captions encoding](captions-embedded-encoder.md).



- **CDI container**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Embedded<br />Teletext

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** WebVTT / **Supported output captions:** Embedded<br />WebVTT<br />(HLS outputs only. Not supported in MediaPackage outputs. Embedded captions require an HLS output with TS segments. Neither format is supported in an HLS output with fMP4 segments.)

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />WebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-in<br />Embedded<br />WebVTT

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
  - **Source caption input:** Teletext / **Supported output captions:** Burn-in<br />Embedded<br />WebVTT

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inWebVTT
  - **Source caption input:** Teletext / **Supported output captions:** Burn-in<br />Embedded<br />WebVTT

- **All input containers(Smart Subtitles generates subtitles from the source audio, not from captions in the source.)**
  - **Source caption input:** Smart Subtitles
  - **Supported output captions:** Burn-in<br />Embedded<br />WebVTT

