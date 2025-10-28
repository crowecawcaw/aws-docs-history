# Designating a delegated GuardDuty administrator account

This section provides steps to designate a delegated administrator in the GuardDuty
organization.

As a management account of the AWS organization, make sure that you read through the
[Considerations and
recommendations](guardduty_organizations.md#delegated_admin_important "guardduty_organizations.md#delegated_admin_important") on how a delegated GuardDuty administrator account operates. Before
proceeding, ensure that you have [Permissions required to designate a
delegated GuardDuty administrator account](organizations_permissions.md "organizations_permissions.md").

Choose a preferred access method to designate a delegated GuardDuty administrator account for your organization. Only a
management account can perform this step.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

To sign in, use the management account credentials for your
AWS Organizations organization. 2. By using the AWS Region selector in the upper-right corner of
the page, select the Region in which you want to designate the
delegated GuardDuty administrator account for your organization. 3. Do one of the following, depending on whether GuardDuty is enabled for
your management account in the current Region:

    * If GuardDuty is not enabled, select **Amazon GuardDuty - all
     features** and choose **Get
     started**. This action will take you to the
     **Welcome to GuardDuty** page.
    * If GuardDuty is enabled, choose **Settings**
     in the navigation pane.

4. Under **Delegated administrator**, enter the
   12-digit AWS account ID of the account that you want to designate
   as the delegated GuardDuty administrator account for the organization.

Make sure to enable GuardDuty for your newly designated delegated GuardDuty administrator account,
otherwise it won't be able to take any action. 5. Choose **Delegate**. 6. (Recommended) Repeat the preceding steps to designate the delegated GuardDuty administrator account
in each AWS Region where you have GuardDuty enabled.

API/CLI

1. Run [enableOrganizationAdminAccount](../APIReference/API_EnableOrganizationAdminAccount.md "../APIReference/API_EnableOrganizationAdminAccount.md") using
   the credentials of the AWS account of the organization's
   management account.
   - Alternatively, you can use AWS Command Line Interface to do this. The
     following AWS CLI command designates a delegated GuardDuty administrator account for your
     current Region only. Run the following AWS CLI command and
     make sure to replace
     `111111111111` with
     the AWS account ID of the account you want to designate as
     a delegated GuardDuty administrator account:

   ```
   aws guardduty enable-organization-admin-account --admin-account-id `111111111111`
   ```

   To designate the delegated GuardDuty administrator account for other Regions, specify the
   Region in the AWS CLI command. The following example
   demonstrates how to enable a delegated GuardDuty administrator account in US West (Oregon).
   Make sure to replace `us-west-2`
   with the Region for which you want to assign the
   delegated GuardDuty administrator account.

   ```
   aws guardduty enable-organization-admin-account --admin-account-id `111111111111` --region `us-west-2`
   ```

   For information about the AWS Regions where GuardDuty is
   available, see [Regions and endpoints](guardduty_regions.md "guardduty_regions.md").If GuardDuty is disabled for your delegated GuardDuty administrator account, it won't be able to take
   any action. If not already done so, make sure to enable GuardDuty for
   the newly designated delegated GuardDuty administrator account.

2. (Recommended) repeat the preceding steps to designate the delegated GuardDuty administrator account
   in each AWS Region where you have GuardDuty enabled.
