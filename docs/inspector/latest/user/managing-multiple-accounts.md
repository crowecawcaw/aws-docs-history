# Managing multiple accounts in Amazon Inspector with AWS Organizations

You can use Amazon Inspector to manage multiple accounts in [an organization](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").
Amazon Inspector supports two approaches for multi-account management:

- **Delegated administrator for AWS Organizations policies** - Provides centralized governance to delegated administrator with automatic enablement of Amazon Inspector across organization accounts across regions.
  Organization policies enforce which scan types are enabled and take precedence over non policy managed delegated administrator and member account enablements.
- **Delegated administrator for non AWS Organizations policy** - An account designated to manage Amazon Inspector for the organization without using organization policies.
  The delegated administrator can enable Amazon Inspector for member accounts and configure scan settings.

These approaches can be used together.
When organization policies are in place, they control resource type enablement (which scan types are enabled), while delegated administrators retain control over scan configuration settings such as scan modes and deep inspection paths.
The following topics describe these management approaches, how to designate a delegated administrator, and how to manage member accounts.

###### Topics

- [Understanding the delegated administrator account and member account in Amazon Inspector](admin-member-relationship.md "admin-member-relationship.md")
- [Designating a delegated administrator account for Amazon Inspector](designating-admin.md "designating-admin.md")
