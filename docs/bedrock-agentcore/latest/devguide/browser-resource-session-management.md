# Resource and session management

The following topics show how the Amazon Bedrock AgentCore Browser works and how you can create the
resources and manage sessions.

## Permissions

To use the Amazon Bedrock AgentCore Browser, you need the following permissions in your IAM policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BedrockAgentCoreInBuiltToolsFullAccess",
 "Effect": "Allow",
 "Action": [
 "bedrock-agentcore:CreateBrowser",
 "bedrock-agentcore:ListBrowsers",
 "bedrock-agentcore:GetBrowser",
 "bedrock-agentcore:DeleteBrowser",
 "bedrock-agentcore:StartBrowserSession",
 "bedrock-agentcore:ListBrowserSessions",
 "bedrock-agentcore:GetBrowserSession",
 "bedrock-agentcore:StopBrowserSession",
 "bedrock-agentcore:UpdateBrowserStream",
 "bedrock-agentcore:ConnectBrowserAutomationStream",
 "bedrock-agentcore:ConnectBrowserLiveViewStream"
 ],
 "Resource": "arn:aws:bedrock-agentcore:`us-east-1`:`111122223333`:browser/*"
 }
 ]
}`

```

If you're using session recording with S3, the execution role you provide when creating
a browser needs the following permissions:

```
{
    "Sid": "BedrockAgentCoreBuiltInToolsS3Policy",
    "Effect": "Allow",
    "Action": [
        "s3:PutObject",
        "s3:ListMultipartUploadParts",
        "s3:AbortMultipartUpload"
    ],
    "Resource": "arn:aws:s3:::example-s3-bucket/example-prefix/*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "{{accountId}}"
        }
    }
}
```

You should also add the following trust policy to the execution role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "BedrockAgentCoreBuiltInTools",
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock-agentcore.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:bedrock-agentcore:`us-east-1`:`111122223333`:*"
 }
 }
 }]
}`

```

## Browser setup for API operations

Run the following commands to set up your Browser Tool that is common to all control
plane and data plane API operations.

```
import boto3
import uuid

REGION = `"<Region>"`
CP_ENDPOINT_URL = f"https://bedrock-agentcore-control.{REGION}.amazonaws.com"
DP_ENDPOINT_URL = f"https://bedrock-agentcore.{REGION}.amazonaws.com"

cp_client = boto3.client(
    'bedrock-agentcore-control',
    region_name=REGION,
    endpoint_url=CP_ENDPOINT_URL
)

dp_client = boto3.client(
    'bedrock-agentcore',
    region_name=REGION,
    endpoint_url=DP_ENDPOINT_URL
)
```

## Creating a Browser Tool and starting a

session

1. ###### Create a Browser Tool

When configuring a Browser Tool, choose the public network setting, recording
configuration for session replay, and permissions through an IAM runtime role that
defines what AWS resources the Browser Tool can access. 2. ###### Start a session

The Browser Tool uses a session-based model. After creating a Browser Tool, you
start a session with a configurable timeout period (default is 15 minutes). Sessions
automatically terminate after the timeout period. Multiple sessions can be active
simultaneously for a single Browser Tool, with each session maintaining its own state
and environment. 3. ###### Interact with the browser

Once a session is started, you can interact with the browser using WebSocket-based
streaming APIs. The Automation endpoint enables your agent to perform browser actions
such as navigating to websites, clicking elements, filling out forms, taking
screenshots, and more. Libraries like browser-use or Playwright can be used to
simplify these interactions.

Meanwhile, the Live View endpoint allows an end user to watch the browser session in
real time and interact with it directly through the live stream. 4. ###### Stop the session

When you're finished using the browser session, you should stop it to release
resources and avoid unnecessary charges. Sessions can be stopped manually or will
automatically terminate after the configured timeout period.
