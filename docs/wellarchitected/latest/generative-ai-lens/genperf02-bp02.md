# GENPERF02-BP02 Optimize inference parameters to improve

response quality

Foundation model response quality can be affected by inference
hyperparameters. Optimize inference hyperparameters for your use
case to help maintain consistent response quality and to help control the
non-deterministic nature of foundation models.

**Desired outcome:** When
implemented, you can reduce the variability of foundation models by
setting hyperparameters and identifying optimum ranges and
values for a use case.

**Benefits of establishing this best
practice:** [Experiment
more often](../framework/rel-dp.md "../framework/rel-dp.md") - Optimize hyperparameters through experimentation
to discern the best range and values for a use case.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Workloads have unique requirements for response quality.
Response quality can be modified by configuring inference
parameters. Inference parameters vary from model to model. For
example, in text-based scenarios, the parameters
temperature, p, and
k are common.

Image, sound, and video models have other common
hyperparameters. Hyperparameter values and ranges can impact
the quality of a model's response, especially for different
task types. When determining the inference parameters required
for your workload, first identify the task for the model to
complete. Common tasks for textual responses include
summarization or question answering; image models may be asked
to generate or modify images. The task helps inform which
hyperparameters are most important in the context of your
workload.

Consider a structured approach to determining the best range
of values for a hyperparameter. An example is testing the
highest and lowest values for each hyperparameter and
comparing the results of each test to your golden data. The
configurations that generate responses most appropriate for
the ground truth prompt should be accepted and iterated on.
You might then adopt a Newtonian approach to finding the ideal
hyperparameter value by incrementing or decrementing a
hyperparameter by half to see the effect this has on the
model's response. Continue in this way until the affects of
the hyperparameter changes are negligible.

The _LLM-as-a-judge_ pattern is a powerful
technique for automating the iterative nature of
hyperparameter tuning. The LLM-as-a-judge pattern uses a
separate LLM to evaluate the performance of a model in
generating a response which is appropriate for the given
prompt. This could be favorable for a large set of ground
truth prompts or in the case where you lack sufficient
resources to facilitate a full human-in-the-loop testing
process. Consider adopting such a robust process for
hyperparameter optimization in the case where workload
requirements change regularly.

Recommendations for task-specific hyperparameter ranges could
be incorporated into an internal development guide for AI
workloads. Consider identifying recommended hyperparameter
ranges broken out by task into your organization's AI policy,
clearly defining the process for changing these ranges.

### Implementation steps

1. Identify the task required of the foundation model.
2. Identify the ground truth data to use for optimizing
   inference hyperparameters.
3. Select the most important hyperparameters for the task.
4. Use an optimization method to maximize response quality.
5. Use these values or ranges to encourage consistent
   high-performance of your applications.

## Resources

**Related best practices:**

- [PERF05-BP01](../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md "../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md")
- [MLPER-03](../machine-learning-lens/mlper-03.md "../machine-learning-lens/mlper-03.md")

**Related documents:**

- [Monitor
  the health and performance of Amazon Bedrock](../../../bedrock/latest/userguide/monitoring.md "../../../bedrock/latest/userguide/monitoring.md")
- [Influence
  response generation with inference parameters](../../../bedrock/latest/userguide/inference-parameters.md "../../../bedrock/latest/userguide/inference-parameters.md")
- [Optimize
  model inference for latency](../../../bedrock/latest/userguide/latency-optimized-inference.md "../../../bedrock/latest/userguide/latency-optimized-inference.md")

**Related examples:**

- [Load
  testing applications](../../../prescriptive-guidance/latest/load-testing/welcome.md "../../../prescriptive-guidance/latest/load-testing/welcome.md")
- [Amazon Bedrock model evaluation is now generally available](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/ "https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/")
- [Best
  practices for load testing Amazon SageMaker AI real-time
  inference endpoints](https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/")
