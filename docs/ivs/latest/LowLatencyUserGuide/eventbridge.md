# Using Amazon EventBridge with IVS Low-Latency Streaming

You can use Amazon EventBridge to monitor your Amazon Interactive Video Service (IVS)
streams.

Amazon IVS sends change events about the status of your streams to Amazon EventBridge. All
events that are delivered are valid. However, events are sent on a best-effort basis, which
means there is no guarantee that:

- Events are delivered — A designated event can occur (e.g., a stream starts) but it
  is possible that Amazon IVS will not send a corresponding change event to
  EventBridge. Amazon IVS tries to deliver events for several hours before giving
  up.
- Events that are delivered will arrive in a specified timeframe — You may receive
  events up to a few hours old.
- Events are delivered in order — Events may be out of order, especially if they are
  sent within a short time of each other. For example, you could see Stream Down
  before Stream Up.
  While it's rare for events to be missing, late, or out of sequence, you should handle
  these possibilities if you write business-critical programs that depend on the order or
  existence of notification events.

You can create EventBridge rules for any of the following events.

| Event Type                 | Event                   | Sent When ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| IVS Stream State Change    | Session Created         | A channel stream key was used successfully and a stream session was<br>created. This event fires when a stream is initiated, before video is<br>processed or delivered to viewers. This event can help you determine if a<br>stream was initiated but failed to go live; e.g., due to misconfiguration or<br>limit breach.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| IVS Stream State Change    | Session Ended           | The encoder disconnected and Amazon IVS is no longer receiving video.<br>This event can help you determine when the encoder stopped sending media.<br>For multitrack streams, the `code` field can provide additional details on why the<br>session ended. For details, see the `code` field in the [StreamEvent](../LowLatencyAPIReference/API_StreamEvent.md "../LowLatencyAPIReference/API_StreamEvent.md")<br>API object.<br>Note: When the encoder disconnects, the Session Ended event may<br>come before the Stream End event. This is because there may be a short<br>period of time after the Session Ended event when Amazon IVS is still<br>processing video.                                                                                                                                                                                                 |
| IVS Stream State Change    | Stream Start            | A stream is being processed and segments are available for the viewer to<br>watch. This event indicates that the video stream is being processed and can<br>be watched by viewers. This event can help you determine if a stream went<br>live successfully.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| IVS Stream State Change    | Stream End              | A stream stops being processed and no longer produces video segments for<br>the viewer. This event can help you determine when the stream ended and no<br>new video segments can be consumed by the viewers. (Also see the note in<br>Session Ended.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| IVS Stream State Change    | Stream Failure          | A stream is not being processed and is not available because processing<br>capacity was exceeded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IVS Stream State Change    | Stream Takeover         | An existing stream was taken over.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| IVS Stream State Change    | Stream Takeover Failure | An attempt to take over an existing stream was rejected. The `code` field provides<br>additional details on why the stream takeover failed. There are several values; note that<br>the long descriptions are provided in the IVS console but not delivered through<br>the IVS API or EventBridge:<br>• `StreamTakeoverMediaMismatch` — The broadcast client attempted to take over<br>with different media properties (e.g., codec, resolution, or video track type) from the<br>original stream.<br>• `StreamTakeoverInvalidPriority` — The broadcast client attempted a takeover<br>with either a priority integer value equal to or lower than the original stream's value or a value outside<br>the allowed range of 1 to 2,147,483,647.<br>• `StreamTakeoverLimitBreached` — The broadcast client reached the maximum allowed<br>takeover attempts for this stream. |
| IVS Stream Health Change   | Starvation Start        | A stream is not receiving data from the streamer; the stream is said to<br>be in “starvation.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| IVS Stream Health Change   | Starvation End          | A starving stream begins receiving data from the streamer and the stream<br>is healthy again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| IVS Limit Breach           | Ingest Bitrate          | The incoming stream’s bitrate exceeds the Amazon IVS limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| IVS Limit Breach           | Ingest Resolution       | The incoming stream’s resolution exceeds the Amazon IVS limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| IVS Limit Breach           | Concurrent Broadcasts   | The total number of channels streaming at the same time exceeds the<br>Amazon IVS limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| IVS Limit Breach           | Concurrent Viewers      | The total number of viewers watching your channels at the same time<br>exceeds the Amazon IVS limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| IVS Recording State Change | Recording Start         | A stream starts being processed, and the recording prefix is<br>created and validated. Segments will be written to the storage location<br>configured for the channel.<br>Note that after a live stream starts and the Recording Start event is<br>emitted, it takes a little time before the manifest files and video<br>segments are written to the S3 bucket that is configured for the<br>channel. We recommend that you play back or process recorded streams<br>only after the Recording End event is sent.                                                                                                                                                                                                                                                                                                                                                        |
| IVS Recording State Change | Recording End           | A stream ends and recording stops for this channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| IVS Recording State Change | Recording Start Failure | A stream starts but recording fails to start due to errors (for example,<br>the S3 bucket does not exist or is not in the correct region). This live<br>stream is not recorded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| IVS Recording State Change | Recording End Failure   | Recording ends with failure, due to errors encountered during recording<br>(e.g., if the attempt to write a master playlist fails). Some objects may<br>still be written to the configured storage location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Note on stream IDs:** The `stream_id` field (in
many events) is a unique stream identifier assigned each time a channel goes live. For a
given channel, each live stream has a new `stream_id`. Hence, each channel ARN
can have many corresponding stream IDs. Stream IDs allow customers to distinguish different
stream sessions on the same channel.

**Note on latency of some events:** Encoder-configuration
settings, especially the IDR/keyframe interval, affect the timing of stream startup and the
latency of related events (Stream Start and Recording Start). A shorter keyframe interval
decreases this latency. See ["Reducing
Latency"](streaming-config.md#streaming-config-reducing-latency "streaming-config.md#streaming-config-reducing-latency") in _Amazon IVS Streaming Configuration_
for information on setting `IDR/Keyframe`.

## Creating Amazon EventBridge Rules for

Amazon IVS

You can create a rule that triggers on an event emitted by Amazon IVS. Follow the
steps in [Create a rule in Amazon
EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User
Guide_. When selecting a service, choose **Interactive
Video Service (IVS)**.

## Examples: Stream State

Change

**Session Created:** This event is sent when a channel stream key was used successfully and a stream session was created.

```
{
   "version": "0",
   "id": "aa5b7a40-36cf-8dc4-5554-32d70e047215",
   "detail-type": "IVS Stream State Change",
   "source": "aws.ivs",
   "account": "535011710559",
   "time": "2024-09-09T16:17:26Z",
   "region": "us-east-1",
   "resources": [
      "arn:aws:ivs:us-west-2:535011710559:channel/UCGaMPGLCbcE"
   ],
   "detail": {
      "event_name": "Session Created",
      "channel_name": "",
      "stream_id": "st-1AuTyMDASvHUTSb8p5PvbsO"
   }
}
```

**Session Ended:** This event is sent when the encoder disconnected and IVS is no longer receiving video.

```
{
   "version": "0",
   "id": "6f2723f3-ee31-9e48-b030-ac865e261a8e",
   "detail-type": "IVS Stream State Change",
   "source": "aws.ivs",
   "account": "535011710559",
   "time": "2024-09-09T16:17:26Z",
   "region": "us-east-1",
   "resources": [
      "arn:aws:ivs:us-west-2:535011710559:channel/UCGaMPGLCbcE"
   ],
   "detail": {
      "event_name": "Session Ended",
      "channel_name": "",
      "code": "MultitrackInputNotAllowed",
      "stream_id": "st-1AuTyMDASvHUTSb8p5PvbsO"
   }
}
```

**Stream Start:** This event is sent when a stream is
being processed and segments are available for the viewer.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Stream State Change",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
   ],
   "detail": {
     "event_name": "Stream Start",
     "channel_name": "Your Channel",
     "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

**Stream End:** This event is sent when a stream stops
being processed and no longer produces video segments for the viewer.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Stream State Change",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
   ],
   "detail": {
     "event_name": "Stream End",
     "channel_name": "Your Channel",
     "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

**Stream Failure:** This event is sent when a stream is
not being processed and is not available because processing capacity was
exceeded.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Stream State Change",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
   ],
   "detail": {
     "event_name": "Stream Failure",
     "channel_name": "Your Channel",
     "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn",
     "reason": "Transcode capacity exceeded. Please try again."
   }
}
```

**Stream Takeover:** This event is sent when an existing stream was taken over.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Stream State Change",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [

"arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
],
   "detail": {
      "event_name": "Stream Takeover",
      "channel_name": "Your Channel",
      "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

**Stream Takeover Failure:** This event is sent when an attempt to take over an existing
stream was rejected. This can be due to mismatched codec/resolution/video-track type, an invalid priority integer,
or surpassing the maximum number of takeovers per stream.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Stream State Change",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
       "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
],
   "detail": {
      "event_name": "Stream Takeover Failure",
      "channel_name": "Your Channel",
      "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn",
      "code": "StreamTakeoverInvalidPriority"
   }
}
```

## Examples: Stream Health

Change

**Starvation Start:** This event is sent when a stream is
not receiving data from the streamer; the stream is said to be in “starvation.”

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Stream Health Change",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
   ],
   "detail": {
     "event_name": "Starvation Start",
     "channel_name": "Your Channel",
     "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

**Starvation End:** This event is sent when a starving
stream begins receiving data from the streamer and the stream is healthy again.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Stream Health Change",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
   ],
   "detail": {
     "event_name": "Starvation End",
     "channel_name": "Your Channel",
     "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

## Examples: Limit Breach

All limit-breach events include the name of the limit that is breached, the value of
the limit, and the number by which the limit was exceeded (value at breach subtracted by
the limit).

**Ingest Bitrate:** This event is sent when the incoming
stream’s bitrate exceeds the Amazon IVS limit.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Limit Breach",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
   ],
   "detail": {
     "limit_name": "Ingest Bitrate",
     "limit_value": 1234,
     "exceeded_by": 3,
     "limit_unit": "bits per second",
     "channel_name": "Your Channel",
     "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

**Ingest Resolution:** This event is sent when the
incoming stream’s resolution (total pixels or pixels per edge) exceeds the Amazon IVS
limits.

Maximum total pixels exceeded:

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Limit Breach",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
      "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"
   ],
   "detail": {
      "limit_name": "Ingest Resolution",
      "limit_value": 495000,
      "exceeded_by": 426600,
      "limit_unit": "total pixels",
      "channel_name": "Your Channel",
      "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

Maximum pixels per edge exceeded:

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Limit Breach",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [
      "arn:aws:ivs:us-east-1:aws_account_id:channel/12345678-1a23-4567-a1bc-1a2b34567890"TBD
   ],
   "detail": {
      "limit_name": "Ingest Resolution",
      "limit_value": 855,
      "exceeded_by": 45,
      "limit_unit": "pixels per edge",
      "channel_name": "Your Channel",
      "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn"
   }
}
```

**Concurrent Broadcasts:** This event is sent when the
total number of channels streaming at the same time exceeds the Amazon IVS limit.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Limit Breach",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [],
   "detail": {
     "limit_name": "Concurrent Broadcasts",
     "limit_value": 2,
     "exceeded_by": 3,
     "limit_unit": "active streams"
   }
}
```

**Concurrent Viewers:** This event is sent when the total
number of viewers watching your channels at the same time exceeds the Amazon IVS
limit.

```
{
   "version": "0",
   "id": "01234567-0123-0123-0123-012345678901",
   "detail-type": "IVS Limit Breach",
   "source": "aws.ivs",
   "account": "aws_account_id",
   "time": "2017-06-12T10:23:43Z",
   "region": "us-east-1",
   "resources": [],
   "detail": {
     "limit_name": "Concurrent Viewers",
     "limit_value": 10,
     "exceeded_by": 11,
     "limit_unit": "viewers"
   }
}
```

## Examples: Recording State

Change

For all recording state change events, the top-level path where all objects for this
live stream are stored is `recording_s3_key_prefix`. In the case of failures,
the reason for the failure is in `recording_status_reason`. The
`recording_duration_ms` field is the number of milliseconds of recording
duration.

**Recording Start:** This event is sent when a stream
starts being processed and segments are being written to the storage location configured
for the channel.

```
{
    "version": "0",
    "id": "12345678-1a23-4567-a1bc-1a2b34567890",
    "detail-type": "IVS Recording State Change",
    "source": "aws.ivs",
    "account": "123456789012",
    "time": "2020-06-23T20:12:36Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ivs:us-west-2:123456789012:channel/AbCdef1G2hij"
    ],
    "detail": {
        "channel_name": "Your Channel",
        "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn",
        "recording_status": "Recording Start",
        "recording_status_reason": "",
        "recording_s3_bucket_name": "r2s3-dev-channel-1-recordings",
        "recording_s3_key_prefix": "ivs/v1/123456789012/AbCdef1G2hij/2020/6/23/20/12/j8Z9O91ndcVs",
        "recording_duration_ms": 0,
        "recording_session_id": "a6RfV23ES97iyfoQ"
    }
}
```

**Recording End:** This event is sent when a stream ends
and recording stops for this channel.

```
{
    "version": "0",
    "id": "12345678-1a23-4567-a1bc-1a2b34567890",
    "detail-type": "IVS Recording State Change",
    "source": "aws.ivs",
    "account": "123456789012",
    "time": "2020-06-24T07:51:32Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ivs:us-west-2:123456789012:channel/AbCdef1G2hij"
    ],
    "detail": {
        "channel_name": "Your Channel",
        "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn",
        "recording_status": "Recording End",
        "recording_status_reason": "",
        "recording_s3_bucket_name": "r2s3-dev-channel-1-recordings",
        "recording_s3_key_prefix": "ivs/v1/123456789012/AbCdef1G2hij/2020/6/23/20/12/j8Z9O91ndcVs",
        "recording_duration_ms": 99370264,
        "recording_session_id": "a6RfV23ES97iyfoQ",
        "recording_session_stream_ids": ["st-254sopYUvi6F78ghpO9vn0A", "st-1A2b3c4D5e6F78ghij9Klmn"]
    }
}
```

**Recording Start Failure:** This event is sent when a
stream starts but recording fails to start due to errors (for example, the S3 bucket
does not exist or is not in the correct region). This live stream is not recorded.

```
{
    "version": "0",
    "id": "12345678-1a23-4567-a1bc-1a2b34567890",
    "detail-type": "IVS Recording State Change",
    "source": "aws.ivs",
    "account": "123456789012",
    "time": "2020-06-23T20:12:36Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ivs:us-west-2:123456789012:channel/AbCdef1G2hij"
    ],
    "detail": {
        "channel_name": "Your Channel",
        "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn",
        "recording_status": "Recording Start Failure",
        "recording_status_reason": "ValidationException",
        "recording_s3_bucket_name": "r2s3-dev-channel-1-recordings",
        "recording_s3_key_prefix": "",
        "recording_duration_ms": 0,
        "recording_session_id": "a6RfV23ES97iyfoQ"
    }
}
```

**Recording End Failure:** This event is sent when
recording ends with failure, due to errors encountered during recording. Some objects
may still be written to the configured storage location.

```
{
    "version": "0",
    "id": "12345678-1a23-4567-a1bc-1a2b34567890",
    "detail-type": "IVS Recording State Change",
    "source": "aws.ivs",
    "account": "123456789012",
    "time": "2020-06-24T07:51:32Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ivs:us-west-2:123456a7-ab1c-2d34-e5f6-1a2b3c4d5678"
    ],
    "detail": {
        "channel_name": "Your Channel",
        "stream_id": "st-1A2b3c4D5e6F78ghij9Klmn",
        "recording_status": "Recording End Failure",
        "recording_status_reason": "InternalServerException",
        "recording_s3_bucket_name": "r2s3-dev-channel-1-recordings",
        "recording_s3_key_prefix": "ivs/v1/123456789012/AbCdef1G2hij/2020/6/23/20/12/j8Z9O91ndcVs",
        "recording_duration_ms": 0,
        "recording_session_id": "a6RfV23ES97iyfoQ"
    }
}
```
