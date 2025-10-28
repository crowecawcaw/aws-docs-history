Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Setting up a space that supports AWS Builder ID

users

You can create a space that manages users with AWS Builder ID access to CodeCatalyst. This is a
CodeCatalyst space for AWS Builder ID users.

To get started, you need the following:

- Your AWS Builder ID to sign in to CodeCatalyst
- Your AWS account to provide for the space access to resources and for billing if
  you go beyond the Free tier.

Before you begin, you must be ready to provide an AWS account ID for an account
where you have administrative privileges. Have your 12-digit AWS account ID ready.
For information about finding your AWS account ID, see [Your AWS account ID and its alias](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md").
To create a space that supports AWS Builder ID users, you start by signing in to CodeCatalyst
with your AWS Builder ID. When you create a space that supports AWS Builder ID users, you have the
**Space administrator** role by default.

###### To sign up as a new user

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you
   are signed in with the same AWS account that you want to use to create your
   space.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. On the welcome page, choose **Sign up**. The **Create
   your AWS Builder ID** page displays. Your AWS Builder ID is an identity you
   create to sign in. It is not the same as an AWS account.
4. In **Your email address**, enter the email address you want to
   associate with CodeCatalyst. Then choose **Next**.
5. In **Your name**, provide the first and last name you want
   displayed in applications where you use your AWS Builder ID. Spaces are allowed. This
   will be your AWS Builder ID profile name, such as **Mary Major**. You can change the name later.

Choose **Next**. The **Email verification** page
displays. 6. A verification code will be sent to the email you specified. Enter this code in
**Verification code**, and then choose
**Verify**. If you don't receive your code after 5 minutes and
cannot find it in your spam or junk folders, then choose **Resend
code**. 7. Once we verify your code, enter a password that meets the requirements in
**Password** and **Confirm password**.

Select the checkbox confirming your agreement with the AWS Customer Agreement
and the AWS Service Terms, and then choose **Create
AWS Builder ID**. 8. On the **Create your CodeCatalyst alias** page, enter an alias you want
to use for your unique user identifier in CodeCatalyst. Choose a shortened version of your
name with no spaces, such as **MaryMajor**.
Other CodeCatalyst users will use this to @mention you in comments and pull requests. Your
CodeCatalyst profile will contain both your full name from your AWS Builder ID and your CodeCatalyst
alias. You cannot change your CodeCatalyst alias later.

Your full name and your alias will display in different areas in CodeCatalyst. For
example, your profile name displays for your listed activity in the activity feed,
but project members will use your alias to @mention you.

Choose **Next**. The page updates to show the **Create
your CodeCatalyst space** section. 9. In **Name your space**, enter the name of your space.
You cannot change this later.

###### Note

Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.

Choose **Next**. The page updates to show the page for adding an
AWS account. This account will be used as the billing account for the
space. 10. In **AWS Region**, choose the Region where you want to store
your space and project data. You cannot change this later. 11. In **AWS account ID**, enter the twelve-digit ID for the
account you want to connect to your space.

In **AWS account verification token**, copy the generated token
ID. The token is automatically copied for you, but you might want to store it while
you approve the AWS connection request. 12. Choose **Verify in AWS**. 13. The **Verify Amazon CodeCatalyst space** page opens in the AWS Management Console.
This is the **Amazon CodeCatalyst Spaces** page. You might need to sign in
to access the page.

In the AWS Management Console, make sure to choose the same AWS Region where you want to
create your space.

To directly access the page, sign in to the Amazon CodeCatalyst Spaces in the AWS Management Console at
https://console.aws.amazon.com/codecatalyst/home/.

The verification token field in the AWS Management Console is automatically populated with the
token generated in CodeCatalyst. 14. Choose **Verify space**.

An **Account verified** success message displays to
show that the account has been added to the space. 15. Remain on the **Verify Amazon CodeCatalyst space** page. Choose the
following link: **To enable the Standard tier or add IAM roles for this
space, view space details.**

The **CodeCatalyst space details** page opens in the AWS Management Console.
This is the **Amazon CodeCatalyst Spaces** page. You might need to log in
to access the page. 16. To turn on the Standard tier so that the space for the AWS account can
update its billing tier, choose **Edit**. Choose the
**STANDARD** option, and then choose
**Update**.

###### Note

This does not upgrade the billing tier to the Standard tier. However, this
configures the AWS account so that you can change the billing tier for your
space at any time in CodeCatalyst. You can turn on the Standard tier at any time.
Without making this change, the space is only able to use the Free
tier. 17. Return to the CodeCatalyst page, and then choose **Next**. 18. A status message displays while your space is being created. When the
space is created, CodeCatalyst opens the page for your space. The view defaults
to the **Projects** tab.

###### Note

If a permissions error or banner is shown, then refresh the page and try to
view the page again. 19. (Optional) Proceed to creating a project for your space.

###### To create and add the CodeCatalyst **CodeCatalystWorkflowDevelopmentRole-`spaceName`**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you
   are logged in with the same AWS account for your space.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then
   choose **AWS accounts**.
4. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
5. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You might need
to log in to access the page. 6. Choose **Create CodeCatalyst development administrator role in IAM**.
This option creates a service role that contains the permissions policy and trust
policy for the development role. The role will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName``.

###### Note

This role is only recommended for use with developer accounts and uses the
`AdministratorAccess` AWS managed policy, giving it full access
to create new policies and resources in this AWS account. 7. Choose **Create development role**. 8. On the connection page, under **IAM roles available to
CodeCatalyst**, view the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role in the list of IAM roles added to
your account. 9. To return to your space, choose **Go to Amazon CodeCatalyst**.

###### To create and add the CodeCatalyst **AWSRoleForCodeCatalystSupport**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you
   are logged in with the same AWS account for your space.
2. Navigate to your CodeCatalyst space. Choose **Settings**, and then
   choose **AWS accounts**.
3. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
4. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You might need
to sign in to access the page. 5. Under **CodeCatalyst space details**, choose **Add CodeCatalyst
Support role**. This option creates a service role that contains the
permissions policy and trust policy for the preview development role. The role will
have a name **AWSRoleForCodeCatalystSupport** with a unique identifier appended. . 6. On the **Add role for CodeCatalyst Support** page, leave the default
selected, and then choose **Create role**. 7. Under **IAM roles available to CodeCatalyst**, view the
`CodeCatalystWorkflowDevelopmentRole-`spaceName`` role in the list of IAM roles added to your account. 8. To return to your space, choose **Go to Amazon CodeCatalyst**.
After you create your AWS Builder ID, create your first space, and add an account, you
can then create a project. .
