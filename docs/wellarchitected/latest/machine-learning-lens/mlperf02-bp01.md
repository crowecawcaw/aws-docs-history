# MLPERF02-BP01 Define relevant evaluation metrics

Establishing clear, meaningful evaluation metrics is essential for
validating machine learning model performance against business
objectives. By selecting metrics that directly relate to your key
performance indicators (KPIs), you can verify that your ML solutions
deliver measurable business value.

**Desired outcome:** You have a
comprehensive set of evaluation metrics that accurately reflect your
business requirements and tolerance for errors. These metrics enable
you to tune your models directly to business objectives, monitor
performance in production, and make data-driven decisions about
model improvements.

**Common anti-patterns:**

- Using the same generic metrics for each model type regardless of
  business context.
- Focusing only on technical metrics without considering business
  impact.
- Overlooking the cost implications of different types of errors
  (false positives and false negatives).
- Failing to establish baseline performance metrics before
  deployment.
- Neglecting continuous monitoring of metrics after model
  deployment.

**Benefits of establishing this best
practice:**

- Alignment of ML models with business goals and objectives.
- Better decision-making through quantifiable performance
  measurement.
- Early detection of model degradation or concept drift.
- Improved ROI from ML investments.
- Clearer communication between technical teams and business
  stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When developing machine learning solutions, establish evaluation
metrics that directly connect to your business objectives. These
metrics must reflect how well your model performs in the context
of your specific use case rather than relying solely on generic
technical measures.

Avoid focusing only on technical metrics without considering
business impact. Many organizations use the same metrics for each
model type regardless of business context, overlook the cost
implications of different types of errors, fail to establish
baseline performance metrics before deployment, and neglect
continuous monitoring after deployment.

For example, in a predictive maintenance scenario, the business
impact of false positives (unnecessarily replacing functioning
equipment) differs from false negatives (missing actual failures).
Understand these business implications to select appropriate
metrics like precision (minimizing false positives) or recall
(minimizing false negatives) based on which error type is more
costly to your business.

Different ML problem types require different evaluation
approaches. Classification models benefit from confusion matrices
that break down performance by class, while regression models need
error measurements that quantify prediction deviations. Custom
metrics can be developed when standard metrics don't adequately
capture business requirements.

Continuous monitoring of these metrics in production is crucial
for detecting model drift and improving ongoing performance.
Setting up automated alerts when metrics fall below thresholds
allows for timely intervention and model updates.

### Implementation steps

1. **Align metrics to business
   objectives**. Begin by clearly understanding the
   KPIs established during the business goal identification
   phase. Determine how ML model performance directly impacts
   these KPIs and identify which types of errors are most
   costly to the business. For example, in fraud detection,
   false negatives (missed fraudulent transactions) may be more
   costly than false positives.
2. **Select appropriate evaluation
   metrics**. Choose metrics based on your ML problem
   type:
   - **For classification
     problems:** Implement confusion matrix
     derivatives (precision, recall, accuracy, F1 score),
     AUC, or log-loss as appropriate for your use case
   - **For regression
     problems:** Utilize RMSE, MAPE, or other error
     measures that align with business sensitivity to
     prediction errors
   - **For recommendation
     systems:** Consider metrics like Normalized
     Discounted Cumulative Gain (NDCG) or precision@k
   - **For time series
     forecasting:** Apply metrics like Mean Absolute
     Scaled Error (MASE) or symmetric Mean Absolute
     Percentage Error (sMAPE)

3. **Develop custom metrics if
   needed**. When standard metrics don't adequately
   capture business requirements, create custom evaluation
   metrics that better reflect the business objectives. Use
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to implement these custom metrics during
   model training and evaluation.
4. **Establish performance
   thresholds**. Calculate the maximum acceptable
   error probability required for the ML model based on
   business tolerance levels. Document these thresholds as
   acceptance criteria for model deployment.
5. **Implement comparative
   experimentation**. Use
   [Amazon SageMaker AI Managed MLFlow 3.0](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md") to organize, track, and
   compare different models trained with various
   hyperparameters and approaches. The enhanced MLFlow
   integration provides robust experiment management at scale
   for complex ML projects. This structured experimentation
   identifies models that optimize your selected metrics within
   acceptable bounds.
6. **Monitor metrics in
   production**. Deploy
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to track model and concept
   drift in real time. Configure alerts when metrics deviate
   from expected performance thresholds, enabling prompt
   remediation actions.
7. **Incorporate feedback
   loops**. Establish mechanisms to collect real-world
   performance data and incorporate it into your evaluation
   process. This feedback assists you to refine metrics and
   models over time to better align with evolving business
   needs.
8. **Balance competing
   metrics**. When multiple metrics are relevant,
   establish a weighting system that reflects their relative
   importance to business outcomes. Document this
   decision-making framework for consistency in model
   evaluation.
9. **Implement bias detection and model
   explainability**. Use
   [Amazon SageMaker AI Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md") to detect bias in your models and
   provide explanations for model predictions. Your evaluation
   framework should include fairness and interpretability
   considerations alongside performance metrics.
10. **Establish automated model evaluation
    pipelines**. Create automated evaluation workflows
    that run consistently across different model versions and
    training iterations. Use
    [SageMaker AI
    Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md") to standardize your evaluation processes
    and provide reproducible results.

## Resources

**Related documents:**

- [Amazon CloudWatch Metrics for Monitoring and Analyzing Training
  Jobs](../../../sagemaker/latest/dg/training-metrics.md "../../../sagemaker/latest/dg/training-metrics.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Fairness,
  model explainability and bias detection with SageMaker AI
  Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [Evaluate,
  explain, and detect bias in models](../../../sagemaker/latest/dg/model-explainability.md "../../../sagemaker/latest/dg/model-explainability.md")
- [Data
  transformation workloads with SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")

**Related videos:**

- [Organize,
  Track, and Evaluate ML Training Runs with Amazon SageMaker AI
  Managed MLFlow](https://www.youtube.com/watch?v=zLOMYKZGxK0 "https://www.youtube.com/watch?v=zLOMYKZGxK0")
- [Foundation
  model evaluation with SageMaker AI Clarify](https://aws.amazon.com/awstv/watch/31248d9d747/ "https://aws.amazon.com/awstv/watch/31248d9d747/")
- [How
  to efficiently manage ML and Gen AI experiments](https://www.youtube.com/watch?v=3xkz_5HOP6k "https://www.youtube.com/watch?v=3xkz_5HOP6k")

**Related examples:**

- [Scikit-Learn
  Data Processing and Model Evaluation](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation")
- [Amazon SageMaker AI Model Monitor Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor")
