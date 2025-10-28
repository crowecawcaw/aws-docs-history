# IVS Broadcast SDK: Custom Image

Sources | Low-Latency Streaming

This guide assumes you are already familiar with how to set up a broadcast session ([Android](broadcast-android.md "broadcast-android.md"), [iOS](broadcast-ios.md "broadcast-ios.md"))
and how to [use the mixed devices API](broadcast-mixed-devices.md "broadcast-mixed-devices.md").

Custom image-input sources allow an application to provide its own image input to the
broadcast SDK, instead of being limited to the preset cameras or screen share. A custom
image source can be as simple as a semi-transparent watermark or static "be right back"
scene, or it can allow the app to do additional custom processing like adding beauty filters
to the camera.

You can have multiple custom image sources, like a watermark plus a camera with beauty
filters. When you use a custom image-input source for custom control of the camera (such as
using beauty-filter libraries that require camera access), the broadcast SDK is no longer
responsible for managing the camera. Instead, the application is responsible for handling
the camera’s lifecycle correctly. See official platform documentation on how your
application should manage the camera.

## Android

After you create a broadcast session, create an image-input source:

```
SurfaceSource surfaceSource = broadcastSession.createImageInputSource();
```

This method returns a `SurfaceSource`, which is an image source backed by a
standard Android [Surface](https://developer.android.com/reference/android/view/Surface "https://developer.android.com/reference/android/view/Surface").
It is automatically attached to the broadcast session, so there is no need to use the
`attachDevice(...)` method afterward. However, the
`SurfaceSource` needs to be bound to a slot; this is covered later below.
The `SurfaceSource` can be resized and rotated. You also can create an
`ImagePreviewView` to display a preview of its contents.

To retrieve the underlying `Surface`:

```
Surface surface = surfaceSource.getInputSurface();
```

This `Surface` can be used as the output buffer for image producers like
Camera2, OpenGL ES, and other libraries. The simplest use case is directly drawing a
static bitmap or color into the Surface’s Canvas. However, many libraries (such as
beauty-filter libraries) provide a method that allows an application to specify an
external `Surface` for rendering. You can use such a method to pass this
`Surface` to the filter library, which allows the library to output
processed frames for the broadcast session to stream.

Finally, the `SurfaceSource` must be bound to a `Mixer.Slot` to
be streamed by the broadcast session:

```
broadcastSession.getMixer().bind(surfaceSource, "customSlot");
```

The [Android sample code](https://github.com/aws-samples/amazon-ivs-broadcast-android-sample "https://github.com/aws-samples/amazon-ivs-broadcast-android-sample") has several examples that use a custom image source in
different ways:

- A semi-transparent watermark is added in the
  `MixerActivity`.
- An MP4 file is looped in the `MixerActivity`.
- The [CameraManager](https://github.com/aws-samples/amazon-ivs-broadcast-android-sample/blob/main/app/src/main/java/com/amazonaws/ivs/basicbroadcast/common/CameraManager.kt "https://github.com/aws-samples/amazon-ivs-broadcast-android-sample/blob/main/app/src/main/java/com/amazonaws/ivs/basicbroadcast/common/CameraManager.kt") utility class does custom management of the device
  camera using the Camera2 method in the `CustomActivity`, which
  applies a simple sepia filter. This example is especially helpful since it shows
  how to manage the camera and pass the broadcast session’s custom
  `SurfaceSource` to the camera capture request. If you use other
  external libraries, follow their documentation on how to configure the library
  to output to the Android `Surface` provided by the broadcast
  session.

## iOS

After you create the broadcast session, create an image-input source:

```
let customSource = broadcastSession.createImageSource(withName: "customSourceName")
```

This method returns an `IVSCustomImageSource`, which is an image source
that allows the application to submit `CMSampleBuffers` manually. For
supported pixel formats, see the iOS Broadcast SDK Reference; a link to the most current
version is in the [Amazon IVS Release Notes](release-notes.md "release-notes.md") for the
latest broadcast SDK release. The source is not automatically attached to the broadcast
session, so you must attach the image source to the session and bind it to a slot before
the source will stream:

```
broadcastSession.attach(customSource, toSlotWithName: "customSourceSlot", onComplete: nil)
```

After the custom source is attached and bound, the application can submit
`CMSampleBuffers` directly to the custom source. You may choose to use
the `onComplete` callback to start doing so.

Samples submitted to the custom source will be streamed in the broadcast
session:

```
customSource.onSampleBuffer(sampleBuffer)
```

For streaming video, use this method in a callback. For example, if you’re using the
camera, then every time a new sample buffer is received from an
`AVCaptureSession`, the application can forward the sample buffer to the
custom image source. If desired, the application can apply further processing (like a
beauty filter) before submitting the sample to the custom image source.

For a static image, after the first sample, the application needs to resubmit the
sample if the custom image source’s slot binding is changed or the source is detached
and reattached to the broadcast session. For example, if you remove the slot from and
then add the slot to the mixer, you must resubmit the sample.

The [iOS
sample app](https://github.com/aws-samples/amazon-ivs-broadcast-ios-sample "https://github.com/aws-samples/amazon-ivs-broadcast-ios-sample") has several examples that use a custom image source in different
ways:

- A semi-transparent watermark is added in
  `MixerViewController`.
- An MP4 file is looped in `MixerViewController`.
- A CIFilter implementation with a device camera is added in
  `CustomSourcesViewController`. This allows an application to
  manage a device camera independently of the Amazon IVS Broadcast SDK. It uses
  `AVCaptureSession` to capture an image from the device camera,
  processes the image using a CIFilter implementation, and submits
  `CMSampleBuffers` to `customSource` for live
  streaming.
