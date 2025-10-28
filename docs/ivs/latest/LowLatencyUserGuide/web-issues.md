# Known Issues & Workarounds in the IVS Web Player

SDK

This document lists known issues that you might encounter when using the Amazon IVS
Web player SDK and suggests potential workarounds.

- When playing recorded content (also known as VOD) on an iOS mobile browser
  (e.g. Safari or Chrome), seeking backwards will mute the player.

**Workaround:** Call
`player.setMuted(false)` after seeking.

- When playing recorded content on an iOS mobile browser, seeking backwards
  works intermittently when directly selecting the desired position.

**Workaround:** Drag the seek bar to the desired
position.

- When playing recorded content on an iOS mobile browser,
  `player.seekTo()` calls do not consistently work.

**Workaround:** Set `currentTime` on
the video HTML element after the `loadeddata` event. For
example:

```
videoEl.addEventListener('loadeddata', () => {
	videoEl.currentTime = 30; // seek 30s from the beginning
});
```

- When playing a live stream or recorded content on an iOS mobile browser,
  captions may not be rendered in different sizes and may be re-rendered multiple
  times.

**Workaround:** None.

- When playing a live stream or recorded content on an iOS mobile browser,
  `player.getQualities()` calls do not return the list of available
  qualities.

**Workaround:** None. The player supports only
auto-quality mode on iOS browsers.

- When native HTML5 controls are enabled, calls to `setQuality()` are
  ignored.

**Workaround:** Disable HTML5 controls before
calling `player.setQuality()`.

- When playing a muted live stream on an iOS mobile browser, player instability
  (e.g., black or frozen screen, buffering) may be seen when resuming an inactive
  player tab (e.g., tab switches or device lock/unlock).

**Workaround:** Use the JavaScript [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API "https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API") to detect page visibility changes and then take
action on the player accordingly. For example:

```
//if client platform is iOS
if (!!navigator.platform && /iPad|iPhone|iPod/.test(navigator.platform)) {
    document.addEventListener(“visibilitychange”, () => {
        if (document.visibilityState === “hidden” && player.isMuted()) {
            player.pause()
        if (document.visibilityState === “visible” &&
            player.getState() != PlayerState.PLAYING) {
            player.play()
        }
    })
}
```

- When using the Web player SDK on iOS Safari, playback authorization will not
  work without a service worker due to limited iOS support for Media Source
  Extensions (MSE).

**Workaround:** Implement a service worker with
the Player SDK. See [Set Up Service
Worker](web-getting-started.md#web-service-worker "web-getting-started.md#web-service-worker") and this [demo](https://github.com/aws-samples/amazon-ivs-player-web-sample/blob/master/samples/service-worker/service-worker.ts "https://github.com/aws-samples/amazon-ivs-player-web-sample/blob/master/samples/service-worker/service-worker.ts").
