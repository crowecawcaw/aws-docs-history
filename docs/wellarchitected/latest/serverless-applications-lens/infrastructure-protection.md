# Infrastructure protection

For scenarios where your serverless application needs to interact with other
components deployed in a virtual private cloud (VPC) or applications residing
on-premises, it’s important to ensure that networking boundaries are considered.

Lambda functions can be configured to access resources within a VPC. Control traffic
at all layers as described in the AWS Well-Architected Framework. For workloads that
require outbound traffic filtering due to compliance reasons, proxies can be used in the
same manner that they are applied in non-serverless architectures.

Enforcing networking boundaries solely at the application code level and giving
instructions as to what resources one could access is not recommended due to separation
of concerns.

For service-to-service communication, favor dynamic authentication, such as temporary
credentials with AWS IAM over static keys. API Gateway and AWS AppSync both support IAM
Authorization that makes it ideal to protect communication to and from AWS
services.
