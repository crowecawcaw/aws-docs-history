Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Removing an account from a space (in

AWS)

You can use the page for CodeCatalyst in AWS to remove an account that has been added to a
space. For this procedure, using administrative permissions for the specific account you are
managing, you sign in the Amazon CodeCatalyst Spaces page in the AWS Management Console to remove an AWS account
from your space. To remove an account that is a designated billing account for your
CodeCatalyst space, make sure to first specify a new billing account.

An account that has been removed can be added again later, but you must create a new
connection between the account and the space. You will need to re-associate any IAM
roles to the added account.

A billing account must be designated for your CodeCatalyst space, even if usage for the
space will not exceed the Free tier. Before you can remove a space for an account
that is a designated billing account, you will need to add another account for your
space.

###### Important

While you can use these steps to remove an account, this is not recommended as the AWS Management Console doesn't show whether your account is connected to
workflows in your space. Any existing workflows connected to this account won't work after the account
is removed and must be configured again with another connected account from the CodeCatalyst console.

You must have the **Space administrator** or
**Power user** role to manage account connections for your
space.

###### To remove an added account

1. In the AWS Management Console, make sure you are logged in with the same account that you want to
   manage.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then
   choose **Billing**.
4. View the billing account information on the page to make sure the account you want to
   remove is not the designated billing account for the space.
5. Choose **Manage billing in AWS**. This opens the Amazon CodeCatalyst Spaces
   in the AWS Management Console. If you're prompted to log in, log in to AWS, and then choose the
   button again to load the page.
6. On the **Amazon CodeCatalyst
   Spaces**
   page, choose the space with the account that you want to remove. The details page for
   the space displays.
7. Choose **Remove space**.
8. In **Remove CodeCatalyst space from this account**, enter the
   space name to confirm. Choose **Remove**.
