# Stopping a browser session

When you are finished using a Browser session, you should stop it to release
resources and avoid unnecessary charges.

AWS CLI
To stop a Browser session using the AWS CLI, use the
`stop-browser-session` command:

```

aws bedrock-agentcore stop-browser-session \
  --region <Region> \
  --browser-id "<your-browser-id>" \
  --session-id "<your-session-id>"

```

Boto3
To stop a Browser session using the AWS SDK for Python (Boto3), use the
`stop_browser_session` method:

###### Request Syntax

The following shows the request syntax:

```

response = dp_client.stop_browser_session(
        browserIdentifier="aws.browser.v1",
        sessionId="<your-session-id>",
    )

```

API
To stop a browser session using the API, use the following call:

```

# Using awscurl
awscurl -X PUT \
  "https://bedrock-agentcore.<Region>.amazonaws.com/browsers/aws.browser.v1/sessions/stop?sessionId=<your-session-id>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

```
