# Known Issues & Workarounds in the IVS

Web Broadcast SDK | Real-Time Streaming

This document lists known issues that you might encounter when using the Amazon IVS
real-time streaming Web broadcast SDK and suggests potential workarounds.

- When closing browser tabs or exiting browsers without calling
  `stage.leave()`, users can still appear in the session with a
  frozen frame or black screen for up to 10 seconds.

**Workaround:** None.

- Safari sessions intermittently appear with a black screen to users joining
  after a session has begun.

**Workaround:** Refresh the browser and reconnect
the session.

- Safari does not recover gracefully from switching networks.

**Workaround:** Refresh the browser and reconnect
the session.

- The developer console repeats an `Error: UnintentionalError at
StageSocket.onClose` error.

**Workaround:** Only one stage can be created per
participant token. This error occurs when more than one `Stage`
instance is created with the same participant token, regardless of whether the
instance is on one device or multiple devices.

- You may have trouble maintaining a
  `StageParticipantPublishState.PUBLISHED` state and may receive
  repeated `StageParticipantPublishState.ATTEMPTING_PUBLISH` states
  when listening to the
  `StageEvents.STAGE_PARTICIPANT_PUBLISH_STATE_CHANGED`
  event.

**Workaround:** Constrain video resolution to
720p when invoking `getUserMedia` or `getDisplayMedia`.
Specifically, your `getUserMedia` and `getDisplayMedia`
constraint values for width and height must not exceed 921600 (1280\*720) when
multiplied together.

- When `stage.leave()` is invoked or a remote participant leaves, a
  404 DELETE error appears in the browser's debug console.

**Workaround:** None. This is a harmless
error.

## Safari Limitations

- Denying a permissions prompt requires resetting the permission
  in Safari website settings at the OS level.
- Safari does not natively detect all devices as effectively as
  Firefox or Chrome. For example, OBS Virtual Camera does not get
  detected.

## Firefox Limitations

- System permissions need to be enabled for Firefox to screen
  share. After enabling them, the user must restart Firefox for it to work
  correctly; otherwise, if permissions are perceived as blocked, the browser
  will throw a [NotFoundError](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia#exceptions "https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia#exceptions") exception.
- The `getCapabilities` method is missing. This means
  users cannot get the media track's resolution or aspect ratio. See this
  [bugzilla thread](https://bugzilla.mozilla.org/show_bug.cgi?id=1179084 "https://bugzilla.mozilla.org/show_bug.cgi?id=1179084").
- Several `AudioContext` properties are missing; e.g.,
  latency and channel count. This could pose a problem for advanced users who
  want to manipulate the audio tracks.

- Camera feeds from `getUserMedia` are restricted to a
  4:3 aspect ratio on MacOS. See [bugzilla
  thread 1](https://bugzilla.mozilla.org/show_bug.cgi?id=1193640 "https://bugzilla.mozilla.org/show_bug.cgi?id=1193640") and [bugzilla
  thread 2](https://bugzilla.mozilla.org/show_bug.cgi?id=1306034 "https://bugzilla.mozilla.org/show_bug.cgi?id=1306034").

- Audio capture is not supported with
  `getDisplayMedia`. See this [bugzilla
  thread](https://bugzilla.mozilla.org/show_bug.cgi?id=1541425 "https://bugzilla.mozilla.org/show_bug.cgi?id=1541425").
- Framerate in screen capture is suboptimal (approximately
  15fps?). See this [bugzilla
  thread](https://bugzilla.mozilla.org/show_bug.cgi?id=1703522 "https://bugzilla.mozilla.org/show_bug.cgi?id=1703522").

## Mobile Web

Limitations

- [getDisplayMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia#browser_compatibility "https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia#browser_compatibility") screen sharing is unsupported on mobile
  devices.

**Workaround**: None.

- Participant takes 15-30 seconds to leave when closing a browser without
  calling `leave()`.

**Workaround**: Add a UI that encourages
users to properly disconnect.

- Backgrounding app causes publishing video to stop.

**Workaround**: Display a UI slate when the
publisher is paused.

- Video framerate drops for approximately 5 seconds after unmuting a camera
  on Android devices.

**Workaround**: None.

- The video feed is stretched on rotation for iOS 16.0.

**Workaround**: Display a UI outlining this
known OS issue.

- Switching the audio-input device automatically switches the audio-output
  device.

**Workaround**: None.

- Backgrounding the browser causes the publishing stream to go black and
  produce only audio.

**Workaround**: None. This is for security
reasons.
