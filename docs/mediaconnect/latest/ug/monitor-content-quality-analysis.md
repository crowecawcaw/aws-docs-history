# Monitoring with content quality

analysis in AWS Elemental MediaConnect

You can use MediaConnect content quality analysis to monitor your source streams more
effectively. This feature enables you to track specific audio and video metrics, helping
you ensure that your content meets required quality standards. By monitoring these metrics, you can quickly identify anomalies in your
streams, enabling you to promptly resolve issues and maintain content quality.

When used alongside other MediaConnect monitoring tools, content quality analysis
provides you with a comprehensive view of your stream's quality. This integrated
monitoring approach enables you to implement proactive measures and ensure a smooth and
reliable media delivery workflow.

###### Contents

- [Key points](#monitor-content-quality-analysis-key-points "#monitor-content-quality-analysis-key-points")
  - [How content quality
    analysis works](#how-content-quality-analysis-works "#how-content-quality-analysis-works")
  - [Considerations](#content-quality-analysis-considerations "#content-quality-analysis-considerations")

- [Next steps](#content-quality-analysis-next-steps "#content-quality-analysis-next-steps")

## Key points

### How content quality

analysis works

You can monitor for the following content quality issues:

- **Silent audio periods -** Use this
  metric to detect periods of audio silence in the stream. This is
  useful for catching muted microphones in live broadcasts, unintended
  silence in recordings, or audio encoding issues.
- **Black frames -** Use this metric to
  detect periods of black video frames in the stream. This is helpful
  for identifying issues in live broadcasts, pre-recorded content, or
  your video encoding process.
- **Frozen frames -** Use this metric
  to detect periods of unchanging video frames in the stream. This is
  valuable for live events, identifying equipment issues, or detecting
  problems in your content delivery.

For each metric, you can set custom duration thresholds to fine-tune when
alerts are triggered based on your specific needs. MediaConnect then monitors
the status of the content within your source stream, posting warnings and alerts
when issues occur in the areas you've chosen to monitor.

### Considerations

- Content quality analysis works with transport stream source flows
  only. CDI flows and bridge flows aren't currently supported.
- The content quality analysis feature only monitors the first video
  stream and the first audio stream it encounters within a single
  source.
- Content quality analysis monitoring is limited to flows with 10
  outputs or fewer. If a flow exceeds 10 outputs, MediaConnect automatically
  disables content analysis for that flow.
- This feature is available at no additional charge in all AWS Regions
  where MediaConnect is available.

## Next steps

To get started with this feature, see [Enabling content quality analysis
and configuring thresholds](enable-content-quality-analysis.md "enable-content-quality-analysis.md").
