# Advanced Use Cases for the IVS iOS Broadcast

SDK | Low-Latency Streaming

Here we present some advanced use cases. Start with the basic setup above and continue
here.

## Create a Broadcast

Configuration

Here we create a custom configuration with two mixer slots that allow us to bind
two video sources to the mixer. One (`custom`) is full screen and laid
out behind the other (`camera`), which is smaller and in the bottom-right
corner. Note that for the `custom` slot we do not set a position, size,
or aspect mode. Because we do not set these parameters, the slot uses the video
settings for size and position.

```
let config = IVSBroadcastConfiguration()
try config.audio.setBitrate(128_000)
try config.video.setMaxBitrate(3_500_000)
try config.video.setMinBitrate(500_000)
try config.video.setInitialBitrate(1_500_000)
try config.video.setSize(CGSize(width: 1280, height: 720))
config.video.defaultAspectMode = .fit
config.mixer.slots = [
    try {
        let slot = IVSMixerSlotConfiguration()
        // Do not automatically bind to a source
        slot.preferredAudioInput = .unknown
        // Bind to user image if unbound
        slot.preferredVideoInput = .userImage
        try slot.setName("custom")
        return slot
    }(),
    try {
        let slot = IVSMixerSlotConfiguration()
        slot.zIndex = 1
        slot.aspect = .fill
        slot.size = CGSize(width: 300, height: 300)
        slot.position = CGPoint(x: config.video.size.width - 400, y: config.video.size.height - 400)
        try slot.setName("camera")
        return slot
    }()
]
```

## Create the Broadcast Session

(Advanced Version)

Create an `IVSBroadcastSession` as you did in the [basic example](broadcast-ios-getting-started.md#broadcast-ios-create-session "broadcast-ios-getting-started.md#broadcast-ios-create-session"), but provide your
custom configuration here. Also provide `nil` for the device array, as we
will add those manually.

```
let broadcastSession = try IVSBroadcastSession(
   configuration: config, // The configuration we created above
   descriptors: nil, // We’ll manually attach devices after
   delegate: self)
```

## Iterate and Attach a Camera

Device

Here we iterate through input devices that the SDK has detected. The SDK will only
return built-in devices on iOS. Even if Bluetooth audio devices are connected, they
will appear as a built-in device. For more information, see [Known Issues & Workarounds in the IVS iOS
Broadcast SDK | Low-Latency Streaming](broadcast-ios-issues.md "broadcast-ios-issues.md").

Once we find a device that we want to use, we call `attachDevice` to
attach it:

```
let frontCamera = IVSBroadcastSession.listAvailableDevices()
    .filter { $0.type == .camera && $0.position == .front }
    .first
if let camera = frontCamera {
    broadcastSession.attach(camera, toSlotWithName: "camera") { device, error in
        // check error
    }
}
```

## Swap Cameras

```
// This assumes you’ve kept a reference called `currentCamera` that points to the current camera.
let wants: IVSDevicePosition = (currentCamera.descriptor().position == .front) ? .back : .front
// Remove the current preview view since the device will be changing.
previewView.subviews.forEach { $0.removeFromSuperview() }
let foundCamera = IVSBroadcastSession
        .listAvailableDevices()
        .first { $0.type == .camera && $0.position == wants }
guard let newCamera = foundCamera else { return }
broadcastSession.exchangeOldDevice(currentCamera, withNewDevice: newCamera) { newDevice, _ in
    currentCamera = newDevice
    if let camera = newDevice as? IVSImageDevice {
        do {
            previewView.addSubview(try finalCamera.previewView())
        } catch {
            print("Error creating preview view \(error)")
        }
    }
}
```

## Create a Custom Input

Source

To input sound or image data that your app generates, use
`createImageSource` or `createAudioSource`. Both these
methods create virtual devices (`IVSCustomImageSource` and
`IVSCustomAudioSource`) that can be bound to the mixer like any other
device.

The devices returned by both these methods accept a `CMSampleBuffer`
through its `onSampleBuffer` function:

- For video sources, the pixel format must be
  `kCVPixelFormatType_32BGRA`,
  `420YpCbCr8BiPlanarFullRange`, or
  `420YpCbCr8BiPlanarVideoRange`.
- For audio sources, the buffer must contain Linear PCM data.

You cannot use an `AVCaptureSession` with camera input to feed a custom
image source while also using a camera device provided by the broadcast SDK. If you
want to use multiple cameras simultaneously, use
`AVCaptureMultiCamSession` and provide two custom image
sources.

Custom image sources primarily should be used with static content such as images,
or with video content:

```
let customImageSource = broadcastSession.createImageSource(withName: "video")
try broadcastSession.attach(customImageSource, toSlotWithName: "custom")
```

## Monitor Network

Connectivity

It is common for mobile devices to temporarily lose and regain network
connectivity while on the go. Because of this, it is important to monitor your app’s
network connectivity and respond appropriately when things change.

When the broadcaster's connection is lost, the broadcast SDK's state will change
to `error` and then `disconnected`. You will be notified of
these changes through the `IVSBroadcastSessionDelegate`. When you receive
these state changes:

1. Monitor your broadcast app’s connectivity state and call
   `start` with your endpoint and stream key, once your
   connection has been restored.
2. **Important:** Monitor the state delegate
   callback and ensure that the state changes to `connected` after
   calling `start` again.

## Detach a Device

If you want to detach and not replace a device, detach it with
`IVSDevice` or `IVSDeviceDescriptor`:

```
broadcastSession.detachDevice(currentCamera)
```

## ReplayKit Integration

To stream the device’s screen and system audio on iOS, you must integrate with
[ReplayKit](https://developer.apple.com/documentation/replaykit?language=objc "https://developer.apple.com/documentation/replaykit?language=objc"). The Amazon IVS broadcast SDK makes it easy to integrate
ReplayKit using `IVSReplayKitBroadcastSession`. In your
`RPBroadcastSampleHandler` subclass, create an instance of
`IVSReplayKitBroadcastSession`, then:

- Start the session in `broadcastStarted`
- Stop the session in `broadcastFinished`

The session object will have three custom sources for screen images, app audio,
and microphone audio. Pass the `CMSampleBuffers` provided in
`processSampleBuffer` to those custom sources.

To handle device orientation, you need to extract ReplayKit-specific metadata from
the sample buffer. Use the following code:

```
let imageSource = session.systemImageSource;
if let orientationAttachment = CMGetAttachment(sampleBuffer, key: RPVideoSampleOrientationKey as CFString, attachmentModeOut: nil) as? NSNumber,
    let orientation = CGImagePropertyOrientation(rawValue: orientationAttachment.uint32Value) {
    switch orientation {
    case .up, .upMirrored:
        imageSource.setHandsetRotation(0)
    case .down, .downMirrored:
        imageSource.setHandsetRotation(Float.pi)
    case .right, .rightMirrored:
        imageSource.setHandsetRotation(-(Float.pi / 2))
    case .left, .leftMirrored:
        imageSource.setHandsetRotation((Float.pi / 2))
    }
}
```

It is possible to integrate ReplayKit using `IVSBroadcastSession`
instead of `IVSReplayKitBroadcastSession`. However, the
ReplayKit-specific variant has several modifications to reduce the internal memory
footprint, to stay within Apple’s memory ceiling for broadcast extensions.

## Get Recommended Broadcast

Settings

To evaluate your user’s connection before starting a broadcast, use
`IVSBroadcastSession.recommendedVideoSettings` to run a brief test.
As the test runs, you will receive several recommendations, ordered from most to
least recommended. In this version of the SDK, it is not possible to reconfigure the
current `IVSBroadcastSession`, so you must deallocate it and then create
a new one with the recommended settings. You will continue to receive
`IVSBroadcastSessionTestResults` until the `result.status`
is `Success` or `Error`. You can check progress with
`result.progress`.

Amazon IVS supports a maximum bitrate of 8.5 Mbps (for channels whose
`type` is `STANDARD` or `ADVANCED`), so the
`maximumBitrate` returned by this method never exceeds 8.5 Mbps. To
account for small fluctuations in network performance, the recommended
`initialBitrate` returned by this method is slightly less than the
true bitrate measured in the test. (Using 100% of the available bandwidth usually is
inadvisable.)

```
func runBroadcastTest() {
    self.test = session.recommendedVideoSettings(with: IVS_RTMPS_URL, streamKey: IVS_STREAMKEY) { [weak self] result in
        if result.status == .success {
            self?.recommendation = result.recommendations[0];
        }
    }
}
```

## Using Auto-Reconnect

IVS supports automatic reconnection to a broadcast if the broadcast stops
unexpectedly without calling the `stop` API; e.g., a temporary loss in
network connectivity. To enable auto-reconnect, set the `enabled`
property on `IVSBroadcastConfiguration.autoReconnect` to
`true`.

When something causes the stream to unexpectedly stop, the SDK retries up to 5
times, following a linear backoff strategy. It notifies your application about the
retry state through the `IVSBroadcastSessionDelegate.didChangeRetryState`
function.

Behind the scenes, auto-reconnect uses IVS [stream-takeover](streaming-config.md#streaming-config-stream-takeover "streaming-config.md#streaming-config-stream-takeover") functionality
by appending a priority number, starting with 1, to the end of the provided stream
key. For the duration of the `IVSBroadcastSession` instance, that number
is incremented by 1 each time a reconnect is attempted. This means if the device’s
connection is lost 4 times during a broadcast, and each loss requires 1-4 retry
attempts, the priority of the last stream up could be anywhere between 5 and 17.
Because of this, _we recommend you do not use IVS stream takeover from
another device while auto-reconnect is enabled in the SDK for the same
channel_. There are no guarantees what priority the SDK is using at
the time, and the SDK will try to reconnect with a higher priority if another device
takes over.

## Use Background Video

You can continue a non-RelayKit broadcast, even with your application in the
background.

To save power and keep foreground applications responsive, iOS gives only one
application at a time access to the GPU. The Amazon IVS Broadcast SDK uses the GPU
at multiple stages of the video pipeline, including compositing multiple input
sources, scaling the image, and encoding the image. While the broadcasting
application is in the background, there is no guarantee that the SDK can perform any
of these actions.

To address this, use the `createAppBackgroundImageSource` method. It
enables the SDK to continue broadcasting both video and audio while in the
background. It returns an `IVSBackgroundImageSource`, which is a normal
`IVSCustomImageSource` with an additional `finish`
function. Every `CMSampleBuffer` provided to the background image source
is encoded at the frame rate provided by your original
`IVSVideoConfiguration`. Timestamps on the
`CMSampleBuffer` are ignored.

The SDK then scales and encodes those images and caches them, automatically
looping that feed when your application goes into the background. When your
application returns to the foreground, the attached image devices become active
again and the pre-encoded stream stops looping.

To undo this process, use `removeImageSourceOnAppBackgrounded`. You do
not have to call this unless you want to explicitly revert the SDK’s background
behavior; otherwise, it is cleaned up automatically on deallocation of the
`IVSBroadcastSession`.

**Notes:**
_We strongly recommend that you call this method as part of
configuring the broadcast session, before the session goes live._ The
method is expensive (it encodes video), so performance of a live broadcast while
this method is running may be degraded.

### Example: Generating a

Static Image for Background Video

Providing a single image to the background source generates a full GOP of that
static image.

Here is an example using CIImage:

```
// Create the background image source
guard let source = session.createAppBackgroundImageSource(withAttemptTrim: true, onComplete: { error in
    print("Background Video Generation Done - Error: \(error.debugDescription)")
}) else {
    return
}

// Create a CIImage of the color red.
let ciImage = CIImage(color: .red)

// Convert the CIImage to a CVPixelBuffer
let attrs = [
    kCVPixelBufferCGImageCompatibilityKey: kCFBooleanTrue,
    kCVPixelBufferCGBitmapContextCompatibilityKey: kCFBooleanTrue,
    kCVPixelBufferMetalCompatibilityKey: kCFBooleanTrue,
] as CFDictionary

var pixelBuffer: CVPixelBuffer!
CVPixelBufferCreate(kCFAllocatorDefault,
                    videoConfig.width,
                    videoConfig.height,
                    kCVPixelFormatType_420YpCbCr8BiPlanarFullRange,
                    attrs,
                    &pixelBuffer)

let context = CIContext()
context.render(ciImage, to: pixelBuffer)

// Submit to CVPixelBuffer and finish the source
source.add(pixelBuffer)
source.finish()
```

Alternately, instead of creating a CIImage of a solid color, you can use
bundled images. The only code shown here is how to convert a UIImage to a
CIImage to use with the previous sample:

```
// Load the pre-bundled image and get it’s CGImage
guard let cgImage = UIImage(named: "image")?.cgImage else {
    return
}

// Create a CIImage from the CGImage
let ciImage = CIImage(cgImage: cgImage)
```

### Example: Video

with AVAssetImageGenerator

You can use an `AVAssetImageGenerator` to generate
`CMSampleBuffers` from an `AVAsset` (though not an HLS
stream `AVAsset`):

```
// Create the background image source
guard let source = session.createAppBackgroundImageSource(withAttemptTrim: true, onComplete: { error in
    print("Background Video Generation Done - Error: \(error.debugDescription)")
}) else {
    return
}

// Find the URL for the pre-bundled MP4 file
guard let url = Bundle.main.url(forResource: "sample-clip", withExtension: "mp4") else {
    return
}
// Create an image generator from an asset created from the URL.
let generator = AVAssetImageGenerator(asset: AVAsset(url: url))
// It is important to specify a very small time tolerance.
generator.requestedTimeToleranceAfter = .zero
generator.requestedTimeToleranceBefore = .zero

// At 30 fps, this will generate 4 seconds worth of samples.
let times: [NSValue] = (0...120).map { NSValue(time: CMTime(value: $0, timescale: CMTimeScale(config.video.targetFramerate))) }
var completed = 0

let context = CIContext(options: [.workingColorSpace: NSNull()])

// Create a pixel buffer pool to efficiently feed the source
let attrs = [
    kCVPixelBufferPixelFormatTypeKey: kCVPixelFormatType_420YpCbCr8BiPlanarFullRange,
    kCVPixelBufferCGImageCompatibilityKey: kCFBooleanTrue,
    kCVPixelBufferCGBitmapContextCompatibilityKey: kCFBooleanTrue,
    kCVPixelBufferMetalCompatibilityKey: kCFBooleanTrue,
    kCVPixelBufferWidthKey: videoConfig.width,
    kCVPixelBufferHeightKey: videoConfig.height,
] as CFDictionary
var pool: CVPixelBufferPool!
CVPixelBufferPoolCreate(kCFAllocatorDefault, nil, attrs, &pool)

generator.generateCGImagesAsynchronously(forTimes: times) { requestTime, image, actualTime, result, error in
    if let image = image {
        // convert to CIImage then CVpixelBuffer
        let ciImage = CIImage(cgImage: image)
        var pixelBuffer: CVPixelBuffer!
        CVPixelBufferPoolCreatePixelBuffer(kCFAllocatorDefault, pool, &pixelBuffer)
        context.render(ciImage, to: pixelBuffer)
        source.add(pixelBuffer)
    }
    completed += 1
    if completed == times.count {
        // Mark the source finished when all images have been processed
        source.finish()
    }
}
```

It is possible to generate `CVPixelBuffers` using an
`AVPlayer` and `AVPlayerItemVideoOutput`. However,
that requires using a `CADisplayLink` and executes closer to
real-time, while `AVAssetImageGenerator` can process the frames much
faster.

### Limitations

Your application needs the [background audio entitlement](https://developer.apple.com/documentation/xcode/configuring-background-execution-modes "https://developer.apple.com/documentation/xcode/configuring-background-execution-modes") to avoid getting suspended after going
into the background.

`createAppBackgroundImageSource` can be called only while your
application is in the foreground, since it needs access to the GPU to
complete.

`createAppBackgroundImageSource` always encodes to a full GOP. For
example, if you have a keyframe interval of 2 seconds (the default) and are
running at 30 fps, it encodes a multiple of 60 frames.

- If fewer than 60 frames are provided, the last frame is repeated until
  60 frames are reached, regardless of the trim option’s value.
- If more than 60 frames are provided and the trim option is
  `true`, the last N frames are dropped, where N is the
  remainder of the total number of submitted frames divided by 60.
- If more than 60 frames are provided and the trim option is
  `false`, the last frame is repeated until the next
  multiple of 60 frames is reached.
