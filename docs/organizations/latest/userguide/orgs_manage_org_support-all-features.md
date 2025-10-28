# Enabling all features for an organization with AWS Organizations

AWS Organizations has two available feature sets:

- [All features](orgs_getting-started_concepts.md#feature-set-all "orgs_getting-started_concepts.md#feature-set-all") – This feature set is
  the preferred and default way to work with AWS Organizations, and it includes all the features of consolidating billing.
  When you create an organization, enabling all features is the default.
  With all features enabled, you can use the advanced account management features
  available in Organizations such as [integration with supported AWS services](orgs_integrate_services_list.md "orgs_integrate_services_list.md") and [organization policies](orgs_manage_policies.md "orgs_manage_policies.md").
- [Consolidated billing features](orgs_getting-started_concepts.md#feature-set-cb-only "orgs_getting-started_concepts.md#feature-set-cb-only") –
  This feature set is limited to generating a single bill across an organization. No other management capabilities are available with consolidated billing.
  If you create an organization with the consolidated billing feature set, you can later
  enable all features. However, you cannot migrate from all features to consolidated billing after all features is enabled.

**Standard migration and assisted migration**

The two approaches for migrating to all features are _standard migration_ and _assisted migration_.

Standard migration is the self-service process available to all AWS Organizations customers to enable the all features mode.

Assisted migration is process available to Enterprise Support plan customers to request that AWS migrate their organization to the all features mode of your behalf.

###### Note

**One-way processes and rollback processes**

- The migration from consolidated billing features to all features is one-way.
  You can't switch an organization with all features enabled back to consolidated
  billing features only.
- After you have begun the assisted migration process, it cannot be rolled back.
  You will need to wait 90 days until the process expires if you want to go through the standard process instead.

###### Topics

- [Considerations](#before-enabling-all "#before-enabling-all")
- [Standard migration process](manage-begin-all-features-standard-migration.md "manage-begin-all-features-standard-migration.md")
- [Assisted migration process](manage-begin-all-features-assisted-migration.md "manage-begin-all-features-assisted-migration.md")

## Considerations

Before changing from an organization that supports only consolidated billing features
to an organization supporting all features, consider the following:

**Invited accounts must approve the migration**

When you start the process to enable all features, AWS Organizations sends a request to
every member account that you _invited_ to join
your organization. Every invited account must approve enabling all features by
accepting the request. Only then can you complete the process to enable all
features in your organization. If an account declines the request, you must
either remove the account from your organization or resend the request. The
request must be accepted before you can complete the process to enable all
features. Accounts that you _created_ using
AWS Organizations don't get a request because they don't need to approve the additional
control.

**Invited accounts are notified which feature set is currently enabled**

The owner of an invited account is informed by the invitation whether
they are joining an organization with consolidated billing only, or with all
features enabled. You can continue inviting accounts to your organization while enabling all
features.

If you invite an account _during_ the
process to enable all features, the invitation states that the
organization they are joining has all features enabled. If you cancel
the process to enable all features before the account accepts the
invitation, that invitation is canceled. You must invite the account
again to be a member of an organization with consolidated billing
features only.

If you invite an account and the invitation is not yet accepted
_before_ you begin the process to
enable all features, that invitation is canceled because the invitation
states that the organization has consolidated billing features only. You
must invite the account again to be a member of an organization with all
features enabled.

**The process of creating accounts in an organization is unaffected by the migration**

You can continue creating accounts in the organization. That process
isn't affected by this change.

**The service-linked role `AWSServiceRoleForOrganizations` is required**

AWS Organizations verifies that every member account has a service-linked role named
`AWSServiceRoleForOrganizations`. This role is mandatory in all accounts to enable
all features. If you deleted the role in an invited account, accepting the
invitation to enable all features recreates the role. If you deleted the role in
an account that was created using AWS Organizations, that account receives an invitation
specifically to recreate that role. All of these invitations must be accepted
for the organization to complete the process of enabling all features.
