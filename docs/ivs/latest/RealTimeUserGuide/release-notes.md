# IVS Release Notes | Real-Time Streaming

This document contains all Amazon IVS Real-Time Streaming release notes, latest first,
organized by date of release.

## January 13, 2026

### Amazon IVS Broadcast SDK:

Android 1.38.0, iOS 1.38.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.38.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/android/")<br>• Layer prioritization function — Added `Priority`<br>enum to `StageVideoConfiguration.Layer` with<br>values: `VERY_LOW`, `LOW`,<br>`MEDIUM`, `HIGH`. This will<br>determine which layer is dropped first under network<br>bandwidth constraints.<br>• Faster stage reconnection after network connectivity<br>is restored.<br>• Changed the codes associated with some errors. See<br>[Mobile Broadcast SDK Error Migration Guide](#broadcast-1380-rt-sdk-error-migration "#broadcast-1380-rt-sdk-error-migration")<br>below.                                                                                                                                                                                                                                                                          |
| [iOS Broadcast SDK<br>1.38.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.38.0/ios/")<br>• Layer prioritization function — Added<br>`IVSLocalStageStreamLayerPriority` enum with values:<br>`VeryLow`, `Low`, `Medium`, `High`. This will determine which<br>layer is dropped first under network bandwidth<br>constraints.<br>• Faster stage reconnection after network connectivity is restored.<br>• Changed the codes associated with some errors. See<br>[Mobile Broadcast SDK Error Migration Guide](#broadcast-1380-rt-sdk-error-migration "#broadcast-1380-rt-sdk-error-migration")<br>below. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.795 MB        | 14.070 MB         |
| armeabi-v7a  | 5.021 MB        | 9.746 MB          |
| x86_64       | 5.904 MB        | 14.630 MB         |
| x86          | 6.161 MB        | 15.198 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.609 MB        | 8.078 MB          |

#### Mobile Broadcast SDK

Error Migration Guide

In version 1.38.0 of the iOS and Android broadcast SDKs, the codes associated
with some errors have changed. Previously, there was no single property that
could be used to uniquely identify any error emitted from the SDKs. Instead, to
understand what an error meant, a combination of the following properties needed
to be examined:

| Android                                                                                                                                                                    | iOS                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BroadcastException.getCode()`<br>`BroadcastException.getUid()`<br>`BroadcastException.getError()`<br>`BroadcastException.getSource()`<br>`BroadcastException.getDetail()` | `NSError.code`<br>`NSError.userInfo[IVSBroadcastUidDescriptionErrorKey]`<br>`NSError.userInfo[IVSBroadcastResultDescriptionErrorKey]`<br>`NSError.userInfo[IVSBroadcastSourceDescriptionErrorKey]`<br>`NSError.userInfo[NSLocalizedDescriptionKey]` |

With version 1.38.0 and greater, `BroadcastException.getCode()`
(Android) and `NSError.code` (iOS) return a unique ID that can be
looked up in the public `BroadcastErrorCode` (Android) and
`IVSBroadcastErrorCode` (iOS) enums.

In addition to making `code` the unique ID for all errors, an
additional field was added: `BroadcastException.getPlatformCode()`
(Android) and
`NSError.userInfo[IVSBroadcastPlatformCodeDescriptionErrorKey]`
(iOS). If an error is caused by the underlying platform (such as a network error
or a video encode or decode error), this field is non-zero and can be used to
collect additional information from the platform’s documentation.

##### Migrating from SDK 1.37.0 and Earlier

To make every error conform to the new strategy, some existing errors had
to change their values. Below is a guide to map existing logic to the new
logic:

- Any error where `code` was non-zero will keep the same
  value for code; however, referencing the code through the new enum
  constants may improve clarity. For example, comparing an error to
  `BroadcastErrorCode.Broadcast.LatencyThresholdReached`
  is clearer than comparing it to `20401`.
- Any error where `UID` had a value (i.e. was not
  `-1` on Android or `"-1"` on iOS) will now
  have the `code` field set to what the existing
  `UID` value was. If you have conditionals comparing
  the `UID` field, you can keep the constants but compare
  them against the `code` field going forward.
- Some legacy errors did not contain a `code` or a
  `UID` value. These were commonly matched based on the
  `message` (Android) or `description` (iOS)
  of the error, which is not a reliable way to identify errors because
  of the dynamic nature of error messages. Because these errors didn’t
  have uniquely identifying characteristics, one-to-one mappings can’t
  be provided. However, most errors kept the same description, so it
  is possible to continue using the same matching logic while also
  gathering and reporting the new `code` value for future
  app releases.

As a concrete example, the error checking in the following table should be
migrated as follows:

| Before                                          | After                                                                                                                                                                                                             |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `error.code == 20401`                           | `error.code ==<br>BroadcastErrorCode.Broadcast.LatencyThresholdReached`<br>No change, but prefer comparison to the enum<br>value.                                                                                 |
| `error.uid == 207`                              | `error.code ==<br>BroadcastErrorCode.Net.SocketRemoteHangup`<br>Compare to `code` instead of<br>`uid`.                                                                                                            |
| `error.message.contains("IceConnectionFailed")` | `error.code ==<br>BroadcastErrorCode.RealTime.PeerConnectionIceConnectionFailed`<br>Don’t compare to `message` (or<br>`source`, or `result/detail`).<br>Instead, find the appropriate enum code to compare<br>to. |

The most important part of an error is still
`BroadcastException.getPlatformCode()` (Android) and
`NSError.userInfo[IVSBroadcastPlatformCodeDescriptionErrorKey]`
(iOS), but in version 1.38.0 and beyond, the `code` field
uniquely identifies errors and allows immediate lookup of the error name and
description in the `BroadcastErrorCode` (Android) and
`IVSBroadcastErrorCode` (iOS) enums. As a result, other
fields like `UID`, `source`, and `detail`
should not be used in lookup logic; they exist only as supplemental
information.

## December 11, 2025

### Amazon IVS Broadcast SDK:

Android 1.37.1 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.37.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.37.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.37.1/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.37.1/android/")<br>• Fixed issues related to participant preview<br>teardown. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.754 MB        | 13.965 MB         |
| armeabi-v7a  | 4.991 MB        | 9.683 MB          |
| x86_64       | 5.858 MB        | 14.529 MB         |
| x86          | 6.128 MB        | 15.120 MB         |

## December 9, 2025

### Participant Token

Exchange

New support for participant token exchange enables you to upgrade or downgrade
token capabilities and update token attributes within the IVS client SDK without
forcing clients to disconnect and reconnect. This is useful for scenarios like
co-hosting, where participants may start with subscribe-only capabilities and later
need publish capabilities.

See the new page on [Token
Exchange](broadcast-mobile-token-exchange.md "broadcast-mobile-token-exchange.md").

## December 5, 2025

### IVS Broadcast SDK: Web 1.31.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.31.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Bug fixes and stability improvements. |

## December 5, 2025

### Amazon IVS Broadcast SDK:

Android 1.37.0, iOS 1.37.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.37.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/android/")<br>• Bug fixes and stability improvements.<br>• Added support for participant token exchange.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.37.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.37.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.37.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.37.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/")<br>• Bug fixes and stability improvements.<br>• Added support for participant token exchange. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.753 MB        | 13.961 MB         |
| armeabi-v7a  | 4.990 MB        | 9.680 MB          |
| x86_64       | 5.857 MB        | 14.525 MB         |
| x86          | 6.127 MB        | 15.116 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.588 MB        | 8.028 MB          |

## November 7, 2025

### Individual Participant

Recording Synchronization

New support for `EXT-X-PROGRAM-DATE-TIME` tags in individual
participant recording HLS playlists enables precise synchronization of multiple
participant recordings during post-processing. This feature provides
millisecond-accurate UTC timestamps at recording start and discontinuity points,
allowing you to create synchronized compositions (such as side-by-side or
picture-in-picture layouts) even when participants experience network interruptions
or join at different times. For details, see [Synchronize Multiple Participant
Recordings](rt-individual-participant-recording.md#ind-part-rec-sync-multiple "rt-individual-participant-recording.md#ind-part-rec-sync-multiple") in _Individual Participant
Recording_.

## October 30, 2025

### IVS Broadcast SDK: Web 1.30.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.30.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Bug fixes and stability improvements. |

## October 30, 2025

### Amazon IVS Broadcast SDK:

Android 1.36.0, iOS 1.36.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.36.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/android/")<br>• Improved camera recovery when returning to the<br>foreground after being in the background for a prolonged<br>period of time.<br>• Added an `embedMessage` method on<br>`ImageDevice` to enable the insertion of<br>metadata payloads into a publishing video stream. See<br>[Embed Messages](android-publish-subscribe.md#android-publish-subscribe-embed-messages "android-publish-subscribe.md#android-publish-subscribe-embed-messages") in the _Android<br>Broadcast SDK Guide_.                                                                                                                                        |
| [iOS Broadcast SDK<br>1.36.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.36.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.36.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.36.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.36.0/ios/")<br>• Added an `embedMessage` method on<br>`IVSImageDevice` to enable the insertion<br>of metadata payloads into a publishing video stream. See<br>[Embed Messages](ios-publish-subscribe.md#ios-publish-subscribe-embed-messages "ios-publish-subscribe.md#ios-publish-subscribe-embed-messages") in the _iOS<br>Broadcast SDK Guide_. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.736 MB        | 13.898 MB         |
| armeabi-v7a  | 4.974 MB        | 9.638 MB          |
| x86_64       | 5.839 MB        | 14.456 MB         |
| x86          | 6.109 MB        | 15.047 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.569 MB        | 7.962 MB          |

## October 14, 2025

### Updated Real-Time Limit:

Compositions

We updated the quota for "maximum concurrent Composition resources per account"
from 5 to 20. It is documented in Service Quotas > [Other
Quotas](service-quotas.md#quotas-other "service-quotas.md#quotas-other").

## October 2, 2025

### IVS Broadcast SDK: Web 1.29.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.29.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Bug fixes and stability improvements. |

## October 2, 2025

### Amazon IVS Broadcast SDK:

Android 1.35.0, iOS 1.35.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Android Broadcast SDK<br>1.35.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/android/")<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [iOS Broadcast SDK<br>1.35.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.35.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.35.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.35.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.35.0/ios/")<br>• `IVSImageDevice.setOnFrameCallback` can now<br>be customized with a `DispatchQueue`, and it<br>can optionally include the `CVPixelBuffer`<br>associated with the frame. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.730 MB        | 13.900 MB         |
| armeabi-v7a  | 4.971 MB        | 9.639 MB          |
| x86_64       | 5.835 MB        | 14.455 MB         |
| x86          | 6.104 MB        | 15.041 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.569 MB        | 7.963 MB          |

## September 16, 2025

### Server-Side Composition

Custom Participant Ordering

New support for custom participant ordering for SSC provides granular control over
participant positioning in both grid and Picture-in-Picture (PiP) layouts. See
[Server-Side
Composition](server-side-composition.md "server-side-composition.md") (various changes, including adding
`participantOrderAttribute` and "Custom Participant Ordering") and
the [IVS Real-Time Streaming API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md") (added
`participantOrderAttribute` to the Composition object).

## September 11, 2025

### Amazon IVS Broadcast SDK:

Android 1.34.0, iOS 1.34.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.34.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/android/")<br>• CPU improvements for publish and subscribe media<br>transport.<br>• Added `packetsLost` to<br>`LocalVideoStats` and<br>`LocalAudioStats`.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [iOS Broadcast SDK<br>1.34.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.34.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.34.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.34.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.34.0/ios/")<br>• CPU improvements for publish and subscribe media<br>transport.<br>• Added `packetsLost` to<br>`IVSLocalVideoStats` and<br>`IVSLocalAudioStats`.<br>• Fixed a bug where devices did not detach after leaving<br>a stage, which could result in privacy indicators<br>unexpectedly being lit. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.796 MB        | 14.089 MB         |
| armeabi-v7a  | 5.036 MB        | 9.788 MB          |
| x86_64       | 5.906 MB        | 14.653 MB         |
| x86          | 6.174 MB        | 15.240 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.594 MB        | 8.046 MB          |

## September 10, 2025

### Interface VPC

Endpoints

New support for interface VPC (Virtual Private Cloud) endpoints enables you to
establish a secure private connection between your Amazon VPC and IVS, for workloads
that require secure, live video ingestion. This keeps your IVS ingest traffic within
the AWS network and off the public internet. Interface VPC endpoints are powered by
AWS PrivateLink, an AWS technology that enables private communication between AWS
services, using an elastic network interface with private IPs in your Amazon VPC.
See [Private
Ingest](../LowLatencyUserGuide/private-ingest-ll.md "../LowLatencyUserGuide/private-ingest-ll.md") in the _IVS Low-Latency Streaming User
Guide_ and [Private Ingest to Stages](rt-rtmp-publishing.md#private-ingest-stages "rt-rtmp-publishing.md#private-ingest-stages") in the _IVS Real-Time
Streaming User Guide_.

## September 4, 2025

### IVS Broadcast SDK: Web 1.28.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.28.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Joining a stage that was deleted, or with a<br>participant token that was disconnected, now reports<br>`STAGE_DELETED` or<br>`STAGE_DISCONNECTED` errors instead of<br>`TIMEOUT`.<br>• Optimized internal polling requests related to<br>simulcast. |

## August 7, 2025

### IVS Broadcast SDK: Web 1.27.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.27.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added `requestQualityStats` to<br>`RemoteStageStream`, which then exposes a<br>simplified object of video and audio stats sourced from<br>`requestRTCStats`.<br>• Updates to ensure that the<br>`RemoteStageStream` muted state and its<br>`mediaStreamTrack` enabled state are<br>always in sync. |

## August 7, 2025

### Amazon IVS Broadcast SDK:

Android 1.33.0, iOS 1.33.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.33.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/android/")<br>• New methods to control device torch:<br>+ `CameraSource.Capabilities`<br>implements `isTorchSupported`.<br>+ `CameraSource.Options.Builder`<br>implements `setEnableTorch`.<br>• The Android broadcast SDK meets Google Play’s [16 KB page-size compatibility requirement](https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html "https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html").<br>(Note: This was implemented as of version 1.23.0 of the<br>SDK.)                                                                                                                                                   |
| [iOS Broadcast SDK<br>1.33.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.33.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.33.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.33.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.33.0/ios/")<br>• New method to control device torch:<br>`IVSImageDevice` implements two<br>properties, `isTorchSupported` and<br>`torchEnabled`. Check if the device<br>supports torch with `isTorchSupported`, and<br>then toggle it by setting<br>`torchEnabled`.<br>• Resolved an issue on iOS 18.5+ with certain VPNs that<br>could result in peer connection timeouts. (Note: This<br>was implemented as of version 1.32.1 of the SDK.) |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.689 MB        | 13.829 MB         |
| armeabi-v7a  | 4.962 MB        | 9.649 MB          |
| x86_64       | 5.806 MB        | 14.413 MB         |
| x86          | 6.066 MB        | 14.983 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.505 MB        | 7.828 MB          |

## July 25, 2025

### Amazon IVS Broadcast SDK:

Android 1.32.2 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.32.2](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.32.2/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.32.2/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.32.2/android/")<br>• Disabled IPv6 for `Stage`<br>connections. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.693 MB        | 13.838 MB         |
| armeabi-v7a  | 4.964 MB        | 9.653 MB          |
| x86_64       | 5.810 MB        | 14.422 MB         |
| x86          | 6.067 MB        | 14.988 MB         |

## July 23, 2025

### Enforcement of New Real-Time

Metrics and Limits: Concurrent Publishers and Subscriptions

On [June 23](#jun23-25-rt-concurrent-limits "#jun23-25-rt-concurrent-limits"), we introduced two
new adjustable service quotas, for the maximum number of concurrent publishers and
concurrent subscriptions across all stages in an AWS Region. Today we start
enforcing these new quotas.

## July 15, 2025

### New Real-Time Limit:

Concurrent Participant Replications

We've introduced a new non-adjustable service quota, for the maximum number of
concurrent replications per participant across all stages in an AWS Region. It is
documented in Service Quotas > [Other
Quotas](service-quotas.md#quotas-other "service-quotas.md#quotas-other").

## July 10, 2025

### Amazon IVS Broadcast SDK:

Android 1.32.1, iOS 1.32.1 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.32.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/android/")<br>• Removed<br>`StageAudioConfiguration.enableEchoCancellation()`.<br>Instead, use `StageAudioManager` to enable or<br>disable echo cancellation.<br>• Modified the `STUDIO` and<br>`SUBSCRIBE_ONLY` presets in<br>`StageAudioManager` to turn off echo<br>cancellation. If you want to use `STUDIO`<br>with echo cancellation, first set the preset, then<br>enable echo cancellation to override<br>`STUDIO`'s default preference for no echo<br>cancellation.<br>• Added a `MixedDevice` API suite for<br>compositing multiple image and audio sources into a<br>single output `Device`, which can be used for<br>publishing more complex audio and visuals to a<br>stage. |
| [iOS Broadcast SDK<br>1.32.1](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.32.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.32.1/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.32.1/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.32.1/ios/")<br>• Added an `IVSMixedDevice` API suite for<br>compositing multiple image and audio sources into a<br>single output `IVSDevice`, which can be used<br>for publishing more complex audio and visuals to a<br>stage.                                                                                                                                                                 |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.692 MB        | 13.840 MB         |
| armeabi-v7a  | 4.965 MB        | 9.655 MB          |
| x86_64       | 5.810 MB        | 14.424 MB         |
| x86          | 6.068 MB        | 14.990 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.508 MB        | 7.900 MB          |

## July 7, 2025

### IVS Broadcast SDK: Web 1.26.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.26.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added `requestQualityStats` to<br>LocalStageStream, which exposes a simplified object of<br>video and audio stats sourced from<br>requestRTCStats.<br>• Fixed websocket leaks that could occur during setup,<br>causing subsequent join failures.<br>• Fixed an issue where 1302 errors would incorrectly<br>surface when retrying a failed subscribe or publish<br>operation.<br>• Improved retry stability for subscribe and publish<br>connections when the join connection is in an ERRORED or<br>CONNECTING state. |

## June 23, 2025

### New Real-Time Metrics and

Limits: Concurrent Publishers and Subscriptions

We've introduced two new adjustable service quotas, for the maximum number of
concurrent publishers and concurrent subscriptions across all stages in an AWS
Region. They are documented in Service Quotas > [Other
Quotas](service-quotas.md#quotas-other "service-quotas.md#quotas-other"). These quotas give you more control over total usage across your
account. Previously, IVS enforced limits only on the number of publishers and
subscribers _per stage_. This made it hard to set safeguards at
the account level and could result in higher usage and associated costs than
expected, especially for customers creating many stages.

**Note:** We will start enforcing these new quotas on
July 23, to allow 30 days for you to review your usage and request service-quota
increases if needed.

We also added two new CloudWatch metrics, `ConcurrentPublishers` and
`ConcurrentSubscriptions`. These metrics help you monitor usage
across all stages and assess whether you are approaching the default limits. They
are documented in Monitoring Real-Time Streaming > [CloudWatch Metrics](stage-health.md#stage-health-cloudwatch-metrics "stage-health.md#stage-health-cloudwatch-metrics"). We recommend setting up [CloudWatch alarms](../../../servicequotas/latest/userguide/configure-cloudwatch.md "../../../servicequotas/latest/userguide/configure-cloudwatch.md") to alert you when your usage is close to a quota
limit.

## June 20, 2025

### E-RTMP Multitrack Video Ingest

Support

You can use E-RTMP (Enhanced Real-Time Messaging Protocol) multitrack video to
send multiple video qualities to your IVS stages. This feature enables adaptive
bitrate streaming, allowing viewers to watch in the best quality for their network
connection. See [E-RTMP Multitrack Video](rt-rtmp-publishing.md#rtmp-multitrack "rt-rtmp-publishing.md#rtmp-multitrack") in the IVS RTMP Publishing
documentation.

## June 16, 2025

### IVS Broadcast SDK: Web 1.25.1

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.25.1](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Removed the NPM unintentional engine enforcement of<br>v22. All LTS node versions are supported as the package<br>is transpiled. |

## June 12, 2025

### Amazon IVS Broadcast SDK:

Android 1.31.0, iOS 1.31.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.31.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/android/")<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.31.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.31.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.31.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.31.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.31.0/ios/")<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.579 MB        | 13.594 MB         |
| armeabi-v7a  | 4.864 MB        | 9.473 MB          |
| x86_64       | 5.697 MB        | 14.173 MB         |
| x86          | 5.951 MB        | 14.724 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.431 MB        | 7.732 MB          |

## June 12, 2025

### IVS Broadcast SDK: Web 1.25.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.25.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed a bug where SEI messages might fail to send<br>after a remote participant encountered an<br>`ERROR` state.<br>• Fixed a bug where multiple remote stage streams might<br>be returned when the<br>`STAGE_STREAM_MUTE_CHANGED` stage event<br>was invoked.<br>• Fixed a bug where<br>`STAGE_PARTICIPANT_STREAMS_REMOVED` was<br>not invoked for streams that had errored. |

## May 29, 2025

### Participant Replication

Participant replication allows you to copy a participant from one stage to
another. This is useful when you want the same participant to appear in multiple
stages at the same time, enabling cross-stage interactions. For documentation
changes, see the [Document History](doc-history.md "doc-history.md") (both User
Guide and API Reference tables).

## May 26, 2025

### Amazon IVS Broadcast SDK:

Android 1.30.1 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Android Broadcast SDK<br>1.30.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.30.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.30.1/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.30.1/android/")<br>• Fixed a low-microphone-volume bug on some Android<br>devices when using SDK-managed microphones from<br>`DeviceDiscovery` with the<br>`STUDIO` audio preset. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.579 MB        | 13.592 MB         |
| armeabi-v7a  | 4.863 MB        | 9.472 MB          |
| x86_64       | 5.696 MB        | 14.171 MB         |
| x86          | 5.950 MB        | 14.722 MB         |

## May 15, 2025

### IVS Broadcast SDK: Web 1.24.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.24.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed memory leaks when leaving and rejoining a<br>stage. |

## May 15, 2025

### Amazon IVS Broadcast SDK:

Android 1.30.0, iOS 1.30.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.30.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/android/")<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.30.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.30.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.30.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.30.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.30.0/ios/")<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.571 MB        | 13.577 MB         |
| armeabi-v7a  | 4.857 MB        | 9.462 MB          |
| x86_64       | 5.691 MB        | 14.156 MB         |
| x86          | 5.944 MB        | 14.708 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.430 MB        | 7.732 MB          |

## May 2, 2025

### IVS Broadcast SDK: Web 1.23.1

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.23.1](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed an issue where participant join events always<br>occurred before `join()` resolved.<br>• Fixed an issue where local participants were<br>erroneously reported as remote participants when leaving<br>and rejoining in quick succession. |

## April 17, 2025

### Amazon IVS Broadcast SDK:

Android 1.29.0, iOS 1.29.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.29.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/android/")<br>• Added a simulcast publisher controls feature. See<br>"Configuring Layered Encoding (Publisher)" in the [Android Broadcast SDK Guide](android-publish-subscribe.md#android-layered-encoding-simulcast-configure-publisher "android-publish-subscribe.md#android-layered-encoding-simulcast-configure-publisher").<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                        |
| [iOS Broadcast SDK<br>1.29.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.29.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.29.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.29.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.29.0/ios/")<br>• Added a simulcast publisher controls feature. See<br>"Configuring Layered Encoding (Publisher)" in the [iOS Broadcast SDK Guide](ios-publish-subscribe.md#ios-layered-encoding-simulcast-configure-publisher "ios-publish-subscribe.md#ios-layered-encoding-simulcast-configure-publisher").<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.566 MB        | 13.546 MB         |
| armeabi-v7a  | 4.853 MB        | 9.444 MB          |
| x86_64       | 5.681 MB        | 14.119 MB         |
| x86          | 5.939 MB        | 14.674 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.429 MB        | 7.715 MB          |

## April 17, 2025

### IVS Broadcast SDK: Web 1.23.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Web Broadcast SDK<br>1.23.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added a simulcast publisher controls feature. See<br>"Configuring Layered Encoding (Publisher)" in the [Web Broadcast SDK Guide](web-publish-subscribe.md#web-layered-encoding-simulcast-configure-publisher "web-publish-subscribe.md#web-layered-encoding-simulcast-configure-publisher").<br>• Improved time to publish latency. This impacts the<br>timing of the `PUBLISHED` event.<br>• Fixed a bug where the SDK fired join category errors<br>via the [ERROR](broadcast-web-error-handling.md "broadcast-web-error-handling.md") callback when connection to the stage<br>was lost but potentially recoverable (specifically,<br>`FAILED` and `TIMEOUT` errors<br>for the `JOIN_ERROR` category).<br>• Fixed a bug with the `insertSeiMessage`<br>operation where a strategy refresh could result in<br>subsequent invocations of `insertSeiMessage`<br>failing to send the SEI message. |

## April 2, 2025

### New Quota: Compositions Per Stage

We added a new quota, for the maximum concurrent compositions allowed per stage.
This is documented in Service Quotas > [Other
Quotas](service-quotas.md#quotas-other "service-quotas.md#quotas-other").

## March 20, 2025

### Amazon IVS Broadcast SDK:

Android 1.28.1, iOS 1.28.1 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.28.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/android/")<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.28.1](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.28.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.28.1/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.28.1/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.28.1/ios/")<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.613 MB        | 13.760 MB         |
| armeabi-v7a  | 4.885 MB        | 9.558 MB          |
| x86_64       | 5.728 MB        | 14.342 MB         |
| x86          | 5.987 MB        | 14.923 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.417 MB        | 7.698 MB          |

## March 20, 2025

### IVS Broadcast SDK: Web 1.22.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.22.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added `null` as a valid return type to the<br>[preferredLayerForStream](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/StageStrategy#preferredlayerforstream "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/StageStrategy#preferredlayerforstream") strategy<br>method.<br>• Fixed a bug where `preferredLayerForStream`<br>was not called again if new layers became available<br>after the stream started.<br>• Fixed a bug where<br>`stream.getHighestQualityLayer` did not<br>pick the highest quality layer after the stream<br>started. |

## March 19, 2025

### Amazon IVS Broadcast SDK:

Android 1.27.2, iOS 1.27.2 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.27.2](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/android/")<br>• Fixed a resource-leak regression that impacted some<br>devices when creating 50 or more stages.<br>• Fixed a regression that could cause an increased rate<br>of video freezes when using third-party publishing<br>software.                                                                                                                                                                                       |
| [iOS Broadcast SDK<br>1.27.2](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.27.2/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.27.2/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.27.2/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.27.2/ios/")<br>• Fixed a regression that could cause an increased rate<br>of video freezes when using third-party publishing<br>software. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.700 MB        | 14.197 MB         |
| armeabi-v7a  | 4.945 MB        | 9.879 MB          |
| x86_64       | 5.810 MB        | 14.802 MB         |
| x86          | 6.073 MB        | 15.412 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.622 MB        | 8.584 MB          |

## March 13, 2025

### Target Segment Duration

This release adds to the IVS real-time streaming API, to allow you to define the
target duration for recorded segments generated when either using composite
recording or recording a stage participant. For specific API changes, see the [Document History](doc-history.md "doc-history.md") (both User Guide and API Reference
tables).

## March 6, 2025

### Individual Participant Recording

Stitching

This is the first release of new functionality. If your stage is configured for
individual participant recording, you can now specify a window of time during which,
if a stage publisher disconnects from a stage and then reconnects, IVS tries to
record to the same S3 prefix as the previous session. In other words, if a publisher
disconnects and then reconnects within the specified interval, the multiple
recordings are considered a single recording and merged. For documentation changes,
see the [Document History](doc-history.md "doc-history.md") (both the User Guide and
API Reference tables).

## March 3, 2025

### Amazon IVS Broadcast SDK: iOS

1.27.1 (Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [iOS Broadcast SDK<br>1.27.1](broadcast-ios.md "broadcast-ios.md") | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.27.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.27.1/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.27.1/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.27.1/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.1/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.27.1/ios/")<br>• Improved focus performance for objects held close to<br>the camera while using the ultra-wide lens on Pro<br>devices. |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.625 MB        | 8.601 MB          |

## February 20, 2025

### Amazon IVS Broadcast SDK:

Android 1.27.0, iOS 1.27.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.27.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/android/")<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.27.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.27.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.27.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.27.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.27.0/ios/")<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.700 MB        | 14.197 MB         |
| armeabi-v7a  | 4.944 MB        | 9.879 MB          |
| x86_64       | 5.809 MB        | 14.802 MB         |
| x86          | 6.073 MB        | 15.412 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.625 MB        | 8.601 MB          |

## February 20, 2025

### IVS Broadcast SDK: Web 1.21.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.21.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Updated `preferredLayerForStream` strategy<br>types to include `null`, which is a valid<br>return.<br>• Fixed TypeScript compile errors when TSconfig<br>`skipLibCheck` is set to false.<br>Note: As part of this release, types have been<br>consolidated into a single rollup. If an application<br>imports nested types based on path, errors may occur. If<br>errors do occur, change the import to simply<br>`'amazon-ivs-broadcast'`. |

## January 30, 2025

### Amazon IVS Broadcast SDK: Android

1.26.0, iOS 1.26.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.26.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/android/")<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.26.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.26.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.26.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.26.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.26.0/ios/")<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.695 MB        | 14.186 MB         |
| armeabi-v7a  | 4.939 MB        | 9.872 MB          |
| x86_64       | 5.804 MB        | 14.790 MB         |
| x86          | 6.065 MB        | 15.398 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.624 MB        | 8.601 MB          |

## January 23, 2025

### IVS Broadcast SDK: Web 1.20.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.20.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added the `insertSeiMessage` method on<br>LocalStageStream to enable the insertion of Supplemental<br>Enhancement Information (SEI) payloads into a publishing<br>video stream. See [Supplemental Enhanced Information](web-publish-subscribe.md#web-publish-subscribe-sei-attributes "web-publish-subscribe.md#web-publish-subscribe-sei-attributes") in the<br>_IVS Broadcast SDK: Web<br>Guide_. |

## December 12, 2024

### Amazon IVS Broadcast SDK: Android

1.25.0, iOS 1.25.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.25.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/android/")<br>• Added a simulcast controls feature. See [Configuring Layered Encoding with Simulcast<br>(Subscriber)](real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber "real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber") in _Streaming<br>Optimizations_.<br>• Made SEI (Supplemental Enhanced Information) payloads<br>available to subscribers with a new field on<br>ImageDeviceFrame objects. See [Get Supplemental Enhancement Information<br>(SEI)](android-publish-subscribe.md#android-publish-subscribe-sei-attributes "android-publish-subscribe.md#android-publish-subscribe-sei-attributes") in the _IVS Broadcast SDK:<br>Android Guide_.<br>• Added the<br>`SubscribeConfiguration::setInitialGain`<br>method to allow the configuration of the initial gain<br>value for incoming audio streams.<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                             |
| [iOS Broadcast SDK<br>1.25.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.25.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.25.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.25.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.25.0/ios/")<br>• Added a simulcast controls feature. See [Configuring Layered Encoding with Simulcast<br>(Subscriber)](real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber "real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber") in _Streaming<br>Optimizations_.<br>• Made SEI (Supplemental Enhanced Information) payloads<br>available to subscribers with a new field on<br>IVSImageDeviceFrame objects. See [Get<br>Supplemental Enhancement Information (SEI)](ios-publish-subscribe.md#ios-publish-subscribe-sei-attributes "ios-publish-subscribe.md#ios-publish-subscribe-sei-attributes") in<br>the _IVS Broadcast SDK: iOS<br>Guide_.<br>• Added the<br>`IVSSubscribeConfiguration.initialGain`<br>method to allow the configuration of the initial gain<br>value for incoming audio streams.<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.677 MB        | 14.103 MB         |
| armeabi-v7a  | 4.905 MB        | 9.791 MB          |
| x86_64       | 5.786 MB        | 14.725 MB         |
| x86          | 6.030 MB        | 15.302 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.625 MB        | 8.585 MB          |

## December 12, 2024

### IVS Broadcast SDK: Web 1.19.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Web Broadcast SDK<br>1.19.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added a simulcast controls feature. See [Configuring Layered Encoding with Simulcast<br>(Subscriber)](real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber "real-time-streaming-optimization.md#real-time-streaming-optimization-simulcast-subscriber") in _Streaming<br>Optimizations_.<br>• Bug fixes and stability improvements. |

## December 10, 2024

### Real-Time Streaming Thumbnail

Configuration

This release allows you to enable/disable the recording of thumbnails for a live
session and modify the interval at which thumbnails are generated for the live
session. This is the first release of this new functionality. See:

- [Individual Participant
  Recording](rt-individual-participant-recording.md "rt-individual-participant-recording.md") — We updated examples and JSON metadata
  information, and we added pricing information and "Thumbnail-Only
  Recordings."
- [Composite Recording](rt-composite-recording.md "rt-composite-recording.md") —
  We updated examples and JSON metadata information, and we added pricing
  information.
- [API Reference
  RT](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md") — We made several changes:
  - Modified the S3DestinationConfiguration object: added
    `thumbnailConfigurations`. This affects the
    GetComposition response and StartComposition request and
    response.
  - Modified the AutoParticipantRecordingConfiguration object: added
    `thumbnailConfiguration` and added `NONE`
    as a valid value for `mediaTypes`. This affects the
    CreateStage request and response, GetStage response, and UpdateStage
    request and response.
  - Added two objects: CompositionThumbnailConfiguration and
    ParticipantThumbnailConfiguration.

## November 13, 2024

### Amazon IVS Broadcast SDK: Android

1.24.0, iOS 1.24.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.24.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/android/")<br>• Bug fixes and stability improvements.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.24.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.24.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.24.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.24.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.24.0/ios/")<br>• Bug fixes and stability improvements. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.521 MB        | 13.791 MB         |
| armeabi-v7a  | 4.789 MB        | 9.623 MB          |
| x86_64       | 5.718 MB        | 14.709 MB         |
| x86          | 5.933 MB        | 15.163 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.589 MB        | 8.466 MB          |

## November 12, 2024

### IVS Broadcast SDK: Web 1.18.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.18.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added a new event to make SEI (Supplemental Enhanced<br>Information) payloads available to subscribers.<br>• Fixed an exception that would occur during unpublish<br>and unsubscribe requests.<br>• Fixed a race condition where joining and leaving<br>rapidly would cause an error for other<br>participants. |

## October 10, 2024

### IVS Broadcast SDK: Web 1.17.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.17.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Minor bug fixes. |

## October 10, 2024

### Amazon IVS Broadcast SDK: Android

1.23.0, iOS 1.23.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.23.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/android/")<br>• With this release we also began publishing a version<br>of the Android broadcast SDK which includes debug<br>symbols. See [Using the SDK with Debug Symbols](broadcast-android-getting-started.md#broadcast-android-using-debug-symbols-rt "broadcast-android-getting-started.md#broadcast-android-using-debug-symbols-rt").<br>• Minor bug fixes. |
| [iOS Broadcast SDK<br>1.23.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.23.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.23.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.23.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.23.0/ios/")<br>• Minor bug fixes.                                        |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.432 MB        | 13.560 MB         |
| armeabi-v7a  | 4.707 MB        | 9.451 MB          |
| x86_64       | 5.626 MB        | 14.459 MB         |
| x86          | 5.838 MB        | 14.908 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.542 MB        | 8.316 MB          |

## September 11, 2024

### Amazon IVS Broadcast SDK: Android

1.22.0, iOS 1.22.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.22.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/android/")<br>• Fixed a bug where certain Android devices show a black<br>frame in the preview after switching camera<br>inputs.<br>• Minor bug fixes.                                                                                                                                                                      |
| [iOS Broadcast SDK<br>1.22.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.22.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.22.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.22.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.22.0/ios/")<br>• Minor bug fixes. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.359 MB        | 13.392 MB         |
| armeabi-v7a  | 4.636 MB        | 9.325 MB          |
| x86_64       | 5.548 MB        | 14.268 MB         |
| x86          | 5.754 MB        | 14.710 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.488 MB        | 8.199 MB          |

## September 11, 2024

### IVS Broadcast SDK: Web 1.16.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.16.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Minor bug fixes. |

## September 9, 2024

### RTMP Ingest

As an alternative to using the IVS broadcast SDK, you can now publish video to an
IVS stage from an RTMP source (in addition to WHIP, which already was supported).
For documentation changes, see the [Document
History](doc-history.md "doc-history.md") (both the User Guide and API Reference tables).

## August 19, 2024

### In-Console Publish/Subscribe

You can now publish and subscribe from the IVS console. In _Getting
Started with IVS Real-Time Streaming_, see [Publish and Subscribe to Video](getting-started-pub-sub.md "getting-started-pub-sub.md").

## August 15, 2024

### IVS Broadcast SDK: Web 1.15.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.15.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed a race condition that impacts publisher media<br>quality when `join()` is called repeatedly.<br>Calling `join()` in succession no longer<br>re-triggers the `STAGE_PARTICIPANT_JOINED`<br>event, along with accompanying publish and stream state<br>changes.<br>• Fixed a bug that causes issues parsing participant<br>tokens when non-text characters are used in the token<br>`attributes` field.<br>• Added a method to configure a participant's<br>subscribers. Initially, you can configure only the<br>jitter-buffer minimum delay. See the SDK reference<br>documentation, [Configuration for Subscribing to<br>Participants](web-publish-subscribe.md#web-publish-subscribe-concepts-strategy-participants-config "web-publish-subscribe.md#web-publish-subscribe-concepts-strategy-participants-config") in the _Web Broadcast<br>SDK Guide_, and [Changing Subscriber Jitter Buffer MinDelay](real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay "real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay")<br>in _Streaming Optimizations_. |

## August 15, 2024

### Amazon IVS Broadcast SDK: Android

1.21.0, iOS 1.21.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.21.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/android/](https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/android/")<br>• Fixed a bug impacting devices with MT6765 chipsets,<br>where the subscriber preview renders black frames under<br>some circumstances.<br>• Added a method to configure a participant's<br>subscribers. Initially, you can configure only the<br>jitter-buffer minimum delay. See the SDK reference<br>documentation, [Configuration for Subscribing to<br>Participants](android-publish-subscribe.md#android-publish-subscribe-concepts-strategy-participants-config "android-publish-subscribe.md#android-publish-subscribe-concepts-strategy-participants-config") in the _Android<br>Broadcast SDK Guide_, and [Changing Subscriber Jitter Buffer MinDelay](real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay "real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay")<br>in _Streaming Optimizations_.<br>• Minor bug fixes.                                                                                                                             |
| [iOS Broadcast SDK<br>1.21.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.21.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.21.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.21.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.21.0/ios/")<br>• Added a method to configure a participant's<br>subscribers. Initially, you can configure only the<br>jitter-buffer minimum delay. See the SDK reference<br>documentation, [Configuration for Subscribing to<br>Participants](ios-publish-subscribe.md#ios-publish-subscribe-concepts-strategy-participants-config "ios-publish-subscribe.md#ios-publish-subscribe-concepts-strategy-participants-config") in the _iOS Broadcast<br>SDK Guide_, and [Changing Subscriber Jitter Buffer MinDelay](real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay "real-time-streaming-optimization.md#real-time-streaming-jitter-buffer-min-delay")<br>in _Streaming Optimizations_.<br>• Minor bug fixes. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.350 MB        | 13.378 MB         |
| armeabi-v7a  | 4.628 MB        | 9.312 MB          |
| x86_64       | 5.538 MB        | 14.253 MB         |
| x86          | 5.744 MB        | 14.694 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.485 MB        | 8.199 MB          |

## July 18, 2024

### IVS Broadcast SDK: Web 1.14.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.14.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• API documentation improvements.<br>• Fixed video and audio stats outliers reported during<br>connection resets.<br>• Minor dependency updates. |

## July 18, 2024

### Amazon IVS Broadcast SDK: Android

1.20.0, iOS 1.20.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.20.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/android")<br>• Fixed a bug that prevented the Broadcast SDK from<br>running on Chromebooks with Intel processors.<br>• Minor bug fixes.                                                                                                                                                                                    |
| [iOS Broadcast SDK<br>1.20.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.20.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.20.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.20.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.20.0/ios")<br>• Minor bug fixes. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.318 MB        | 13.299 MB         |
| armeabi-v7a  | 4.605 MB        | 9.254 MB          |
| x86_64       | 5.507 MB        | 14.168 MB         |
| x86          | 5.715 MB        | 14.608 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.465 MB        | 8.164 MB          |

## June 26, 2024

### Generate Participant Tokens with a Key

Pair

You can now generate participant tokens on your own server application by using a
key pair. This enables you to avoid calling CreateParticipantToken every time you
need a participant token. For documentation changes, see the [Document History](doc-history.md "doc-history.md") (both the User Guide and API
Reference tables).

## June 20, 2024

### Individual Participant

Recording

Individual participant recording allows IVS real-time streaming customers to
record IVS stage publishers individually into S3 buckets. See [Recording](rt-recording.md "rt-recording.md"), [Individual Participant
Recording](rt-individual-participant-recording.md "rt-individual-participant-recording.md"), and changes in the [Real-Time Streaming API
Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md"). (For specific documentation changes, see the [Document History](doc-history.md "doc-history.md").)

## June 13, 2024

### Amazon IVS Broadcast SDK: Android

1.19.0, iOS 1.19.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Android Broadcast SDK<br>1.19.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/android")<br>• Recent Android versions require an icon in the<br>notification that is displayed when capturing the<br>screen. If desired, you can now customize the icon by<br>calling `setSmallIcon` on the<br>`Notification.Builder` returned by<br>`Session #<br>createServiceNotificationBuilder`.<br>• Improved connection recovery time on devices<br>transitioning from wifi to cellular connections. This<br>change requires the `CHANGE_NETWORK_STATE`<br>permission. |
| [iOS Broadcast SDK<br>1.19.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.19.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.19.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.19.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.19.0/ios")<br>• Minor bug fixes.                                                                                                                                                     |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.304 MB        | 13.340 MB         |
| armeabi-v7a  | 4.598 MB        | 9.299 MB          |
| x86_64       | 5.495 MB        | 14.207 MB         |
| x86          | 5.694 MB        | 14.625 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.393 MB        | 7.949 MB          |

## June 13, 2024

### IVS Broadcast SDK: Web 1.13.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.13.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Updated the duration of event change behavior for<br>`StageEvents.STAGE_PARTICIPANT_SUBSCRIBE_STATE_CHANGED`<br>and<br>`StageEvents.STAGE_PARTICIPANT_PUBLISH_STATE_CHANGED`.<br>Participants now remain in the<br>`ATTEMPTING_SUBSCRIBE` or<br>`ATTEMPTING_PUBLISH` state for a longer<br>time, until the `ERRORED` event is<br>fired.<br>• Added the `StageEvents.ERROR` event for<br>listening to errors encountered by the SDK. See [Error<br>Handling](broadcast-web-error-handling.md "broadcast-web-error-handling.md") in the \*Real-Time Broadcast<br>SDK: Web Guide<br>• for more<br>information. |

## May 20, 2024

### IVS Broadcast SDK: Web 1.12.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Web Broadcast SDK<br>1.12.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Improved retry handling for publish and subscribe<br>operations.<br>• Improved analytics, specifically latency and<br>audio-quality measurement. |

## May 16, 2024

### Amazon IVS Broadcast SDK: Android

1.18.0, iOS 1.18.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Android Broadcast SDK<br>1.18.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/android")<br>• The SDK now sends specific error codes when a<br>connected Stage is deleted by the AWS control plane, or<br>when the token in use is revoked.<br>• Minor bug fixes.                                                                                                                                                                                                                                                                                                                                                                                 |
| [iOS Broadcast SDK<br>1.18.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.18.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.18.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.18.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.18.0/ios")<br>• The SDK now sends specific error codes when a<br>connected Stage is deleted by the AWS control plane, or<br>when the token in use is revoked.<br>• Added the IVSCamera `setVideoZoomFactor`<br>method and the associated `IVSCameraDelegate`<br>methods. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.275 MB        | 13.279 MB         |
| armeabi-v7a  | 4.573 MB        | 9.254 MB          |
| x86_64       | 5.472 MB        | 14.142 MB         |
| x86          | 5.664 MB        | 14.554 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.393 MB        | 7.916 MB          |

## May 6, 2024

### IVS Broadcast SDK: Web 1.11.0

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.11.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed an edge case where the SDK did not attempt to<br>recover on a stage `DISCONNECT`.<br>• Updated the error message for a `join()`<br>timeout error. Instead of "InitialConnectTimedOut after<br>10 seconds," the SDK now returns "Operation timed<br>out." |

## April 30, 2024

### IVS Broadcast SDK: Web 1.10.1

(Real-Time Streaming)

| Platform                                                           | Downloads and Changes                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.10.1](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Minor bug fixes. |

## April 30, 2024

### Amazon IVS Broadcast SDK: Android 1.15.2,

iOS 1.15.2 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.15.2](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/android")<br>• Minor bug fixes. Upgrade to this version only if you<br>have a specific reason to do so; otherwise, use the<br>highest version that is released.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.15.2](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.15.2/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.15.2/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.15.2/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.15.2/ios")<br>• Minor bug fixes. Upgrade to this version only if you<br>have a specific reason to do so; otherwise, use the<br>highest version that is released. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.244 MB        | 13.198 MB         |
| armeabi-v7a  | 4.543 MB        | 9.192 MB          |
| x86_64       | 5.437 MB        | 14.051 MB         |
| x86          | 5.631 MB        | 14.461 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.359 MB        | 7.836 MB          |

## April 22, 2024

### Amazon IVS Broadcast SDK: Android

1.17.0, iOS 1.17.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.17.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/android")<br>• Fixed a rare crash that can occur while<br>publishing.                                                                                                                                                                                                                                                                                                                                     |
| [iOS Broadcast SDK<br>1.17.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.17.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.17.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.17.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.17.0/ios")<br>• The `AmazonIVSBroadcast` framework now<br>includes a privacy manifest, as required by<br>Apple. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.273 MB        | 13.275 MB         |
| armeabi-v7a  | 4.571 MB        | 9.251 MB          |
| x86_64       | 5.468 MB        | 14.137 MB         |
| x86          | 5.662 MB        | 14.549 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.388 MB        | 7.916 MB          |

## March 21, 2024

### Amazon IVS Broadcast SDK: Android

1.16.0, iOS 1.16.0, Web 1.10.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.10.0](broadcast-web.md "broadcast-web.md")             | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed an intermittent error when cleaning up<br>connections after unsubscribing or leaving a<br>stage.                                                                                                                                                                                             |
| [Android Broadcast SDK<br>1.16.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/android")<br>• Fixed a previews freeze on the Exynos variant of<br>Samsung devices with Android 14.<br>• Added a function for querying camera zoom capabilities<br>and setting the zoom factor.                                                                                                                            |
| [iOS Broadcast SDK<br>1.16.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.16.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.16.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.16.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.16.0/ios")<br>• Minor bug fixes. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.253 MB        | 13.21 MB          |
| armeabi-v7a  | 4.551 MB        | 9.204 MB          |
| x86_64       | 5.447 MB        | 14.070 MB         |
| x86          | 5.640 MB        | 14.480 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.361 MB        | 7.836 MB          |

## March 13, 2024

### Amazon IVS Broadcast SDK: Android

1.15.1, iOS 1.15.1 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.15.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/android")<br>• Fixed a rare crash when subscribing to a remote<br>participant.                                                                                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.15.1](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.15.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.15.1/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.15.1/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.15.1/ios")<br>• Fixed a rare crash when subscribing to a remote<br>participant. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.243 MB        | 13.194 MB         |
| armeabi-v7a  | 4.541 MB        | 9.188 MB          |
| x86_64       | 5.628 MB        | 14.455 MB         |
| x86          | 5.434 MB        | 14.046 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.358 MB        | 7.820 MB          |

## March 13, 2024

### Server-Side Composition API

Updates

We introduced new properties to the GridConfiguration and a new picture-in-picture
layout, enhancing the customization options for compositions. For specific
documentation changes, see the [Document History](doc-history.md "doc-history.md")
(see the table of API Reference changes).

**Important**: Ensure your application does not
depend on the specific features of the current layout, such as size and position of
tiles. _Visual improvements to layouts can be introduced at
any time_.

## March 8, 2024

### Server-Side Composition Layout

Updates

Today we enabled the changes to the default grid layout that are described in the
[February 7, 2024](#feb07-24-rt "#feb07-24-rt") entry.

## February 22, 2024

### Amazon IVS Broadcast SDK: Android

1.15.0, iOS 1.15.0, Web 1.9.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.9.0](broadcast-web.md "broadcast-web.md")              | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Improved internal error handling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Android Broadcast SDK<br>1.15.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/android")<br>• Minor bug fixes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [iOS Broadcast SDK<br>1.15.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.15.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.15.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.15.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.15.0/ios")<br>• Added an `AVPictureInPictureController`<br>extension to allow creating a new instance with an<br>`IVSImagePreviewView`.<br>• Added a new API on `IVSImageDevice` to<br>create an `AVSampleBufferDisplayLayer` to<br>which the device renders.<br>• Fixed a low bitrate issue on devices running iOS 17<br>and later.<br>• Minor bug fixes. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.243 MB        | 13.194 MB         |
| armeabi-v7a  | 4.541 MB        | 9.188 MB          |
| x86_64       | 5.628 MB        | 14.455 MB         |
| x86          | 5.434 MB        | 14.046 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.358 MB        | 7.820 MB          |

## February 7, 2024

### Server-Side Composition Layout

Updates

This release introduces visual improvements to the default grid layout. These
changes will optimize how video is displayed and reduce blank space. These changes
will be enabled on March 7, 2024.

**Important**: Ensure your application does not
depend on the specific features of the current layout, such as size and position of
tiles. _Visual improvements to layouts can be introduced at
any time_.

| Description of the Change                                                                                                                    | Old                                                                                                    | New                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Automatically selects the optimal placement of participants to<br>maximize video size.                                                       | Two colored rectangles labeled with numbers 1 and 2, representing a simple choice or option selection. | Two colored rectangles labeled with numbers: pink rectangle with "1" and blue rectangle with "2".       |
| Enhances space utilization by reducing gaps and minimizing<br>black bars.                                                                    | Five colored rectangles numbered 1 to 5, arranged in two rows on a black background.                   | Colored rectangles numbered 1 to 5 arranged in a grid-like pattern.                                     |
| Adds a new “camera off” indicator for clear visibility of<br>participants not sharing video.                                                 | AWS Management Console interface showing the IAM dashboard with user management options.               | Muted video icon displayed in three separate sections on a dark background.                             |
| Improves space utilization and proportions for portrait use<br>cases.                                                                        | Two colored rectangles labeled with numbers 1 and 2, representing a comparison or choice.              | Two colored rectangles labeled with numbers 1 and 2, representing a simple diagram or interface layout. |
| Enhances space utilization in portrait use cases by minimizing<br>spacing between participants and reducing letterboxing or<br>pillarboxing. | Three colored rectangles labeled with numbers 1, 2, and 3 arranged vertically.                         | Three horizontal color blocks numbered 1 to 3, in red, blue, and yellow from top to bottom.             |

## February 6, 2024

### OBS and WHIP Support

IVS can be used with WHIP-compatible encoders like OBS to publish to IVS real-time
streaming. WHIP (WebRTC-HTTP Ingestion Protocol) is an IETF draft developed to
standardize WebRTC ingestion. See the new page on [OBS and WHIP Support](obs-whip-support.md "obs-whip-support.md").

## February 1, 2024

### Amazon IVS Broadcast SDK: Android

1.14.1, iOS 1.14.1, Web 1.8.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.8.0](broadcast-web.md "broadcast-web.md")              | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Layered encoding with simulcast is now disabled by<br>default.<br>• Fixed an issue where a Stage instance would not<br>cleanly disconnect when a Stage was deleted, or when a<br>participant was disconnected from the server. The SDK<br>now emits a `STAGE_CONNECTION_STATE_CHANGED`<br>event with a state of `DISCONNECTED` (instead<br>of `ERRORED` and then<br>`CONNECTING`).<br>• Fixed issue where publishing would fail when updating<br>the strategy with empty audio or video tracks.                                                                                                                                                                                                         |
| [Android Broadcast SDK<br>1.14.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/android")<br>• Layered encoding with simulcast is now disabled by<br>default.<br>• Updated `libWebRTC` from M108 to<br>M119.<br>• Fixed several crashes to improve overall<br>stability.<br>• Added support for stereo publishing. This can be<br>enabled through the `StageAudioConfiguration`<br>object.<br>• Fixed a bug causing a black feed from participants<br>after joining a session.<br>• Updated internal `libWebRTC` references to<br>avoid symbol conflicts when other `libWebRTC`<br>versions are included in the same host<br>application.                                                                                                                                                                       |
| [iOS Broadcast SDK<br>1.14.1](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.14.1/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.14.1/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.14.1/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.14.1/ios")<br>• Layered encoding with simulcast is now disabled by<br>default.<br>• Updated `libWebRTC` from M108 to<br>M119.<br>• Fixed several crashes to improve overall<br>stability.<br>• Added support for stereo publishing. This can be<br>enabled through<br>`IVSLocalStageStreamAudioConfiguration`.<br>• Fixed a crash when enabling audio-only mode for other<br>participants.<br>• Improved TTV and reduced binary size. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.223 MB        | 13.118 MB         |
| armeabi-v7a  | 4.524 MB        | 9.134 MB          |
| x86_64       | 5.418 MB        | 13.955 MB         |
| x86          | 5.61 MB         | 14.369 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.350 MB        | 7.790 MB          |

## January 3, 2024

### Amazon IVS Broadcast SDK: Android

1.13.4, iOS 1.13.4, Web 1.7.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.7.0](broadcast-web.md "broadcast-web.md")              | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Improved time-to-video for subscribers joining<br>stages.<br>• Removed the `minAudioBitrateKbps` property<br>(it was unused).<br>• Improved network recovery during internet outages or<br>changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Android Broadcast SDK<br>1.13.4](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/android")<br>• StageAudioConfiguration now supports setting whether<br>echo cancellation should be enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [iOS Broadcast SDK<br>1.13.4](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.13.4/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.13.4/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.13.4/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.13.4/ios")<br>• On iOS, we improved the audio engine for both<br>recording and playback with a focus on stability and<br>recoverability. This enhances support for route changes<br>while in use, improves battery recovery for edge cases,<br>and reduces the amount of main thread blocking.<br>• Fixed an issue where the microphone might stay active<br>even after it was detached from a stage, leaving the iOS<br>privacy indicator on. (The SDK was not processing<br>incoming audio at the time.) |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.187 MB        | 13.025 MB         |
| armeabi-v7a  | 4.491 MB        | 9.056 MB          |
| x86_64       | 5.359 MB        | 13.829 MB         |
| x86          | 5.553 MB        | 14.214 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.45 MB         | 7.84 MB           |

## December 7, 2023

### New CloudWatch Metrics

We renamed the PacketLoss (Stage) metric to be DownloadPacketLoss (Stage). We also
released additional CloudWatch metrics for IVS real-time streaming:

- DownloadPacketLoss (Stage,Participant)
- DroppedFrames (Stage,Participant)
- SubscribeBitrate (Stage,Participant,MediaType)

For details, see [Monitoring IVS Real-Time
Streaming](stage-health.md "stage-health.md").

## December 4, 2023

### Amazon IVS Broadcast SDK: Android

1.13.2 and iOS 1.13.2 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| All mobile (Android and iOS)                                                   | • Noise-suppression configuration is available for<br>developers to enable/disable for publishing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Android Broadcast SDK<br>1.13.2](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/android")<br>• Improved the time it takes to load the video (TTV)<br>when joining the first stage in a session.                                                                                                                                                                                                                            |
| [iOS Broadcast SDK<br>1.13.2](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.13.2/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.13.2/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.13.2/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.13.2/ios")<br>• No changes in the real-time SDK. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.177 MB        | 13.01 MB          |
| armeabi-v7a  | 4.485 MB        | 9.045 MB          |
| x86_64       | 5.352 MB        | 13.808 MB         |
| x86          | 5.547 MB        | 14.192 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.45 MB         | 7.82 MB           |

## November 21, 2023

### Amazon IVS Broadcast SDK:

Android 1.13.1 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.13.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.13.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.1/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.13.1/android")<br>• Fixed an issue that caused a crash when quickly<br>leaving, releasing, and rejoining the same stage. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.177 MB        | 13.102 MB         |
| armeabi-v7a  | 4.485 MB        | 9.046 MB          |
| x86_64       | 5.353 MB        | 13.809 MB         |
| x86          | 5.547 MB        | 14.192 MB         |

## November 17, 2023

### Amazon IVS Broadcast SDK: Android

1.13.0 and iOS 1.13.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All mobile (Android and iOS)                                                   | • Updated [Streaming<br>Optimizations](real-time-streaming-optimization.md "real-time-streaming-optimization.md"). Among other things, the<br>"Adaptive Streaming: Layered Encoding with Simulcast"<br>feature now requires explicit opt-in and is supported<br>only in recent versions of the SDK.<br>• Improved the stability of stages by reducing<br>occurrences of rare crashes.<br>• Improved the time it takes to load the video (TTV)<br>when joining a stage.<br>• Improved the experience with Bluetooth devices.<br>• Optimized SDK CPU and memory usage, and reduced the<br>library size.<br>• Added the `StageAudioManager` class, which<br>can be used to set audio capture and playback<br>parameters, including presets for voice communication,<br>media playback and more. For details, see the new page,<br>[IVS<br>Broadcast SDK: Mobile Audio Modes](broadcast-mobile-audio-modes.md "broadcast-mobile-audio-modes.md").<br>• Added a new `requestQualityStats` function<br>to display structured quality events from WebRTC<br>stats.<br>• Added a new function to update the audio bitrate. It<br>is set on `LocalStageStream` objects just<br>like the video configuration, but through a new audio<br>configuration object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Android Broadcast SDK<br>1.13.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/android")<br>• All methods on the `StageRenderer`<br>interface are now optional.<br>• Added support to `Surfaceview`-based<br>preview for better performance. The existing<br>`getPreview` methods in<br>`Session` and `StageStream`<br>continue to return a subclass of<br>`TextureView`, but this may change in a<br>future SDK version.<br>+ If your application depends on<br>`TextureView` specifically, you can<br>continue with no changes. You also can switch from<br>`getPreview` to<br>`getPreviewTextureView` to prepare for<br>the eventual change of what the default<br>`getPreview` returns.<br>+ If your application does not require<br>`TextureView` specifically, we<br>recommend switching to<br>`getPreviewSurfaceView` for lower CPU<br>and memory usage.<br>• The SDK now implements a new type of preview called<br>`ImagePreviewSurfaceTarget` which works<br>with the application-provided Android Surface object. It<br>is not a subclass of Android View, which provides better<br>flexibility.<br>• Fixed the case where `onFrame` callback for<br>remote participant is called at the wrong time with the<br>wrong size.<br>• `SurfaceSource # getInputSurface` is now<br>annotated with `@Nullable`. Your code should<br>check it before using it.<br>• Added `UserId` and `attributes`<br>to `ParticipantInfo`. The `UserId`<br>and `attributes` properties are embedded in<br>the token and applications can retrieve them via<br>`ParticipantInfo` whenever a participant<br>joins.<br>• Camera capture and preview rendering now defaults to<br>720 x 1280 or publish resolution (whichever is greater)<br>at 15 fps. You can adjust the resolution and/or the fps<br>using `StageVideoConfiguration #<br>setCameraCaptureQuality`.<br>• `IllegalArgumentException` thrown when<br>setting configuration properties now includes the<br>provided value in the exception message. |
| [iOS Broadcast SDK<br>1.13.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.13.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.13.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.13.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.13.0/ios")<br>• Fixed the issue where the SDK does not change video<br>configuration if the video configuration is updated<br>before publishing.<br>• Incorporated the Google fix for a LibVPX security<br>vulnerability (CVE-2023-5217). (Note that the Android<br>SDK did not require any changes for this issue.)<br>• Applications using other libraries that include<br>`libWebRTC` will no longer have conflicts<br>with the IVS Broadcast SDK.<br>• All methods on the `IVSStageRenderer`<br>protocol are now marked `@optional`.<br>• Microphones and cameras returned by our SDKs now have<br>a guaranteed sorting order, as documented in the SDKs<br>themselves.<br>• Multiple cameras can now have a value of<br>`true` for their `isDefault`<br>property, one for each position as determined by the<br>operating system.<br>• Added `IVSStageAudioManager`, which allows<br>precise control over the underlying<br>`AVAudioSession` to enable a wider<br>variety of use cases for Stages functionality.<br>• Added `UserId` to<br>`ParticipantInfo`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.17 MB         | 13.00 MB          |
| armeabi-v7a  | 4.48 MB         | 9.04 MB           |
| x86_64       | 5.35 MB         | 13.80 MB          |
| x86          | 5.54 MB         | 14.18 MB          |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 3.45 MB         | 7.84 MB           |

## November 16, 2023

### Composite Recording

This new feature enables recording the composited view of an IVS Stage to an
Amazon S3 bucket. For more information, see:

- [Composite Recording](rt-composite-recording.md "rt-composite-recording.md") – This
  is a new page.
- [Getting Started with IVS Real-Time
  Streaming](getting-started.md "getting-started.md") – We added S3 endpoints to the policy in "Set Up IAM
  Permissions."
- [Service Quotas](service-quotas.md "service-quotas.md") – We added call-rate
  quotas for the new endpoints.
- [IVS Real-Time
  Streaming API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md") – We added 4 StorageConfiguration
  endpoints and 7 objects (DestinationDetail, RecordingConfiguration,
  S3DestinationConfiguration, S3Detail, S3StorageConfiguration,
  StorageConfiguration, StorageConfigurationSummary). We also modified 3
  objects (Composition, Destination, DestinationConfiguration); this affects
  the GetComposition response and the StartComposition request and
  response.

## November 16, 2023

### Server-Side Composition

IVS server-side composition enables clients to offload the composition and
broadcasting of an IVS stage to an IVS-managed service. Server-side composition and
RTMP broadcast to a channel are invoked through IVS control plane endpoints in the
stage’s home region. For more information, see:

- [Getting Started with IVS Real-Time
  Streaming](getting-started.md "getting-started.md") – We added SSC endpoints to the policy in "Set Up IAM
  Permissions."
- [Using Amazon EventBridge with IVS Real-Time
  Streaming](eventbridge.md "eventbridge.md") – We added new metrics.
- [Server-Side Composition](server-side-composition.md "server-side-composition.md") –
  This new document includes an overview and setup instructions.
- [Service Quotas (Real-Time Streaming)](service-quotas.md "service-quotas.md")
  – We added new call-rate limits and other quotas.
- [Real-Time Streaming
  API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md") – We added 8 Composition and EncoderConfiguration
  endpoints and 11 objects (ChannelDestinationConfiguration, Composition,
  CompositionSummary, Destination, DestinationConfiguration,
  DestinationSummary, EncoderConfiguration, EncoderConfigurationSummary,
  GridConfiguration, LayoutConfiguration, and Video).

In the _IVS Low-Latency Streaming User Guide_,
see:

- [Enabling
  Multiple Hosts on an IVS Stream](../LowLatencyUserGuide/multiple-hosts.md "../LowLatencyUserGuide/multiple-hosts.md") – We added "Broadcasting a
  Stage: Client-Side versus Server-Side Composition" and updated "4. Broadcast
  the Stage."

## October 16, 2023

### Amazon IVS Broadcast SDK: Web 1.6.0

(Real-Time Streaming)

| Platform                                                          | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Web Broadcast SDK<br>1.6.0](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Improved Time-To-Video (TTV).<br>• Added `maxAudioBitrate` configuration,<br>supporting up to 128kbps of mono or stereo audio<br>channels. |

## October 12, 2023

### New CloudWatch Metrics and

Participant Data

We released CloudWatch metrics for IVS real-time streaming. For details, see [Monitoring IVS Real-Time Streaming](stage-health.md "stage-health.md").

We also added six fields to the Participant API object: `browserName`,
`browserVersion`, `ispName`, `osName`,
`osVersion`, and `sdkVersion`. This affects the
GetParticipant response. See the [IVS Real-Time Streaming API
Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md").

## October 12, 2023

### Amazon IVS Broadcast SDK:

Android 1.12.1 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Broadcast SDK<br>1.12.1](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.12.1/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.12.1/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.12.1/android")<br>• Fixed a bug where calling<br>`BroadcastSession.setListener` resulted<br>in an error. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.853 MB        | 16.375 MB         |
| armeabi-v7a  | 4.895 MB        | 10.803 MB         |
| x86_64       | 6.149 MB        | 17.318 MB         |
| x86          | 6.328 MB        | 17.186 MB         |

## September 14, 2023

### Amazon IVS Broadcast SDK: Web 1.5.2

(Real-Time Streaming)

| Platform                                                          | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Web Broadcast SDK<br>1.5.2](broadcast-web.md "broadcast-web.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed a bug that prevented republishing with<br>`refreshStrategy` when the published<br>state enters an `ERRORED` state. |

## August 23, 2023

### Amazon IVS Broadcast SDK: Web

1.5.1, Android 1.12.0, and iOS 1.12.0 (Real-Time Streaming)

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.5.1](broadcast-web.md "broadcast-web.md")              | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Fixed a bug with internal Maybe types on TypeScript<br>5.<br>• Added better detection for Simulcast support.<br>• Fixed two race conditions with<br>`refreshStrategy` when trying to<br>publish.<br>• Fixed a race condition with<br>`refreshStrategy` when trying to update<br>participants to subscribe to.                                                                                                                               |
| All mobile (Android and iOS)                                                   | • Fixed a rare issue where publishing action is never<br>completed.<br>• Improved the stability of stages by reducing<br>occurrences of rare crashes.<br>• Improved the stability of stages by resolving<br>race-condition issues caused by rapid join /<br>leave.<br>• Added a new `setOnFrameCallback` method on<br>`ImageDevice`. This allows observation as<br>frames pass through the device itself, giving insight<br>into the aspect ratio of the latest images. This method<br>also can be used to detect when the first frame is<br>rendered for a remote participant in a stage.                                                                                                  |
| [Android Broadcast SDK<br>1.12.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/android")<br>• Android 9 is now supported.<br>• Improved CPU usage and performance.                                                                                                                                                                                                                                                                                                                                                                                 |
| [iOS Broadcast SDK<br>1.12.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.12.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.12.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.12.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.12.0/ios")<br>• Corrected the signature of<br>`IVSDeviceDiscovery.createAudioSourceWithName`<br>to return an `IVSCustomAudioSource` instead<br>of `IVSCustomImageSource`. |

#### Broadcast SDK Size:

Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.853 MB        | 16.375 MB         |
| armeabi-v7a  | 4.895 MB        | 10.803 MB         |
| x86_64       | 6.149 MB        | 17.318 MB         |
| x86          | 6.328 MB        | 17.186 MB         |

#### Broadcast SDK Size:

iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 5.06 MB         | 10.92 MB          |

## August 7, 2023

### Amazon IVS Broadcast SDK: Web 1.5.0, Android 1.11.0,

and iOS 1.11.0

| Platform                                                                       | Downloads and Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web Broadcast SDK<br>1.5.0](broadcast-web.md "broadcast-web.md")              | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")<br>• Added Simulcast – When enabled, this feature allows<br>the publisher to send high<br>• and low-quality layers of<br>video. Subscribers automatically select their optimal<br>quality based on their network conditions. See [Optimizing Media](web-publish-subscribe.md#web-publish-subscribe-optimizing-media "web-publish-subscribe.md#web-publish-subscribe-optimizing-media").                                                       |
| All mobile (Android and iOS)                                                   | Added Simulcast – When enabled, this feature allows the<br>publisher to send high<br>• and low-quality layers of video.<br>Subscribers automatically select their optimal quality based on<br>their network conditions. See “Enable/Disable Layered Encoding<br>with Simulcast” in the [Android](android-publish-subscribe.md#android-publish-subscribe-simulcast "android-publish-subscribe.md#android-publish-subscribe-simulcast") and [iOS](ios-publish-subscribe.md#ios-publish-subscribe-simulcast "ios-publish-subscribe.md#ios-publish-subscribe-simulcast") Broadcast SDK Guides.                                                                                               |
| [Android Broadcast SDK<br>1.11.0](broadcast-android.md "broadcast-android.md") | **Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/android](https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/android "https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/android")<br>• Fixed an issue where creating many stages eventually<br>results in a crash. (The exact number of stages depends<br>on the device.)                                                                                                                                                                                                                                                                                                                |
| [iOS Broadcast SDK<br>1.11.0](broadcast-ios.md "broadcast-ios.md")             | **Download for real-time streaming:**<br>[https://broadcast.live-video.net/1.11.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.11.0/AmazonIVSBroadcast-Stages.xcframework.zip "https://broadcast.live-video.net/1.11.0/AmazonIVSBroadcast-Stages.xcframework.zip")<br>**Reference documentation:**<br>[https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/ios](https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/ios "https://aws.github.io/amazon-ivs-broadcast-docs/1.11.0/ios")<br>• Corrected the signature of<br>`IVSDeviceDiscovery.createAudioSourceWithName`<br>to return `IVSCustomAudioSource` instead of<br>`IVSCustomImageSource`. |

#### Broadcast SDK Size: Android

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64-v8a    | 5.811 MB        | 16.186 MB         |
| armeabi-v7a  | 4.857 MB        | 10.646 MB         |
| x86_64       | 6.108 MB        | 17.122 MB         |
| x86          | 6.289 MB        | 16.994 MB         |

#### Broadcast SDK Size: iOS

| Architecture | Compressed Size | Uncompressed Size |
| ------------ | --------------- | ----------------- |
| arm64        | 5.030 MB        | 10.810 MB         |

## August 7, 2023

### Real-Time Streaming

Amazon Interactive Video Service (IVS) Real-Time Streaming enables you to deliver
live streams with a latency that can be under 300 milliseconds from host to
viewer.

Major documentation changes accompany this release. The [IVS documentation landing page](../../../ivs.md "../../../ivs.md")
now has separate sections for real-time streaming and low-latency streaming. Each
section has its own User Guide and API Reference. For documentation details, see the
Document History (for both [real-time](doc-history.md "doc-history.md") and [low-latency](../LowLatencyUserGuide/doc-history.md "../LowLatencyUserGuide/doc-history.md") documentation changes). For real-time streaming, start with
the [IVS
Real-Time Streaming User Guide](what-is.md "what-is.md") and [IVS Real-Time Streaming API
Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md").
