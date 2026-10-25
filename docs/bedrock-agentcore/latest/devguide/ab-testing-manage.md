

# Manage an A/B test
<a name="ab-testing-manage"></a>

Update an A/B test to start it, pause it, or stop it. You use the `UpdateABTest` operation to change execution status.

**Note**  
The AgentCore CLI lifecycle commands identify a test by its A/B test ID. Get the ID from the `run` command response or list tests with `agentcore eval ab-test list`.

## Code samples
<a name="manage-ab-test-examples"></a>

### View, pause, resume, and stop
<a name="manage-ab-test-start-stop"></a>

**Example**  
List all A/B test jobs, or view one in detail, including its variants, execution status, and results:  

```
agentcore eval ab-test list
agentcore eval ab-test get --id <ab-test-id>
```
Start a test that you created with `--enable-on-create false`, or resume a paused test:  

```
agentcore eval ab-test resume --id <ab-test-id>
```
Pause a running test. Traffic stops splitting and all requests route to the control variant. Can be resumed.  

```
agentcore eval ab-test pause --id <ab-test-id>
```
Stop a test permanently. All traffic reverts to the control variant. This cannot be undone.  

```
agentcore eval ab-test stop --id <ab-test-id>
```
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

### Route traffic to the winning variant
<a name="manage-ab-test-promote"></a>

When the results are statistically significant, stop the test. For a target-based test, no routing change is required if the control won. If the treatment won, create or update a Gateway rule that routes traffic to the treatment target. For a configuration-bundle test, create or update a Gateway rule for the winning bundle version even if the control won, because the agent’s default configuration can differ from the control bundle.

**Example**  
The `ab-test stop` command uses the AgentCore CLI, and the rule commands use the AWS CLI.  
For a target-based A/B test:  

```
agentcore eval ab-test stop --id <ab-test-id>

aws bedrock-agentcore-control create-gateway-rule \
  --gateway-identifier <gateway-id> \
  --priority 100 \
  --conditions '[{"matchPaths":{"anyOf":["/<control-target>/*"]}}]' \
  --actions '[{"routeToTarget":{"staticRoute":{"targetName":"<treatment-target>"}}}]'
```
For a configuration-bundle A/B test:  

```
agentcore eval ab-test stop --id <ab-test-id>

aws bedrock-agentcore-control create-gateway-rule \
  --gateway-identifier <gateway-id> \
  --priority 100 \
  --conditions '[{"matchPaths":{"anyOf":["/<target-name>/*"]}}]' \
  --actions '[{"configurationBundle":{"staticOverride":{"bundleArn":"<winning-bundle-arn>","bundleVersion":"<winning-bundle-version-id>"}}}]'
```
The rule commands update the live Gateway immediately. The rule is not part of the project, and `agentcore deploy` does not manage it. To change an existing production rule instead, use `aws bedrock-agentcore-control update-gateway-rule --gateway-identifier <gateway-id> --rule-id <rule-id>`.  
Save the rule ID returned by the create command. To find the rule ID later, run `agentcore gateway rule list --gateway-id <gateway-id>`. If the rule is later replaced or no longer needed, remove it:  

```
aws bedrock-agentcore-control delete-gateway-rule \
  --gateway-identifier <gateway-id> \
  --rule-id <rule-id>
```
To route traffic to the winning variant, stop the test, then call `create_gateway_rule` or `update_gateway_rule` on the `bedrock-agentcore-control` client. For examples, see [Gateway rules API examples](gateway-rules-examples.md).

### Delete an A/B test
<a name="manage-ab-test-remove"></a>

Delete an A/B test and its associated metadata. The test must be in `STOPPED` execution status before it can be deleted. Deleting a test does not affect the configuration bundles, AgentCore Gateway, or online evaluation configuration that the test referenced. It also does not delete the `AgentCoreABTest-<test-name>-<hash>` execution role that the AgentCore CLI creates when you omit `--role-arn`. Delete that role in IAM when you no longer need it.

**Example**  

```
agentcore eval ab-test delete --id <ab-test-id>
```
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
<a name="manage-ab-test-execution-states"></a>


| From | To | Description | 
| --- | --- | --- | 
|  `NOT_STARTED`  |  `RUNNING`  | Start the test. The AgentCore Gateway begins splitting traffic. | 
|  `RUNNING`  |  `PAUSED`  | Pause the test. Traffic stops splitting; all traffic routes to control. | 
|  `PAUSED`  |  `RUNNING`  | Resume a paused test. | 
|  `RUNNING`  |  `STOPPED`  | Stop the test permanently. Traffic routing ends immediately. | 
|  `PAUSED`  |  `STOPPED`  | Stop a paused test permanently. | 