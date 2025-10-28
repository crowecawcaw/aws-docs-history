# Listing browser sessions

You can list all active browser sessions to monitor and manage your resources. This is
useful for tracking active sessions, identifying long-running sessions, or finding
sessions that need to be stopped.

AWS CLI
To list Browser sessions using the AWS CLI, use the
`list-browser-sessions` command:

```

aws bedrock-agentcore list-browser-sessions \
  --region <Region> \
  --browser-id "<your-browser-id>" \
  --max-results 10

```

You can also filter sessions by status:

```

aws bedrock-agentcore list-browser-sessions \
  --region <Region> \
  --browser-id "<your-browser-id>" \
  --status "READY"

```

Boto3
To list Browser sessions using the AWS SDK for Python (Boto3), use the
`list_browser_sessions` method:

###### Request Syntax

The following shows the request syntax:

```

response = dp_client.list_browser_sessions(
    browserIdentifier="aws.browser.v1"
)

```

You can also filter sessions by status:

```

# List only active sessions
filtered_response = dp_client.list_browser_sessions(
    browserIdentifier="aws.browser.v1",
    status="READY"
)

# Print filtered session information
for session in filtered_response['items']:
    print(f"Ready Session ID: {session['sessionId']}")
    print(f"Name: {session['name']}")
    print("---")

```

API
To list browser sessions using the API, use the following call:

```

# Using awscurl
awscurl -X POST \
  "https://bedrock-agentcore.<Region>.amazonaws.com/browsers/<your-browser-id>/sessions/list" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region> \
  -d '{
    "maxResults": 10
  }'

```

You can also filter sessions by status:

```

# Using awscurl
awscurl -X POST \
  "https://bedrock-agentcore.<Region>.amazonaws.com/browsers/aws.browser.v1/sessions/list" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region> \
  -d '{
    "maxResults": 10,
    "status": "READY"
  }'

```
