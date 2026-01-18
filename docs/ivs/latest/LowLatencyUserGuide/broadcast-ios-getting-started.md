# Getting Started with the IVS iOS

Broadcast SDK | Low-Latency Streaming

This document takes you through the steps involved in getting started with the Amazon
IVS low-latency streaming iOS broadcast SDK.

## Install the Library

We recommend that you integrate broadcast SDK via Swift Package Manager.
(Alternatively, you can integrate via CocoaPods or manually add the framework to
your project.)

### Recommended: Integrate the

Broadcast SDK (Swift Package Manager)

1. Download the Package.swift file from [https://broadcast.live-video.net/1.38.0/Package.swift](https://broadcast.live-video.net/1.38.0/Package.swift "https://broadcast.live-video.net/1.38.0/Package.swift").
2. In your project, create a new directory named AmazonIVSBroadcast and
   add it to version control.
3. Place the downloaded Package.swift file in the new directory.
4. In Xcode, go to **File > Add Package
   Dependencies** and select **Add
   Local...**
5. Navigate to and select the AmazonIVSBroadcast directory that you
   created, and select **Add Package**.
6. When prompted to **Choose Package Products for
   AmazonIVSBroadcast**, select **AmazonIVSBroadcast** as your **Package
   Product** by setting your application target in the
   **Add to Target** section.
7. Select **Add Package**.

### Alternate Approach: Integrate

the Broadcast SDK (CocoaPods)

**Important**: CocoaPods is in maintenance mode
(security fixes only) and after December 2026, no new packages or updates can be
published to the CocoaPods repository. Existing packages will remain available
but frozen. We recommend using Swift Package Manager for all new
projects.

Releases are published via CocoaPods under the name
`AmazonIVSBroadcast`. Add this dependency to your Podfile:

```
pod 'AmazonIVSBroadcast'
```

Run `pod install` and the SDK will be available in your
`.xcworkspace`.

### Alternate Approach: Install the

Framework Manually

1. Download the latest version from [https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast.xcframework.zip](https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast.xcframework.zip "https://broadcast.live-video.net/1.38.0/AmazonIVSBroadcast.xcframework.zip").
2. Extract the contents of the archive.
   `AmazonIVSBroadcast.xcframework` contains the SDK for
   both device and simulator.
3. Embed `AmazonIVSBroadcast.xcframework` by dragging it into
   the **Frameworks, Libraries, and Embedded
   Content** section of the **General** tab for your application target.

![The Frameworks, Libraries, and Embedded Content section of the General tab for your application target.](images/iOS_Broadcast_SDK_Guide_xcframework.png)

## Implement

IVSBroadcastSession.Delegate

Implement `IVSBroadcastSession.Delegate`, which allows you to receive
state updates and device-change notifications:

```
extension ViewController : IVSBroadcastSession.Delegate {
   func broadcastSession(_ session: IVSBroadcastSession,
                         didChange state: IVSBroadcastSession.State) {
      print("IVSBroadcastSession did change state \(state)")
   }

   func broadcastSession(_ session: IVSBroadcastSession,
                         didEmitError error: Error) {
      print("IVSBroadcastSession did emit error \(error)")
   }
}
```

## Request Permissions

Your app must request permission to access the user’s camera and mic. (This is not
specific to Amazon IVS; it is required for any application that needs access to
cameras and microphones.)

Here, we check whether the user has already granted permissions and, if not, we
ask for them:

```
switch AVCaptureDevice.authorizationStatus(for: .video) {
case .authorized: // permission already granted.
case .notDetermined:
   AVCaptureDevice.requestAccess(for: .video) { granted in
       // permission granted based on granted bool.
   }
case .denied, .restricted: // permission denied.
@unknown default: // permissions unknown.
}
```

You need to do this for both `.video` and `.audio` media
types, if you want access to cameras and microphones, respectively.

You also need to add entries for `NSCameraUsageDescription` and
`NSMicrophoneUsageDescription` to your `Info.plist`.
Otherwise, your app will crash when trying to request permissions.

## Disable the Application Idle

Timer

This is optional but recommended. It prevents your device from going to sleep
while using the broadcast SDK, which would interrupt the broadcast.

```
override func viewDidAppear(_ animated: Bool) {
   super.viewDidAppear(animated)
   UIApplication.shared.isIdleTimerDisabled = true
}
override func viewDidDisappear(_ animated: Bool) {
   super.viewDidDisappear(animated)
   UIApplication.shared.isIdleTimerDisabled = false
}
```

## (Optional) Set Up

AVAudioSession

By default, the broadcast SDK will set up your application’s
`AVAudioSession`. If you want to manage this yourself, set
`IVSBroadcastSession.applicationAudioSessionStrategy` to
`noAction`. Without control of the `AVAudioSession`, the
broadcast SDK cannot manage microphones internally. To use microphones with the
`noAction` option, you can create an
`IVSCustomAudioSource` and provide your own samples via an
`AVCaptureSession`, `AVAudioEngine` or another tool that
provides PCM audio samples.

If you are manually setting up your `AVAudioSession`, at a minimum you
need to set the category as `.record` or `.playbackAndRecord`,
and set it to `active`. If you want to record audio from Bluetooth
devices, you need to specify the `.allowBluetooth` option as well:

```
do {
   try AVAudioSession.sharedInstance().setCategory(.record, options: .allowBluetooth)
   try AVAudioSession.sharedInstance().setActive(true)
} catch {
   print("Error configuring AVAudioSession")
}
```

We recommend that you let the SDK handle this for you. Otherwise, if you want to
choose between different audio devices, you will need to manually manage the
ports.

## Create the Broadcast Session

The broadcast interface is `IVSBroadcastSession`. Initialize it as
shown below:

```
let broadcastSession = try IVSBroadcastSession(
   configuration: IVSPresets.configurations().standardLandscape(),
   descriptors: IVSPresets.devices().frontCamera(),
   delegate: self)
```

Also see [Create the Broadcast Session
(Advanced Version)](broadcast-ios-use-cases.md#broadcast-ios-create-session-advanced "broadcast-ios-use-cases.md#broadcast-ios-create-session-advanced")

## Set the IVSImagePreviewView for

Preview

If you want to display a preview for an active camera device, add the preview
`IVSImagePreviewView` for the device to your view hierarchy:

```
// If the session was just created, execute the following
// code in the callback of IVSBroadcastSession.awaitDeviceChanges
// to ensure all devices have been attached.
if let devicePreview = try broadcastSession.listAttachedDevices()
   .compactMap({ $0 as? IVSImageDevice })
   .first?
   .previewView()
{
   previewView.addSubview(devicePreview)
}
```

## Start a Broadcast

The hostname that you receive in the `ingestEndpoint` response field of
the `GetChannel` operation needs to have `rtmps://` prepended
and `/app` appended. The complete URL should be in this format:
`rtmps://{{ ingestEndpoint }}/app`

```
try broadcastSession.start(with: IVS_RTMPS_URL, streamKey: IVS_STREAMKEY)
```

The iOS broadcast SDK supports only RTMPS ingest (not insecure RTMP ingest).

## Stop a Broadcast

```
broadcastSession.stop()
```

## Manage Lifecycle Events

### Audio Interruptions

There are several scenarios where the broadcast SDK will not have exclusive
access to audio-input hardware. Some example scenarios that you need to handle
are:

- User receives a phone call or FaceTime call
- User activates Siri

Apple makes it easy to respond to these events by subscribing to
`AVAudioSession.interruptionNotification`:

```
NotificationCenter.default.addObserver(
   self,
   selector: #selector(audioSessionInterrupted(_:)),
   name: AVAudioSession.interruptionNotification,
   object: nil)
```

Then you can handle the event with something like this:

```
// This assumes you have a variable `isRunning` which tracks if the broadcast is currently live, and another variable `wasRunningBeforeInterruption` which tracks whether the broadcast was active before this interruption to determine if it should resume after the interruption has ended.

@objc
private func audioSessionInterrupted(_ notification: Notification) {
   guard let userInfo = notification.userInfo,
         let typeValue = userInfo[AVAudioSessionInterruptionTypeKey] as? UInt,
         let type = AVAudioSession.InterruptionType(rawValue: typeValue)
   else {
      return
   }
   switch type {
   case .began:
      wasRunningBeforeInterruption = isRunning
      if isRunning {
         broadcastSession.stop()
      }
   case .ended:
      defer {
         wasRunningBeforeInterruption = false
      }
      guard let optionsValue = userInfo[AVAudioSessionInterruptionOptionKey] as? UInt else { return }
      let options = AVAudioSession.InterruptionOptions(rawValue: optionsValue)
      if options.contains(.shouldResume) && wasRunningBeforeInterruption {
         try broadcastSession.start(
            with: IVS_RTMPS_URL,
            streamKey: IVS_STREAMKEY)
      }
   @unknown default: break
   }
}
```

### App Going Into

Background

Standard applications on iOS are not allowed to use cameras in the background.
There also are restrictions on video encoding in the background: since hardware
encoders are limited, only foreground applications have access. Because of this,
the broadcast SDK automatically terminates its session and sets its
`isReady` property to `false`. When your application
is about to enter the foreground again, the broadcast SDK reattaches all the
devices to their original `IVSMixerSlotConfiguration` entries.

The broadcast SDK does this by responding to
`UIApplication.didEnterBackgroundNotification` and
`UIApplication.willEnterForegroundNotification`.

If you are providing custom image sources, you should be prepared to handle
these notifications. You may need to take extra steps to tear them down before
the stream is terminated.

See [Use Background Video](broadcast-ios-use-cases.md#broadcast-ios-background-video "broadcast-ios-use-cases.md#broadcast-ios-background-video")
for a workaround that enables streaming while your application is in the
background.

### Media Services Lost

In very rare cases, the entire media subsystem on an iOS device will crash. In
this scenario, we can no longer broadcast. It is up to your application to
respond to these notifications appropriately. At a minimum, subscribe to these
notifications:

- [mediaServicesWereLostNotification](https://developer.apple.com/documentation/avfaudio/avaudiosession/1616457-mediaserviceswerelostnotificatio "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616457-mediaserviceswerelostnotificatio") — Respond by stopping
  your broadcast and completely deallocating your
  `IVSBroadcastSession` . All internal components used by
  the broadcast session will be invalidated.
- [mediaServicesWereResetNotification](https://developer.apple.com/documentation/avfaudio/avaudiosession/1616540-mediaserviceswereresetnotificati "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616540-mediaserviceswereresetnotificati") — Respond by notifying
  your users that they can broadcast again. Depending on your use case,
  you may be able to automatically start broadcasting again at this
  point.
