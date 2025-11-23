# MLOPS01-BP02 Discuss and agree on the level of model

explainability

Establish clear expectations with business stakeholders about the
level of model explainability needed for your machine learning use
case. Explainability provides an understanding of how and why a
model makes predictions, which builds trust, enables auditing, and
supports adherence to regulatory requirements.

**Desired outcome:** You establish
explainability requirements early in your machine learning project
lifecycle. You implement appropriate methods to provide the agreed
level of model explainability, building stakeholder trust and
improving your adherence to regulations. You use explainability
metrics in your evaluations and tradeoff analyses, verifying that
the model meets business needs while remaining interpretable.

**Common anti-patterns:**

- Treating explainability as an afterthought rather than a core
  requirement.
- Choosing the most complex model without considering
  explainability requirements.
- Failing to establish explainability metrics before model
  development.
- Neglecting to communicate model decisions in terms
  understandable to business stakeholders.

**Benefits of establishing this best
practice:**

- Increased stakeholder trust in model predictions.
- Better ability to troubleshoot and improve models.
- Enhanced ability to detect and address model biases.
- Improved model adoption by users who understand how decisions
  are made.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When implementing machine learning models, you need to balance
prediction accuracy with explainability. Highly complex models
like deep neural networks might provide superior predictive
performance but often function as an opaque system, making their
decision-making processes difficult to interpret. In contrast,
simpler models like decision trees offer greater transparency but
may sacrifice some accuracy.

The appropriate level of explainability depends on your specific
use case. In regulated industries like healthcare, finance, or
insurance, high explainability might be mandatory for
compliance-aligned reasons. For applications where human safety or
significant financial decisions are involved, understanding why a
model made a specific prediction becomes critical.

Work with your business stakeholders to understand their
explainability requirements before selecting modeling approaches.
Consider both technical and non-technical aspects of
explainability - technical stakeholders may need detailed feature
importance measures, while business users might need simple,
intuitive explanations of model decisions.

### Implementation steps

1. **Understand business requirements for
   explainability**. Meet with stakeholders to
   determine how much transparency is needed based on use case,
   industry regulations, and business objectives. In regulated
   industries like healthcare and finance, regulations often
   mandate that automated decisions be explainable to affected
   individuals.
2. **Evaluate model types based on
   explainability needs**. Consider inherently
   interpretable models (linear regression, decision trees) for
   high explainability requirements, or more complex models
   with following explanation techniques when higher accuracy
   is the priority.
3. **Set up SageMaker AI
   Clarify**. Implement Amazon SageMaker AI Clarify to
   create explainability reports and detect potential biases in
   your datasets or models. Clarify includes enhanced bias
   detection and new fairness metrics for more comprehensive
   explainability analysis. SageMaker AI Clarify integrates
   with SageMaker AI's model building, training, and deployment
   capabilities.
4. **Choose appropriate SHAP
   baselines**. Shapley Additive exPlanations (SHAP)
   values determine how each feature contributes to
   predictions. Configure appropriate baselines in SageMaker AI
   Clarify based on your data characteristics. You can choose
   baselines with "low information content" (for
   example, average values from the training dataset) or high
   information content (representing a specific class of
   interest).
5. **Generate and interpret feature
   attribution reports**. Use SageMaker AI Clarify to
   generate feature attribution reports showing which features
   most influenced model predictions and how they did so.
   Review these reports with stakeholders to verify that they
   provide the required level of understanding.
6. **Create user-friendly explanation
   interfaces**. Develop appropriate visualization
   tools or explanation interfaces that present model insights
   in ways that are meaningful to various stakeholders, from
   data scientists to business users.
7. **Implement continuous explainability
   monitoring**. Set up ongoing monitoring of model
   explanations to detect drift in feature importance or
   unexpected behavior patterns over time.
8. **Apply responsible AI principles to
   generative models**. For generative AI
   applications, implement additional explainability measures
   such as prompt transparency, citation of sources, and
   confidence scores to assist users in understanding how
   outputs were generated.

## Resources

**Related documents:**

- [Model
  Explainability](../../../sagemaker/latest/dg/clarify-model-explainability.md "../../../sagemaker/latest/dg/clarify-model-explainability.md")
- [Configure
  a SageMaker AI Clarify Processing Job](../../../sagemaker/latest/dg/clarify-processing-job-configure-parameters.md "../../../sagemaker/latest/dg/clarify-processing-job-configure-parameters.md")
- [SHAP
  Baselines for Explainability](../../../sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.md "../../../sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.md")
- [Explain
  text classification model predictions using Amazon SageMaker AI
  Clarify](https://aws.amazon.com/blogs/machine-learning/explain-text-classification-model-predictions-using-amazon-sagemaker-clarify/ "https://aws.amazon.com/blogs/machine-learning/explain-text-classification-model-predictions-using-amazon-sagemaker-clarify/")
