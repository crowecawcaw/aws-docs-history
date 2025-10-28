# MLOE-12: Automate operations through MLOps and CI/CD

Automate ML workload operations using infrastructure as code
(IaC) and configuration as code (CaC). Select appropriate MLOps
mechanisms to orchestrate your ML workflows and integrate with
CI/CD pipelines for automated deployments. This approach ensures
consistency across your staging and production deployment
environments. Enable model observability and version control
across your hosting infrastructure.

## Implementation plan

You can choose either AWS CloudFormation or AWS Cloud Development Kit (AWS CDK):

- **Use AWS CloudFormation** -[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") enables you to create and provision
  AWS deployments predictably and repeatedly by using a
  template file to create and delete a collection of
  resources together as a single unit (a stack). You can
  manage and provision stacks across multiple AWS accounts
  and AWS Regions.
- **Use AWS Cloud Development Kit (AWS CDK)** - Use
  [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") (AWS CDK) as a software development
  framework for defining cloud infrastructure in code and
  provisioning it through AWS CloudFormation. You can define
  your cloud resources in AWS CDK using familiar programming
  languages.

You can choose any of the following MLOps strategies based on
your ML workflows:

- **Use SageMaker AI Pipelines to
  orchestrate your workflows**

Using
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/"), you can create ML workflows with
Python SDK, and then visualize and manage your workflow using
Amazon SageMaker AI Studio. Amazon SageMaker AI Pipelines logs every
step of your workflow, creating an audit trail of model
components such as training data, platform configurations,
model parameters, and learning gradients. 

- **Use AWS Step Functions**-
  You can also use
  [AWS Step Functions Data Science SDK](../../../step-functions/latest/dg/concepts-python-sdk.md "../../../step-functions/latest/dg/concepts-python-sdk.md") for

Amazon SageMaker AI to automate training of a machine learning
model. Define all the

steps in the workflow and set up alerts to start the flow.

- **Use third-party tools** -
  Use third-party deployment orchestration tools, such as

Apache Airflow, that integrate with AWS service APIs to
automate model training and deployment.
[Amazon
Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/ "https://aws.amazon.com/managed-workflows-for-apache-airflow/")
orchestrates your workflows using Directed Acyclic Graphs
(DAGs) written in Python.

data is available.

## Documents

- [Infrastructure
  as Code](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md")
- [AWS CloudFormation](../../../cloudformation/index.md "../../../cloudformation/index.md")
- [AWS Cloud Development Kit (AWS CDK) (CDK)](../../../cdk/latest/guide/home.md "../../../cdk/latest/guide/home.md")
- [SageMaker AI
  Pipelines](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [Step
  Functions Data Science SDK](https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/ "https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/")

## Blogs

- [AWS CloudFormation – Create Your AWS Stack from a
  Recipe](https://aws.amazon.com/blogs/aws/cloudformation-create-your-aws-stack-from-a-recipe/ "https://aws.amazon.com/blogs/aws/cloudformation-create-your-aws-stack-from-a-recipe/")
- [Automate
  Amazon SageMaker AI Studio setup using AWS SDK](https://aws.amazon.com/blogs/machine-learning/automate-amazon-sagemaker-studio-setup-using-aws-cdk/ "https://aws.amazon.com/blogs/machine-learning/automate-amazon-sagemaker-studio-setup-using-aws-cdk/")
- [Secure
  multi-account model deployment with Amazon SageMaker AI: Part
  1](https://aws.amazon.com/blogs/machine-learning/part-1-secure-multi-account-model-deployment-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/part-1-secure-multi-account-model-deployment-with-amazon-sagemaker/")
- [Secure
  multi-account model deployment with Amazon SageMaker AI: Part
  2](https://aws.amazon.com/blogs/machine-learning/part-2-secure-multi-account-model-deployment-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/part-2-secure-multi-account-model-deployment-with-amazon-sagemaker/")
- [Organize
  your machine learning journey with SageMaker AI
  Pipelines](https://aws.amazon.com/blogs/machine-learning/organize-your-machine-learning-journey-with-amazon-sagemaker-experiments-and-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/organize-your-machine-learning-journey-with-amazon-sagemaker-experiments-and-amazon-sagemaker-pipelines/")
