# Stopping a AgentCore Code Interpreter

session

When you are finished using a Code Interpreter session, you should stop it to release
resources and avoid unnecessary charges.

AWS CLI
To stop a code interpreter session using the AWS CLI, use the
`stop-code-interpreter-session` command:

```
aws bedrock-agentcore stop-code-interpreter-session \
  --region <Region> \
  --code-interpreter-id "<your-code-interpreter-id>" \
  --session-id "<your-session-id>"

```

Boto3
To stop a Code Interpreter session using the AWS SDK for Python, use the
`stop_code_interpreter_session` method:

```
import boto3

# Initialize the boto3 client
dp_client = boto3.client(
    'bedrock-agentcore',
    region_name="<Region>",
    endpoint_url="https://bedrock-agentcore.<Region>.amazonaws.com"
)

# Stop the Code Interpreter session
response = dp_client.stop_code_interpreter_session(
    codeInterpreterIdentifier="aws.codeinterpreter.v1",
    sessionId="<your-session-id>"
)

print("Session stopped successfully")

```

API
To stop a code interpreter session using the API, use the following call:

```
# Using awscurl
awscurl -X PUT \
  "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/sessions/stop?sessionId=<your-session-id>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

```
