# Manage an A/B test

Update an A/B test to start it, pause it, or stop it. You use the `UpdateABTest` operation to change execution status.

## Code samples

### Start, pause, and stop

###### Example

AgentCore CLI
Start (resume) a paused test:

```
agentcore resume ab-test customerSupportTargetTest
```

Pause a running test. Traffic stops splitting and all requests route to the control variant. Can be resumed.

```
agentcore pause ab-test customerSupportTargetTest
```

Stop a test permanently. All traffic reverts to the control variant. This cannot be undone.

```
agentcore stop ab-test customerSupportTargetTest
```

AWS SDK (boto3)
Start a test (set execution status to `RUNNING`):

```
import boto3
import uuid

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.update_ab_test(
    abTestId="customerSupportPromptTest-Ab1Cd2Ef3G",
    executionStatus="RUNNING",
    clientToken=str(uuid.uuid4()),
)
print(f"Execution status: {response['executionStatus']}")
```

Pause a running test:

```
response = client.update_ab_test(
    abTestId="customerSupportPromptTest-Ab1Cd2Ef3G",
    executionStatus="PAUSED",
    clientToken=str(uuid.uuid4()),
)
print(f"Execution status: {response['executionStatus']}")
```

Stop a running test permanently:

```
response = client.update_ab_test(
    abTestId="customerSupportPromptTest-Ab1Cd2Ef3G",
    executionStatus="STOPPED",
    clientToken=str(uuid.uuid4()),
)
print(f"Execution status: {response['executionStatus']}")
```

### Delete an A/B test

Delete an A/B test and its associated metadata. The test must be in `STOPPED` execution status before it can be deleted. Deleting a test does not affect the configuration bundles, AgentCore Gateway, or online evaluation configuration that the test referenced.

###### Example

AgentCore CLI

```
agentcore remove ab-test --name customerSupportTargetTest
```

AWS SDK (boto3)
Stop and then delete:

```
import boto3
import uuid

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

# First stop the test if it's running
client.update_ab_test(
    abTestId="customerSupportPromptTest-Ab1Cd2Ef3G",
    executionStatus="STOPPED",
    clientToken=str(uuid.uuid4()),
)

# Then delete
response = client.delete_ab_test(
    abTestId="customerSupportPromptTest-Ab1Cd2Ef3G"
)
print(f"Deleted: {response['abTestId']}")
```

## Execution status transitions

| From          | To        | Description                                                             |
| ------------- | --------- | ----------------------------------------------------------------------- |
| `NOT_STARTED` | `RUNNING` | Start the test. The AgentCore Gateway begins splitting traffic.         |
| `RUNNING`     | `PAUSED`  | Pause the test. Traffic stops splitting; all traffic routes to control. |
| `PAUSED`      | `RUNNING` | Resume a paused test.                                                   |
| `RUNNING`     | `STOPPED` | Stop the test permanently. Traffic routing ends immediately.            |
| `PAUSED`      | `STOPPED` | Stop a paused test permanently.                                         |
