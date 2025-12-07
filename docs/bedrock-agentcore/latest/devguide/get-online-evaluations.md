# Get online evaluation

The `GetOnlineEvaluationConfig` API retrieves the complete details and
current status of an existing online evaluation configuration. This synchronous
operation returns the full configuration including data sources, evaluators, execution
status, and operational metadata.

Use this API to monitor the configuration's lifecycle status (Creating, Active,
Updating, or Deleting), check current execution status (ENABLED or DISABLED), and
retrieve all configuration parameters including evaluator lists, data source settings,
and output destinations.

## Code samples for Starter

Toolkit, AgentCore SDK, and AWS SDK

The following code samples demonstrate how to get online evaluation configuration
details using different development approaches. Choose the method that best fits
your development environment and preferences.

AgentCore CLI

```
agentcore eval online get --config-id "config-abc123"
```

AgentCore SDK

```
from bedrock_agentcore_starter_toolkit import Evaluation

# Initialize the evaluation client
eval_client = Evaluation()

config_id = "config-abc123"
print(f"\nUsing config_id: {config_id}")

config_details = eval_client.get_online_config(config_id)
# Display configuration details
print(f"Config Name: {config_details['onlineEvaluationConfigName']}")
print(f"Config ID: {config_details['onlineEvaluationConfigId']}")
print(f"Status: {config_details['status']}")
```

AWS SDK

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.get_online_evaluation_config(
    onlineEvaluationConfigId='your_config_id'
)
```

AWS CLI

```
aws bedrock-agentcore-control get-online-evaluation-config \
    --online-evaluation-config-id your_config_id
```

## Console

You can view detailed information about a specific online evaluation configuration
through the console interface.

###### To get online evaluation configuration details

1. Open the Amazon Bedrock AgentCore console.
2. In the navigation pane, choose **Evaluation**.
3. In the **Evaluation configurations** card, view the table
   that lists the evaluation configurations you have created.
4. To view information for a specific evaluation configuration, choose the
   configuration name to view its details.
