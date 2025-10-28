# MLPER-07: Establish a model performance evaluation pipeline

Capture key metrics related to model performance using an
end-to-end performance pipeline to evaluate the success of a
model. Choose specific metrics based on the use case and the
business KPIs. Sample key metrics include training or validation
errors, and prediction accuracy. Specific model performance
metrics include Root Mean Squared Error (RMSE), accuracy,
precision, recall, F1 score, and area under the curve (AUC).
Establish a fully automated performance testing pipeline system
to initiate evaluation every time there is an updated model or
data.

## Implementation plan

- **Create an end-to-end workflow with
  Amazon SageMaker AI Pipelines** - Start with a
  workflow template to establish an initial infrastructure
  for model training and deployment.
  [SageMaker AI
  Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md") helps you automate different steps of the
  ML workflow. These steps include data loading, data
  transformation, training, tuning, and deployment. With
  SageMaker AI Pipelines, you can share and reuse workflows to
  re-create or optimize models, helping you scale ML
  throughout your organization. Within SageMaker AI Pipelines,
  the
  [SageMaker AI
  Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") tracks the model versions and
  respective artifacts. These artifacts include the metadata
  and lineage data collected throughout the model
  development lifecycle. SageMaker AI Model Registry can also
  enable automating model deployment with CI/CD.

## Documents

- [Define
  a Pipeline](../../../sagemaker/latest/dg/define-pipeline.md "../../../sagemaker/latest/dg/define-pipeline.md")

## Blogs

- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")
- [Extend
  Amazon SageMaker AI Pipelines to include custom steps using
  callback steps](https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/ "https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/")

## Videos

- [Introducing
  Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=Hvz2GGU3Z8g "https://www.youtube.com/watch?v=Hvz2GGU3Z8g")
- [How
  to create fully automated ML workflows with Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg "https://www.youtube.com/watch?v=W7uabCTfLrg")

## Examples

- [SageMaker AI
  Pipelines – Immersion Day](https://sagemaker-immersionday.workshop.aws/lab6.html "https://sagemaker-immersionday.workshop.aws/lab6.html")
