# MLREL-05: Automate managing data changes

Automate managing changes to training data using version control
technology. This will enable
reproducibility to re-create the exact version of a model in the
event of a failure.

## Implementation plan

- **Use AWS MLOps Framework**

* [AWS MLOps Framework](../../../solutions/latest/aws-mlops-framework/welcome.md "../../../solutions/latest/aws-mlops-framework/welcome.md") provides a standard interface for
  managing ML pipelines for
  [Amazon Machine Learning services](https://aws.amazon.com/machine-learning/ "https://aws.amazon.com/machine-learning/") and third-party services.
  The solution’s template allows you to upload your trained
  models (also referred to as *bring your own
  model*). It configures the orchestration of the
  pipeline, and monitors the pipeline's operations. This
  solution increases agility and efficiency by allowing
  repeating of successful processes at scale. One of the key
  components of MLOps pipeline in SageMaker AI is Model
  Registry.
  [SageMaker AI
  Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") tracks the model versions and
  respective artifacts, including the lineage and metadata.

## Documents

- [AWS MLOps Framework](https://aws.amazon.com/solutions/implementations/mlops-workload-orchestrator/ "https://aws.amazon.com/solutions/implementations/mlops-workload-orchestrator/")
- [Register
  and Deploy Models with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")

## Blogs

- [Amazon SageMaker AI Pipelines Brings DevOps Capabilities to your
  Machine Learning Projects](https://aws.amazon.com/blogs/aws/amazon-sagemaker-pipelines-brings-devops-to-machine-learning-projects/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-pipelines-brings-devops-to-machine-learning-projects/")

## Videos

- [Solving
  with AWS Solutions: AWS MLOps Framework](https://www.youtube.com/watch?v=24JoiN_-LMo "https://www.youtube.com/watch?v=24JoiN_-LMo")

## Examples

- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops "https://github.com/aws-samples/amazon-sagemaker-secure-mlops")
