# Add users and groups to

your sync scope

###### Note

When adding groups to your sync scope, sync groups directly from the trusted on-premises
domain rather than from groups in the AWS Managed Microsoft AD domain. Groups synced directly from the
trusted domain contain actual user objects that IAM Identity Center can access and synchronize successfully.

Add your Active Directory users and groups to IAM Identity Center by following these steps.

###### To add users

1. Open the [IAM Identity Center
   console.](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon")
2. Choose **Settings**.
3. On the **Settings** page, choose the **Identity
   source** tab, choose **Actions**, and then choose
   **Manage Sync**.
4. On the **Manage Sync** page, choose the **Users**
   tab, and then choose **Add users and groups**.
5. On the **Users** tab, under **User**, enter the
   exact user name and choose **Add**.
6. Under **Added Users and Groups**, review the user that you want to
   add.
7. Choose **Submit**.
8. In the navigation pane, choose **Users**. If the user that you
   specified doesn't display in the list, choose the refresh icon to update the list of
   users.

###### To add groups

1. Open the [IAM Identity Center
   console.](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon")
2. Choose **Settings**.
3. On the **Settings** page, choose the **Identity
   source** tab, choose **Actions**, and then choose
   **Manage Sync**.
4. On the **Manage Sync** page, choose the **Groups**
   tab, and then choose **Add users and groups**.
5. Choose the **Groups** tab. Under **Group**, enter
   the exact group name and choose **Add**.
6. Under **Added Users and Groups**, review the group that you want to
   add.
7. Choose **Submit**.
8. In the navigation pane, choose **Groups**. If the group that you
   specified doesn't display in the list, choose the refresh icon to update the list of
   groups.
