# Starting a browser session

After creating a browser, you can start a session to interact with web applications.

AWS CLI
To start a Browser session using the AWS CLI, use the
`start-browser-session` command:

```

 aws bedrock-agentcore start-browser-session \
  --region <Region> \
  --browser-identifier "my-browser" \
  --name "my-browser-session" \
  --session-timeout-seconds 900 \
  --view-port width=1456,height=819

```

Boto3
To start a Browser session using the AWS SDK for Python (Boto3), use the
`start_browser_session` method:

###### Request Syntax

The following shows the request syntax:

```

response = dp_client.start_browser_session(
    browserIdentifier="aws.browser.v1",
    name="browser-session-1",
    sessionTimeoutSeconds=3600,
    viewPort={
        'height': 819,
        'width': 1456
    }
)

```

BrowserClient
To start a browser session using the BrowserClient class for more control over
the session lifecycle:

```

from bedrock_agentcore.tools.browser_client import BrowserClient

# Create a browser client
client = BrowserClient(region="us-west-2")

# Start a browser session
client.start()
print(f"Session ID: {client.session_id}")

try:
    # Generate WebSocket URL and headers
    url, headers = client.generate_ws_headers()

    # Perform browser operations with your preferred automation tool

finally:
    # Always close the session when done
    client.stop()

```

API
To create a new browser session using the API, use the following call:

```

# Using awscurl
awscurl -X PUT \
  "https://bedrock-agentcore.<Region>.amazonaws.com/browsers/aws.browser.v1/sessions/start" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region> \
  -d '{
    "name": "browser-session-abc12345",
    "description": "browser sandbox session",
    "sessionTimeoutSeconds": 300,
    "viewPort": {
       "height": 819,
       "width": 1456
    }
  }'

```
