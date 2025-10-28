# MLREL-06: Enable CI/CD/CT automation with traceability

Enable source code, data, and artifact version control of ML
workloads to enable roll back to a specific version. Incorporate
continuous integration (CI), continuous delivery (CD), and
continuous training (CT) practices to ML workload operations.
This will enable automation with added traceability.

## Implementation plan

- **Use Amazon SageMaker AI
  Pipelines**- Manual changes to a system can cost
  additional time and impair reproducibility. Changes to an
  ML workload should be conducted, tracked and rolled back
  automatically.
  [MLOps](../../../sagemaker/latest/dg/sagemaker-projects-why.md "../../../sagemaker/latest/dg/sagemaker-projects-why.md")
  is a collection of best practices around integrating and
  deploying reproducible, auditable changes. MLOps increases
  your productivity while automating all facets of your ML
  development cycle (MLDC).
  [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") is the first purpose-built,
  continuous integration (CI), continuous delivery (CD), and
  continuous training (CT) service. With SageMaker AI
  Pipelines, create, automate, and manage end-to-end ML
  workflows at scale.

## Documents

- [AWS MLOps Framework](https://aws.amazon.com/solutions/implementations/mlops-workload-orchestrator/ "https://aws.amazon.com/solutions/implementations/mlops-workload-orchestrator/")
- [SageMaker AI
  Pipelines Overview](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [Continuous
  Delivery for Machine Learning on AWS](https://d1.awsstatic.com/whitepapers/mlops-continuous-delivery-machine-learning-on-aws.pdf "https://d1.awsstatic.com/whitepapers/mlops-continuous-delivery-machine-learning-on-aws.pdf")

## Blogs

- [Improve
  your data science workflow with a multi-branch training
  MLOps pipeline using AWS](https://aws.amazon.com/blogs/machine-learning/improve-your-data-science-workflow-with-a-multi-branch-training-mlops-pipeline-using-aws/ "https://aws.amazon.com/blogs/machine-learning/improve-your-data-science-workflow-with-a-multi-branch-training-mlops-pipeline-using-aws/")

- [Build
  a CI/CD pipeline for deploying custom machine learning
  models using AWS services](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/ "https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/")
- [Create
  Amazon SageMaker AI projects with image building CI/CD
  pipelines](https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/ "https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/")

## Videos

- [AWS re:Invent 2020: How to create fully automated ML workflows
  with Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg "https://www.youtube.com/watch?v=W7uabCTfLrg")
- [Inawisdom:
  Machine Learning and Automated Model Retraining with
  SageMaker AI](https://www.youtube.com/watch?v=1kbWvlHBYLk "https://www.youtube.com/watch?v=1kbWvlHBYLk")

## Examples

- [Amazon
  Sagemaker MLOps (with classic CI/CD tools) Workshop](https://github.com/awslabs/amazon-sagemaker-mlops-workshop "https://github.com/awslabs/amazon-sagemaker-mlops-workshop")
- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops "https://github.com/aws-samples/amazon-sagemaker-secure-mlops")
