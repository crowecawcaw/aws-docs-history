# MLOE-02: Discuss and agree on the level of model explainability

Discuss and agree with the business stakeholders on the
acceptable level of model explainability required for the use
case. Use the agreed level as a metric for evaluations and
[tradeoff
analysis](../framework/ops_priorities_eval_tradeoffs.md "../framework/ops_priorities_eval_tradeoffs.md") across the ML lifecycle. Explainability can help
with understanding the cause of a prediction, auditing, and
meeting regulatory requirements. It can be useful for building
trust ensuring that the model is working as expected.

## Implementation plan

- **Understand business
  requirements** - The adoption of AI systems in
  regulated domains requires trust. This can be built by
  providing reliable explanations on the deployed
  predictions. Model explainability can be particularly
  important to reliability, safety, and compliance
  requirements. Use SageMaker AI Clarify to create
  explainability reports and detect dataset or model bias.
- **Agree on an acceptable level of
  explainability** - Communicate with stakeholders
  across the project about the level of explainability that
  is required for the project. Agree to a level that helps
  you meet business requirements.
- **Choose good baselines –**
  Shapley values determine the contribution that each
  feature made to model prediction.
  [SHAP
  Baselines for Explainability](../../../sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.md "../../../sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.md") are crucial to
  building fair and explainable ML models. Choose the
  baseline carefully since model explanations are based on
  deviations from the baseline (the baseline, in the ML
  context, is a hypothetical instance). You can choose a
  baseline with a ‘low information content’ (e.g., by
  constructing an average instance from the training dataset
  by taking either the median or average for numerical
  features and the mode for categorical features) or a
  baseline with ‘high information content’ (e.g., an
  instance which represents a particular class of instances
  that you are interested in). SageMaker AI Clarify, which uses
  [Shapley
  Additive exPlanations (SHAP)](../../../sagemaker/latest/dg/clarify-shapley-values.md "../../../sagemaker/latest/dg/clarify-shapley-values.md"), calculates baselines
  automatically in the input dataset by using clustering
  methods such as K-means or K-prototypes.  For more on SHAP
  baselines and parameters, please see the documents listed
  below.

## Documents

- [Fairness, model explainability and bias detection with SageMaker Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [SHAP
  Baselines](../../../sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.md "../../../sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.md")
