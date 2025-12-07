# Update online evaluation

The `UpdateOnlineEvaluationConfig` API modifies an existing online
evaluation configuration, allowing you to change evaluators, data sources, execution
settings, and other parameters. This operation intelligently handles updates with no
disruption to running evaluations.

Updates can only be made when your evaluation configuration is in Active or
UpdateFailed status. If the configuration is currently being created, updated, or
deleted, you'll receive a conflict error and should retry after the operation
completes.

## Execution control

The execution status parameter controls whether your online evaluation
configuration actively processes agent traces. Understanding these states helps you
manage evaluation costs and performance.

- **Enabling evaluation** – When changing from
  DISABLED to ENABLED, the system provisions the service to begin processing
  traces from your specified data sources.
- **Disabling evaluation** – When changing from
  ENABLED to DISABLED, the system stops processing new traces while preserving
  your configuration for future use.

## Code samples for Starter

Toolkit, AgentCore SDK, and AWS SDK

The following code samples demonstrate how to update online evaluation
configurations using different development approaches. Choose the method that best
fits your development environment and preferences.

AgentCore CLI

```
# Update description
agentcore eval online update --config-id "config-abc123" \
  --description "Updated description for online evaluation"
```

AgentCore SDK

```
from bedrock_agentcore_starter_toolkit import Evaluation

# Initialize the evaluation client
eval_client = Evaluation()
config_id = "config-abc123"
print(f"\nUsing config_id: {config_id}")

# update description
eval_client.update_online_config(
    config_id=config_id,
    description="Updated description for online evaluation"
)
print("✅ Description updated")
```

AWS SDK

```
import boto3

client = boto3.client('bedrock-agentcore-control')

update_config_response = client.update_online_evaluation_config(
    onlineEvaluationConfigId='your_config_id',
    description="Updated description for online evaluation"
)
```

AWS CLI

```
aws bedrock-agentcore-control update-online-evaluation-config \
    --online-evaluation-config-id your_config_id \
    --description "Updated description for online evaluation"
```

## Console

Modify your online evaluation configuration settings using the console's editing
interface, which provides form validation and guided configuration options.

###### To update an online evaluation configuration

1. Open the Amazon Bedrock AgentCore console.
2. In the navigation pane, choose **Evaluation**.
3. In the **Evaluation configurations** card, view the table
   that lists the evaluation configurations you have created.
4. Choose one of the following methods to update the configuration:
   - Choose the evaluation configuration name to view its details, then
     choose **Edit** in the upper right of the details
     page.
   - Select the evaluation configuration so that it is highlighted,
     then choose **Edit** at the top of the
     **Evaluation configurations** card.

5. Update the fields as needed.
6. Choose **Update evaluation configuration** to save the
   changes.
