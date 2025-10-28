# MLREL-13: Ensure a recoverable endpoint with a managed version control strategy

Ensure an endpoint responsible for hosting model predictions,
and all components responsible for generating that endpoint,
are fully recoverable. Some of these components include model
artifacts, container images, and endpoint configurations.
Ensure all required components are version controlled, and
traceable in a lineage tracker system.

## Implementation plan

- **Implement MLOps best practices
  with Amazon SageMaker AI Pipelines and Projects**

* [Amazon](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/")
  [SageMaker AI
  Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") is a service for building machine
  learning pipelines. It automates developing, training,
  and deploying models in a versioned, predictable
  manner. [Amazon SageMaker AI Projects](../../../sagemaker/latest/dg/sagemaker-projects-whatis.md "../../../sagemaker/latest/dg/sagemaker-projects-whatis.md") enable teams of data
  scientists and developers to collaborate on machine
  learning business problems. A SageMaker AI project is an
  [Service Catalog](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md") provisioned product that enables
  you to easily create an end-to-end ML solution.
  SageMaker AI Projects entities include pipeline executions,
  registered models, endpoints, datasets, and code
  repositories.

- **Use infrastructure as code (IaC)
  tools** - Use
  [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") to define and build your
  infrastructure, including your model endpoints. Store
  your AWS CloudFormation code in git repositories so that you can version control your
  infrastructure code.
- **Use Amazon Elastic Container Registry (Amazon ECR)** - Store your containers
  in
  [Amazon ECR](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md"), an artifact repository for Docker
  containers. Amazon ECR automatically creates a version
  hash for your containers as you update them, allowing
  you to roll back to previous versions.

## Documents

- [AWS CloudFormation](../../../cloudformation/index.md "../../../cloudformation/index.md")
- [Infrastructure
  as Code](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md")
- [SageMaker AI
  Pipelines Overview](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [What
  is a SageMaker AI Project?](../../../sagemaker/latest/dg/sagemaker-projects-whatis.md "../../../sagemaker/latest/dg/sagemaker-projects-whatis.md")
- [What
  is Service Catalog?](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md")
- [What
  is Amazon Elastic Container Registry](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md")

## Blogs

- [Building,
  automating, managing, and scaling ML workﬂows using
  Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")
- [Multi-account
  model deployment with Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/multi-account-model-deployment-with-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/multi-account-model-deployment-with-amazon-sagemaker-pipelines/")
- [Automate
  feature engineering pipelines with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/automate-feature-engineering-pipelines-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/automate-feature-engineering-pipelines-with-amazon-sagemaker/")

## Videos

- [Infrastructure
  as Code on AWS - AWS Online Tech Talks](https://www.youtube.com/watch?v=cKQtPZwf97s "https://www.youtube.com/watch?v=cKQtPZwf97s")
- [AWS re:Invent 2020: How to create fully automated ML
  workﬂows with Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg "https://www.youtube.com/watch?v=W7uabCTfLrg")
- [Introducing
  Amazon SageMaker AI Pipelines - AWS re:Invent 2020](https://www.youtube.com/watch?v=Hvz2GGU3Z8g "https://www.youtube.com/watch?v=Hvz2GGU3Z8g")
- [AWS re:Invent 2020: Implementing MLOps practices with Amazon SageMaker AI](https://www.youtube.com/watch?v=8ZpE-9LnaJk "https://www.youtube.com/watch?v=8ZpE-9LnaJk")

## Examples

- [CI/CD
  Pipeline for AWS CloudFormation templates on AWS](https://aws.amazon.com/quickstart/architecture/cicd-taskcat/ "https://aws.amazon.com/quickstart/architecture/cicd-taskcat/")
- [Amazon SageMaker AI MLOps](https://github.com/aws-samples/mlops-amazon-sagemaker-devops-with-ml "https://github.com/aws-samples/mlops-amazon-sagemaker-devops-with-ml")
