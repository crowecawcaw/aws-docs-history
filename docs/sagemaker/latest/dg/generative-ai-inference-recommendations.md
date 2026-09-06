

# Optimized generative AI inference recommendations
<a name="generative-ai-inference-recommendations"></a>

Amazon SageMaker AI now supports inference recommendations, a capability that eliminates manual optimization and benchmarking to deliver optimal inference performance. Instead of manually testing combinations of GPU instance types, serving containers, parallelism strategies, and optimization techniques, you provide your model and workload requirements, and SageMaker AI returns validated, deployment-ready configurations with real performance metrics.

Inference recommendations analyzes your model's architecture, narrows the configuration space, and applies goal-aligned optimizations such as speculative decoding for throughput and kernel tuning for latency. By evaluating multiple instance types, you can select the most price-performant option for your workload. It benchmarks each configuration on real GPU infrastructure, so you can deploy with confidence and right-size your inference spend.

## How it works
<a name="generative-ai-inference-recommendations-how-it-works"></a>

Getting started with inference recommendations is straightforward, whether through SageMaker AI Studio or the SageMaker AI APIs. The following steps describe the workflow.

1. **Prepare your model.** Point to model artifacts in Amazon S3 or the SageMaker AI Model Registry. Inference recommendations supports HuggingFace checkpoint format with SafeTensor weights, including base models and custom or fine-tuned models.

1. **Define your workload.** Describe your expected traffic patterns, including input and output token distributions and concurrency levels. You can use inline specifications or a representative dataset from Amazon S3.

1. **Set your goal.** Choose a single performance objective: optimize for cost, minimize latency, or maximize throughput. Select up to three instance types to compare.

1. **Review results.** SageMaker AI returns validated configurations with real performance metrics: Time to First Token (TTFT), inter-token latency, request latency at P50/P90/P99, throughput, and cost per configuration. Each configuration is deployment-ready.

1. **Deploy.** Deploy the chosen configuration to a SageMaker AI inference endpoint with a single action from SageMaker AI Studio, or programmatically through the API.

You can also benchmark existing production endpoints to validate current performance or compare against new configurations.

## Use cases
<a name="generative-ai-inference-recommendations-use-cases"></a>

The following are common use cases for inference recommendations.
+ **Pre-deployment validation.** Optimize and benchmark a new model before committing to a production deployment. Validate how the model performs before you invest in scaling it.
+ **Regression testing after updates.** Validate performance after a container update, framework upgrade, or serving library release. Confirm that your configuration is still optimal before pushing to production.
+ **Right-sizing when conditions change.** When traffic patterns shift or new instance types become available, re-run inference recommendations in hours rather than restarting a weeks-long manual process.
+ **Model comparison.** Compare the performance and cost of different model variants across instance types to make an informed selection before production deployment.
+ **Cost optimization.** Benchmark existing production endpoints to identify over-provisioned infrastructure. Use the results to right-size and reduce recurring inference spend.

## Pricing
<a name="generative-ai-inference-recommendations-pricing"></a>

Inference recommendations has no additional service fee. You can use existing ML Reservations (Flexible Training Plans) at no additional compute cost, or use on-demand compute that is provisioned automatically.

## Supported Regions
<a name="generative-ai-inference-recommendations-regions"></a>

Inference recommendations is available in the following AWS Regions:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Asia Pacific (Singapore)
+ Asia Pacific (Tokyo)
+ Europe (Frankfurt)
+ Europe (Ireland)