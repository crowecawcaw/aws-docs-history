

# IVS Release Notes \| Real-Time Streaming
<a name="release-notes"></a>

This document contains all Amazon IVS Real-Time Streaming release notes, latest first, organized by date of release.

## August 27, 2026
<a name="aug27-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.46.0, iOS 1.46.0 (Real-Time Streaming)
<a name="aug27-26-broadcast-mobile-rt-1460"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.46.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.46.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.46.0/android/)+  Fixed a rare crash that could occur when calling `leave()` on a stage while it is handling a fatal error. <br />+  Introduced `RealTimeConnection` APIs that create a persistent connection across multiple stages, reducing time to video when users transition between stages. <br />+  Fixed a rare crash that could occur if OpenSL ES audio playback failed to start correctly. <br />+  Fixed rare playback and recording issues on some device models when using STUDIO or SUBSCRIBE\_ONLY audio use case presets.  | 
| [iOS Broadcast SDK 1.46.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.46.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.46.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.46.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.46.0/ios/)+  Fixed a rare crash that could occur when calling `leave()` on a stage while it is handling a fatal error. <br />+  Introduced `IVSRealTimeConnection` APIs that create a persistent connection across multiple stages, reducing time to video when users transition between stages.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1460-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 6.089 MB | 14.784 MB | 
| armeabi-v7a | 5.277 MB | 10.235 MB | 
| x86\_64 | 6.206 MB | 15.378 MB | 
| x86 | 6.481 MB | 16.010 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1460-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 4.085 MB | 8.297 MB | 

## August 27, 2026
<a name="aug27-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.39.0 (Real-Time Streaming)
<a name="aug27-26-broadcast-web-rt-1390"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.39.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed an issue where Firefox users could not reconnect to a stage after being offline for an extended period. <br />+  Fixed a [RangeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError) that causes publishing to fail on Chrome 152\+ when simulcast was enabled.  | 

## August 19, 2026
<a name="aug19-26-connection-reuse-rt"></a>

### Connection Reuse Across Stages
<a name="aug19-26-connection-reuse-rt-desc"></a>

You can now reuse a single connection across multiple stages, reducing time to video when users transition between stages. Use the new `RealTimeConnection` feature to establish the network connection once and share it across stage joins, eliminating repeated connection setup. This is useful for applications where users browse a feed of live streams and quickly move from one to the next. See [Reducing Time to Video When Switching Between Stages](real-time-streaming-optimization.md#real-time-streaming-stage-switching).

## August 19, 2026
<a name="aug19-26-broadcast-android-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.43.2 (Real-Time Streaming)
<a name="aug19-26-broadcast-android-rt-1432"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.43.2](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.43.2/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.43.2/android/)+  Fixed an issue that could cause audio to fail to play on some Pixel devices.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1432-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 6.041 MB | 14.669 MB | 
| armeabi-v7a | 5.234 MB | 10.164 MB | 
| x86\_64 | 6.151 MB | 15.250 MB | 
| x86 | 6.427 MB | 15.875 MB | 

## August 12, 2026
<a name="aug12-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.38.1 (Real-Time Streaming)
<a name="aug12-26-broadcast-web-rt-1381"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.38.1](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed `PUBLISH_ERROR` (code 1015) caused [by a Simulcast regression in Chrome 152\+ for publishers](https://issues.webrtc.org/issues/545191307) with simulcast enabled and [two or fewer layers configured](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/web-publish-subscribe.html#web-publish-subscribe-layered-encoding-simulcast).  | 

## August 11, 2026
<a name="aug11-26-broadcast-android-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.43.1 (Real-Time Streaming)
<a name="aug11-26-broadcast-android-rt-1431"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.43.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.43.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.43.1/android/)+  Fixed a rare crash that could occur if OpenSL ES audio playback failed to start correctly. <br />+  Fixed an issue that could cause audio to play at reduced volume on some Samsung devices.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1431-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 6.041 MB | 14.669 MB | 
| armeabi-v7a | 5.234 MB | 10.164 MB | 
| x86\_64 | 6.151 MB | 15.250 MB | 
| x86 | 6.427 MB | 15.875 MB | 

## July 30, 2026
<a name="jul30-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.45.0, iOS 1.45.0 (Real-Time Streaming)
<a name="jul30-26-broadcast-mobile-rt-1450"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.45.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.45.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.45.0/android/)+  Fixed an issue where subscribers could see a frozen video stream after recovering from network degradation. <br />+  Fixed a rare crash related to `CustomImageSource` usage in stages. <br />+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.45.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.45.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.45.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.45.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.45.0/ios/)+  Fixed an issue where subscribers could see a frozen video stream after recovering from network degradation. <br />+  Bug fixes and stability improvements. <br />+  Support for iOS 14 will be deprecated as of IVS Broadcast SDK 1.48.0.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1450-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 6.071 MB | 14.716 MB | 
| armeabi-v7a | 5.260 MB | 10.188 MB | 
| x86\_64 | 6.186 MB | 15.307 MB | 
| x86 | 6.459 MB | 15.940 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1450-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 4.077 MB | 8.281 MB | 

## July 30, 2026
<a name="jul30-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.38.0 (Real-Time Streaming)
<a name="jul30-26-broadcast-web-rt-1370"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.38.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed edge case where audio would be dropped in stage composition due to temporary publisher network failure.  | 

## July 7, 2026
<a name="jul07-26-broadcast-ios-rt"></a>

### Amazon IVS Broadcast SDK: iOS 1.44.1 (Real-Time Streaming)
<a name="jul07-26-broadcast-ios-rt-1441"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [iOS Broadcast SDK 1.44.1](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.44.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.44.1/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.44.1/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.44.1/ios/)+  Fixed a rare deadlock when leaving and deallocating an `IVSStage`.  | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1441-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 4.073 MB | 8.281 MB | 

## July 2, 2026
<a name="jul02-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.44.0, iOS 1.44.0 (Real-Time Streaming)
<a name="jul02-26-broadcast-mobile-rt-1440"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.44.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.44.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.44.0/android/)+  Improved network utilization during publish and subscribe operations. <br />+  Improved recovery performance for subscribers after network degradation.  | 
| [iOS Broadcast SDK 1.44.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.44.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.44.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.44.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.44.0/ios/)+  Improved network utilization during publish and subscribe operations. <br />+  Improved recovery performance for subscribers after network degradation.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1440-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 6.061 | 14.699 | 
| armeabi-v7a | 5.250 | 10.175 | 
| x86\_64 | 6.176 | 15.289 | 
| x86 | 6.452 | 15.922 | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1440-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 4.072 | 8.264 | 

## July 2, 2026
<a name="jul02-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.37.0 (Real-Time Streaming)
<a name="jul02-26-broadcast-web-rt-1370"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.37.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Bug fixes and stability improvements.  | 

## June 4, 2026
<a name="jun04-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.43.0, iOS 1.43.0 (Real-Time Streaming)
<a name="jun04-26-broadcast-mobile-rt-1430"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.43.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.43.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.43.0/android/)+  The callback provided to the Stage.setAudioCallback API added in 1.42.0 will now be persisted across leave/join cycles, where previously it was cleared on leave.  <br />+  Fixed a rare crash when tearing down the last Stage that was publishing with the device's microphone.  | 
| [iOS Broadcast SDK 1.43.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.43.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.43.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.43.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.43.0/ios/)+  The callback provided to the IVSStage.setAudioCallback API added in 1.42.0 will now be persisted across leave/join cycles, where previously it was cleared on leave. <br />+  Fixed a bug where the camera torch may turn back on unintentionally after changing cameras and rotating the device.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1430-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 6.040 MB | 14.665 MB | 
| armeabi-v7a | 5.232 MB | 10.161 MB | 
| x86\_64 | 6.149 MB | 15.246 MB | 
| x86 | 6.425 MB | 15.870 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1430-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 4.078 MB | 8.281 MB | 

## June 4, 2026
<a name="jun04-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.36.0 (Real-Time Streaming)
<a name="jun04-26-broadcast-web-rt-1360"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.36.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Bug fixes and performance improvements.  | 

## May 7, 2026
<a name="may07-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.42.0, iOS 1.42.0 (Real-Time Streaming)
<a name="may07-26-broadcast-mobile-rt-1420"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.42.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.42.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.42.0/android/)+  Added `Stage.setAudioCallback` for receiving mixed PCM audio data from all remote participants. Must be called before `join()`; automatically cleared on `leave()`. <br />+  Bug fixes and performance improvements.  | 
| [iOS Broadcast SDK 1.42.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.42.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.42.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.42.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.42.0/ios/)+  Added `IVSSStage.setAudioCallback` for receiving mixed PCM audio data from all remote participants. Must be called before `join`; automatically cleared on `leave`. <br />+  Bug fixes and performance improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1420-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.853 MB | 14.194 MB | 
| armeabi-v7a | 5.078 MB | 9.840 MB | 
| x86\_64 | 5.967 MB | 14.758 MB | 
| x86 | 6.220 MB | 15.318 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1420-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.888 MB | 7.935 MB | 

## May 7, 2026
<a name="may07-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.35.0 (Real-Time Streaming)
<a name="may07-26-broadcast-web-rt-1350"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.35.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Bug fixes and performance improvements.  | 

## April 16, 2026
<a name="apr16-26-token-exchange-ssc"></a>

### Web Broadcast SDK Token Exchange
<a name="apr16-26-token-exchange-ssc-desc"></a>

Server-side composition layouts now update dynamically after token exchange. If your layout uses attributes such as `featuredParticipantAttribute` or `participantOrderAttribute`, changes made as part of a token exchange will immediately update the active composition without requiring the participant to reconnect. 

In addition, token exchange is now supported in the web broadcast SDK, implemented through the `exchangeToken` method added in [Web Broadcast SDK 1.33.0](#mar12-26-broadcast-web-rt).

## April 9, 2026
<a name="apr09-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.34.0 (Real-Time Streaming)
<a name="apr09-26-broadcast-web-rt-1340"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.34.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed a bug where subscribe or publish attempts immediately following `exchangeToken` invocations could fail. <br />+  Added additional information in the details property for `TOKEN_EXCHANGE_FAILED` errors.  | 

## April 9, 2026
<a name="apr09-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.41.0, iOS 1.41.0 (Real-Time Streaming)
<a name="apr09-26-broadcast-mobile-rt-1410"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.41.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.41.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.41.0/android/)+  Added ability to choose between platform-native echo cancellation, AECM, or AEC3 algorithms with automatic fallback support. <br />+  Added ability to choose between platform-native or software-based noise suppression with automatic fallback support. <br />+  **Important:** If you use `StageAudioConfiguration.enableNoiseSuppression`, you must now call `StageAudioManager.enableNoiseSuppression` instead. Noise suppression is now managed globally rather than per-stream.  <br />+  Software noise suppression is now disabled by default for `STUDIO` and `SUBSCRIBE_ONLY` audio mode presets to align with iOS.   | 
| [iOS Broadcast SDK 1.41.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.41.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.41.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.41.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.41.0/ios/)+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1410-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.834 MB | 14.157 MB | 
| armeabi-v7a | 5.056 MB | 9.812 MB | 
| x86\_64 | 5.945 MB | 14.721 MB | 
| x86 | 6.200 MB | 15.285 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1410-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.927 MB | 7.980 MB | 

## April 8, 2026
<a name="apr8-26-redundant-ingest"></a>

### Redundant Ingest 24/7 Streaming
<a name="apr8-26-redundant-ingest"></a>

Redundant ingest is now available for RTMP(S) and E-RTMP(S) streams. This feature enables streaming from two encoders simultaneously to a single stage, with automated failover for the same source media. Redundant ingest is ideal for live events, 24/7 live streams, or any scenario where uninterrupted delivery is essential. By streaming from two encoders, you can protect against unexpected disruptions while also enabling continuous 24/7 streaming. For more information, see:
+ User Guide — We added [Redundant Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html#redundant-ingest) in *IVS RTMP Publishing*.
+ [Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html) — Changes are described in the “API Reference” table of the [Document History](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/doc-history.html#history-real-time-api-reference).

## March 12, 2026
<a name="mar12-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.33.0 (Real-Time Streaming)
<a name="mar12-26-broadcast-web-rt-1330"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.33.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Implemented the `exchangeToken` method for real-time token exchange.  <br />+  Implemented the STAGE\_PARTICIPANT\_METADATA\_CHANGED event, which fires when `attributes` and/or `userId` change(s) after token exchanges. <br />+  Added the `encoderImplementation` field on the request local stage stream `requestQualityStats()` method.  | 

## March 12, 2026
<a name="mar12-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.40.0, iOS 1.40.0 (Real-Time Streaming)
<a name="mar12-26-broadcast-mobile-rt-1400"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.40.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.40.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.40.0/android/)+  Improved error messages around TLS certificate validation failures and expanded error enum codes.  | 
| [iOS Broadcast SDK 1.40.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.40.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.40.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.40.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.40.0/ios/)+  Improved error messages around TLS certificate validation failures and expanded error enum codes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1400-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.823 MB | 14.139 MB | 
| armeabi-v7a | 5.046 MB | 9.798 MB | 
| x86\_64 | 5.935 MB | 14.702 MB | 
| x86 | 6.190 MB | 15.265 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1400-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.939 MB | 8.013 MB | 

## February 13, 2026
<a name="feb13-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.39.0, iOS 1.39.0 (Real-Time Streaming)
<a name="feb13-26-broadcast-mobile-rt-1390"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.39.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.39.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.39.0/android/)+  Minor bug fixes for Bluetooth headset reconnects using the STUDIO audio mode.  <br />+  Updated core Android build tools and NDK version. <br />+  Fixed rare deadlock when stopping a `MixedImageDevice`.   | 
| [iOS Broadcast SDK 1.39.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.39.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.39.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.39.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.39.0/ios/)+  Updated Xcode to version 26.2. <br />+  Effective with this release, the IVS SDKs are no longer distributed via CocoaPods. <br />CocoaPods announced its deprecation in 2024 and will enter read-only state later this year. Swift Package Manager (SPM) replaces CocoaPods as Apple’s supported dependency-management solution and is the standard way to integrate SDKs in modern Xcode projects. <br />We recommend that you migrate to SPM or integrate the IVS SDK frameworks directly into your project. IVS SDKs are fully supported via both approaches. <br />Related documentation changes were made in:   [Getting Started with IVS Real-Time Streaming](getting-started-broadcast-sdk.md#getting-started-broadcast-sdk-ios) – "Step 4: Integrate the IVS Broadcast SDK" > "iOS"   [iOS Broadcast SDK Guide](broadcast-ios-getting-started.md#broadcast-ios-install) – "Install the Library"    | 

#### Broadcast SDK Size: Android
<a name="broadcast-1390-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.788 MB | 14.059 MB | 
| armeabi-v7a | 5.016 MB | 9.740 MB | 
| x86\_64 | 5.898 MB | 14.615 MB | 
| x86 | 6.154 MB | 15.184 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1390-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.932 MB | 7.996 MB | 

## February 12, 2026
<a name="feb12-26-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.32.0 (Real-Time Streaming)
<a name="feb12-26-broadcast-web-rt-1320"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.32.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Bug fixes and stability improvements.  | 

## January 13, 2026
<a name="jan13-26-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.38.0, iOS 1.38.0 (Real-Time Streaming)
<a name="jan13-26-broadcast-mobile-rt-1380"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.38.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/android/)+  Layer prioritization function — Added `Priority` enum to `StageVideoConfiguration.Layer` with values: `VERY_LOW`, `LOW`, `MEDIUM`, `HIGH`. This will determine which layer is dropped first under network bandwidth constraints. <br />+  Faster stage reconnection after network connectivity is restored. <br />+  Changed the codes associated with some errors. See [Mobile Broadcast SDK Error Migration Guide](#broadcast-1380-rt-sdk-error-migration) below.  | 
| [iOS Broadcast SDK 1.38.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/ios/)+  Layer prioritization function — Added `IVSLocalStageStreamLayerPriority` enum with values: `VeryLow`, `Low`, `Medium`, `High`. This will determine which layer is dropped first under network bandwidth constraints. <br />+  Faster stage reconnection after network connectivity is restored. <br />+  Changed the codes associated with some errors. See [Mobile Broadcast SDK Error Migration Guide](#broadcast-1380-rt-sdk-error-migration) below.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1380-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.795 MB | 14.070 MB | 
| armeabi-v7a | 5.021 MB | 9.746 MB | 
| x86\_64 | 5.904 MB | 14.630 MB | 
| x86 | 6.161 MB | 15.198 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1380-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.609 MB | 8.078 MB | 

#### Mobile Broadcast SDK Error Migration Guide
<a name="broadcast-1380-rt-sdk-error-migration"></a>

In version 1.38.0 of the iOS and Android broadcast SDKs, the codes associated with some errors have changed. Previously, there was no single property that could be used to uniquely identify any error emitted from the SDKs. Instead, to understand what an error meant, a combination of the following properties needed to be examined: 


| Android | iOS | 
| --- | --- | 
| `BroadcastException.getCode()`<br />`BroadcastException.getUid()`<br />`BroadcastException.getError()`<br />`BroadcastException.getSource()`<br />`BroadcastException.getDetail()` | `NSError.code`<br />`NSError.userInfo[IVSBroadcastUidDescriptionErrorKey]`<br />`NSError.userInfo[IVSBroadcastResultDescriptionErrorKey]`<br />`NSError.userInfo[IVSBroadcastSourceDescriptionErrorKey]`<br />`NSError.userInfo[NSLocalizedDescriptionKey]` | 

With version 1.38.0 and greater, `BroadcastException.getCode()` (Android) and `NSError.code` (iOS) return a unique ID that can be looked up in the public `BroadcastErrorCode` (Android) and `IVSBroadcastErrorCode` (iOS) enums. 

In addition to making `code` the unique ID for all errors, an additional field was added: `BroadcastException.getPlatformCode()` (Android) and `NSError.userInfo[IVSBroadcastPlatformCodeDescriptionErrorKey]` (iOS). If an error is caused by the underlying platform (such as a network error or a video encode or decode error), this field is non-zero and can be used to collect additional information from the platform’s documentation.

##### Migrating from SDK 1.37.0 and Earlier
<a name="broadcast-1380-rt-sdk-error-migration-from-earlier"></a>

To make every error conform to the new strategy, some existing errors had to change their values. Below is a guide to map existing logic to the new logic:
+ Any error where `code` was non-zero will keep the same value for code; however, referencing the code through the new enum constants may improve clarity. For example, comparing an error to `BroadcastErrorCode.Broadcast.LatencyThresholdReached` is clearer than comparing it to `20401`. 
+ Any error where `UID` had a value (i.e. was not `-1` on Android or `"-1"` on iOS) will now have the `code` field set to what the existing `UID` value was. If you have conditionals comparing the `UID` field, you can keep the constants but compare them against the `code` field going forward.
+ Some legacy errors did not contain a `code` or a `UID` value. These were commonly matched based on the `message` (Android) or `description` (iOS) of the error, which is not a reliable way to identify errors because of the dynamic nature of error messages. Because these errors didn’t have uniquely identifying characteristics, one-to-one mappings can’t be provided. However, most errors kept the same description, so it is possible to continue using the same matching logic while also gathering and reporting the new `code` value for future app releases. 

As a concrete example, the error checking in the following table should be migrated as follows:


| Before | After | 
| --- | --- | 
| `error.code == 20401` | `error.code == BroadcastErrorCode.Broadcast.LatencyThresholdReached`<br />No change, but prefer comparison to the enum value. | 
| `error.uid == 207` | `error.code == BroadcastErrorCode.Net.SocketRemoteHangup`<br />Compare to `code` instead of `uid`. | 
| `error.message.contains("IceConnectionFailed")` | `error.code == BroadcastErrorCode.RealTime.PeerConnectionIceConnectionFailed`<br />Don’t compare to `message` (or `source`, or `result/detail`). Instead, find the appropriate enum code to compare to. | 

The most important part of an error is still `BroadcastException.getPlatformCode()` (Android) and `NSError.userInfo[IVSBroadcastPlatformCodeDescriptionErrorKey]` (iOS), but in version 1.38.0 and beyond, the `code` field uniquely identifies errors and allows immediate lookup of the error name and description in the `BroadcastErrorCode` (Android) and `IVSBroadcastErrorCode` (iOS) enums. As a result, other fields like `UID`, `source`, and `detail` should not be used in lookup logic; they exist only as supplemental information. 

## December 11, 2025
<a name="dec11-25-broadcast-android-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.37.1 (Real-Time Streaming)
<a name="dec11-25-broadcast-android-rt-1371"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.37.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.37.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.37.1/android/)+  Fixed issues related to participant preview teardown.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1371-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.754 MB | 13.965 MB | 
| armeabi-v7a | 4.991 MB | 9.683 MB | 
| x86\_64 | 5.858 MB | 14.529 MB | 
| x86 | 6.128 MB | 15.120 MB | 

## December 9, 2025
<a name="dec09-25-participant-token-exchange"></a>

### Participant Token Exchange
<a name="dec09-25-participant-token-exchange-desc"></a>

New support for participant token exchange enables you to upgrade or downgrade token capabilities and update token attributes within the IVS client SDK without forcing clients to disconnect and reconnect. This is useful for scenarios like co-hosting, where participants may start with subscribe-only capabilities and later need publish capabilities. 

See the new page on [Token Exchange](broadcast-mobile-token-exchange.md).

## December 5, 2025
<a name="dec05-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.31.0 (Real-Time Streaming)
<a name="dec05-25-broadcast-web-rt-1310"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.31.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Bug fixes and stability improvements.  | 

## December 5, 2025
<a name="dec05-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.37.0, iOS 1.37.0 (Real-Time Streaming)
<a name="dec05-25-broadcast-mobile-rt-1370"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.37.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/android/)+  Bug fixes and stability improvements. <br />+  Added support for participant token exchange.  | 
| [iOS Broadcast SDK 1.37.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.37.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.37.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/)+  Bug fixes and stability improvements. <br />+  Added support for participant token exchange.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1370-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.753 MB | 13.961 MB | 
| armeabi-v7a | 4.990 MB | 9.680 MB | 
| x86\_64 | 5.857 MB | 14.525 MB | 
| x86 | 6.127 MB | 15.116 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1370-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.588 MB | 8.028 MB | 

## November 7, 2025
<a name="nov07-25-ipr-synchronization-rt"></a>

### Individual Participant Recording Synchronization
<a name="nov07-25-ipr-synchronization-rt-desc"></a>

New support for `EXT-X-PROGRAM-DATE-TIME` tags in individual participant recording HLS playlists enables precise synchronization of multiple participant recordings during post-processing. This feature provides millisecond-accurate UTC timestamps at recording start and discontinuity points, allowing you to create synchronized compositions (such as side-by-side or picture-in-picture layouts) even when participants experience network interruptions or join at different times. For details, see [Synchronize Multiple Participant Recordings](rt-individual-participant-recording.md#ind-part-rec-sync-multiple) in *Individual Participant Recording*.

## October 30, 2025
<a name="oct30-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.30.0 (Real-Time Streaming)
<a name="oct30-25-broadcast-web-rt-1300"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.30.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Bug fixes and stability improvements.  | 

## October 30, 2025
<a name="oct30-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.36.0, iOS 1.36.0 (Real-Time Streaming)
<a name="oct30-25-broadcast-mobile-rt-1360"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.36.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/android/)+  Improved camera recovery when returning to the foreground after being in the background for a prolonged period of time. <br />+  Added an `embedMessage` method on `ImageDevice` to enable the insertion of metadata payloads into a publishing video stream. See [Embed Messages](android-publish-subscribe.md#android-publish-subscribe-embed-messages) in the *Android Broadcast SDK Guide*.  | 
| [iOS Broadcast SDK 1.36.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.36.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.36.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/ios/)+  Added an `embedMessage` method on `IVSImageDevice` to enable the insertion of metadata payloads into a publishing video stream. See [Embed Messages](ios-publish-subscribe.md#ios-publish-subscribe-embed-messages) in the *iOS Broadcast SDK Guide*.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1360-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.736 MB | 13.898 MB | 
| armeabi-v7a | 4.974 MB | 9.638 MB | 
| x86\_64 | 5.839 MB | 14.456 MB | 
| x86 | 6.109 MB | 15.047 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1360-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.569 MB | 7.962 MB | 

## October 14, 2025
<a name="oct14-25-rt-compositions"></a>

### Updated Real-Time Limit: Compositions
<a name="oct14-25-rt-compositions-desc"></a>

We updated the quota for "maximum concurrent Composition resources per account" from 5 to 20. It is documented in Service Quotas > [Other Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html#quotas-other).

## October 2, 2025
<a name="oct02-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.29.0 (Real-Time Streaming)
<a name="oct02-25-broadcast-web-rt-1290"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.29.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Bug fixes and stability improvements.  | 

## October 2, 2025
<a name="oct02-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.35.0, iOS 1.35.0 (Real-Time Streaming)
<a name="oct02-25-broadcast-mobile-rt-1350"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.35.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/android/)+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.35.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.35.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.35.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/ios/)+  `IVSImageDevice.setOnFrameCallback` can now be customized with a `DispatchQueue`, and it can optionally include the `CVPixelBuffer` associated with the frame.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1350-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.730 MB | 13.900 MB | 
| armeabi-v7a | 4.971 MB | 9.639 MB | 
| x86\_64 | 5.835 MB | 14.455 MB | 
| x86 | 6.104 MB | 15.041 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1350-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.569 MB | 7.963 MB | 

## September 16, 2025
<a name="sep16-25-ssc-custom-participant-ordering"></a>

### Server-Side Composition Custom Participant Ordering
<a name="sep16-25-ssc-custom-participant-ordering"></a>

New support for custom participant ordering for SSC provides granular control over participant positioning in both grid and Picture-in-Picture (PiP) layouts. See [Server-Side Composition](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/server-side-composition.html) (various changes, including adding `participantOrderAttribute` and "Custom Participant Ordering") and the [IVS Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html) (added `participantOrderAttribute` to the Composition object).

## September 11, 2025
<a name="sep11-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.34.0, iOS 1.34.0 (Real-Time Streaming)
<a name="sep11-25-broadcast-mobile-rt-1340"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.34.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/android/)+  CPU improvements for publish and subscribe media transport. <br />+  Added `packetsLost` to `LocalVideoStats` and `LocalAudioStats`.  | 
| [iOS Broadcast SDK 1.34.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.34.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.34.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/ios/)+  CPU improvements for publish and subscribe media transport. <br />+  Added `packetsLost` to `IVSLocalVideoStats` and `IVSLocalAudioStats`. <br />+  Fixed a bug where devices did not detach after leaving a stage, which could result in privacy indicators unexpectedly being lit.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1340-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.796 MB | 14.089 MB | 
| armeabi-v7a | 5.036 MB | 9.788 MB | 
| x86\_64 | 5.906 MB | 14.653 MB | 
| x86 | 6.174 MB | 15.240 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1340-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.594 MB | 8.046 MB | 

## September 10, 2025
<a name="sep10-25-interface-vpc-endpoints-rt"></a>

### Interface VPC Endpoints
<a name="sep10-25-interface-vpc-endpoints-rt-desc"></a>

New support for interface VPC (Virtual Private Cloud) endpoints enables you to establish a secure private connection between your Amazon VPC and IVS, for workloads that require secure, live video ingestion. This keeps your IVS ingest traffic within the AWS network and off the public internet. Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables private communication between AWS services, using an elastic network interface with private IPs in your Amazon VPC. See [Private Ingest](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-ingest-ll.html) in the *IVS Low-Latency Streaming User Guide* and [Private Ingest to Stages](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html#private-ingest-stages) in the *IVS Real-Time Streaming User Guide*.

## September 4, 2025
<a name="sep04-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.28.0 (Real-Time Streaming)
<a name="sep04-25-broadcast-web-rt-1280"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.28.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Joining a stage that was deleted, or with a participant token that was disconnected, now reports `STAGE_DELETED` or `STAGE_DISCONNECTED` errors instead of `TIMEOUT`. <br />+  Optimized internal polling requests related to simulcast.  | 

## August 7, 2025
<a name="aug07-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.27.0 (Real-Time Streaming)
<a name="aug07-25-broadcast-web-rt-1270"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.27.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added `requestQualityStats` to `RemoteStageStream`, which then exposes a simplified object of video and audio stats sourced from `requestRTCStats`. <br />+  Updates to ensure that the `RemoteStageStream` muted state and its `mediaStreamTrack` enabled state are always in sync.  | 

## August 7, 2025
<a name="aug07-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.33.0, iOS 1.33.0 (Real-Time Streaming)
<a name="aug07-25-broadcast-mobile-rt-1330"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.33.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/android/)+  New methods to control device torch:   `CameraSource.Capabilities` implements `isTorchSupported`.   `CameraSource.Options.Builder` implements `setEnableTorch`.   <br />+  The Android broadcast SDK meets Google Play’s [16 KB page-size compatibility requirement](https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html). (Note: This was implemented as of version 1.23.0 of the SDK.)  | 
| [iOS Broadcast SDK 1.33.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.33.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.33.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/ios/)+  New method to control device torch: `IVSImageDevice` implements two properties, `isTorchSupported` and `torchEnabled`. Check if the device supports torch with `isTorchSupported`, and then toggle it by setting `torchEnabled`. <br />+  Resolved an issue on iOS 18.5\+ with certain VPNs that could result in peer connection timeouts. (Note: This was implemented as of version 1.32.1 of the SDK.)  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1330-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.689 MB | 13.829 MB | 
| armeabi-v7a | 4.962 MB | 9.649 MB | 
| x86\_64 | 5.806 MB | 14.413 MB | 
| x86 | 6.066 MB | 14.983 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1330-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.505 MB | 7.828 MB | 

## July 25, 2025
<a name="jul25-25-broadcast-android-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.32.2 (Real-Time Streaming)
<a name="jul25-25-broadcast-android-rt-1322"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.32.2](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.32.2/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.32.2/android/)+  Disabled IPv6 for `Stage` connections.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1322-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.693 MB | 13.838 MB | 
| armeabi-v7a | 4.964 MB | 9.653 MB | 
| x86\_64 | 5.810 MB | 14.422 MB | 
| x86 | 6.067 MB | 14.988 MB | 

## July 23, 2025
<a name="jul23-25-rt"></a>

### Enforcement of New Real-Time Metrics and Limits: Concurrent Publishers and Subscriptions
<a name="jul23-25-rt-concurrent-limits-rt"></a>

On [June 23](#jun23-25-rt-concurrent-limits), we introduced two new adjustable service quotas, for the maximum number of concurrent publishers and concurrent subscriptions across all stages in an AWS Region. Today we start enforcing these new quotas.

## July 15, 2025
<a name="jul15-25-rt-participant-replications"></a>

### New Real-Time Limit: Concurrent Participant Replications
<a name="jul15-25-rt-participant-replications-desc"></a>

We've introduced a new non-adjustable service quota, for the maximum number of concurrent replications per participant across all stages in an AWS Region. It is documented in Service Quotas > [Other Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html#quotas-other).

## July 10, 2025
<a name="jul10-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.32.1, iOS 1.32.1 (Real-Time Streaming)
<a name="jul10-25-broadcast-mobile-rt-1321"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.32.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/android/)+  Removed `StageAudioConfiguration.enableEchoCancellation()`. Instead, use `StageAudioManager` to enable or disable echo cancellation. <br />+  Modified the `STUDIO` and `SUBSCRIBE_ONLY` presets in `StageAudioManager` to turn off echo cancellation. If you want to use `STUDIO` with echo cancellation, first set the preset, then enable echo cancellation to override `STUDIO`'s default preference for no echo cancellation. <br />+  Added a `MixedDevice` API suite for compositing multiple image and audio sources into a single output `Device`, which can be used for publishing more complex audio and visuals to a stage.  | 
| [iOS Broadcast SDK 1.32.1](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.32.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.32.1/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/ios/)+  Added an `IVSMixedDevice` API suite for compositing multiple image and audio sources into a single output `IVSDevice`, which can be used for publishing more complex audio and visuals to a stage.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1321-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.692 MB | 13.840 MB | 
| armeabi-v7a | 4.965 MB | 9.655 MB | 
| x86\_64 | 5.810 MB | 14.424 MB | 
| x86 | 6.068 MB | 14.990 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1321-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.508 MB | 7.900 MB | 

## July 7, 2025
<a name="jul07-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.26.0 (Real-Time Streaming)
<a name="jul07-25-broadcast-web-rt-1260"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.26.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added `requestQualityStats` to LocalStageStream, which exposes a simplified object of video and audio stats sourced from requestRTCStats. <br />+  Fixed websocket leaks that could occur during setup, causing subsequent join failures. <br />+  Fixed an issue where 1302 errors would incorrectly surface when retrying a failed subscribe or publish operation. <br />+  Improved retry stability for subscribe and publish connections when the join connection is in an ERRORED or CONNECTING state.  | 

## June 23, 2025
<a name="jun23-25-rt-concurrent-limits"></a>

### New Real-Time Metrics and Limits: Concurrent Publishers and Subscriptions
<a name="jun23-25-rt-concurrent-limits-new"></a>

We've introduced two new adjustable service quotas, for the maximum number of concurrent publishers and concurrent subscriptions across all stages in an AWS Region. They are documented in Service Quotas > [Other Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html#quotas-other). These quotas give you more control over total usage across your account. Previously, IVS enforced limits only on the number of publishers and subscribers *per stage*. This made it hard to set safeguards at the account level and could result in higher usage and associated costs than expected, especially for customers creating many stages.

**Note:** We will start enforcing these new quotas on July 23, to allow 30 days for you to review your usage and request service-quota increases if needed.

We also added two new CloudWatch metrics, `ConcurrentPublishers` and `ConcurrentSubscriptions`. These metrics help you monitor usage across all stages and assess whether you are approaching the default limits. They are documented in Monitoring Real-Time Streaming > [CloudWatch Metrics](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/stage-health.html#stage-health-cloudwatch-metrics). We recommend setting up [CloudWatch alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html) to alert you when your usage is close to a quota limit.

## June 20, 2025
<a name="jun20-25-rt"></a>

### E-RTMP Multitrack Video Ingest Support
<a name="jun20-25-multitrack-for-rt"></a>

You can use E-RTMP (Enhanced Real-Time Messaging Protocol) multitrack video to send multiple video qualities to your IVS stages. This feature enables adaptive bitrate streaming, allowing viewers to watch in the best quality for their network connection. See [E-RTMP Multitrack Video](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html#rtmp-multitrack) in the IVS RTMP Publishing documentation.

## June 16, 2025
<a name="jun16-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.25.1 (Real-Time Streaming)
<a name="jun16-25-broadcast-web-rt-1251"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.25.1](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Removed the NPM unintentional engine enforcement of v22. All LTS node versions are supported as the package is transpiled.  | 

## June 12, 2025
<a name="jun12-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.31.0, iOS 1.31.0 (Real-Time Streaming)
<a name="jun12-25-broadcast-mobile-rt-1310"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.31.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/android/)+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.31.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.31.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.31.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/ios/)+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1310-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.579 MB | 13.594 MB | 
| armeabi-v7a | 4.864 MB | 9.473 MB | 
| x86\_64 | 5.697 MB | 14.173 MB | 
| x86 | 5.951 MB | 14.724 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1310-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.431 MB | 7.732 MB | 

## June 12, 2025
<a name="jun12-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.25.0 (Real-Time Streaming)
<a name="jun12-25-broadcast-web-rt-1250"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.25.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed a bug where SEI messages might fail to send after a remote participant encountered an `ERROR` state. <br />+  Fixed a bug where multiple remote stage streams might be returned when the `STAGE_STREAM_MUTE_CHANGED` stage event was invoked. <br />+  Fixed a bug where `STAGE_PARTICIPANT_STREAMS_REMOVED` was not invoked for streams that had errored.  | 

## May 29, 2025
<a name="may29-25-rt"></a>

### Participant Replication
<a name="may29-25-participant-replication"></a>

Participant replication allows you to copy a participant from one stage to another. This is useful when you want the same participant to appear in multiple stages at the same time, enabling cross-stage interactions. For documentation changes, see the [Document History](doc-history.md) (both User Guide and API Reference tables).

## May 26, 2025
<a name="may26-25-broadcast-android-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.30.1 (Real-Time Streaming)
<a name="may26-25-broadcast-android-rt-1301"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.30.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.30.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.30.1/android/)+  Fixed a low-microphone-volume bug on some Android devices when using SDK-managed microphones from `DeviceDiscovery` with the `STUDIO` audio preset.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1301-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.579 MB | 13.592 MB | 
| armeabi-v7a | 4.863 MB | 9.472 MB | 
| x86\_64 | 5.696 MB | 14.171 MB | 
| x86 | 5.950 MB | 14.722 MB | 

## May 15, 2025
<a name="may15-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.24.0 (Real-Time Streaming)
<a name="may15-25-broadcast-web-rt-1240"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.24.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed memory leaks when leaving and rejoining a stage.  | 

## May 15, 2025
<a name="may15-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.30.0, iOS 1.30.0 (Real-Time Streaming)
<a name="may15-25-broadcast-mobile-rt-1300"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.30.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/android/)+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.30.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.30.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.30.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/ios/)+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1300-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.571 MB | 13.577 MB | 
| armeabi-v7a | 4.857 MB | 9.462 MB | 
| x86\_64 | 5.691 MB | 14.156 MB | 
| x86 | 5.944 MB | 14.708 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1300-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.430 MB | 7.732 MB | 

## May 2, 2025
<a name="may02-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.23.1 (Real-Time Streaming)
<a name="may02-25-broadcast-web-rt-1231"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.23.1](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed an issue where participant join events always occurred before `join()` resolved. <br />+  Fixed an issue where local participants were erroneously reported as remote participants when leaving and rejoining in quick succession.  | 

## April 17, 2025
<a name="apr17-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.29.0, iOS 1.29.0 (Real-Time Streaming)
<a name="apr17-25-broadcast-mobile-rt-1290"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.29.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/android/)+  Added a simulcast publisher controls feature. See "Configuring Layered Encoding (Publisher)" in the [Android Broadcast SDK Guide](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/android-publish-subscribe.html#android-layered-encoding-simulcast-configure-publisher). <br />+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.29.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.29.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.29.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/ios/)+  Added a simulcast publisher controls feature. See "Configuring Layered Encoding (Publisher)" in the [iOS Broadcast SDK Guide](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ios-publish-subscribe.html#ios-layered-encoding-simulcast-configure-publisher). <br />+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1290-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.566 MB | 13.546 MB | 
| armeabi-v7a | 4.853 MB | 9.444 MB | 
| x86\_64 | 5.681 MB | 14.119 MB | 
| x86 | 5.939 MB | 14.674 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1290-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.429 MB | 7.715 MB | 

## April 17, 2025
<a name="apr17-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.23.0 (Real-Time Streaming)
<a name="apr17-25-broadcast-web-rt-1230"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.23.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added a simulcast publisher controls feature. See "Configuring Layered Encoding (Publisher)" in the [Web Broadcast SDK Guide](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/web-publish-subscribe.html#web-layered-encoding-simulcast-configure-publisher). <br />+  Improved time to publish latency. This impacts the timing of the `PUBLISHED` event. <br />+  Fixed a bug where the SDK fired join category errors via the [ERROR](broadcast-web-error-handling.md) callback when connection to the stage was lost but potentially recoverable (specifically, `FAILED` and `TIMEOUT` errors for the `JOIN_ERROR` category). <br />+  Fixed a bug with the `insertSeiMessage` operation where a strategy refresh could result in subsequent invocations of `insertSeiMessage` failing to send the SEI message.  | 

## April 2, 2025
<a name="apr02-25-rt"></a>

### New Quota: Compositions Per Stage
<a name="apr02-25-max-comp-stage"></a>

We added a new quota, for the maximum concurrent compositions allowed per stage. This is documented in Service Quotas > [Other Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html#quotas-other).

## March 20, 2025
<a name="mar20-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.28.1, iOS 1.28.1 (Real-Time Streaming)
<a name="mar20-25-broadcast-mobile-rt-1281"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.28.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/android/)+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.28.1](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.28.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.28.1/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/ios/)+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1281-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.613 MB | 13.760 MB | 
| armeabi-v7a | 4.885 MB | 9.558 MB | 
| x86\_64 | 5.728 MB | 14.342 MB | 
| x86 | 5.987 MB | 14.923 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1281-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.417 MB | 7.698 MB | 

## March 20, 2025
<a name="mar20-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.22.0 (Real-Time Streaming)
<a name="mar20-25-broadcast-web-rt-1220"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.22.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added `null` as a valid return type to the [preferredLayerForStream](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/StageStrategy#preferredlayerforstream) strategy method. <br />+  Fixed a bug where `preferredLayerForStream` was not called again if new layers became available after the stream started. <br />+  Fixed a bug where `stream.getHighestQualityLayer` did not pick the highest quality layer after the stream started.  | 

## March 19, 2025
<a name="mar19-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.27.2, iOS 1.27.2 (Real-Time Streaming)
<a name="mar19-25-broadcast-mobile-rt-1272"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.27.2](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/android/)+  Fixed a resource-leak regression that impacted some devices when creating 50 or more stages. <br />+  Fixed a regression that could cause an increased rate of video freezes when using third-party publishing software.  | 
| [iOS Broadcast SDK 1.27.2](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.27.2/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.27.2/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/ios/)+  Fixed a regression that could cause an increased rate of video freezes when using third-party publishing software.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1272-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.700 MB | 14.197 MB | 
| armeabi-v7a | 4.945 MB | 9.879 MB | 
| x86\_64 | 5.810 MB | 14.802 MB | 
| x86 | 6.073 MB | 15.412 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1272-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.622 MB | 8.584 MB | 

## March 13, 2025
<a name="mar13-25-rt"></a>

### Target Segment Duration
<a name="mar13-25-target-segment-duration"></a>

This release adds to the IVS real-time streaming API, to allow you to define the target duration for recorded segments generated when either using composite recording or recording a stage participant. For specific API changes, see the [Document History](doc-history.md) (both User Guide and API Reference tables).

## March 6, 2025
<a name="mar6-25-rt"></a>

### Individual Participant Recording Stitching
<a name="mar6-25-ipr-vod-stitching"></a>

This is the first release of new functionality. If your stage is configured for individual participant recording, you can now specify a window of time during which, if a stage publisher disconnects from a stage and then reconnects, IVS tries to record to the same S3 prefix as the previous session. In other words, if a publisher disconnects and then reconnects within the specified interval, the multiple recordings are considered a single recording and merged. For documentation changes, see the [Document History](doc-history.md) (both the User Guide and API Reference tables).

## March 3, 2025
<a name="mar03-25-broadcast-ios-rt"></a>

### Amazon IVS Broadcast SDK: iOS 1.27.1 (Real-Time Streaming)
<a name="mar03-25-broadcast-ios-rt-1271"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [iOS Broadcast SDK 1.27.1](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.27.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.27.1/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.27.1/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.1/ios/)+  Improved focus performance for objects held close to the camera while using the ultra-wide lens on Pro devices.  | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1271-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.625 MB | 8.601 MB | 

## February 20, 2025
<a name="feb20-25-broadcast-mobile-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.27.0, iOS 1.27.0 (Real-Time Streaming)
<a name="feb20-25-broadcast-mobile-rt-1270"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.27.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/android/)+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.27.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.27.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.27.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/ios/)+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1270-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.700 MB | 14.197 MB | 
| armeabi-v7a | 4.944 MB | 9.879 MB | 
| x86\_64 | 5.809 MB | 14.802 MB | 
| x86 | 6.073 MB | 15.412 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1270-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.625 MB | 8.601 MB | 

## February 20, 2025
<a name="feb20-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.21.0 (Real-Time Streaming)
<a name="feb20-25-broadcast-web-rt-1210"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.21.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Updated `preferredLayerForStream` strategy types to include `null`, which is a valid return. <br />+  Fixed TypeScript compile errors when TSconfig `skipLibCheck` is set to false. <br />Note: As part of this release, types have been consolidated into a single rollup. If an application imports nested types based on path, errors may occur. If errors do occur, change the import to simply `'amazon-ivs-broadcast'`.  | 

## January 30, 2025
<a name="jan30-25-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.26.0, iOS 1.26.0 (Real-Time Streaming)
<a name="jan30-25-broadcast-ai-rt-1260"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.26.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/android/)+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.26.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.26.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.26.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/ios/)+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1260-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.695 MB | 14.186 MB | 
| armeabi-v7a | 4.939 MB | 9.872 MB | 
| x86\_64 | 5.804 MB | 14.790 MB | 
| x86 | 6.065 MB | 15.398 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1260-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.624 MB | 8.601 MB | 

## January 23, 2025
<a name="jan23-25-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.20.0 (Real-Time Streaming)
<a name="jan23-25-broadcast-web-rt-1200"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.20.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added the `insertSeiMessage` method on LocalStageStream to enable the insertion of Supplemental Enhancement Information (SEI) payloads into a publishing video stream. See [Supplemental Enhanced Information](web-publish-subscribe.md#web-publish-subscribe-sei-attributes) in the *IVS Broadcast SDK: Web Guide*.  | 

## December 12, 2024
<a name="dec12-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.25.0, iOS 1.25.0 (Real-Time Streaming)
<a name="dec12-24-broadcast-ai-rt-1250"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.25.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/android/)+  Added a simulcast controls feature. See [Configuring Layered Encoding with Simulcast (Subscriber)](real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber) in *Streaming Optimizations*. <br />+  Made SEI (Supplemental Enhanced Information) payloads available to subscribers with a new field on ImageDeviceFrame objects. See [Get Supplemental Enhancement Information (SEI)](android-publish-subscribe.md#android-publish-subscribe-sei-attributes) in the *IVS Broadcast SDK: Android Guide*. <br />+  Added the `SubscribeConfiguration::setInitialGain` method to allow the configuration of the initial gain value for incoming audio streams. <br />+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.25.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.25.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.25.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/ios/)+  Added a simulcast controls feature. See [Configuring Layered Encoding with Simulcast (Subscriber)](real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber) in *Streaming Optimizations*. <br />+  Made SEI (Supplemental Enhanced Information) payloads available to subscribers with a new field on IVSImageDeviceFrame objects. See [Get Supplemental Enhancement Information (SEI)](ios-publish-subscribe.md#ios-publish-subscribe-sei-attributes) in the *IVS Broadcast SDK: iOS Guide*. <br />+  Added the `IVSSubscribeConfiguration.initialGain` method to allow the configuration of the initial gain value for incoming audio streams. <br />+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1250-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.677 MB | 14.103 MB | 
| armeabi-v7a | 4.905 MB | 9.791 MB | 
| x86\_64 | 5.786 MB | 14.725 MB | 
| x86 | 6.030 MB | 15.302 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1250-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.625 MB | 8.585 MB | 

## December 12, 2024
<a name="dec12-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.19.0 (Real-Time Streaming)
<a name="dec12-24-broadcast-web-rt-1190"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.19.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added a simulcast controls feature. See [Configuring Layered Encoding with Simulcast (Subscriber)](real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber) in *Streaming Optimizations*. <br />+  Bug fixes and stability improvements.  | 

## December 10, 2024
<a name="dec10-24-thumbnails-rt-date"></a>

### Real-Time Streaming Thumbnail Configuration
<a name="dec10-24-thumbnails-rt"></a>

This release allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session. This is the first release of this new functionality. See:
+  [Individual Participant Recording](rt-individual-participant-recording.md) — We updated examples and JSON metadata information, and we added pricing information and "Thumbnail-Only Recordings."
+ [Composite Recording](rt-composite-recording.md) — We updated examples and JSON metadata information, and we added pricing information.
+ [API Reference RT](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html) — We made several changes:
  + Modified the S3DestinationConfiguration object: added `thumbnailConfigurations`. This affects the GetComposition response and StartComposition request and response.
  + Modified the AutoParticipantRecordingConfiguration object: added `thumbnailConfiguration` and added `NONE` as a valid value for `mediaTypes`. This affects the CreateStage request and response, GetStage response, and UpdateStage request and response.
  + Added two objects: CompositionThumbnailConfiguration and ParticipantThumbnailConfiguration.

## November 13, 2024
<a name="nov13-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.24.0, iOS 1.24.0 (Real-Time Streaming)
<a name="nov13-24-broadcast-ai-rt-1240"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.24.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/android/)+  Bug fixes and stability improvements.  | 
| [iOS Broadcast SDK 1.24.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.24.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.24.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/ios/)+  Bug fixes and stability improvements.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1240-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.521 MB | 13.791 MB | 
| armeabi-v7a | 4.789 MB | 9.623 MB | 
| x86\_64 | 5.718 MB | 14.709 MB | 
| x86 | 5.933 MB | 15.163 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1240-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.589 MB | 8.466 MB | 

## November 12, 2024
<a name="nov12-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.18.0 (Real-Time Streaming)
<a name="nov12-24-broadcast-web-rt-1180"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.18.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added a new event to make SEI (Supplemental Enhanced Information) payloads available to subscribers. <br />+  Fixed an exception that would occur during unpublish and unsubscribe requests. <br />+  Fixed a race condition where joining and leaving rapidly would cause an error for other participants.  | 

## October 10, 2024
<a name="oct10-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.17.0 (Real-Time Streaming)
<a name="oct10-24-broadcast-web-rt-1170"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.17.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Minor bug fixes.  | 

## October 10, 2024
<a name="oct10-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.23.0, iOS 1.23.0 (Real-Time Streaming)
<a name="oct10-24-broadcast-ai-rt-1230"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.23.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/android/)+  With this release we also began publishing a version of the Android broadcast SDK which includes debug symbols. See [Using the SDK with Debug Symbols](broadcast-android-getting-started.md#broadcast-android-using-debug-symbols-rt). <br />+  Minor bug fixes.  | 
| [iOS Broadcast SDK 1.23.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.23.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.23.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/ios/)+  Minor bug fixes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1230-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.432 MB | 13.560 MB | 
| armeabi-v7a | 4.707 MB | 9.451 MB | 
| x86\_64 | 5.626 MB | 14.459 MB | 
| x86 | 5.838 MB | 14.908 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1230-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.542 MB | 8.316 MB | 

## September 11, 2024
<a name="sep11-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.22.0, iOS 1.22.0 (Real-Time Streaming)
<a name="sep11-24-broadcast-ai-rt-1220"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.22.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/android/)+  Fixed a bug where certain Android devices show a black frame in the preview after switching camera inputs. <br />+  Minor bug fixes.  | 
| [iOS Broadcast SDK 1.22.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.22.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.22.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/ios/)+  Minor bug fixes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1220-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.359 MB | 13.392 MB | 
| armeabi-v7a | 4.636 MB | 9.325 MB | 
| x86\_64 | 5.548 MB | 14.268 MB | 
| x86 | 5.754 MB | 14.710 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1220-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.488 MB | 8.199 MB | 

## September 11, 2024
<a name="sep11-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.16.0 (Real-Time Streaming)
<a name="sep11-24-broadcast-web-rt-1160"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.16.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Minor bug fixes.  | 

## September 9, 2024
<a name="sep9-24-rt"></a>

### RTMP Ingest
<a name="sep9-24-rt-rtmp-ingest"></a>

As an alternative to using the IVS broadcast SDK, you can now publish video to an IVS stage from an RTMP source (in addition to WHIP, which already was supported). For documentation changes, see the [Document History](doc-history.md) (both the User Guide and API Reference tables).

## August 19, 2024
<a name="aug19-24-rt"></a>

### In-Console Publish/Subscribe
<a name="in-console-publish-subscribe"></a>

You can now publish and subscribe from the IVS console. In *Getting Started with IVS Real-Time Streaming*, see [Publish and Subscribe to Video](getting-started-pub-sub.md).

## August 15, 2024
<a name="aug15-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.15.0 (Real-Time Streaming)
<a name="aug15-24-broadcast-web-rt-1150"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.15.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed a race condition that impacts publisher media quality when `join()` is called repeatedly. Calling `join()` in succession no longer re-triggers the `STAGE_PARTICIPANT_JOINED` event, along with accompanying publish and stream state changes. <br />+  Fixed a bug that causes issues parsing participant tokens when non-text characters are used in the token `attributes` field. <br />+  Added a method to configure a participant's subscribers. Initially, you can configure only the jitter-buffer minimum delay. See the SDK reference documentation, [Configuration for Subscribing to Participants](web-publish-subscribe.md#web-publish-subscribe-concepts-strategy-participants-config) in the *Web Broadcast SDK Guide*, and [Changing Subscriber Jitter Buffer MinDelay](real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay) in *Streaming Optimizations*.  | 

## August 15, 2024
<a name="aug15-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.21.0, iOS 1.21.0 (Real-Time Streaming)
<a name="aug15-24-broadcast-ai-rt-1210"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.21.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/android/)+  Fixed a bug impacting devices with MT6765 chipsets, where the subscriber preview renders black frames under some circumstances. <br />+  Added a method to configure a participant's subscribers. Initially, you can configure only the jitter-buffer minimum delay. See the SDK reference documentation, [Configuration for Subscribing to Participants](android-publish-subscribe.md#android-publish-subscribe-concepts-strategy-participants-config) in the *Android Broadcast SDK Guide*, and [Changing Subscriber Jitter Buffer MinDelay](real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay) in *Streaming Optimizations*. <br />+  Minor bug fixes.  | 
| [iOS Broadcast SDK 1.21.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.21.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.21.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/ios/)+  Added a method to configure a participant's subscribers. Initially, you can configure only the jitter-buffer minimum delay. See the SDK reference documentation, [Configuration for Subscribing to Participants](ios-publish-subscribe.md#ios-publish-subscribe-concepts-strategy-participants-config) in the *iOS Broadcast SDK Guide*, and [Changing Subscriber Jitter Buffer MinDelay](real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay) in *Streaming Optimizations*. <br />+  Minor bug fixes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1210-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.350 MB | 13.378 MB | 
| armeabi-v7a | 4.628 MB | 9.312 MB | 
| x86\_64 | 5.538 MB | 14.253 MB | 
| x86 | 5.744 MB | 14.694 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1210-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.485 MB | 8.199 MB | 

## July 18, 2024
<a name="jul18-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.14.0 (Real-Time Streaming)
<a name="jul18-24-broadcast-web-rt-1140"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.14.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  API documentation improvements. <br />+  Fixed video and audio stats outliers reported during connection resets. <br />+  Minor dependency updates.  | 

## July 18, 2024
<a name="jul18-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.20.0, iOS 1.20.0 (Real-Time Streaming)
<a name="jul18-24-broadcast-ai-rt-1200"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.20.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/android)+  Fixed a bug that prevented the Broadcast SDK from running on Chromebooks with Intel processors. <br />+  Minor bug fixes.  | 
| [iOS Broadcast SDK 1.20.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.20.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.20.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/ios)+  Minor bug fixes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1200-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.318 MB | 13.299 MB | 
| armeabi-v7a | 4.605 MB | 9.254 MB | 
| x86\_64 | 5.507 MB | 14.168 MB | 
| x86 | 5.715 MB | 14.608 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1200-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.465 MB | 8.164 MB | 

## June 26, 2024
<a name="jun25-24-rt"></a>

### Generate Participant Tokens with a Key Pair
<a name="key-pair-participant-tokens"></a>

You can now generate participant tokens on your own server application by using a key pair. This enables you to avoid calling CreateParticipantToken every time you need a participant token. For documentation changes, see the [Document History](doc-history.md) (both the User Guide and API Reference tables).

## June 20, 2024
<a name="june-20-ind-part-rec"></a>

### Individual Participant Recording
<a name="june-20-ind-part-rec-details"></a>

Individual participant recording allows IVS real-time streaming customers to record IVS stage publishers individually into S3 buckets. See [Recording](rt-recording.md), [Individual Participant Recording](rt-individual-participant-recording.md), and changes in the [Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html). (For specific documentation changes, see the [Document History](doc-history.md).)

## June 13, 2024
<a name="jun13-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.19.0, iOS 1.19.0 (Real-Time Streaming)
<a name="jun13-24-broadcast-ai-rt-1190"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.19.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/android)+  Recent Android versions require an icon in the notification that is displayed when capturing the screen. If desired, you can now customize the icon by calling `setSmallIcon` on the `Notification.Builder` returned by `Session # createServiceNotificationBuilder`. <br />+  Improved connection recovery time on devices transitioning from wifi to cellular connections. This change requires the `CHANGE_NETWORK_STATE` permission.  | 
| [iOS Broadcast SDK 1.19.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.19.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.19.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/ios)+  Minor bug fixes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1190-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.304 MB | 13.340 MB | 
| armeabi-v7a | 4.598 MB | 9.299 MB | 
| x86\_64 | 5.495 MB | 14.207 MB | 
| x86 | 5.694 MB | 14.625 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1190-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.393 MB | 7.949 MB | 

## June 13, 2024
<a name="jun13-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.13.0 (Real-Time Streaming)
<a name="jun13-24-broadcast-web-rt-1130"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.13.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Updated the duration of event change behavior for `StageEvents.STAGE_PARTICIPANT_SUBSCRIBE_STATE_CHANGED` and `StageEvents.STAGE_PARTICIPANT_PUBLISH_STATE_CHANGED`. Participants now remain in the `ATTEMPTING_SUBSCRIBE` or `ATTEMPTING_PUBLISH` state for a longer time, until the `ERRORED` event is fired. <br />+  Added the `StageEvents.ERROR` event for listening to errors encountered by the SDK. See [Error Handling](broadcast-web-error-handling.md) in the *Real-Time Broadcast SDK: Web Guide* for more information.  | 

## May 20, 2024
<a name="may20-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.12.0 (Real-Time Streaming)
<a name="may20-24-broadcast-web-rt-1120"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.12.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Improved retry handling for publish and subscribe operations. <br />+  Improved analytics, specifically latency and audio-quality measurement.  | 

## May 16, 2024
<a name="may16-24-broadcast-ai-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.18.0, iOS 1.18.0 (Real-Time Streaming)
<a name="may16-24-broadcast-ai-rt-1180"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.18.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/android)+  The SDK now sends specific error codes when a connected Stage is deleted by the AWS control plane, or when the token in use is revoked. <br />+  Minor bug fixes.  | 
| [iOS Broadcast SDK 1.18.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.18.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.18.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/ios)+  The SDK now sends specific error codes when a connected Stage is deleted by the AWS control plane, or when the token in use is revoked. <br />+  Added the IVSCamera `setVideoZoomFactor` method and the associated `IVSCameraDelegate` methods.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1180-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.275 MB | 13.279 MB | 
| armeabi-v7a | 4.573 MB | 9.254 MB | 
| x86\_64 | 5.472 MB | 14.142 MB | 
| x86 | 5.664 MB | 14.554 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1180-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.393 MB | 7.916 MB | 

## May 6, 2024
<a name="may06-24-broadcast-web-rt"></a>

### IVS Broadcast SDK: Web 1.11.0 (Real-Time Streaming)
<a name="may06-24-broadcast-web-rt-1110"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.11.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed an edge case where the SDK did not attempt to recover on a stage `DISCONNECT`. <br />+  Updated the error message for a `join()` timeout error. Instead of "InitialConnectTimedOut after 10 seconds," the SDK now returns "Operation timed out."  | 

## April 30, 2024
<a name="apr30-24-broadcast-web-1101-rt"></a>

### IVS Broadcast SDK: Web 1.10.1 (Real-Time Streaming)
<a name="apr30-24-broadcast-web-1101"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.10.1](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Minor bug fixes.  | 

## April 30, 2024
<a name="apr30-24-broadcast-1152-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.15.2, iOS 1.15.2 (Real-Time Streaming)
<a name="apr30-24-broadcast-1152"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.15.2](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/android)+  Minor bug fixes. Upgrade to this version only if you have a specific reason to do so; otherwise, use the highest version that is released.  | 
| [iOS Broadcast SDK 1.15.2](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.15.2/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.15.2/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/ios)+  Minor bug fixes. Upgrade to this version only if you have a specific reason to do so; otherwise, use the highest version that is released.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1152-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.244 MB | 13.198 MB | 
| armeabi-v7a | 4.543 MB | 9.192 MB | 
| x86\_64 | 5.437 MB | 14.051 MB | 
| x86 | 5.631 MB | 14.461 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1152-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.359 MB | 7.836 MB | 

## April 22, 2024
<a name="apr22-24-broadcast-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.17.0, iOS 1.17.0 (Real-Time Streaming)
<a name="apr22-24-broadcast-rt-1170"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.17.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/android)+  Fixed a rare crash that can occur while publishing.  | 
| [iOS Broadcast SDK 1.17.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.17.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.17.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/ios)+  The `AmazonIVSBroadcast` framework now includes a privacy manifest, as required by Apple.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1170-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.273 MB | 13.275 MB | 
| armeabi-v7a | 4.571 MB | 9.251 MB | 
| x86\_64 | 5.468 MB | 14.137 MB | 
| x86 | 5.662 MB | 14.549 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1170-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.388 MB | 7.916 MB | 

## March 21, 2024
<a name="mar21-24-broadcast-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.16.0, iOS 1.16.0, Web 1.10.0 (Real-Time Streaming)
<a name="mar21-24-rt-broadcast-1160-1100"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.10.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed an intermittent error when cleaning up connections after unsubscribing or leaving a stage.  | 
| [Android Broadcast SDK 1.16.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/android)+  Fixed a previews freeze on the Exynos variant of Samsung devices with Android 14. <br />+  Added a function for querying camera zoom capabilities and setting the zoom factor.  | 
| [iOS Broadcast SDK 1.16.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.16.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.16.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/ios)+  Minor bug fixes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1160-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.253 MB | 13.21 MB | 
| armeabi-v7a | 4.551 MB | 9.204 MB | 
| x86\_64 | 5.447 MB | 14.070 MB | 
| x86 | 5.640 MB | 14.480 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1160-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.361 MB | 7.836 MB | 

## March 13, 2024
<a name="mar13-24-broadcast-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.15.1, iOS 1.15.1 (Real-Time Streaming)
<a name="mar13-24-rt-broadcast-1151"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.15.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/android)+  Fixed a rare crash when subscribing to a remote participant.  | 
| [iOS Broadcast SDK 1.15.1](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.15.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.15.1/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/ios)+  Fixed a rare crash when subscribing to a remote participant.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1151-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.243 MB | 13.194 MB | 
| armeabi-v7a | 4.541 MB | 9.188 MB | 
| x86\_64 | 5.628 MB | 14.455 MB | 
| x86 | 5.434 MB | 14.046 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1151-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.358 MB | 7.820 MB | 

## March 13, 2024
<a name="mar13-24-rt"></a>

### Server-Side Composition API Updates
<a name="server-side-composition-pip-updates"></a>

We introduced new properties to the GridConfiguration and a new picture-in-picture layout, enhancing the customization options for compositions. For specific documentation changes, see the [Document History](doc-history.md) (see the table of API Reference changes).

**Important**: Ensure your application does not depend on the specific features of the current layout, such as size and position of tiles. *Visual improvements to layouts can be introduced at any time*.

## March 8, 2024
<a name="mar08-24-rt"></a>

### Server-Side Composition Layout Updates
<a name="server-side-composition-grid-updates"></a>

Today we enabled the changes to the default grid layout that are described in the [February 7, 2024](#feb07-24-rt) entry.

## February 22, 2024
<a name="feb22-24-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.15.0, iOS 1.15.0, Web 1.9.0 (Real-Time Streaming)
<a name="feb22-24-rt-broadcast-1150-190"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.9.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Improved internal error handling.  | 
| [Android Broadcast SDK 1.15.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/android)+  Minor bug fixes.  | 
| [iOS Broadcast SDK 1.15.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.15.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.15.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/ios)+  Added an `AVPictureInPictureController` extension to allow creating a new instance with an `IVSImagePreviewView`. <br />+  Added a new API on `IVSImageDevice` to create an `AVSampleBufferDisplayLayer` to which the device renders. <br />+  Fixed a low bitrate issue on devices running iOS 17 and later. <br />+  Minor bug fixes.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1150-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.243 MB | 13.194 MB | 
| armeabi-v7a | 4.541 MB | 9.188 MB | 
| x86\_64 | 5.628 MB | 14.455 MB | 
| x86 | 5.434 MB | 14.046 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1150-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.358 MB | 7.820 MB | 

## February 7, 2024
<a name="feb07-24-rt"></a>

### Server-Side Composition Layout Updates
<a name="server-Side-composition-layout-updates"></a>

This release introduces visual improvements to the default grid layout. These changes will optimize how video is displayed and reduce blank space. These changes will be enabled on March 7, 2024.

**Important**: Ensure your application does not depend on the specific features of the current layout, such as size and position of tiles. *Visual improvements to layouts can be introduced at any time*.


| Description of the Change | Old | New | 
| --- | --- | --- | 
| Automatically selects the optimal placement of participants to maximize video size. |  ![Two colored rectangles labeled with numbers 1 and 2, representing a simple choice or option selection.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image1_ed9.png)  |  ![Two colored rectangles labeled with numbers: pink rectangle with "1" and blue rectangle with "2".](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image2.png)  | 
| Enhances space utilization by reducing gaps and minimizing black bars. |  ![Five colored rectangles numbered 1 to 5, arranged in two rows on a black background.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image3.png)  |  ![Colored rectangles numbered 1 to 5 arranged in a grid-like pattern.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image4.png)  | 
| Adds a new “camera off” indicator for clear visibility of participants not sharing video. |  ![AWS Management Console interface showing the IAM dashboard with user management options.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image5.png)  |  ![Muted video icon displayed in three separate sections on a dark background.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image6.png)  | 
| Improves space utilization and proportions for portrait use cases. |  ![Two colored rectangles labeled with numbers 1 and 2, representing a comparison or choice.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image7_ed5.png)  |  ![Two colored rectangles labeled with numbers 1 and 2, representing a simple diagram or interface layout.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image8.png)  | 
| Enhances space utilization in portrait use cases by minimizing spacing between participants and reducing letterboxing or pillarboxing. |  ![Three colored rectangles labeled with numbers 1, 2, and 3 arranged vertically.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image9_ed1.png)  |  ![Three horizontal color blocks numbered 1 to 3, in red, blue, and yellow from top to bottom.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/ssc_2024-02-07_image10.png)  | 

## February 6, 2024
<a name="feb06-24"></a>

### OBS and WHIP Support
<a name="whip-obs-support"></a>

IVS can be used with WHIP-compatible encoders like OBS to publish to IVS real-time streaming. WHIP (WebRTC-HTTP Ingestion Protocol) is an IETF draft developed to standardize WebRTC ingestion. See the new page on [OBS and WHIP Support](obs-whip-support.md).

## February 1, 2024
<a name="feb01-24-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.14.1, iOS 1.14.1, Web 1.8.0 (Real-Time Streaming)
<a name="feb01-24-rt-broadcast-1141-180"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.8.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Layered encoding with simulcast is now disabled by default. <br />+  Fixed an issue where a Stage instance would not cleanly disconnect when a Stage was deleted, or when a participant was disconnected from the server. The SDK now emits a `STAGE_CONNECTION_STATE_CHANGED` event with a state of `DISCONNECTED` (instead of `ERRORED` and then `CONNECTING`). <br />+  Fixed issue where publishing would fail when updating the strategy with empty audio or video tracks.  | 
| [Android Broadcast SDK 1.14.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/android)+  Layered encoding with simulcast is now disabled by default. <br />+  Updated `libWebRTC` from M108 to M119. <br />+  Fixed several crashes to improve overall stability. <br />+  Added support for stereo publishing. This can be enabled through the `StageAudioConfiguration` object. <br />+  Fixed a bug causing a black feed from participants after joining a session. <br />+  Updated internal `libWebRTC` references to avoid symbol conflicts when other `libWebRTC` versions are included in the same host application.  | 
| [iOS Broadcast SDK 1.14.1](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.14.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.14.1/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/ios)+  Layered encoding with simulcast is now disabled by default. <br />+  Updated `libWebRTC` from M108 to M119. <br />+  Fixed several crashes to improve overall stability. <br />+  Added support for stereo publishing. This can be enabled through `IVSLocalStageStreamAudioConfiguration`. <br />+  Fixed a crash when enabling audio-only mode for other participants. <br />+  Improved TTV and reduced binary size.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1141-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.223 MB | 13.118 MB | 
| armeabi-v7a | 4.524 MB | 9.134 MB | 
| x86\_64 | 5.418 MB | 13.955 MB | 
| x86 | 5.61 MB | 14.369 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1141-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.350 MB | 7.790 MB | 

## January 3, 2024
<a name="jan03-24-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.13.4, iOS 1.13.4, Web 1.7.0 (Real-Time Streaming)
<a name="jan03-24-rt-broadcast-1134-170"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.7.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Improved time-to-video for subscribers joining stages. <br />+  Removed the `minAudioBitrateKbps` property (it was unused). <br />+  Improved network recovery during internet outages or changes.  | 
| [Android Broadcast SDK 1.13.4](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/android)+  StageAudioConfiguration now supports setting whether echo cancellation should be enabled.  | 
| [iOS Broadcast SDK 1.13.4](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.13.4/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.13.4/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/ios)+  On iOS, we improved the audio engine for both recording and playback with a focus on stability and recoverability. This enhances support for route changes while in use, improves battery recovery for edge cases, and reduces the amount of main thread blocking. <br />+  Fixed an issue where the microphone might stay active even after it was detached from a stage, leaving the iOS privacy indicator on. (The SDK was not processing incoming audio at the time.)  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1134-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.187 MB | 13.025 MB | 
| armeabi-v7a | 4.491 MB | 9.056 MB | 
| x86\_64 | 5.359 MB | 13.829 MB | 
| x86 | 5.553 MB | 14.214 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1134-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.45 MB | 7.84 MB | 

## December 7, 2023
<a name="dec07-23-rt"></a>

### New CloudWatch Metrics
<a name="new-cloudwatch-metrics"></a>

We renamed the PacketLoss (Stage) metric to be DownloadPacketLoss (Stage). We also released additional CloudWatch metrics for IVS real-time streaming:
+ DownloadPacketLoss (Stage,Participant)
+ DroppedFrames (Stage,Participant)
+ SubscribeBitrate (Stage,Participant,MediaType)

 For details, see [Monitoring IVS Real-Time Streaming](stage-health.md).

## December 4, 2023
<a name="dec04-23-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.13.2 and iOS 1.13.2 (Real-Time Streaming)
<a name="dec04-23-rt-broadcast-1132"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| All mobile (Android and iOS) |  +  Noise-suppression configuration is available for developers to enable/disable for publishing.   | 
| [Android Broadcast SDK 1.13.2](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/android)+  Improved the time it takes to load the video (TTV) when joining the first stage in a session.  | 
| [iOS Broadcast SDK 1.13.2](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.13.2/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.13.2/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/ios)+  No changes in the real-time SDK.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1132-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.177 MB | 13.01 MB | 
| armeabi-v7a | 4.485 MB | 9.045 MB | 
| x86\_64 | 5.352 MB | 13.808 MB | 
| x86 | 5.547 MB | 14.192 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1132-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.45 MB | 7.82 MB | 

## November 21, 2023
<a name="nov21-23-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.13.1 (Real-Time Streaming)
<a name="nov21-23-rt-broadcast-android-1131"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.13.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.13.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.1/android)+  Fixed an issue that caused a crash when quickly leaving, releasing, and rejoining the same stage.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1131-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.177 MB | 13.102 MB | 
| armeabi-v7a | 4.485 MB | 9.046 MB | 
| x86\_64 | 5.353 MB | 13.809 MB | 
| x86 | 5.547 MB | 14.192 MB | 

## November 17, 2023
<a name="nov17-23-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.13.0 and iOS 1.13.0 (Real-Time Streaming)
<a name="nov17-23-rt-broadcast-1130"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| All mobile (Android and iOS) |  +  Updated [Streaming Optimizations](real-time-streaming-optimization.md). Among other things, the "Adaptive Streaming: Layered Encoding with Simulcast" feature now requires explicit opt-in and is supported only in recent versions of the SDK. <br />+  Improved the stability of stages by reducing occurrences of rare crashes. <br />+  Improved the time it takes to load the video (TTV) when joining a stage. <br />+  Improved the experience with Bluetooth devices. <br />+  Optimized SDK CPU and memory usage, and reduced the library size. <br />+  Added the `StageAudioManager` class, which can be used to set audio capture and playback parameters, including presets for voice communication, media playback and more. For details, see the new page, [IVS Broadcast SDK: Mobile Audio Modes](broadcast-mobile-audio-modes.md). <br />+  Added a new `requestQualityStats` function to display structured quality events from WebRTC stats. <br />+  Added a new function to update the audio bitrate. It is set on `LocalStageStream` objects just like the video configuration, but through a new audio configuration object.   | 
| [Android Broadcast SDK 1.13.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/android)+  All methods on the `StageRenderer` interface are now optional. <br />+  Added support to `Surfaceview`-based preview for better performance. The existing `getPreview` methods in `Session` and `StageStream` continue to return a subclass of `TextureView`, but this may change in a future SDK version.   If your application depends on `TextureView` specifically, you can continue with no changes. You also can switch from `getPreview` to `getPreviewTextureView` to prepare for the eventual change of what the default `getPreview` returns.   If your application does not require `TextureView` specifically, we recommend switching to `getPreviewSurfaceView` for lower CPU and memory usage.   <br />+  The SDK now implements a new type of preview called `ImagePreviewSurfaceTarget` which works with the application-provided Android Surface object. It is not a subclass of Android View, which provides better flexibility. <br />+  Fixed the case where `onFrame` callback for remote participant is called at the wrong time with the wrong size. <br />+  `SurfaceSource # getInputSurface` is now annotated with `@Nullable`. Your code should check it before using it. <br />+  Added `UserId` and `attributes` to `ParticipantInfo`. The `UserId` and `attributes` properties are embedded in the token and applications can retrieve them via `ParticipantInfo` whenever a participant joins. <br />+  Camera capture and preview rendering now defaults to 720 x 1280 or publish resolution (whichever is greater) at 15 fps. You can adjust the resolution and/or the fps using `StageVideoConfiguration # setCameraCaptureQuality`. <br />+  `IllegalArgumentException` thrown when setting configuration properties now includes the provided value in the exception message.  | 
| [iOS Broadcast SDK 1.13.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.13.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.13.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/ios)+  Fixed the issue where the SDK does not change video configuration if the video configuration is updated before publishing. <br />+  Incorporated the Google fix for a LibVPX security vulnerability (CVE-2023-5217). (Note that the Android SDK did not require any changes for this issue.) <br />+  Applications using other libraries that include `libWebRTC` will no longer have conflicts with the IVS Broadcast SDK. <br />+  All methods on the `IVSStageRenderer` protocol are now marked `@optional`. <br />+  Microphones and cameras returned by our SDKs now have a guaranteed sorting order, as documented in the SDKs themselves.  <br />+  Multiple cameras can now have a value of `true` for their `isDefault` property, one for each position as determined by the operating system. <br />+  Added `IVSStageAudioManager`, which allows precise control over the underlying `AVAudioSession` to enable a wider variety of use cases for Stages functionality. <br />+  Added `UserId` to `ParticipantInfo`.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-1130-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.17 MB | 13.00 MB | 
| armeabi-v7a | 4.48 MB | 9.04 MB | 
| x86\_64 | 5.35 MB | 13.80 MB | 
| x86 | 5.54 MB | 14.18 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-1130-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 3.45 MB | 7.84 MB | 

## November 16, 2023
<a name="nov16-23"></a>

### Composite Recording
<a name="server-side-composite-recording-rt"></a>

This new feature enables recording the composited view of an IVS Stage to an Amazon S3 bucket. For more information, see:
+ [Composite Recording](rt-composite-recording.md) – This is a new page. 
+ [Getting Started with IVS Real-Time Streaming](getting-started.md) – We added S3 endpoints to the policy in "Set Up IAM Permissions." 
+ [Service Quotas](service-quotas.md) – We added call-rate quotas for the new endpoints. 
+ [IVS Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html) – We added 4 StorageConfiguration endpoints and 7 objects (DestinationDetail, RecordingConfiguration, S3DestinationConfiguration, S3Detail, S3StorageConfiguration, StorageConfiguration, StorageConfigurationSummary). We also modified 3 objects (Composition, Destination, DestinationConfiguration); this affects the GetComposition response and the StartComposition request and response.

## November 16, 2023
<a name="nov16-23-rt"></a>

### Server-Side Composition
<a name="server-side-composition-rt"></a>

IVS server-side composition enables clients to offload the composition and broadcasting of an IVS stage to an IVS-managed service. Server-side composition and RTMP broadcast to a channel are invoked through IVS control plane endpoints in the stage’s home region. For more information, see:
+ [Getting Started with IVS Real-Time Streaming](getting-started.md) – We added SSC endpoints to the policy in "Set Up IAM Permissions."
+ [Using Amazon EventBridge with IVS Real-Time Streaming](eventbridge.md) – We added new metrics.
+ [Server-Side Composition](server-side-composition.md) – This new document includes an overview and setup instructions.
+ [Service Quotas (Real-Time Streaming)](service-quotas.md) – We added new call-rate limits and other quotas.
+ [Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html) – We added 8 Composition and EncoderConfiguration endpoints and 11 objects (ChannelDestinationConfiguration, Composition, CompositionSummary, Destination, DestinationConfiguration, DestinationSummary, EncoderConfiguration, EncoderConfigurationSummary, GridConfiguration, LayoutConfiguration, and Video).

In the *IVS Low-Latency Streaming User Guide*, see:
+ [Enabling Multiple Hosts on an IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html) – We added "Broadcasting a Stage: Client-Side versus Server-Side Composition" and updated "4. Broadcast the Stage."

## October 16, 2023
<a name="oct16-23-rt"></a>

### Amazon IVS Broadcast SDK: Web 1.6.0 (Real-Time Streaming)
<a name="oct16-23-rt-broadcast-160"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.6.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Improved Time-To-Video (TTV). <br />+  Added `maxAudioBitrate` configuration, supporting up to 128kbps of mono or stereo audio channels.  | 

## October 12, 2023
<a name="oct12-23"></a>

### New CloudWatch Metrics and Participant Data
<a name="cloudwatch-metrics-participant-data"></a>

We released CloudWatch metrics for IVS real-time streaming. For details, see [Monitoring IVS Real-Time Streaming](stage-health.md).

We also added six fields to the Participant API object: `browserName`, `browserVersion`, `ispName`, `osName`, `osVersion`, and `sdkVersion`. This affects the GetParticipant response. See the [IVS Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html).

## October 12, 2023
<a name="oct12-23-rt"></a>

### Amazon IVS Broadcast SDK: Android 1.12.1 (Real-Time Streaming)
<a name="oct12-23-rt-broadcast-android-1121"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Broadcast SDK 1.12.1](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.12.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.12.1/android)+  Fixed a bug where calling `BroadcastSession.setListener` resulted in an error.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-android-1121-sdk-size-android-rt"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.853 MB | 16.375 MB | 
| armeabi-v7a | 4.895 MB | 10.803 MB | 
| x86\_64 | 6.149 MB | 17.318 MB | 
| x86 | 6.328 MB | 17.186 MB | 

## September 14, 2023
<a name="sep14-23"></a>

### Amazon IVS Broadcast SDK: Web 1.5.2 (Real-Time Streaming)
<a name="sep14-23-broadcast-152-rt"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.5.2](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed a bug that prevented republishing with `refreshStrategy` when the published state enters an `ERRORED` state.  | 

## August 23, 2023
<a name="aug23-23_2"></a>

### Amazon IVS Broadcast SDK: Web 1.5.1, Android 1.12.0, and iOS 1.12.0 (Real-Time Streaming)
<a name="aug23-23_2-broadcast-151-1120-rt"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.5.1](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Fixed a bug with internal Maybe types on TypeScript 5. <br />+  Added better detection for Simulcast support. <br />+  Fixed two race conditions with `refreshStrategy` when trying to publish. <br />+  Fixed a race condition with `refreshStrategy` when trying to update participants to subscribe to.  | 
| All mobile (Android and iOS) |  +  Fixed a rare issue where publishing action is never completed. <br />+  Improved the stability of stages by reducing occurrences of rare crashes. <br />+  Improved the stability of stages by resolving race-condition issues caused by rapid join / leave. <br />+  Added a new `setOnFrameCallback` method on `ImageDevice`. This allows observation as frames pass through the device itself, giving insight into the aspect ratio of the latest images. This method also can be used to detect when the first frame is rendered for a remote participant in a stage.   | 
| [Android Broadcast SDK 1.12.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/android)+  Android 9 is now supported. <br />+  Improved CPU usage and performance.  | 
| [iOS Broadcast SDK 1.12.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.12.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.12.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/ios)+  Corrected the signature of `IVSDeviceDiscovery.createAudioSourceWithName` to return an `IVSCustomAudioSource` instead of `IVSCustomImageSource`.  | 

#### Broadcast SDK Size: Android
<a name="broadcast-151-1120-rt-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.853 MB | 16.375 MB | 
| armeabi-v7a | 4.895 MB | 10.803 MB | 
| x86\_64 | 6.149 MB | 17.318 MB | 
| x86 | 6.328 MB | 17.186 MB | 

#### Broadcast SDK Size: iOS
<a name="broadcast-151-1120-rt-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 5.06 MB | 10.92 MB | 

## August 7, 2023
<a name="aug07-23-broadcast"></a>

### Amazon IVS Broadcast SDK: Web 1.5.0, Android 1.11.0, and iOS 1.11.0
<a name="simulcast-ga"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Web Broadcast SDK 1.5.0](broadcast-web.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference)+  Added Simulcast – When enabled, this feature allows the publisher to send high- and low-quality layers of video. Subscribers automatically select their optimal quality based on their network conditions. See [Optimizing Media](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/web-publish-subscribe.html#web-publish-subscribe-optimizing-media).  | 
| All mobile (Android and iOS) | Added Simulcast – When enabled, this feature allows the publisher to send high- and low-quality layers of video. Subscribers automatically select their optimal quality based on their network conditions. See “Enable/Disable Layered Encoding with Simulcast” in the [Android](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/android-publish-subscribe.html#android-publish-subscribe-simulcast) and [iOS](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ios-publish-subscribe.html#ios-publish-subscribe-simulcast) Broadcast SDK Guides. | 
| [Android Broadcast SDK 1.11.0](broadcast-android.md) | **Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/android)+  Fixed an issue where creating many stages eventually results in a crash. (The exact number of stages depends on the device.)  | 
| [iOS Broadcast SDK 1.11.0](broadcast-ios.md) | **Download for real-time streaming: ** [https://broadcast.live-video.net/1.11.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.11.0/AmazonIVSBroadcast-Stages.xcframework.zip)<br />**Reference documentation:** [https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/ios)+  Corrected the signature of `IVSDeviceDiscovery.createAudioSourceWithName` to return `IVSCustomAudioSource` instead of `IVSCustomImageSource`.  | 

#### Broadcast SDK Size: Android
<a name="simulcast-ga-android-size"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64-v8a | 5.811 MB | 16.186 MB | 
| armeabi-v7a | 4.857 MB | 10.646 MB | 
| x86\_64 | 6.108 MB | 17.122 MB | 
| x86 | 6.289 MB | 16.994 MB | 

#### Broadcast SDK Size: iOS
<a name="simulcast-ga-ios-size"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| arm64 | 5.030 MB | 10.810 MB | 

## August 7, 2023
<a name="aug07-23-rt"></a>

### Real-Time Streaming
<a name="real-time-streaming-ga"></a>

Amazon Interactive Video Service (IVS) Real-Time Streaming enables you to deliver live streams with a latency that can be under 300 milliseconds from host to viewer.

Major documentation changes accompany this release. The [ IVS documentation landing page](https://docs.aws.amazon.com/ivs/) now has separate sections for real-time streaming and low-latency streaming. Each section has its own User Guide and API Reference. For documentation details, see the Document History (for both [real-time](doc-history.md) and [low-latency](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/doc-history.html) documentation changes). For real-time streaming, start with the [IVS Real-Time Streaming User Guide](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/what-is.html) and [IVS Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html).