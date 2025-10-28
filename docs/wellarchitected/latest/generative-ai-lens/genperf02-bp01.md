# GENPERF02-BP01 Load test model endpoints

Foundation model performance is dependent on several factors,
including the hosting architecture and the average prompt
complexity. Load testing model endpoints using the average
complexity prompt helps to determine a baseline level of
performance, which informs future architecture decisions and ongoing
operational considerations.

**Desired outcome:** When
implemented, this best practice helps you identify the average
performance efficiency of a foundation model. This baseline can be
used to inform future decisions and determine how close the high
watermark of demand is to the upper-limit of the model's
performance.

**Benefits of establishing this best
practice:** [Experiment
more often](../framework/rel-dp.md "../framework/rel-dp.md") - Load testing model endpoints assists in the
ongoing maintenance and performance of foundation models at scale.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Every workload has unique performance requirements, such as low
latency, rapid scalability, or intermittent demand. Clearly define
the performance needs of your generative AI application. Develop a
test suite designed to simulate the heaviest expected load to your
application before anticipated performance degradation. Test
models and model endpoints against these requirements to determine
if additional architectural considerations are required to bridge
the gap between performance needs and observed performance
results. Consider using a ground truth data set to standardize
results across multiple models.

On Amazon Bedrock, review the published metrics for inference
latency and throughput before testing. These details may assist in
the model selection process. If a model has throughput
limitations, consider introducing provisioned throughput
capabilities to your endpoint. Alternatively, if model inference
latency is high, consider introducing prompt caching.

On Amazon SageMaker AI, inference endpoints should be tested with
respect to the inference endpoint instance type and size. Load
test inference endpoints as you might load test other
high-performance compute options. Depending on the model being
hosted, there may be an opportunity to modify additional inference
parameters. Research the inference options available to the model
you are hosting, and test the effect of different inference
parameters on your performance criteria. For SageMaker AI hosted
models, you can optimize memory, I/O, and computation by selecting
an appropriate serving stack and instance type. SageMaker AI large
model inference (LMI) deep learning containers provide options for
request batching, quantization options, and tensor parallelism.
You can use these capabilities to balance performance with other
workload metrics like complexity and cost.

For low latency and real-time application use cases, consider
caching common prompts using Amazon Bedrock prompt caching. When
combined with application improvements, prompt caching can improve
the latency and performance of model endpoints by reducing the
load on those endpoints for common prompts. Implementing streaming
responses can also improve a user's perceived latency on responses
not in the cache.

Consider the usage requirements of some generative AI workloads,
batch inference may be a potent alternative to traditional
inference requests for model endpoints. Batch inference is more
efficient for processing large volumes of prompts, especially when
evaluating, experimenting, or performing offline analysis on
foundation models. It allows you to aggregate responses and
analyze them in batches. If higher latency is acceptable in your
scenario, batch inference may be a better choice than real-time
invoke model. Batch processing can introduce additional latency
compared to real-time inference.

### Implementation steps

1. Develop a load testing harness which prompts a foundation
   model at configurable rates.
2. Collect performance information from the model from the load
   test.
3. Determine if the model's performance is acceptable and make
   the appropriate infrastructure changes.

## Resources

**Related practices:**

- [PERF05-BP04](../performance-efficiency-pillar/perf_process_culture_load_test.md "../performance-efficiency-pillar/perf_process_culture_load_test.md")

**Related guides, videos, and documentation:**

- [Monitor
  the health and performance of Amazon Bedrock](../../../bedrock/latest/userguide/monitoring.md "../../../bedrock/latest/userguide/monitoring.md")

**Related examples:**

- [Load
  testing applications](../../../prescriptive-guidance/latest/load-testing/welcome.md "../../../prescriptive-guidance/latest/load-testing/welcome.md")
- [Amazon Bedrock model evaluation is now generally available](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/ "https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/")
- [Best
  practices for load testing Amazon SageMaker AI real-time
  inference endpoints](https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/")

**Related tools:**

- [Bedrock
  Latency Benchmarking](https://github.com/gilinachum/bedrock-latency "https://github.com/gilinachum/bedrock-latency")
