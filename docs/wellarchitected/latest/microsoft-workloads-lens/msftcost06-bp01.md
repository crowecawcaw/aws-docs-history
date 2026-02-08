# MSFTCOST06-BP01 Use AWS Managed Microsoft Active

Directory

AWS Managed Microsoft AD provides redundant Windows Server domain
controllers across two Availability Zones in your VPC. It handles
all maintenance tasks automatically, including monitoring,
replication, backups, and updates. The service supports
directory-aware workloads like SharePoint and .NET applications, and
can integrate with on-premises Active Directory through trust
relationships. Based on size requirements, you can either choose the
Standard or the Enterprise edition.

**Desired outcome:** By implementing
AWS Managed Microsoft Active Directory, you aim to reduce
operational overhead and costs associated with managing Active
Directory in the AWS Cloud. This solution provides a highly
available, fully managed directory service that automatically
handles maintenance tasks, supports directory-aware workloads, and
enables integration with on-premises Active Directory. The result is
a more efficient, scalable, and cost-effective approach to directory
services in your cloud environment.

**Common anti-patterns:**

- Managing your own domain controllers on EC2 instances, resulting
  in unnecessary operational overhead from manual patching,
  backups, monitoring, and high availability configuration.
- Creating multiple standalone Active Directory environments
  across different workloads instead of using a centralized
  managed service, leading to increased costs and management
  complexity.

**Benefits of establishing this best
practice:**

- Reduced operational overhead: AWS handles maintenance tasks such
  as patching, backups, and monitoring, freeing up IT staff to
  focus on core business activities.
- Improved reliability and availability: The service automatically
  deploys domain controllers across multiple Availability Zones,
  ensuring high availability and disaster recovery capabilities.
- Seamless integration: Enables easy connection with on-premises
  Active Directory through trust relationships, facilitating
  hybrid cloud scenarios and simplifying user access management
  across environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement AWS Managed Microsoft AD effectively, start by
assessing your directory service needs and selecting the
appropriate edition (Standard or Enterprise) based on your
organization's size and requirements. Plan your VPC and network
configuration to ensure proper connectivity for your domain
controllers. If you have an existing on-premises Active Directory,
establish a trust relationship to enable seamless integration.
Migrate your directory-aware workloads gradually, beginning with
less critical applications to gain experience and confidence.
Leverage AWS IAM Identity Center for unified access management
across your AWS environment. Finally, regularly review and
optimize your setup to ensure it continues to meet your evolving
needs while maximizing cost efficiency.

### Implementation steps

1. Prepare your environment by configuring VPC with appropriate
   subnets across multiple AZs and setting up required network
   connectivity for hybrid scenarios
2. Deploy AWS Managed Microsoft AD by selecting the appropriate
   edition, choosing target VPC and subnets, and configuring
   directory administrator credentials and DNS settings
3. Establish connectivity and access through security group
   configuration, trust relationship setup with on-premises AD
   if needed, and AWS IAM Identity Center integration
4. Migrate workloads gradually, starting with test
   applications, followed by directory-aware workloads, while
   updating DNS settings and application configurations
5. Monitor and maintain the environment using CloudWatch
   metrics, managing directory users and groups, and performing
   regular access permission audits

## Resources

**Related documents:**

- [AWS Managed Microsoft AD](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-aws-managed.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-aws-managed.md")
- [How
  to migrate your on-premises domain to AWS Managed Microsoft AD
  using ADMT](https://aws.amazon.com/blogs/security/how-to-migrate-your-on-premises-domain-to-aws-managed-microsoft-ad-using-admt/ "https://aws.amazon.com/blogs/security/how-to-migrate-your-on-premises-domain-to-aws-managed-microsoft-ad-using-admt/")
