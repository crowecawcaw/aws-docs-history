

# Changing the delegated GuardDuty administrator account
<a name="change-guardduty-delegated-admin"></a>

You can remove the delegated GuardDuty administrator account for your organization in each Region and then delegate a new administrator in each Region. To maintain the security posture for your organization's member accounts in a Region, you must have a delegated GuardDuty administrator account in that Region.

**Note**  
Before you remove a delegated GuardDuty administrator account, you must disassociate all the member accounts associated with the delegated GuardDuty administrator account, and then delete them from the GuardDuty organization. For more information about these steps, see the following documents:  
[Disassociating (removing) member account from administrator account](disassociate-remove-member-account-from-admin.md)
[Deleting member accounts from GuardDuty organization](delete-member-accounts-guardduty-organization.md)

## Removing existing delegated GuardDuty administrator account
<a name="remove-existing-guardduty-delegated-admin"></a>

**Step 1 - To remove existing delegated GuardDuty administrator account in each Region**

1. As the existing delegated GuardDuty administrator account, list all the member accounts linked with your administrator account. Run [ListMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMembers.html) with `OnlyAssociated=false`.

1. If the auto-enable preference for GuardDuty or any of the optional protection plans is set to `ALL`, then run [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html) to update the organization configuration to either `NEW` or `NONE`. This action will prevent an error when you disassociate all the member accounts in the next step.

1. Run [DisassociateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateMembers.html) to disassociate all the member accounts that are associated with the administrator account.

1. Run [DeleteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html) to delete the associations between the administrator account and member accounts.

1. As the organization management account, run [DisableOrganizationAdminAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisableOrganizationAdminAccount.html) to remove the existing delegated GuardDuty administrator account.

1. Repeat these steps in each AWS Region where you have this delegated GuardDuty administrator account.

**Step 2 - To de-register existing delegated GuardDuty administrator account in AWS Organizations (One-time global action)**
+ Run [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html) in the *AWS Organizations API Reference*, to de-register the existing delegated GuardDuty administrator account in AWS Organizations. 

  Alternatively, you can run the following AWS CLI command:

  ```
  aws organizations deregister-delegated-administrator --account-id {{111122223333}} --service-principal guardduty.amazonaws.com
  ```

  Make sure to replace {{111122223333}} with the existing delegated GuardDuty administrator account.

  After you de-register the old delegated GuardDuty administrator account, you can add it as a member account to the new delegated GuardDuty administrator account.

## Designating a new delegated GuardDuty administrator account in each Region
<a name="designate-new-guardduty-delegated-admin"></a>

1. Designate a new delegated GuardDuty administrator account in each Region by using your preferred access method - GuardDuty console, or API or AWS CLI. For more information, see [Designating a delegated GuardDuty administrator account](delegated-admin-designate.md).

1. Run [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html) to view the current auto-enable configuration for your organization.
**Important**  
Before you add any members to the new delegated GuardDuty administrator account, you must verify the auto-enable configuration for your organization. This configuration is specific to the new delegated GuardDuty administrator account and the selected Region, and doesn't relate to AWS Organizations. When you add (a new or an existing) organization member account under the new delegated GuardDuty administrator account, the auto-enable configuration of the new delegated GuardDuty administrator account will apply at the time of enabling GuardDuty or any of its optional protection plans.

   Change the organization configuration for the new delegated GuardDuty administrator account by using your preferred access method - GuardDuty console, or API or AWS CLI. For more information, see [Setting organization auto-enable preferences](set-guardduty-auto-enable-preferences.md).