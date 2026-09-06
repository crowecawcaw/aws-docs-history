

# Getting Started​ with the IVS iOS Broadcast SDK \| Real-Time Streaming
<a name="broadcast-ios-getting-started"></a>

This document takes you through the steps involved in getting started with the IVS real-time streaming iOS broadcast SDK.

## Install the Library
<a name="broadcast-ios-install"></a>

We recommend that you integrate broadcast SDK via Swift Package Manager. (Alternatively, you can manually add the framework to your project.)

### Recommended: Integrate the Broadcast SDK (Swift Package Manager)
<a name="broadcast-ios-install-swift"></a>

1. Download the Package.swift file from [https://broadcast.live-video.net/1.46.0/Package.swift](https://broadcast.live-video.net/1.46.0/Package.swift).

1. In your project, create a new directory named AmazonIVSBroadcast and add it to version control.

1. Place the downloaded Package.swift file in the new directory.

1. In Xcode, go to **File > Add Package Dependencies** and select **Add Local...**

1. Navigate to and select the AmazonIVSBroadcast directory that you created, and select **Add Package**.

1. When prompted to **Choose Package Products for AmazonIVSBroadcast**, select **AmazonIVSBroadcastStages** as your **Package Product** by setting your application target in the **Add to Target** section.

1. Select **Add Package**.

**Important**: The IVS real-time streaming broadcast SDK includes all features of the IVS low-latency streaming broadcast SDK. It is not possible to integrate both SDKs in the same project.

### Alternate Approach: Install the Framework Manually
<a name="broadcast-ios-install-manual"></a>

1. Download the latest version from [ https://broadcast.live-video.net/1.46.0/AmazonIVSBroadcast-Stages.xcframework.zip](https://broadcast.live-video.net/1.46.0/AmazonIVSBroadcast-Stages.xcframework.zip).

1. Extract the contents of the archive. `AmazonIVSBroadcast.xcframework` contains the SDK for both device and simulator.

1. Embed `AmazonIVSBroadcast.xcframework` by dragging it into the **Frameworks, Libraries, and Embedded Content** section of the **General** tab for your application target.  
![The Frameworks, Libraries, and Embedded Content section of the General tab for your application target.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/iOS_Broadcast_SDK_Guide_xcframework.png)

## Request Permissions
<a name="broadcast-ios-permissions"></a>

Your app must request permission to access the user’s camera and mic. (This is not specific to Amazon IVS; it is required for any application that needs access to cameras and microphones.)

Here, we check whether the user has already granted permissions and, if not, we ask for them:

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

You need to do this for both `.video` and `.audio` media types, if you want access to cameras and microphones, respectively.

You also need to add entries for `NSCameraUsageDescription` and `NSMicrophoneUsageDescription` to your `Info.plist`. Otherwise, your app will crash when trying to request permissions.

## Disable the Application Idle Timer
<a name="broadcast-ios-disable-idle-timer"></a>

This is optional but recommended. It prevents your device from going to sleep while using the broadcast SDK, which would interrupt the broadcast.

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