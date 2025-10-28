# MLSEC-08: Secure governed ML environment

Protect ML operations environments using managed services with
best practices including: detective and preventive guardrails,
monitoring, security, and incident management. Explore data in a
managed and secure development environment. Centrally manage the
configuration of development environments and enable self-service
provisioning for the users.

## Implementation plan

- **Break out ML workloads**
  by organizational unit access patterns. This will enable
  delegating required access to each group, such as
  administrators or data analysts.
- **Use guardrails and service control
  policies (SCPs)** to enforce best practices for
  each environment type. Limit infrastructure management
  access to administrators.
- **Verify all sensitive data has
  access through restricted, isolated
  environments**. Ensure network isolation,
  dedicated resources, and check service dependencies.
- **Secure ML algorithm
  implementation** using a restricted development
  environment. Secure model training and hosting containers
  by following the security processes required for your
  organization.

## Documents

- [Security
  in Amazon SageMaker AI](../../../sagemaker/latest/dg/security.md "../../../sagemaker/latest/dg/security.md")
- [Build
  a secure enterprise machine learning platform on
  AWS](../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md")
- [Use
  Amazon SageMaker AI Notebook Instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md")
- [Amazon SageMaker AI with Guardrails on AWS](https://aws.amazon.com/quickstart/architecture/amazon-sagemaker-with-guardrails/ "https://aws.amazon.com/quickstart/architecture/amazon-sagemaker-with-guardrails/")

## Blogs

- [Setting
  up secure, well-governed machine learning environments on
  AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws "https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws")
- [Securing
  Amazon SageMaker AI Studio Connectivity using a private
  VPC](https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/ "https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/")
- [Enable
  self-service, secured data science using Amazon SageMaker AI
  notebooks and AWS Service](https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/ "https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/")
  [Catalog](https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/ "https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/")
- [Accelerating
  Machine Learning Development with Data Science as a
  Service from Change Healthcare](https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/ "https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/")
