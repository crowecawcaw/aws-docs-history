# Working with MQCS

MediaLive creates a media quality confidence score (MQCS) for the outputs in the following
types of output groups:

- CMAF Ingest output groups, when the destination for the outputs is an AWS Elemental MediaPackage
  channel.
  MediaPackage uses the score to make better decisions about handling inputs from MediaLive.

MediaLive generates the quality score of each frame segment, and includes that score in the
output. The score is a number from 0 to 100, where 100 is the best quality. The score is
based on the characteristics of the input and output. All of the following conditions reduce
the quality score:

- Black Frames: The source in the input consists of black frames.
- Freeze Frames: The source in the input consists of freeze frames.
- Fill Frame Insertion: MediaLive has detected a problem with the input and is encoding
  frames according to its input loss handling. For more information, see [Handling loss of video input](feature-input-loss.md "feature-input-loss.md").
- Video Frame Drops: MediaLive has dropped one or more frames without encoding them. The
  frames didn’t get included in the output.
- SVQ : SVQ stands for speed versus quality. MediaLive has intentionally reduced the
  quality of a video encode in order to maintain realtime operation. This condition is
  very rare.

## Setting up

The MQCS feature is enabled automatically in the applicable output. No setup is
required.

## Monitoring the MQCS

MediaLive generates metrics with information about the quality score. See [MQCS metrics](eml-metrics-quality-score.md "eml-metrics-quality-score.md").

MediaLive generates alert 6045 when the quality score drops below the acceptable level.
See [List of alerts for channels](monitor-activity-types-alerts-channels.md "monitor-activity-types-alerts-channels.md").
