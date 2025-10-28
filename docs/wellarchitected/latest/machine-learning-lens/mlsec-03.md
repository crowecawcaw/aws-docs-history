# MLSEC-03: Ensure least privilege access

Protect all resources across various phases of the ML lifecycle
using the principle of least privilege. These resources include:
data, algorithms, code, hyperparameters, trained model
artifacts, and infrastructure. Provide dedicated network
environments with dedicated resources and services to operate
any individual project. 

## Implementation plan

- **Restrict access based on business
  roles for individuals** - Identify roles that
  need to explore data to build models, features, and
  algorithms. Map those roles to access patterns using
  role-based authentication. This approach helps you achieve
  least privilege access to sensitive data, assets, and
  services on a project-by-project basis.
- **Use account separation and AWS Organizations** - Establish tagging and
  role-based access grants. Understand workflows of the
  different user types. Use
  [Service Catalog](https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc "https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc") to create pre-provisioned
  environments for quick deployment including a
  multi-account architecture that segregates workloads
  between development, test, and production with appropriate
  governance based on data sensitivity and compliance
  requirements. Tag data and buckets that contain
  sensitive workloads. Use these tags to grant granular
  access to individuals.
- **Break out ML workloads by access
  pattern and structure organizational units** -
  Delegate specific access to each group, such as
  administrators or data analysts, as required. Use
  guardrails and service control policies (SCPs) to enforce
  best practices for each access type and group. Limit
  infrastructure access to administrators. Verify all
  sensitive data is accessed through restricted, dedicated,
  and isolated environments.

## Documents

- [Amazon SageMaker AI with Guardrails on AWS](https://aws.amazon.com/quickstart/architecture/amazon-sagemaker-with-guardrails/ "https://aws.amazon.com/quickstart/architecture/amazon-sagemaker-with-guardrails/")
- [Service Catalog](https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc "https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc")
- [Build
  a Secure Enterprise Machine Learning Platform on
  AWS](../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md")
- [AWS Well Architected Framework Security Pillar : Protecting
  Data at Rest](../security-pillar/protecting-data-at-rest.md "../security-pillar/protecting-data-at-rest.md")

## Blogs

- [Building
  secure Amazon SageMaker AI access URLs with Service Catalog](https://aws.amazon.com/blogs/mt/building-secure-amazon-sagemaker-access-urls-with-aws-service-catalog/ "https://aws.amazon.com/blogs/mt/building-secure-amazon-sagemaker-access-urls-with-aws-service-catalog/")
- [Setting
  up secure, well-governed machine learning environments on
  AWS - for detailed guidance on](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/ "https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/")
  [SCP
  and OU strategies](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/ "https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/")

## Videos

- [AWS re:Invent 2020: Architectural best practices for machine
  learning applications](https://www.youtube.com/watch?v=fBytsYBVgbo "https://www.youtube.com/watch?v=fBytsYBVgbo")
- [AWS re:Invent 2020: Secure and compliant machine learning for
  regulated industries](https://www.youtube.com/watch?v=8p-B3sTLmFg "https://www.youtube.com/watch?v=8p-B3sTLmFg")
- [AWSre:Inforce
  2019: Amazon SageMaker AI Model Development in a Highly
  Regulated Environment](https://youtu.be/cSYFqKRQ0j0?t=1051 "https://youtu.be/cSYFqKRQ0j0?t=1051")
  [(SDD315)](https://youtu.be/cSYFqKRQ0j0?t=1051 "https://youtu.be/cSYFqKRQ0j0?t=1051")

## Examples

- [Build
  your own Anomaly Detection ML Pipeline](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/build-your-own-anomaly-detection-ml-pipeline-ra.pdf?did=wp_card&trk=wp_card "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/build-your-own-anomaly-detection-ml-pipeline-ra.pdf?did=wp_card&trk=wp_card")
- [AWS MLOps Framework](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/aws-mlops-framework-sol.pdf?did=wp_card&trk=wp_card "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/aws-mlops-framework-sol.pdf?did=wp_card&trk=wp_card")
