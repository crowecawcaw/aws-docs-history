# Prerequisites

Before using the CI/CD CLI, you need:

- **Python 3.8 or later**
- **AWS credentials** configured with permissions to deploy resources to your target Amazon SageMaker Unified Studio projects. See [Sample IAM policy](cicd-sample-iam-policy.md "cicd-sample-iam-policy.md") for required permissions.
- **Existing Amazon SageMaker Unified Studio projects** at each target stage. The CLI deploys application workloads into existing projects — it does not create domains or projects. Use AWS CloudFormation, AWS CDK, or Terraform for infrastructure setup.
