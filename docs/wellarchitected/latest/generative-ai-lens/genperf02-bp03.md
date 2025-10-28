# GENPERF02-BP03 Select and customize the appropriate model for

your use case

There are several industry-leading model providers, and each offers
different model families and sizes. When you select a model, choose
the appropriate model family and size for your use case to provide
consistent performance.

**Desired outcome:** When
implemented, this best practice helps you select a model for your
use case. You understand the reasons you chose your specific model,
and your chosen model provides solid performance and consistency
across your use case.

**Benefits of establishing this best
pracice:**

- [Experiment
  more often](../framework/rel-dp.md "../framework/rel-dp.md") - Optimize hyperparameters through experimentation
  to discern the best range and values for a use case.
- [Consider
  mechanical sympathy](../framework/perf-dp.md "../framework/perf-dp.md") - Not all foundation models are created
  equal, and some have significant advantages over others. Select the
  appropriate model for your use case by understanding how the models
  perform.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When selecting a model for a task, curate a suite of tests sourced
from your ground truth data set, and test model performance
against those prompt-response pairs. Consider testing across model
family or model size to surface candidate models. In addition to
testing ground truth data, consider testing challenging prompts or
prompts created deliberately with questionable or unconventional
intent. Evaluate the model's ability to respond to this class of
prompts before finally selecting a model. Consider using public
benchmarks and metrics to to augment your ground truth data.
Amazon Bedrock Evaluations or the open-source fmeval library test
foundation models against open-source performance evaluation data
sets and return results in the form of metrics like accuracy or
toxicity scores. To get a holistic perspective on model
performance, consider combining these approaches to inform model
selection.

Model routers are a powerful capability if your testing suite
yields inconclusive results. If a family of models performs well
against a prompt testing suite, but different model sizes within
that family show varied performance with no clear leader, use a
model router. Amazon Bedrock model routers forward prompts to the
best model based on the prompt itself. This technique simplifies
the model selection process but may not be appropriate for all use
cases.

In some scenarios, a specific model may be the most performant of
the options available, but there may be additional room for
improvement. In these scenarios, consider customizing the model.
Fine-tuning is a technique which improves a model's performance on
a specific set of tasks, which requires a small amount of labeled
data. Ground truth prompt-response data can be used to fine-tune a
model.

Additionally, models can be domain adapted through continuous
pre-training. Continuous pre-training requires more data than
fine-tuning, but the result is a model which is highly performant
on a domain of knowledge or tasks. These customization techniques
require significant investment, consider doing this after reducing
the number of candidate models through traditional model testing
techniques.

Model distillation is another customization option to consider.
Distillation generates synthetic data from a large foundation
model (teacher) and uses the synthetic data to fine-tune a smaller
model (student) for your specific use case. Model distillation
helps preserve performance and avoid scenarios where you might
over-provision a large model for a fine-tuned use case.

### Implementation steps

1. Select a range of models from different model providers.
2. Implement a load testing and hyperparameter testing harness
   for each of the models.
3. Test each model against the ground truth data set.
4. Select the model which performs best on average for the
   given use case.

## Resources

**Related practices:**

- [PERF02-BP01](../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md "../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md")

**Related guides, videos, and documentation:**

- [Supported
  foundation models in Amazon Bedrock](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md")
- [Optimize
  model inference for latency](../../../bedrock/latest/userguide/latency-optimized-inference.md "../../../bedrock/latest/userguide/latency-optimized-inference.md")

**Related examples:**

- [FMEval
  Library](https://github.com/aws/fmeval "https://github.com/aws/fmeval")
- [Evaluate,
  compare, and select the best foundation models for your use
  case in Amazon Bedrock (preview)](https://aws.amazon.com/blogs/aws/evaluate-compare-and-select-the-best-foundation-models-for-your-use-case-in-amazon-bedrock-preview/ "https://aws.amazon.com/blogs/aws/evaluate-compare-and-select-the-best-foundation-models-for-your-use-case-in-amazon-bedrock-preview/")
