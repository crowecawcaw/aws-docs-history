# MLPER-08: Establish feature statistics

Establish key statistics to measure changes in the data that
affect model outcomes. The effect of changes in data on model
inference depends on the sensitivity of the model to data
features. Analyze the feature importance and sensitivity of the
model to select the features to monitor. Monitor the statistics
of features that have the largest influence on inferences. Place
acceptability limits on the range of data to alert when
important features drift outside the statistical range of the
training data. Significant drifts in important features would
suggest model re-training.

## Implementation plan

- **Analyze and evaluate
  data** - Use
  [Amazon SageMaker AI Data Wrangler](../../../sagemaker/latest/dg/data-wrangler-analyses.md "../../../sagemaker/latest/dg/data-wrangler-analyses.md") to analyze the distribution
  of the selected features. After training the model, map
  out the regions in feature space where the predictions
  change abruptly and where the predictions are invariant.
  Establish a baseline for monitoring the data with
  [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/"). Perform a sensitivity
  analysis of changes in the feature values near the
  decision boundaries of the model. Analyze the feature
  importance to understand how new data will affect the
  model’s predictions.
  [Amazon SageMaker AIExperiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") will help to organize model
  testing. Use
  [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") to check for data biases and
  imbalances. Monitor the statistics of data used in
  production inferences. Consider retraining the model if
  the features are outside the original distribution of the
  training data.

## Documents

- [Amazon SageMaker AI Data Wrangler: Analyze and Visualize](../../../sagemaker/latest/dg/data-wrangler-analyses.md "../../../sagemaker/latest/dg/data-wrangler-analyses.md")
- [Detect
  Pretraining Data Bias](../../../sagemaker/latest/dg/clarify-detect-data-bias.md "../../../sagemaker/latest/dg/clarify-detect-data-bias.md")

## Blogs

- [Exploratory
  data analysis, feature engineering, and operationalizing
  your data flow into your ML](https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/")
  [pipeline
  with Amazon SageMaker AIData Wrangler](https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/")
- [Amazon SageMaker AI Model Monitor– Fully Managed Automatic
  Monitoring for Your Machine Learning](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
  [Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
- [How
  Clarify helps machine learning developers detect
  unintended bias](https://www.amazon.science/latest-news/how-clarify-helps-machine-learning-developers-detect-unintended-bias "https://www.amazon.science/latest-news/how-clarify-helps-machine-learning-developers-detect-unintended-bias")

## Videos

- [Prepare
  data for machine learning with ease, speed, and
  accuracy](https://www.youtube.com/watch?v=Wi3eJxfX754 "https://www.youtube.com/watch?v=Wi3eJxfX754")
- [Detect
  machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")
- [Accelerate
  data preparation with Amazon SageMaker AIData Wrangler](https://www.youtube.com/watch?v=_bsat_2N8LI "https://www.youtube.com/watch?v=_bsat_2N8LI")

## Examples

- [Feature
  Engineering, ImmersionDay Workshop](https://sagemaker-immersionday.workshop.aws/lab1.html "https://sagemaker-immersionday.workshop.aws/lab1.html")
