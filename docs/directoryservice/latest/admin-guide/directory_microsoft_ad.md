

# AWS Managed Microsoft AD
<a name="directory_microsoft_ad"></a>

*AWS Directory Service for Microsoft Active Directory*, also referred to as AWS Managed Microsoft AD, runs Microsoft Active Directory as a managed service powered by Windows Server 2019. It creates a highly available pair of domain controllers in your Amazon VPC across different Availability Zones, with AWS automatically managing host monitoring, recovery, data replication, snapshots, and software updates. This service enables you to run directory-aware workloads, manage users and groups, provide single sign-on, create and apply group policies, and securely connect to Amazon EC2 instances.

Directory Service offers two Microsoft Active Directory solutions: *AWS Directory Service for Microsoft Active Directory* provides a fully managed Active Directory service in the AWS Cloud, while *AWS Managed Microsoft AD (Hybrid Edition)* extends your existing self-managed AD to AWS.

*AWS Managed Microsoft AD (Standard Edition and Enterprise Edition)* create new managed AD domains to manage users, devices, and computers on AWS. These directories establish resource forests that create trust relationships with your existing AD domains on-premises, in AWS, or in multi-cloud environments. Users can access AWS resources with their existing credentials from your current AD domains. User identities stay in your existing AD domains while the resource forest manages your AWS resources, maintaining operational isolation between environments while providing seamless single sign-on.

*AWS Managed Microsoft AD (Hybrid Edition)* connects your self-managed Active Directory with AWS Directory Service for Microsoft Active Directory, creating an integrated identity environment spanning both your infrastructure and the AWS Cloud. This solution extends your directory services to AWS without synchronizing user identities, establishes trust relationships between environments, and provides seamless access using existing credentials.

With AWS Managed Microsoft AD, you can run directory-aware workloads in the AWS Cloud, including Microsoft SharePoint and custom .NET and SQL Server-based applications. You can also configure trust relationships between AWS Managed Microsoft AD and your existing self-managed Microsoft Active Directory, providing users and groups with access to resources in either domain using AWS IAM Identity Center.

## Which to choose
<a name="choosing_ms_ad"></a>

You can choose between two AWS Directory Service services with the features and scalability that best meet your needs. The following table helps you determine which Directory Service option works best for your organization.



| Use case | Recommended solution | 
| --- | --- | 
| Run directory-aware workloads, AWS applications, or Linux applications requiring LDAP support | *AWS Managed Microsoft AD (Standard Edition and Enterprise Edition)* create new managed AD domains to manage users, devices, and computers on AWS. These directories establish resource forests that create trust relationships with your existing AD domains on-premises, in AWS, or in multi-cloud environments. Users can access AWS resources with their existing credentials from your current AD domains. User identities stay in your existing AD domains while the resource forest manages your AWS resources, maintaining operational isolation between environments while providing seamless single sign-on. | 
| Extend existing Active Directory to AWS | *AWS Managed Microsoft AD (Hybrid Edition)* connects your self-managed Active Directory with AWS Directory Service for Microsoft Active Directory, creating an integrated identity environment spanning both your infrastructure and the AWS Cloud. This solution extends your directory services to AWS without synchronizing user identities, establishes trust relationships between environments, and provides seamless access using existing credentials. | 

## Topics
<a name="ms-ad-topics"></a>
+ [Getting started with AWS Managed Microsoft AD](ms_ad_getting_started.md)
+ [Understanding AWS Managed Microsoft AD (Hybrid Edition)](aws-hybrid-directory.md)