# MediaConnect flow content quality event

AWS Elemental MediaConnect publishes the following event when an issue is detected with content quality: `MediaConnect Flow Content Quality`

MediaConnect publishes this event in three scenarios:

1. When the duration threshold is breached for one of the following
   metrics:
   - **Black frames**: Periods of black video frames are detected in the stream.
   - **Frozen frames**: Periods of unchanging video frames are detected in the stream.
   - **Silent audio**: Periods of audio silence are detected in the stream.

2. When audio or video content is missing from the stream. This happens when
   monitoring is configured for audio or video streams, but MediaConnect can’t detect
   the expected data to monitor.
3. When a previously reported issue has been resolved (clearing
   state).
   MediaConnect publishes these events whenever the state of any monitored condition
   changes. This includes when issues are first detected, when they clear, or
   any combination of these changes. For example, a single event might show
   some issues that are clearing while others are being detected, depending on
   what changed during that reporting period.

In the event JSON, you'll see the following fields to
indicate these issues:

###### For duration threshold breaches:

- `black_frames_duration_breaching`: true when black
  frames exceed the threshold
- `frozen_frames_duration_breaching`: true when frozen
  frames exceed the threshold
- `silent_audio_duration_breaching`: true when silent
  audio exceeds the threshold

###### For missing audio/video:

- `audio_missing`: true when audio content is
  missing
- `video_missing`: true when video content is
  missing
  These alerts are visible on the MediaConnect console, or by
  using the `describe-flow` AWS Command Line Interface (AWS CLI) command. For more information
  about the `describe-flow` command, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow.html").

For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following message is an example of the `MediaConnect Flow Content
 Quality` event. In this example, the event indicates both missing audio
content and a frozen frames duration threshold breach in the stream.

```
{
    "impacted": true,
    "streams": [
        {
            "audio_missing": true,
        },
        }
            "frozen_frames_duration_breaching": true,
        }
    ]
}
```
