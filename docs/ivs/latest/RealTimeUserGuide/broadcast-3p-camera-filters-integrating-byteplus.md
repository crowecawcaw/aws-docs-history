# Using BytePlus with the IVS Broadcast SDK

This document explains how to use the BytePlus Effects SDK with the IVS broadcast SDK.

## Android

### Install and

Set Up the BytePlus Effects SDK

See the BytePlus [Android Access Guide](https://docs.byteplus.com/en/effects/docs/android-v4101-access-guide "https://docs.byteplus.com/en/effects/docs/android-v4101-access-guide") for details on how to install, initialize, and
set up the BytePlus Effects SDK.

### Set Up the

Custom Image Source

After initializing the SDK, feed processed camera frames with a filter effect
applied to a custom-image input source. To do that, create an instance of a
`DeviceDiscovery` object and create a custom image source. Note
that when you use a custom image input source for custom control of the camera,
the broadcast SDK is no longer responsible for managing the camera. Instead, the
application is responsible for handling the camera’s lifecycle correctly.

```
var deviceDiscovery = DeviceDiscovery(applicationContext)
var customSource = deviceDiscovery.createImageInputSource( BroadcastConfiguration.Vec2(
720F, 1280F
))
var surface: Surface = customSource.inputSurface
var filterStream = ImageLocalStageStream(customSource)
```

### Convert Output

to a Bitmap and Feed to Custom Image Input Source

To enable camera frames with a filter effect applied from the BytePlus Effect
SDK to be forwarded directly to the IVS broadcast SDK, convert the BytePlus
Effects SDK’s output of a texture to a bitmap. When an image is processed, the
`onDrawFrame()` method is invoked by the SDK. The
`onDrawFrame()` method is a public method of Android’s [GLSurfaceView.Renderer](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer "https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer") interface. In the Android sample app
provided by BytePlus, this method is called on every camera frame; it outputs a
texture. Concurrently, you can supplement the `onDrawFrame()` method
with logic to convert this texture to a bitmap and feed it to a custom image
input source. As shown in the following code sample, use the
`transferTextureToBitmap` method provided by the BytePlus SDK to
do this conversion. This method is provided by the [com.bytedance.labcv.core.util.ImageUtil](https://docs.byteplus.com/en/effects/docs/android-v4101-access-guide#Appendix:%20convert%20input%20texture%20to%202D%20texture%20with%20upright%20face "https://docs.byteplus.com/en/effects/docs/android-v4101-access-guide#Appendix:%20convert%20input%20texture%20to%202D%20texture%20with%20upright%20face") library from the BytePlus
Effects SDK, as shown in the following code sample.You can then render to the
underlying Android `Surface` of a `CustomImageSource` by
writing the resulting bitmap to a Surface’s canvas. Many successive invocations
of `onDrawFrame()` results in a sequence of bitmaps, and when
combined, creates a stream of video.

```
import com.bytedance.labcv.core.util.ImageUtil;
...
protected ImageUtil imageUtility;
...


@Override
public void onDrawFrame(GL10 gl10) {
  ...
  // Convert BytePlus output to a Bitmap
  Bitmap outputBt = imageUtility.transferTextureToBitmap(output.getTexture(),ByteEffect
  Constants.TextureFormat.Texture2D,output.getWidth(), output.getHeight());

  canvas = surface.lockCanvas(null);
  canvas.drawBitmap(outputBt, 0f, 0f, null);
  surface.unlockCanvasAndPost(canvas);
```
