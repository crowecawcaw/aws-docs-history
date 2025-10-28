# Updating browser streams

You can update browser streams to enable or disable automation. This is useful when
you need to enter sensitive information like login credentials that you don't want the
agent to see.

Boto3

```
response = dp_client.update_browser_stream(
    browserIdentifier="aws.browser.v1",
    sessionId="<your-session-id>",
    streamUpdate={
        "automationStreamUpdate": {
            "streamStatus": "DISABLED"  # or "ENABLED"
        }
    }
)
```

API

```
awscurl -X PUT \
  "https://bedrock-agentcore.<Region>.amazonaws.com/browsers/aws.browser.v1/sessions/streams/update?sessionId=<your-session-id>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region> \
  -d '{
    "streamUpdate": {
            "automationStreamUpdate": {
              "streamStatus": "ENABLED"
            }
          }
  }'
```

CLI

```
aws bedrock-agentcore update-browser-stream \
  --region <Region> \
  --browser-id "<your-browser-id>" \
  --session-id "<your-session-id>" \
  --stream-update automationStreamUpdate={streamStatus=ENABLED}
```
