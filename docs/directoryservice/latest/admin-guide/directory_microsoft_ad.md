# AWS Managed Microsoft AD

_AWS Directory Service for Microsoft Active Directory_, also referred to as AWS Managed Microsoft AD, runs Microsoft Active Directory as a
managed service powered by Windows Server 2019. It creates a highly available
pair of domain controllers in your Amazon VPC across different Availability Zones, with AWS
automatically managing host monitoring, recovery, data replication, snapshots, and software
updates. This service enables you to run directory-aware workloads, manage users and groups,
provide single sign-on, create and apply group policies, and securely connect to Amazon EC2
instances.

Directory Service offers two Microsoft Active Directory solutions: _AWS Directory Service for Microsoft Active Directory_ provides a fully
managed Active Directory service in the AWS Cloud, while _AWS Managed Microsoft AD (Hybrid Edition)_
extends your existing self-managed AD to AWS.

_AWS Managed Microsoft AD (Standard Edition and Enterprise Edition)_ create new
managed AD domains to manage users, devices, and computers on AWS. These directories establish
resource forests that create trust relationships with your existing AD domains on-premises, in
AWS, or in multi-cloud environments. Users can access AWS resources with their existing
credentials from your current AD domains. User identities stay in your existing AD domains while
the resource forest manages your AWS resources, maintaining operational isolation between
environments while providing seamless single sign-on.

_AWS Managed Microsoft AD (Hybrid Edition)_ connects your self-managed Active Directory with
AWS Directory Service for Microsoft Active Directory, creating an integrated identity environment spanning both your infrastructure
and the AWS Cloud. This solution extends your directory services to AWS without synchronizing
user identities, establishes trust relationships between environments, and provides seamless access
using existing credentials.

With AWS Managed Microsoft AD, you can run directory-aware workloads in the AWS Cloud, including Microsoft
SharePoint and custom .NET and SQL Server-based applications. You can also
configure trust relationships between AWS Managed Microsoft AD and your existing self-managed Microsoft Active Directory,
providing users and groups with access to resources in either domain using AWS IAM Identity Center.

## Which to choose

You can choose between two AWS Directory Service services with the features and scalability that best
meet your needs. The following table helps you determine which Directory Service option works best
for your organization.

| Use case                                                                                      | Recommended solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Run directory-aware workloads, AWS applications, or Linux applications requiring LDAP support | \*AWS Managed Microsoft AD (Standard Edition and Enterprise Edition)<br>• create new<br>managed AD domains to manage users, devices, and computers on AWS. These directories establish<br>resource forests that create trust relationships with your existing AD domains on-premises, in<br>AWS, or in multi-cloud environments. Users can access AWS resources with their existing<br>credentials from your current AD domains. User identities stay in your existing AD domains while<br>the resource forest manages your AWS resources, maintaining operational isolation between<br>environments while providing seamless single sign-on. |
| Extend existing Active Directory to AWS                                                       | \*AWS Managed Microsoft AD (Hybrid Edition)<br>• connects your self-managed Active Directory with<br>AWS Directory Service for Microsoft Active Directory, creating an integrated identity environment spanning both your infrastructure<br>and the AWS Cloud. This solution extends your directory services to AWS without synchronizing<br>user identities, establishes trust relationships between environments, and provides seamless access<br>using existing credentials.                                                                                                                                                               |

## Topics

- [Getting started with AWS Managed Microsoft AD](ms_ad_getting_started.md "ms_ad_getting_started.md")
- [Understanding AWS Managed Microsoft AD (Hybrid Edition)](aws-hybrid-directory.md "aws-hybrid-directory.md")
