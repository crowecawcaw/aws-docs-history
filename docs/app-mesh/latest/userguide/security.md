# Security in AWS App Mesh

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that is built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
describes this as security _of_ the cloud and security
_in_ the cloud:

- **Security of the cloud** – AWS is
  responsible for protecting the infrastructure that runs AWS services in the AWS
  Cloud. AWS also provides you with services that you can use securely. Third-party
  auditors regularly test and verify the effectiveness of our security as part of the
  [AWS compliance
  programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to
  AWS App Mesh, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/"). App Mesh is responsible
  for securely delivering configuration to local proxies, including secrets such as
  TLS certificate private keys.
- **Security in the cloud** – Your responsibility
  is determined by the AWS service that you use. You are also responsible for other
  factors including:

      + The sensitivity of your data, your company’s requirements, and applicable
       laws and regulations.
      + The security configuration of the App Mesh data plane, including the
       configuration of the security groups that allow traffic to pass between
       services within your VPC.
      + The configuration of your compute resources associated with App Mesh.
      + The IAM policies associated with your compute resources and what
       configuration they are allowed to retrieve from the App Mesh control
       plane.

  This documentation helps you understand how to apply the shared responsibility model when
  using App Mesh. The following topics show you how to configure App Mesh to meet
  your security and compliance objectives. You also learn how to use other AWS services that
  help you to monitor and secure your App Mesh resources.

**App Mesh security tenet**

Customers should be able to tune the security to the extent they need.
Platform should not block them from being more secure. Platform features are
secure by default.

###### Topics

- [Transport Layer Security (TLS)](tls.md "tls.md")
- [Mutual TLS authentication](mutual-tls.md "mutual-tls.md")
- [How AWS App Mesh works with IAM](security-iam.md "security-iam.md")
- [Logging AWS App Mesh API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Data protection in AWS App Mesh](data-protection.md "data-protection.md")
- [Compliance validation for AWS App Mesh](compliance.md "compliance.md")
- [Infrastructure security in AWS App Mesh](infrastructure-security.md "infrastructure-security.md")
- [Resilience in AWS App Mesh](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Configuration and vulnerability analysis in AWS App Mesh](configuration-vulnerability-analysis.md "configuration-vulnerability-analysis.md")
