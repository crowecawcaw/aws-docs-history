# MLSEC04-BP01 Secure governed ML environment

Creating a secure and governed ML environment allows you to protect
valuable data and models while enabling teams to innovate
efficiently. By implementing proper guardrails, monitoring, and
security practices, you maintain control while providing the
flexibility ML practitioners need to deliver business value.

**Desired outcome:** You establish a
secure ML operational environment using AWS managed services that
incorporates best practices for security, governance, and
monitoring. You create development environments that allow data
scientists to explore data safely while maintaining organizational
security standards. Your ML environments are centrally managed with
proper access controls, yet offer self-service capabilities to
improve productivity. This balance between security and flexibility
enables your organization to innovate while protecting sensitive
assets.

**Common anti-patterns:**

- Using a single shared account for ML workloads regardless of
  sensitivity or access requirements.
- Allowing unrestricted access to ML infrastructure and production
  environments.
- Implementing manual provisioning processes that create
  bottlenecks for data scientists.
- Neglecting to isolate environments containing sensitive data.
- Failing to implement continuous monitoring and detection
  controls for ML operations.

**Benefits of establishing this best
practice:**

- Reduced security risks through proper isolation and access
  controls.
- Improved governance with enforced security guardrails.
- Enhanced productivity through self-service capabilities.
- Improves adherence to regulatory requirements.
- Simplified management of ML environments.
- Faster time-to-market for ML initiatives.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing your ML environment requires thoughtful architecture that
balances security with productivity. You need to consider how
different teams interact with ML resources and implement controls
appropriate to their roles and the sensitivity of data being
processed. AWS provides managed services like
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") that can be configured with security best
practices in mind.

Begin by understanding your organization's access patterns and
data sensitivity levels. This knowledge assists you when
determining how to structure your AWS accounts and implementing
appropriate security controls. For example, you might separate
development, testing, and production environments across different
accounts with increasing security restrictions. This multi-account
strategy allows you to implement tailored security controls for
each environment while maintaining proper isolation.

Once you've established your account structure, implement
preventive guardrails using
[AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") and service control policies (SCPs) to
enforce security boundaries. Detective controls using services
like [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") and
[Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") provide continuous monitoring to identify
potential security issues. By combining preventive and detective
controls, you create defense-in-depth protection for your ML
environments.

For environments handling sensitive data, implement additional
security measures like network isolation, encryption, and
fine-grained access controls. Amazon SageMaker AI can be deployed
within a VPC to limit network access, while
[AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
provides robust encryption capabilities for data at rest and in
transit. These measures protect sensitive information throughout
the ML lifecycle.

### Implementation steps

1. **Break out ML workloads by
   organizational unit access patterns**. Create a
   multi-account strategy that aligns with your organization's
   structure and security requirements. For example, create
   separate accounts for data science development, model
   training, and production model deployment. This separation
   allows you to implement role-based access control (RBAC)
   with appropriate permissions for each team. Use
   [Amazon SageMaker AI Role Manager](../../../sagemaker/latest/dg/role-manager.md "../../../sagemaker/latest/dg/role-manager.md") to quickly define
   persona-based IAM roles for different user types (data
   scientists, MLOps engineers, business analysts) with
   preconfigured templates that provide least privilege access.
   Use
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") to manage your multi-account
   environment efficiently.
2. **Use guardrails and service control
   policies (SCPs) to enforce best practices**.
   Implement SCPs through
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") to establish preventive guardrails that
   restrict actions across accounts. For example, create
   policies that block the disabling of security services,
   limit the AWS regions that can be used, or restrict the
   creation of public resources. Complement SCPs with
   [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") rules to detect non-compatible resources and
   automatically remediate issues. Limit infrastructure
   management access to administrators while allowing data
   scientists to focus on model development.
3. **Verify that sensitive data has
   access through restricted, isolated environments**.
   Implement
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") within a private VPC to control network
   traffic to and from your ML environment. Configure security
   groups and network ACLs to restrict access to authorized
   sources. Use
   [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") to access AWS services without traversing
   the public internet. Enable encryption for sensitive data
   using [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") for both data at rest and in
   transit. Review service dependencies to verify that they
   meet your security requirements.
4. **Secure ML algorithm implementation
   using a restricted development environment**.
   Deploy
   [Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/ "https://aws.amazon.com/sagemaker/studio/") with appropriate security controls
   to provide data scientists with a secure development
   environment. Implement
   [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") roles with least
   privilege permissions for each development environment. Use
   [Amazon SageMaker AI Domain](../../../sagemaker/latest/dg/gs-studio-onboard.md "../../../sagemaker/latest/dg/gs-studio-onboard.md") configurations to manage user access
   to resources. Scan container images for vulnerabilities
   before deploying them for model training or hosting using
   [Amazon ECR image scanning](../../../AmazonECR/latest/userguide/image-scanning.md "../../../AmazonECR/latest/userguide/image-scanning.md").
5. **Implement centralized management and
   monitoring**. Use
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") to track API activity across your ML
   environments. Deploy
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") for operational monitoring of your ML
   resources. Implement
   [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") to detect suspicious activity. Centralize
   logs in a dedicated security account for comprehensive
   visibility across your ML environments. Create automated
   alerts for security-related events that require
   investigation.
6. **Enable self-service provisioning
   with guardrails**. Implement
   [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/") to provide pre-approved, secure
   templates for ML resources like SageMaker AI environments.
   Configure lifecycle policies to automatically shut down idle
   resources and reduce costs. Use
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") or
   [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") to define infrastructure as code with security
   best practices built in. This allows data scientists to
   provision resources quickly while maintaining adherence to
   organizational standards.
7. **Secure model artifacts and ML
   pipelines**. Implement version control for models
   and code using
   [Amazon SageMaker AI MLflow Model Registry](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md"). Configure
   [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") with appropriate access controls
   to automate the ML lifecycle. Use
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") and
   [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/") to implement CI/CD for ML applications with
   security checks built into the deployment process.
8. **Implement foundation model security
   controls**. When using large language models (LLMs)
   or other foundation models, implement guardrails to block
   the generation of harmful content. Implement content
   filtering to verify responsible AI usage. For enterprise
   governance of foundation models, implement
   [SageMaker AI
   JumpStart Private Model Hub](../../../sagemaker/latest/dg/jumpstart-curated-hubs.md "../../../sagemaker/latest/dg/jumpstart-curated-hubs.md") to create curated
   repositories of approved models with centralized access
   controls and version management. Use
   [SageMaker AI
   Catalog](../../../sagemaker/latest/dg/sagemaker-projects-templates-custom.md "../../../sagemaker/latest/dg/sagemaker-projects-templates-custom.md") as a central metadata hub for secure sharing
   and governed access to ML assets across business units.
   Implement
   [Amazon SageMaker AI Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md") to document model limitations,
   ethical considerations, and intended uses. Monitor model
   outputs for drift and bias using
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md").

## Resources

**Related documents:**

- [Amazon SageMaker AI Role Manager](../../../sagemaker/latest/dg/role-manager.md "../../../sagemaker/latest/dg/role-manager.md")
- [Private
  curated hubs for foundation model access control in
  JumpStart](../../../sagemaker/latest/dg/jumpstart-curated-hubs.md "../../../sagemaker/latest/dg/jumpstart-curated-hubs.md")
- [Admin
  guide for private model hubs in Amazon SageMaker AI
  JumpStart](../../../sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide.md "../../../sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide.md")
- [Configure
  security in Amazon SageMaker AI](../../../sagemaker/latest/dg/security.md "../../../sagemaker/latest/dg/security.md")
- [Build
  a secure enterprise machine learning platform on AWS](../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md")
- [Security
  Pillar - AWS Well-Architected Framework](../security-pillar/welcome.md "../security-pillar/welcome.md")
- [Model
  governance to manage permissions and track model
  performance](../../../sagemaker/latest/dg/governance.md "../../../sagemaker/latest/dg/governance.md")
- [Setting
  up secure, well-governed machine learning environments on
  AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws "https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws")
- [Securing
  Amazon SageMaker AI Studio connectivity using a private
  VPC](https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/ "https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/")
- [Enable
  self-service, secured data science using Amazon SageMaker AI and
  Service Catalog](https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/ "https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/")
- [Accelerating
  Machine Learning Development with Data Science as a Service
  from Change Healthcare](https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/ "https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/")

**Related videos:**

- [Architectural
  best practices for machine learning applications](https://www.youtube.com/watch?v=fBytsYBVgbo "https://www.youtube.com/watch?v=fBytsYBVgbo")
- [Secure
  and compliant machine learning for regulated industries](https://www.youtube.com/watch?v=8p-B3sTLmFg "https://www.youtube.com/watch?v=8p-B3sTLmFg")
- [Amazon SageMaker AI Model Development in a Highly Regulated
  Environment (SDD315)](https://youtu.be/cSYFqKRQ0j0?t=1051 "https://youtu.be/cSYFqKRQ0j0?t=1051")
