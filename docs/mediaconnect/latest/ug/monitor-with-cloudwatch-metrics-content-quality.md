# AWS Elemental MediaConnect

metrics to monitor content quality

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to
evaluate the quality of the content that's transmitted by MediaConnect.

## Content quality metrics

The following table lists the content quality metrics that AWS Elemental MediaConnect
sends to CloudWatch.

| Metric                  | Description                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| `AudioStreamMissing`    | Monitors instances when the expected audio stream is not detected in the content.            |
| `BlackFramesBreaching`  | Tracks the duration of black frames in the video that surpasses the specified threshold.     |
| `FrozenFramesBreaching` | Monitors instances when the video remains unchanged for longer than the specified threshold. |
| `SilentAudioBreaching`  | Measures the duration of silent audio that exceeds the specified threshold.                  |
| `TimecodePresent`       | Indicates whether a valid timecode is present in the media stream.                           |
| `VideoStreamMissing`    | Monitors instances when the expected video stream is absent from the content.                |
