

# Send telemetry to CloudWatch Omni
<a name="omni-send-telemetry"></a>

CloudWatch Omni reads what Amazon CloudWatch has ingested. Configure your application, OpenTelemetry exporter, or collector to send telemetry to a CloudWatch OTLP endpoint. After that telemetry is in the CloudWatch Dataset for your space, it is available in CloudWatch Omni.

**Where to start**
+ [**Send application telemetry to CloudWatch Omni**](omni-send-application-telemetry.md)
  + **Environment:** [Amazon EC2](./omni-send-application-telemetry.html#omni-send-application-telemetry-amazon-ec2), [Amazon ECS](./omni-send-application-telemetry.html#omni-send-application-telemetry-amazon-ecs), [Amazon EKS](./omni-send-application-telemetry.html#omni-send-application-telemetry-amazon-eks), [Azure VM](./omni-send-application-telemetry.html#omni-send-application-telemetry-azure-vm), or [Azure AKS](./omni-send-application-telemetry.html#omni-send-application-telemetry-azure-aks).
  + On AWS Lambda there is no agent to deploy. See [Send application telemetry from AWS Lambda](omni-send-application-telemetry-from-aws-lambda.md).
+ [**Send AI agent telemetry to CloudWatch Omni**](omni-send-ai-agent-telemetry.md)
  + **Environment:** [Amazon Bedrock AgentCore](./omni-send-ai-agent-telemetry.html#omni-send-ai-agent-telemetry-agentcore), [AWS Lambda](./omni-send-ai-agent-telemetry.html#omni-send-ai-agent-telemetry-aws-lambda), [Amazon EC2](./omni-send-ai-agent-telemetry.html#omni-send-ai-agent-telemetry-amazon-ec2), [Amazon ECS](./omni-send-ai-agent-telemetry.html#omni-send-ai-agent-telemetry-amazon-ecs), or [Amazon EKS](./omni-send-ai-agent-telemetry.html#omni-send-ai-agent-telemetry-amazon-eks). The links open Step 2; Step 1 is the same for every environment.


| Your situation | Start here | 
| --- | --- | 
| My application already emits OpenTelemetry and sends it to a collector I run | Nothing to install. Configure your collector to sign requests and send to an endpoint below (see Bring your own collector under "Choose how you collect"), then confirm data arrives with the Your application appears check in Step 3 of [Send application telemetry](omni-send-application-telemetry.md). | 
| My application already emits OpenTelemetry but has no collector | Step 1 of [Send application telemetry](omni-send-application-telemetry.md), Deploy the CloudWatch agent, then Step 2, Point your application at the agent, and Step 3, Verify. Skip Step 4. | 
| My application is not instrumented yet | [Send application telemetry to CloudWatch Omni](omni-send-application-telemetry.md), all four steps. | 
| Telemetry stopped arriving, or never arrived | The troubleshooting table on the page you set up with: [applications](omni-send-application-telemetry.md), [Lambda](omni-send-application-telemetry-from-aws-lambda.md), or [AI agents](omni-send-ai-agent-telemetry.md). | 
| My workload runs somewhere not listed | Any OpenTelemetry collector or SDK can send to the endpoints below with SigV4-signed requests. See the collection comparison in [Getting started with OTLP](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPGettingStarted.html) in the Amazon CloudWatch User Guide. | 

**Note**  
**Assisted setup.** The **Add source** wizard in the Omni web UI (**Settings › Ingestion**) walks through the same choices and generates commands for your selections. From your coding agent, the Omni skills in the Agent Toolkit for AWS do the same; see [Use Omni skills](omni-use-omni-skills.md). From your editor, see [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

**How telemetry reaches your space**

![Ingestion path showing that CloudWatch Omni reads what Amazon CloudWatch ingested. Your source, an agent or application, sends OpenTelemetry data through a collector or the SDK to an OTLP endpoint inside Amazon CloudWatch, which stores it in the CloudWatch Dataset for your space, and CloudWatch Omni queries that Dataset. A collectorless path lets the ADOT SDK send traces to the endpoint directly.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-ingestion-path.png)


**Forwarding to the Dataset**

The **CloudWatch Dataset integration** is the step between Amazon CloudWatch and the Dataset in the diagram above: it forwards your CloudWatch logs and traces into the Dataset for your space. Setting up a space in the CloudWatch console also creates the integration and an execution role that the CloudWatch Logs service assumes, so forwarding starts without a separate step. The space and the integration are separate resources — console setup creates them together, and you manage them independently. For the roles setup creates, see [Set up Omni for a single account](omni-set-up-omni-for-a-single-account.md). The integration forwards logs and traces together. Metrics are not forwarded; Omni queries them directly from CloudWatch Metrics.

There is one Dataset integration per account in a Region, and forwarding is same-account and same-Region. The execution role's `logs:IntegrateWithDataset` permissions control which log groups forward. Log groups in the Delivery log class do not forward, regardless of the role's permissions.

To manage the integration directly — for example, with the AWS CLI or infrastructure as code — follow these three steps.

**Step 1. Create an execution role for the CloudWatch Logs service to assume.** This example uses the name `CloudWatchOmniDatasetIntegrationRole`; you can use any name. The role must be in the same account as the Dataset and the integration — IAM does not support passing a role across accounts. Use this trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "logs.amazonaws.com" },
    "Action": "sts:AssumeRole",
    "Condition": {
      "StringEquals": { "aws:SourceAccount": "<account-id>" },
      "ArnLike": { "aws:SourceArn": "arn:aws:observabilityadmin:<region>:<account-id>:dataset-integration/default" }
    }
  }]
}
```

In both `Condition` values, `<account-id>` is the account that owns the role, the Dataset, and the integration. With any other account ID the create call still succeeds, but no logs forward.

**Step 2. Attach this permissions policy to the role.** The `log-group:*` resource forwards all log groups in the account except Delivery-class log groups; to forward only specific log groups, replace `*` with a log group name. If your space's Dataset is encrypted with a customer managed AWS KMS key, the key's policy must also allow this role `kms:Encrypt`, `kms:Decrypt`, and `kms:GenerateDataKey` on records entering the Dataset — see the `AllowCallerDatasetForwarding` statement in the sample key policy in [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "logs:IntegrateWithDataset",
      "Resource": ["arn:aws:logs:<region>:<account-id>:log-group:*"]
    },
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutRecords",
      "Resource": "*"
    }
  ]
}
```

**Step 3. Create the Dataset integration, passing the execution role.** Creating or updating the integration requires `iam:PassRole` on the execution role.

```
aws observabilityadmin create-dataset-integration \
    --role-arn arn:aws:iam::<account-id>:role/CloudWatchOmniDatasetIntegrationRole \
    --region <region>
```

**Changing what is forwarded.** Updates to the execution role's `logs:IntegrateWithDataset` permissions take effect within a few minutes. Changes to what is forwarded apply going forward: removing a log group stops future records from forwarding, and records already in the Dataset remain until they pass their retention period. To change the execution role, use `update-dataset-integration`; to stop all forwarding, use `delete-dataset-integration`.

**Choose how you collect**

The collection path you choose affects which features you get: entity correlation and Container Insights are not available on every path. For a comparison of the CloudWatch agent, an upstream OpenTelemetry Collector, a custom collector, and collectorless export with the AWS Distro for OpenTelemetry (ADOT) SDK, see [Getting started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPGettingStarted.html) in the Amazon CloudWatch User Guide.

The CloudWatch agent is the recommended path for applications, and it is the path [Send application telemetry to CloudWatch Omni](omni-send-application-telemetry.md) uses. AI agents and Lambda functions do not use a collector: an AI agent exports its traces directly from the ADOT SDK, and Lambda delivers segments and logs itself. To configure the CloudWatch agent for OTLP, see [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPCloudWatchAgent.html) in the Amazon CloudWatch User Guide.

**Bring your own collector.** Point a self-managed OpenTelemetry Collector's exporters at the endpoints below. The collector's role needs the permissions named in the "Authentication" section of this page, and each exporter needs SigV4 signing configured; for the collector configuration, see [Getting started with OTLP](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPGettingStarted.html) in the Amazon CloudWatch User Guide.

**Choose an endpoint**


| Endpoint | Use for | Authentication | 
| --- | --- | --- | 
| Traces | Application traces forwarded by the CloudWatch agent, and AgentCore runtime traces. The primary signal for Omni. | SigV4 only | 
| Metrics | Custom OpenTelemetry metrics, queryable with PromQL. | SigV4, or a bearer token | 
| Logs | Log records, forwarded to a log group and log stream you name in request headers. | SigV4, or a bearer token | 

For the hostnames, per-signal request headers, protocol support, and the ingestion limits that apply to each, see [OTLP endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html).

**Important**  
Enable Transaction Search in the Region before you send traces. It is an account-level setting, and until it is enabled spans do not arrive.

**Authentication**

AWS Signature Version 4 (SigV4) with short-lived credentials is the default for every path and the only method the traces endpoint accepts. A workload running on AWS compute signs with the role it already has, but that role must carry the permissions for the path you use, and the three paths do not share one permission set. Each procedure page shows the statement to attach.
+ Collector path: the CloudWatch agent's managed policy, `CloudWatchAgentServerPolicy`.
+ An AgentCore runtime: the trace-delivery actions `xray:GetSamplingRules`, `xray:GetSamplingTargets`, `xray:PutTelemetryRecords`, and `xray:PutTraceSegments` on the runtime's execution role.

Workloads outside AWS can federate for temporary credentials; the Azure procedure does this. Restrict bearer tokens to scenarios where short-lived credentials are not feasible. The metrics and logs endpoints accept a long-lived bearer token. The traces endpoint does not, and accepts SigV4 only. See [Setting up bearer token authentication for Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLP-MetricsBearerTokenAuth.html). Token creation requires IAM mutating actions, so it is an administrator task.

**Environment support**

For the environments, languages, and frameworks with a documented path, the signals each produces, and the minimum library versions, see [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md).

On-premises hosts can obtain temporary AWS credentials with [IAM Roles Anywhere](https://aws.amazon.com/iam/roles-anywhere/), so a collector on your own hosts signs requests with SigV4 instead of storing a long-lived key.

**Next steps**

When telemetry is arriving, see [Monitor AI agents](omni-monitor-ai-agents.md) and [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md). To control who can access the space, see [Control access to your space](omni-control-access-to-your-space.md). To keep sensitive content out of the telemetry you send and store, see [Protect sensitive data](omni-data-protection.md).