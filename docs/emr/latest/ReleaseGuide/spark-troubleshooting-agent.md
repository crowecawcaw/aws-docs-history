

# Apache Spark Troubleshooting Agent for Amazon EMR and AWS Glue

The Apache Spark Troubleshooting Agent for Amazon EMR is a conversational AI capability that simplifies the troubleshooting of Apache Spark applications on Amazon EMR (EMR on EC2, EMR Serverless, and EMR on EKS), AWS Glue, and Amazon SageMaker notebooks. Traditional Spark troubleshooting requires extensive manual analysis of logs, performance metrics, and error patterns to identify root causes and code fixes. The troubleshooting agent simplifies this process through natural language prompts, automated workload analysis, and intelligent code recommendations.

You can use the troubleshooting agent to troubleshoot PySpark and Scala application failures. The agent analyzes your failed jobs, identifies the root cause of each failure, and provides actionable recommendations and code fixes while giving you full control over implementation decisions.

When you ask about a failed run, the `analyze_spark_workload` tool uses the troubleshooting agent. For setup, pricing, and architecture, see [Spark Troubleshooting and Optimization Agents](spark-troubleshoot.md).

If you've already set up the optimization agent, you can use the troubleshooting agent on the same platforms without additional setup. To get code recommendations, also add the code recommendation server. For more information, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

## Get started with the troubleshooting agent
<a name="spark-troubleshooting-agent-get-started"></a>

**To troubleshoot a failed job run from the console**

1. Open the job runs for your application, job, or cluster.

1. Select the failed job run, and then choose **Analyze with AI**. On some consoles, this button is called **Troubleshoot with AI**.

1. Review the root cause analysis. If the issue is in your code, also review the recommended code fix.

1. Apply the fix in a non-production run. Then run the job again.

**To troubleshoot a failed job run with an MCP client**

1. Set up the Apache Spark agents in your MCP client. For more information, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

1. Ask the agent to troubleshoot a failed run. For example:

   ```
   Troubleshoot my EMR-Serverless job run with application id 00xxxxxxxx and job run id 00xxxxxxxx
   ```

   ```
   Troubleshoot my Glue job with job run id jr_xxxxxxxxxxxxxxxxxxxxxxxxxxxx and job name test_job
   ```

1. Review the root cause and the recommended fixes. Ask follow-up questions about any of them.

1. If the issue is in your PySpark code, ask for a code fix. For example:

   ```
   Recommend code fix for my Glue job with job run id jr_JOB_RUN_ID and job name test_job
   ```

1. Apply the fix in a non-production run. Then run the job again.

**Important**  
The agent only reads your job runs. It doesn't change your job. Test recommended changes in a non-production run before you apply them to production jobs.

For console details, see [Using the Troubleshooting Agent](spark-troubleshooting-using-troubleshooting-agent.md). For more prompts, see [Troubleshooting prompt examples](spark-troubleshooting-agent-prompt-examples.md). For requirements, see [Scope of Spark troubleshooting and user requirements](spark-troubleshooting-features.md#scope-of-spark-troubleshooting-and-user-requirements).

## How the troubleshooting agent works
<a name="spark-troubleshooting-agent-how"></a>

The agent orchestrates the troubleshooting using specialized tools. The workflow follows these steps:

1. **Feature extraction and context building** – The agent collects and analyzes telemetry data from your Spark application, including Spark History Server logs, configuration settings, and error traces. It extracts key performance metrics, resource utilization patterns, and failure signatures to build a context profile for the analysis.

1. **Analysis and root cause identification** – The agent uses AI models and a Spark knowledge base to correlate the extracted features and identify the root cause of the failure. You receive the following:
   + **Analysis insights** – Technical details about what the agent discovered and analyzed.
   + **Root cause** – A clear explanation of what went wrong and why.
   + **Initial assessment** – Whether the issue is code-related, configuration-related, or resource-related, with general guidance for mitigation.

1. **Code recommendations (when applicable)** – If the analysis identifies a code-related issue based on the error classification, the agent can use the code recommendation tool to provide a specific fix, with exact before-and-after code and suggested replacements.

**Topics**
+ [Get started with the troubleshooting agent](#spark-troubleshooting-agent-get-started)
+ [How the troubleshooting agent works](#spark-troubleshooting-agent-how)
+ [Using the Troubleshooting Agent](spark-troubleshooting-using-troubleshooting-agent.md)
+ [Troubleshooting features and capabilities](spark-troubleshooting-features.md)
+ [Troubleshooting prompt examples](spark-troubleshooting-agent-prompt-examples.md)