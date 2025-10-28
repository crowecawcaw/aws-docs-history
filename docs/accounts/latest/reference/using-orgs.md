# When to use AWS Organizations

AWS Organizations is an AWS service that you can use to manage your AWS accounts as a group.
This provides features like consolidated billing, where all of your accounts' bills are
grouped together and handled by a single payer. You can also centrally manage the security
of your organization by using policy based controls. For more information about AWS Organizations,
see the [AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").

**Trusted access**

When you use AWS Organizations to manage your accounts as a group, most administrative tasks for
the organization can be performed by only the organization's
_management account_. By default, this includes only operations
related to managing the organization itself. You can extend this additional functionality to
other AWS services by enabling _trusted access_ between
Organizations and that service. Trusted access grants permissions to the specified AWS service to
access information about the organization and the accounts it contains. When you enable
trusted access for Account Management, the Account Management service grants Organizations and its management account
permissions to access the metadata, such as the primary or alternate contact information,
for all of the organization's member accounts.

For more information, see [Enable trusted access for AWS Account Management](using-orgs-trusted-access.md "using-orgs-trusted-access.md").

**Delegated admin**

After you enable trusted access, you can also choose to designate one of your member
accounts as a _delegated admin_ account for AWS Account Management. This allows the
delegated admin account to perform the same Account Management metadata management tasks for the member
accounts in your organization that previously only the management account could do. The
delegated admin account can access only the management tasks for the Account Management service. The
delegated admin account doesn't have all of the administrative access to the organization
that the management account has.

For more information, see [Enable a delegated admin account for
AWS Account Management](using-orgs-delegated-admin.md "using-orgs-delegated-admin.md").

**Service control policies**

When your AWS account is part of an organization that is
managed by AWS Organizations, then the administrator of the organization can apply [service control
policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") that can limit what the principals in member accounts can do. An
SCP never grants permissions; instead, it is a filter that limits what permissions can be
used by the member account. A user or role (_a principal_) in a member
account can perform only those operations that are in the intersection of what is allowed by
the SCPs that apply to the account and the IAM permission policies attached to the
principal. For example, you can use SCPs to prevent any principal in an account from
modifying their own account's alternate contacts.

For example SCPs that apply to AWS accounts, see [Restrict access using AWS Organizations service control
policies](using-orgs-example-scps.md "using-orgs-example-scps.md").
