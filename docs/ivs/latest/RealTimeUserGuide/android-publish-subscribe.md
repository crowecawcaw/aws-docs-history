# Publishing & Subscribing with the IVS

Android Broadcast SDK | Real-Time Streaming

This document takes you through the steps involved in publishing and subscribing to a
stage using the IVS real-time streaming Android broadcast SDK.

## Concepts

Three core concepts underlie real-time functionality: [stage](#android-publish-subscribe-concepts-stage "#android-publish-subscribe-concepts-stage"), [strategy](#android-publish-subscribe-concepts-strategy "#android-publish-subscribe-concepts-strategy"), and [renderer](#android-publish-subscribe-concepts-renderer "#android-publish-subscribe-concepts-renderer"). The
design goal is minimizing the amount of client-side logic necessary to build a
working product.

### Stage

The `Stage` class is the main point of interaction between the host
application and the SDK. It represents the stage itself and is used to join and
leave the stage. Creating and joining a stage requires a valid, unexpired token
string from the control plane (represented as `token`). Joining and
leaving a stage are simple.

```
Stage stage = new Stage(context, token, strategy);

try {
	stage.join();
} catch (BroadcastException exception) {
	// handle join exception
}

stage.leave();
```

The `Stage` class is also where the `StageRenderer` can
be attached:

```
stage.addRenderer(renderer); // multiple renderers can be added
```

### Strategy

The `Stage.Strategy` interface provides a way for the host
application to communicate the desired state of the stage to the SDK. Three
functions need to be implemented: `shouldSubscribeToParticipant`,
`shouldPublishFromParticipant`, and
`stageStreamsToPublishForParticipant`. All are discussed
below.

#### Subscribing to Participants

```
Stage.SubscribeType shouldSubscribeToParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo);
```

When a remote participant joins the stage, the SDK queries the host
application about the desired subscription state for that participant. The
options are `NONE`, `AUDIO_ONLY`, and
`AUDIO_VIDEO`. When returning a value for this function, the
host application does not need to worry about the publish state, current
subscription state, or stage connection state. If `AUDIO_VIDEO`
is returned, the SDK waits until the remote participant is publishing before
subscribing, and it updates the host application through the renderer
throughout the process.

Here is a sample implementation:

```
@Override
Stage.SubscribeType shouldSubscribeToParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
	return Stage.SubscribeType.AUDIO_VIDEO;
}
```

This is the complete implementation of this function for a host
application that always wants all participants to see each other; e.g., a
video chat application.

More advanced implementations also are possible. Use the
`userInfo` property on `ParticipantInfo` to
selectively subscribe to participants based on server-provided
attributes:

```
@Override
Stage.SubscribeType shouldSubscribeToParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
	switch(participantInfo.userInfo.get(“role”)) {
		case “moderator”:
			return Stage.SubscribeType.NONE;
		case “guest”:
			return Stage.SubscribeType.AUDIO_VIDEO;
		default:
			return Stage.SubscribeType.NONE;
	}
}
```

This can be used to create a stage where moderators can monitor all guests
without being seen or heard themselves. The host application could use
additional business logic to let moderates see each other but remain
invisible to guests.

#### Configuration for Subscribing to Participants

```
SubscribeConfiguration subscribeConfigurationForParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo);
```

If a remote participant is being subscribed to (see [Subscribing to Participants](#android-publish-subscribe-concepts-strategy-participants "#android-publish-subscribe-concepts-strategy-participants")), the SDK queries the host
application about a custom subscribe configuration for that participant.
This configuration is optional and allows the host application to control
certain aspects of subscriber behavior. For information on what can be
configured, see [SubscribeConfiguration](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/SubscribeConfiguration "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/SubscribeConfiguration") in the SDK reference
documentation.

Here is a sample implementation:

```
@Override
public SubscribeConfiguration subscribeConfigrationForParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
    SubscribeConfiguration config = new SubscribeConfiguration();

    config.jitterBuffer.setMinDelay(JitterBufferConfiguration.JitterBufferDelay.MEDIUM());

    return config;
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
boolean shouldPublishFromParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo);
```

Once connected to the stage, the SDK queries the host application to see
if a particular participant should publish. This is invoked only on local
participants that have permission to publish based on the provided
token.

Here is a sample implementation:

```
@Override
boolean shouldPublishFromParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
	return true;
}
```

This is for a standard video chat application where users always want to
publish. They can mute and unmute their audio and video, to instantly be
hidden or seen/heard. (They also can use publish/unpublish, but that is much
slower. Mute/unmute is preferable for use cases where changing visibility
often is desirable.)

#### Choosing Streams to Publish

```
@Override
List<LocalStageStream> stageStreamsToPublishForParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo);
}
```

When publishing, this is used to determine what audio and video streams
should be published. This is covered in more detail later in [Publish a Media
Stream](#android-publish-subscribe-publish-stream "#android-publish-subscribe-publish-stream").

#### Updating the Strategy

The strategy is intended to be dynamic: the values returned from any of
the above functions can be changed at any time. For example, if the host
application does not want to publish until the end user taps a button, you
could return a variable from `shouldPublishFromParticipant`
(something like `hasUserTappedPublishButton`). When that variable
changes based on an interaction by the end user, call
`stage.refreshStrategy()` to signal to the SDK that it should
query the strategy for the latest values, applying only things that have
changed. If the SDK observes that the
`shouldPublishFromParticipant` value has changed, it will
start the publish process. If the SDK queries and all functions return the
same value as before, the `refreshStrategy` call will not perform
any modifications to the stage.

If the return value of `shouldSubscribeToParticipant` changes
from `AUDIO_VIDEO` to `AUDIO_ONLY`, the video stream
will be removed for all participants with changed returned values, if a
video stream existed previously.

Generally, the stage uses the strategy to most efficiently apply the
difference between the previous and current strategies, without the host
application needing to worry about all the state required to manage it
properly. Because of this, think of calling
`stage.refreshStrategy()` as a cheap operation, because it
does nothing unless the strategy changes.

### Renderer

The `StageRenderer` interface communicates the state of the stage
to the host application. Updates to the host application’s UI usually can be
powered entirely by the events provided by the renderer. The renderer provides
the following functions:

```
void onParticipantJoined(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo);

void onParticipantLeft(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo);

void onParticipantPublishStateChanged(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull Stage.PublishState publishState);

void onParticipantSubscribeStateChanged(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull Stage.SubscribeState subscribeState);

void onStreamsAdded(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull List<StageStream> streams);

void onStreamsRemoved(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull List<StageStream> streams);

void onStreamsMutedChanged(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull List<StageStream> streams);

void onError(@NonNull BroadcastException exception);

void onConnectionStateChanged(@NonNull Stage stage, @NonNull Stage.ConnectionState state, @Nullable BroadcastException exception);

void onStreamAdaptionChanged(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull RemoteStageStream stream, boolean adaption);

void onStreamLayersChanged(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull RemoteStageStream stream, @NonNull List<RemoteStageStream.Layer> layers);

void onStreamLayerSelected(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull RemoteStageStream stream, @Nullable RemoteStageStream.Layer layer, @NonNull RemoteStageStream.LayerSelectedReason reason);
```

For most of these methods, the corresponding `Stage` and
`ParticipantInfo` are provided.

It is not expected that the information provided by the renderer impacts the
return values of the strategy. For example, the return value of
`shouldSubscribeToParticipant` is not expected to change when
`onParticipantPublishStateChanged` is called. If the host
application wants to subscribe to a particular participant, it should return the
desired subscription type regardless of that participant’s publish state. The
SDK is responsible for ensuring that the desired state of the strategy is acted
on at the correct time based on the state of the stage.

The `StageRenderer` can be attached to the stage class:

```
stage.addRenderer(renderer); // multiple renderers can be added
```

Note that only publishing participants trigger
`onParticipantJoined`, and whenever a participant stops
publishing or leaves the stage session, `onParticipantLeft` is
triggered.

## Publish a Media

Stream

Local devices such as built-in microphones and cameras are discovered via
`DeviceDiscovery`. Here is an example of selecting the front-facing
camera and default microphone, then return them as `LocalStageStreams` to
be published by the SDK:

```
DeviceDiscovery deviceDiscovery = new DeviceDiscovery(context);

List<Device> devices = deviceDiscovery.listLocalDevices();
List<LocalStageStream> publishStreams = new ArrayList<LocalStageStream>();

Device frontCamera = null;
Device microphone = null;

// Create streams using the front camera, first microphone
for (Device device : devices) {
	Device.Descriptor descriptor = device.getDescriptor();
	if (!frontCamera && descriptor.type == Device.Descriptor.DeviceType.Camera && descriptor.position = Device.Descriptor.Position.FRONT) {
		front Camera = device;
	}
	if (!microphone && descriptor.type == Device.Descriptor.DeviceType.Microphone) {
		microphone = device;
	}
}

ImageLocalStageStream cameraStream = new ImageLocalStageStream(frontCamera);
AudioLocalStageStream microphoneStream = new AudioLocalStageStream(microphoneDevice);

publishStreams.add(cameraStream);
publishStreams.add(microphoneStream);

// Provide the streams in Stage.Strategy
@Override
@NonNull List<LocalStageStream> stageStreamsToPublishForParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
	return publishStreams;
}
```

## Display and Remove

Participants

After subscribing is completed, you will receive an array of
`StageStream` objects through the renderer’s
`onStreamsAdded` function. You can retrieve the preview from an
`ImageStageStream`:

```
ImagePreviewView preview = ((ImageStageStream)stream).getPreview();

// Add the view to your view hierarchy
LinearLayout previewHolder = findViewById(R.id.previewHolder);
preview.setLayoutParams(new LinearLayout.LayoutParams(
		LinearLayout.LayoutParams.MATCH_PARENT,
		LinearLayout.LayoutParams.MATCH_PARENT));
previewHolder.addView(preview);
```

You can retrieve the audio-level stats from an
`AudioStageStream`:

```
((AudioStageStream)stream).setStatsCallback((peak, rms) -> {
	// handle statistics
});
```

When a participant stops publishing or is unsubscribed from, the
`onStreamsRemoved` function is called with the streams that were
removed. Host applications should use this as a signal to remove the participant’s
video stream from the view hierarchy.

`onStreamsRemoved` is invoked for all scenarios in which a stream might
be removed, including:

- The remote participant stops publishing.
- A local device unsubscribes or changes subscription from
  `AUDIO_VIDEO` to `AUDIO_ONLY`.
- The remote participant leaves the stage.
- The local participant leaves the stage.

Because `onStreamsRemoved` is invoked for all scenarios, no custom
business logic is required around removing participants from the UI during remote or
local leave operations.

## Mute and Unmute Media

Streams

`LocalStageStream` objects have a `setMuted` function that
controls whether the stream is muted. This function can be called on the stream
before or after it is returned from the `streamsToPublishForParticipant`
strategy function.

**Important**: If a new `LocalStageStream`
object instance is returned by `streamsToPublishForParticipant` after a
call to `refreshStrategy`, the mute state of the new stream object is
applied to the stage. Be careful when creating new `LocalStageStream`
instances to make sure the expected mute state is maintained.

## Monitor Remote Participant

Media Mute State

When a participant changes the mute state of their video or audio stream, the
renderer `onStreamMutedChanged` function is invoked with a list of
streams that have changed. Use the `getMuted` method on
`StageStream` to update your UI accordingly.

```
@Override
void onStreamsMutedChanged(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull List<StageStream> streams) {
	for (StageStream stream : streams) {
		boolean muted = stream.getMuted();
		// handle UI changes
	}
}
```

## Get WebRTC

Statistics

To get the latest WebRTC statistics for a publishing stream or a subscribing
stream, use `requestRTCStats` on `StageStream`. When a
collection is completed, you will receive statistics through the
`StageStream.Listener` which can be set on
`StageStream`.

```
stream.requestRTCStats();

@Override
void onRTCStats(Map<String, Map<String, String>> statsMap) {
	for (Map.Entry<String, Map<String, string>> stat : statsMap.entrySet()) {
		for(Map.Entry<String, String> member : stat.getValue().entrySet()) {
			Log.i(TAG, stat.getKey() + “ has member “ + member.getKey() + “ with value “ + member.getValue());
		}
	}
}
```

## Get Participant

Attributes

If you specify attributes in the `CreateParticipantToken` operation
request, you can see the attributes in `ParticipantInfo`
properties:

```
@Override
void onParticipantJoined(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
	for (Map.Entry<String, String> entry : participantInfo.userInfo.entrySet()) {
		Log.i(TAG, “attribute: “ + entry.getKey() + “ = “ + entry.getValue());
	}
}
```

## Embed Messages

The `embedMessage` method on ImageDevice allows you to insert metadata
payloads directly into video frames during publishing. This enables
frame-synchronized messaging for real-time applications. Message embedding is
available only when using the SDK for real-time publishing (not low-latency
publishing).

Embedded messages are not guaranteed to arrive to subscribers because they are
embedded directly within video frames and transmitted over UDP, which does not
guarantee packet delivery. Packet loss during transmission can result in lost
messages, especially in poor network conditions. To mitigate this, the
`embedMessage` method includes a `repeatCount` parameter
that duplicates the message across multiple consecutive frames, increasing delivery
reliability. This capability is available only for video streams.

### Using embedMessage

Publishing clients can embed message payloads into their video stream using
the `embedMessage` method on ImageDevice. The payload size must be
greater than 0KB and less than 1KB. The number of embedded messages inserted per
second must not exceed 10KB per second.

```
val surfaceSource: SurfaceSource = imageStream.device as SurfaceSource
val message = "hello world"
val messageBytes = message.toByteArray(StandardCharsets.UTF_8)

try {
    surfaceSource.embedMessage(messageBytes, 0)
} catch (e: BroadcastException) {
    Log.e("EmbedMessage", "Failed to embed message: ${e.message}")
}
```

### Repeating Message Payloads

Use `repeatCount` to duplicate the message across multiple frames
for improved reliability. This value must be between 0 and 30. Receiving clients
must have logic to de-duplicate the message.

```
try {
    surfaceSource.embedMessage(messageBytes, 5)
    // repeatCount: 0-30, receiving clients should handle duplicates
} catch (e: BroadcastException) {
    Log.e("EmbedMessage", "Failed to embed message: ${e.message}")
}
```

### Reading Embedded Messages

See "Get Supplemental Enhancement Information (SEI)" below for how to read
embedded messages from incoming streams.

## Get Supplemental

Enhancement Information (SEI)

The Supplemental Enhancement Information (SEI) NAL unit is used to store
frame-aligned metadata alongside the video. Subscribing clients can read SEI
payloads from a publisher who is publishing H.264 video by inspecting the
`embeddedMessages` property on the `ImageDeviceFrame`
objects coming out of the publisher’s `ImageDevice`. To do this, acquire
a publisher’s `ImageDevice`, then observe each frame via a callback
provided to `setOnFrameCallback`, as shown in the following
example:

```
// in a StageRenderer’s onStreamsAdded function, after acquiring the new ImageStream

val imageDevice = imageStream.device as ImageDevice
imageDevice.setOnFrameCallback(object : ImageDevice.FrameCallback {
	override fun onFrame(frame: ImageDeviceFrame) {
    		for (message in frame.embeddedMessages) {
        		if (message is UserDataUnregisteredSeiMessage) {
            		val seiMessageBytes = message.data
            		val seiMessageUUID = message.uuid

            		// interpret the message's data based on the UUID
        		}
    		}
	}
})
```

## Continue Session in

the Background

When the app enters the background, you may want to stop publishing or subscribe
only to other remote participants’ audio. To accomplish this, update your
`Strategy` implementation to stop publishing, and subscribe to
`AUDIO_ONLY` (or `NONE`, if applicable).

```
// Local variables before going into the background
boolean shouldPublish = true;
Stage.SubscribeType subscribeType = Stage.SubscribeType.AUDIO_VIDEO;

// Stage.Strategy implementation
@Override
boolean shouldPublishFromParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
	return shouldPublish;
}

@Override
Stage.SubscribeType shouldSubscribeToParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
	return subscribeType;
}

// In our Activity, modify desired publish/subscribe when we go to background, then call refreshStrategy to update the stage
@Override
void onStop() {
	super.onStop();
	shouldPublish = false;
	subscribeTpye = Stage.SubscribeType.AUDIO_ONLY;
	stage.refreshStrategy();
}
```

## Layered

Encoding with Simulcast

Layered encoding with simulcast is an IVS real-time streaming feature that allows
publishers to send multiple different quality layers of video, and subscribers to
dynamically or manually configure those layers. The feature is described more in the
[Streaming Optimizations](real-time-streaming-optimization.md "real-time-streaming-optimization.md")
document.

### Configuring Layered Encoding (Publisher)

As a publisher, to enable layered encoding with simulcast, add the following
configuration to your `LocalStageStream` on instantiation:

```
// Enable Simulcast
StageVideoConfiguration config = new StageVideoConfiguration();
config.simulcast.setEnabled(true);

ImageLocalStageStream cameraStream = new ImageLocalStageStream(frontCamera, config);

// Other Stage implementation code
```

Depending on the resolution you set on video configuration, a set number of
layers will be encoded and sent as defined in the [Default Layers,
Qualities, and Framerates](real-time-streaming-optimization.md#real-time-streaming-optimization-default-layers "real-time-streaming-optimization.md#real-time-streaming-optimization-default-layers") section of _Streaming
Optimizations_.

Also, you can optionally configure individual layers from within the simulcast
configuration:

```
// Enable Simulcast
StageVideoConfiguration config = new StageVideoConfiguration();
config.simulcast.setEnabled(true);

List<StageVideoConfiguration.Simulcast.Layer> simulcastLayers = new ArrayList<>();
simulcastLayers.add(StagePresets.SimulcastLocalLayer.DEFAULT_720);
simulcastLayers.add(StagePresets.SimulcastLocalLayer.DEFAULT_180);

config.simulcast.setLayers(simulcastLayers);

ImageLocalStageStream cameraStream = new ImageLocalStageStream(frontCamera, config);

// Other Stage implementation code
```

Alternately, you can create your own custom layer configurations for up to
three layers. If you provide an empty array or no value, the defaults described
above are used. Layers are described with the following required property
setters:

- `setSize: Vec2;`
- `setMaxBitrate: integer;`
- `setMinBitrate: integer;`
- `setTargetFramerate: integer;`

Starting from the presets, you can either override individual properties or
create an entirely new configuration:

```
// Enable Simulcast
StageVideoConfiguration config = new StageVideoConfiguration();
config.simulcast.setEnabled(true);

List<StageVideoConfiguration.Simulcast.Layer> simulcastLayers = new ArrayList<>();

// Configure high quality layer with custom framerate
StageVideoConfiguration.Simulcast.Layer customHiLayer = StagePresets.SimulcastLocalLayer.DEFAULT_720;
customHiLayer.setTargetFramerate(15);

// Add layers to the list
simulcastLayers.add(customHiLayer);
simulcastLayers.add(StagePresets.SimulcastLocalLayer.DEFAULT_180);

config.simulcast.setLayers(simulcastLayers);

ImageLocalStageStream cameraStream = new ImageLocalStageStream(frontCamera, config);

// Other Stage implementation code
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

### Option 1: Initial Layer Quality Preference

Using the `subscribeConfigurationForParticipant` strategy, it is
possible to choose what initial layer you want to receive as a
subscriber:

```
@Override
public SubscribeConfiguration subscribeConfigrationForParticipant(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo) {
    SubscribeConfiguration config = new SubscribeConfiguration();

    config.simulcast.setInitialLayerPreference(SubscribeSimulcastConfiguration.InitialLayerPreference.LOWEST_QUALITY);

    return config;
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

**Note:** For initial layer preferences (the `setInitialLayerPreference` call) to take
effect, a re-subscribe is necessary as these updates do not apply to the active
subscription.

### Option 2:

Preferred Layer for Stream

The `preferredLayerForStream` strategy method lets you select a
layer after the stream has started. This strategy method receives the
participant and the stream information, so you can select a layer on a
participant-by-participant basis. The SDK calls this method in response to
specific events, such as when stream layers change, the participant state
changes, or the host application refreshes the strategy.

The strategy method returns a `RemoteStageStream.Layer` object,
which can be one of the following:

- A layer object, such as one returned by
  `RemoteStageStream.getLayers`.
- null, which indicates that no layer should be selected and dynamic
  adaption is preferred.

For example, the following strategy will always have the users selecting the
lowest quality layer of video available:

```
@Nullable
@Override
public RemoteStageStream.Layer preferredLayerForStream(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull RemoteStageStream stream) {
    return stream.getLowestQualityLayer();
}
```

To reset the layer selection and return to dynamic adaption, return null or
undefined in the strategy. In this example, `appState` is a
placeholder variable that represents the host application’s state.

```
@Nullable
@Override
public RemoteStageStream.Layer preferredLayerForStream(@NonNull Stage stage, @NonNull ParticipantInfo participantInfo, @NonNull RemoteStageStream stream) {
    if (appState.isAutoMode) {
        return null;
    } else {
        return appState.layerChoice;
    }
}
```

### Option 3: RemoteStageStream Layer Helpers

`RemoteStageStream` has several helpers which can be used to make
decisions about layer selection and display the corresponding selections to end
users:

- **Layer Events** — Alongside
  `StageRenderer`, the
  `RemoteStageStream.Listener` has events which communicate
  layer and simulcast adaption changes:
  - `void onAdaptionChanged(boolean adaption)`
  - `void onLayersChanged(@NonNull List<Layer>
layers)`
  - `void onLayerSelected(@Nullable Layer layer, @NonNull
LayerSelectedReason reason)`

- **Layer Methods** —
  `RemoteStageStream` has several helper methods which can
  be used to get information about the stream and the layers being
  presented. These methods are available on the remote stream provided in
  the `preferredLayerForStream` strategy, as well as remote
  streams exposed via `StageRenderer.onStreamsAdded`.
  - `stream.getLayers`
  - `stream.getSelectedLayer`
  - `stream.getLowestQualityLayer`
  - `stream.getHighestQualityLayer`
  - `stream.getLayersWithConstraints`

For details, see the `RemoteStageStream` class in the [SDK
reference documentation](https://aws.github.io/amazon-ivs-broadcast-docs/latest/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/latest/android/"). For the `LayerSelected` reason,
if `UNAVAILABLE` is returned, this indicates that the requested layer
could not be selected. A best-effort selection is made in its place, which
typically is a lower quality layer to maintain stream stability.

## Video-Configuration

Limitations

The SDK does not support forcing portrait mode or landscape mode using
`StageVideoConfiguration.setSize(BroadcastConfiguration.Vec2 size)`.
In portrait orientation, the smaller dimension is used as the width; in landscape
orientation, the height. This means that the following two calls to
`setSize` have the same effect on the video configuration:

```
StageVideo Configuration config = new StageVideo Configuration();

config.setSize(BroadcastConfiguration.Vec2(720f, 1280f);
config.setSize(BroadcastConfiguration.Vec2(1280f, 720f);
```

## Handling Network

Issues

When the local device’s network connection is lost, the SDK internally tries to
reconnect without any user action. In some cases, the SDK is not successful and user
action is needed. There are two main errors related to losing the network
connection:

- Error code 1400, message: "PeerConnection is lost due to unknown network
  error"
- Error code 1300, message: "Retry attempts are exhausted"

If the first error is received but the second is not, the SDK is still connected
to the stage and will try to reestablish its connections automatically. As a
safeguard, you can call `refreshStrategy` without any changes to the
strategy method’s return values, to trigger a manual reconnect attempt.

If the second error is received, the SDK’s reconnect attempts have failed and the
local device is no longer connected to the stage. In this case, try to rejoin the
stage by calling `join` after your network connection has been
reestablished.

In general, encountering errors after joining a stage successfully indicates that
the SDK was unsuccessful in reestablishing a connection. Create a new
`Stage` object and try to join when network conditions
improve.

## Using Bluetooth

Microphones

To publish using Bluetooth microphone devices, you must start a Bluetooth SCO
connection:

```
Bluetooth.startBluetoothSco(context);
// Now bluetooth microphones can be used
…
// Must also stop bluetooth SCO
Bluetooth.stopBluetoothSco(context);
```
