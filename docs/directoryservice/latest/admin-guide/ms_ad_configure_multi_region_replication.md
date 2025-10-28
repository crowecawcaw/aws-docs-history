# Configure Multi-Region

replication for AWS Managed Microsoft AD

Multi-Region replication can be used to automatically replicate your AWS Managed Microsoft AD directory
data across multiple AWS Regions. This replication can improve performance for users and
applications in disperse geographic locations. AWS Managed Microsoft AD uses native Active Directory replication to
replicate your directory's data securely to the new Region.

Multi-Region replication is only supported for the **Enterprise Edition**
of AWS Managed Microsoft AD.

You can use automated multi-Region replication in most Regions where AWS Managed Microsoft AD is
available.

###### Important

Multi-Region replication is unavailable in opt-in Regions. The following are opt-in Regions:

- Africa (Cape Town) af-south-1
- Asia Pacific (Hong Kong) ap-east-1
- Asia Pacific (Hyderabad) ap-south-2
- Asia Pacific (Jakarta) ap-southeast-3
- Asia Pacific (Melbourne) ap-southeast-4
- Asia Pacific (Thailand) ap-southeast-7
- Canada West (Calgary) ca-west-1
- Europe (Milan) eu-south-1
- Europe (Spain) eu-south-2
- Europe (Zurich) eu-central-2
- Israel (Tel Aviv) il-central-1
- Middle East (Bahrain) me-south-1
- Middle East (UAE) me-central-1
- Mexico (Central) mx-central-1
  For more information about opt-in Regions and how to enable them, see [Specify which
  AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management
  Guide_.

## How Multi-Region replication works

With the Multi-Region replication feature, AWS Managed Microsoft AD eliminates the undifferentiated
heavy lifting of managing a global Active Directory infrastructure. When configured, AWS
replicates all customer directory data including users, groups, group policies, and schema
across multiple AWS Regions.

Once a new Region has been added, the following operations automatically occur as shown in
the illustration:

- AWS Managed Microsoft AD creates two domain controllers in the selected VPC and deploys them to
  the new Region in the same AWS account. Your directory identifier
  (`directory_id`) remains the same across all Regions. You can add additional
  domain controllers later if you want.
- AWS Managed Microsoft AD configures the networking connection between the primary Region and the
  new Region.
- AWS Managed Microsoft AD creates a new Active Directory site and gives it the same name as the Region, such as
  us-east-1. You can also rename this later using the Active Directory Sites and Services
  tool.
- AWS Managed Microsoft AD replicates all Active Directory objects and configurations to the new
  Region, including users, groups, group policies, Active Directory trusts, organizational
  units, and Active Directory schema. Active Directory site links are configured to use
  [Change Notification](https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/modify-default-intra-site-dc-replication-interval "https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/modify-default-intra-site-dc-replication-interval"). With change notification between sites enabled, changes
  propagate to the remote site with the same frequency that they are propagated within the
  source site, including changes that warrant urgent replication.
- If this is the first Region you've added, AWS Managed Microsoft AD makes all features multi-Region
  aware. For more information, see [Global vs Regional features](multi-region-global-region-features.md "multi-region-global-region-features.md").

![Multi-region replication of a AWS Managed Microsoft AD Active Directory between a primary region and an additional region.](images/multiregion.png)

### Active Directory sites

Multi-Region replication supports multiple Active Directory sites (one Active Directory site per Region). When a
new Region is added, it is given the same name as the Region—for example, us-east-1.
You can also rename this later using Active Directory Sites and Services.

### AWS services

AWS services such as Amazon RDS for SQL Server and Amazon FSx connect to the local instances
of the global directory. This allows your users to sign in once to Active Directory-aware applications
that run in AWS as well as AWS services like Amazon RDS for SQL Server in any AWS Region.
To do so, users need credentials from AWS Managed Microsoft AD or on-premises Active Directory when you have a trust
with your AWS Managed Microsoft AD.

You can use the following AWS services with the multi-Region replication
feature.

- Amazon EC2
- Amazon FSx for Windows File Server
- Amazon Relational Database Service for SQL Server
- Amazon RDS for Oracle
- Amazon RDS for MySQL
- Amazon RDS for PostgreSQL
- Amazon RDS for MariaDB
- Amazon Aurora for MySQL
- Amazon Aurora for PostgreSQL

### Failover

In the event that all domain controllers in one Region are down, AWS Managed Microsoft AD recovers
the domain controllers and replicates the directory data automatically. Meanwhile domain
controllers in other Regions stay up and running.

## Benefits of multi-Region replication

With multi-Region replication in AWS Managed Microsoft AD, Active Directory-aware applications use the directory
locally for high performance and the multi-Region feature for resiliency. You can use
multi-Region replication with Active Directory-aware applications like SharePoint and SQL Server Always On
as well as AWS services like Amazon RDS for SQL Server and FSx for Windows File Server. The following are
additional benefits of multi-Region replication.

- It lets you deploy a single AWS Managed Microsoft AD instance globally, quickly, and eliminates
  the heavy lifting of self-managing a global Active Directory infrastructure.
- It makes it easier and more cost-effective for you to deploy and manage Windows and
  Linux workloads in multiple AWS Regions. Automated multi-Region replication enables
  optimal performance in your global Active Directory-aware applications. All applications deployed in
  Windows or Linux instances use AWS Managed Microsoft AD locally in the Region, which enables responses
  to user requests from the closest Region possible.
- It provides multi-Region resiliency. Deployed in the highly available AWS managed
  infrastructure, AWS Managed Microsoft AD handles automated software updates, monitoring, recovery, and
  the security of the underlying Active Directory infrastructure across all Regions. This allows you to
  focus on building your applications.

###### Topics

- [Global vs Regional features](multi-region-global-region-features.md "multi-region-global-region-features.md")
- [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md")
- [Adding a replicated Region for AWS Managed Microsoft AD](multi-region-add-region.md "multi-region-add-region.md")
- [Deleting a replicated Region for AWS Managed Microsoft AD](multi-region-delete-region.md "multi-region-delete-region.md")
