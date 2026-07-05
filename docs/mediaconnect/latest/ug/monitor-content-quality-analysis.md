# Monitoring with content quality analysis in AWS Elemental MediaConnect

You can use MediaConnect content quality analysis to monitor your source streams and
router inputs more effectively. Use this feature to track specific audio and
video metrics and ensure that your content meets required quality standards.
By monitoring these metrics, you can quickly identify anomalies in your streams
and promptly resolve issues to maintain content quality.

Content quality analysis is available for both MediaConnect flows and router inputs.
When used alongside other MediaConnect monitoring tools, content quality analysis provides
you with a comprehensive view of your stream's quality. With this integrated monitoring
approach, you can implement proactive measures and ensure a smooth and reliable
media delivery workflow.

## Key points

### How content quality analysis works

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
the status of the content within your source stream or router input, posting
warnings and alerts when issues occur in the areas you've chosen to
monitor.

You can enable content quality analysis for MediaConnect flows and router inputs.

### Considerations

Note the following when using content quality analysis.

- MediaConnect monitors only the first video track and
  the first audio track within the stream.
- MediaConnect monitors only the first program within a multi-program transport stream (MPTS).

###### Flows

The following considerations apply to flows.

- Content quality analysis is limited to flows with 10 outputs or
  fewer. If a flow exceeds 10 outputs, MediaConnect automatically disables
  content quality analysis for that flow.
- Content quality analysis is not currently supported for CDI flows
  and MediaConnect Gateway bridges.

###### Router inputs

The following considerations apply to router inputs.

- Content quality analysis is automatically disabled when the aggregate
  bitrate on a router input exceeds 400 Mbps. It is also disabled when
  more than 10 router outputs are connected to the router.

## Next steps

To get started with this feature, see [Enabling content quality analysis](enable-content-quality-analysis.md "enable-content-quality-analysis.md").
