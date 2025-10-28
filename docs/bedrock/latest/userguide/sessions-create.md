# Create a session to prepare to store conversation history and context

To create a session, you use the [CreateSession](../APIReference/API_agent-runtime_CreateSession.md "../APIReference/API_agent-runtime_CreateSession.md") API operation. In the
response, Amazon Bedrock returns a unique session ID and Amazon Resource Name (ARN) for the session. You use either the session
ID or the ARN when you use the [CreateInvocation](../APIReference/API_agent-runtime_CreateInvocation.md "../APIReference/API_agent-runtime_CreateInvocation.md") and [PutInvocationStep](../APIReference/API_agent-runtime_PutInvocationStep.md "../APIReference/API_agent-runtime_PutInvocationStep.md") API operations to record the session events.

When you create a session, you can specify a AWS KMS key to encrypt conversations. For information about encryption, see [Session encryption](sessions-encryption.md "sessions-encryption.md").

```
def create_session():
try:
    session_id = client.create_session(
        encryptionKeyArn="arn:aws:kms:us-west-2:<123456789012>:key/keyId",
        tags={
            'Environment': 'Test',
            'Project': 'Demo'
        },
        sessionMetadata={
            "deviceType": "mobile"
        }
    )["sessionId"]
    print("Session created. Session ID: " + session_id)
    return session_id
except ClientError as e:
    print(f"Error: {e}")
```
