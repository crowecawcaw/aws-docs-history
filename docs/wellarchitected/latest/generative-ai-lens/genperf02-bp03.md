# GENPERF02-BP03 Select and customize the appropriate model for

your use case

There are several industry-leading model providers, and each
offers different model families and sizes. When you select a
model, choose the appropriate model family and size for your use
case to provide consistent performance for your workload.

**Desired outcome:** When
implemented, this best practice helps you select the ideal model
for your use case. You understand the reasons a specific model
was chosen, and your chosen model provides robust performance
and consistency for your use case.

**Benefits of establishing this best
pracice:**

- [Experiment
  more often](../framework/rel-dp.md "../framework/rel-dp.md") - Identify the best model for your use case,
  developing a mechanism to update the appropriate model quickly.
- [Consider
  mechanical sympathy](../framework/perf-dp.md "../framework/perf-dp.md") - Not all foundation models are
  created equal, and some have significant advantages over others.
  Select the appropriate model for your use case by understanding
  how models perform on different tasks.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When selecting a model for a task, curate a suite of tests
sourced from your ground truth data set, and test model
performance against those prompt-response pairs. These tests
should emulate the specific task a model will be performing as
part of the use case, such as summarization or question
answering. Consider testing across model family or model size
to surface candidate models.

In addition to testing ground truth data, consider testing
challenging prompts or prompts created deliberately with
questionable or unconventional intent. Evaluate the model's
ability to respond to this class of prompts before finally
selecting a model. Consider using public benchmarks and
metrics to augment your ground truth data. Amazon Bedrock
Evaluations or the open-source fmeval library test foundation
models against open-source performance evaluation data sets
and return results in the form of metrics like accuracy or
toxicity scores.

Automate model selection using an intelligent model router.
Model routers, such as Amazon Bedrock's Prompt Routing
capability, are a powerful capability if your testing suite
yields inconclusive results within a model family. If a family
of models performs well against a prompt testing suite, but
different model sizes within that family show varied
performance with no clear leader, use a model router. Amazon
Bedrock model routers forward prompts to the best model based
on the prompt itself. This technique simplifies the model
selection process but may not be appropriate for all use
cases, especially for self-hosted models. For situations where
your workload is serviced primarily by self-hosted models,
carefully evaluate open-source prompt routing options or
develop your own.

In some scenarios, there may be room to improve a model which
outperforms alternatives through model customization. In these
scenarios, consider fine-tuning.
_Fine-tuning_ is a technique that improves
a model's performance on a specific set of tasks, which
requires a small amount of labeled data. Ground truth
prompt-response data can be used to fine-tune a model.

Additionally, models can be domain adapted through continuous
pre-training. _Continuous pre-training_
requires more data than fine-tuning, but the result is a model
which is highly performant on a domain of knowledge or tasks.
These customization techniques require significant investment,
consider doing this after reducing the number of candidate
models through traditional model testing techniques.

_Model distillation_ is another
customization option to consider. Distillation generates
synthetic data from a large foundation model (teacher) and
uses the synthetic data to fine-tune a smaller model (student)
for your specific use case. Model distillation helps preserve
performance and avoid scenarios where you might over-provision
a large model for a fine-tuned use case.

Track the dominant model family and size for each workload's
task. While your organization's AI usage policy may be too
broad, consider developing an AI usage document for each
workload to maintain a permanent understanding of your
organization's decisions around AI models for each workload.
As models continue to be developed with new capabilities,
reference this document to discern if it is appropriate to
re-test the current leading model for a workload.

### Implementation steps

1. Define minimum performance and response quality
   thresholds for your workload.
2. Select a range of models from different model providers.
3. Implement tests to facilitate rapid testing for each of
   the models.
4. Test each model against the ground truth data set, and
   identify which models surpass the minimum performance
   and response quality thresholds.
5. Select the model which performs best on average for the
   given use case.
6. Consider elevating model performance situationally, and
   use techniques like prompt routing or customization
   where appropriate.
7. Document results in an AI usage document to track model
   usage and encourage data-driven decision-making within
   the organization.

## Resources

**Related best practices:**

- [PERF02-BP01](../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md "../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md")
- [MLPER-06](../machine-learning-lens/mlper-06.md "../machine-learning-lens/mlper-06.md")
- [MLPER-16](../machine-learning-lens/mlper-16.md "../machine-learning-lens/mlper-16.md")

**Related documents:**

- [Understanding
  intelligent prompt routing in Amazon Bedrock](../../../bedrock/latest/userguide/prompt-routing.md "../../../bedrock/latest/userguide/prompt-routing.md")
- [Supported
  foundation models in Amazon Bedrock](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md")
- [Optimize
  model inference for latency](../../../bedrock/latest/userguide/latency-optimized-inference.md "../../../bedrock/latest/userguide/latency-optimized-inference.md")

**Related examples:**

- [Enhance
  conversational AI with advanced routing techniques with Amazon
  Bedrock](https://aws.amazon.com/blogs/machine-learning/enhance-conversational-ai-with-advanced-routing-techniques-with-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/enhance-conversational-ai-with-advanced-routing-techniques-with-amazon-bedrock/")
- [Multi-LLM
  routing strategies for generative AI applications on
  AWS](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/ "https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/")
- [FMEval
  Library](https://github.com/aws/fmeval "https://github.com/aws/fmeval")
- [Evaluate,
  compare, and select the best foundation models for your use
  case in Amazon Bedrock (preview)](https://aws.amazon.com/blogs/aws/evaluate-compare-and-select-the-best-foundation-models-for-your-use-case-in-amazon-bedrock-preview/ "https://aws.amazon.com/blogs/aws/evaluate-compare-and-select-the-best-foundation-models-for-your-use-case-in-amazon-bedrock-preview/")
