

# Get started with Insights

This walkthrough creates an online evaluation that uses `Builtin.FailureAnalysis`, then reads the resulting Insights through the Agent Insights APIs. For an overview of the online workflow, see [Insights in online evaluation](online-evaluations-insights.md).

The setup steps take about 15 minutes. The time required to generate an Agent Insight depends on incoming traffic and the available failure evidence.

## Prerequisites
<a name="insights-getting-started-prerequisites"></a>

Before you begin, identify the following resources:
+ The CloudWatch log group that contains your agent traces.
+ The OpenTelemetry `service.name` value for your agent. You configure this value in `serviceNames` and use it as `applicationName` in the Agent Insights APIs.
+ An evaluation execution role that meets the [Evaluations prerequisites](evaluations-prerequisites.md).

## Use the AWS CLI
<a name="insights-getting-started-cli"></a>

In the following commands, replace the example Region, log group, service name, and role ARN with values for your environment. The Store ID is always `default-insight-store`.

### Step 1: Enable the default Agent Insight Store
<a name="_step_1_enable_the_default_agent_insight_store"></a>

The Store starts disabled. List it before you create the evaluation:

```bash
aws bedrock-agentcore-control list-agent-insight-stores \
    --region us-west-2
```

The response contains one Store. Its ID is `default-insight-store`. Enable it:

```bash
aws bedrock-agentcore-control update-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --enablement-status ENABLED \
    --region us-west-2
```

Use `GetAgentInsightStore` to poll the asynchronous update:

```bash
aws bedrock-agentcore-control get-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --region us-west-2
```

Continue after `enablementStatus` is `ENABLED` and `status` is `ACTIVE`.

### Step 2: Create an online evaluation
<a name="_step_2_create_an_online_evaluation"></a>

Create an online evaluation configuration that uses the failure analysis evaluator:

```bash
aws bedrock-agentcore-control create-online-evaluation-config \
    --online-evaluation-config-name "production_failure_analysis" \
    --description "Find recurring failures in production traffic" \
    --rule '{"samplingConfig":{"samplingPercentage":100.0}}' \
    --data-source-config '{
        "cloudWatchLogs": {
            "logGroupNames": [
                "/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"
            ],
            "serviceNames": ["MyAgent.DEFAULT"]
        }
    }' \
    --evaluators '[{"evaluatorId":"Builtin.FailureAnalysis"}]' \
    --evaluation-execution-role-arn \
        "arn:aws:iam::111122223333:role/AgentCoreEvaluationRole" \
    --enable-on-create \
    --region us-west-2
```

Save the `onlineEvaluationConfigId` from the response. You use it to delete the configuration when you finish the walkthrough. For the deletion command, see [Step 6: Clean up](#insights-getting-started-cleanup).

### Step 3: Generate failure evidence
<a name="_step_3_generate_failure_evidence"></a>

Send normal traffic to your agent. We write a session result for each selected session. After we have enough related failure evidence to create a pattern, we write an Agent Insight to the default Store. We aggregate the insight at the agent level identified by `serviceName`, not by the online evaluation configuration ID.

### Step 4: List active Agent Insights
<a name="_step_4_list_active_agent_insights"></a>

Use the following AWS CLI command to list active Agent Insights for your application:

```bash
aws bedrock-agentcore list-agent-insights \
    --application-name "MyAgent.DEFAULT" \
    --archive-status ACTIVE \
    --region us-west-2
```

A successful response contains an `agentInsights` list. If the list is empty, the evaluation might not have processed enough related failure evidence.

### Step 5: Get Agent Insight details
<a name="_step_5_get_agent_insight_details"></a>

Use the following AWS CLI command to get one Agent Insight. Replace `<agent-insight-id>` with an ID returned by `ListAgentInsights`:

```bash
aws bedrock-agentcore get-agent-insight \
    --application-name "MyAgent.DEFAULT" \
    --agent-insight-id <agent-insight-id> \
    --region us-west-2
```

The response includes the generated pattern description, root causes, suggested fixes, affected-session count, and sample sessions. Use the sample session identifiers to inspect the corresponding traces.

### Step 6: Clean up
<a name="insights-getting-started-cleanup"></a>

If you don’t want the online evaluation to keep processing traffic, delete the configuration. Replace `online-evaluation-config-id` with the configuration ID returned in Step 2:

```bash
aws bedrock-agentcore-control delete-online-evaluation-config \
    --online-evaluation-config-id <online-evaluation-config-id> \
    --region us-west-2
```

Delete the online evaluation configuration to stop future processing. Existing Agent Insights remain in the Store. To remove them, disable the default Store:

**Warning**  
Disabling the Store permanently removes all Agent Insights in the current account and Region. This includes findings from other online and batch evaluations. Before you disable the Store, retrieve any Agent Insights that you need to retain.

```bash
aws bedrock-agentcore-control update-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --enablement-status DISABLED \
    --region us-west-2
```

Poll `GetAgentInsightStore` until the Store reaches `INACTIVE`.

## Use the AWS SDK for Python
<a name="insights-getting-started-sdk"></a>

The following Python example performs the same Store enablement, evaluation creation, and Agent Insight retrieval:

```python
import boto3
import time

REGION = "us-west-2"
APPLICATION_NAME = "MyAgent.DEFAULT"
STORE_ID = "default-insight-store"

control = boto3.client(
    "bedrock-agentcore-control",
    region_name=REGION,
)
data = boto3.client(
    "bedrock-agentcore",
    region_name=REGION,
)

store = control.get_agent_insight_store(agentInsightStoreId=STORE_ID)
if store["enablementStatus"] == "DISABLED":
    control.update_agent_insight_store(
        agentInsightStoreId=STORE_ID,
        enablementStatus="ENABLED",
    )

while store["status"] != "ACTIVE" or store["enablementStatus"] != "ENABLED":
    if store["status"] == "ERROR":
        reason = store.get("failureReason", "unknown")
        raise RuntimeError(f"Agent Insight Store update failed: {reason}")
    time.sleep(5)
    store = control.get_agent_insight_store(agentInsightStoreId=STORE_ID)

created = control.create_online_evaluation_config(
    onlineEvaluationConfigName="production_failure_analysis",
    description="Find recurring failures in production traffic",
    rule={"samplingConfig": {"samplingPercentage": 100.0}},
    dataSourceConfig={
        "cloudWatchLogs": {
            "logGroupNames": [
                "/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"
            ],
            "serviceNames": [APPLICATION_NAME],
        }
    },
    evaluators=[{"evaluatorId": "Builtin.FailureAnalysis"}],
    evaluationExecutionRoleArn=(
        "arn:aws:iam::111122223333:role/AgentCoreEvaluationRole"
    ),
    enableOnCreate=True,
)
print("Online evaluation:", created["onlineEvaluationConfigId"])

# Run this after the evaluation has processed failing sessions.
listed = data.list_agent_insights(
    applicationName=APPLICATION_NAME,
    archiveStatus="ACTIVE",
)

for summary in listed["agentInsights"]:
    detail = data.get_agent_insight(
        applicationName=APPLICATION_NAME,
        agentInsightId=summary["agentInsightId"],
    )
    print(detail["name"])
    print(detail["description"])
    for cause in detail.get("rootCauses", []):
        print("Root cause:", cause["name"])
        print("Suggested fix:", cause.get("suggestedFix"))
```

Delete the online evaluation configuration when you no longer need it. For instructions, see [Step 6: Clean up](#insights-getting-started-cleanup).

## Next steps
<a name="insights-getting-started-next"></a>

You now have an online evaluation that can turn related failures into Agent Insights. You can:
+  [List, read, archive, or restore Agent Insights](insights-manage.md).
+  [Manage the Agent Insight Store](insights-store.md).
+  [Configure data protection](insights-security.md).
+ Generate point-in-time failure insights from an existing set of sessions with [Insights in batch evaluation](batch-evaluations-insights.md).