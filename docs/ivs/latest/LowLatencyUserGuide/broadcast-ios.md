# IVS Broadcast SDK: iOS Guide | Low-Latency Streaming

The IVS Low-Latency Streaming iOS Broadcast SDK provides the interfaces required to
broadcast to Amazon IVS on iOS.

The `AmazonIVSBroadcast` module implements the interface described in this
document. The following operations are supported:

- Set up (initialize) a broadcast session.
- Manage broadcasting.
- Attach and detach input devices.
- Manage a composition session.
- Receive events.
- Receive errors.
  **Latest version of iOS broadcast SDK:** 1.37.0 ([Release Notes](release-notes.md#dec05-25-broadcast-mobile-ll "release-notes.md#dec05-25-broadcast-mobile-ll"))

**Reference documentation:** For information on the most
important methods available in the Amazon IVS iOS broadcast SDK, see the reference
documentation at [https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/1.37.0/ios/").

**Sample code:** See the iOS sample repository on GitHub:
[https://github.com/aws-samples/amazon-ivs-broadcast-ios-sample](https://github.com/aws-samples/amazon-ivs-broadcast-ios-sample "https://github.com/aws-samples/amazon-ivs-broadcast-ios-sample").

**Platform requirements:** iOS 14+

## How iOS Chooses Camera

Resolution and Frame Rate

The camera managed by the broadcast SDK optimizes its resolution and frame rate
(frames-per-second, or FPS) to minimize heat production and energy consumption. This
section explains how the resolution and frame rate are selected to help host
applications optimize for their use cases.

When attaching an `IVSCamera` to an `IVSBroadcastSession`,
the camera is optimized for a frame rate of
`IVSVideoConfiguration.targetFramerate` and a resolution of
`IVSVideoConfiguration.size`. These values are provided to the
`IVSBroadcastSession` on initialization.
