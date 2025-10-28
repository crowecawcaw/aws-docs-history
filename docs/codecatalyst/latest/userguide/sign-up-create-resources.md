Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a new space and

development role (starting without an invitation)

You can sign up for Amazon CodeCatalyst without an invitation to an existing space or project.
When you do, you will create a space and project after creating your AWS Builder ID. As
part of creating a space, you will need to add an AWS account for
billing purposes.

###### Tip

If you encounter any problems while signing up for your Amazon CodeCatalyst profile, follow the
steps provided on that page. If you need additional help, see [Problems signing up](ipa-troubleshooting.md#id-troubleshooting-sign-up "ipa-troubleshooting.md#id-troubleshooting-sign-up").

Here is one possible flow for a user starting out with CodeCatalyst without an invitation to a project
or a space.

Mary Major is a developer who is interested in CodeCatalyst and decides to try it
out. She navigates to the CodeCatalyst console and chooses the option to sign up and create an
AWS Builder ID. Mary provides an email address and password to create her AWS Builder ID. She will
be able to use her AWS Builder ID to sign in to CodeCatalyst and other applications. When asked to
choose an alias, she specifies `MaryMajor` as the CodeCatalyst user name that
will display in CodeCatalyst and that other project members will use to @mention Mary.

Next, Mary is automatically directed to create a space. As part of this flow,
Mary is asked to associate an AWS account with the space she's creating
so that she can see the sample code in her first project build and deploy. She adds that
information and creates her space, where she chooses the option to create a preview
development role that can be used for projects in her new space. Mary chooses to create
a project, and then she views a list of blueprints for projects. After reviewing the
information for the available blueprints, she decides to try the
**Modern three-tier web application** blueprint for her first project. She fills in
the required fields and creates the project. As soon as the project is ready, she's taken to
a project summary page that includes recent activity as well as links to project code and
the workflow that automatically builds and deploys that code. She explores both the code and
the workflow, including viewing the deployed sample web application. Liking what she sees,
she decides to invite some of her co-workers to the project to start exploring
CodeCatalyst.

When she has a moment, Mary configures her AWS Builder ID to sign in to CodeCatalyst with
multi-factor authentication (MFA). With MFA configured, Mary can sign in to CodeCatalyst using
a combination of her CodeCatalyst password and a passcode or token from an approved third-party
authentication app.

## Creating a new space and IAM roles

Follow these steps to sign up for your Amazon CodeCatalyst profile, create a space, and
add an account, a support role, and a developer role for your space.

The final procedure creates and add the developer role. The developer role is an AWS
IAM role that enables your CodeCatalyst workflows to access AWS resources. The developer
role is a service role used to manage AWS services and will be created in the account
that is signed in. A service role is an [IAM
role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform actions on your behalf. An IAM
administrator can create, modify, and delete a service role from within IAM. The role
will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName``. For more information about the role and role policy,
see [Understanding the CodeCatalystWorkflowDevelopmentRole-spaceName service role](ipa-iam-roles.md#ipa-iam-roles-service-role "ipa-iam-roles.md#ipa-iam-roles-service-role").

###### Note

As a security best practice, only assign administrative access to administrative
users and developers who need to manage access to AWS resources in the
space.

Before you begin, you must be ready to provide an AWS account ID for an account
where you have administrative privileges. Have your 12-digit AWS account ID ready. For
information about finding your AWS account ID, see [Your AWS account ID and its alias](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md").

###### To sign up as a new user

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you are
   signed in with the same AWS account that you want to use to create your space.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. On the welcome page, choose **Sign up**. The **Create your
   AWS Builder ID** page displays. Your AWS Builder ID is an identity you create to sign in.
   It is not the same as an AWS account.
4. In **Your email address**, enter the email address you want to associate
   with CodeCatalyst. Then choose **Next**.
5. In **Your name**, provide the first and last name you want displayed in
   applications where you use your AWS Builder ID. Spaces are allowed. This will be your AWS Builder ID
   profile name, such as **Mary Major**. You can change
   the name later.

Choose **Next**. The **Email verification** page
displays. 6. A verification code will be sent to the email you specified. Enter this code in
**Verification code**, and then choose **Verify**. If you
don't receive your code after 5 minutes and cannot find it in your spam or junk folders, then
choose **Resend code**. 7. Once we verify your code, enter a password that meets the requirements in
**Password** and **Confirm password**.

Select the checkbox confirming your agreement with the AWS Customer Agreement and the
AWS Service Terms, and then choose **Create AWS Builder ID**. 8. On the **Create your CodeCatalyst alias** page, enter an alias you want to use
for your unique user identifier in CodeCatalyst. Choose a shortened version of your name with no
spaces, such as **MaryMajor**. Other CodeCatalyst users will
use this to @mention you in comments and pull requests. Your CodeCatalyst profile will contain both
your full name from your AWS Builder ID and your CodeCatalyst alias. You cannot change your CodeCatalyst alias
later.

Your full name and your alias will display in different areas in CodeCatalyst. For example, your
profile name displays for your listed activity in the activity feed, but project members will
use your alias to @mention you.

Choose **Next**. The page updates to show the **Create your
CodeCatalyst space** section. 9. In **Name your space**, enter the name of your space. You
cannot change this later.

###### Note

Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces. 10. In **AWS Region** dropdown menu, choose the region where you want to store your
space and project data. You cannot change this later. 11. Choose **Next**. The page updates to show the page for adding an
AWS account. This account will be used as the billing account for the space. 12. In **AWS account ID**, enter the twelve-digit ID for the account you
want to connect to your space.

In **AWS account verification token**, copy the generated token ID. The
token is automatically copied for you, but you might want to store it while you approve the
AWS connection request. 13. Choose **Go to the AWS console to verify**. 14. The **Verify Amazon CodeCatalyst space** page opens in the AWS Management Console. This is
the **Amazon CodeCatalyst spaces** page. You might need to sign in to access the
page.

In the AWS Management Console, make sure to choose the same AWS Region where you want to create your
space.

To directly access the page, sign in to the Amazon CodeCatalyst Spaces in the AWS Management Console at
https://console.aws.amazon.com/codecatalyst/home/.

The verification token field in the AWS Management Console is automatically populated with the token
generated in CodeCatalyst. 15. (Optional) Under **Authorized paid tiers**, choose **Authorize
paid tiers (Standard, Enterprise)** to turn on the paid tiers for your billing
account.

###### Note

This does not upgrade the billing tier to a paid tier. However, this configures
the AWS account so that you can change the billing tier for your space at any time in
CodeCatalyst. You can turn on the paid tiers at any time. Without making this change, the
space is only able to use the Free tier. 16. Choose **Verify space**.

An **Account verified** success message displays to show that
the account has been added to the space. 17. Remain on the **Verify Amazon CodeCatalyst space** page. Choose the following
link: **To add IAM roles for this space, view space details.**

The connections page with **CodeCatalyst space details** opens in the AWS Management Console.
This is the **Amazon CodeCatalyst spaces** page. You might need to log in to access the
page. 18. Return to the CodeCatalyst page, and then choose **Next**. 19. A status message displays while your space is being created. When the space is
created, CodeCatalyst the following message is displayed: **Your space is ready. Your last
step is creating a project.**. You can do one of the following:

    * Choose **Skip for now**.
    * Choose **Create your first project** for your space. For
     a tutorial that shows you how to create a project with a blueprint, see [Tutorial: Creating a project with the
     Modern three-tier web application blueprint](getting-started-template-project.md "getting-started-template-project.md")

###### Note

If a permissions error or banner is shown, then refresh the page and try to view the
page again.

###### To create and add the CodeCatalyst **CodeCatalystWorkflowDevelopmentRole-`spaceName`**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you are
   logged in with the same AWS account for your space.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
4. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
5. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst spaces** page. You might need to log in
to access the page. 6. Choose **Create CodeCatalyst development administrator role in IAM**. This
option creates a service role that contains the permissions policy and trust policy for the
development role. The role will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName``. For more information about the
role and role policy, see [Understanding the CodeCatalystWorkflowDevelopmentRole-spaceName service role](ipa-iam-roles.md#ipa-iam-roles-service-role "ipa-iam-roles.md#ipa-iam-roles-service-role").

###### Note

This role is only recommended for use with developer accounts and uses the
`AdministratorAccess` AWS managed policy, giving it full access to create new
policies and resources in this AWS account. 7. Choose **Create development role**. 8. On the connections page, under **IAM roles available to CodeCatalyst**, view
the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role in the list of IAM roles added to your account. 9. To return to your space, choose **Go to Amazon CodeCatalyst**.

###### To create and add the CodeCatalyst **AWSRoleForCodeCatalystSupport**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you are
   logged in with the same AWS account for your space.
2. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
3. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
4. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You might need to sign in
to access the page. 5. Under **CodeCatalyst space details**, choose **Add CodeCatalyst Support
role**. This option creates a service role that contains the permissions policy and
trust policy for the preview development role. The role will have a name **AWSRoleForCodeCatalystSupport**
with a unique identifier appended. For more information about the role and role policy, see
[Understanding the AWSRoleForCodeCatalystSupport service
role](ipa-iam-roles.md#ipa-iam-roles-support-role "ipa-iam-roles.md#ipa-iam-roles-support-role"). 6. On the **Add role for CodeCatalyst Support** page, leave the default selected,
and then choose **Create role**. 7. Under **IAM roles available to CodeCatalyst**, view the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role
in the list of IAM roles added to your account. 8. To return to your space, choose **Go to Amazon CodeCatalyst**.

After you create your AWS Builder ID, create your first space, and add an account,
you can then create a project. For more information, see [Creating a project](projects-create.md "projects-create.md"). If this is your first
time using CodeCatalyst, we suggest starting with [Tutorial: Creating a project with the
Modern three-tier web application blueprint](getting-started-template-project.md "getting-started-template-project.md").
