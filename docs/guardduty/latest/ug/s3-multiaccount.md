# Enabling S3 Protection in multiple-account

environments

In a multi-account environment, only the delegated GuardDuty administrator account has the option to configure (enable
or disable) S3 Protection for the member accounts in their AWS organization. The GuardDuty
member accounts can't modify this configuration from their accounts. The delegated GuardDuty administrator account
manages their member accounts using AWS Organizations. The delegated GuardDuty administrator account can choose to have S3 Protection
automatically enabled on all accounts, only new accounts, or no accounts in the
organization. For more information, see [Managing accounts with
AWS Organizations](guardduty_organizations.md "guardduty_organizations.md").

Choose your preferred access method to enable S3 Protection for the delegated GuardDuty administrator account.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose
   **S3 Protection**.
3. On the **S3 Protection** page, choose
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
Run [updateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md") by using the detector
ID of the delegated GuardDuty administrator account for the current Region and passing the
`features` object `name` as
`S3_DATA_EVENTS` and `status` as
`ENABLED`.

Alternatively, you can configure S3 Protection by using AWS Command Line Interface. Run
the following command, and make sure to replace
`12abc34d567e8fa901bc2d34e56789f0` with
the detector ID of the delegated GuardDuty administrator account for the current Region.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --features '[{"Name": "S3_DATA_EVENTS", "Status": "ENABLED"}]'
```

Choose your preferred access method to enable S3 Protection for the delegated GuardDuty administrator account.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Sign in using your administrator account account. 2. Do one of the following:

###### Using the **S3 Protection** page

    1. In the navigation pane, choose
     **S3 Protection**.
    2. Choose **Enable for all
     accounts**. This action automatically
     enables S3 Protection for both existing and new accounts
     in the organization.
    3. Choose **Save**.


    ###### Note

    It may take up to 24 hours to update the configuration for the member accounts.

###### Using the **Accounts** page

    1. In the navigation pane, choose
     **Accounts**.
    2. On the **Accounts** page, choose
     **Auto-enable** preferences
     before **Add accounts by
     invitation**.
    3. In the **Manage auto-enable
     preferences** window, choose
     **Enable for all accounts** under
     **S3 Protection**.
    4. Choose **Save**.

If you can't use the **Enable for all
accounts** option, see [Selectively enable S3 Protection in member
accounts](#s3-enable-members "#s3-enable-members").

API/CLI

- To selectively enable S3 Protection for your member accounts,
  invoke the [updateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md") API
  operation using your own `detector
ID`.
- The following example shows how you can enable S3 Protection for
  a single member account. Make sure to replace
  `12abc34d567e8fa901bc2d34e56789f0`
  with the `detector-id` of the delegated GuardDuty administrator account, and
  `111122223333`.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-member-detectors --detector-id `12abc34d567e8fa901bc2d34e56789f0` --account-ids `111122223333` --features '[{"name": "S3_DATA_EVENTS", "status": "`ENABLED`"}]'
```

###### Note

You can also pass a list of account IDs separated by a
space.

- When the code has successfully executed, it returns an
  empty list of `UnprocessedAccounts`. If there
  were any problems changing the detector settings for an
  account, that account ID is listed along with a summary of
  the issue.

Choose your preferred access method to enable S3 Protection for all the existing
active member accounts in your organization.

Console

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Sign in using the delegated GuardDuty administrator account credentials. 2. In the navigation pane, choose
**S3 Protection**. 3. On the **S3 Protection** page, you can view the
current status of the configuration. Under the
**Active member accounts** section,
choose **Actions**. 4. From the **Actions** dropdown menu,
choose **Enable for all existing active member
accounts**. 5. Choose **Confirm**.

API/CLI

- To selectively enable S3 Protection for your member accounts,
  invoke the [updateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md") API
  operation using your own `detector
ID`.
- The following example shows how you can enable S3 Protection for
  a single member account. Make sure to replace
  `12abc34d567e8fa901bc2d34e56789f0`
  with the `detector-id` of the delegated GuardDuty administrator account, and
  `111122223333`.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-member-detectors --detector-id `12abc34d567e8fa901bc2d34e56789f0` --account-ids `111122223333` --features '[{"name": "S3_DATA_EVENTS", "status": "`ENABLED`"}]'
```

###### Note

You can also pass a list of account IDs separated by a
space.

- When the code has successfully executed, it returns an
  empty list of `UnprocessedAccounts`. If there
  were any problems changing the detector settings for an
  account, that account ID is listed along with a summary of
  the issue.

Choose your preferred access method to enable S3 Protection for new accounts that
join your organization.

Console
The delegated GuardDuty administrator account can enable for new member accounts in an organization
through the console, using either the **S3 Protection**
or **Accounts** page.

###### To auto-enable S3 Protection for new member accounts

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Make sure to use the delegated GuardDuty administrator account credentials. 2. Do one of the following:

    * Using the **S3 Protection**
     page:




    	1. In the navigation pane, choose
    	 **S3 Protection**.
    	2. On the **S3 Protection** page,
    	 choose **Edit**.
    	3. Choose **Configure accounts
    	 manually**.
    	4. Select **Automatically enable for
    	 new member accounts**. This step ensures
    	 that whenever a new account joins your
    	 organization, S3 Protection will be automatically
    	 enabled for their account. Only the organization
    	 delegated GuardDuty administrator account can modify this configuration.
    	5. Choose **Save**.
    * Using the **Accounts**
     page:




    	1. In the navigation pane, choose
    	 **Accounts**.
    	2. On the **Accounts** page,
    	 choose **Auto-enable**
    	 preferences.
    	3. In the **Manage auto-enable
    	 preferences** window, select
    	 **Enable for new accounts** under
    	 **S3 Protection**.
    	4. Choose **Save**.

API/CLI

- To selectively enable S3 Protection for your member accounts,
  invoke the [UpdateOrganizationConfiguration](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md")
  API operation using your own `detector
ID`.
- The following example shows how you can enable S3 Protection for
  a single member account. Set the preferences to
  automatically enable or disable the protection plan in that
  Region for new accounts (`NEW`) that join the
  organization, all the accounts (`ALL`), or none
  of the accounts (`NONE`) in the organization. For
  more information, see [autoEnableOrganizationMembers](../APIReference/API_UpdateOrganizationConfiguration.md#guardduty-UpdateOrganizationConfiguration-request-autoEnableOrganizationMembers "../APIReference/API_UpdateOrganizationConfiguration.md#guardduty-UpdateOrganizationConfiguration-request-autoEnableOrganizationMembers"). Based on your
  preference, you may need to replace `NEW` with
  `ALL` or `NONE`.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-organization-configuration --detector-id `12abc34d567e8fa901bc2d34e56789f0` --auto-enable --features '[{"Name": "S3_DATA_EVENTS", "autoEnable": "`NEW`"}]'
```

- When the code has successfully executed, it returns an
  empty list of `UnprocessedAccounts`. If there
  were any problems changing the detector settings for an
  account, that account ID is listed along with a summary of
  the issue.

Choose your preferred access method to selectively enable S3 Protection for member
accounts.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Make sure to use the delegated GuardDuty administrator account credentials. 2. In the navigation pane, choose
**Accounts**.

On the **Accounts** page, review the
**S3 Protection** column for the status of
your member account. 3. ###### To selectively enable S3 Protection

Select the account for which you want to enable S3 Protection.
You can select multiple accounts at a time. In the
**Edit Protection Plans** dropdown
menu, choose **S3Pro**, and then choose the
appropriate option.

API/CLI
To selectively enable S3 Protection for your member accounts, run the
[updateMemberDetectors](../APIReference/API_UpdateMemberDetector.md "../APIReference/API_UpdateMemberDetector.md") API operation
using your own detector ID. The following example shows how you can
enable S3 Protection for a single member account. To disable it, replace
`true` with `false`.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
 aws guardduty update-member-detectors --detector-id `12abc34d567e8fa901bc2d34e56789f0` --account-ids `123456789012` --features '[{"Name" : "S3_DATA_EVENTS", "Status" : "ENABLED"}]'
```

###### Note

You can also pass a list of account IDs separated by a
space.

When the code has successfully executed, it returns an empty list
of `UnprocessedAccounts`. If there were any problems
changing the detector settings for an account, that account ID is
listed along with a summary of the issue.

###### Note

If you use scripts to on-board new accounts and want to
disable S3 Protection in your new accounts, you can modify the [createDetector](../APIReference/API_CreateDetector.md "../APIReference/API_CreateDetector.md") API operation
with the optional `dataSources` object as described
in this topic.
