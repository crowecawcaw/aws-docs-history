# MLSEC03-BP01 Provide least privilege access

Protect resources across various phases of the ML lifecycle using
the principle of least privilege. These resources include: data,
algorithms, code, hyperparameters, trained model artifacts, and
infrastructure. Provide dedicated network environments with
dedicated resources and services to operate individual projects.

**Desired outcome:** You establish a
secure machine learning environment by implementing the principle of
least privilege for resources involved in your ML workflows. Your
organization controls access to sensitive data, models, and
infrastructure based on business roles, maintains clear separation
between development, test, and production environments, and uses
appropriate governance mechanisms to enforce security policies. This
approach minimizes your attack surface and protects valuable ML
assets.

**Common anti-patterns:**

- Granting excessive permissions to data scientists or developers
  beyond what they need.
- Using a single AWS account for ML workloads without proper
  separation.
- Not tagging sensitive data and resources for access control
  purposes.
- Failing to isolate ML environments based on data sensitivity
  requirements.
- Relying solely on manual access management without proper
  governance structures.

**Benefits of establishing this best
practice:**

- Reduced risk of unauthorized access to sensitive data and ML
  assets.
- Clear segregation of duties based on business roles.
- Improves adherence to regulatory requirements for data
  protection.
- Simplified governance through standardized access patterns.
- Minimized potential impact of security breaches.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting machine learning workflows requires a comprehensive
security approach that applies the principle of least privilege to
resources involved. By carefully controlling who has access to
data, code, and infrastructure, you can reduce the risk of
unauthorized access or data breaches.

When implementing least privilege for ML resources, consider the
different phases of the ML lifecycle and the types of access
needed by various roles. For example, data scientists might need
read access to training data but not production systems, while ML
engineers may need deployment permissions but limited access to
raw data.

Setting up a multi-account architecture with
[AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") provides strong isolation between
environments with different security requirements. This allows you
to maintain separate development, testing, and production
environments with appropriate controls for each.

### Implementation steps

1. **Define role-based access control for
   ML teams**. Identify the distinct roles within your
   ML workflow, such as data scientists, ML engineers, and
   operations teams. Map these roles to specific access
   patterns required for their daily tasks. Use
   [Amazon SageMaker AI Role Manager](../../../sagemaker/latest/dg/role-manager.md "../../../sagemaker/latest/dg/role-manager.md") to quickly create
   persona-based IAM roles with preconfigured templates for
   common ML roles including data scientists, MLOps engineers,
   and business analysts. This reduces manual permissions
   management and facilitates least privilege access by
   default. Complement with
   [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") for custom role-based
   policies. Implement regular access reviews to verify that
   permissions remain appropriate as responsibilities change.
2. **Implement account separation with
   AWS Organizations**. Create a multi-account
   architecture that segregates workloads between development,
   test, and production environments. Use
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") to centrally manage accounts and apply
   consistent policies. Establish tagging strategies to
   identify data sensitivity levels and resource ownership.
   Apply these tags to relevant resources like S3 buckets
   containing training data or SageMaker AI instances. Use
   [Service
   Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/") to create pre-provisioned environments that
   align with security requirements.
3. **Organize ML workloads by access
   patterns**. Group ML workloads based on common
   access requirements and security profiles. Create
   organizational units (OUs) in AWS Organizations that reflect
   these groupings. Delegate specific access permissions to
   each group according to their needs. Apply service control
   policies (SCPs) to enforce security guardrails at the
   organizational unit level. Limit administrative access to
   infrastructure to designated administrators only.
4. **Isolate sensitive data
   environments**. Create dedicated, isolated
   environments for working with sensitive data. Implement
   network controls such as security groups and network ACLs to
   restrict data flow between environments. Use
   [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") endpoints to provide private connectivity to AWS
   services without traversing the public internet. Configure
   [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") for secure access to SageMaker AI endpoints
   from within your VPC.
5. **Implement automated security
   controls**. Deploy
   [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") rules to continuously monitor resource
   configurations for adherence to security policies. Use
   [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") for threat detection across your ML
   infrastructure. Implement
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") to log and monitor API calls related to ML
   resources. Consider using
   [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") to automatically discover and protect sensitive
   data stored in Amazon S3.
6. **Use secure ML development
   practices**. Implement code repositories with
   appropriate access controls for ML code and models. Use
   version control for artifacts including data, code, and
   model parameters. Apply the principle of least privilege to
   CI/CD pipelines that deploy ML models. Implement model
   governance processes that include security reviews before
   deployment to production.
7. **Deploy ML guardrails with service
   control policies**. Create SCPs that enforce
   requirements across your ML environments. Define policies
   that block storage of sensitive data in unencrypted formats.
   Restrict network egress from environments containing
   sensitive data. Limit which AWS Regions can be used for
   specific types of ML workloads based on requirements.
8. **Implement safeguards for AI
   systems**. For AI workloads, implement additional
   security controls to protect against input injection
   attacks. Implement built-in guardrails for responsible AI
   use. Apply input validation for user inputs to AI systems.
   Implement output filtering to avoid inadvertent disclosure
   of sensitive information. Consider using
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") with governance features to enforce
   compliance-aligned and responsible AI practices.

## Resources

**Related documents:**

- [Amazon SageMaker AI Role Manager](../../../sagemaker/latest/dg/role-manager.md "../../../sagemaker/latest/dg/role-manager.md")
- [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/")
- [Build
  a Secure Enterprise Machine Learning Platform on AWS](../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md")
- [Protecting
  data at rest](../security-pillar/protecting-data-at-rest.md "../security-pillar/protecting-data-at-rest.md")
- [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [Building
  secure Amazon SageMaker AI access URLs with Service
  Catalog](https://aws.amazon.com/blogs/mt/building-secure-amazon-sagemaker-access-urls-with-aws-service-catalog/ "https://aws.amazon.com/blogs/mt/building-secure-amazon-sagemaker-access-urls-with-aws-service-catalog/")
- [Setting
  up secure, well-governed machine learning environments on
  AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/ "https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/")
- [ML
  security: Using Amazon SageMaker AI with AWS PrivateLink](https://aws.amazon.com/blogs/machine-learning/connect-to-amazon-services-using-aws-privatelink-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/connect-to-amazon-services-using-aws-privatelink-in-amazon-sagemaker/")

**Related videos:**

- [Architectural
  best practices for machine learning applications](https://www.youtube.com/watch?v=fBytsYBVgbo "https://www.youtube.com/watch?v=fBytsYBVgbo")
- [Secure
  and compliant machine learning for regulated industries](https://www.youtube.com/watch?v=8p-B3sTLmFg "https://www.youtube.com/watch?v=8p-B3sTLmFg")
- [Amazon SageMaker AI Model Development in a Highly Regulated
  Environment (SDD315)](https://youtu.be/cSYFqKRQ0j0?t=1051 "https://youtu.be/cSYFqKRQ0j0?t=1051")

**Related examples:**

- [Build
  your own Anomaly Detection ML Pipeline](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/build-your-own-anomaly-detection-ml-pipeline-ra.pdf?did=wp_card&trk=wp_card "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/build-your-own-anomaly-detection-ml-pipeline-ra.pdf?did=wp_card&trk=wp_card")
- [AWS MLOps Framework](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/aws-mlops-framework-sol.pdf?did=wp_card&trk=wp_card "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/aws-mlops-framework-sol.pdf?did=wp_card&trk=wp_card")
- [Secure
  ML deployment architecture reference](../../../prescriptive-guidance/latest/patterns/deploy-ml-models-securely-on-aws.md "../../../prescriptive-guidance/latest/patterns/deploy-ml-models-securely-on-aws.md")
- [Secure
  Data Science Reference Architecture](https://github.com/aws-samples/secure-data-science-reference-architecture "https://github.com/aws-samples/secure-data-science-reference-architecture")
