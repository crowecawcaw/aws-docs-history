# IAM Access Analyzer findings

IAM Access Analyzer generates findings for external access, internal access, and unused access in
your AWS account or organization.

For external access, IAM Access Analyzer generates a finding for each instance of a resource-based
policy that grants access to a resource within your zone of trust to a principal that is not
within your zone of trust. When you create an external access analyzer, you choose an organization
or AWS account to analyze. Any principal in the organization or account that you choose for the
analyzer is considered trusted. Because principals in the same organization or account are
trusted, the resources and principals within the organization or account comprise the zone of
trust for the analyzer. Any sharing that is within the zone of trust is considered safe, so
IAM Access Analyzer does not generate a finding. For example, if you select an organization as the zone
of trust for an analyzer, all resources and principals in the organization are within the zone of
trust. If you grant permissions to an Amazon S3 bucket in one of your organization member accounts to a
principal in another organization member account, IAM Access Analyzer does not generate a finding. But
if you grant permission to a principal in an account that is not a member of the organization,
IAM Access Analyzer generates a finding.

For internal access, IAM Access Analyzer generates findings when there is a possible access path
between an IAM role or user within your organization and your specified resources. Similar to
external access analysis, the scope you choose (organization or account) determines what is
considered internal. If you select an organization as the scope, IAM Access Analyzer will generate
findings for access paths between principals and resources within your organization. If you select
an account, findings will be generated for access paths within that specific account.
IAM Access Analyzer uses automated reasoning to evaluate all IAM policies to monitor who has access to
your resources.

The combination of external and internal access findings with the same zone of trust provides
a comprehensive analysis of all possible access to a particular resource, both from within and
outside your defined trust boundary.

For unused access, IAM Access Analyzer generates findings for unused access granted in your AWS
organization and accounts. When you create an unused access analyzer, IAM Access Analyzer continuously
monitors all IAM roles and users in your AWS organization and accounts and generates findings
for unused access. IAM Access Analyzer generates the following types of findings for unused
access:

- **Unused roles** – Roles with no access activity within
  the specified usage window.
- **Unused IAM user access keys and passwords** –
  Credentials belonging to IAM users that have not been used to access your AWS account in the
  specified usage window.
- **Unused permissions** – Service-level and action-level
  permissions that weren't used by a role within the specified usage window. IAM Access Analyzer uses
  identity-based policies attached to roles to determine the services and actions that those roles
  can access. IAM Access Analyzer supports review of unused permissions for all service-level
  permissions. For a complete list of action-level permissions that are supported for unused
  access findings, see [IAM action last
  accessed information services and actions](access_policies_last-accessed-action-last-accessed.md "access_policies_last-accessed-action-last-accessed.md").

###### Note

IAM Access Analyzer offers external access findings for free. There are charges for unused access
findings based on the number of IAM roles and users analyzed per analyzer per month. There are
also charges for internal access findings based on the number of AWS resources monitored per
analyzer per month. For more details about pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

###### Topics

- [Understand how IAM Access Analyzer findings work](access-analyzer-concepts.md "access-analyzer-concepts.md")
- [Getting started with
  AWS Identity and Access Management Access Analyzer](access-analyzer-getting-started.md "access-analyzer-getting-started.md")
- [View the IAM Access Analyzer findings
  dashboard](access-analyzer-dashboard.md "access-analyzer-dashboard.md")
- [Review IAM Access Analyzer findings](access-analyzer-findings-view.md "access-analyzer-findings-view.md")
- [Filter IAM Access Analyzer findings](access-analyzer-findings-filter.md "access-analyzer-findings-filter.md")
- [Archive IAM Access Analyzer findings](access-analyzer-findings-archive.md "access-analyzer-findings-archive.md")
- [Resolve IAM Access Analyzer findings](access-analyzer-findings-remediate.md "access-analyzer-findings-remediate.md")
- [IAM Access Analyzer error findings](access-analyzer-error-findings.md "access-analyzer-error-findings.md")
- [IAM Access Analyzer supported resource types for
  external and internal access](access-analyzer-resources.md "access-analyzer-resources.md")
- [Delegated administrator for
  IAM Access Analyzer](access-analyzer-delegated-administrator.md "access-analyzer-delegated-administrator.md")
- [Archive rules](access-analyzer-archive-rules.md "access-analyzer-archive-rules.md")
- [Monitoring AWS Identity and Access Management Access Analyzer with
  Amazon EventBridge](access-analyzer-eventbridge.md "access-analyzer-eventbridge.md")
- [Integrate IAM Access Analyzer with
  AWS Security Hub](access-analyzer-securityhub-integration.md "access-analyzer-securityhub-integration.md")
- [Logging IAM Access Analyzer API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [IAM Access Analyzer filter keys](access-analyzer-reference-filter-keys.md "access-analyzer-reference-filter-keys.md")
- [Using service-linked roles for
  AWS Identity and Access Management Access Analyzer](access-analyzer-using-service-linked-roles.md "access-analyzer-using-service-linked-roles.md")
