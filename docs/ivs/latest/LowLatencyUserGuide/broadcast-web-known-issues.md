# Known Issues & Workarounds in the IVS Web Broadcast SDK | Low-Latency Streaming

This document lists known issues that you might encounter when using the Amazon IVS low-latency streaming Web broadcast SDK
and suggests potential workarounds.

- Viewers may experience green artifacts or irregular framerate, when watching streams from broadcasters who are using Safari on Intel-based Mac devices.

**Workaround:** Redirect broadcasters on Intel Mac devices to broadcast using Chrome.

- The web broadcast SDK requires port 4443 to be open. VPNs and firewalls can
  block port 4443 and prevent you from streaming.

**Workaround:** Disable VPNs and/or configure
firewalls to ensure that port 4443 is not blocked.

- Switching from landscape to portrait mode is buggy.

**Workaround:** None.

- The resolution reported in the HLS manifest is incorrect. It is set as the
  initially received resolution, which usually is much lower than what is possible
  and does not reflect any upscaling that happens during the duration of the
  webRTC connection.

**Workaround:** None.

- Subsequent client instances created after the initial page is loaded may not
  respond to `maxFramerate` settings that are different from the first
  client instance.

**Workaround:** Set `StreamConfig`
only once, through the `IVSBroadcastClient.create` function when the
first client instance is created.

- On iOS, capturing multiple video device sources is not supported by
  WebKit.

**Workaround:** Follow [this issue](https://bugs.webkit.org/show_bug.cgi?id=238492 "https://bugs.webkit.org/show_bug.cgi?id=238492") to
track development progress.

- On iOS, calling `getUserMedia()` once you already have a video
  source will stop any other video source retrieved using
  `getUserMedia()`.

**Workaround:** None.

- WebRTC dynamically chooses the best bitrate and resolution for the resources
  that are available. Your stream will not be high quality if your hardware or
  network cannot support it. The quality of your stream may change during the
  broadcast as more or fewer resources are available.

**Workaround:** Provide at least 200 kbps
upload.

- If Auto-Record to Amazon S3 is enabled for a channel and the Web Broadcast SDK
  is used, recording to the same S3 prefix may not work, as the Web Broadcast SDK
  dynamically changes bitrates and qualities.

**Workaround:** None.

- When using Next.js, an `Uncaught ReferenceError: self is not
defined` error may be encountered, depending on how the SDK is
  imported.

**Workaround:**
[Dynamically import the library](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading "https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading") when using Next.js.

- You may be unable to import the module using a script tag of type
  `module`; i.e., `<script type="module"
src="..."\>`.

**Workaround:** The library does not have an ES6
build. Remove the `type="module"` from the script tag.

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
