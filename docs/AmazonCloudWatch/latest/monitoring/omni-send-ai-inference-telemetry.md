

# Collect AI inference telemetry
<a name="omni-send-ai-inference-telemetry"></a>

In CloudWatch Omni, AI Inference Insights is the monitoring experience for inference telemetry. It covers self-hosted vLLM engines that run on Amazon ECS or on Amazon EKS. Setting it up needs no application code changes, because you configure your engine and a collector rather than your application.

Choose one of the following setup paths. The Amazon EKS add-on path is the least work if you run on Amazon EKS.
+ [Set up on Amazon EKS with the CloudWatch Observability add-on](#omni-ai-inference-setup-eks-addon) – On Amazon EKS, install the CloudWatch Observability add-on and turn on OTel Container Insights. The add-on collects your engine and accelerator metrics and declares the workload as AI inference for you. This is also the same collection path that Accelerated Compute Insights uses, so you configure it once for both.
+ [Set up with a coding assistant](#omni-ai-inference-setup-assistant) – Copy a prompt from Omni that gives your coding assistant the Omni MCP server and skills, and then ask the assistant to do the setup.
+ [Set up manually in Omni](#omni-ai-inference-setup-manual) – Work through the guided setup in Omni for Amazon ECS or Amazon EKS. Omni generates the configuration for you to copy.

**Note**  
Accelerated Compute Insights in the Amazon CloudWatch console provides this same capability in a different console, and covers Amazon EKS only. The Amazon EKS add-on path below serves both. For more information, see [Accelerated Compute Insights](Accelerated-Compute-Insights.md).

## Set up on Amazon EKS with the CloudWatch Observability add-on
<a name="omni-ai-inference-setup-eks-addon"></a>

On Amazon EKS, install the latest version of the `amazon-cloudwatch-observability` add-on and turn on OTel Container Insights. The add-on then collects your engine metrics and your accelerator metrics, so you do not configure a separate pipeline for each.

You can install the add-on in any of the following ways:
+ From Omni, on the **AWS platforms** page in **Settings**. Omni gives you a script that configures the IAM trust, installs the Amazon EKS Pod Identity Agent, associates the role with the `cloudwatch-agent` service account, and installs the add-on.
+ With the `aws eks create-addon` command, or from the Amazon EKS console.
+ With the CloudWatch Observability Helm chart, if you manage cluster components with Helm.

For the add-on setup steps, see [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md). For the accelerator metrics that the same add-on collects, see [Get started with Accelerated Compute Insights](Accelerated-Compute-Insights-Get-Started.md).

On this path, the add-on declares the workload as AI inference for you. The add-on's vLLM pipeline sets the `aws.service.type` resource attribute to `ai_inference` on the engine's metrics, so you do not set it yourself. For KServe workloads, the add-on sets the attribute on the predictor revision of an InferenceService. It does not set the attribute on transformer or explainer revisions, or on a plain Knative service, because those do not run the model. For more information about the attribute, see [Declare the workload as AI inference](#omni-ai-inference-declare-workload).

**Note**  
Automatic declaration requires add-on version `v7.0.0-eksbuild.1` or later. On an earlier version, set the attribute yourself.

Traces are still a separate step on this path. See [Send vLLM traces](#omni-ai-inference-send-traces).

## Set up with a coding assistant
<a name="omni-ai-inference-setup-assistant"></a>

Omni can give your coding assistant everything it needs to do the setup for you. In **Settings**, on the **Ingestion** page, Omni provides a prompt that you copy into your coding assistant. The prompt installs the CloudWatch Omni skills and the Omni MCP server in that assistant. You then ask the assistant to carry out the setup task.

Use this path when you want the configuration written for you instead of copying it yourself. Review what the assistant changes before you apply it.

## Set up manually in Omni
<a name="omni-ai-inference-setup-manual"></a>

The guided setup in Omni collects the details of your environment and then presents the steps that match it. It covers both Amazon ECS and Amazon EKS.

**To start the AI inference setup**

1. In CloudWatch Omni, choose **Settings**.

1. Open the **Ingestion** page.

1. Choose **Add new source**.

1. For **What you are monitoring**, choose **AI inference**.

1. Choose the resource where your engine runs: Amazon ECS or Amazon EKS.

1. For **Collector**, choose either the CloudWatch agent, which builds the export pipeline from a short JSON configuration, or the OpenTelemetry Collector Contrib distribution, if you already run one.

1. (Optional) To include the trace steps, select **Show the steps to send vLLM traces**.

Omni then generates a JSON configuration for Amazon ECS, or a manifest for Amazon EKS, with the scripts and configuration files embedded. Copy it and replace the placeholder values with your own before you apply it.

On Amazon ECS, you prepare Amazon EC2 GPU capacity, the task role, the DCGM exporter, the vLLM container, and a collector sidecar in the task. On Amazon EKS, you prepare GPU nodes, collector permissions, the DCGM exporter, the vLLM workload, and the collector.

## Declare the workload as AI inference
<a name="omni-ai-inference-declare-workload"></a>

Omni recognizes a workload as AI inference from the OpenTelemetry resource attribute `aws.service.type`, set to `ai_inference` on the engine's telemetry. Omni also reads that same attribute from the engine's traces, which gives the node the **AI Inference** type on the application map.

**Important**  
Omni does not discover your workload as AI inference without this attribute. Who sets it depends on your setup path.
+ **Amazon EKS add-on path** – The add-on sets the attribute for you. See [Set up on Amazon EKS with the CloudWatch Observability add-on](#omni-ai-inference-setup-eks-addon).
+ **Amazon ECS, and any path where you run your own collector** – Set the attribute yourself, in your collector configuration.

## Send vLLM traces
<a name="omni-ai-inference-send-traces"></a>

Traces are optional, and they send one trace for each request. Traces build the application topology, so they make the workload appear as a service with an application in Omni.

**Important**  
We recommend that you send traces. On Amazon EKS, Omni might not list the service at all until traces arrive. On Amazon ECS, traces list the service sooner and give it its application.

## Verify your telemetry
<a name="omni-ai-inference-verify"></a>

The guided setup ends with the **Verify your application is instrumented** step. After you run your instrumented application, this step confirms that it is exporting telemetry. This step usually takes less than 5 minutes.

After your telemetry arrives, the workload appears in AI Inference Insights. For more information about the monitoring experience, see [AI Inference Insights](omni-ai-inference-insights.md).

**Note**  
CloudWatch rejects a range selector that is longer than 24 hours. When you select a time range longer than 24 hours, the engine rates and the time-to-first-token percentile cover only the last 24 hours of that range. The workload index also holds only the workloads seen in those last 24 hours. For more information, see [AI Inference Insights](omni-ai-inference-insights.md).