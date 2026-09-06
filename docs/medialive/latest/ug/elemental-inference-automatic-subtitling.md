

# Smart Subtitles using Elemental Inference
<a name="elemental-inference-automatic-subtitling"></a>

In an AWS Elemental MediaLive channel, you can enable the Smart Subtitles feature to automatically generate subtitles from the audio in your source media. This feature uses AWS Elemental Inference smart subtitles, which applies automatic speech recognition (ASR) to transcribe audio into timed subtitle text.

Smart Subtitles generates subtitles in TTML or WebVTT format. Use TTML for MediaPackage V2, CMAF Ingest, and Microsoft Smooth output groups. Use WebVTT for HLS and MediaPackage output groups.

**Topics**
+ [Get ready](automatic-subtitling-get-ready.md)
+ [Setting up Smart Subtitles (console)](automatic-subtitling-setup-console.md)
+ [Disabling Smart Subtitles](automatic-subtitling-disable.md)