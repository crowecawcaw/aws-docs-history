# Navigating the root and organizational unit (OU) hierarchy with AWS Organizations

To navigate to different OUs or to the root when moving accounts or attaching
policies, you can use the default "tree" view.

AWS Management Console

###### To navigate the organization as a 'tree'

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, at the top of the
   **Organization** section, select the **Hierarchy** toggle (instead of **List**).
3. The tree initially appears showing the root, displaying only the
   first level of child OUs and accounts. To expand the tree to show
   deeper levels, choose the expand icon (
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) next to any parent entity. To reduce clutter
   and collapse a branch of the tree, choose the collapse icon (
   ![Downward-pointing gray triangle icon, commonly used to indicate dropdown menus.](images/console-collapse.png)
   ) next to an expanded parent entity.
4. Choose the name of an OU or root to view its details and perform
   certain operations. Alternatively, you can choose the radio button
   next to the name, and perform certain operations on that entity in
   the **Actions** menu.

You can also view the list of only the accounts in your organization in tabular form,
without having to first navigate to an OU to find them. In this view you can't see any
of the OUs or manipulate the policies attached to them.

AWS Management Console

###### To view the organization as a flat list of accounts with no

hierarchy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, at the top of the
   **Organization** section, choose the
   **View AWS accounts only** switch icon to
   turn it on.
   ![Speech bubble icon representing a chat or conversation interface.](images/console-switch-on.png)
   .
3. The list of accounts is displayed without any hierarchy.
