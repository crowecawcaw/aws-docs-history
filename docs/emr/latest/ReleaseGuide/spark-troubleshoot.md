

# Spark Troubleshooting and Optimization Agents

The Apache Spark agents analyze your Apache Spark workloads on Amazon EMR and AWS Glue. You can use the agents from an MCP client with natural language prompts, or directly from the console. In either case, the `analyze_spark_workload` tool on the Amazon SageMaker Unified Studio remote MCP server is invoked and picks the analysis based on how the run ended:
+ For a failed run, the Apache Spark Troubleshooting Agent finds the root cause and recommends fixes.
+ For a successful run, the Apache Spark Optimization Agent recommends configuration and data changes that improve performance.

## Architecture
<a name="spark-troubleshooting-agent-architecture"></a>

The following diagram shows how the Apache Spark agents work. The numbers show the order of the steps.

![Architecture of the Apache Spark agents: you ask from an MCP client or the Analyze with AI button, and the Amazon SageMaker Unified Studio remote MCP server reads your Spark workload data, extracts features, and generates recommendations. For failed runs, it also generates code recommendations, and guardrails apply at every stage.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/spark-agents-architecture.png)


You start by asking about your job run in natural language (1) from an MCP client in your development environment, or by choosing the **Analyze with AI** button in the console (2). An MCP client connects through the [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws). The proxy runs on your machine, signs each request with SigV4 using the credentials from your AWS CLI profile, and forwards it to the Amazon SageMaker Unified Studio remote MCP server. The remote MCP server reads your job run data (3), analyzes it (4), proposes code fixes for failed runs when the issue is in your code (5), and returns recommendations with explanations (6).

### How the agents use your identity
<a name="spark-agents-identity"></a>

Both agents act as the IAM identity that your MCP client is configured with. That identity is either your own identity or a dedicated role that your AWS CLI profile assumes. The identity's permissions define what the agents can read. You don't need any separate MCP-specific permissions.

For each request, the remote MCP server uses short-lived credentials for your identity to call Amazon EMR, AWS Glue, Amazon S3, and Amazon CloudWatch Logs, and to read Spark History Server or Spark UI data. The server doesn't use access of its own to read your resources, and it doesn't store your credentials.

Requests made through the server carry the condition keys `aws:ViaAWSMCPService` and `aws:CalledViaAWSMCP`. You can use these keys to scope what the agents can do. For more information, see [How can I get more fine-grained control over the agents' permissions?](spark-troubleshooting-agent-iam-setup.md#qa-fine-grained-permissions).

The agents only read data. They don't modify, start, or stop your jobs. For the policies that each platform needs, see [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md).

### Guardrails
<a name="spark-agents-guardrails"></a>

Both agents apply the following guardrails:
+ **PII masking** – Before any data reaches the model, Amazon Comprehend detects PII and masks it. The model's response is also masked. Masked values aren't restored in the analysis output.
+ **Content guardrail** – Every model call goes through an Amazon Bedrock guardrail that blocks harmful content and prompt attacks.

Each agent adds its own checks, some of which are described in the following sections.

### Troubleshooting agent
<a name="spark-agents-troubleshooting-flow"></a>

The troubleshooting agent runs on failed runs on Amazon EMR on EC2, EMR Serverless, EMR on EKS, and AWS Glue.

**Extracts features and builds context (3)**

The agent reads evidence about the failed run from your platform:
+ **EMR on EC2** – Step and container logs from Amazon S3, and the EMR persistent UI.
+ **EMR Serverless** – Driver and executor logs from Amazon S3 or Amazon CloudWatch Logs, and the Spark History Server.
+ **EMR on EKS** – Logs from Amazon S3 or Amazon CloudWatch Logs, and the persistent UI.
+ **AWS Glue** – Amazon CloudWatch Logs, and the Glue Studio Spark UI, built from the event logs.

On every platform, the agent also reads the run's Spark configuration and extracts the stack traces.

**Analyzes the failure and recommends fixes (4)**

Deterministic rules drive the analysis, along with relevant guidance that the agent retrieves from its curated Spark troubleshooting knowledge base. The agent then generates the root cause and recommended fixes.

You get back the root cause and recommendations, plus which artifacts the agent could and couldn't analyze (`artifacts_analyzed`). If no code change is needed, the analysis ends here. When code recommendations apply, the response tells your MCP client to call `spark_code_recommendation`.

**Recommends code changes (5)**

Code recommendations apply to code-related errors in PySpark jobs.

The tool maps the parts of your script that are relevant to the error, applies fix guidance specific to the error type, and proposes code changes, along with `spark-submit` argument changes when they're needed. These are proposals only. The tool does not apply them.

Code recommendations add their own guardrails. For example, sensitive data in your script and stack trace is masked before it reaches the model, then restored in the proposed changes so they're usable. A content guardrail also runs on code generation.

For more information, see [Apache Spark Troubleshooting Agent for Amazon EMR and AWS Glue](spark-troubleshooting-agent.md).

### Optimization agent
<a name="spark-agents-optimization-flow"></a>

The optimization agent runs only on successful runs on Amazon EMR Serverless and AWS Glue.

**Extracts features and builds context (3)**

The agent primarily reads the following from your run:
+ **Spark event data** – Stages, tasks, executors, shuffle, and SQL plans. On EMR Serverless, this data comes from the Spark History Server. On AWS Glue, it comes from the Glue Studio Spark UI, built from the run's event logs in Amazon S3.
+ **Configuration** – The run's submitted and effective configuration, at the application level and the job run level.

**Generates recommendations (4)**

The agent combines the following to produce recommendations:
+ **Rule-based investigations** – Deterministic checks look for issues in four categories:
  + **Memory** – GC pressure, spill, out-of-memory, and disk full.
  + **Data** – Skew, stragglers, too few partitions, oversized tasks, and slow reads.
  + **Capacity** – Idle or underused capacity, right-sizing, backlog against the capacity ceiling, and contention for shared capacity.
  + **Execution** – Fetch failures, killed containers, oversized execution plans, and adaptive query execution settings.
+ **Intent** – Your goal, cost or performance, comes from your prompt. A cost goal means lowering what the run costs to execute, and a performance goal means speeding runtime. If you don't state a goal, the agent optimizes for performance. With a baseline and no stated goal, the agent uses whichever metric regressed. Intent-based models use your goal to decide which recommendations are allowed and how capacity is sized.
+ **Knowledge base** – Spark tuning guidance curated by AWS engineers from their experience running Spark at scale, matched to your platform, version, and the issues found.
+ **Baseline comparison** – A baseline comparison happens only when you name a baseline by its run ID. The baseline must be an earlier run of the same job (AWS Glue) or the same application (EMR Serverless). The agent compares configuration, metrics, stages, and capacity, and determines how to mitigate the regression. If the baseline can't be used, the agent analyzes the current run on its own.

**Validates recommendations**

Before the agent returns results, deterministic rules drop or adjust recommendations that the evidence doesn't support:
+ They drop settings that can't take effect.
+ They block changes that work against your goal, such as changes that raise cost under a cost goal, or capacity cuts that could slow the job under a performance goal.
+ They withhold capacity changes when nothing shows that capacity is the problem.
+ They ensure that each recommendation is valid for the platform it's for.

You get back a summary, prioritized recommendations tagged `[config]`, `[infra]`, or `[data]`, recommended Spark properties with their current and recommended values, and the baseline comparison when one was used.

The optimization agent doesn't support code recommendations through the `spark_code_recommendation` tool.

For more information, see [Apache Spark Optimization Agent for Amazon EMR and AWS Glue](spark-optimization-agent.md).

## Tools
<a name="spark-agents-tools"></a>

The Amazon SageMaker Unified Studio remote MCP server provides the following tools for the Apache Spark agents.



| Tool | MCP server | Used by | 
| --- | --- | --- | 
| analyze\_spark\_workload | sagemaker-unified-studio-mcp-troubleshooting | Both agents | 
| spark\_code\_recommendation | sagemaker-unified-studio-mcp-code-rec | Troubleshooting agent only | 

Your MCP client calls these tools based on your prompt.

## Feature list for each agent
<a name="spark-agents-features"></a>

The following table lists the features that each agent supports.



| Aspect | Apache Spark Troubleshooting Agent | Apache Spark Optimization Agent | 
| --- | --- | --- | 
| Run state analyzed | Failed runs | Successful runs | 
| Supported platforms | EMR on EC2, EMR Serverless, EMR on EKS, AWS Glue, and Amazon SageMaker notebooks | EMR Serverless and AWS Glue | 
| Output | Root cause analysis and code fixes | Performance and cost analysis, and configuration and data recommendations | 
| Code recommendations | Yes | No | 
| Entry points | MCP clients, the Troubleshoot with AI button (EMR on EC2 and EMR on EKS consoles), the Analyze with AI button (EMR Serverless and AWS Glue consoles), and the notebook Fix with AI button | MCP clients, the Analyze with AI button (EMR Serverless and AWS Glue consoles), and the notebook Fix with AI button | 

## Pricing
<a name="spark-agents-pricing"></a>

The Apache Spark agents are available at no additional cost as part of Amazon EMR and AWS Glue. The agents provide analysis and recommendations. You pay only for the Amazon EMR or AWS Glue resources that you use, including any runs you start to validate a recommended change.

## Available Regions
<a name="spark-agents-available-regions"></a>

The Apache Spark agents are available in the following Regions:
+ **Asia Pacific**: Tokyo (ap-northeast-1), Seoul (ap-northeast-2), Singapore (ap-southeast-1), Sydney (ap-southeast-2), Mumbai (ap-south-1), Osaka (ap-northeast-3), Hong Kong (ap-east-1), Taipei (ap-east-2), Hyderabad (ap-south-2), Jakarta (ap-southeast-3), Melbourne (ap-southeast-4), Malaysia (ap-southeast-5), New Zealand (ap-southeast-6), and Thailand (ap-southeast-7)
+ **North America**: Canada (ca-central-1), Calgary (ca-west-1), and Mexico (mx-central-1)
+ **Europe**: Stockholm (eu-north-1), Ireland (eu-west-1), London (eu-west-2), Paris (eu-west-3), Frankfurt (eu-central-1), Zurich (eu-central-2), Milan (eu-south-1), and Spain (eu-south-2)
+ **Middle East**: Tel Aviv (il-central-1)
+ **Africa**: Cape Town (af-south-1)
+ **South America**: São Paulo (sa-east-1)
+ **United States**: N. Virginia (us-east-1), Ohio (us-east-2), Oregon (us-west-2), and N. California (us-west-1)

**Topics**
+ [Architecture](#spark-troubleshooting-agent-architecture)
+ [Tools](#spark-agents-tools)
+ [Feature list for each agent](#spark-agents-features)
+ [Pricing](#spark-agents-pricing)
+ [Available Regions](#spark-agents-available-regions)
+ [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md)
+ [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md)
+ [Apache Spark Troubleshooting Agent for Amazon EMR and AWS Glue](spark-troubleshooting-agent.md)
+ [Apache Spark Optimization Agent for Amazon EMR and AWS Glue](spark-optimization-agent.md)
+ [Common errors and FAQs for the Apache Spark agents](spark-troubleshooting-agent-troubleshooting.md)
+ [Configuring interface VPC endpoints for Amazon SageMaker Unified Studio MCP](spark-troubleshooting-agent-vpc-endpoints.md)
+ [Cross-Region processing for the Apache Spark agents](spark-troubleshooting-cross-region-processing.md)
+ [Logging Amazon SageMaker Unified Studio MCP calls using AWS CloudTrail](spark-troubleshooting-cloudtrail-integration.md)
+ [Data handling for the Apache Spark agents](spark-agents-service-improvements.md)