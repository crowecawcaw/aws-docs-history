

# Recurring insights report
<a name="insights-recurring-report"></a>

Create an online evaluation configuration with insights and a clustering schedule. The service automatically runs insights analysis on the configured cadence without manual intervention.

**Topics**
+ [Create the configuration](#insights-recurring-create)
+ [Configuration parameters](#insights-recurring-params)
+ [Update a configuration](#insights-recurring-update)
+ [View recurring report results](#insights-recurring-view)
+ [Manage the configuration](#insights-recurring-manage)

## Create the configuration
<a name="insights-recurring-create"></a>

**Example**  

```
agentcore add online-insights --name my_agent_insights --runtime MyAgent --insights Builtin.Insight.FailureAnalysis --sampling-rate 100 --clustering-frequency DAILY --enable-on-create --json
```
Then deploy via CloudFormation:  

```
agentcore deploy -y --json
```

1. Run `agentcore` to open the TUI, then select **add** and choose **Online Insights**:  
![Insights wizard: select agent to monitor](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/insights-add-agent.png)

1. Select the insights to enable:  
![Insights wizard: select insights](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/insights-add-insights.png)

1. Set the sampling rate:  
![Insights wizard: set sampling rate](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/insights-add-sampling-rate.png)

1. Choose clustering frequencies:  
![Insights wizard: select clustering frequency](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/insights-add-clustering.png)

1. Enter a config name:  
![Insights wizard: enter config name](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/insights-add-name.png)

1. Review the configuration and press Enter to confirm:  
![Insights wizard: review configuration](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/insights-add-confirm.png)

```
import boto3

client_cp = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

response = client_cp.create_online_evaluation_config(
    onlineEvaluationConfigName="my_agent_insights",
    rule={
        "samplingConfig": {"samplingPercentage": 100.0},
        "sessionConfig": {"sessionTimeoutMinutes": 30},
    },
    dataSourceConfig={
        "cloudWatchLogs": {
            "serviceNames": ["MyAgent.DEFAULT"],
            "logGroupNames": [
                "/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"
            ],
        }
    },
    insights=[
        {"insightId": "Builtin.Insight.FailureAnalysis"},
        {"insightId": "Builtin.Insight.UserIntent"},
    ],
    clusteringConfig={"frequencies": ["DAILY"]},
    evaluationExecutionRoleArn="arn:aws:iam::123456789012:role/AgentCoreEvaluationRole",
    enableOnCreate=True,
)

config_id = response["onlineEvaluationConfigId"]
print(f"Created config: {config_id}")
```

This tells the service to:
+ Sample sessions at the configured rate (100% in this example — adjust `--sampling-rate` or `samplingPercentage` to analyze a subset of traffic).
+ Run failure analysis and user intent extraction on each sampled session.
+ Trigger a clustering report daily.

## Configuration parameters
<a name="insights-recurring-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `insights`  | List | Required (mutually exclusive with `evaluators`) | List of insight types to run. Each entry has an `insightId`. Maximum 10. | 
|  `rule.samplingConfig.samplingPercentage`  | Number | No (default: 100) | Percentage of sessions to analyze (1—​100). Use a lower sampling rate for high-traffic agents to control costs while still surfacing failure patterns. | 
|  `clusteringConfig`  | Object | No | Configures periodic batch evaluation jobs for clustering. Contains a `frequencies` list. Can only be used when `insights` is provided. | 
|  `clusteringConfig.frequencies`  | List of strings | Yes (within `clusteringConfig`) | One or more of: `DAILY`, `WEEKLY`, `MONTHLY`. Maximum 3 values. | 

**Note**  
Insights and evaluators are mutually exclusive — you must provide one or the other, not both. If you want both quality scoring and failure triage for the same agent, create two separate configurations pointing at the same data source.

## Update a configuration
<a name="insights-recurring-update"></a>

Modify the insights or clustering frequency:

```
client_cp.update_online_evaluation_config(
    onlineEvaluationConfigId=config_id,
    insights=[
        {"insightId": "Builtin.Insight.FailureAnalysis"},
        {"insightId": "Builtin.Insight.UserIntent"},
    ],
    clusteringConfig={"frequencies": ["DAILY", "WEEKLY"]},
)
```

## View recurring report results
<a name="insights-recurring-view"></a>

Recurring reports produce batch evaluation jobs automatically. Use `ListBatchEvaluations` to find completed reports, then `GetBatchEvaluation` to retrieve results:

```
client = boto3.client("bedrock-agentcore", region_name="us-west-2")

# List recent batch evaluations
evaluations = client.list_batch_evaluations()

for eval_summary in evaluations.get("batchEvaluations", []):
    if eval_summary["status"] == "COMPLETED" and eval_summary.get("insights"):
        result = client.get_batch_evaluation(
            batchEvaluationId=eval_summary["batchEvaluationId"]
        )
        print(f"Report: {eval_summary['batchEvaluationName']}")
        if "failureAnalysisResult" in result:
            failures = result["failureAnalysisResult"]["failures"]
            print(f"  Found {len(failures)} failure categories")
```

## Manage the configuration
<a name="insights-recurring-manage"></a>

**Example**  
Pause:  

```
agentcore pause online-insights my_agent_insights --json
```
Resume:  

```
agentcore resume online-insights my_agent_insights --json
```
Remove:  

```
agentcore remove online-insights --name my_agent_insights --yes --json
```
Pause or resume:  

```
# Pause
client_cp.update_online_evaluation_config(
    onlineEvaluationConfigId=config_id,
    executionStatus="DISABLED",
)

# Resume
client_cp.update_online_evaluation_config(
    onlineEvaluationConfigId=config_id,
    executionStatus="ENABLED",
)
```
Delete:  

```
client_cp.delete_online_evaluation_config(
    onlineEvaluationConfigId=config_id,
)
```

**Warning**  
Deleting a configuration does not delete past batch evaluation results. Historical insight results remain accessible through `GetBatchEvaluation`.