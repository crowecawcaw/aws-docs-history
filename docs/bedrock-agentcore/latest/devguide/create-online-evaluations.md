# Create online evaluation

The `CreateOnlineEvaluationConfig` API creates a new online evaluation
configuration that continuously monitors your agent's performance using live traffic.
This asynchronous operation sets up the service to evaluate agent traces as they are
generated during normal operation.

When you create an online evaluation, you specify a unique configuration name, the
data source to monitor (either a list of CloudWatch log groups or an agent endpoint), and a
list of evaluators to apply (up to 10, combining built-in and custom evaluators). You
also provide an IAM service role ARN for execution. The `enableOnCreate`
parameter is required and determines whether the evaluation starts running immediately
upon creation (`executionStatus` = true) or remains disabled until explicitly
enabled (`executionStatus` = false).

###### Topics

- [Execution status control](#execution-status-control "#execution-status-control")
- [Evaluator protection](#evaluator-protection "#evaluator-protection")
- [Code samples for Starter
  Toolkit, AgentCore SDK, and AWS SDK](#create-online-evaluation-code-samples "#create-online-evaluation-code-samples")
- [Console](#create-online-evaluation-console "#create-online-evaluation-console")

## Execution status control

The `executionStatus` parameter determines whether the evaluation job
actively processes traces:

- **ENABLED** – The evaluation job runs
  continuously, processing incoming traces and generating evaluation
  results.
- **DISABLED** – The evaluation configuration
  exists but the job is paused. No traces are processed or evaluated.

## Evaluator protection

When you create an evaluation configuration with `executionStatus` set
to `ENABLED`, the system automatically locks any custom evaluators you've
selected. Once locked:

- **No modifications allowed** – You cannot
  update the evaluator's configuration, prompts, or settings. Clone a new
  evaluator if you need to make changes.
- **No deletion allowed** – You cannot delete
  the evaluator while any evaluation job is using it (running).

## Code samples for Starter

Toolkit, AgentCore SDK, and AWS SDK

The following code samples demonstrate how to create online evaluation
configurations using different development approaches. Choose the method that best
fits your development environment and preferences.

AgentCore CLI

```
# Create online evaluation configuration
# - Config names must use underscores, not hyphens
# - By default, auto-creates IAM execution role and enables the config
AGENT_ID="YOUR_AGENT_ID"
CONFIG_NAME="YOUR_CONFIG_NAME"
agentcore eval online create \
  --name $CONFIG_NAME \
  --agent-id $AGENT_ID \
  --sampling-rate 1.0 \
  --evaluator "Builtin.GoalSuccessRate" \
  --evaluator "Builtin.Helpfulness" \
  --description "Online Evaluation Config"
```

AgentCore SDK

```
from bedrock_agentcore_starter_toolkit import Evaluation

# Initialize the evaluation client
eval_client = Evaluation()

# Replace these with your actual values
config_name = "YOUR_CONFIG_NAME"
agent_id = "YOUR_AGENT_ID"  # e.g., agent_myagent-ABC123xyz

# Create online evaluation configuration
config = eval_client.create_online_config(
    config_name=config_name,                  # Must use underscores, not hyphens
    agent_id=agent_id,                        # Agent ID (e.g., agent_myagent-ABC123xyz)
    sampling_rate=1.0,                        # Percentage to evaluate (0-100). 1.0 = evaluate 1% of interactions
    evaluator_list=["Builtin.GoalSuccessRate", "Builtin.Helpfulness"],  # List of evaluator IDs
    config_description="Online Evaluation Config",  # Optional description
    auto_create_execution_role=True,          # Automatically creates IAM role (default: True)
    enable_on_create=True                     # Enable immediately after creation (default: True)
)

print("✅ Online evaluation configuration created!")
print(f"Config ID: {config['onlineEvaluationConfigId']}")
print(f"Status: {config['status']}")

# Save the config ID for later operations
config_id = config['onlineEvaluationConfigId']
print(f"\nSaved config_id: {config_id}")
```

AWS SDK

```
import boto3

# Your input log group that contains agent traces
LOG_GROUP_NAME = "/aws/agentcore/test-agent-traces"

# The service.name attribute from Otel
SERVICE_NAME = "strands_healthcare_single_agent.DEFAULT"

# The role created earlier with the required permissions for eval
role_arn = f"arn:aws:iam::{ACCOUNT_ID}:role/AgentCoreEvaluationRole"

client = boto3.client('bedrock-agentcore-control')

create_config_response = client.create_online_evaluation_config(
    onlineEvaluationConfigName="strands_healthcare_agent_1",
    description="Continuous evaluation of a healthcare agent",
    rule={
        "samplingConfig": {"samplingPercentage": 80.0}
    },
    dataSourceConfig={
        "cloudWatchLogs": {
            "logGroupNames": [LOG_GROUP_NAME],
            "serviceNames": [SERVICE_NAME]
        }
    },
    evaluators=[{"evaluatorId":"Builtin.Helpfulness"}],
    evaluationExecutionRoleArn=role_arn,
    enableOnCreate=True
)
```

AWS CLI

```
aws bedrock-agentcore-control create-online-evaluation-config \
    --online-evaluation-config-name "strands_healthcare_agent_1" \
    --description "Continuous evaluation of a healthcare agent" \
    --rule '{"samplingConfig": {"samplingPercentage": 80.0}}' \
    --data-source-config '{"cloudWatchLogs": {"logGroupNames": ["/aws/agentcore/test-agent-traces"], "serviceNames": ["strands_healthcare_single_agent.DEFAULT"]}}' \
    --evaluators '[{"evaluatorId": "Builtin.Helpfulness"}]' \
    --evaluation-execution-role-arn "arn:aws:iam::{YOUR_ACCOUNT_ID}:role/AgentCoreEvaluationRole" \
    --enable-on-create
```

## Console

You can create online evaluation configurations using the Amazon Bedrock AgentCore console's
visual interface. This method provides guided forms and validation to help you
configure your evaluation settings.

###### To create an AgentCore online evaluation

1. Open the Amazon Bedrock AgentCore console.
2. In the left navigation pane, choose
   **Evaluation**.
3. Choose **Create evaluation configuration**.
   1. (Optional) For **Evaluation name**, enter a name
      for the online evaluation configuration.
   2. (Optional) To enable the evaluation configuration after it's
      created, select the checkbox under the evaluation name.
   3. (Optional) For **Evaluation configuration
      description**, enter a description for the AgentCore
      evaluation configuration.
   4. (Optional) For **Session idle timeout**, enter a
      duration between 1 and 60 minutes. The default is 15 minutes.

4. For **Data source**, choose one of the following:
   1. **Define with an agent endpoint** – Choose an
      agent that you previously created on AgentCore Runtime, or create a
      new agent by choosing **Agents**. Then, choose an
      endpoint from the agent.
   2. **Select a CloudWatch log group** – Select up to
      5 log groups. Enter the service name used by your agent for
      observability. For agents hosted on AgentCore Runtime, service name
      follows the format
      <agent-runtime-name>.<agent-runtime-endpoint-name>. For
      agents running outside AgentCore Runtime, service name is configured
      in OTEL_RESOURCE_ATTRIBUTES environment variable.

5. For **Evaluators**, select up to 10 evaluators per
   evaluation configuration, including built-in and custom evaluators.
6. (Optional) For **Filters**, add up to 5 filters to
   identify which sessions to evaluate.
7. (Optional) For **Sampling**, choose a percentage between
   0.01% and 100% to control the percentage of sessions that are evaluated. The
   default is 10%.
8. For **Amazon Bedrock IAM role**, choose one of the
   following:
   1. **Use an existing role** – Select an IAM
      service role that already has the required permissions.
   2. **Create a new role** – Create a new IAM
      service role.

9. Choose **Create evaluation configuration** to create the
   AgentCore online evaluation configuration.
