AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Creating a

resource data sync

Before you configure a resource data sync for Explorer, note the following
details.

- Explorer supports a maximum of five resource data syncs.
- After you create a resource data sync for a Region, you can't change
  the _account options_ for that sync. For example, if
  you create a sync in the us-east-2 (Ohio) Region and you choose the
  **Include only the current account** option, you
  can't edit that sync later and choose the **Include all accounts
  from my AWS Organizations configuration** option. Instead, you must
  delete the first resource data sync, and create a new one.
- OpsData viewed in Explorer is read-only.
  Use the following procedure to create a resource data sync for
  Explorer.

###### To create a resource data sync

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explorer**.
3. Choose **Settings**.
4. In the **Configure resource data sync** section,
   choose **Create resource data sync**.
5. For **Resource data sync name**, enter a name.
6. In the **Add accounts** section, choose an
   option.

###### Note

To use either of the AWS Organizations options, you must be logged into the
AWS Organizations management account or you must be logged into an Explorer
delegated administrator account. For more information about the
delegated administrator account, see [Configuring a delegated
administrator for Explorer](Explorer-setup-delegated-administrator.md "Explorer-setup-delegated-administrator.md"). 7. In the **Regions to include** section, choose one of
the following options.

    * Choose **All current and future regions** to
     automatically sync data from all current AWS Regions and any
     new Regions that come online in the future.
    * Choose **All regions** to automatically sync
     data from all current AWS Regions.
    * Individually choose Regions that you want to include.

8. Choose **Create resource data sync**.
   The system can take several minutes to populate Explorer with data after you
   create a resource data sync. You can view the sync by choosing it from the
   **Select a resource data sync** list in Explorer.
