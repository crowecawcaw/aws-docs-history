# Getting Started​ with the IVS Web

Broadcast SDK | Real-Time Streaming

This document takes you through the steps involved in getting started with the IVS
real-time streaming Web broadcast SDK.

## Imports

The building blocks for real-time are located in a different namespace than the
root broadcasting modules.

### Using a Script

Tag

The Web broadcast SDK is distributed as a JavaScript library and can be
retrieved at [https://web-broadcast.live-video.net/1.29.0/amazon-ivs-web-broadcast.js](https://web-broadcast.live-video.net/1.29.0/amazon-ivs-web-broadcast.js "https://web-broadcast.live-video.net/1.29.0/amazon-ivs-web-broadcast.js").

The classes and enums defined in the examples below can be found on the global
object `IVSBroadcastClient`:

```
const { Stage, SubscribeType } = IVSBroadcastClient;
```

### Using npm

To install the `npm` package:

```
npm install amazon-ivs-web-broadcast
```

The classes, enums, and types also can be imported from the package
module:

```
import { Stage, SubscribeType, LocalStageStream } from 'amazon-ivs-web-broadcast'
```

### Server-Side Rendering Support

The Web Broadcast SDK Stages library cannot be loaded in a server-side
context, as it references browser primitives necessary to the functioning of the
library when loaded. To work around this, load the library dynamically, as
demonstrated in the [Web Broadcast Demo using Next and React](https://github.com/aws-samples/amazon-ivs-broadcast-web-demo/blob/main/hooks/useBroadcastSDK.js#L26-L31 "https://github.com/aws-samples/amazon-ivs-broadcast-web-demo/blob/main/hooks/useBroadcastSDK.js#L26-L31").

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

For real-time streaming, ensure that media is constrained to 720p resolution.
Specifically, your `getUserMedia` and `getDisplayMedia`
constraint values for width and height must not exceed 921600 (1280\*720) when
multiplied together.

```
const videoConfiguration = {
  maxWidth: 1280,
  maxHeight: 720,
  maxFramerate: 30,
}

window.cameraStream = await navigator.mediaDevices.getUserMedia({
   video: {
       deviceId: window.videoDevices[0].deviceId,
       width: {
           ideal: videoConfiguration.maxWidth,
       },
       height: {
           ideal:videoConfiguration.maxHeight,
       },
   },
});
window.microphoneStream = await navigator.mediaDevices.getUserMedia({
   audio: { deviceId: window.audioDevices[0].deviceId },
});
```
