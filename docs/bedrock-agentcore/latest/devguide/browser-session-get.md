# Get Browser session

You can get information about a browser session that you have created.

AWS CLI
To get information about a browser session using the AWS CLI, use the
`get-browser-session` command:

```

aws bedrock-agentcore get-browser-session \
  --region <Region> \
  --browser-identifier "aws.browser.v1" \
  --session-id "<your-session-id>"

```

Boto3
To get information about a browser session using the AWS SDK for Python
(Boto3), use the `get_browser_session` method:

###### Request Syntax

The following shows the request syntax:

```

response = dp_client.get_browser_session(
    browserIdentifier="aws.browser.v1",
    sessionId="<your-session-id>"
)

```

API
To get information about a browser session using the API, use the following
call:

```

# Using awscurl
awscurl -X GET \
  "https://bedrock-agentcore.<Region>.amazonaws.com/browsers/aws.browser.v1/sessions/get?sessionId=<your-session-id>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

{
  "browserIdentifier": "aws.browser.v1",
  "createdAt": "2025-07-14T22:16:40.713152248Z",
  "lastUpdatedAt": "2025-07-14T22:16:40.713152248Z",
  "name": "testBrowserSession1752531400",
  "sessionId": "<your-session-id>",
  "sessionReplayArtifact": null,
  "sessionTimeoutSeconds": 900,
  "status": "TERMINATED",
  "streams": {
    "automationStream": {
      "streamEndpoint": "wss://bedrock-agentcore.<Region>.amazonaws.com/browser-streams/aws.browser.v1/sessions/<your-session-id>/automation",
      "streamStatus": "ENABLED"
    },
    "liveViewStream": {
      "streamEndpoint": "https://bedrock-agentcore.<Region>.amazonaws.com/browser-streams/aws.browser.v1/sessions/<your-session-id>/live-view"
    }
  },
  "viewPort": {
    "height": 819,
    "width": 1456
  }
}

```
