

# Apache Spark Optimization Agent for Amazon EMR and AWS Glue

The Apache Spark Optimization Agent analyzes successful Spark runs on EMR Serverless and AWS Glue and returns prioritized recommendations that reduce cost or runtime.

When you ask about a successful run, the `analyze_spark_workload` tool uses the optimization agent. You can use the optimization agent from MCP clients or from the console. For setup, pricing, and architecture, see [Spark Troubleshooting and Optimization Agents](spark-troubleshoot.md).

If you've already set up the troubleshooting agent, you can use the optimization agent on the same platforms without additional setup. For more information, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

## Get started with the optimization agent
<a name="spark-optimization-agent-get-started"></a>

**To optimize a job run from the console**

1. Open the job runs for your application or job.

1. Select a successful job run, and then choose **Analyze with AI**.

1. Choose **Performance** or **Cost**, and then choose **View recommendations**.

1. Review the recommendations on the run's **AI analysis** tab.

1. Apply the changes that you want in a non-production run, and compare its runtime and cost with the original run.

**To find out why a job run got slower, from the console**

1. Select the slower successful job run, and then choose **Analyze with AI**.

1. Under **Baseline job**, choose an earlier, better-performing run of the same job, and then choose **Compare with baseline**.

1. Review what changed on the run's **AI analysis** tab.

**To optimize a job run with an MCP client**

1. Set up the Apache Spark agents in your MCP client. For more information, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

1. Ask the agent to optimize a successful run. Say whether you want it faster or cheaper. For example:

   ```
   How can I make my EMR Serverless job run {{job-run-id}} in application {{application-id}} faster?
   ```

   ```
   How can I reduce the cost of my Glue job {{job-name}} run {{job-run-id}}?
   ```

1. To find out why a run got slower, name an earlier, better-performing run as the baseline:

   ```
   My EMR Serverless job run {{job-run-id}} in application {{application-id}} got slower than run {{baseline-job-run-id}}. Tell me why and how to fix it.
   ```

1. Review the recommendations. Ask follow-up questions about any of them.

1. Apply the changes that you want in a non-production run. Then ask the agent to analyze the new run.

**Important**  
The agent only reads your job runs. It doesn't change your job. Test recommended changes in a non-production run before you apply them to production jobs.

For console details, see [Using the Optimization Agent](spark-optimization-using.md). For more prompts, see [Optimization prompt examples](spark-optimization-prompt-examples.md). For requirements, such as supported versions and Spark event data, see [Scope of Spark optimization and user requirements](spark-optimization-features.md#scope-of-spark-optimization-and-user-requirements).

## Types of optimization analysis
<a name="spark-optimization-agent-types"></a>

The optimization agent supports two kinds of analysis.
+ **Single-run optimization** – The agent analyzes one successful run for common sources of inefficiency, such as idle or underused capacity, data skew, memory pressure, and inefficient reads.
+ **Baseline comparison (regression analysis)** – The agent compares a less performant run against an earlier, better-performing baseline run. It looks at configuration, run metrics, stage and task behavior, shuffle, and capacity to isolate what changed.

For how to run each kind of analysis, see [Optimization features and capabilities](spark-optimization-features.md).

## How the optimization agent works
<a name="spark-optimization-agent-how"></a>

The workflow follows these steps:

1. **Feature extraction and context building** – The agent reads the run's configuration and Spark event data, and measures where time went, how evenly data was distributed, and how much capacity sat idle. This step also incorporates the optional baseline run and the cost or runtime intent.

1. **Analysis and optimization recommendations** – The agent uses AI models and knowledge of how each platform allocates capacity to turn the measurements into prioritized recommendations. You receive the following:
   + **Summary** – A short description of how the run behaved.
   + **Recommendations** – Prioritized changes, each tagged as one of the following:
     + An infrastructure change (`[infra]`), such as application capacity or worker type and count
     + A Spark configuration change (`[config]`)
     + A data layout change (`[data]`), such as repartitioning or compacting small files
   + **Recommended Spark properties (when applicable)** – The current and proposed value of each Spark property that the agent suggests changing.
   + **Comparison (baseline comparison only)** – What changed between the two runs.

**Topics**
+ [Get started with the optimization agent](#spark-optimization-agent-get-started)
+ [Types of optimization analysis](#spark-optimization-agent-types)
+ [How the optimization agent works](#spark-optimization-agent-how)
+ [Using the Optimization Agent](spark-optimization-using.md)
+ [Optimization features and capabilities](spark-optimization-features.md)
+ [Optimization prompt examples](spark-optimization-prompt-examples.md)