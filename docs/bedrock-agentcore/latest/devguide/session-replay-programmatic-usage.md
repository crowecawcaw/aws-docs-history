# Session replay programmatic examples

For advanced use cases, you can build custom session replay viewers and integrate recording
data into your own analysis workflows.

The following GitHub examples show a standalone session replay viewer and what the
complete browser experience looks like when using the browser session replay
feature.

For additional examples, see [AgentCore Browser examples on GitHub](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/interactive_tools/ "https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/interactive_tools/").

The standalone session replay viewer is a separate tool for viewing recorded
browser sessions directly from Amazon S3 without creating a new browser.

- Connect directly to S3 to view recordings
- View any past recording by specifying its session ID
- Display error messages when artifacts are missing from S3, with console replay
  URLs specific to session ID
- Interactive video playback interface with timeline navigation
- Action markers on timeline showing form fills, clicks, and navigation
  events
- Observability table displaying pages traveled with duration and URL
  details
- Console events, CDP logs, and network logs for each page interaction
- Session duration tracking integrated at page level
- Real-time action verification with visual correlation between video and action
  data

```
# View the latest recording in a bucket
python view_recordings.py --bucket session-record-test-123456789012 --prefix replay-data

# View a specific recording
python view_recordings.py --bucket session-record-test-123456789012 --prefix replay-data --session 01JZVDG02M8MXZY2N7P3PKDQ74

# Use a specific AWS profile
python view_recordings.py --bucket session-record-test-123456789012 --prefix replay-data --profile my-profile

```

For reference, see [Standalone session replay viewer on GitHub](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/interactive_tools/live_view_sessionreplay/view_recordings.py "https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/interactive_tools/live_view_sessionreplay/view_recordings.py").

A comprehensive tool for creating browser sessions with recording capabilities and
advanced replay features.

- Create browser sessions with automatic recording to S3
- Live view with interactive control (take/release)
- Adjust display resolution on the fly
- Automatic session recording to S3
- Integrated session replay viewer with video player interface
- Timeline scrubbing with precise action location tracking
- Page-by-page analysis with navigation timeline and URL copying
- Form filling action verification with click location details
- Session duration tracking integrated at page level
- Real-time action verification with visual correlation between video and action
  data

```
# View the latest recording in a bucket
python -m live_view_sessionreplay.browser_interactive_session

```

For reference, see [Interactive browser session on GitHub](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/interactive_tools/live_view_sessionreplay/browser_interactive_session.py "https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/interactive_tools/live_view_sessionreplay/browser_interactive_session.py").
