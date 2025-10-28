# Integrating Third-Party Camera

Filters

You can integrate third-party camera filter SDKs with the IVS broadcast SDK by feeding
the filter SDK’s output to a [custom image
input source](broadcast-custom-image-sources.md "broadcast-custom-image-sources.md"). A custom image-input source allows an application to provide
its own image input to the Broadcast SDK. A third-party filter provider’s SDK may manage
the camera’s lifecycle to process images from the camera, apply a filter effect, and
output it in a format that can be passed to a custom image source.

![Integrating third-party camera filter SDKs with the IVS broadcast SDK by feeding the filter SDK’s output to a custom image input source.](images/3P_Camera_Filters_Integrating.png)
Consult your third-party filter provider’s documentation for built-in methods to
convert a camera frame, with the filter effect, applied to a format that can be passed
to a [custom image-input source](broadcast-custom-image-sources.md "broadcast-custom-image-sources.md").
The process varies, depending on which version of the IVS broadcast SDK is used:

- **Web** — The filter provider must be able to
  render its output to a canvas element. The [captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream "https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream") method can then be used to return a MediaStream of
  the canvas’s contents. The MediaStream can then be converted to an instance of a
  [LocalStageStream](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/classes/LocalStageStream "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/classes/LocalStageStream") and published to a Stage.
- **Android** — The filter provider’s SDK can
  either render a frame to an Android `Surface` provided by the IVS
  broadcast SDK or convert the frame to a bitmap. If using a bitmap, it can then
  be rendered to the underlying `Surface` provided by the custom image
  source, by unlocking and writing to a canvas.
- **iOS** — A third-party filter provider’s SDK
  must provide a camera frame with a filter effect applied as a
  `CMSampleBuffer`. Refer to your third-party filter vendor SDK’s
  documentation for information on how to get a `CMSampleBuffer` as the
  final output after a camera image is processed.
