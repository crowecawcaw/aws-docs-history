# Known Issues & Workarounds in the IVS

Android Broadcast SDK | Low-Latency Streaming

This document lists known issues that you might encounter when using the Amazon IVS low-latency
streaming Android broadcast SDK and suggests potential workarounds.

- Using an external microphone connected through Bluetooth can be unstable. When
  a Bluetooth device is connected or disconnected during a broadcasting session,
  microphone input may stop working until the device is explicitly detached and
  reattached.

**Workaround:** If you plan to use a Bluetooth
headset, connect it before starting the broadcast and leave it connected
throughout the broadcast.

- The broadcast SDK does not support access on external cameras connected via
  USB.

**Workaround:** Do not use external cameras
connected via USB.

- Submitting audio data faster than realtime (using a custom audio source)
  results in audio drift.

**Workaround:** Do not submit audio data faster
than realtime.

- Android 6 and 7 devices cannot receive the broadcast SDK's
  `onDeviceAdded` and `onDeviceRemoved` callbacks for
  microphones, because these Android versions allow only the system’s default
  microphone.

**Workaround:** For these devices, the broadcast
SDK uses the system's default microphone.

- When an `ImagePreviewView` is removed from a parent (e.g.,
  `removeView()` is called at the parent), the
  `ImagePreviewView` is released immediately. The
  `ImagePreviewView` does not show any frames when it is added to
  another parent view.

**Workaround:** Request another preview using
`getPreview`.

- Some Android video encoders cannot be configured with a video size less than
  176x176. Configuring a smaller size causes an error and prevents
  streaming.

**Workaround:** Do not configure the video size
to be less than 176x176.

- Enabling B-frames can improve compression quality; however some encoders provide less precise bitrate control when B-frames are enabled, which may cause issues during network fluctuations.

**Workaround:** Consider disabling B-frames if consistent bitrate adherence is more important than compression efficiency for your use case.
