

# Consolidating GuardDuty administrator accounts under a single organization
<a name="consolidate-orgs"></a>

GuardDuty recommends using association through AWS Organizations to manage member accounts under a delegated GuardDuty administrator account. You can use the example process outlined below to consolidate administrator account and member associated by invitation in an organization under a single GuardDuty delegated GuardDuty administrator account.

**Note**  
GuardDuty recommends using AWS Organizations instead of GuardDuty invitations, to manage your member accounts. For more information, see [Managing accounts with AWS Organizations](guardduty_organizations.md).

Accounts that are already being managed by a delegated GuardDuty administrator account, or active member accounts that are associated with delegated GuardDuty administrator account can't be added to a different delegated GuardDuty administrator account. Each organization can have only one delegated GuardDuty administrator account per Region, and each member account can have only one delegated GuardDuty administrator account.

Choose a preferred access method to consolidate GuardDuty administrator accounts under a single delegated GuardDuty administrator account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   To log in, use the credentials of the management account of the organization.

1. All the accounts for which you want to manage GuardDuty must be a part of your organization. For information about adding an account to your organization, see [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html). 

1. Make sure all the member accounts are associated with the account that you want to designate as the single delegated GuardDuty administrator account. Disassociate any member account that is still associated with the pre-existing administrator accounts.

   The following steps will help you disassociate member accounts from the pre-existing administrator account:

   1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   1. To log in, use the credentials of the pre-existing administrator account.

   1. In the navigation pane, choose **Accounts**.

   1. On the **Accounts** page, select one or more accounts that you want to disassociate from the administrator account.

   1. Choose **Actions** and then choose **Disassociate account**.

   1. Choose **Confirm** to finalize the step.

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   To log in, use the management account credentials.

1. In the navigation pane, choose **Settings**. On the **Settings** page, designate the delegated GuardDuty administrator account for the organization.

1. Log in to the designated delegated GuardDuty administrator account.

1. Add members from the organization. For more information, see [Managing GuardDuty accounts with AWS Organizations](guardduty_organizations.md).

------
#### [ API/CLI ]

1. All the accounts for which you want to manage GuardDuty must be a part of your organization. For information about adding an account to your organization, see [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html). 

1. Make sure all the member accounts are associated with the account that you want to designate as the single delegated GuardDuty administrator account. 

   1. Run [DisassociateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateMembers.html) to disassociate any member account that is still associated with the pre-existing administrator accounts.

   1. Alternatively, you can use AWS Command Line Interface to run the following command and replace {{777777777777}} with the detector ID of the pre-existing administrator account from which you want to disassociate the member account. Replace {{666666666666}} with the AWS account ID of the member account that you want to disassociate. 

      ```
      aws guardduty disassociate-members --detector-id {{777777777777}} --account-ids {{666666666666}}    
      ```

1. Run [EnableOrganizationAdminAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EnableOrganizationAdminAccount.html) to delegate an AWS account as the delegated GuardDuty administrator account.

   Alternatively, you can use AWS Command Line Interface to run the following command to delegate a delegated GuardDuty administrator account:

   ```
   aws guardduty enable-organization-admin-account --admin-account-id {{777777777777}}
   ```

1. Add members from the organization. For more information, see [Create or add member member accounts using API](guardduty_become_console.md#guardduty_become_api).

------

**Important**  
To maximize the effectiveness of GuardDuty, a regional service, we recommend that you designate your delegated GuardDuty administrator account and add all your member accounts in every Region.