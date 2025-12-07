# Getting Started​ with the IVS Web Broadcast SDK | Low-Latency Streaming

This document takes you through the steps involved in getting started with the Amazon IVS low-latency streaming Web broadcast SDK.

## Install the Library​

Note that the IVSBroadcastClient leverages [reflect-metadata](https://www.npmjs.com/package/reflect-metadata "https://www.npmjs.com/package/reflect-metadata"),
which extends the global Reflect object. Although this should not create any
conflicts, there may be rare instances where this could cause unwanted
behavior.

### Using a Script

Tag​

The Web broadcast SDK is distributed as a JavaScript library and can be
retrieved at [https://web-broadcast.live-video.net/1.31.0/amazon-ivs-web-broadcast.js](https://web-broadcast.live-video.net/1.31.0/amazon-ivs-web-broadcast.js "https://web-broadcast.live-video.net/1.31.0/amazon-ivs-web-broadcast.js").

When loaded via `<script>` tag, the library exposes a global
variable in the window scope named `IVSBroadcastClient`.

### Using npm​

To install the `npm` package:

```
npm install amazon-ivs-web-broadcast
```

You can now access the `IVSBroadcastClient` object and pull in
other modules and consts such as `Errors`,
`BASIC_LANDSCAPE`:

```
import IVSBroadcastClient, {
   Errors,
   BASIC_LANDSCAPE
} from 'amazon-ivs-web-broadcast';
```

## Samples

To get started quickly, see the examples below:

- [Single broadcast to
  an IVS channel (HTML and JavaScript)](https://codepen.io/amazon-ivs/pen/poLRoPp "https://codepen.io/amazon-ivs/pen/poLRoPp")
- [Single broadcast with screen share
  to an IVS channel](https://stream.ivs.rocks/ "https://stream.ivs.rocks/") ([React
  Source Code](https://github.com/aws-samples/amazon-ivs-broadcast-web-demo "https://github.com/aws-samples/amazon-ivs-broadcast-web-demo"))

## Create an Instance of the

AmazonIVSBroadcastClient​

To use the library, you must create an instance of the client. You can
do that by calling the `create` method on `IVSBroadcastClient`
with the `streamConfig` parameter (specifying constraints of your
broadcast like resolution and framerate). You can specify the ingest endpoint when
creating the client or you can set this when you start a stream.

The ingest endpoint can be found in the AWS Console or returned by the
CreateChannel operation (e.g., UNIQUE_ID.global-contribute.live-video.net).

```
const client = IVSBroadcastClient.create({
   // Enter the desired stream configuration
   streamConfig: IVSBroadcastClient.BASIC_LANDSCAPE,
   // Enter the ingest endpoint from the AWS console or CreateChannel API
   ingestEndpoint: 'UNIQUE_ID.global-contribute.live-video.net',
});
```

These are the common supported stream configurations. Presets are
`BASIC` up to 480p and 1.5 Mbps bitrate, BASIC Full HD up to 1080p
and 3.5 Mbps bitrate, and `STANDARD` (or `ADVANCED`) up to
1080p and 8.5 Mbps bitrate. You can customize the bitrate, frame rate, and
resolution if desired. For more information, see [BroadcastClientConfig](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/BroadcastClientConfig "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/BroadcastClientConfig").

```
IVSBroadcastClient.BASIC_LANDSCAPE;
IVSBroadcastClient.BASIC_FULL_HD_LANDSCAPE;
IVSBroadcastClient.STANDARD_LANDSCAPE;
IVSBroadcastClient.BASIC_PORTRAIT;
IVSBroadcastClient.BASIC_FULL_HD_PORTRAIT;
IVSBroadcastClient.STANDARD_PORTRAIT;
```

You can import these individually if using the `npm`
package.

Note: Make sure that your client-side configuration aligns with the back-end
channel type. For instance, if the channel type is `STANDARD`,
`streamConfig` should be set to one of the
`IVSBroadcastClient.STANDARD_*` values. If channel type is
`ADVANCED`, you’ll need to set the configuration manually as shown
below (using `ADVANCED_HD` as an example):

```
const client = IVSBroadcastClient.create({
   // Enter the custom stream configuration
   streamConfig: {
      maxResolution: {
         width: 1080,
         height: 1920,
     },
     maxFramerate: 30,
     /**
      * maxBitrate is measured in kbps
      */
     maxBitrate: 3500,
   },
   // Other configuration . . .
});
```

## Request Permissions

Your app must request permission to access the user’s camera and
microphone, and it must be served using HTTPS. (This is not specific to Amazon IVS;
it is required for any website that needs access to cameras and microphones.)

Here's an example function showing how you can request and capture
permissions for both audio and video devices:

```
async function handlePermissions() {
   let permissions = {
       audio: false,
       video: false,
   };
   try {
       const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
       for (const track of stream.getTracks()) {
           track.stop();
       }
       permissions = { video: true, audio: true };
   } catch (err) {
       permissions = { video: false, audio: false };
       console.error(err.message);
   }
   // If we still don't have permissions after requesting them display the error message
   if (!permissions.video) {
       console.error('Failed to get video permissions.');
   } else if (!permissions.audio) {
       console.error('Failed to get audio permissions.');
   }
}
```

For additional information, see the [Permissions API](https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API "https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API") and [MediaDevices.getUserMedia()](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia "https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia").

## Set Up a Stream

Preview

To preview what will be broadcast, provide the SDK with a `<canvas>`
element.

```
// where #preview is an existing <canvas> DOM element on your page
const previewEl = document.getElementById('preview');
client.attachPreview(previewEl);
```

## List Available Devices

To see what devices are available to capture, query the browser's [MediaDevices.enumerateDevices()](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/enumerateDevices "https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/enumerateDevices") method:

```
const devices = await navigator.mediaDevices.enumerateDevices();
window.videoDevices = devices.filter((d) => d.kind === 'videoinput');
window.audioDevices = devices.filter((d) => d.kind === 'audioinput');
```

## Retrieve a MediaStream from a

Device

After acquiring the list of available devices, you can retrieve a stream
from any number of devices. For example, you can use the `getUserMedia()`
method to retrieve a stream from a camera.

If you'd like to specify which device to capture the stream from, you
can explicitly set the `deviceId` in the `audio` or
`video` section of the media constraints. Alternately, you can omit
the `deviceId` and have users select their devices from the browser
prompt.

You also can specify an ideal camera resolution using the `width` and
`height` constraints. (Read more about these constraints [here](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints#properties_of_video_tracks "https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints#properties_of_video_tracks").) The SDK automatically applies width and height constraints that
correspond to your maximum broadcast resolution; however, it's a good idea to also
apply these yourself to ensure that the source aspect ratio is not changed after you
add the source to the SDK.

```
const streamConfig = IVSBroadcastClient.BASIC_LANDSCAPE;
...
window.cameraStream = await navigator.mediaDevices.getUserMedia({
   video: {
       deviceId: window.videoDevices[0].deviceId,
       width: {
           ideal: streamConfig.maxResolution.width,
       },
       height: {
           ideal: streamConfig.maxResolution.height,
       },
   },
});
window.microphoneStream = await navigator.mediaDevices.getUserMedia({
   audio: { deviceId: window.audioDevices[0].deviceId },
});
```

## Add Device to a Stream

After acquiring the stream, you may add devices to the layout by
specifying a unique name (below, this is `camera1`) and composition
position (for video). For example, by specifying your webcam device, you add your
webcam video source to the broadcast stream.

When specifying the video-input device, you must specify the index,
which represents the “layer” on which you want to broadcast. This is synonymous to
image editing or CSS, where a z-index represents the ordering of layers to render.
Optionally, you can provide a position, which defines the x/y coordinates (as well
as the size) of the stream source.

For details on parameters, see [VideoComposition](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/VideoComposition "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/VideoComposition").

```
client.addVideoInputDevice(window.cameraStream, 'camera1', { index: 0 }); // only 'index' is required for the position parameter
client.addAudioInputDevice(window.microphoneStream, 'mic1');
```

## Start a Broadcast

To start a broadcast, provide the stream key for your Amazon IVS channel:

```
client
   .startBroadcast(streamKey)
   .then((result) => {
       console.log('I am successfully broadcasting!');
   })
   .catch((error) => {
       console.error('Something drastically failed while broadcasting!', error);
   });
```

## Stop a Broadcast

```
client.stopBroadcast();
```

## Swap Video Positions

The client supports swapping the composition positions of video devices:

```
client.exchangeVideoDevicePositions('camera1', 'camera2');
```

## Mute Audio

To mute audio, either remove the audio device using
`removeAudioInputDevice` or set the `enabled` property on
the audio track:

```
let audioStream = client.getAudioInputDevice(AUDIO_DEVICE_NAME);
audioStream.getAudioTracks()[0].enabled = false;
```

Where `AUDIO_DEVICE_NAME` is the name given to the original audio
device during the `addAudioInputDevice()` call.

To unmute:

```
let audioStream = client.getAudioInputDevice(AUDIO_DEVICE_NAME);
audioStream.getAudioTracks()[0].enabled = true;
```

## Hide Video

To hide video, either remove the video device using
`removeVideoInputDevice` or set the `enabled` property on
the video track:

```
let videoStream = client.getVideoInputDevice(VIDEO_DEVICE_NAME).source;
videoStream.getVideoTracks()[0].enabled = false;
```

Where `VIDEO_DEVICE_NAME` is the name given to the video device during
the original `addVideoInputDevice()` call.

To unhide:

```
let videoStream = client.getVideoInputDevice(VIDEO_DEVICE_NAME).source;
videoStream.getVideoTracks()[0].enabled = true;
```
