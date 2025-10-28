# Known Issues & Workarounds in the

IVS Android Broadcast SDK | Real-Time Streaming ​

This document lists known issues that you might encounter when using the Amazon IVS
real-time streaming Android broadcast SDK and suggests potential workarounds.

- When an Android device goes to sleep and wakes up, it is possible for the
  preview to be in a frozen state.

**Workaround:** Create and use a new
`Stage`.

- When a participant joins with a token that is being used by another
  participant, the first connection is disconnected without a specific
  error.

**Workaround:** None.

- There is a rare issue where the publisher is publishing but the publish state
  that subscribers receive is `inactive`.

**Workaround:** Try leaving and then joining the
session. If the issue remains, create a new token for the publisher.

- A rare audio-distortion issue may occur intermittently during a stage session,
  typically on calls of longer durations.

**Workaround:** The participant with distorted
audio can either leave and rejoin the session, or unpublish and republish their
audio to fix the issue.

- External microphones are not supported when publishing to a stage.

**Workaround:** Do not use an external microphone
connected via USB for publishing to a stage.

- Publishing to a stage with screen share using
  `createSystemCaptureSources` is not supported.

**Workaround:** Manage the system capture
manually, using custom image-input sources and custom audio-input
sources.

- When an `ImagePreviewView` is removed from a parent (e.g.,
  `removeView()` is called at the parent), the
  `ImagePreviewView` is released immediately. The
  `ImagePreviewView` does not show any frames when it is added to
  another parent view.

**Workaround:** Request another preview using
`getPreview`.

- When joining a stage with a Samsung Galaxy S22/+ with Android 12, you may
  encounter a 1401 error and the local device fails to join the stage or joins but
  has no audio.

**Workaround:** Upgrade to Android 13.

- When joining a stage with a Nokia X20 on Android 13, the camera may fail to
  open and an exception is thrown.

**Workaround:** None.

- Devices with the MediaTek Helio chipset may not render video of remote
  participants properly.

**Workaround:** None.

- On a few devices, the device OS may choose a different microphone than what’s
  selected through the SDK. This is because the Amazon IVS Broadcast SDK cannot
  control how the `VOICE_COMMUNICATION` audio route is defined, as it
  varies according to different device manufacturers.

**Workaround:** None.

- Some Android video encoders cannot be configured with a video size less than
  176x176. Configuring a smaller size causes an error and prevents
  streaming.

**Workaround:** Do not configure the video size
to be less than 176x176.
