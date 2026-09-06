

# Agent details - Evaluations
<a name="session-traces-evaluations"></a>

Evaluations provides continuous quality monitoring metrics for your AI agents. You can use the information provided by the dashboard to assess the performance, quality, and reliability of your AI agents. 

Instead of relying on simulated test cases, evaluations capture real user sessions and agent interactions, providing a comprehensive view of agent performance, from input to final output. With agent evaluations, you can define sampling rules to evaluate only a percentage of the sessions or traces, and then apply a variety of evaluators to asses and score an AI agent's operational performance. The resulting assessments and scores are displayed in the Evaluations dashboard, allowing you to monitor trends, identify potential quality issues, set alarms, and investigate and diagnose potential issues.

The Evaluations dashboard lists all of the evaluations that have been enabled and configured for the selected agent. For more information about configuring evaluations for an agent, see [ AgentCore evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html). You can expand each evaluation to view the sessions, traces, and spans that were evaluated. 

![Evaluations.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/evals_overview.png)


**Topics**
+ [Evaluations details](#session-traces-evaluations-details)
+ [Evaluations graphs](#session-traces-evaluations-graphs)
+ [Work with evaluation results](#session-traces-evaluations-raw-results)

## Evaluations details
<a name="session-traces-evaluations-details"></a>

For each evaluation, the dashboard includes the following sections:

------
#### [ Evaluation configuration metrics ]

Provides metrics for the overall evaluation configuration. An evaluator defines how to assess a specific aspect of an AI agent's performance. To view more details about an evaluator, choose its name in the **Evaluator** column. To view a bar chart and analyze trends for an evaluator, choose the value in the **Count** column.

![Evaluation configuration metrics.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/evals_01.png)


------
#### [ Session evaluations ]

Provides evaluation results for evaluators at the session level. A session represents a logical grouping of related interactions from a single user or workflow. A session can contain one or more traces. You can choose a session to filter down to the list of traces within that session in the **Trace evaluations** section.

![Session evaluations.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/evals_02.png)


------
#### [ Trace evaluations ]

Provides evaluation results for evaluators at the trace level. A trace is a complete record of a single agent execution or request. A trace can contain one or more spans. Choose a trace to view the trace details along with all the evaluators that were run on that trace.

![Trace evaluations.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/evals_03.png)


------
#### [ Span evaluations ]

Provides evaluation results for evaluators at the span level. A span represents the individual operations performed during that execution. Choose a span to view the span details along with all the operations performed during that span.

![Span evaluations.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/evals_04.png)


------

## Evaluations graphs
<a name="session-traces-evaluations-graphs"></a>

The Evaluations dashboard also includes a bar graph for each evaluator. The graphs show the trends for each evaluator over time, and enable you to set alarms for specific metric values. To set an alarm, click a bar in the graph, and then choose **Alarm** (bell) icon. For more information, see [Using Amazon CloudWatch alarms](CloudWatch_Alarms.md).

![Evaluations graphs.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/evals_graphs.png)


## Work with evaluation results
<a name="session-traces-evaluations-raw-results"></a>

If you need direct access to your evaluation results data, or if you want to create custom visualizations or work outside the AgentCore Evaluations console, you can access your evaluation results directly through CloudWatch Logs, CloudWatch Metrics, and CloudWatch dashboards.

**Topics**
+ [Accessing evaluation results in CloudWatch Logs](#accessing-evaluation-results-logs)
+ [Accessing evaluation metrics in CloudWatch Metrics](#accessing-evaluation-metrics)
+ [Creating Custom Dashboards](#creating-custom-dashboards)
+ [Setting alarms on evaluation metrics](#setting-alarms-evaluation-metrics)
+ [Additional Resources](#additional-resources)

### Accessing evaluation results in CloudWatch Logs
<a name="accessing-evaluation-results-logs"></a>

Your evaluation results are automatically published to CloudWatch Logs in Embedded Metric Format (EMF).

**To find your evaluation results log group**

1. Open the CloudWatch console.

1. In the navigation pane, choose **Logs Management** > **Log groups**.

1. Search for or navigate to the log groups with prefix: `/aws/bedrock-agentcore/evaluations/`.

1. Within this log group, the log events contain the evaluation results.

For more information about working with log groups and querying log data, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) and [Analyzing Log Data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

### Accessing evaluation metrics in CloudWatch Metrics
<a name="accessing-evaluation-metrics"></a>

Evaluation results metrics are automatically extracted from the Embedded Metric Format (EMF) logs and published to CloudWatch Metrics.

**To find your evaluation metrics**

1. Open the CloudWatch console.

1. In the navigation pane, choose **Metrics** > **Classic metrics**.

1. Select the **Bedrock AgentCore/Evaluations** namespace.

1. Browse available metrics by dimensions.

For more information about viewing and working with metrics, see [ Using CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [Graphing Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph_metrics.html).

### Creating Custom Dashboards
<a name="creating-custom-dashboards"></a>

You can create custom dashboards to visualize your evaluation metrics alongside other operational metrics.

**To create a dashboard with evaluation metrics**

1. In the CloudWatch console, choose **Dashboards** from the navigation pane.

1. Choose **Create dashboard**.

1. Add widgets and select metrics from the **Bedrock AgentCore/Evaluations** namespace.

1. Customize the time range, statistic, and visualization type for your needs.

For detailed instructions, see [ Creating and Working with Custom Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) and [ Using CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

### Setting alarms on evaluation metrics
<a name="setting-alarms-evaluation-metrics"></a>

You can set alarms to notify you when evaluation metrics cross specified thresholds that you have specified, such as when correctness drops below acceptable levels.

**To create an alarm on evaluation metrics**

1. In the CloudWatch console, choose **Alarms** > **All alarms**.

1. Choose **Create alarm**.

1. Choose **Select metric** and navigate to the **Bedrock AgentCore/Evaluations** namespace.

1. Select the metric you want to monitor.

1. Configure the threshold conditions (dynamic anomaly detection threshold available where you don't need to specified a static number threshold) and notification actions.

For detailed instructions, see [Using CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) and [Creating a CloudWatch Alarm Based on a Static Threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html).

### Additional Resources
<a name="additional-resources"></a>
+ [CloudWatch Embedded Metric Format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.html)
+ [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)
+ [Creating Composite Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html)