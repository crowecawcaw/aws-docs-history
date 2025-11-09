# Publishing & Subscribing with the IVS Web

Broadcast SDK | Real-Time Streaming

This document takes you through the steps involved in publishing and subscribing to a
stage using the IVS real-time streaming Web broadcast SDK.

## Concepts

Three core concepts underlie real-time functionality: [stage](#web-publish-subscribe-concepts-stage "#web-publish-subscribe-concepts-stage"), [strategy](#web-publish-subscribe-concepts-strategy "#web-publish-subscribe-concepts-strategy"), and [events](#web-publish-subscribe-concepts-events "#web-publish-subscribe-concepts-events"). The design goal
is minimizing the amount of client-side logic necessary to build a working
product.

### Stage

The `Stage` class is the main point of interaction between the host
application and the SDK. It represents the stage itself and is used to join and
leave the stage. Creating and joining a stage requires a valid, unexpired token
string from the control plane (represented as `token`). Joining and
leaving a stage are simple:

```
const stage = new Stage(token, strategy)

try {
   await stage.join();
} catch (error) {
   // handle join exception
}

stage.leave();
```

### Strategy

The `StageStrategy` interface provides a way for the host
application to communicate the desired state of the stage to the SDK. Three
functions need to be implemented: `shouldSubscribeToParticipant`,
`shouldPublishParticipant`, and
`stageStreamsToPublish`. All are discussed below.

To use a defined strategy, pass it to the `Stage` constructor. The
following is a complete example of an application using a strategy to publish a
participant's webcam to the stage and subscribe to all participants. Each
required strategy function's purpose is explained in detail in the subsequent
sections.

```
const devices = await navigator.mediaDevices.getUserMedia({
   audio: true,
   video: {
        width: { max: 1280 },
        height: { max: 720 },
    }
});
const myAudioTrack = new LocalStageStream(devices.getAudioTracks()[0]);
const myVideoTrack = new LocalStageStream(devices.getVideoTracks()[0]);

// Define the stage strategy, implementing required functions
const strategy = {
   audioTrack: myAudioTrack,
   videoTrack: myVideoTrack,

   // optional
   updateTracks(newAudioTrack, newVideoTrack) {
      this.audioTrack = newAudioTrack;
      this.videoTrack = newVideoTrack;
   },

   // required
   stageStreamsToPublish() {
      return [this.audioTrack, this.videoTrack];
   },

   // required
   shouldPublishParticipant(participant) {
      return true;
   },

   // required
   shouldSubscribeToParticipant(participant) {
      return SubscribeType.AUDIO_VIDEO;
   }
};

// Initialize the stage and start publishing
const stage = new Stage(token, strategy);
await stage.join();


// To update later (e.g. in an onClick event handler)
strategy.updateTracks(myNewAudioTrack, myNewVideoTrack);
stage.refreshStrategy();
```

#### Subscribing to Participants

```
shouldSubscribeToParticipant(participant: StageParticipantInfo): SubscribeType
```

When a remote participant joins the stage, the SDK queries the host
application about the desired subscription state for that participant. The
options are `NONE`, `AUDIO_ONLY`, and
`AUDIO_VIDEO`. When returning a value for this function, the
host application does not need to worry about the publish state, current
subscription state, or stage connection state. If `AUDIO_VIDEO`
is returned, the SDK waits until the remote participant is publishing before
it subscribes, and it updates the host application by emitting events
throughout the process.

Here is a sample implementation:

```
const strategy = {

   shouldSubscribeToParticipant: (participant) => {
      return SubscribeType.AUDIO_VIDEO;
   }

   // ... other strategy functions
}
```

This is the complete implementation of this function for a host
application that always wants all participants to see each other; e.g., a
video chat application.

More advanced implementations also are possible. For example, assume the
application provides a `role` attribute when creating the token
with CreateParticipantToken. The application could use the
`attributes` property on `StageParticipantInfo` to
selectively subscribe to participants based on the server-provided
attributes:

```
const strategy = {

   shouldSubscribeToParticipant(participant) {
      switch (participant.attributes.role) {
         case 'moderator':
            return SubscribeType.NONE;
         case 'guest':
            return SubscribeType.AUDIO_VIDEO;
         default:
            return SubscribeType.NONE;
      }
   }
   // . . . other strategies properties
}
```

This can be used to create a stage where moderators can monitor all guests
without being seen or heard themselves. The host application could use
additional business logic to let moderators see each other but remain
invisible to guests.

#### Configuration for Subscribing to Participants

```
subscribeConfiguration(participant: StageParticipantInfo): SubscribeConfiguration
```

If a remote participant is being subscribed to (see [Subscribing to Participants](#web-publish-subscribe-concepts-strategy-participants "#web-publish-subscribe-concepts-strategy-participants")), the SDK queries the host
application about a custom subscribe configuration for that participant.
This configuration is optional and allows the host application to control
certain aspects of subscriber behavior. For information on what can be
configured, see [SubscribeConfiguration](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/SubscribeConfiguration "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/SubscribeConfiguration") in the SDK reference
documentation.

Here is a sample implementation:

```
const strategy = {

   subscribeConfiguration: (participant) => {
      return {
         jitterBuffer: {
            minDelay: JitterBufferMinDelay.MEDIUM
         }
      }

   // ... other strategy functions
}
```

This implementation updates the jitter-buffer minimum delay for all
subscribed participants to a preset of `MEDIUM`.

As with `shouldSubscribeToParticipant`, more advanced
implementations are possible. The given `ParticipantInfo` can be
used to selectively update the subscribe configuration for specific
participants.

We recommend using the default behaviors. Specify custom configuration
only if there is a particular behavior you want to change.

#### Publishing

```
shouldPublishParticipant(participant: StageParticipantInfo): boolean
```

Once connected to the stage, the SDK queries the host application to see
if a particular participant should publish. This is invoked only on local
participants that have permission to publish based on the provided
token.

Here is a sample implementation:

```
const strategy = {

   shouldPublishParticipant: (participant) => {
      return true;
   }

   // . . . other strategies properties
}
```

This is for a standard video chat application where users always want to
publish. They can mute and unmute their audio and video, to instantly be
hidden or seen/heard. (They also can use publish/unpublish, but that is much
slower. Mute/unmute is preferable for use cases where changing visibility
often is desirable.)

#### Choosing

Streams to Publish

```
stageStreamsToPublish(): LocalStageStream[];
```

When publishing, this is used to determine what audio and video streams should
be published. This is covered in more detail later in [Publish a Media
Stream](#web-publish-subscribe-publish-stream "#web-publish-subscribe-publish-stream").

#### Updating

the Strategy

The strategy is intended to be dynamic: the values returned from any of
the above functions can be changed at any time. For example, if the host
application does not want to publish until the end user taps a button, you
could return a variable from `shouldPublishParticipant`
(something like `hasUserTappedPublishButton`). When that variable
changes based on an interaction by the end user, call
`stage.refreshStrategy()` to signal to the SDK that it should
query the strategy for the latest values, applying only things that have
changed. If the SDK observes that the `shouldPublishParticipant`
value has changed, it starts the publish process. If the SDK queries and all
functions return the same value as before, the `refreshStrategy`
call does not modify the stage.

If the return value of `shouldSubscribeToParticipant` changes
from `AUDIO_VIDEO` to `AUDIO_ONLY`, the video stream
is removed for all participants with changed returned values, if a video
stream existed previously.

Generally, the stage uses the strategy to most efficiently apply the
difference between the previous and current strategies, without the host
application needing to worry about all the state required to manage it
properly. Because of this, think of calling
`stage.refreshStrategy()` as a cheap operation, because it
does nothing unless the strategy changes.

### Events

A `Stage` instance is an event emitter. Using
`stage.on()`, the state of the stage is communicated to the host
application. Updates to the host application’s UI usually can be supported
entirely by the events. The events are as follows:

```
stage.on(StageEvents.STAGE_CONNECTION_STATE_CHANGED, (state) => {})
stage.on(StageEvents.STAGE_PARTICIPANT_JOINED, (participant) => {})
stage.on(StageEvents.STAGE_PARTICIPANT_LEFT, (participant) => {})
stage.on(StageEvents.STAGE_PARTICIPANT_PUBLISH_STATE_CHANGED, (participant, state) => {})
stage.on(StageEvents.STAGE_PARTICIPANT_SUBSCRIBE_STATE_CHANGED, (participant, state) => {})
stage.on(StageEvents.STAGE_PARTICIPANT_STREAMS_ADDED, (participant, streams) => {})
stage.on(StageEvents.STAGE_PARTICIPANT_STREAMS_REMOVED, (participant, streams) => {})
stage.on(StageEvents.STAGE_STREAM_ADAPTION_CHANGED, (participant, stream, isAdapting) => ())
stage.on(StageEvents.STAGE_STREAM_LAYERS_CHANGED, (participant, stream, layers) => ())
stage.on(StageEvents.STAGE_STREAM_LAYER_SELECTED, (participant, stream, layer, reason) => ())
stage.on(StageEvents.STAGE_STREAM_MUTE_CHANGED, (participant, stream) => {})
stage.on(StageEvents.STAGE_STREAM_SEI_MESSAGE_RECEIVED, (participant, stream) => {})
```

For most of these events, the corresponding `ParticipantInfo` is
provided.

It is not expected that the information provided by the events impacts the
return values of the strategy. For example, the return value of
`shouldSubscribeToParticipant` is not expected to change when
`STAGE_PARTICIPANT_PUBLISH_STATE_CHANGED` is called. If the host
application wants to subscribe to a particular participant, it should return the
desired subscription type regardless of that participant’s publish state. The
SDK is responsible for ensuring that the desired state of the strategy is acted
on at the correct time based on the state of the stage.

## Publish a Media

Stream

Local devices like microphones and cameras are retrieved using the same steps as
outlined above in [Retrieve a
MediaStream from a Device](broadcast-web-getting-started.md#broadcast-web-retrieve-mediastream "broadcast-web-getting-started.md#broadcast-web-retrieve-mediastream")​. In the example we use
`MediaStream` to create a list of `LocalStageStream`
objects used for publishing by the SDK:

```
try {
    // Get stream using steps outlined in document above
    const stream = await getMediaStreamFromDevice();

    let streamsToPublish = stream.getTracks().map(track => {
        new LocalStageStream(track)
    });

    // Create stage with strategy, or update existing strategy
    const strategy = {
        stageStreamsToPublish: () => streamsToPublish
    }
}
```

## Publish a

Screenshare

Applications often need to publish a screenshare in addition to the user's web
camera. Publishing a screenshare necessitates creating an additional token for the
stage, specifically for publishing the screenshare's media. Use
`getDisplayMedia` and constrain the resolution to a maximum of 720p.
After that, the steps are similar to publishing a camera to the stage.

```
// Invoke the following lines to get the screenshare's tracks
const media = await navigator.mediaDevices.getDisplayMedia({
   video: {
      width: {
         max: 1280,
      },
      height: {
         max: 720,
      }
   }
});
const screenshare = { videoStream: new LocalStageStream(media.getVideoTracks()[0]) };
const screenshareStrategy = {
   stageStreamsToPublish: () => {
      return [screenshare.videoStream];
   },
   shouldPublishParticipant: (participant) => {
      return true;
   },
   shouldSubscribeToParticipant: (participant) => {
      return SubscribeType.AUDIO_VIDEO;
   }
}
const screenshareStage = new Stage(screenshareToken, screenshareStrategy);
await screenshareStage.join();
```

## Display and Remove

Participants

After subscribing is completed, you receive an array of `StageStream`
objects through the `STAGE_PARTICIPANT_STREAMS_ADDED` event. The event
also gives you participant info to help when displaying media streams:

```
stage.on(StageEvents.STAGE_PARTICIPANT_STREAMS_ADDED, (participant, streams) => {
    let streamsToDisplay = streams;

    if (participant.isLocal) {
        // Ensure to exclude local audio streams, otherwise echo will occur
        streamsToDisplay = streams.filter(stream => stream.streamType === StreamType.VIDEO)
    }

    // Create or find video element already available in your application
    const videoEl = getParticipantVideoElement(participant.id);

    // Attach the participants streams
    videoEl.srcObject = new MediaStream();
    streamsToDisplay.forEach(stream => videoEl.srcObject.addTrack(stream.mediaStreamTrack));
})
```

When a participant stops publishing or is unsubscribed from a stream, the
`STAGE_PARTICIPANT_STREAMS_REMOVED` function is called with the
streams that were removed. Host applications should use this as a signal to remove
the participant’s video stream from the DOM.

`STAGE_PARTICIPANT_STREAMS_REMOVED` is invoked for all scenarios in
which a stream might be removed, including:

- The remote participant stops publishing.
- A local device unsubscribes or changes subscription from
  `AUDIO_VIDEO` to `AUDIO_ONLY`.
- The remote participant leaves the stage.
- The local participant leaves the stage.

Because `STAGE_PARTICIPANT_STREAMS_REMOVED` is invoked for all
scenarios, no custom business logic is required around removing participants from
the UI during remote or local leave operations.

## Mute and Unmute Media

Streams

`LocalStageStream` objects have a `setMuted` function that
controls whether the stream is muted. This function can be called on the stream
before or after it is returned from the `stageStreamsToPublish` strategy
function.

**Important**: If a new `LocalStageStream`
object instance is returned by `stageStreamsToPublish` after a call to
`refreshStrategy`, the mute state of the new stream object is applied
to the stage. Be careful when creating new `LocalStageStream` instances
to make sure the expected mute state is maintained.

## Monitor Remote Participant Media

Mute State

When participants change the mute state of their video or audio, the
`STAGE_STREAM_MUTE_CHANGED` event is triggered with a list of streams
that have changed. Use the `isMuted` property on `StageStream`
to update your UI accordingly:

```
stage.on(StageEvents.STAGE_STREAM_MUTE_CHANGED, (participant, stream) => {
   if (stream.streamType === 'video' && stream.isMuted) {
       // handle UI changes for video track getting muted
   }
})
```

Also, you can look at [StageParticipantInfo](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference#stageparticipantinfo "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference#stageparticipantinfo") for state information on whether audio or video is
muted:

```
stage.on(StageEvents.STAGE_STREAM_MUTE_CHANGED, (participant, stream) => {
   if (participant.videoStopped || participant.audioMuted) {
       // handle UI changes for either video or audio
   }
})
```

## Get WebRTC Statistics

The `requestQualityStats()` method provides access to detailed WebRTC
statistics for both local and remote streams. This is available on both
LocalStageStream and RemoteStageStream objects. It returns comprehensive quality
metrics including network quality, packet statistics, bitrate information, and
frame-related metrics.

This is an asynchronous method with which you can retrieve statistics either via
await or by chaining a promise. It returns `undefined` when statistics
are not available; e.g., the stream is not active or internal statistics are
unavailable. If statistics are available, and depending on the stream (remote or
local, video or audio), the method returns a [LocalVideoStats](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/LocalVideoStats "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/LocalVideoStats"), [LocalAudioStats](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/LocalAudioStats "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/LocalAudioStats"), [RemoteVideoStats](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/RemoteVideoStats "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/RemoteVideoStats"), or [RemoteAudioStats](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/RemoteAudioStats "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/RemoteAudioStats") object.

Note that for video streams with simulcast, the array contains multiple stat
objects (one per layer).

**Best Practices**

- Polling frequency — Call `requestQualityStats()`
  at reasonable intervals (1-5 seconds) to avoid performance impact
- Error handling — Always check if the returned value is
  `undefined` before processing
- Memory management — Clear intervals/timeouts when streams are
  no longer needed
- Network quality — Use `networkQuality` for user
  feedback regarding possible degradations caused by the network. For
  details, see [NetworkQuality](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/enumerations/NetworkQuality "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/enumerations/NetworkQuality").

**Example Usage**

```
// For local streams
const localStats = await localVideoStream.requestQualityStats();
const audioStats = await localAudioStream.requestQualityStats();

// For remote streams
const remoteVideoStats = await remoteVideoStream.requestQualityStats();
const remoteAudioStats = await remoteAudioStream.requestQualityStats();

// Example: Monitor stats every 10 seconds
const statsInterval = setInterval(async () => {
   const stats = await localVideoStream.requestQualityStats();
   if (stats) {
      // Note: If simulcast is enabled, you may receive multiple
      // stats records for each layer
      stats.forEach(layer => {
         const rid = layer.rid || 'default';
         console.log(`Layer ${rid}:`, {
            active: layer.active,
            networkQuality: layer.networkQuality,
            packetsSent: layer.packetsSent,
            bytesSent: layer.bytesSent,
            resolution: `${layer.frameWidth}x${layer.frameHeight}`,
            fps: layer.framesPerSecond
         });
      });
   }
}, 10000);
```

## Optimizing Media

It's recommended to limit `getUserMedia` and
`getDisplayMedia` calls to the following constraints for the best
performance:

```
const CONSTRAINTS = {
    video: {
        width: { ideal: 1280 }, // Note: flip width and height values if portrait is desired
        height: { ideal: 720 },
        framerate: { ideal: 30 },
    },
};
```

You can further constrain the media through additional options passed to the
`LocalStageStream` constructor:

```
const localStreamOptions = {
    minBitrate?: number;
    maxBitrate?: number;
    maxFramerate?: number;
    simulcast: {
        enabled: boolean
    }
}
const localStream = new LocalStageStream(track, localStreamOptions)
```

In the code above:

- `minBitrate` sets a minimum bitrate that the browser should be
  expected to use. However, a low complexity video stream may push the encoder
  to go lower than this bitrate.
- `maxBitrate` sets a maximum bitrate that the browser should be
  expected to not exceed for this stream.
- `maxFramerate` sets a maximum frame rate that the browser
  should be expected to not exceed for this stream.
- The `simulcast` option is usable only on Chromium-based
  browsers. It enables sending three rendition layers of the stream.
  - This allows the server to choose which rendition to send to other
    participants, based on their networking limitations.
  - When `simulcast` is specified along with a
    `maxBitrate` and/or `maxFramerate` value,
    it is expected that the highest rendition layer will be configured
    with these values in mind, provided the `maxBitrate` does
    not go below the internal SDK’s second highest layer’s default
    `maxBitrate` value of 900 kbps.
  - If `maxBitrate` is specified as too low compared to the
    second highest layer’s default value, `simulcast` will be
    disabled.
  - `simulcast` cannot be toggled on and off without
    republishing the media through a combination of having
    `shouldPublishParticipant` return `false`,
    calling `refreshStrategy`, having
    `shouldPublishParticipant` return `true`
    and calling `refreshStrategy` again.

## Get Participant

Attributes

If you specify attributes in the `CreateParticipantToken` operation
request, you can see the attributes in `StageParticipantInfo`
properties:

```
stage.on(StageEvents.STAGE_PARTICIPANT_JOINED, (participant) => {
   console.log(`Participant ${participant.id} info:`, participant.attributes);
})
```

## Supplemental Enhancement

Information (SEI)

The Supplemental Enhancement Information (SEI) NAL unit is used to store
frame-aligned metadata alongside the video. It can be used when publishing and
subscribing to H.264 video streams. SEI payloads are not guaranteed to
arrive to subscribers, especially in bad network conditions. As the SEI payload
stores data directly within the H.264 frame structure, this capability cannot be
leveraged for audio-only streams.

### Inserting SEI

Payloads

Publishing clients can insert SEI payloads to a stage stream that is being
published by configuring their video's LocalStageStream to enable
`inBandMessaging` and subsequently invoking the
`insertSeiMessage` method. Note that enabling
`inBandMessaging` increases SDK memory usage.

Payloads must be of the [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer") type. The payload size must be greater than 0KB and
less than 1KB. The number of SEI messages inserted per second must not exceed
10KB per second.

```
const config = {
    inBandMessaging: { enabled: true }
};
const vidStream = new LocalStageStream(videoTrack, config);
const payload = new TextEncoder().encode('hello world').buffer;
vidStream.insertSeiMessage(payload);
```

#### Repeating SEI

Payloads

Optionally provide a `repeatCount` to repeat the insertion of
SEI payloads for the next N frames sent. This could be helpful to mitigate
the inherent loss that may occur due to the underlying UDP transport
protocol used to send video. Note this value must be between 0 and 30.
Receiving clients must have logic to de-duplicate the message.

```
vidStream.insertSeiMessage(payload, { repeatCount: 5 }); // Optional config, repeatCount must be between 0 and 30
```

### Reading SEI

Payloads

Subscribing clients can read SEI payloads from a publisher who is publishing
H.264 video if present by configuring the subscriber(s)
`SubscribeConfiguration` to enable `inBandMessaging`
and listening to the `StageEvents.STAGE_STREAM_SEI_MESSAGE_RECEIVED`
event, as shown in the following example:

```
const strategy = {
    subscribeConfiguration: (participant) => {
        return {
            inBandMessaging: {
                enabled: true
            }
        }
    }
    // ... other strategy functions
}

stage.on(StageEvents.STAGE_STREAM_SEI_MESSAGE_RECEIVED, (participant, seiMessage) => {
    console.log(seiMessage.payload, seiMessage.uuid);
});
```

## Layered Encoding

with Simulcast

Layered encoding with simulcast is an IVS real-time streaming feature that allows
publishers to send multiple different quality layers of video, and subscribers to
dynamically or manually change those layers. The feature is described more in the
[Streaming Optimizations](real-time-streaming-optimization.md "real-time-streaming-optimization.md") document.

### Configuring

Layered Encoding (Publisher)

As a publisher, to enable layered encoding with simulcast, add the following
configuration to your `LocalStageStream` on instantiation:

```
// Enable Simulcast
let cameraStream = new LocalStageStream(cameraDevice, {
   simulcast: { enabled: true }
})
```

Depending on the input resolution of your camera device, a set number of
layers will be encoded and sent as defined in the [Default Layers,
Qualities, and Framerates](real-time-streaming-optimization.md#real-time-streaming-optimization-default-layers "real-time-streaming-optimization.md#real-time-streaming-optimization-default-layers") section of _Streaming
Optimizations_.

Also, you can optionally configure individual layers from within the simulcast
configuration:

```
import { SimulcastLayerPresets } from ‘amazon-ivs-web-broadcast’

// Enable Simulcast
let cameraStream = new LocalStageStream(cameraDevice, {
   simulcast: {
      enabled: true,
      layers: [
         SimulcastLayerPresets.DEFAULT_720,
          SimulcastLayerPresets.DEFAULT_360,
          SimulcastLayerPresets.DEFAULT_180,
   }
})
```

Alternately, you can create your own custom layer configurations for up to
three layers. If you provide an empty array or no value, the defaults described
above are used. Layers are described with the following required
properties:

- `height: number;`
- `width: number;`
- `maxBitrateKbps: number;`
- `maxFramerate: number;`

Starting from the presets, you can either override individual properties or
create an entirely new configuration:

```
import { SimulcastLayerPresets } from ‘amazon-ivs-web-broadcast’

const custom720pLayer = {
   ...SimulcastLayerPresets.DEFAULT_720,
   maxFramerate: 15,
}

const custom360pLayer = {
       maxBitrateKbps: 600,
       maxFramerate: 15,
       width: 640,
       height: 360,
}

// Enable Simulcast
let cameraStream = new LocalStageStream(cameraDevice, {
   simulcast: {
      enabled: true,
      layers: [
         custom720pLayer,
         custom360pLayer,
   }
})
```

For maximum values, limits, and errors which can be triggered when configuring
individual layers, see the SDK reference documentation.

### Configuring Layered Encoding (Subscriber)

As a subscriber, there is nothing needed to enable layered encoding. If a
publisher is sending simulcast layers, then by default the server dynamically
adapts between the layers to choose the optimal quality based on the
subscriber's device and network conditions.

Alternatively, to pick explicit layers that the publisher is sending, there
are several options, described below.

### Option

1: Initial Layer Quality Preference

Using the `subscribeConfiguration` strategy, it is possible to
choose what initial layer you want to receive as a subscriber:

```
const strategy = {
    subscribeConfiguration: (participant) => {
        return {
            simulcast: {
                initialLayerPreference: InitialLayerPreference.LOWEST_QUALITY
            }
        }
    }
    // ... other strategy functions
}
```

By default, subscribers always are sent the lowest quality layer first; this
slowly ramps up to the highest quality layer. This optimizes end-user bandwidth
consumption and provides the best time to video, reducing initial video freezes
for users on weaker networks.

These options are available for `InitialLayerPreference`:

- `LOWEST_QUALITY` — The server delivers the lowest quality
  layer of video first. This optimizes bandwidth consumption, as well as
  time to media. Quality is defined as the combination of size, bitrate,
  and framerate of the video. For example, 720p video is lower quality
  than 1080p video.
- `HIGHEST_QUALITY` — The server delivers the highest quality
  layer of video first. This optimizes quality but may increase the time
  to media. Quality is defined as the combination of size, bitrate, and
  framerate of the video. For example, 1080p video is higher quality than
  720p video.

**Note:** For initial layer preferences (the
`initialLayerPreference` call) to take effect, a re-subscribe is
necessary as these updates do not apply to the active subscription.

### Option 2:

Preferred Layer for Stream

Once a stream has started, you can use the `preferredLayerForStream` strategy method. This strategy method exposes the participant and the
stream information.

The strategy method can be returned with the following:

- The layer object directly, based on what
  `RemoteStageStream.getLayers` returns
- The layer object label string, based on
  `StageStreamLayer.label`
- Undefined or null, which indicates that no layer should be selected,
  and dynamic adaption is preferred

For example, the following strategy will always have the users selecting the
lowest quality layer of video available:

```
const strategy = {
    preferredLayerForStream: (participant, stream) => {
        return stream.getLowestQualityLayer();
    }
    // ... other strategy functions
}
```

To reset the layer selection and return to dynamic adaption, return null or
undefined in the strategy. In this example `appState` is a dummy
variable that represents the possible application state.

```
const strategy = {
    preferredLayerForStream: (participant, stream) => {
        if (appState.isAutoMode) {
            return null;
        } else {
            return appState.layerChoice
        }
    }
    // ... other strategy functions
}
```

### Option 3: RemoteStageStream Layer Helpers

`RemoteStageStream` has several helpers which can be used to make
decisions about layer selection and display the corresponding selections to end
users:

- **Layer Events** — Alongside
  `StageEvents`, the `RemoteStageStream` object
  itself has events which communicate layer and simulcast adaption
  changes:
  - `stream.on(RemoteStageStreamEvents.ADAPTION_CHANGED,
(isAdapting) => {})`
  - `stream.on(RemoteStageStreamEvents.LAYERS_CHANGED,
(layers) => {})`
  - `stream.on(RemoteStageStreamEvents.LAYER_SELECTED,
(layer, reason) => {})`

- **Layer Methods** —
  `RemoteStageStream` has several helper methods which can
  be used to get information about the stream and the layers being
  presented. These methods are available on the remote stream provided in
  the `preferredLayerForStream` strategy, as well as remote
  streams exposed via
  `StageEvents.STAGE_PARTICIPANT_STREAMS_ADDED`.
  - `stream.getLayers`
  - `stream.getSelectedLayer`
  - `stream.getLowestQualityLayer`
  - `stream.getHighestQualityLayer`

For details, see the `RemoteStageStream` class in the [SDK
reference documentation](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference"). For the `LAYER_SELECTED` reason,
if `UNAVAILABLE` is returned, this indicates that the requested layer
could not be selected. A best-effort selection is made in its place, which
typically is a lower quality layer to maintain stream stability.

## Handling Network

Issues

When the local device’s network connection is lost, the SDK internally tries to
reconnect without any user action. In some cases, the SDK is not successful and user
action is needed.

Broadly the state of the stage can be handled via the
`STAGE_CONNECTION_STATE_CHANGED` event:

```
stage.on(StageEvents.STAGE_CONNECTION_STATE_CHANGED, (state) => {
   switch (state) {
      case StageConnectionState.DISCONNECTED:
         // handle disconnected UI
         return;
      case StageConnectionState.CONNECTING:
         // handle establishing connection UI
         return;
      case StageConnectionState.CONNECTED:
         // SDK is connected to the Stage
         return;
      case StageConnectionState.ERRORED:
         // SDK encountered an error and lost its connection to the stage. Wait for CONNECTED.
         return;
    }
})
```

In general, you can ignore an errored state that is encountered after successfully
joining a stage, as the SDK will try to recover internally. If the SDK reports an
`ERRORED` state and the stage remains in the `CONNECTING`
state for an extended period of time (e.g., 30 seconds or longer), you probably are
disconnected from the network.

## Broadcast the Stage to an

IVS Channel

To broadcast a stage, create a separate `IVSBroadcastClient` session
and then follow the usual instructions for broadcasting with the SDK, described
above. The list of `StageStream` exposed via
`STAGE_PARTICIPANT_STREAMS_ADDED` can be used to retrieve the
participant media streams which can be applied to the broadcast stream composition,
as follows:

```
// Setup client with preferred settings
const broadcastClient = getIvsBroadcastClient();

stage.on(StageEvents.STAGE_PARTICIPANT_STREAMS_ADDED, (participant, streams) => {
    streams.forEach(stream => {
        const inputStream = new MediaStream([stream.mediaStreamTrack]);
        switch (stream.streamType) {
            case StreamType.VIDEO:
                broadcastClient.addVideoInputDevice(inputStream, `video-${participant.id}`, {
                    index: DESIRED_LAYER,
                    width: MAX_WIDTH,
                    height: MAX_HEIGHT
                });
                break;
            case StreamType.AUDIO:
                broadcastClient.addAudioInputDevice(inputStream, `audio-${participant.id}`);
                break;
        }
    })
})
```

Optionally, you can composite a stage and broadcast it to an IVS low-latency
channel, to reach a larger audience. See [Enabling Multiple
Hosts on an Amazon IVS Stream](../LowLatencyUserGuide/multiple-hosts.md "../LowLatencyUserGuide/multiple-hosts.md") in the IVS Low-Latency Streaming User
Guide.
