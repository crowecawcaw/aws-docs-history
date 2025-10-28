# Account details in Amazon Quick Suite

Use this section to change the account-wide settings in Amazon Quick Suite. To open your account
settings, choose the profile icon, and then select **Manage
Quick Suite**. Then, click on **Account
settings**.

## Deleting your Amazon Quick Suite subscription and closing

your account

###### Warning

**Deleting your Amazon Quick Suite subscription permanently destroys all
organizational data across all AWS regions and cannot be reversed.**

This action will immediately and permanently delete:

- Every dashboard, analysis, and dataset across your entire organization
  in all regions
- All user accounts and their associated work
- Custom data sources and connections
- All sharing permissions and folder structures
- Historical usage data and audit logs
- All customizations, themes, and organizational settings
  **Account deletion from any region affects your entire
  global Quick Suite deployment.** Even if you have Quick Suite resources
  in multiple AWS regions, this single action deletes everything worldwide.

**There is no recovery option.** Once deleted, this data
cannot be restored by AWS or recovered through any means.

**Before proceeding:** Export critical dashboards, back up
datasets, and ensure all stakeholders are informed of this permanent action.

The act of deleting your Amazon Quick Suite subscription is immediate and final. Deletion
removes every Amazon Quick Suite asset on the AWS account you are using. It doesn't delete
namespaces that you added. (The **Default** namespace is deleted
automatically.) You can locate and delete namespaces by using the API operations [ListNamespaces](../../../quicksight/latest/APIReference/API_ListNamespaces.md "../../../quicksight/latest/APIReference/API_ListNamespaces.md") and [DeleteNamespace](../../../quicksight/latest/APIReference/API_DeleteNamespace.md "../../../quicksight/latest/APIReference/API_DeleteNamespace.md").

You can terminate your Amazon Quick Suite account from the **Manage
Quick Suite** menu or by using the API. To prevent someone from deleting a
Amazon Quick Suite user account accidentally or maliciously, Amazon Quick Suite uses permissions, a
switch for the **Account termination protection** setting, and a
required confirmation word.

After your account is deleted, you can create a new Amazon Quick Suite account. The process
doesn't take more than 15 minutes. The settings for edition and user authorization
method on the new account can be the same or different.

Before you can delete your Amazon Quick Suite account, make sure of the following:

- You're signed in using the IAM account or AWS root account that was used
  to create your Amazon Quick Suite account.
- You understand that your AWS account is not deleted when you terminate your
  Amazon Quick Suite account. To instead close your AWS account, see [Closing an AWS account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md").

- Terminating your account deletes all users, all uploaded data, and assets (for
  example, datasets, data sources, queries, dashboards, analyses, settings, and so
  on).

###### Topics

- [Permissions and access to account
  termination](#delete-account-permissions "#delete-account-permissions")
- [Deleting your account](#delete-account "#delete-account")

### Permissions and access to account

termination

You need the following special permissions to terminate a Amazon Quick Suite account.
Without these permissions, you won't be able to terminate a Amazon Quick Suite user
account. Contact your account administrator for help.

- You're a Amazon Quick Suite administrator and have an `Admin` role in
  Amazon Quick Suite.
- You need permissions to run the following (except if you're the root admin
  user (IAM ) who added Amazon Quick Suite)
  - `quicksight:Unsubscribe`
  - `ds:UnauthorizeApplication`
  - `ds:DeleteDirectory`
  - `ds:DescribeDirectories`
  - `quicksight:UpdateAccountSettings`

- To remove custom namespaces, you need permission to run the following API
  operations:

      + `quicksight:ListNamespaces`
      + `quicksight:DeleteNamespace`

  You don't need extra permissions to delete the default namespace.

###### Warning

Terminating your account is an instant action that cannot be undone by you or
by AWS.

### Deleting your account

The following sections outlines the different ways you can terminate your
Amazon Quick Suite instance.

###### To terminate your Amazon Quick Suite account without the Amazon Quick Suite UI

- Sign in to AWS where you want to remove Amazon Quick Suite.

###### To terminate your account by using the Amazon Quick Suite UI

1. Choose your profile on the application bar, and then choose
   **Manage Quick Suite**.
2. Use one of the following methods to open the **Account
   termination** screen.
   - Use this [direct link](https://us-east-1.quicksight.aws.amazon.com/sn/console/unsubscribe "https://us-east-1.quicksight.aws.amazon.com/sn/console/unsubscribe") to the screen.
   - Choose **Account settings**,
     **Manage**.

3. On the **Account termination** page, confirm that you are
   viewing the correct Amazon Quick Suite account by checking the name listed for
   account name.
4. Toggle off **Account termination protection is on**.
   Doing this enables the **Delete account** section.
5. For **Type "confirm" to delete this account**, enter the
   word confirmation word shown on your screen.
