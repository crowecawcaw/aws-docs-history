# Known Issues & Workarounds in the IVS Android Player SDK

This document lists known issues that you might encounter when using the Amazon IVS Android player SDK
and suggests potential workarounds.

- The Android player SDK has a runtime dependency on OkHttp version 4.x. Using
  OkHttp version 3.x may cause instability or crashes due to an API signature
  mismatch and OkHttp backwards compatibility issues. Specifically, the player
  depends on OkHttp version 4.2.2, but it should be compatible with any 4.x
  version.

**Workaround:** Use a 4.x version of OkHttp or
remove OkHttp from your application.

- When using an Android 11 (API level 30) emulator, you may experience
  video-layout issues (specifically, zooming of the stream).

**Workaround:** Play back on the real device
instead.
