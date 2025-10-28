# Retrieve conversation history and context from a session

Use the [GetSession](../APIReference/API_agent-runtime_GetSession.md "../APIReference/API_agent-runtime_GetSession.md"), [ListInvocations](../APIReference/API_agent-runtime_ListInvocations.md "../APIReference/API_agent-runtime_ListInvocations.md"), and [GetInvocationStep](../APIReference/API_agent-runtime_GetInvocationStep.md "../APIReference/API_agent-runtime_GetInvocationStep.md") API operations to retrieve session details, details for
the interaction state at different checkpoints, and summary information for all invocations.

The following example code shows how to get text and image data for a checkpoint with
the AWS SDK for Python (Boto3) and the [GetInvocationStep](../APIReference/API_agent-runtime_GetInvocationStep.md "../APIReference/API_agent-runtime_GetInvocationStep.md") API operation.

```
def get_invocation_step(invocation_identifier, session_identifier, invocation_step_identifier):
try:
    response = client.get_invocation_step(
        sessionIdentifier=session_identifier,
        invocationIdentifier=invocation_identifier,
        invocationStepId=invocation_step_identifier
    )  ["invocationStep"]["payload"]["contentBlocks"]
    print(response)
except ClientError as e:
    print(f"Error: {e}")
```
