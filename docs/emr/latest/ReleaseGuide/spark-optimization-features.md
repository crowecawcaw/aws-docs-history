

# Optimization features and capabilities

## Supported platforms for the optimization agent
<a name="spark-optimization-platforms"></a>
+ **Languages**: Python and Scala Spark applications
+ **Target platforms**: EMR Serverless and AWS Glue

## How the optimization agent reads your workload data
<a name="spark-optimization-how"></a>

After a Spark run succeeds, you can use the optimization agent to find where the run spends time or leaves capacity unused.

When you prompt the agent to optimize a run, it connects to your platform's resources and extracts features. These features are Spark event data (stages, query plans, and executors), the submitted configuration, and run metrics.
+ On EMR Serverless: it connects to the EMR Serverless [Spark History Server](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html) for the job run. It also reads the job run details and the application's configuration, including maximum capacity.
+ On AWS Glue: it builds the context from the Glue Studio [Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html), using the Spark event logs that the run wrote to Amazon S3, plus the job and job run details.
+ For a baseline comparison: the agent reads the same data for the baseline run.

For the output that you receive, see [Apache Spark Optimization Agent for Amazon EMR and AWS Glue](spark-optimization-agent.md).

## Analysis options
<a name="spark-optimization-options"></a>
+ **Baseline comparison**: Compare a less performant run against an earlier, better-performing baseline run of the same job. Name the baseline by its run ID. The baseline must be a successful run that meets the same requirements as the run that you're analyzing, including a supported version and available Spark event data. For these requirements, see [Scope of Spark optimization and user requirements](#scope-of-spark-optimization-and-user-requirements). If the baseline can't be used, the agent falls back to single-run analysis. For common causes, see [Observation: Baseline comparison falls back to single-run analysis](spark-troubleshooting-agent-troubleshooting.md#optimization-baseline-fallback).
+ **Optimization intent**: State in your prompt whether to optimize for cost or runtime, for example "optimize for cost" or "make it faster." If you don't state an intent, the agent optimizes for runtime. Cost and runtime often improve together, but not always. For example, adding capacity can shorten a run while increasing the total compute you pay for.

For example prompts, see [Optimization prompt examples](spark-optimization-prompt-examples.md).

## Scope of Spark optimization and user requirements
<a name="scope-of-spark-optimization-and-user-requirements"></a>
+ **Supported Spark workload states**: The optimization agent supports successful Spark workloads only.
+ **EMR Serverless**: Release `emr-7.6.0` and later. The agent reads Spark event data from the EMR Serverless Spark History Server, which relies on managed log storage. Managed storage is on by default and keeps logs for 30 days. Runs older than 30 days, or runs with managed storage turned off, can't be analyzed.
+ **AWS Glue**: Version 4.0 and later. The run must have the Spark UI enabled: set `--enable-spark-ui` to `true` and set `--spark-event-logs-path`. Both single-file and rolling event logs work. Runs that wrote event logs only to the legacy path (`--enable-spark-ui-legacy-path`) aren't supported. The maximum supported Spark event log size is 512 MB, and 1 GB for rolling logs. For more information, see [Monitoring with the Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html).
+ **IAM permissions**: The optimization agent uses the same permissions as the troubleshooting agent for EMR Serverless and AWS Glue. For more information, see [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md).
+ **Regional resources**: The optimization agent is Regional and uses the underlying EMR Serverless and AWS Glue resources in that Region for the optimization process. Cross-Region optimization isn't supported.
+ **Regions**: For the Regions where the agent is available, see [Available Regions](spark-troubleshoot.md#spark-agents-available-regions).