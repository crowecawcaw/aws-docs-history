# Enabling RDS Protection in multiple-account

environments

In a multiple-account environment, only the delegated GuardDuty administrator account has the option to enable or disable
the RDS Protection feature for the member accounts in their organization. The GuardDuty member accounts
can't modify this configuration from their accounts. The delegated GuardDuty administrator account manages their member accounts
using AWS Organizations. This delegated GuardDuty administrator account can choose to auto-enable RDS login activity monitoring for all the
new accounts as they join the organization. For more information about multiple-account
environments, see [Multiple accounts in GuardDuty](guardduty_accounts.md "guardduty_accounts.md").

Choose your preferred access method to configure RDS Login Activity Monitoring for the
delegated GuardDuty administrator account.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **RDS Protection**.
3. On the **RDS Protection** page, choose
   **Edit**.
4. Do one of the following:

###### Using **Enable for all accounts**

    * Choose **Enable for all accounts**. This will enable
     the protection plan for all the active GuardDuty accounts in your AWS organization, including the new accounts that
     join the organization.
    * Choose **Save**.

###### Using **Configure accounts manually**

    * To enable the protection plan only for the delegated GuardDuty administrator account account, choose
     **Configure accounts manually**.
    * Choose **Enable** under the
     **delegated GuardDuty administrator account (this account)** section.
    * Choose **Save**.

API/CLI
Run the [updateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md") API operation using your own regional
detector ID and passing the `features` object `name` as
`RDS_LOGIN_EVENTS` and `status` as
`ENABLED`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command,
and replace `12abc34d567e8fa901bc2d34e56789f0` with your
account's detector ID and `us-east-1` with the Region where
you want to enable RDS Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --features '[{"Name": "RDS_LOGIN_EVENTS", "Status": "ENABLED"}]'
```

Choose your preferred access method to enable the RDS Protection feature for all member
accounts. This includes existing member accounts and the new accounts that join the
organization.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Make sure to use the delegated GuardDuty administrator account credentials. 2. Do one of the following:

###### Using the **RDS Protection** page

    1. In the navigation pane, choose **RDS Protection**.
    2. Choose **Enable for all accounts**. This action
     automatically enables RDS Protection for both existing and new accounts in the
     organization.
    3. Choose **Save**.


    ###### Note

    It may take up to 24 hours to update the configuration for the member accounts.

###### Using the **Accounts** page

    1. In the navigation pane, choose **Accounts**.
    2. On the **Accounts** page, choose
     **Auto-enable** preferences before **Add accounts
     by invitation**.
    3. In the **Manage auto-enable preferences** window,
     choose **Enable for all accounts** under
     **RDS Login Activity Monitoring**.
    4. Choose **Save**.

If you can't use the **Enable for all accounts** option,
see [Selectively enable RDS Protection for
member accounts](#enable-disable-rds-pro-selectively "#enable-disable-rds-pro-selectively").

API/CLI
To selectively enable or disable RDS Protection for your member accounts, invoke the
[updateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md") API operation using your own
`detector ID`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command,
and replace `12abc34d567e8fa901bc2d34e56789f0` with your
account's detector ID and `us-east-1` with the Region where
you want to enable RDS Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-member-detectors --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --account-ids `111122223333` --features '[{"name": "RDS_LOGIN_EVENTS", "status": "`ENABLED`"}]'
```

You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of
`UnprocessedAccounts`. If there were any problems changing the detector
settings for an account, that account ID is listed along with a summary of the
issue.

Choose your preferred access method to enable RDS Protection for all the existing active
member accounts in your organization. The member accounts that already have GuardDuty enabled,
are referred to as existing active members.

Console

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Sign in using the delegated GuardDuty administrator account credentials. 2. In the navigation pane, choose **RDS Protection**. 3. On the **RDS Protection** page, you can view the current status
of the configuration. Under the **Active member accounts**
section, choose **Actions**. 4. From the **Actions** dropdown menu, choose **Enable
for all existing active member accounts**. 5. Choose **Confirm**.

API/CLI
Run the [updateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md") API operation using your own
`detector ID`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command,
and replace `12abc34d567e8fa901bc2d34e56789f0` with your
account's detector ID and `us-east-1` with the Region where
you want to enable RDS Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-member-detectors --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --account-ids `111122223333` --features '[{"name": "RDS_LOGIN_EVENTS", "status": "`ENABLED`"}]'
```

You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of
`UnprocessedAccounts`. If there were any problems changing the detector
settings for an account, that account ID is listed along with a summary of the
issue.

Choose your preferred access method to enable RDS login activity for new accounts that
join your organization.

Console
The delegated GuardDuty administrator account can enable for new member accounts in an organization through the
console, using either the **RDS Protection** or
**Accounts** page.

###### To auto-enable RDS Protection for new member accounts

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Make sure to use the delegated GuardDuty administrator account credentials. 2. Do one of the following:

    * Using the **RDS Protection** page:




    	1. In the navigation pane, choose **RDS Protection**.
    	2. On the **RDS Protection** page, choose
    	 **Edit**.
    	3. Choose **Configure accounts manually**.
    	4. Select **Automatically enable for new member
    	 accounts**. This step ensures that whenever a new account
    	 joins your organization, RDS Protection will be automatically enabled for
    	 their account. Only the organization delegated GuardDuty administrator account can modify this
    	 configuration.
    	5. Choose **Save**.
    * Using the **Accounts** page:




    	1. In the navigation pane, choose **Accounts**.
    	2. On the **Accounts** page, choose
    	 **Auto-enable** preferences.
    	3. In the **Manage auto-enable preferences** window,
    	 select **Enable for new accounts** under
    	 **RDS Login Activity Monitoring**.
    	4. Choose **Save**.

API/CLI
To selectively enable or disable RDS Protection for your member accounts, invoke the
[UpdateOrganizationConfiguration](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md") API operation using your
own `detector ID`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command,
and replace `12abc34d567e8fa901bc2d34e56789f0` with your
account's detector ID and `us-east-1` with the Region where
you want to enable RDS Protection. If you don't want to enable it for all the new accounts
joining the organization, set `autoEnable` to `NONE`.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-organization-configuration --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --auto-enable --features '[{"Name": "RDS_LOGIN_EVENTS", "AutoEnable": "NEW"}]'
```

When the code has successfully executed, it returns an empty list of
`UnprocessedAccounts`. If there were any problems changing the detector
settings for an account, that account ID is listed along with a summary of the
issue.

Choose your preferred access method to selectively enable monitoring RDS login activity
for member accounts.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Make sure to use the delegated GuardDuty administrator account credentials. 2. In the navigation pane, choose **Accounts**.

On the **Accounts** page, review the
**RDS login activity** column for the status of your member
account. 3. ###### To selectively enable or disable RDS login activity

Select the account for which you want to configure RDS Protection. You can select
multiple accounts at a time. In the **Edit Protection Plans**
dropdown menu, choose **RDS Login Activity**, and then choose
the appropriate option.

API/CLI
To selectively enable or disable RDS Protection for your member accounts, invoke the
[updateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md") API operation using your own
`detector ID`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command,
and replace `12abc34d567e8fa901bc2d34e56789f0` with your
account's detector ID and `us-east-1` with the Region where
you want to enable RDS Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-member-detectors --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --account-ids `111122223333` --features '[{"Name": "RDS_LOGIN_EVENTS", "Status": "`ENABLED`"}]'
```

###### Note

You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of
`UnprocessedAccounts`. If there were any problems changing the detector
settings for an account, that account ID is listed along with a summary of the
issue.
