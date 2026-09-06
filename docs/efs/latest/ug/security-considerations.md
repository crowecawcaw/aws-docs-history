

# Securing your data in Amazon EFS
<a name="security-considerations"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Elastic File System, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using Amazon EFS. The following topics show you how to configure Amazon EFS to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Amazon EFS resources. 

**Topics**
+ [Data protection in Amazon EFS](data-protection.md)
+ [Identity and access management for Amazon EFS](security-iam.md)
+ [Using IAM to control access to file systems](iam-access-control-nfs-efs.md)
+ [Compliance validation for Amazon EFS](EFS-compliance.md)
+ [Resilience in Amazon EFS](disaster-recovery-resiliency.md)
+ [Controlling network access to EFS file systems for NFS clients](NFS-access-control-efs.md)
+ [Network File System (NFS) level users, groups, and permissions](accessing-fs-nfs-permissions.md)
+ [Working with access points](efs-access-points.md)
+ [Blocking public access to EFS file systems](access-control-block-public-access.md)
+ [Network isolation for Amazon EFS](network-isolation.md)