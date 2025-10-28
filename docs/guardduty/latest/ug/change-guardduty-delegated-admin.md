# Changing the delegated GuardDuty administrator account

You can remove the delegated GuardDuty administrator account for your organization in each Region and then delegate a
new administrator in each Region. To maintain the security posture for your
organization's member accounts in a Region, you must have a delegated GuardDuty administrator account in that
Region.

###### Note

Before you remove a delegated GuardDuty administrator account, you must disassociate all the member accounts
associated with the delegated GuardDuty administrator account, and then delete them from the GuardDuty organization. For
more information about these steps, see the following documents:

- [Disassociating
  (removing) member account from administrator account](disassociate-remove-member-account-from-admin.md "disassociate-remove-member-account-from-admin.md")
- [Deleting member accounts
  from GuardDuty organization](delete-member-accounts-guardduty-organization.md "delete-member-accounts-guardduty-organization.md")

## Removing existing

delegated GuardDuty administrator account

###### Step 1 - To remove existing delegated GuardDuty administrator account in each Region

1. As the existing delegated GuardDuty administrator account, list all the member accounts associated with your
   administrator account. Run [ListMembers](../APIReference/API_ListMembers.md "../APIReference/API_ListMembers.md") with
   `OnlyAssociated=false`.
2. If the auto-enable preference for GuardDuty or any of the optional protection
   plans is set to `ALL`, then run [UpdateOrganizationConfiguration](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md") to update
   the organization configuration to either `NEW` or
   `NONE`. This action will prevent an error when you
   disassociate all the member accounts in the next step.
3. Run [DisassociateMembers](../APIReference/API_DisassociateMembers.md "../APIReference/API_DisassociateMembers.md") to disassociate all the
   member accounts that are associated with the administrator account.
4. Run [DeleteMembers](../APIReference/API_DeleteMembers.md "../APIReference/API_DeleteMembers.md") to delete the associations
   between the administrator account and member accounts.
5. As the organization management account, run [DisableOrganizationAdminAccount](../APIReference/API_DisableOrganizationAdminAccount.md "../APIReference/API_DisableOrganizationAdminAccount.md") to remove
   the existing delegated GuardDuty administrator account.
6. Repeat these steps in each AWS Region where you have this
   delegated GuardDuty administrator account.

###### Step 2 - To de-register existing delegated GuardDuty administrator account in AWS Organizations (One-time global

action)

- Run [DeregisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md") in the
  _AWS Organizations API Reference_, to de-register the existing delegated GuardDuty administrator account
  in AWS Organizations.

Alternatively, you can run the following AWS CLI command:

```
aws organizations deregister-delegated-administrator --account-id `111122223333` --service-principal guardduty.amazonaws.com
```

Make sure to replace `111122223333`
with the existing delegated GuardDuty administrator account.

After you de-register the old delegated GuardDuty administrator account, you can add it as a member account
to the new delegated GuardDuty administrator account.

## Designating a new delegated GuardDuty administrator account

in each Region

1. Designate a new delegated GuardDuty administrator account in each Region by using your preferred access
   method - GuardDuty console, or API or AWS CLI. For more information, see [Designating a delegated GuardDuty administrator account](delegated-admin-designate.md "delegated-admin-designate.md").
2. Run [DescribeOrganizationConfiguration](../APIReference/API_DescribeOrganizationConfiguration.md "../APIReference/API_DescribeOrganizationConfiguration.md") to view the current
   auto-enable configuration for your organization.

###### Important

Before you add any members to the new delegated GuardDuty administrator account, you must verify the
auto-enable configuration for your organization. This configuration is
specific to the new delegated GuardDuty administrator account and the selected Region, and doesn't relate
to AWS Organizations. When you add (a new or an existing) organization member
account under the new delegated GuardDuty administrator account, the auto-enable configuration of the new
delegated GuardDuty administrator account will apply at the time of enabling GuardDuty or any of its optional
protection plans.

Change the organization configuration for the new delegated GuardDuty administrator account by using your
preferred access method - GuardDuty console, or API or AWS CLI. For more
information, see [Setting organization auto-enable
preferences](set-guardduty-auto-enable-preferences.md "set-guardduty-auto-enable-preferences.md").
