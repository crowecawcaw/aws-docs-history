

# Monitoring
<a name="agent-access-mcp-server-monitoring"></a>

You can monitor agent activity through three services: AWS CloudTrail for session events, CloudWatch for operational metrics, and Amazon S3 for stored screenshots.
+ **AWS CloudTrail**: logs the following agent session activity:
  + When an agent connects to a session
  + The tools an agent calls
  + When a session ends

  Tool calls are recorded as data events, one for each `agentaccess-mcp` action the agent invokes (for example, `GetScreenshot`, `LeftClick`, or `TypeText`). For the full list of actions, see [Agent and permissions requirements](agent-access-mcp-prerequisites.md#agent-access-prereqs-agent). Because these are data events, you must set up a trail to log them. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *CloudTrail User Guide*.
+ **CloudWatch**: the following operational metrics are available in CloudWatch for agent sessions:
  + `Invocations`
  + `Latency`
  + `ClientErrors`
  + `ServerErrors`
  + `McpSessionStart`
  + `McpSessionDuration`
+ **Amazon S3**: if you configure screenshot storage, screenshots captured during agent sessions are available in the Amazon S3 bucket that you specify. Screenshots are stored with the following key format:

  ```
  agentaccess/screenshots/year={{YYYY}}/month={{MM}}/day={{DD}}/{{session-id}}/{{timestamp}}.png
  ```

  The {{session-id}} in the path is the WorkSpaces Applications streaming session ID.