# Amazon GameLift Streams Web SDK release notes

This page describes changes for each release of the Amazon GameLift Streams Web SDK.

## Version 1.2.0

- Improved device detection and support for some smart TVs.
- Made the `audioElement` input optional. Without it, audio is embedded in the provided video element.
  This simplifies media playback on devices that support only one media element at a time, such as certain smart TVs.

## Version 1.1.0

- Improved performance metrics reporting.
- Added a `maxStreamResolution` property to the stream configuration, which allows you to
  set the maximum resolution for the stream.
- Added a forced codec parameter that allows you to specify the video codec for the WebRTC connection.
- Improved Safari and iOS/iPadOS/tvOS web view compatibility.

## Version 1.0.0

General availability (GA) release of the Amazon GameLift Streams Web SDK with streaming support. This initial release provides
the core functionality for integrating Amazon GameLift Streams into web applications, including WebRTC-based game streaming,
input handling, and client connection management.
