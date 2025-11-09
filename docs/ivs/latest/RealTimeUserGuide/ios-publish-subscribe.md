# Publishing & Subscribing with the IVS iOS

Broadcast SDK | Real-Time Streaming

This document takes you through the steps involved in publishing and subscribing to a
stage using the IVS real-time streaming iOS broadcast SDK.

## Concepts

Three core concepts underlie real-time functionality: [stage](#ios-publish-subscribe-concepts-stage "#ios-publish-subscribe-concepts-stage"), [strategy](#ios-publish-subscribe-concepts-strategy "#ios-publish-subscribe-concepts-strategy"), and [renderer](#ios-publish-subscribe-concepts-renderer "#ios-publish-subscribe-concepts-renderer"). The design
goal is minimizing the amount of client-side logic necessary to build a working
product.

### Stage

The `IVSStage` class is the main point of interaction between the
host application and the SDK. The class represents the stage itself and is used
to join and leave the stage. Creating or joining a stage requires a valid,
unexpired token string from the control plane (represented as
`token`). Joining and leaving a stage are simple.

```
let stage = try IVSStage(token: token, strategy: self)

try stage.join()

stage.leave()
```

The `IVSStage` class also is where the
`IVSStageRenderer` and `IVSErrorDelegate` can be
attached:

```
let stage = try IVSStage(token: token, strategy: self)
stage.errorDelegate = self
stage.addRenderer(self) // multiple renderers can be added
```

### Strategy

The `IVSStageStrategy` protocol provides a way for the host
application to communicate the desired state of the stage to the SDK. Three
functions need to be implemented: `shouldSubscribeToParticipant`,
`shouldPublishParticipant`, and
`streamsToPublishForParticipant`. All are discussed below.

#### Subscribing to Participants

```
func stage(_ stage: IVSStage, shouldSubscribeToParticipant participant: IVSParticipantInfo) -> IVSStageSubscribeType
```

When a remote participant joins a stage, the SDK queries the host
application about the desired subscription state for that participant. The
options are `.none`, `.audioOnly`, and
`.audioVideo`. When returning a value for this function, the
host application does not need to worry about the publish state, current
subscription state, or stage connection state. If `.audioVideo`
is returned, the SDK waits until the remote participant is publishing before
subscribing, and it updates the host application through the renderer
throughout the process.

Here is a sample implementation:

```
func stage(_ stage: IVSStage, shouldSubscribeToParticipant participant: IVSParticipantInfo) -> IVSStageSubscribeType {
    return .audioVideo
}
```

This is the complete implementation of this function for a host
application that always wants all participants to see each other; e.g., a
video-chat application.

More advanced implementations also are possible. Use the
`attributes` property on `IVSParticipantInfo` to
selectively subscribe to participants based on server-provided
attributes:

```
func stage(_ stage: IVSStage, shouldSubscribeToParticipant participant: IVSParticipantInfo) -> IVSStageSubscribeType {
    switch participant.attributes["role"] {
    case "moderator": return .none
    case "guest": return .audioVideo
    default: return .none
    }
}
```

This can be used to create a stage where moderators can monitor all guests
without being seen or heard themselves. The host application could use
additional business logic to let moderators see each other but remain
invisible to guests.

#### Configuration for Subscribing to Participants

```
func stage(_ stage: IVSStage, subscribeConfigurationForParticipant participant: IVSParticipantInfo) -> IVSSubscribeConfiguration
```

If a remote participant is being subscribed to (see [Subscribing to Participants](#ios-publish-subscribe-concepts-strategy-participants "#ios-publish-subscribe-concepts-strategy-participants")), the SDK queries the host
application about a custom subscribe configuration for that participant.
This configuration is optional and allows the host application to control
certain aspects of subscriber behavior. For information on what can be
configured, see [SubscribeConfiguration](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/SubscribeConfiguration "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference/interfaces/SubscribeConfiguration") in the SDK reference
documentation.

Here is a sample implementation:

```
func stage(_ stage: IVSStage, subscribeConfigurationForParticipant participant: IVSParticipantInfo) -> IVSSubscribeConfiguration {
    let config = IVSSubscribeConfiguration()

    try! config.jitterBuffer.setMinDelay(.medium())

    return config
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
func stage(_ stage: IVSStage, shouldPublishParticipant participant: IVSParticipantInfo) -> Bool
```

Once connected to the stage, the SDK queries the host application to see
if a particular participant should publish. This is invoked only on local
participants that have permission to publish based on the provided
token.

Here is a sample implementation:

```
func stage(_ stage: IVSStage, shouldPublishParticipant participant: IVSParticipantInfo) -> Bool {
    return true
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
func stage(_ stage: IVSStage, streamsToPublishForParticipant participant: IVSParticipantInfo) -> [IVSLocalStageStream]
```

When publishing, this is used to determine what audio and video streams
should be published. This is covered in more detail later in [Publish a Media
Stream](#ios-publish-subscribe-publish-stream "#ios-publish-subscribe-publish-stream").

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
value has changed, it will start the publish process. If the SDK queries and
all functions return the same value as before, the
`refreshStrategy` call will not make any modifications to the
stage.

If the return value of `shouldSubscribeToParticipant` changes
from `.audioVideo` to `.audioOnly`, the video stream
will be removed for all participants with changed returned values, if a
video stream existed previously.

Generally, the stage uses the strategy to most efficiently apply the
difference between the previous and current strategies, without the host
application needing to worry about all the state required to manage it
properly. Because of this, think of calling
`stage.refreshStrategy()` as a cheap operation, because it
does nothing unless the strategy changes.

### Renderer

The `IVSStageRenderer` protocol communicates the state of the stage
to the host application. Updates to the host application’s UI usually can be
powered entirely by the events provided by the renderer. The renderer provides
the following functions:

```
func stage(_ stage: IVSStage, participantDidJoin participant: IVSParticipantInfo)

func stage(_ stage: IVSStage, participantDidLeave participant: IVSParticipantInfo)

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, didChange publishState: IVSParticipantPublishState)

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, didChange subscribeState: IVSParticipantSubscribeState)

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, didAdd streams: [IVSStageStream])

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, didRemove streams: [IVSStageStream])

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, didChangeMutedStreams streams: [IVSStageStream])

func stage(_ stage: IVSStage, didChange connectionState: IVSStageConnectionState, withError error: Error?)

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, stream: IVSRemoteStageStream, didChangeStreamAdaption adaption: Bool)

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, stream: IVSRemoteStageStream, didChange layers: [IVSRemoteStageStreamLayer])

func stage(_ stage: IVSStage, participant: IVSParticipantInfo, stream: IVSRemoteStageStream, didSelect layer: IVSRemoteStageStreamLayer?, reason: IVSRemoteStageStream.LayerSelectedReason)

```

It is not expected that the information provided by the renderer impacts the
return values of the strategy. For example, the return value of
`shouldSubscribeToParticipant` is not expected to change when
`participant:didChangePublishState` is called. If the host
application wants to subscribe to a particular participant, it should return the
desired subscription type regardless of that participant’s publish state. The
SDK is responsible for ensuring that the desired state of the strategy is acted
on at the correct time based on the state of the stage.

Note that only publishing participants trigger
`participantDidJoin`, and whenever a participant stops publishing or
leaves the stage session, `participantDidLeave` is triggered.

## Publish a Media

Stream

Local devices such as built-in microphones and cameras are discovered via
`IVSDeviceDiscovery`. Here is an example of selecting the
front-facing camera and default microphone, then returning them as
`IVSLocalStageStreams` to be published by the SDK:

```
let devices = IVSDeviceDiscovery().listLocalDevices()

// Find the camera virtual device, choose the front source, and create a stream
let camera = devices.compactMap({ $0 as? IVSCamera }).first!
let frontSource = camera.listAvailableInputSources().first(where: { $0.position == .front })!
camera.setPreferredInputSource(frontSource)
let cameraStream = IVSLocalStageStream(device: camera)

// Find the microphone virtual device and create a stream
let microphone = devices.compactMap({ $0 as? IVSMicrophone }).first!
let microphoneStream = IVSLocalStageStream(device: microphone)

// Configure the audio manager to use the videoChat preset, which is optimized for bi-directional communication, including echo cancellation.
IVSStageAudioManager.sharedInstance().setPreset(.videoChat)

// This is a function on IVSStageStrategy
func stage(_ stage: IVSStage, streamsToPublishForParticipant participant: IVSParticipantInfo) -> [IVSLocalStageStream] {
    return [cameraStream, microphoneStream]
}
```

## Display and Remove

Participants

After subscribing is completed, you will receive an array of
`IVSStageStream` objects through the renderer’s
`didAddStreams` function. To preview or receive audio level stats
about this participant, you can access the underlying `IVSDevice` object
from the stream:

```
if let imageDevice = stream.device as? IVSImageDevice {
    let preview = imageDevice.previewView()
    /* attach this UIView subclass to your view */
} else if let audioDevice = stream.device as? IVSAudioDevice {
    audioDevice.setStatsCallback( { stats in
        /* process stats.peak and stats.rms */
    })
}
```

When a participant stops publishing or is unsubscribed from, the
`didRemoveStreams` function is called with the streams that were
removed. Host applications should use this as a signal to remove the participant’s
video stream from the view hierarchy.

`didRemoveStreams` is invoked for all scenarios in which a stream might
be removed, including:

- The remote participant stops publishing.
- A local device unsubscribes or changes subscription from
  `.audioVideo` to `.audioOnly`.
- The remote participant leaves the stage.
- The local participant leaves the stage.

Because `didRemoveStreams` is invoked for all scenarios, no custom
business logic is required around removing participants from the UI during remote or
local leave operations.

## Mute and Unmute Media

Streams

`IVSLocalStageStream` objects have a `setMuted` function
that controls whether the stream is muted. This function can be called on the stream
before or after it is returned from the `streamsToPublishForParticipant`
strategy function.

**Important**: If a new
`IVSLocalStageStream` object instance is returned by
`streamsToPublishForParticipant` after a call to
`refreshStrategy`, the mute state of the new stream object is applied
to the stage. Be careful when creating new `IVSLocalStageStream`
instances to make sure the expected mute state is maintained.

## Monitor Remote Participant Media

Mute State

When a participant changes the mute state of its video or audio stream, the
renderer `didChangeMutedStreams` function is invoked with an array of
streams that have changed. Use the `isMuted` property on
`IVSStageStream` to update your UI accordingly:

```
func stage(_ stage: IVSStage, participant: IVSParticipantInfo, didChangeMutedStreams streams: [IVSStageStream]) {
    streams.forEach { stream in
        /* stream.isMuted */
    }
}
```

## Create a Stage

Configuration

To customize the values of a stage’s video configuration, use
`IVSLocalStageStreamVideoConfiguration`:

```
let config = IVSLocalStageStreamVideoConfiguration()
try config.setMaxBitrate(900_000)
try config.setMinBitrate(100_000)
try config.setTargetFramerate(30)
try config.setSize(CGSize(width: 360, height: 640))
config.degradationPreference = .balanced
```

## Get WebRTC Statistics

To get the latest WebRTC statistics for a publishing stream or a subscribing
stream, use `requestRTCStats` on `IVSStageStream`. When a
collection is completed, you will receive statistics through the
`IVSStageStreamDelegate` which can be set on
`IVSStageStream`. To continually collect WebRTC statistics, call this
function on a `Timer`.

```
func stream(_ stream: IVSStageStream, didGenerateRTCStats stats: [String : [String : String]]) {
    for stat in stats {
      for member in stat.value {
         print("stat \(stat.key) has member \(member.key) with value \(member.value)")
      }
   }
}
```

## Get Participant

Attributes

If you specify attributes in the `CreateParticipantToken` operation
request, you can see the attributes in `IVSParticipantInfo`
properties:

```
func stage(_ stage: IVSStage, participantDidJoin participant: IVSParticipantInfo) {
    print("ID: \(participant.participantId)")
    for attribute in participant.attributes {
        print("attribute: \(attribute.key)=\(attribute.value)")
    }
}
```

## Embed Messages

The `embedMessage` method on IVSImageDevice allows you to insert
metadata payloads directly into video frames during publishing. This enables
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
the `embedMessage` method on IVSImageDevice. The payload size must be
greater than 0KB and less than 1KB. The number of embedded messages inserted per
second must not exceed 10KB per second.

```
let imageDevice: IVSImageDevice = imageStream.device as! IVSImageDevice
let messageData = Data("hello world".utf8)

do {
    try imageDevice.embedMessage(messageData, withRepeatCount: 0)
} catch {
    print("Failed to embed message: \(error)")
}
```

### Repeating Message Payloads

Use `repeatCount` to duplicate the message across multiple frames
for improved reliability. This value must be between 0 and 30. Receiving clients
must have logic to de-duplicate the message.

```
try imageDevice.embedMessage(messageData, withRepeatCount: 5)

// repeatCount: 0-30, receiving clients should handle duplicates
```

### Reading Embedded Messages

See "Get Supplemental Enhancement Information (SEI)" below for how to read
embedded messages from incoming streams.

## Get Supplemental Enhancement

Information (SEI)

The Supplemental Enhancement Information (SEI) NAL unit is used to store
frame-aligned metadata alongside the video. Subscribing clients can read SEI
payloads from a publisher who is publishing H.264 video by inspecting the
`embeddedMessages` property on the `IVSImageDeviceFrame`
objects coming out of the publisher’s `IVSImageDevice`. To do this,
acquire a publisher’s `IVSImageDevice`, then observe each frame via a
callback provided to `setOnFrameCallback`, as shown in the following
example:

```
// in an IVSStageRenderer’s stage:participant:didAddStreams: function, after acquiring the new IVSImageStream

let imageDevice: IVSImageDevice? = imageStream.device as? IVSImageDevice
imageDevice?.setOnFrameCallback { frame in
	for message in frame.embeddedMessages {
    		if let seiMessage = message as? IVSUserDataUnregisteredSEIMessage {
        		let seiMessageData = seiMessage.data
        		let seiMessageUUID = seiMessage.UUID

        		// interpret the message's data based on the UUID
    		}
	}
}
```

## Continue Session in the

Background

When the app enters the background, you can continue to be in the stage while
hearing remote audio, though it is not possible to continue to send your own image
and audio. You will need to update your `IVSStrategy` implementation to
stop publishing and subscribe to `.audioOnly` (or `.none`, if
applicable):

```
func stage(_ stage: IVSStage, shouldPublishParticipant participant: IVSParticipantInfo) -> Bool {
    return false
}
func stage(_ stage: IVSStage, shouldSubscribeToParticipant participant: IVSParticipantInfo) -> IVSStageSubscribeType {
    return .audioOnly
}
```

Then make a call to `stage.refreshStrategy()`.

## Layered Encoding

with Simulcast

Layered encoding with simulcast is an IVS real-time streaming feature that allows
publishers to send multiple different quality layers of video, and subscribers to
dynamically or manually configure those layers. The feature is described more in the
[Streaming Optimizations](real-time-streaming-optimization.md "real-time-streaming-optimization.md")
document.

### Configuring

Layered Encoding (Publisher)

As a publisher, to enable layered encoding with simulcast, add the following
configuration to your `IVSLocalStageStream` on instantiation:

```
// Enable Simulcast
let config = IVSLocalStageStreamVideoConfiguration()
config.simulcast.enabled = true

let cameraStream = IVSLocalStageStream(device: camera, configuration: config)

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
let config = IVSLocalStageStreamVideoConfiguration()
config.simulcast.enabled = true

let layers = [
    IVSStagePresets.simulcastLocalLayer().default720(),
    IVSStagePresets.simulcastLocalLayer().default180()
]

try config.simulcast.setLayers(layers)

let cameraStream = IVSLocalStageStream(device: camera, configuration: config)

// Other Stage implementation code
```

Alternately, you can create your own custom layer configurations for up to
three layers. If you provide an empty array or no value, the defaults described
above are used. Layers are described with the following required property
setters:

- `setSize: CGSize;`
- `setMaxBitrate: integer;`
- `setMinBitrate: integer;`
- `setTargetFramerate: float;`

Starting from the presets, you can either override individual properties or
create an entirely new configuration:

```
// Enable Simulcast
let config = IVSLocalStageStreamVideoConfiguration()
config.simulcast.enabled = true

let customHiLayer = IVSStagePresets.simulcastLocalLayer().default720()
try customHiLayer.setTargetFramerate(15)

let layers = [
    customHiLayer,
    IVSStagePresets.simulcastLocalLayer().default180()
]

try config.simulcast.setLayers(layers)

let cameraStream = IVSLocalStageStream(device: camera, configuration: config)

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

### Option

1: Initial Layer Quality Preference

Using the `subscribeConfigurationForParticipant` strategy, it is
possible to choose what initial layer you want to receive as a
subscriber:

```
func stage(_ stage: IVSStage, subscribeConfigurationForParticipant participant: IVSParticipantInfo) -> IVSSubscribeConfiguration {
    let config = IVSSubscribeConfiguration()

    config.simulcast.initialLayerPreference = .lowestQuality

    return config
}
```

By default, subscribers always are sent the lowest quality layer first; this
slowly ramps up to the highest quality layer. This optimizes end-user bandwidth
consumption and provides the best time to video, reducing initial video freezes
for users on weaker networks.

These options are available for `InitialLayerPreference`:

- `lowestQuality` — The server delivers the lowest quality
  layer of video first. This optimizes bandwidth consumption, as well as
  time to media. Quality is defined as the combination of size, bitrate,
  and framerate of the video. For example, 720p video is lower quality
  than 1080p video.
- `highestQuality` — The server delivers the highest quality
  layer of video first. This optimizes quality but may increase the time
  to media. Quality is defined as the combination of size, bitrate, and
  framerate of the video. For example, 1080p video is higher quality than
  720p video.

**Note:** For initial layer preferences (the
`initialLayerPreference` call) to take effect, a re-subscribe is
necessary as these updates do not apply to the active subscription.

### Option 2:

Preferred Layer for Stream

The `preferredLayerForStream` strategy method lets you select a
layer after the stream has started. This strategy method receives the
participant and the stream information, so you can select a layer on a
participant-by-participant basis. The SDK calls this method in response to
specific events, such as when stream layers change, the participant state
changes, or the host application refreshes the strategy.

The strategy method returns an `IVSRemoteStageStreamLayer` object,
which can be one of the following:

- A layer object, such as one returned by
  `IVSRemoteStageStream.layers`.
- null, which indicates that no layer should be selected and dynamic
  adaption is preferred.

For example, the following strategy will always have the users selecting the
lowest quality layer of video available:

```
func stage(_ stage: IVSStage, participant: IVSParticipantInfo, preferredLayerFor stream: IVSRemoteStageStream) -> IVSRemoteStageStreamLayer? {
    return stream.lowestQualityLayer
}
```

To reset the layer selection and return to dynamic adaption, return null or
undefined in the strategy. In this example, `appState` is a
placeholder variable that represents the host application’s state.

```
func stage(_ stage: IVSStage, participant: IVSParticipantInfo, preferredLayerFor stream: IVSRemoteStageStream) -> IVSRemoteStageStreamLayer? {
    If appState.isAutoMode {
        return nil
    } else {
        return appState.layerChoice
    }
}
```

### Option 3: RemoteStageStream Layer Helpers

`IVSRemoteStageStream` has several helpers which can be used to
make decisions about layer selection and display the corresponding selections to
end users:

- **Layer Events** — Alongside
  `IVSStageRenderer`, the
  `IVSRemoteStageStreamDelegate` has events which
  communicate layer and simulcast adaption changes:
  - `func stream(_ stream: IVSRemoteStageStream,
didChangeAdaption adaption: Bool)`
  - `func stream(_ stream: IVSRemoteStageStream, didChange
layers: [IVSRemoteStageStreamLayer])`
  - `func stream(_ stream: IVSRemoteStageStream, didSelect
layer: IVSRemoteStageStreamLayer?, reason:
IVSRemoteStageStream.LayerSelectedReason)`

- **Layer Methods** —
  `IVSRemoteStageStream` has several helper methods which
  can be used to get information about the stream and the layers being
  presented. These methods are available on the remote stream provided in
  the `preferredLayerForStream` strategy, as well as remote
  streams exposed via `func stage(_ stage: IVSStage, participant:
IVSParticipantInfo, didAdd streams: [IVSStageStream])`.
  - `stream.layers`
  - `stream.selectedLayer`
  - `stream.lowestQualityLayer`
  - `stream.highestQualityLayer`
  - `stream.layers(with:
IVSRemoteStageStreamLayerConstraints)`

For details, see the `IVSRemoteStageStream` class in the [SDK
reference documentation](https://aws.github.io/amazon-ivs-broadcast-docs/latest/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/latest/ios/"). For the `LayerSelected` reason,
if `UNAVAILABLE` is returned, this indicates that the requested layer
could not be selected. A best-effort selection is made in its place, which
typically is a lower quality layer to maintain stream stability.

## Broadcast the Stage to an

IVS Channel

To broadcast a stage, create a separate `IVSBroadcastSession` and then
follow the usual instructions for broadcasting with the SDK, described above. The
`device` property on `IVSStageStream` will be either an
`IVSImageDevice` or `IVSAudioDevice` as shown in the
snippet above; these can be connected to the `IVSBroadcastSession.mixer`
to broadcast the entire stage in a customizable layout.

Optionally, you can composite a stage and broadcast it to an IVS low-latency
channel, to reach a larger audience. See [Enabling Multiple
Hosts on an Amazon IVS Stream](../LowLatencyUserGuide/multiple-hosts.md "../LowLatencyUserGuide/multiple-hosts.md") in the IVS Low-Latency Streaming User
Guide.
