# Securing your Amazon Neptune database

Cloud security at AWS is the highest priority. As an AWS customer,
you benefit from a data center and network architecture that is built to meet
the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_
the cloud and security _in_ the cloud:

- **Security of the cloud** –
  AWS is responsible for protecting the infrastructure that runs AWS services
  in the AWS Cloud. AWS also provides you with services that you can use
  securely. Third-party auditors regularly test and verify the effectiveness
  of our security as part of the [AWS
  compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to
  Amazon Neptune, see [AWS
  Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** –
  Your responsibility is determined by the AWS service that you use.
  You are also responsible for other factors including the sensitivity
  of your data, your company’s requirements, and applicable laws and
  regulations.
  This documentation helps you understand how to apply the shared
  responsibility model when using Neptune. The following topics show
  you how to configure Neptune to meet your security and compliance
  objectives. You also learn how to use other AWS services that help you
  to monitor and secure your Neptune resources.

###### Topics

- [Amazon Neptune operating system upgrades](security-os-upgrades.md "security-os-upgrades.md")
- [Protecting data in your Amazon Neptune database](data-protection.md "data-protection.md")
- [Authenticating your Amazon Neptune database with AWS Identity and Access Management](iam-auth.md "iam-auth.md")
- [Enabling IAM database authentication in
  Amazon Neptune](iam-auth-enable.md "iam-auth-enable.md")
- [Connecting to your Amazon Neptune database using AWS Identity and Access Management authentication](iam-auth-connecting.md "iam-auth-connecting.md")
- [Managing access to Amazon Neptune databases using IAM policies](security-iam-access-manage.md "security-iam-access-manage.md")
- [Using service-linked roles for Amazon Neptune](security-iam-service-linked-roles.md "security-iam-service-linked-roles.md")
- [Using temporary credentials to connect to Amazon Neptune](iam-auth-temporary-credentials.md "iam-auth-temporary-credentials.md")
- [Logging and monitoring usage and performance in Amazon Neptune](security-monitoring.md "security-monitoring.md")
- [Compliance considerations for Amazon Neptune](neptune-compliance.md "neptune-compliance.md")
- [Building resilient and disaster-tolerant Amazon Neptune deployments](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
