

# Publishing and Subscribing with the IVS Linux Broadcast SDK \| Real-Time Streaming

This document takes you through the steps involved in publishing and subscribing to a stage using the IVS real-time streaming Linux broadcast SDK.

## Concepts
<a name="linux-publish-subscribe-concepts"></a>

Three core concepts underlie real-time functionality: [stage](#linux-publish-subscribe-concepts-stage), [strategy](#linux-publish-subscribe-concepts-strategy), and [hooks](#linux-publish-subscribe-concepts-hooks). The design goal is minimizing the amount of client-side logic necessary to build a working product.

### Stage
<a name="linux-publish-subscribe-concepts-stage"></a>

The stage is the main point of interaction between your application and the SDK. It represents the stage itself, and you use it to join and leave the stage. Creating and joining a stage requires a valid, unexpired token string from the control plane (represented as `token`). Joining and leaving a stage are simple.

------
#### [ C ]

```c
aws_ivs_realtime_stage* stage = NULL;
aws_ivs_realtime_error* error = NULL;
if (!aws_ivs_realtime_stage_create(token, strategy, &events, &stage, &error)) {
    // handle create error
    aws_ivs_realtime_error_destroy(error);
    return;
}
if (!aws_ivs_realtime_stage_join(stage, &error)) {
    // handle join error
    aws_ivs_realtime_error_destroy(error);
}
aws_ivs_realtime_stage_leave(stage, NULL); // Pass NULL when you do not need the error.
aws_ivs_realtime_stage_destroy(stage);
```

------
#### [ Go ]

```go
stage, err := realtime.NewStage(realtime.StageConfig{
    Token:    token,
    Strategy: strategy,
    Hooks:    hooks,
})
if err != nil {
    // handle create error
    return
}
defer stage.Close()
if err := stage.Join(); err != nil {
    // handle join error
}
stage.Leave() // Ignore the error when you do not need it.
```

------

`join` returns when the connection attempt starts, not when it succeeds. The SDK reports the progress through the connection state hook. After `leave`, the same stage can join again.

You give the stage its strategy and its hooks when you create it. The stage keeps both until you destroy it. To receive no events, pass `null` for the callback table in C, or leave `Hooks` empty in Go.

### Strategy
<a name="linux-publish-subscribe-concepts-strategy"></a>

The strategy provides a way for the host application to communicate the desired state of the stage to the SDK. Three functions need to be implemented: `subscription_types`, `should_publish`, and `streams_to_publish` (in Go: `SubscriptionTypes`, `ShouldPublish`, and `StreamsToPublish`). All are discussed below.

In C, fill in an `aws_ivs_realtime_stage_strategy_callbacks` table and create a strategy handle from it. Set `size` to the size of the table and supply all three callbacks. The SDK copies the table, so later changes to it have no effect. In Go, implement the `StageStrategy` interface.

------
#### [ C ]

```c
aws_ivs_realtime_stage_strategy_callbacks callbacks = {0};
callbacks.size = sizeof(callbacks);
callbacks.subscription_types = subscription_types;
callbacks.should_publish = should_publish;
callbacks.streams_to_publish = streams_to_publish;
callbacks.user_data = app;
aws_ivs_realtime_stage_strategy* strategy = NULL;
if (!aws_ivs_realtime_stage_strategy_create(&callbacks, &strategy, &error)) {
    // handle error
    aws_ivs_realtime_error_destroy(error);
    return;
}
// After the stage that uses it is destroyed:
aws_ivs_realtime_stage_strategy_destroy(strategy);
```

------
#### [ Go ]

```go
type strategy struct{}
func (s *strategy) SubscriptionTypes(participant realtime.ParticipantInfo) realtime.StreamType {
    return realtime.StreamTypeAudio
}
func (s *strategy) ShouldPublish(participant realtime.ParticipantInfo) bool {
    return false
}
func (s *strategy) StreamsToPublish(participant realtime.ParticipantInfo) realtime.PublishStreams {
    return realtime.PublishStreams{}
}
```

------

#### Subscribing to participants
<a name="linux-publish-subscribe-concepts-strategy-participants"></a>

When a remote participant joins the stage, the SDK queries the host application about the desired subscription state for that participant. Return `AUDIO` to subscribe to the audio of the participant, or `NONE` to not subscribe. When returning a value for this function, you do not need to worry about the publish state, current subscription state, or stage connection state. If `AUDIO` is returned, the SDK waits until the remote participant is publishing before subscribing, and it updates the host application through the hooks throughout the process.

The SDK does not support subscribing to or publishing video yet.

Here is a sample implementation:

------
#### [ C ]

```c
static aws_ivs_realtime_stream_type subscription_types(const aws_ivs_realtime_participant_info* participant, void* user_data) {
    return AWS_IVS_REALTIME_STREAM_TYPE_AUDIO;
}
```

------
#### [ Go ]

```go
func (s *strategy) SubscriptionTypes(participant realtime.ParticipantInfo) realtime.StreamType {
    return realtime.StreamTypeAudio
}
```

------

Use this implementation when your host application needs to hear every participant, such as a recording service.

For more information about subscribing based on participant attributes, see [Get Participant Attributes](#linux-publish-subscribe-attributes).

#### Publishing
<a name="linux-publish-subscribe-concepts-strategy-publishing"></a>

Once connected to the stage, the SDK queries the host application to see if the local participant should publish. This is invoked only on local participants that have permission to publish based on the provided token.

Here is a sample implementation:

------
#### [ C ]

```c
static bool should_publish(const aws_ivs_realtime_participant_info* participant, void* user_data) {
    return true;
}
```

------
#### [ Go ]

```go
func (s *strategy) ShouldPublish(participant realtime.ParticipantInfo) bool {
    return true
}
```

------

This is for an application that always publishes, such as a bot that plays audio into the stage. To stop publishing, return `false` and refresh the strategy.

#### Choosing streams to publish
<a name="linux-publish-subscribe-concepts-strategy-streams"></a>

When publishing, `streams_to_publish` determines what audio should be published. In C, name the audio source on the `streams` collector with `aws_ivs_realtime_publish_streams_set_audio`. Do not store the collector. In Go, return the source in a `PublishStreams` value.

The SDK compares the streams you name with the streams it already publishes. A stream it already publishes stays as is, and a stream you leave out stops. For more information about publishing audio, see [Publish Audio](#linux-publish-subscribe-publish-audio).

#### Updating the strategy
<a name="linux-publish-subscribe-concepts-strategy-updates"></a>

The strategy is intended to be dynamic: the values returned from any of the above functions can be changed at any time. For example, if the host application does not want to publish until it receives a command from your backend, you could return a variable from `should_publish` (something like `publish_requested`). When that variable changes, call `aws_ivs_realtime_stage_refresh_strategy` (Go: `Stage.RefreshStrategy`) to signal to the SDK that it should query the strategy for the latest values, applying only things that have changed.

If the SDK observes that the `should_publish` value has changed, it starts the publish process. If the SDK queries and all functions return the same value as before, the refresh call does not modify the stage.

------
#### [ C ]

```c
static bool should_publish(const aws_ivs_realtime_participant_info* participant, void* user_data) {
    struct app* app = user_data;
    return atomic_load(&app->publish_requested);
}
// When the command arrives:
atomic_store(&app->publish_requested, true);
aws_ivs_realtime_stage_refresh_strategy(stage, NULL);
```

------
#### [ Go ]

```go
type strategy struct {
    publishRequested atomic.Bool
}
func (s *strategy) ShouldPublish(participant realtime.ParticipantInfo) bool {
    return s.publishRequested.Load()
}
// When the command arrives:
s.publishRequested.Store(true)
stage.RefreshStrategy()
```

------

The SDK calls the strategy on its own thread, the same thread that calls the hooks. The command arrives on another thread, so the samples use an atomic flag.

If the return value of `subscription_types` changes from `AUDIO` to `NONE`, the SDK unsubscribes from that participant.

Generally, the stage uses the strategy to most efficiently apply the difference between the previous and current strategies, without the host application needing to worry about all the state required to manage it properly. Because of this, think of refreshing the strategy as a cheap operation, because it does nothing unless the strategy changes. You can refresh the strategy from inside a hook or strategy callback.

### Hooks
<a name="linux-publish-subscribe-concepts-hooks"></a>

The hooks communicate the state of the stage to the host application. In C, they are the function pointers in an `aws_ivs_realtime_stage_event_callbacks` table. In Go, they are the fields of `StageHooks`. Every hook is optional: leave it `null` in C, or `nil` in Go, to skip that event. The hooks are:

------
#### [ C ]

```c
typedef struct {
    size_t size;
    void* user_data;
    aws_ivs_realtime_connection_state_changed_cb on_connection_state_changed;
    aws_ivs_realtime_participant_joined_cb on_participant_joined;
    aws_ivs_realtime_participant_left_cb on_participant_left;
    aws_ivs_realtime_participant_metadata_updated_cb on_participant_metadata_updated;
    aws_ivs_realtime_participant_publish_state_changed_cb on_participant_publish_state_changed;
    aws_ivs_realtime_participant_subscribe_state_changed_cb on_participant_subscribe_state_changed;
    aws_ivs_realtime_streams_added_cb on_streams_added;
    aws_ivs_realtime_streams_removed_cb on_streams_removed;
    aws_ivs_realtime_streams_muted_changed_cb on_streams_muted_changed;
    aws_ivs_realtime_error_cb on_error;
} aws_ivs_realtime_stage_event_callbacks;
```

------
#### [ Go ]

```go
type StageHooks struct {
    OnConnectionStateChanged           func(ConnectionStateChangedEvent)
    OnParticipantJoined                func(ParticipantJoinedEvent)
    OnParticipantLeft                  func(ParticipantLeftEvent)
    OnParticipantMetadataUpdated       func(ParticipantMetadataUpdatedEvent)
    OnParticipantPublishStateChanged   func(ParticipantPublishStateChangedEvent)
    OnParticipantSubscribeStateChanged func(ParticipantSubscribeStateChangedEvent)
    OnStreamsAdded                     func(StreamsAddedEvent)
    OnStreamsRemoved                   func(StreamsRemovedEvent)
    OnStreamsMutedChanged              func(StreamsMutedChangedEvent)
    OnError                            func(ErrorEvent)
}
```

------

It is not expected that the information provided by the hooks impacts the return values of the strategy. For example, the return value of `subscription_types` is not expected to change when the publish state of a participant changes. If the host application wants to subscribe to a particular participant, it should return the desired subscription type regardless of that participant's publish state. The SDK is responsible for ensuring that the desired state of the strategy is acted on at the correct time based on the state of the stage.

The hooks are attached to the stage when you create it:

------
#### [ C ]

```c
static void on_connection_state_changed(aws_ivs_realtime_connection_state state, const aws_ivs_realtime_error* error, void* user_data) {
    if (error != NULL) {
        fprintf(stderr, "connection error %d: %s\n", error->code, error->message);
    }
}
aws_ivs_realtime_stage_event_callbacks events = {0};
events.size = sizeof(events);
events.on_connection_state_changed = on_connection_state_changed;
events.user_data = app;
if (!aws_ivs_realtime_stage_create(token, strategy, &events, &stage, &error)) {
    // handle error
    aws_ivs_realtime_error_destroy(error);
    return;
}
```

------
#### [ Go ]

```go
hooks := realtime.StageHooks{
    OnConnectionStateChanged: func(event realtime.ConnectionStateChangedEvent) {
        if event.Err != nil {
            log.Printf("connection error: %v", event.Err)
        }
    },
}
stage, err := realtime.NewStage(realtime.StageConfig{Token: token, Strategy: strategy, Hooks: hooks})
```

------

Only publishing participants trigger the participant joined hook. When a participant stops publishing or leaves the stage session, the SDK triggers the participant left hook. The local participant triggers the participant joined hook when the stage connects.

## Publish Audio
<a name="linux-publish-subscribe-publish-audio"></a>

The host application supplies the audio it publishes. Create an audio source that describes the audio you will push: the sample rate, the channel count, and the *Pulse Code Modulation (PCM)* format. Name the source in `streams_to_publish`, then push PCM to it as you produce it.

------
#### [ C ]

```c
aws_ivs_realtime_audio_source* audio_source = NULL;
if (!aws_ivs_realtime_audio_source_create(48000, 2, AWS_IVS_REALTIME_PCM_FORMAT_S16_INTERLEAVED, &audio_source, &error)) {
    // handle error
    aws_ivs_realtime_error_destroy(error);
    return;
}
// In the strategy:
static bool should_publish(const aws_ivs_realtime_participant_info* participant, void* user_data) {
    return true;
}
static void streams_to_publish(const aws_ivs_realtime_participant_info* participant, aws_ivs_realtime_publish_streams* streams, void* user_data) {
    struct app* app = user_data;
    aws_ivs_realtime_publish_streams_set_audio(streams, app->audio_source, NULL);
}
// On your audio thread, push 48 kHz stereo audio, 10 ms at a time:
enum { FRAMES = 480, CHANNELS = 2 };
int16_t samples[FRAMES * CHANNELS];
int64_t pts = 0;
while (running) {
    produce_audio(samples, FRAMES);
    if (!aws_ivs_realtime_audio_source_push_buffer(audio_source, (const uint8_t*)samples, sizeof(samples), FRAMES, pts, &error)) {
        // handle error
        aws_ivs_realtime_error_destroy(error);
        error = NULL;
    }
    pts += FRAMES;
    wait_until_next_buffer();
}
```

------
#### [ Go ]

```go
source, err := realtime.NewAudioSource(realtime.AudioSourceConfig{
    SamplesPerSec: 48000,
    NumChannels:   2,
    Format:        realtime.PCMFormatS16Interleaved,
})
if err != nil {
    // handle error
}
defer source.Close()
// In the strategy:
func (s *strategy) ShouldPublish(participant realtime.ParticipantInfo) bool {
    return true
}
func (s *strategy) StreamsToPublish(participant realtime.ParticipantInfo) realtime.PublishStreams {
    return realtime.PublishStreams{Audio: s.source}
}
// Push 48 kHz stereo audio, 10 ms at a time:
const frames = 480
var pts int64
ticker := time.NewTicker(10 * time.Millisecond)
defer ticker.Stop()
for range ticker.C {
    data := produceAudio(frames) // frames x 2 channels x 2 bytes
    if err := source.PushBuffer(realtime.AudioBuffer{Data: data, NumFrames: frames, PTS: pts}); err != nil {
        log.Printf("push failed: %v", err)
    }
    pts += frames
}
```

------

Push audio in real time, as you produce it, in buffers of 10 ms to 100 ms. The SDK does not pace audio, and it drops audio that you push faster than real time. For the supported formats and the other rules of the audio source, see the API documentation.

To stop publishing audio, leave the source out of `streams_to_publish` and refresh the strategy.

## Receive Participant Audio
<a name="linux-publish-subscribe-receive-audio"></a>

The SDK delivers subscribed audio as PCM, in one of two ways:
+ **Mixed audio**: One callback receives the audio of all subscribed participants, mixed together.
+ **Audio for each participant**: A callback on each audio stream receives the audio of that participant only, before mixing.

You can use both at the same time.

### Mixed audio
<a name="linux-publish-subscribe-receive-audio-mixed"></a>

Register the mixed audio callback before you join the stage, or after you leave it. The registration stays across leave and join.

------
#### [ C ]

```c
static void on_audio(const uint8_t* data, size_t data_size, size_t num_frames, size_t bytes_per_sample,
                     size_t num_channels, uint32_t samples_per_sec, int64_t timestamp_ms, void* user_data) {
    // Runs on the audio thread. Return promptly.
}
if (!aws_ivs_realtime_stage_set_audio_callback(stage, on_audio, app, &error)) {
    // handle error
    aws_ivs_realtime_error_destroy(error);
    return;
}
```

------
#### [ Go ]

```go
err := stage.SetPCMCallback(func(buf realtime.PCMBuffer) {
    // Runs on the audio thread. Return promptly.
    log.Printf("%d frames at %d Hz", buf.NumFrames, buf.SamplesPerSec)
})
```

------

For the format and lifetime of the audio data, see the API documentation of the audio callback.

### Audio for each participant
<a name="linux-publish-subscribe-receive-audio-per-participant"></a>

Register a callback on each audio stream in the streams added hook. The registration lasts as long as the stream. When a stream ends, the SDK reports it through the streams removed hook. A replacement stream has a new stream ID and needs its own registration.

------
#### [ C ]

```c
static void on_streams_added(const aws_ivs_realtime_participant_info* participant,
                             aws_ivs_realtime_stage_stream* const* streams, size_t streams_count, void* user_data) {
    if (participant->is_local) {
        return;
    }
    for (size_t i = 0; i < streams_count; i++) {
        aws_ivs_realtime_stream_type type;
        if (!aws_ivs_realtime_stage_stream_get_stream_type(streams[i], &type, NULL) || type != AWS_IVS_REALTIME_STREAM_TYPE_AUDIO) {
            continue;
        }
        // To tell participants apart, pass a per-participant context in place of user_data.
        aws_ivs_realtime_stage_stream_set_audio_callback(streams[i], on_participant_audio, user_data, NULL);
    }
}
```

------
#### [ Go ]

```go
OnStreamsAdded: func(event realtime.StreamsAddedEvent) {
    if event.Participant.IsLocal {
        return
    }
    participantID := event.Participant.ParticipantID
    for _, stream := range event.Streams {
        audio, ok := stream.(realtime.AudioStageStream)
        if !ok {
            continue
        }
        err := audio.SetPCMCallback(func(buf realtime.PCMBuffer) {
            // Runs on the audio thread. Return promptly.
            handleAudio(participantID, buf)
        })
        if err != nil {
            log.Printf("audio callback for %s: %v", participantID, err)
        }
    }
},
```

------

The registration stays active after the hook returns, so you do not need to keep the stream to keep receiving its audio.

To tell streams apart, compare their stream IDs (C: `aws_ivs_realtime_stage_stream_get_stream_id`, Go: `StreamID`). A stream ID is unique within the stage and does not change. In C, do not compare handle pointers, because a clone is a different pointer to the same stream.

When a participant stops publishing or you unsubscribe from them, the SDK calls the streams removed hook with the removed streams. You must use this as a signal to release the state you keep for those streams.

The SDK invokes the streams removed hook for all scenarios in which it might remove a stream, including:
+ The remote participant stops publishing.
+ The local participant unsubscribes from the remote participant.
+ The remote participant leaves the stage.
+ The local participant leaves the stage.

Because the SDK invokes the streams removed hook for all scenarios, you do not need custom business logic to release participant state during remote or local leave operations.

## Get Participant Attributes
<a name="linux-publish-subscribe-attributes"></a>

If you specify attributes in the `CreateParticipantToken` operation request, you can see the attributes in the participant info. For example, this strategy subscribes only to participants whose `role` attribute is `guest`:

------
#### [ C ]

```c
static const char* find_attribute(const aws_ivs_realtime_participant_info* participant, const char* key) {
    for (size_t i = 0; i < participant->attributes_count; i++) {
        if (strcmp(participant->attributes_keys[i], key) == 0) {
            return participant->attributes_values[i];
        }
    }
    return NULL;
}
static aws_ivs_realtime_stream_type subscription_types(const aws_ivs_realtime_participant_info* participant, void* user_data) {
    const char* role = find_attribute(participant, "role");
    if (role != NULL && strcmp(role, "guest") == 0) {
        return AWS_IVS_REALTIME_STREAM_TYPE_AUDIO;
    }
    return AWS_IVS_REALTIME_STREAM_TYPE_NONE;
}
```

------
#### [ Go ]

```go
func (s *strategy) SubscriptionTypes(participant realtime.ParticipantInfo) realtime.StreamType {
    switch participant.Attributes["role"] {
    case "guest":
        return realtime.StreamTypeAudio
    default:
        return realtime.StreamTypeNone
    }
}
```

------

You can use this to create a host application that listens only to guests and ignores moderators.

When the user ID or attributes of a participant change, the participant metadata updated hook delivers the new participant info. It has the same participant ID as before.

## Handling Network Issues
<a name="linux-publish-subscribe-network"></a>

If the network connection drops, the SDK tries to reconnect without action from the host application. If it cannot reconnect, the connection state hook reports `DISCONNECTED` with an error. Call `join` again after the network connection recovers. If `join` fails with a fatal error, create a new stage.

------
#### [ C ]

```c
static void on_connection_state_changed(aws_ivs_realtime_connection_state state, const aws_ivs_realtime_error* error, void* user_data) {
    if (state == AWS_IVS_REALTIME_CONNECTION_STATE_DISCONNECTED && error != NULL) {
        // schedule a rejoin
    }
}
```

------
#### [ Go ]

```go
OnConnectionStateChanged: func(event realtime.ConnectionStateChangedEvent) {
    if event.State == realtime.ConnectionStateDisconnected && event.Err != nil {
        // schedule a rejoin
    }
},
```

------