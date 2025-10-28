# Delete a session and all of its data

After you end a session, you can delete it with the [DeleteSession](../APIReference/API_agent-runtime_DeleteSession.md "../APIReference/API_agent-runtime_DeleteSession.md") API operation. Deleting a session deletes all Invocations, and InvocationSteps and
associated data. You can’t undo deleting a session.

The following example code shows how to delete a session with the AWS SDK for Python (Boto3).

```
def delete_session(session_identifier):
try:
    client.delete_session(
        sessionIdentifier=session_identifier
    )
    print("session deleted")
except ClientError as e:
    print(f"Error: {e}")
```
