# Advanced Use Cases for the IVS Android Broadcast SDK |

Low-Latency Streaming

Here we present some advanced use cases. Start with the basic setup above and continue
here.

## Create a Broadcast

Configuration

Here we create a custom configuration with two mixer slots that allow us to bind
two video sources to the mixer. One (`custom`) is full screen and laid
out behind the other (`camera`), which is smaller and in the bottom-right
corner. Note that for the `custom` slot we do not set a position, size,
or aspect mode. Because we do not set these parameters, the slot will use the video
settings for size and position.

```
BroadcastConfiguration config = BroadcastConfiguration.with($ -> {
    $.audio.setBitrate(128_000);
    $.video.setMaxBitrate(3_500_000);
    $.video.setMinBitrate(500_000);
    $.video.setInitialBitrate(1_500_000);
    $.video.setSize(1280, 720);
    $.mixer.slots = new BroadcastConfiguration.Mixer.Slot[] {
            BroadcastConfiguration.Mixer.Slot.with(slot -> {
                // Do not automatically bind to a source
                slot.setPreferredAudioInput(
                           Device.Descriptor.DeviceType.UNKNOWN);
                // Bind to user image if unbound
                slot.setPreferredVideoInput(
                           Device.Descriptor.DeviceType.USER_IMAGE);
                slot.setName("custom");
                return slot;
            }),
            BroadcastConfiguration.Mixer.Slot.with(slot -> {
                slot.setzIndex(1);
                slot.setAspect(BroadcastConfiguration.AspectMode.FILL);
                slot.setSize(300, 300);
                slot.setPosition($.video.getSize().x - 350,
                        $.video.getSize().y - 350);
                slot.setName("camera");
                return slot;
            })
    };
    return $;
});
```

## Create the Broadcast

Session (Advanced Version)

Create a `BroadcastSession` as you did in the [basic example](broadcast-android-getting-started.md#broadcast-android-create-session "broadcast-android-getting-started.md#broadcast-android-create-session"), but provide
your custom configuration here. Also provide `null` for the device array,
as we will add those manually.

```
// Create a broadcast-session instance and sign up to receive broadcast
// events and errors.
Context ctx = getApplicationContext();
broadcastSession = new BroadcastSession(ctx,
                       broadcastListener,
                       config, // The configuration we created above
                       null); // We’ll manually attach devices after
```

## Iterate and Attach a Camera

Device

Here we iterate through input devices that the SDK has detected. On Android 7
(Nougat) this will only return default microphone devices, because the Amazon IVS
Broadcast SDK does not support selecting non-default devices on this version of
Android.

Once we find a device that we want to use, we call `attachDevice` to
attach it. A lambda function is called on the main thread when attaching the input
device has completed. In case of failure, you will receive an error in the
Listener.

```
for(Device.Descriptor desc: BroadcastSession.listAvailableDevices(getApplicationContext())) {
    if(desc.type == Device.Descriptor.DeviceType.CAMERA &&
            desc.position == Device.Descriptor.Position.FRONT) {
        session.attachDevice(desc, device -> {
            LinearLayout previewHolder = findViewById(R.id.previewHolder);
            ImagePreviewView preview = ((ImageDevice)device).getPreviewView();
            preview.setLayoutParams(new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.MATCH_PARENT));
            previewHolder.addView(preview);
            // Bind the camera to the mixer slot we created above.
            session.getMixer().bind(device, "camera");
        });
        break;
    }
}
```

## Swap Cameras

```
// This assumes you’ve kept a reference called "currentCamera" that points to
// a front facing camera
for(Device device: BroadcastSession.listAvailableDevices()) {
   if(device.type == Device.Descriptor.DeviceType.CAMERA &&
          Device.position != currentCamera.position) {
        // Remove the preview view for the old device.
        // setImagePreviewTextureView is an example function
        // that handles your view hierarchy.
        setImagePreviewView(null);
        session.exchangeDevices(currentCamera, device, camera -> {
             // Set the preview view for the new device.
             setImagePreviewView(camera.getPreviewView());
             currentCamera = camera;
        });
        break;
   }
}
```

## Create an Input

Surface

To input sound or image data that your app generates, use
`createImageInputSource` or `createAudioInputSource`. Both
these methods create and attach virtual devices that can be bound to the mixer like
any other device.

The `SurfaceSource` returned by `createImageInputSource` has
a `getInputSurface` method, which will give you a `Surface`
that you can use with the Camera2 API, OpenGL, or Vulkan, or anything else that can
write to a Surface.

The `AudioDevice` returned by `createAudioInputSource` can
receive Linear PCM data generated by AudioRecorder or other means.

```
SurfaceSource source = session.createImageInputSource();
Surface surface = source.getInputSurface();
session.getMixer().bind(source, “custom”);
```

## Detach a Device

If you want to detach and not replace a device, detach it with `Device`
or `Device.Descriptor`.

```
session.detachDevice(currentCamera);
```

## Screen and System Audio

Capture

The Amazon IVS Broadcast SDK for Android includes some helpers that simplify
capturing the device’s screen (Android 6 and higher) and system audio (Android 10
and higher). If you want to manage these manually, you can create a custom
image-input source and a custom audio-input source.

To create a screen and system audio-capture session, you must first create a
permission-request intent:

```
public void startScreenCapture() {
    MediaProjectionManager manager =
                         (MediaProjectionManager) getApplicationContext()
                         .getSystemService(Context.MEDIA_PROJECTION_SERVICE);
    if(manager != null) {
        Intent intent = manager.createScreenCaptureIntent();
        startActivityIfNeeded(intent, SCREEN_CAPTURE_REQUEST_ID);
    }
}
```

To use this feature, you must provide a class that extends
`com.amazonaws.ivs.broadcast.SystemCaptureService`. You do not have
to override any of its methods, but the class needs to be there to avoid any
potential collisions between services.

You also must add a couple of elements to your Android manifest:

```
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<application ...>
    <service android:name=".ExampleSystemCaptureService"
         android:foregroundServiceType="mediaProjection"
         android:isolatedProcess="false" />
</application>
...
```

Your class that extends `SystemCaptureService` must be named in the
`<service>` element. On Android 9 and later, the
`foregroundServiceType` must be `mediaProjection`.

Once the permissions intent has returned, you may proceed with creating the screen
and system audio-capture session. On Android 8 and later, you must provide a
notification to be displayed in your user’s Notification Panel. The Amazon IVS
Broadcast SDK for Android provides the convenience method
`createServiceNotificationBuilder`. Alternately, you may provide your
own notification.

```
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if(requestCode != SCREEN_CAPTURE_REQUEST_ID
       || Activity.RESULT_OK != resultCode) {
        return;
    }
    Notification notification = null;
    if(Build.VERSION.SDK_INT >= 26) {
        Intent intent = new Intent(getApplicationContext(),
                                   NotificationActivity.class);
        notification = session
                         .createServiceNotificationBuilder("example",
                                            "example channel", intent)
                         .build();
    }
    session.createSystemCaptureSources(data,
                  ExampleSystemCaptureService.class,
                  Notification,
                  devices -> {
        // This step is optional if the mixer slots have been given preferred
        // input device types SCREEN and SYSTEM_AUDIO
        for (Device device : devices) {
            session.getMixer().bind(device, "game");
        }
    });
}
```

## Get Recommended Broadcast

Settings

To evaluate your user’s connection before starting a broadcast, use the
`recommendedVideoSettings` method to run a brief test. As the test
runs, you will receive several recommendations, ordered from most to least
recommended. In this version of the SDK, it is not possible to reconfigure the
current `BroadcastSession`, so you will need to `release()` it
and then create a new one with the recommended settings. You will continue to
receive `BroadcastSessionTest.Results` until the
`Result.status` is `SUCCESS` or `ERROR`. You
can check progress with `Result.progress`.

Amazon IVS supports a maximum bitrate of 8.5 Mbps (for channels whose
`type` is `STANDARD` or `ADVANCED`), so the
`maximumBitrate` returned by this method never exceeds 8.5 Mbps. To
account for small fluctuations in network performance, the recommended
`initialBitrate` returned by this method is slightly less than the
true bitrate measured in the test. (Using 100% of the available bandwidth usually is
inadvisable.)

```
void runBroadcastTest() {
    this.test = session.recommendedVideoSettings(RTMPS_ENDPOINT, RTMPS_STREAMKEY,
        result -> {
            if (result.status == BroadcastSessionTest.Status.SUCCESS) {
                this.recommendation = result.recommendations[0];
            }
        });
}
```

## Using Auto-Reconnect

IVS supports automatic reconnection to a broadcast if the broadcast stops unexpectedly without calling the `stop` API; e.g., a temporary loss in network connectivity. To enable auto-reconnect, call `setEnabled(true)` on `BroadcastConfiguration.autoReconnect`.

When something causes the stream to unexpectedly stop, the SDK retries up to 5 times, following a linear backoff strategy. It notifies your application about the retry state through the `BroadcastSession.Listener.onRetryStateChanged` method.

Behind the scenes, auto-reconnect uses IVS [stream-takeover](streaming-config.md#streaming-config-stream-takeover "streaming-config.md#streaming-config-stream-takeover") functionality by appending a priority number, starting with 1, to the end of the provided stream key. For the duration of the `BroadcastSession` instance, that number is incremented by 1 each time a reconnect is attempted. This means if the device’s connection is lost 4 times during a broadcast, and each loss requires 1-4 retry attempts, the priority of the last stream up could be anywhere between 5 and 17. Because of this, _we recommend you do not use IVS stream takeover from another device while auto-reconnect is enabled in the SDK for the same channel_. There are no guarantees what priority the SDK is using at the time, and the SDK will try to reconnect with a higher priority if another device takes over.

## Using Bluetooth

Microphones

To broadcast using Bluetooth microphone devices, you must start a Bluetooth SCO
connection:

```
Bluetooth.startBluetoothSco(context);
// Now bluetooth microphones can be used
…
// Must also stop bluetooth SCO
Bluetooth.stopBluetoothSco(context);
```
