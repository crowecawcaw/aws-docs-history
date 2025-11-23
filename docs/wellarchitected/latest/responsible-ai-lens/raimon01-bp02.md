# RAIMON01-BP02 Set operational performance baselines and apply

methods for drift detection

Set performance trend baselines by collecting initial production
data over a representative time period to capture your system's
actual operating performance, which may vary from your release
criteria thresholds. Use statistical methods to characterize normal
performance variation patterns, seasonal trends, and expected
behavioral ranges for each monitored metric based on observed system
behavior. Implement drift detection techniques such as statistical
process control charts, change point detection algorithms, and trend
analysis that can identify when current performance deviates
significantly from established baseline trends, indicating the
system is not performing as expected.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Establish a baseline using either the training data or a
   representative validation dataset, defining the expected data
   distribution and model behavior.
2. Establish data collection to gather relevant metrics during
   normal operations, capturing representative system behavior
   including peak/off-peak periods and seasonal variations.
3. Use statistical tests and algorithms to compare live data and
   monitored metrics against the established baseline. Pre-built
   rules or custom rules can be configured to define thresholds
   for acceptable deviations. When a deviation exceeds these
   thresholds, it may indicate potential data drift, model
   performance degradation, or bias. Amazon SageMaker AI Model
   Monitor and SageMaker AI Clarify are examples of services
   supporting these functions.

## Resources

**Related tools:**

- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Fairness,
  model explainability and bias detection with SageMaker AI
  Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [Bias
  drift for models in production](../../../sagemaker/latest/dg/clarify-model-monitor-bias-drift.md "../../../sagemaker/latest/dg/clarify-model-monitor-bias-drift.md")

**Related documents**

- [Automated
  monitoring of your machine learning models with Amazon SageMaker AI AIModel Monitor and](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/")
  [sending
  predictions to human review workflows using Amazon A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/")
- [Amazon SageMaker AI AI Model Monitor– Fully Managed Automatic Monitoring
  for Your Machine Learning](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
  [Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
- [AWS re:Invent 2020: Detect machine learning (ML) model drift in
  production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")
- [ISO/IEC
  42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
