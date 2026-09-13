

# Results and output
<a name="results-and-output"></a>

Online evaluation results are automatically saved to Amazon CloudWatch. By default, the service writes them as JSON log entries to a dedicated CloudWatch log group.

**Topics**
+ [Log group structure](#log-group-structure)
+ [Choose where results are written](#result-destination)
+ [Publish metrics to a custom namespace](#custom-metrics-namespace)
+ [Result format](#result-format)
+ [Viewing results in CloudWatch Observability Console](#viewing-results-console)
+ [Viewing evaluation scores in CloudWatch Metrics](#viewing-scores-metrics)

## Log group structure
<a name="log-group-structure"></a>

If you use the default dedicated destination, the service writes evaluation results to `/aws/bedrock-agentcore/evaluations/results/<online-evaluation-config-id>` . You can see the resolved result log group for a configuration on that evaluation’s **details page** in the Amazon Bedrock AgentCore console.

Each evaluation generates a separate log entry within this log group. Additionally, evaluation scores are emitted as CloudWatch metrics for monitoring and analysis.

## Choose where results are written
<a name="result-destination"></a>

Use `resultDestination` in `outputConfig.cloudWatchConfig` to choose where online evaluation results are written. If you don’t set it, the service uses a dedicated log group:
+  `DEDICATED_LOG_GROUP` (default) – Writes results to a dedicated result log group. If you don’t set `logGroupName`, the service uses `/aws/bedrock-agentcore/evaluations/results/<online-evaluation-config-id>`. To use a different dedicated log group, set `logGroupName` (see [Use a custom output log group](#custom-output-log-group)).
+  `SOURCE_LOG_GROUP` – Writes results back to the same log group that supplied the agent traces, so evaluations appear alongside the traces they scored. Don’t set `logGroupName` when you use this value.

### Use a custom output log group
<a name="custom-output-log-group"></a>

When `resultDestination` is `DEDICATED_LOG_GROUP`, you can set `logGroupName` to send results to a log group that you choose. If the log group already exists, the service uses it as-is. If it doesn’t exist, the service creates it, so the evaluation execution role must allow `logs:CreateLogGroup` for that log group. The name can’t use the reserved `/aws/bedrock-agentcore/evaluations/` prefix, except for this configuration’s own service-managed default group.

```
# Write results back to the trace source log group
outputConfig={"cloudWatchConfig": {"resultDestination": "SOURCE_LOG_GROUP"}}

# Write results to a custom dedicated log group
outputConfig={"cloudWatchConfig": {"resultDestination": "DEDICATED_LOG_GROUP", "logGroupName": "/my/team/evaluation-results"}}
```

## Publish metrics to a custom namespace
<a name="custom-metrics-namespace"></a>

Evaluation scores are also published as CloudWatch metrics. By default, the service uses the `Bedrock-AgentCore/Evaluations` namespace. To publish metrics under your own namespace, for example to separate results by team or tenant, set `metricsNamespace` in `outputConfig.cloudWatchConfig`. The value can’t begin with `AWS/`.

```
outputConfig={"cloudWatchConfig": {"metricsNamespace": "MyTeam/Evaluations"}}
```

## Result format
<a name="result-format"></a>

Evaluation results follow OpenTelemetry semantic conventions for GenAI evaluation result events. When possible, each event is parented to the original span ID and includes the original trace ID and session ID.

You can use CloudWatch Logs Insights to query and analyze your evaluation results, and CloudWatch Metrics to monitor evaluation trends over time.

## Viewing results in CloudWatch Observability Console
<a name="viewing-results-console"></a>

You can view and analyze your evaluation results using the CloudWatch Observability Console. The console provides visualizations, metrics, and detailed logs of your agent evaluations.

 **To view evaluation results** 

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/) 

1. In the navigation pane, choose **GenAI Observability** > **Bedrock AgentCore** 

1. Under the **Agents** section, select the agent and endpoint associated with your evaluation configuration

1. Navigate to the **Evaluations** tab for detailed results

For more details, see [AWS CloudWatch session trace evaluations documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/session-traces-evaluations.html).

## Viewing evaluation scores in CloudWatch Metrics
<a name="viewing-scores-metrics"></a>

Evaluation scores are published as CloudWatch metrics. By default, they appear in the `Bedrock-AgentCore/Evaluations` namespace. If you set `metricsNamespace`, look for that custom namespace instead when you browse metrics in CloudWatch.

 **To view evaluation scores** 

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/) 

1. In the navigation pane, choose **Metrics** > **All Metrics** 

1. In the **Browse** tab, select **Bedrock-AgentCore/Evaluations** or the custom namespace that you configured in `outputConfig.cloudWatchConfig.metricsNamespace` 

1. Select dimension combinations to optionally narrow down results by evaluator type or evaluation label

For more details, see [AWS CloudWatch session trace evaluations documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/session-traces-evaluations.html).