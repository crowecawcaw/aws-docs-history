# GENPERF01-BP01 Define a ground truth data set of prompts and

responses

_Ground truth data_ facilitates model testing for
use case specific scenarios and should be developed and curated for
generative AI workloads.

**Desired outcome:** When
implemented, this best practice improves the performance of model
selection by measuring a model's performance on task specific
prompt-response pairs.

**Benefits of establishing this best
practice:** [Experiment
more often](../framework/rel-dp.md "../framework/rel-dp.md") - Ground truth testing facilitates rapid
experimentation for models on tasks specific to your workload's
unique requirements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

_Ground truth data_, also known as a
_golden dataset_, is data classified to be
true. Ground truth data is vital for the efficient testing of
data-driven workloads, particularly generative AI workloads.
Customers should develop ground truth data for their generative AI
applications to facilitate the testing process.

Ground truth data for generative AI traditionally consists of a
prompt and a desirable response to said prompt. For prompts that
supplement responses with data from external sources, customers
can extend the ground truth data to include source documentation
or other useful metadata. At a minimum, a prompt and a
sufficiently acceptable response are required for a usable ground
truth data set.

Ground truth data should be considered a living artifact, one that
changes and extends based on the use cases being tested. For
generative AI workloads, ground truth prompts should be clear and
succinct, but not repeated. Ground truth responses should
similarly be clear and succinct, and responses can be repeated if
a response addresses multiple prompts. When developing a ground
truth data set, don't be overly concerned with slight differences
in prompts that essentially ask a model to perform the same task.
Prompts in the ground truth data set should be specific to the
kinds of tasks you expect a model to solve.

### Implementation steps

1. Define a series of prompts and their expected responses.
   Consider using Amazon SageMaker Ground Truth or similar to
   scale the curation of this dataset.
2. Create a nested dictionary of data.
   - The first several layers are organizational, referring
     to abstractions like language, business domain, or use
     case.
   - The last layer includes the prompt-response pairs, where
     the prompt is the key and the expected response is the
     value.
   - Store the dictionary in object-storage or a database.

3. Define test scenarios corresponding to your golden dataset.
4. Develop a testing harness that can automatically test models
   as they are made available using the ground truth data.

## Resources

**Related practices:**

- [PERF05-BP01](../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md "../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md")
- [PERF05-BP03](../performance-efficiency-pillar/perf_process_culture_workload_performance.md "../performance-efficiency-pillar/perf_process_culture_workload_performance.md")

**Related guides, videos, and documentation:**

- [Amazon SageMaker AI JumpStart Foundation Models](../../../sagemaker/latest/dg/jumpstart-foundation-models.md "../../../sagemaker/latest/dg/jumpstart-foundation-models.md")
- [Automate
  data labeling](../../../sagemaker/latest/dg/sms-automated-labeling.md "../../../sagemaker/latest/dg/sms-automated-labeling.md")

**Related examples:**

- [High-quality
  human feedback for your generative AI applications from Amazon SageMaker Ground Truth Plus](https://aws.amazon.com/blogs/machine-learning/high-quality-human-feedback-for-your-generative-ai-applications-from-amazon-sagemaker-ground-truth-plus/ "https://aws.amazon.com/blogs/machine-learning/high-quality-human-feedback-for-your-generative-ai-applications-from-amazon-sagemaker-ground-truth-plus/")
