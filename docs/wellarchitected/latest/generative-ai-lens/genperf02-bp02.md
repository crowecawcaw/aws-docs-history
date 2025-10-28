# GENPERF02-BP02 Optimize inference parameters to improve

response quality

Foundation model performance can be affected by inference
hyperparameters. Optimize inference hyperparameters for your use
case to help maintain consistent performance and control the
non-deterministic nature of foundation models.

**Desired outcome:** When
implemented, you can reduce the variability of foundation models by
controlling hyperparameters and identifying optimum ranges and
values for a use case.

**Benefits of establishing this best
practice:** [Experiment
more often](../framework/rel-dp.md "../framework/rel-dp.md") - Optimize hyperparameters through experimentation
to discern the best range and values for a use case.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Every workload has unique requirements for response quality.
Response quality can be modified by configuring inference
parameters. Inference parameters vary from model to model. For
example, in text-based scenarios, the parameters
`temperature`, `p`, and `k` are common.

When determining the inference parameters required for your
workload, consider a structured approach to determining the best
range of values for a hyperparameter. An example of this approach
is testing the highest and lowest values for each hyperparameter
and comparing the results of each test to your ground truth data.
The configurations that generate responses most appropriate for
the ground truth prompt should be accepted and iterated on. You
might then increment or decrement a hyperparameter by half its
possible range of values to see the effect this has on the model's
response. Continue in this way until hyperparameter changes are
negligible.

To automate this testing, you might leverage the LLM-as-a-judge
pattern. The LLM-as-a-judge pattern uses a separate LLM to
evaluate the performance of a model in generating a response which
is appropriate for the given prompt. This could be favorable for a
large set of ground truth prompts or in the case where you lack
sufficient resources to facilitate a full human-in-the-loop
testing process.

These are some recommendations for optimizing inference
parameters. The majority of use cases don't need extensive testing
of inference parameters and should take small number of iterations
to identify acceptable ranges for these parameters.

### Implementation steps

1. Identify a subset of ground truth data to use for
   hyperparameter optimization.
2. Leverage a search paradigm like grid search or bayesian
   search to identify the best range of values for
   hyperparameters.
3. Use these values or ranges to encourage consistent
   high-performance of your applications.

## Resources

**Related practices:**

- [PERF05-BP01](../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md "../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md")

**Related guides, videos, and documentation:**

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
