

# Security in Amazon Elastic VMware Service

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:
+  **Security of the cloud**: AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Elastic VMware Service (Amazon EVS), see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+  **Security in the cloud**: Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

With Amazon EVS, you are also responsible for the VMware Cloud Foundation (VCF) software that runs in your environment, including its configuration and credentials. What Amazon EVS does for you differs by deployment mode. For the split of responsibilities between AWS, Broadcom, and you in each mode, see [Shared responsibility and support](plan-shared-responsibility.md).

The procedures in [Deploy in Self-deployed mode](getting-started-self-deployed.md) deploy VCF 9.x. Pages in [Deploy in EVS-deployed mode](evs-deployed-overview.md) cover VCF 5.2.x. A page with no line and outside those sections covers both.

Use the following topics to configure Amazon EVS to meet your security and compliance objectives, and to monitor and secure your Amazon EVS resources with other AWS services.

**Topics**
+ [Data protection for Amazon EVS](data-protection.md)
+ [Identity and access management for Amazon Elastic VMware Service](security-iam.md)
+ [Resilience for Amazon EVS](disaster-recovery-resiliency.md)
+ [Compliance validation for Amazon EVS](compliance-validation.md)
+ [Infrastructure security for Amazon EVS](infrastructure-security.md)