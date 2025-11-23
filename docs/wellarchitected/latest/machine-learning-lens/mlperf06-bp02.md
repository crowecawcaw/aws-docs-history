# MLPERF06-BP02 Evaluate model explainability

Model explainability allows you to understand and interpret how your
machine learning models arrive at their decisions. By evaluating
model explainability, you gain insights into the factors that
influence predictions to build trustworthy AI systems that meet
business requirements and regulatory standards.

**Desired outcome:** You can
demonstrate why your machine learning models make predictions, which
enables you to build trust with stakeholders, adhere to regulatory
requirements, and identify potential biases in model outcomes. You
have the tools to balance model complexity with explainability based
on your business needs and can produce documentation that satisfies
governance requirements.

**Common anti-patterns:**

- Treating machine learning models as unknown without
  understanding their decision-making process.
- Ignoring explainability requirements until after model
  deployment.
- Prioritizing model performance metrics over interpretability
  when business or regulations requires explainability.
- Failing to document model explanations for regulatory adherence.
- Using complex models when simpler, more interpretable
  alternatives would meet business requirements.

**Benefits of establishing this best
practice:**

- Increased trust from stakeholders and end-users in AI systems.
- Improves adherence with regulations requiring transparent AI
  decision-making.
- Ability to detect and mitigate biases in model predictions.
- Enhanced model debugging and performance improvement.
- Better alignment between model behavior and business objectives.
- More effective model governance and risk management.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model explainability is a critical aspect of responsible AI
development. When you evaluate explainability, you assess how
transparently your machine learning models make decisions and
whether those decisions can be explained to stakeholders,
regulators, and end-users. This transparency is particularly
important in regulated industries and for applications where
decisions impact individuals.

Avoid treating machine learning models as opaque without
understanding their decision-making process. Many organizations
ignore explainability requirements until after model deployment,
prioritize model performance metrics over interpretability when
business or regulatory requirements demand explainability, and
fail to document model explanations for regulatory adherence.

The trade-off between model complexity and explainability is a key
consideration. Complex models like deep neural networks may
deliver higher accuracy but are often harder to interpret. Simpler
models like decision trees or linear regression provide more
straightforward explanations but might sacrifice some performance.
Your choice should be guided by your business context, including
regulatory requirements and the importance of building trust with
end-users.

For example, a credit approval system may require clear
explanations for why applications are denied, while a
manufacturing quality control system might prioritize accuracy
over explainability. By evaluating these requirements early, you
can select appropriate modeling approaches and develop the right
metrics for assessing both performance and interpretability.

### Implementation steps

1. **Assess explainability
   requirements**. Begin by understanding the business
   and compliance-aligned needs that drive your explainability
   requirements. Consider regulatory constraints (like GDPR,
   which includes a right to explanation), business
   transparency goals, and stakeholder expectations. Document
   these requirements clearly and prioritize them based on
   their importance to your use case.
2. **Select appropriate model
   types**. Choose model architectures that align with
   your explainability needs. If high explainability is
   required, consider inherently interpretable models like
   decision trees, rule-based systems, or linear models. For
   applications where performance takes priority, more complex
   models with post-hoc explanation techniques may be
   appropriate.
3. **Implement Amazon SageMaker AI
   Clarify**.
   [Amazon SageMaker AI Clarify](../../../sagemaker/latest/dg/clarify-model-explainability.md "../../../sagemaker/latest/dg/clarify-model-explainability.md") provides tools to explain model
   predictions using feature attribution methods. It can
   identify which features contribute most to a prediction,
   enabling you to understand and communicate model behavior.
   SageMaker AI Clarify supports various model types and
   integrates seamlessly with the SageMaker AI environment.
4. **Apply feature attribution
   techniques**. Use feature attribution methods like
   [SHAP
   (SHapley Additive exPlanations) values](../../../sagemaker/latest/dg/clarify-shapley-values.md "../../../sagemaker/latest/dg/clarify-shapley-values.md") through
   SageMaker AI Clarify to quantify the contribution of each
   feature to individual predictions. These techniques explain
   both global model behavior (which features are most
   important overall) and local explanations (why a prediction
   was made).
5. **Establish explainability
   metrics**. Define quantitative metrics to assess
   model explainability, such as feature importance stability,
   explanation fidelity, or consistency. Use these metrics to
   objectively evaluate explainability alongside traditional
   performance metrics like accuracy or F1 score. Include these
   metrics in your model evaluation framework and monitoring
   systems.
6. **Create model
   documentation**. Develop comprehensive
   documentation that describes how your model works, what
   features influence its decisions, and how explanations are
   generated. This documentation should be understandable by
   both technical and non-technical stakeholders. SageMaker AI
   Clarify can generate reports that contribute to model
   governance documentation.
7. **Implement bias detection**.
   Use
   [SageMaker AI
   Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md") to detect potential bias in your models
   during development and production. Configure the appropriate
   bias metrics based on your use case and sensitive
   attributes. Regularly assess these metrics to verify that
   your model remains fair across different demographic groups.
8. **Set up continuous
   monitoring**. Configure SageMaker AI Clarify to
   monitor production inferences for bias or feature
   attribution drift. This allows you to detect when model
   explanations change over time, which might indicate problems
   with the model or changes in the underlying data. Establish
   alerts for shifts in explanations or bias metrics.
9. **Integrate human review
   processes**. For high-stakes decisions, implement
   human-in-the-loop review of model explanations using Amazon SageMaker AI Clarify in combination with
   [Amazon
   Augmented AI (A2I)](https://aws.amazon.com/augmented-ai/ "https://aws.amazon.com/augmented-ai/"). This provides an additional layer
   of oversight and can build confidence in the model's
   decisions.

## Resources

**Related documents:**

- [Model
  Explainability](../../../sagemaker/latest/dg/clarify-model-explainability.md "../../../sagemaker/latest/dg/clarify-model-explainability.md")
- [Feature
  Attributions that Use Shapley Values](../../../sagemaker/latest/dg/clarify-shapley-values.md "../../../sagemaker/latest/dg/clarify-shapley-values.md")
- [Run
  SageMaker AI Clarify Processing Jobs for Bias Analysis and
  Explainability](../../../sagemaker/latest/dg/clarify-processing-job-run.md "../../../sagemaker/latest/dg/clarify-processing-job-run.md")
- [Data
  and model quality monitoring with SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [ML
  model explainability with Amazon SageMaker AI Clarify and the
  SKLearn pre-built container](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/ "https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/")
- [Human-in-the-loop
  review of model explanations with Amazon SageMaker AI Clarify and
  Amazon A2I](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/")

**Related examples:**

- [Fairness
  and Explainability with SageMaker AI Clarify](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-experiments/sagemaker_clarify_integration/tracking_bias_explainability.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-experiments/sagemaker_clarify_integration/tracking_bias_explainability.html")
- [Explainability
  with Amazon SageMaker AI Debugger](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/xgboost_census_explanations/xgboost-census-debugger-rules.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/xgboost_census_explanations/xgboost-census-debugger-rules.html")
- [Amazon SageMaker AI Clarify Processing GitHub Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify")
