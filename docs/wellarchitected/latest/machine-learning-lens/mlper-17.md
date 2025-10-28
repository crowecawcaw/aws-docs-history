# MLPER-17: Review for updated data/features for retraining

Establish a framework to run data exploration and feature
engineering at pre-determined time intervals based on data
volatility and availability. New features that have not been
considered in the model training can affect the accuracy of
model inferences.

## Implementation plan

- **Explore changing data with
  Amazon SageMaker AI Data Wrangler** - Evaluate the
  rate of change of the business environment to set a
  schedule for validating and possibly changing model
  input data and features. Analyze the data using
  [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/ "https://aws.amazon.com/sagemaker/data-wrangler/") and explore new features.
  Establish a team who will periodically evaluate and
  possibly change features and retrain the model.

## Documents

- [Prepare
  ML Data with Amazon SageMaker AI Data Wrangler](../../../sagemaker/latest/dg/data-wrangler.md "../../../sagemaker/latest/dg/data-wrangler.md")
- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")

## Blogs

- [Exploratory
  data analysis, feature engineering, and operationalizing
  your data ﬂow into your ML pipeline with Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/")

## Videos

- [Introducing
  Amazon SageMaker AI Data Wrangler – AWS re:Invent
  2020](https://www.youtube.com/watch?v=tbGGOic21PU "https://www.youtube.com/watch?v=tbGGOic21PU")
