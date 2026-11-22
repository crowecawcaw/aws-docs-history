

# Using the Optimization Agent

## Supported deployment modes
<a name="spark-optimization-deployment-modes"></a>

The Apache Spark Optimization Agent analyzes successful Spark workloads, including identifying idle capacity, data skew, and memory pressure, and recommending configuration, infrastructure, and data changes, for the following deployment modes:
+ EMR Serverless
+ AWS Glue

For the detailed features, capabilities, and limitations, see [Optimization features and capabilities](spark-optimization-features.md).

## Supported interfaces
<a name="spark-optimization-interfaces"></a>

### Optimizing EMR Serverless and AWS Glue applications with Kiro CLI
<a name="spark-optimization-kiro"></a>

Start Kiro CLI or your MCP client and verify the loaded tools for the optimization process.

```
sagemaker-unified-studio-mcp-troubleshooting (MCP)
 - analyze_spark_workload       not trusted
```

You are now ready to start the Spark optimization workflow.

You can start the optimization process with the following prompt:

```
Analyze EMR Serverless job run {{job-run-id}} in application {{application-id}} and recommend optimizations
```

For example prompts on each platform, see [Optimization prompt examples](spark-optimization-prompt-examples.md). To compare a run against a baseline or optimize for cost, see [Optimization features and capabilities](spark-optimization-features.md).

To use the agent with other MCP clients, such as Cline, Claude Code, or GitHub Copilot, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

## Optimize from the console
<a name="spark-optimization-console"></a>

You can start the optimization agent with the **Analyze with AI** button on the EMR Serverless and AWS Glue consoles.

### Analyze with AI button for the EMR Serverless console
<a name="spark-optimization-console-emr-serverless"></a>

Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home) and navigate to **EMR Studio**. Open your EMR Studio URL. Navigate to **Applications** and select the application to optimize. Open the **Batch job runs** tab. Select the checkbox next to the successful job run, and then choose **Analyze with AI** at the top. Alternatively, choose the **Success** status of the job run, and then choose **Analyze with AI** in the popover. For a successful job run, the **Analyze with AI** button starts the optimization agent.

In the **Analyze with AI** dialog, under **Optimize for**, choose **Performance** or **Cost**. **Performance** is the default, and optimizes for runtime. Then do one of the following:
+ To analyze the run on its own, choose **View recommendations**.
+ To compare the run with a baseline, choose an earlier, better-performing run of the same job under **Baseline job**, and then choose **Compare with baseline**.

The recommendations appear on the **AI analysis** tab of the job run.

The following screenshot shows the **Analyze with AI** button for a successful job run in EMR Studio.

![The Batch job runs tab of an EMR Serverless application in EMR Studio, with a successful job run selected and the Analyze with AI button at the top of the table.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/spark-optimize-emrs-analyze-with-ai.png)


### Analyze with AI button for the AWS Glue console
<a name="spark-optimization-console-glue"></a>

Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/). Under **ETL jobs**, choose the job. On the **Runs** tab, select the successful job run, and then choose **Analyze with AI** at the top. For a successful job run, the **Analyze with AI** button starts the optimization agent.

In the **Optimization Recommendations** dialog, under **Optimize for**, choose **Performance** or **Cost**. **Performance** is the default, and optimizes for runtime. Then do one of the following:
+ To analyze the run on its own, choose **View Recommendations**.
+ To compare the run with a baseline, choose an earlier, better-performing run of the same job under **Baseline job**, and then choose **Compare with baseline**.

The recommendations appear on the **AI analysis** tab of the job run.

The following screenshot shows the **Analyze with AI** button for a successful job run in the AWS Glue console.

![The Runs tab of an AWS Glue job, with a successful job run selected, the Analyze with AI button at the top of the table, and the optimization summary on the AI analysis tab.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/spark-optimize-glue-analyze-with-ai.png)
