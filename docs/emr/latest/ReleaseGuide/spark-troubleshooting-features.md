

# Features and Capabilities
<a name="spark-troubleshooting-features"></a>

## Supported Platforms
<a name="supported-platforms"></a>
+ **Languages**: Python and Scala Spark applications
+ **Target Platforms**: Amazon EMR on EC2, EMR Serverless, EMR on EKS, and AWS Glue

## How It Works
<a name="how-it-works"></a>

When your Spark application fails, you can use the troubleshooting agent to automatically investigate what went wrong. It analyzes your Spark event logs, error messages, and resource usage to pinpoint the exact issue—whether it's a Spark executor running out of memory, a configuration error, or a code bug.

When you ask a natural language prompt to analyze your Spark workload, the agent connects to your platform's resources and extract features (which includes Spark event logs, query plans, executor timelines, log traces, configurations and metrics):
+ On EMR-EC2: it connects to [EMR Persistent UI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html) for the cluster
+ On Glue: it builds the context from Glue Studio's [Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html) for the job
+ On EMR-Serverless: it connects to EMR-Serverless [Spark History Server](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html) for the job
+ On EMR on EKS: it connects to EMR Persistent UI for the job.
+ The agent also analyzes your error stack traces and configuration details to give you actionable insights.

For failed workloads, you get a clear root cause explanation and specific steps to fix it. If the agent detects a code-related issue, it automatically provides code recommendations to show you exactly what to change in your code. You can also request code-level suggestions directly anytime you want them without the full analysis.

## Available Regions
<a name="available-regions"></a>

The Spark Troubleshooting Agent is available in the following regions:
+ **Asia Pacific**: Tokyo (ap-northeast-1), Seoul (ap-northeast-2), Singapore (ap-southeast-1), Sydney (ap-southeast-2), and Mumbai (ap-south-1)
+ **North America**: Canada (ca-central-1)
+ **Europe**: Stockholm (eu-north-1), Ireland (eu-west-1), London (eu-west-2), Paris (eu-west-3), and Frankfurt (eu-central-1)
+ **South America**: São Paulo (sa-east-1)
+ **United States**: North Virginia (us-east-1), Ohio (us-east-2), and Oregon (us-west-2)

## Scope of Spark Troubleshooting and User Requirements
<a name="scope-requirements"></a>
+ **Supported Spark workload states**: The tools will only support responses for failed Spark workloads.
+ **EMR Persistent UI:** When analyzing Amazon EMR on EC2 and EMR on EKS workloads, the analyze tool will attempt to connect to EMR Persistent UI to retrieve key Spark information. EMR Persistent UI considerations are documented [ here](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html#app-history-spark-UI-limitations).
+ **Glue Studio Spark UI**: When analyzing AWS Glue workloads, the analyze tool will attempt to retrieve key Spark information by parsing user's Spark event logs from Amazon S3. Maximum allowed Spark event log size is documented [ here](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html): 512 MB and 2 GB for rolling logs.
+ **Code Recommendations:** Only supported for Amazon EMR on EC2, EMR Serverless, EMR on EKS, and AWS Glue PySpark workloads
+ **Regional resources:** The Spark Troubleshooting Agent is regional and uses the underlying EMR resources in that region for the troubleshooting process. Cross-region troubleshooting is not supported.