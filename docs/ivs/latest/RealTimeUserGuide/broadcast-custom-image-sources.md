# IVS Broadcast SDK: Custom Image

Sources | Real-Time Streaming

Custom image-input sources allow an application to provide its own image input to the
broadcast SDK, instead of being limited to the preset cameras. A custom image source can be
as simple as a semi-transparent watermark or static “be right back” scene, or it can allow
the app to do additional custom processing like adding beauty filters to the camera.

When you use a custom image-input source for custom control of the camera (such as using
beauty-filter libraries that require camera access), the broadcast SDK is no longer responsible
for managing the camera. Instead, the application is responsible for handling the camera’s
lifecycle correctly. See official platform documentation on how your application should manage
the camera.

## Android

After you create a `DeviceDiscovery` session, create an image-input source:

```
CustomImageSource imageSource = deviceDiscovery.createImageInputSource(new BroadcastConfiguration.Vec2(1280, 720));
```

This method returns a `CustomImageSource`, which is an image source backed by a
standard Android [Surface](https://developer.android.com/reference/android/view/Surface "https://developer.android.com/reference/android/view/Surface").
The sublcass `SurfaceSource` can be resized and rotated. You also can create an `ImagePreviewView`
to display a preview of its contents.

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

This `CustomImageSource` can be wrapped in a `LocalStageStream`
and returned by the `StageStrategy` to publish to a `Stage`.

## iOS

After you create a `DeviceDiscovery` session, create an image-input source:

```
let customSource = broadcastSession.createImageSource(withName: "customSourceName")
```

This method returns an `IVSCustomImageSource`, which is an image source
that allows the application to submit `CMSampleBuffers` manually. For
supported pixel formats, see the iOS Broadcast SDK Reference; a link to the most current
version is in the [Amazon IVS Release Notes](release-notes.md "release-notes.md") for the
latest broadcast SDK release.

Samples submitted to the custom source will be streamed to the Stage:

```
customSource.onSampleBuffer(sampleBuffer)
```

For streaming video, use this method in a callback. For example, if you’re using the
camera, then every time a new sample buffer is received from an
`AVCaptureSession`, the application can forward the sample buffer to the
custom image source. If desired, the application can apply further processing (like a
beauty filter) before submitting the sample to the custom image source.

The `IVSCustomImageSource` can be wrapped in an `IVSLocalStageStream` and returned by the
`IVSStageStrategy` to publish to a `Stage`.
