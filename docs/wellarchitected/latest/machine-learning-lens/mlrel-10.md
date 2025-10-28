# MLREL-10: Automate endpoint changes through a pipeline

Manual change management is error prone, and incurs a high
effort cost. Use automated pipelines (that integrate with a
change management tracking system) to deploy changes to your
model endpoints. Versioned pipeline inputs and artifacts allow
you to track the changes and automatically rollback after a
failed change.

## Implementation plan

- **Use Amazon SageMaker AI
  Pipelines** - Deploying changes through a
  pipeline is a safe engineering method that enables
  consistency.
  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/")
  [Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/")
  is the purpose-built, easy-to-use continuous integration
  and continuous delivery (CI/CD) service which enables you
  to create, automate, and manage end-to-end ML workflows at
  scale.

## Documents

- [SageMaker AI
  Pipelines Overview](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [What
  is a SageMaker AI Project?](../../../sagemaker/latest/dg/sagemaker-projects-whatis.md "../../../sagemaker/latest/dg/sagemaker-projects-whatis.md")

## Blogs

- [Build
  a CI/CD pipeline for deploying custom machine learning
  models using AWS services](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/ "https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/")
- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines")
- [Build
  Custom SageMaker AI Project Templates – Best Practices](https://aws.amazon.com/blogs/machine-learning/build-custom-sagemaker-project-templates-best-practices/ "https://aws.amazon.com/blogs/machine-learning/build-custom-sagemaker-project-templates-best-practices/")

## Videos

- [AWS re:Invent 2021: Implementing MLOps practices with Amazon SageMaker AI](https://youtu.be/fuXUi_hoK78 "https://youtu.be/fuXUi_hoK78")
- [AWS re:Invent 2020: How to create fully automated ML workflows
  with Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg "https://www.youtube.com/watch?v=W7uabCTfLrg")
- [AWS on Air 2020: AWS What’s Next ft. Amazon SageMaker AI
  Pipelines](https://www.youtube.com/watch?v=LStze9UMoVE "https://www.youtube.com/watch?v=LStze9UMoVE")

## Examples

- [Comparing
  model metrics with SageMaker AI Pipelines and SageMaker AI Model
  Registry](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-pipeline-compare-model-versions "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-pipeline-compare-model-versions")
