

# Enabling EKS Protection in multiple-account environments
<a name="eks-protection-enable-multiple-accounts"></a>

In a multiple-account environment, only the delegated GuardDuty administrator account has the option to enable or disable the EKS Protection; feature for the member accounts in their organization. The GuardDuty member accounts can't modify this configuration from their accounts. The delegated GuardDuty administrator account manages their member accounts using AWS Organizations. This delegated GuardDuty administrator account can choose to auto-enable EKS Protection for all the new accounts as they join the organization. For more information about multiple-account environments, see [Managing multiple accounts in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html).

## Configuring EKS Audit Log Monitoring for delegated GuardDuty administrator account
<a name="configure-eks-audit-log-monitoring-delegatedadmin"></a>

Choose your preferred access method to configure EKS Audit Log Monitoring for the delegated GuardDuty administrator account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **EKS Audit Logs**, you can view the current configuration status of EKS Audit Log Monitoring.

1. Do one of the following:

**Using **Enable for all accounts****
   + Choose **Enable for all accounts**. This will enable the protection plan for all the active GuardDuty accounts in your AWS organization, including the new accounts that join the organization.
   + Choose **Save**.

**Using **Configure accounts manually****
   + To enable the protection plan only for the delegated GuardDuty administrator account account, choose **Configure accounts manually**.
   + Choose **Enable** under the **delegated GuardDuty administrator account (this account)** section.
   + Choose **Save**.

------
#### [ API/CLI ]

Run the [updateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API operation using your own regional detector ID and passing the `features` object `name` as `EKS_AUDIT_LOGS` and `status` as `ENABLED` or `DISABLED`.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

You can enable or disable EKS Audit Log Monitoring by running the following AWS CLI command. Make sure to use delegated GuardDuty administrator account's valid {{detector ID}}. 

**Note**  
The following example code enables EKS Audit Log Monitoring. Make sure to replace {{12abc34d567e8fa901bc2d34e56789f0}} with the `detector-id` of the delegated GuardDuty administrator account and {{555555555555}} with the AWS account of the delegated GuardDuty administrator account. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --features '[{"Name": "EKS_AUDIT_LOGS", "Status": "{{ENABLED}}"}]'
```

To disable EKS Audit Log Monitoring, replace `ENABLED` with `DISABLED`.

------

## Auto-enable EKS Audit Log Monitoring for all member accounts
<a name="k8s-autoenable"></a>

Choose your preferred access method to enable the EKS Audit Log Monitoring for existing member accounts in your organization.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. Do one of the following:

**Using the **Protection Plans** page**

   1. In the navigation pane, choose **Protection Plans**.

   1. Choose **Configure all enablements**. Under **EKS Audit Logs**, you can view the current status of EKS Audit Log Monitoring for active member accounts in your organization. 

   1. Choose **Enable for all accounts**. This action automatically enables EKS Audit Log Monitoring for both the existing and new accounts in the organization.

   1. Choose **Save all**, then choose **Confirm and save**.
**Note**  
It may take up to 24 hours to update the configuration for the member accounts.

**Using the **Accounts** page**

   1. In the navigation pane, choose **Accounts**.

   1. On the **Accounts** page, choose **Auto-enable** preferences before **Add accounts by invitation**.

   1. In the **Manage auto-enable preferences** window, choose **Enable for all accounts** under **EKS Audit Log Monitoring**.

   1. Choose **Save**.

   If you can't use the **Enable for all accounts** option and want to customize EKS Audit Log Monitoring configuration for specific accounts in your organization, see [Selectively enable or disable EKS Audit Log Monitoring for member accounts](#k8s-enable-disable-selective-members-org).

------
#### [ API/CLI ]
+ To selectively enable or disable EKS Audit Log Monitoring for your member accounts, run the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. 
+ The following example shows how you can enable EKS Audit Log Monitoring for a single member account. To disable it, replace `ENABLED` with `DISABLED`. 

  To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --account-ids {{111122223333}} --features '[{"name": "EKS_AUDIT_LOGS", "status": "{{ENABLED}}"}]'
  ```
**Note**  
You can also pass a list of account IDs separated by a space.
+ When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------

## Enable EKS Audit Log Monitoring for all existing active member accounts
<a name="enable-for-all-existing-members-eks-audit-log"></a>

Choose your preferred access method to enable EKS Audit Log Monitoring for all existing active member accounts in the organization.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Sign in using the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **EKS Audit Logs**, under the **Active member accounts** section, choose **Actions**.

1. From the **Actions** dropdown menu, choose **Enable for all existing active member accounts**.

1. Choose **Save**.

------
#### [ API/CLI ]
+ To selectively enable or disable EKS Audit Log Monitoring for your member accounts, run the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. 
+ The following example shows how you can enable EKS Audit Log Monitoring for a single member account. To disable it, replace `ENABLED` with `DISABLED`. 

  To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --account-ids {{111122223333}} --features '[{"name": "EKS_AUDIT_LOGS", "status": "{{ENABLED}}"}]'
  ```
**Note**  
You can also pass a list of account IDs separated by a space.
+ When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------

## Auto-enable EKS Audit Log Monitoring for new member accounts
<a name="k8s-auto-enable-new-member-org"></a>

The newly added member accounts must **Enable** GuardDuty before selecting configuring GuardDuty-initiated malware scan. The member accounts managed by invitation can configure GuardDuty-initiated malware scan manually for their accounts. For more information, see [Step 3 - Accept an invitation](guardduty_become_console.md#guardduty_accept_invite_proc).

Choose your preferred access method to enable EKS Audit Log Monitoring for new accounts that join your organization.

------
#### [ Console ]

The delegated GuardDuty administrator account can enable EKS Audit Log Monitoring for new member accounts in an organization, using either the **EKS Audit Log Monitoring** or **Accounts** page.

**To auto-enable EKS Audit Log Monitoring for new member accounts**

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. Do one of the following:
   + Using the **Protection Plans** page:

     1. In the navigation pane, choose **Protection Plans**.

     1. Choose **Configure all enablements**. Under **EKS Audit Logs**, configure the auto-enable setting.

     1. Choose **Configure accounts manually**.

     1. Select **Automatically enable for new member accounts**. This step ensures that whenever a new account joins your organization, EKS Audit Log Monitoring will be automatically enabled for their account. Only the organization delegated GuardDuty administrator account can modify this configuration.

     1. Choose **Save**.
   + Using the **Accounts** page:

     1. In the navigation pane, choose **Accounts**.

     1. On the **Accounts** page, choose **Auto-enable** preferences.

     1. In the **Manage auto-enable preferences** window, select **Enable for new accounts** under **EKS Audit Log Monitoring**.

     1. Choose **Save**.

------
#### [ API/CLI ]
+ To selectively enable or disable EKS Audit Log Monitoring for your new accounts, run the [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html) API operation using your own {{detector ID}}. 
+ The following example shows how you can enable EKS Audit Log Monitoring for the new members that join your organization. You can also pass a list of account IDs separated by a space.

  To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty update-organization-configuration --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --auto-enable --features '[{"Name": "EKS_AUDIT_LOGS", "AutoEnable": "NEW"}]'
  ```

------

## Selectively enable or disable EKS Audit Log Monitoring for member accounts
<a name="k8s-enable-disable-selective-members-org"></a>

Choose your preferred access method to enable or disable EKS Audit Log Monitoring for selective member accounts in your organization.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Accounts**.

   On the **Accounts** page, review the **EKS Audit Log Monitoring** column for the status of your member account. 

1. 

**To enable or disable EKS Audit Log Monitoring**

   Select an account that you want to configure for EKS Audit Log Monitoring. You can select multiple accounts at a time. Under the **Edit Protection Plans** dropdown, choose **EKS Audit Log Monitoring**, and then choose the appropriate option.

------
#### [ API/CLI ]

To selectively enable or disable EKS Audit Log Monitoring for your member accounts, invoke the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. 

The following example shows how you can enable EKS Audit Log Monitoring for a single member account. To disable it, replace `ENABLED` with `DISABLED`. You can also pass a list of account IDs separated by a space.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --accountids {{111122223333}} --features '[{"Name": "EKS_AUDIT_LOGS", "Status": "{{ENABLED}}"}]'
```

------