# Clarify availability change

###### Note

Amazon SageMaker Clarify is no longer open to new customers.
Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
Clarify, but we do not plan to introduce new features.

## AWS-published monitoring solutions, standardized bias metrics, SHAP, and Amazon Bedrock Evaluations

The combination of the AWS-published open-source SageMaker AI monitoring solutions,
base computation of the standardized bias metrics Clarify reports, the SHAP library that
SageMaker Clarify itself is built on, [Amazon SageMaker AI
MLflow](mlflow.md "mlflow.md"), [Amazon
CloudWatch](../../../cloudwatch.md "../../../cloudwatch.md"), [Amazon QuickSight](../../../quick/latest/userguide/quick-sight-getting-started.md "../../../quick/latest/userguide/quick-sight-getting-started.md"), and [Amazon Bedrock
Evaluations](../../../bedrock/latest/userguide/evaluation.md "../../../bedrock/latest/userguide/evaluation.md") serves as a replacement for Amazon SageMaker
Clarify. This guidance provides the following:

- **AWS-published reference solutions are the
  foundation.** The [open-source Amazon SageMaker AI monitoring solutions](https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring "https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring") in the
  `aws-samples` GitHub organization are production-tested reference architectures
  built entirely on AWS managed services (Amazon SageMaker AI, SageMaker AI MLflow,
  Amazon Athena, AWS Lambda, Amazon EventBridge, Amazon SQS, Amazon SNS, Amazon
  QuickSight). They run inside your own AWS account and operationalize bias and
  explainability analysis as part of an end-to-end, governed pipeline rather than as ad hoc
  scripts. These are the same reference solutions used in the [SageMaker Model Monitor migration guidance](https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring "https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring").
- **The bias metrics are standardized arithmetic, not a library
  dependency.** Clarify's pre-training and post-training bias metrics (DPL, DPPL,
  DI, CI, and related measures) are published, industry-standard formulas computed from
  label counts and confusion-matrix values. You reproduce them with pandas and scikit-learn,
  code you own, test, and version inside your own pipeline.
- **SHAP is the same engine Clarify uses.** SageMaker
  Clarify computes feature attribution using the SHAP library internally (see the [Clarify SHAP values
  documentation](clarify-shapley-values.md "clarify-shapley-values.md")). Adopting SHAP directly produces Shapley-value
  attributions.
- **Amazon Bedrock Evaluations for foundation models
  only.** Amazon Bedrock Evaluations and Amazon Bedrock Guardrails are the
  AWS-managed path for LLM and generative AI evaluation. They replace Clarify's
  foundation model evaluation (FMEval) capability. They are not a replacement for predictive
  (tabular/classical ML) bias detection or explainability.

## Removing Clarify

### Discontinue Clarify processing jobs for new analysis

If your workflow includes running SageMaker Clarify Processing Jobs using the
`SageMakerClarifyProcessor` class, the `clarify.BiasConfig` /
`clarify.SHAPConfig` configurations, or the `run_bias()` /
`run_explainability()` methods from the SageMaker Python SDK, transition to the
alternatives described in the Configuring Replacements section below.

### Delete or retain Clarify output artifacts (optional)

Clarify Processing Jobs store output artifacts in Amazon S3:

- **Bias analysis reports:**
  `analysis.json`, with pre-training and post-training bias metrics
- **SHAP explanations:**
  `explanations_shap/out.csv`, with per-instance local SHAP values
- **Global SHAP values:** Aggregated feature importance
  scores
- **Partial dependence plots (PDPs):** Feature effect
  visualizations
- **Constraints files:** Used by Model Monitor for bias
  drift and feature attribution drift baselines

If you need to retain these for compliance, regulatory audit trails, or historical
reference, leave them in S3 or archive to S3 Glacier. If they are no longer needed, delete
the S3 prefix.

### Remove Clarify from SageMaker Pipelines (if used)

If you have SageMaker Pipelines with `ClarifyCheckStep` or
`ProcessingStep` steps that invoke Clarify, replace them with a
`ProcessingStep` that runs the standardized metric computation and SHAP,
following the same pattern the AWS-published reference solutions use inside SageMaker
Pipelines (see Configuring Replacements below).

## Configuring replacements

The replacement path computes the standardized bias metrics directly with pandas and
scikit-learn, and computes feature attribution with SHAP (the same engine Clarify uses). You
run these inside the AWS-published reference solutions and SageMaker Pipelines, logging
results to a SageMaker AI MLflow App so your bias and explainability results carry the same
lineage, versioning, and governance as your training runs.

### Replacing pre-training and post-training bias detection

Clarify's pre-training metrics are published, standardized formulas based on label
counts and class proportions. Computing them directly keeps the bias check simple, owned and
testable by your team, and consistent with what the AWS-published reference solutions do
inside their monitoring jobs.

Refer to the [Clarify pre-training bias
metrics reference](clarify-measure-data-bias.md "clarify-measure-data-bias.md") for the exact formula behind each metric, so your
implementation matches Clarify's output.

Clarify's post-training metrics are standardized functions of per-group
confusion-matrix counts. Computing them directly from predictions and ground truth keeps the
check simple and owned by your team, and it matches the per-segment approach the
AWS-published reference solutions use for bias drift. Log the per-segment results to a
SageMaker AI MLflow App for governance and trend tracking.

Refer to the [Clarify post-training
bias metrics reference](clarify-measure-post-training-bias.md "clarify-measure-post-training-bias.md") for the exact formula behind each metric.

### Replacing model explainability (SHAP feature attribution)

The SHAP library is the same engine that powers SageMaker Clarify's explainability.
Using it directly gives you more flexibility:

```
pip install shap
```

For production use, the AWS-published reference solutions include a
`6_shap_explainability.ipynb` notebook that generates global feature importance,
individual prediction explanations, and feature interaction analysis for a deployed model,
logging the results to a SageMaker AI MLflow App.

Refer to [SHAP
documentation](https://shap.readthedocs.io/en/latest/ "https://shap.readthedocs.io/en/latest/") for the API reference.

### Replacing bias drift and feature attribution drift monitoring

This approach operationalizes the same standardized metrics (directly computed fairness
metrics and SHAP feature importance) on a schedule, with governance, lineage, and alerting,
using the [Amazon SageMaker AI monitoring solutions](https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring "https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring"). It uses the same EventBridge + Lambda

- Athena (Iceberg) + MLflow + SNS + QuickSight pattern that the Model Monitor migration
  guidance uses for data and model quality drift, so bias drift and feature attribution drift
  become additional metrics in the same governance pipeline rather than a separate
  system.

### Replacing foundation model (LLM) evaluation

#### Option 1: fmeval library (recommended for SageMaker-hosted models)

The `fmeval` library is the same evaluation engine Clarify's foundation
model evaluation is built on, and it can be used independently of Clarify Processing
Jobs:

```
pip install fmeval
```

The `fmeval` library supports: text summarization, question answering,
classification, open-ended generation, factual knowledge, toxicity, robustness (semantic
perturbations), and prompt stereotyping evaluation. For ongoing, in-production LLM quality
monitoring on SageMaker endpoints, the AWS-published [LLM Inference Monitoring](https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring/sagemaker-endpoint-llm-monitoring "https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring/sagemaker-endpoint-llm-monitoring") and [LLM Quality Observability with Grafana](https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring/quality-monitoring-with-grafana "https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/monitoring/quality-monitoring-with-grafana") reference solutions run MLflow generative AI
evaluations (Safety, Relevance, Fluency, Guidelines, Coherence) using Amazon Bedrock
models.

Refer to [Use the
fmeval library to run an automatic evaluation](clarify-foundation-model-evaluate-auto-lib.md "clarify-foundation-model-evaluate-auto-lib.md") and [Track LLM model evaluation using Amazon SageMaker managed MLflow and FMEval](https://aws.amazon.com/blogs/machine-learning/track-llm-model-evaluation-using-amazon-sagemaker-managed-mlflow-and-fmeval/ "https://aws.amazon.com/blogs/machine-learning/track-llm-model-evaluation-using-amazon-sagemaker-managed-mlflow-and-fmeval/")
for detailed steps.

#### Option 2: Amazon Bedrock Evaluations (managed service)

Amazon Bedrock Evaluations provides a managed alternative for foundation model
evaluation without requiring Clarify Processing Jobs:

1. Open the **Amazon Bedrock console**.
2. Choose **Evaluations** from the left
   navigation.
3. Choose **Create evaluation job**.
4. Select evaluation type:

   - **Automatic evaluation**: Predefined algorithms
     for accuracy, robustness, toxicity
   - **Human evaluation**: Bring human workers for
     subjective quality assessment

5. Select models to evaluate (JumpStart models, Bedrock models, or custom
   endpoints).
6. Choose built-in datasets or upload custom prompt datasets.
7. Review evaluation results with comparative metrics across models.

Bedrock Evaluations supports evaluating models hosted on Bedrock, custom models, and
external models (including on-premises or multi-cloud deployments) as long as you provide
evaluation data in the required format.

Refer to [Evaluate
the performance of Amazon Bedrock resources](../../../bedrock/latest/userguide/evaluation.md "../../../bedrock/latest/userguide/evaluation.md") and [Evaluate models or RAG systems using Amazon Bedrock Evaluations](https://aws.amazon.com/blogs/machine-learning/evaluate-models-or-rag-systems-using-amazon-bedrock-evaluations-now-generally-available/ "https://aws.amazon.com/blogs/machine-learning/evaluate-models-or-rag-systems-using-amazon-bedrock-evaluations-now-generally-available/") for detailed
steps.

#### Option 3: Amazon Bedrock Guardrails (runtime safety)

For runtime content filtering (toxicity, PII, harmful content) that SageMaker Clarify
evaluates at assessment time, Amazon Bedrock Guardrails provides continuous runtime
protection for generative AI applications:

- **Content filters**: Block harmful, hateful, sexual,
  violent, or insulting content
- **Denied topics**: Prevent model responses on
  specific topics
- **Sensitive information filters**: Detect and redact
  PII (names, addresses, SSN, credit cards)
- **Contextual grounding checks**: Reduce
  hallucinations by grounding responses in source data
- **Automated Reasoning checks**: Validate factual
  accuracy using formal reasoning

Refer to [Detect and
filter harmful content by using Amazon Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") for detailed
steps.
