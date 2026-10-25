

# Recurring insights report
<a name="insights-recurring-report"></a>

**Insights job creation ends October 16, 2026**  
Beginning October 16, 2026, Amazon Bedrock AgentCore insights no longer supports creating new batch or recurring insights. Existing recurring insight jobs continue to process sessions and generate reports through October 30, 2026. Beginning October 31, existing recurring insights will also stop generating reports. Historical batch results and recurring insights reports remain available.  
This change is part of a redesign of Insights. A new Insights experience will be available soon.

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
agentcore add online-insight \
  --name my_agent_insights \
  --agent MyAgent \
  --insight Builtin.Insight.FailureAnalysis \
  --sampling-rate 100 \
  --clustering-frequency DAILY \
  --enable-on-create true \
  --json
```
Run this from inside an AgentCore project, and replace `MyAgent` with the name of a Runtime in that project. Then deploy the project:  

```
agentcore deploy --json
```

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
+ Sample sessions at the configured rate. This example uses 100%. To analyze a subset of traffic, lower `--sampling-rate` or `samplingPercentage`.
+ Run failure analysis and user intent extraction on each sampled session.
+ Trigger a clustering report daily.

## Configuration parameters
<a name="insights-recurring-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `insights`  | List | Required (mutually exclusive with `evaluators`) | List of insight types to run. Each entry has an `insightId`. Maximum 10. | 
|  `rule.samplingConfig.samplingPercentage`  | Number | Yes | Percentage of sessions to analyze (0.01-100). Use a lower sampling rate for high-traffic agents to control costs while still surfacing failure patterns. | 
|  `clusteringConfig`  | Object | No | Configures periodic batch evaluation jobs for clustering. Contains a `frequencies` list. Can only be used when `insights` is provided. | 
|  `clusteringConfig.frequencies`  | List of strings | Yes (within `clusteringConfig`) | One or more of: `DAILY`, `WEEKLY`, `MONTHLY`. Maximum 3 values. | 

**Note**  
Insights and evaluators are mutually exclusive. Provide one or the other, not both. If you want both quality scoring and failure triage for the same agent, create two separate configurations pointing at the same data source.

## Update a configuration
<a name="insights-recurring-update"></a>

Modify the insights or clustering frequency:

**Example**  
For a config that you added with `agentcore add online-insight`, change `insights` or `clusteringConfig` in the `onlineEvalConfigs` array in `agentcore/agentcore.json`, then run `agentcore deploy`.  
For a config that is not part of a project, update it by ID. Run `agentcore eval online-insight list` to find the ID. `--insight` replaces the list of insights, and `--clustering-frequency` replaces the set of frequencies:  

```
agentcore eval online-insight update \
  --id <ONLINE_INSIGHT_ID> \
  --insight Builtin.Insight.FailureAnalysis Builtin.Insight.UserIntent \
  --clustering-frequency DAILY WEEKLY
```

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

Recurring reports produce batch evaluation jobs automatically.

**Example**  
List the batch insights runs, then get the results of one run by its ID:  

```
agentcore eval batch-insights list --json
agentcore eval batch-insights get --id <BATCH_INSIGHTS_ID> --json
```
Use `ListBatchEvaluations` to find completed reports, then `GetBatchEvaluation` to retrieve results:  

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
For a config that you added with `agentcore add online-insight`, set its `enableOnCreate` to `false` in `agentcore/agentcore.json` and run `agentcore deploy` to pause it. Set `enableOnCreate` to `true` and deploy to resume it. To delete it, remove it from the project, then deploy:  

```
agentcore remove online-insight --name my_agent_insights
agentcore deploy
```
For a config that is not part of a project, use its ID. Run `agentcore eval online-insight list` to find it.  
Pause:  

```
agentcore eval online-insight pause --id <ONLINE_INSIGHT_ID> --json
```
Resume:  

```
agentcore eval online-insight resume --id <ONLINE_INSIGHT_ID> --json
```
Delete:  

```
agentcore eval online-insight delete --id <ONLINE_INSIGHT_ID> --json
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