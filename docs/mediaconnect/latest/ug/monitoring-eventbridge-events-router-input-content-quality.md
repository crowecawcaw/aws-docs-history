# MediaConnect router input content quality event

AWS Elemental MediaConnect publishes the following event when the content quality status changes
on a router input: `MediaConnect Router Input Content Quality`

MediaConnect publishes this event in three scenarios:

1. When the duration threshold is breached for one of the following
   metrics:

   - **Black frames**: Periods of black
     video frames are detected in the stream.
   - **Frozen frames**: Periods of
     unchanging video frames are detected in the stream.
   - **Silent audio**: Periods of audio
     silence are detected in the stream.

2. When audio or video content is missing from the stream. This happens when
   monitoring is configured for audio or video streams, but MediaConnect can't detect
   the expected data to monitor.
3. When a previously reported issue has been resolved (clearing
   state).
   The event includes both the `current` and `previous` state
   for each monitored metric. Each metric reports one of the following values:

- `DETECTED` – The issue is actively being detected
  (threshold breached or stream missing).
- `NOT_DETECTED` – The metric is enabled and no issue is
  detected.
- `DISABLED` – The metric is not enabled for this router
  input.
  The event detail contains the following fields:

- `blackFrames`: Status of black frames detection.
- `frozenFrames`: Status of frozen frames detection.
- `silentAudio`: Status of silent audio detection.
- `audioMissing`: Status of audio stream presence.
- `videoMissing`: Status of video stream presence.
  You can view content quality analysis status for a router input on the MediaConnect
  console, or by using the `get-router-input` AWS Command Line Interface (AWS CLI) command.
  For more information about the `get-router-input` command, see the [AWS CLI Command Reference](../../../cli/latest/reference/mediaconnect/get-router-input.md "../../../cli/latest/reference/mediaconnect/get-router-input.md").

For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following message is an example of the `MediaConnect Router Input Content
 Quality` event. In this example, the event indicates that black frames
have been detected on the router input, while the previous state showed no issues
detected.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Input Content Quality",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerInput:1-AbCdEfGhIjKlMnOp-abcdef123456"
  ],
  "detail": {
    "current": {
      "blackFrames": "DETECTED",
      "frozenFrames": "NOT_DETECTED",
      "silentAudio": "NOT_DETECTED",
      "audioMissing": "NOT_DETECTED",
      "videoMissing": "NOT_DETECTED"
    },
    "previous": {
      "blackFrames": "NOT_DETECTED",
      "frozenFrames": "NOT_DETECTED",
      "silentAudio": "NOT_DETECTED",
      "audioMissing": "NOT_DETECTED",
      "videoMissing": "NOT_DETECTED"
    }
  }
}
```
