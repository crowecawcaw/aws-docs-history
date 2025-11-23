# MLREL03-BP03 Validate models with relevant data

Testing and validating machine learning models with appropriate data
is essential for reliable performance in production. Use real and
representative data that covers many possible patterns and scenarios
to avoid model failures when deployed in real-world environments.

**Desired outcome:** You establish
processes that validate your machine learning models with
real-world, representative data before deployment. You can identify
distribution mismatches between training, validation, test, and
inference data early, allowing you to address issues before they
impact production performance. Your validation approach includes
both real-world and engineered data to account for the scenarios
your model might encounter.

**Common anti-patterns:**

- Testing models with only synthetic data that doesn't represent
  real-world conditions.
- Failing to check for distribution mismatch between training and
  production data.
- Ignoring edge cases and rare scenarios in validation datasets.
- Using validation data that lacks diversity or has sampling
  biases.
- Neglecting periodic revalidation after models are deployed.

**Benefits of establishing this best
practice:**

- Reduces risk of model failures in production environments.
- Enables early detection of data drift and model quality
  degradation.
- Creates more robust models that perform well across expected
  scenarios.
- Increases trust in model predictions from stakeholders.
- Improves alignment between model performance in testing and
  production.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Validating your machine learning models with relevant data is a
critical step in the ML development lifecycle. Data that fails to
represent the full range of scenarios your model will encounter in
production can lead to poor performance, biased outputs, or
complete failures when deployed. The key challenge lies in
obtaining and using data that accurately mirrors your production
environment.

Begin by analyzing your data sources to capture the breadth and
depth of real-world scenarios. This includes common cases as well
as edge cases that might be rare but important. For example, a
model designed to detect fraudulent transactions needs exposure to
both typical and unusual fraud patterns. Missing these edge cases
can create vulnerabilities in your deployed model.

Pay particular attention to distribution mismatches, where the
statistical properties of your training, validation, test, and
eventual inference data differ. These mismatches often lead to
degraded model performance in production. For instance, if you
train a product recommendation model on data from one demographic
group but deploy it for a different group, the model may make
irrelevant recommendations.

Implement continuous monitoring after deployment to detect when
the data distribution shifts over time, which is common in
real-world applications. This allows you to retrain models before
performance degradation impacts business outcomes.

### Implementation steps

1. **Establish data quality
   criteria**. Define what constitutes representative
   data for your use case. Include requirements for data
   completeness, diversity, and coverage of edge cases.
   Document these criteria as part of your ML development
   process to create consistency across projects.
2. **Implement cross-validation
   techniques**. Use techniques like k-fold
   cross-validation to verify that your model generalizes well
   across different subsets of your data. This can identify
   potential overfitting issues before deployment and provides
   a more robust estimate of how your model will perform in
   production.
3. **Use Amazon SageMaker AI MLFlow
   Tracking**. Set up experiments to track and compare
   different training runs with various data configurations.
   [SageMaker AI
   MLFlow Tracking](../../../sagemaker/latest/dg/mlflow-create-tracking-server.md "../../../sagemaker/latest/dg/mlflow-create-tracking-server.md") allows you to organize, monitor, and
   evaluate your machine learning experiments systematically.
   This can identify which data configurations lead to the best
   performance and provides a historical record for future
   reference.
4. **Create engineered test
   data**. Generate synthetic data to supplement
   real-world data, especially for rare but important edge
   cases. Verify that this synthetic data maintains the
   statistical properties of real data while providing coverage
   for scenarios that might be underrepresented in your
   original dataset.
5. **Implement data drift
   detection**. Set up processes to continuously
   compare the distribution of inference data with your
   baseline training data. Use this comparison to identify when
   the real-world data begins to diverge from what the model
   was trained on, which can signal the need for retraining.
6. **Use Amazon SageMaker AI Model
   Monitor**. Deploy
   [Model
   Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to automatically track and analyze model
   behavior in production. Configure alerts for deviations in
   model quality, data quality, bias drift, and feature
   attribution drift. SageMaker AI Model Monitor continuously
   evaluates your deployed models and notifies you when action
   is needed.
7. **Establish a regular validation
   cadence**. Schedule periodic evaluations of your
   model using fresh data, even if drift hasn't been detected.
   This can catch subtle changes that might not trigger
   automated alerts but could still affect model performance
   over time.
8. **Document validation
   results**. Create detailed reports of validation
   processes and outcomes for each model version. Include
   metrics on data representativeness, performance across
   different data segments, and identified gaps or biases.

## Resources

**Related documents:**

- [Evaluating
  ML Models](../../../machine-learning/latest/dg/evaluating_models.md "../../../machine-learning/latest/dg/evaluating_models.md")
- [Cross-Validation](../../../machine-learning/latest/dg/cross-validation.md "../../../machine-learning/latest/dg/cross-validation.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/")
- [Detect
  data drift using Amazon SageMaker AI Model Monitor](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/")
- [Monitoring
  in-production ML models at large scale using Amazon SageMaker AI
  Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/ "https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/")

**Related videos:**

- [How
  To Efficiently Manage ML experiments using Amazon SageMaker AI ML
  Flow](https://www.youtube.com/watch?v=3xkz_5HOP6k "https://www.youtube.com/watch?v=3xkz_5HOP6k")
- [Detect
  machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")

**Related examples:**

- [Amazon SageMaker AI Model Monitor](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor")
