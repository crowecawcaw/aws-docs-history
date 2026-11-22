

# Monitor endpoints with inference recommendations

With SageMaker AI inference recommendations, you learn when a change could improve the performance or lower the cost of your generative AI inference endpoints. Monitoring is on by default for eligible endpoints, with no setup required, and you can opt an endpoint out. SageMaker AI looks only at operational signals: latency, GPU utilization, and the endpoint's serving configuration. SageMaker AI doesn't collect the requests and responses that your endpoint serves, and monitoring has no additional cost.

Inference recommendations follow a simple loop:

1. **Observe** – SageMaker AI tracks the latency and hardware utilization of eligible endpoints.

1. **Notify** – when there is something worth acting on, you receive a notification through AWS Health that explains what was observed, why it matters, and a recommended next step.

1. **Recommend** – from the notification, you open the SageMaker AI agentic experience in Amazon SageMaker Studio, filled in with the endpoint and its recent traffic, and benchmark alternatives on separate compute. For more information, see [Optimized generative AI inference recommendations](generative-ai-inference-recommendations.md).

1. **Decide** – you compare response time, throughput, and cost side by side. Your endpoint doesn't change until you apply a result.

## Eligible endpoints
<a name="realtime-endpoints-improvement-notifications-scope"></a>

Monitoring covers real-time endpoints, and inference components on real-time endpoints, that run on GPU instances and serve a model with the vLLM inference engine. This includes the SageMaker AI Large Model Inference (LMI) container. Endpoints on CPU instances, or on AWS Inferentia or AWS Trainium instances, aren't monitored. For the telemetry that SageMaker AI collects from these endpoints, see [Telemetry from inference endpoints](data-privacy.md#data-privacy-inference).

## Findings
<a name="realtime-endpoints-improvement-notifications-findings"></a>

The following table summarizes what triggers each finding and what a benchmark tests when you choose to run one.


| Finding | What triggers it | What a benchmark tests | 
| --- | --- | --- | 
| Latency drift | The endpoint's median (p50) time to first token or median end-to-end latency rises compared with the previous week. The comparison is against the endpoint's own history, so you don't set a threshold. | Tensor parallelism settings, and other instance types or sizes. | 
| Underutilized GPUs | GPU utilization stays well below capacity over the week. | Cheaper instance types and smaller sizes at your observed peak traffic. | 
| Speculative decoding not enabled | Your model and serving container support speculative decoding, and it isn't enabled. For more information, see [Speculative decoding](model-optimize.md#speculative-decoding). | Your current configuration compared with speculative decoding enabled. | 
| Stale serving container | A newer version of the endpoint's serving container is available, with performance improvements, security patches for critical and high-severity CVEs, or both. | Your current container compared with the updated container. | 
| Untuned GPU kernels | The endpoint's GPU kernel configuration isn't tuned for its model and hardware, and SageMaker AI has a tuned configuration. | Default kernels compared with tuned kernels. | 

## Understanding a notification
<a name="realtime-endpoints-improvement-notifications-receive"></a>

SageMaker AI sends findings through AWS Health. One notification per endpoint covers all of that endpoint's findings. You receive it in AWS Health in the console and by email, with the subject `[Action May be Required] SageMaker AI inference improvements for the {{endpoint-name}} endpoint`. Each notification has the same structure:
+ **Endpoint** – the endpoint that the findings apply to.
+ **What we noticed** – the observation, with any estimate labeled as an estimate.
+ **Why it matters** – the impact on latency, capacity, or cost.
+ **Recommended action** – what to benchmark, and how to start.

A notification reports observations. No benchmark has run at this point.

Notifications are Region specific, so you see an endpoint's findings when you're signed in to that endpoint's Region.

Each notification is also an AWS Health event in Amazon EventBridge, with the event type code `AWS_SAGEMAKER_INFERENCE_OPTIMIZATION_RECOMMENDATION`. To act on these events automatically, for example to open a ticket in your own system, create an EventBridge rule with the following JSON event pattern.

```json
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": {
    "eventTypeCode": ["AWS_SAGEMAKER_INFERENCE_OPTIMIZATION_RECOMMENDATION"]
  }
}
```

For more information, see [Monitoring AWS Health events with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) in the *AWS Health User Guide*.

## Acting on a notification
<a name="realtime-endpoints-improvement-notifications-act"></a>

To act on a finding, you need the following:
+ Access to the [AWS Health Dashboard](https://health.aws.amazon.com/health/home) and the [AWS User Notifications console](https://console.aws.amazon.com/notifications/).
+ A domain in [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html), and IAM permissions to run [Optimized generative AI inference recommendations](generative-ai-inference-recommendations.md) and update endpoints.
+ Enough service quota for the benchmark instances that you want to test.

**To go from a notification to a decision**

1. Open the AWS User Notifications console, and then open the notification.

1. Choose **Recommended actions**. This opens the SageMaker AI agentic experience in Studio with the endpoint and its recent traffic filled in.

1. Run [Optimized generative AI inference recommendations](generative-ai-inference-recommendations.md) to benchmark your current configuration against alternatives on separate compute. Your endpoint keeps serving as it does today.

1. Compare the options side by side on response time, throughput, and cost per million tokens.

1. (Optional) Apply the result to one production variant.

Before you apply a result, review the configuration difference and the benchmarked results. Apply the change to one production variant first, and keep the current configuration available for rollback. Keeping your current configuration is a normal outcome. Nothing deploys automatically. Benchmarks incur standard SageMaker AI charges, or use your ML reservation if you have one. For more information about inference recommendations, see [Optimized generative AI inference recommendations](generative-ai-inference-recommendations.md).

## Managing notifications or opting out of monitoring
<a name="realtime-endpoints-improvement-notifications-stop"></a>
+ To manage how you receive notifications, use the AWS User Notifications console.
+ To opt an endpoint out of monitoring, set the `OPT_OUT_TRACKING` environment variable, with any value, on a container of the model. SageMaker AI then collects no monitoring telemetry for the endpoint, so it also sends no notifications for it. For instructions on opting out, see [Opt out of telemetry from an inference endpoint](data-privacy.md#data-privacy-inference-opt-out).

**Note**  
Opting out with `OPT_OUT_TRACKING` isn't available yet for endpoints that host inference components. To opt an inference component endpoint out of monitoring, contact [AWS Support](https://console.aws.amazon.com/support/).