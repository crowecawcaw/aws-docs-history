

# Troubleshooting features and capabilities

## Supported platforms for the troubleshooting agent
<a name="supported-platforms"></a>
+ **Languages**: Python and Scala Spark applications
+ **Target platforms**: EMR on EC2, EMR Serverless, EMR on EKS, and AWS Glue

## How the troubleshooting agent reads your workload data
<a name="how-it-works"></a>

When your Spark application fails, you can use the troubleshooting agent to automatically investigate what went wrong. It analyzes your Spark event logs, error messages, and resource usage to pinpoint the exact issue—whether it's a Spark executor running out of memory, a configuration error, or a code bug.

When you ask a natural language prompt to analyze your Spark workload, the agent connects to your platform's resources and extracts features (which include Spark event logs, query plans, executor timelines, log traces, configurations, and metrics):
+ On EMR on EC2: it connects to the [EMR persistent UI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html) for the cluster.
+ On AWS Glue: it builds the context from the Glue Studio [Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html) for the job.
+ On EMR Serverless: it connects to the EMR Serverless [Spark History Server](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html) for the job.
+ On EMR on EKS: it connects to the EMR persistent UI for the job.
+ The agent also analyzes your error stack traces and configuration details to give you actionable insights.

For failed workloads, you get a clear root cause explanation and specific steps to fix it. If the agent detects a code-related issue, it automatically provides code recommendations to show you exactly what to change in your code. You can also request code-level suggestions directly anytime you want them, without the full analysis.

## Scope of Spark troubleshooting and user requirements
<a name="scope-of-spark-troubleshooting-and-user-requirements"></a>
+ **Supported Spark workload states**: The tools support responses for failed Spark workloads only.
+ **EMR persistent UI**: When analyzing EMR on EC2 and EMR on EKS workloads, the analyze tool attempts to connect to the EMR persistent UI to retrieve key Spark information. EMR persistent UI considerations are documented in [Spark UI limitations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html#app-history-spark-UI-limitations).
+ **Glue Studio Spark UI**: When analyzing AWS Glue workloads, the analyze tool attempts to retrieve key Spark information by parsing your Spark event logs from Amazon S3. The maximum supported Spark event log size is 512 MB, and 1 GB for rolling logs. For more information, see [Monitoring with the Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html).
+ **Code recommendations**: Supported only for EMR on EC2, EMR Serverless, EMR on EKS, and AWS Glue PySpark workloads.
+ **Regional resources**: The troubleshooting agent is Regional and uses the underlying Amazon EMR resources in that Region for the troubleshooting process. Cross-Region troubleshooting is not supported.
+ **Regions**: For the Regions where the agent is available, see [Available Regions](spark-troubleshoot.md#spark-agents-available-regions).