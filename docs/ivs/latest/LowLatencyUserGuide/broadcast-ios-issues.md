# Known Issues & Workarounds in the IVS iOS

Broadcast SDK | Low-Latency Streaming

This document lists known issues that you might encounter when using the Amazon IVS
low-latency streaming iOS broadcast SDK and suggests potential workarounds.

- A bug in ReplayKit causes rapid memory growth when plugging in a wired headset
  during a stream.

**Workaround:** Start the stream with the wired
headset already plugged in, use a Bluetooth headset, or do not use an external
microphone.

- If at any point during a ReplayKit stream you enable the microphone and then
  interrupt the audio session (e.g., with a phone call or by activating Siri),
  system audio will stop working. This is a ReplayKit bug that we are working with
  Apple to resolve.

**Workaround:** On an audio interruption, stop
the broadcast and alert the user.

- AirPods do not record any audio if the `AVAudioSession` category is
  set to `record`. By default, the SDK uses `playAndRecord`,
  so this issue manifests only if the category is changed to
  `record`.

**Workaround:** If there is a chance that AirPods
will be used to record audio, use `playAndRecord` even if your
application is not playing back media.

- When AirPods are connected to an iOS 12 device, no other microphone can be
  used to record audio. Attempting to switch to an internal microphone immediately
  reverts back to the AirPods.

**Workaround:** None. If AirPods are connected to
iOS 12, they are the only device that can record audio.

- Submitting audio data faster than realtime (using a custom audio source)
  results in audio drift.

**Workaround:** Do not submit audio data faster
than realtime.

- Audio artifacts can appear at bitrates under 68 kbps when using a high sample
  rate (44100 Hz or greater) and two channels.

**Workaround:** Increase the bitrate to 68 kbps
or higher, decrease the sample rate to 24000 Hz or lower, or set channels to

1.

- When echo cancellation is enabled on `IVSMicrophone` devices, only
  a single microphone source is returned by the
  `listAvailableInputSources` method.

**Workaround:** None. This behavior is controlled
by iOS.

- Changing Bluetooth audio routes can be unpredictable. If you connect a new
  device mid-session, iOS may or may not automatically change the input route.
  Also, it is not possible to choose between multiple Bluetooth headsets that are
  connected at the same time. This happens in both regular broadcast and stage
  sessions.

**Workaround:** If you plan to use a Bluetooth
headset, connect it before starting the broadcast or stage and leave it
connected throughout the session.

- iOS removes access to the camera when the AirPods popup appears after opening
  a paired AirPods case while leaving the AirPods themselves in the case. This
  results in the video for a broadcast or stage freezing.

**Workaround:** None. iOS completely revokes
camera access while the popup is being rendered and it is impossible for
third-party applications to prevent the popup.

- Enabling B-frames can improve compression quality; however some encoders provide less precise bitrate control when B-frames are enabled, which may cause issues during network fluctuations.

**Workaround:** Consider disabling B-frames if consistent bitrate adherence is more important than compression efficiency for your use case.
