

# Smart Subtitles using Elemental Inference
<a name="elemental-inference-automatic-subtitling"></a>

In an AWS Elemental MediaLive channel, you can enable the Smart Subtitles feature to automatically generate subtitles from the audio in your source media. This feature uses AWS Elemental Inference smart subtitles, which applies automatic speech recognition (ASR) to transcribe audio into timed subtitle text.

Smart Subtitles generates subtitles as TTML or WebVTT sidecar captions, or burns them into the video. Use TTML or WebVTT for MediaPackage V2 and CMAF Ingest output groups, TTML for Microsoft Smooth output groups, and WebVTT for HLS and MediaPackage output groups. You can burn subtitles into the video in any output group that supports burn-in captions.

**Topics**
+ [Get ready](automatic-subtitling-get-ready.md)
+ [Setting up Smart Subtitles (console)](automatic-subtitling-setup-console.md)
+ [Disabling Smart Subtitles](automatic-subtitling-disable.md)