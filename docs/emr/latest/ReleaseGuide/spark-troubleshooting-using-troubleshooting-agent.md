

# Using the Troubleshooting Agent

## Supported deployment modes
<a name="supported-deployment-modes"></a>

The Apache Spark Troubleshooting Agent for Amazon EMR supports comprehensive analysis of failed Spark workloads, including automated error diagnosis, root cause analysis, code recommendations, and actionable suggestions to fix the failure, for the following Spark deployment modes:
+ EMR on EC2
+ EMR Serverless
+ EMR on EKS
+ AWS Glue

For the detailed features, capabilities, and limitations, see [Troubleshooting features and capabilities](spark-troubleshooting-features.md).

## Supported interfaces
<a name="supported-interfaces"></a>

### Troubleshooting cells within Amazon SageMaker notebooks
<a name="troubleshooting-sagemaker-notebooks"></a>

A demonstration of the troubleshooting experience with Amazon SageMaker notebooks. For any notebook cell failure, you can ask the Amazon SageMaker Notebook Agent to troubleshoot the failure and request the analysis, followed by a possible code fix if the error resulted from code, by choosing the **Fix with AI** button.

[![AWS Videos](https://img.youtube.com/vi/btW8hwio0tE/0.jpg)](https://www.youtube.com/watch?v=btW8hwio0tE)


### Troubleshooting AWS Glue and EMR Spark applications with Kiro CLI
<a name="troubleshooting-glue-emr-applications"></a>

Start Kiro CLI or your MCP client and verify the loaded tools for the troubleshooting process.

```
...
 sagemaker-unified-studio-mcp-code-rec (MCP)
 - spark_code_recommendation    not trusted

 sagemaker-unified-studio-mcp-troubleshooting (MCP)
 - analyze_spark_workload       not trusted
...
```

You are now ready to start the Spark troubleshooting workflow.

A demonstration of the troubleshooting experience with Kiro CLI. You can start the troubleshooting process with the following prompt:

```
Analyze my Glue job. The job name is "xxx" and the job run id is "xxx"
```

For example prompts on each platform, see [Troubleshooting prompt examples](spark-troubleshooting-agent-prompt-examples.md).

[![AWS Videos](https://img.youtube.com/vi/YLwV_EenJXY/0.jpg)](https://www.youtube.com/watch?v=YLwV_EenJXY)


To use the agent with other MCP clients, such as Cline, Claude Code, or GitHub Copilot, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

## Troubleshoot from the console
<a name="troubleshoot-ai-button-console"></a>

You can start the troubleshooting agent directly from the console. Choose **Troubleshoot with AI** on EMR on EC2 and EMR on EKS, or choose **Analyze with AI** on EMR Serverless and AWS Glue.

### Troubleshoot with AI button for the EMR on EC2 console
<a name="troubleshoot-ai-button-emr-ec2"></a>

Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home). Choose **EMR on EC2** and select your cluster. Open the **Steps** tab. For any failed Spark step, choose **Failed**. This reveals the **Troubleshoot with AI** button in the popover. Alternatively, select the checkbox next to the failed step and choose **Troubleshoot with AI** at the top.

The following video shows how to use the **Troubleshoot with AI** button for EMR on EC2.

[![AWS Videos](https://img.youtube.com/vi/BPOlS55EqR8/0.jpg)](https://www.youtube.com/watch?v=BPOlS55EqR8)


### Analyze with AI button for the EMR Serverless console
<a name="troubleshoot-ai-button-emr-serverless"></a>

Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home) and navigate to **EMR Studio**. Open your EMR Studio URL. Navigate to **Applications** and select the application to troubleshoot. Open the **Batch job runs** tab. Select the checkbox next to the failed job run, and then choose **Analyze with AI** at the top. Alternatively, choose the **Failed** status of the job run, and then choose **Analyze with AI** in the popover. For a failed job run, the **Analyze with AI** button starts the troubleshooting agent.

The root cause analysis appears on the **AI analysis** tab of the job run.

The following screenshot shows the **Analyze with AI** button for a failed job run in EMR Studio.

![The Batch job runs tab of an EMR Serverless application in EMR Studio, with a failed job run selected and the Analyze with AI button at the top of the table.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/spark-troubleshoot-emrs-analyze-with-ai.png)


### Analyze with AI button for the AWS Glue console
<a name="troubleshoot-ai-button-glue"></a>

Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/). Under **ETL jobs**, choose the job. On the **Runs** tab, select the failed job run, and then choose **Analyze with AI** at the top. For a failed job run, the **Analyze with AI** button starts the troubleshooting agent.

The root cause analysis appears on the **AI analysis** tab of the job run.

The following screenshot shows the **Analyze with AI** button for a failed job run in the AWS Glue console.

![The Runs tab of an AWS Glue job, with a failed job run selected, the Analyze with AI button at the top of the table, and the root cause analysis on the AI analysis tab.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/spark-troubleshoot-glue-analyze-with-ai.png)


### Troubleshoot with AI button for the EMR on EKS console
<a name="troubleshoot-ai-button-emr-eks"></a>

Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home). Choose **EMR on EKS virtual clusters** and select your cluster. For any failed Spark job run, choose **Failed**. This reveals the **Troubleshoot with AI** button in the popover.

The following video shows how to use the **Troubleshoot with AI** button for EMR on EKS.

[![AWS Videos](https://img.youtube.com/vi/UqCVYpG_NuM/0.jpg)](https://www.youtube.com/watch?v=UqCVYpG_NuM)
