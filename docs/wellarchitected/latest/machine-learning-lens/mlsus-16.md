# MLSUS-16: Retrain only when necessary

Because of model drift, robustness requirements, or new ground
truth data being available, models usually need to be
retrained. Instead of retraining arbitrarily, monitor your ML
model in production, automate your model drift detection and
only retrain when your model’s predictive performance has
fallen below defined KPIs.

## Implementation plan

- **Determine key performance
  indicators** - With business stakeholders,
  identify a minimum acceptable accuracy and a maximum
  acceptable error.
- **Monitor your model deployed in
  Production** - Automate your model drift
  detection using
  [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/")
- **Automate your retraining
  pipelines** - Use
  [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/"),
  [AWS Step Functions Data Science SDK for Amazon SageMaker AI](https://aws.amazon.com/about-aws/whats-new/2019/11/introducing-aws-step-functions-data-science-sdk-amazon-sagemaker/ "https://aws.amazon.com/about-aws/whats-new/2019/11/introducing-aws-step-functions-data-science-sdk-amazon-sagemaker/") or third-party tools to automate your
  retraining pipelines.

## Resources

- [MLPER-01:
  Determine key performance indicators](mlper-01.md "mlper-01.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 3, deployment
  and monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/")
- [Monitoring
  in-production ML models at large scale using Amazon SageMaker AI Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/ "https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/")
- [Automating
  model retraining and deployment using the AWS Step Functions Data Science SDK for Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/")
- [Automate
  model retraining with Amazon SageMaker AI Pipelines when
  drift is detected](https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/ "https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/")
