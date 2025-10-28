Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding an AWS account to a

space

You use the CodeCatalyst console and the AWS Management Console to connect your space to an AWS account.

Before adding an AWS account to a space in CodeCatalyst, complete the following
prerequisites:

- Create an AWS account and acquire permissions to create AWS
  IAM roles in the account you want to connect.
- Create the IAM role or roles you want to associate with your account
  connection, including the IAM policies with permissions for the roles.
- Acquire the **Space administrator** role in the CodeCatalyst
  space where you want to create the connection.

###### Topics

- [Step 1: Creating a connection
  request](#ipa-connect-account-create-request "#ipa-connect-account-create-request")
- [Step 2:
  Accepting
  an account connection
  request](#ipa-connect-account-create-accept "#ipa-connect-account-create-accept")
- [Step 3: Review an approved
  connection](#ipa-connect-account-create-review "#ipa-connect-account-create-review")
- [Step 4: Add IAM roles to your
  connection](#ipa-connect-account-linkedroles "#ipa-connect-account-linkedroles")
- [Next steps: Create additional IAM roles
  for your account connection](#ipa-connect-account-next "#ipa-connect-account-next")

## Step 1: Creating a connection

request

Creating a connection request in the CodeCatalyst console generates a connection token
that you can use to complete authorization.

You must have the **Space administrator** or
**Power user** role in the CodeCatalyst space where you
want to create the connection. You must also have administrative permissions for the
AWS account you want to add.

###### To create a connection

1. In the AWS Management Console, make sure you are logged in with the same account that you want to
   create a connection with.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
4. Choose **Add an AWS account**.
5. On the **Associate AWS account with Amazon CodeCatalyst** page, in
   **AWS account ID**, enter the twelve-digit ID for the account you want to
   connect to your space. For information about finding your AWS account ID, see [Your
   AWS account ID and its alias](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md").
6. In **Amazon CodeCatalyst display name**, enter a reference name for the
   account.
7. (Optional) In **Connection description**, enter a description for the
   account that will help you choose the projects where the account and role or roles will
   apply.
8. Choose **Associate AWS account**.
9. The page returns to the **AWS account details** page where a success
   banner displays.

## Step 2:

Accepting
an account connection
request

After you submit a request in the CodeCatalyst console to connect to your AWS account, you work with your AWS administrator to accept the
connection request by submitting it with the provided connection token.

Make
sure you have administrator permissions for your account, and you're signed in to
the AWS Management Console with the same AWS account for which you're creating the
connection.

###### To approve a connection request (console)

1. In the AWS Management Console, make sure you are logged in with the same account that you want to
   create a connection with.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then
   choose **AWS accounts**.
4. On the **AWS account details** page, choose **Complete
   setup in the AWS Management Console**.
5. The **Verify Amazon CodeCatalyst space** page opens in the AWS Management Console.
   This is the **Amazon CodeCatalyst Spaces** page. You might need to log in to
   access the page.

To directly access the page, sign in to the Amazon CodeCatalyst Spaces in the AWS Management Console at
https://console.aws.amazon.com/codecatalyst/home/.

The verification token is automatically entered in **Verification
token**. A success message shows a message that the token is a valid
token. 6. (Optional) Under **Authorized paid tiers**, choose **Authorize
paid tiers (Standard, Enterprise)** to turn on the paid tiers for your billing
account.

###### Note

This does not upgrade the billing tier to a paid tier. However, this configures
the AWS account so that you can change the billing tier for your space at any time in
CodeCatalyst. You can turn on the paid tiers at any time. Without making this change, the
space is only able to use the Free tier. 7. Choose **Verify space**.

An **Account verified** success message displays to show
that the account has been added to the space.

## Step 3: Review an approved

connection

After getting a connection approved, you can view the connection in the console,
along with the IAM roles you added to it.

###### To review an approved connection

1. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
2. The account connection is listed with the date it was created.
3. Choose the account display name. The **AWS account details** page
   displays.

## Step 4: Add IAM roles to your

connection

If you're using an IAM role configured for a CodeCatalyst deploy action, add the role
to your deployment environment. For more information, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

## Next steps: Create additional IAM roles

for your account connection

After you create a connection, you can create additional IAM roles to add to it.
The IAM roles that you add are dependent on your workflows. For example, a CodeCatalyst
build action requires the CodeCatalyst build role.
.

To connect your account, you will need the Amazon Resource Name (ARN) for the
roles you created. Copy the ARN for your role or roles as detailed here. For more
information about working with ARNs for IAM roles, see [Amazon Resource Name
(ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

To access your IAM role ARN

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the search box, enter the name of the role you want to add.
4. Choose the role from the list.

The role's **Summary** page appears. 5. At the top, copy the **Role ARN** value.
