# GENPERF01-BP02 Collect performance metrics from generative AI

workloads

Foundation model performance on specific tasks is measured and
quantified in different ways depending on the desired outcome.
It is important to discern the performance of a model over time
when selecting foundation models for generative AI workloads by
identifying performance metrics and evaluating model
performance. This is true not just for model inference, but
model training and customization workloads as well.

**Desired outcome:** When
implemented, your organization improves its ability to evaluate
model performance against the identified performance metric.

**Benefits of establishing this best
practice:**
[Experiment
more often](../framework/rel-dp.md "../framework/rel-dp.md") - Testing model performance using quantifiable
evaluation metrics assists in the selection of foundation models
for generative AI workloads.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Traditional performance monitoring and optimization focus on
the efficiency of compute, network, memory and storage
resources. Generative AI workloads add new dimensions to the
performance considerations, particularly concerning response
quality. Inaccurate model responses or models responding in an
overly casual, dismissive, or even toxic manner may be
considered under-performing. Consult your organization's AI
policy for more details on what constitutes an
under-performing language model with respect to your use case.

Different use cases may have several relevant metrics for use
in evaluating model performance. Performance metrics for
inference workloads may capture model response latency or
throughput. Performance metrics for model customization or
training workloads are likely focused on model training times.
Ultimately, a model should respond with accurately, robustly,
and somewhat predictably. Capturing model performance against
these metrics and evaluating model performance against your
organization's AI performance requirements helps to provide
consistently high performing generative AI workloads.

Generative AI tasks should report metrics, telemetry and logs
to a centralized logging and monitoring solution such as
Amazon CloudWatch. By configuring Amazon CloudWatch or
similar, customers can collect performance metrics from model
endpoints hosted in Amazon SageMaker AI or generative AI
services like Amazon Q for Amazon Bedrock. These metrics can
be used to identify which models perform well against a
metric, and which need additional performance improvements.

Performance metrics may also be collected by applications and
services that interact with models. Collect metrics and
application traces pertaining to the flow of information
rather than a specific piece of the workflow. Work to
determine how your entire application performs when
interacting with generative AI solutions. This can help you
triage performance concerns faster and improve resolution
times.

Use internal golden datasets or external benchmarking datasets
to evaluate model performance on specific tasks. Consult model
cards to identify model strengths and weaknesses, evaluating
on selected datasets where appropriate. Benchmark custom
models on a suite of tests using internal and external data to
develop a well-rounded understanding of your model's
performance.

Note that a model may not excel at all tasks. Be judicious
when selecting a performance metric for your model, and
consult your organization's AI policy to identify which
performance metric to prioritize for your use case.

### Implementation steps

1. Identify the performance metrics to prioritize for your
   generative AI use case.
2. Develop a mechanism to capture the performance metrics.

- Implement a trace framework like
  [OpenLLMetry](https://github.com/traceloop/openllmetry "https://github.com/traceloop/openllmetry")
  to capture additional metrics.
- Capture metrics using Amazon CloudWatch or a similar
  centralized logging and monitoring solution.
- Use a benchmarking dataset within an evaluation
  framework such as
  [fmeval](https://github.com/aws/fmeval "https://github.com/aws/fmeval").

1. Establish reasonable performance thresholds and alert
   accordingly.

- Use Amazon CloudWatch alarms for production alerting on
  latency, throughput, or other traditional performance
  metrics.
- Incorporate regular benchmarking using internal golden
  datasets, and update the dataset as your customer's
  usage changes.
- Consult model cards for new models, and perform custom
  benchmarking of new models where appropriate.

1. Identify, capture, and log remediation actions in your
   organization's AI policy.

- For example, increased latency on self-hosted models may
  call for horizontal scaling to remediate the issue. Your
  organization's AI policy should define acceptable
  latency thresholds.
- For example, a model response which is identified as a
  hallucination may call for updates to a system prompt.
  Such an update should require testing against internal
  golden datasets to verify that system prompt changes do
  not adversely affect related prompt workflows.

1. Implement a centralized experiment tracking solution
   such as Amazon SageMaker AI with MLflow.

## Resources

**Related best practices:**

- [PERF05-BP01](../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md "../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md")
- [PERF05-BP02](../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md "../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md")
- [PERF05-BP03](../performance-efficiency-pillar/perf_process_culture_workload_performance.md "../performance-efficiency-pillar/perf_process_culture_workload_performance.md")
- [PERF05-BP05](../performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.md "../performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.md")
- [MLPER-03](../machine-learning-lens/mlper-03.md "../machine-learning-lens/mlper-03.md")
- [MLPER-06](../machine-learning-lens/mlper-06.md "../machine-learning-lens/mlper-06.md")
- [MLPER-07](../machine-learning-lens/mlper-07.md "../machine-learning-lens/mlper-07.md")
- [MLPER-09](../machine-learning-lens/mlper-09.md "../machine-learning-lens/mlper-09.md")
- [MLPER-15](../machine-learning-lens/mlper-15.md "../machine-learning-lens/mlper-15.md")
- [MLPER-16](../machine-learning-lens/mlper-16.md "../machine-learning-lens/mlper-16.md")

**Related documents:**

- [Monitor
  the health and performance of Amazon Bedrock](../../../bedrock/latest/userguide/monitoring.md "../../../bedrock/latest/userguide/monitoring.md")
- [Customize
  your workflow using the fmeval library](../../../sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-lib-custom.md "../../../sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-lib-custom.md")
- [Machine
  learning experiments using Amazon SageMaker AI with
  MLflow](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")

**Related examples:**

- [Track
  LLM model evaluation using Amazon SageMaker AI managed MLFlow and
  FMEval](https://aws.amazon.com/blogs/machine-learning/track-llm-model-evaluation-using-amazon-sagemaker-managed-mlflow-and-fmeval/ "https://aws.amazon.com/blogs/machine-learning/track-llm-model-evaluation-using-amazon-sagemaker-managed-mlflow-and-fmeval/")
- [Evaluate
  large language models for quality and responsibility](https://aws.amazon.com/blogs/machine-learning/evaluate-large-language-models-for-quality-and-responsibility/ "https://aws.amazon.com/blogs/machine-learning/evaluate-large-language-models-for-quality-and-responsibility/")
- [Monitoring
  Generative AI application using Amazon Bedrock and Amazon CloudWatch integration](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/ "https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/")

**Related tools:**

- [Traceloop
  OpenLLMetry](https://github.com/traceloop/openllmetry "https://github.com/traceloop/openllmetry")
- [AWS fmeval
  Model Evaluation Library](https://github.com/aws/fmeval "https://github.com/aws/fmeval")
- [AWS Samples fm-evaluation-at-scale](https://github.com/aws-samples/fm-evaluation-at-scale "https://github.com/aws-samples/fm-evaluation-at-scale")
