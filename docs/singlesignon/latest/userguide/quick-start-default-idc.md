# Configure user access with the default IAM Identity Center

directory

When you enable IAM Identity Center for the first time, it is automatically configured with an Identity Center
directory as your default identity source, so you do not need to choose an identity source. If
your organization uses another identity provider such as Microsoft Active Directory, Microsoft
Entra ID, or Okta consider integrating that identity source with IAM Identity Center instead of
using the default configuration.

**Objective**

In this tutorial, you'll use the default directory as your identity source and an IAM Identity Center
organization instance to set up and test an administrative user. This administrative user
creates and manages users and groups and grants AWS access with permission sets. In the next
steps, you'll create the following:

- An administrative user named `Nikki Wolf`
- A group named `Admin team`
- A permission set named `AdminAccess`
  To verify everything was created correctly, you'll sign in and set the administrative user's
  password. After completing this tutorial, you can use the administrative user to add more users
  in IAM Identity Center, create additional permission sets, and set up organizational access to applications.
  Alternatively, if you want to grant users access to application, you can follow [step 1](#gs-qs-step1 "#gs-qs-step1") of this procedure and [configure
  application access](manage-your-applications.md "manage-your-applications.md").

The following prerequisites are needed to complete this tutorial:

- [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md") and
  have an [organization instance of
  IAM Identity Center](organization-instances-identity-center.md "organization-instances-identity-center.md").
  - If you have an [account instance](account-instances-identity-center.md "account-instances-identity-center.md") of IAM Identity Center, you can create users and groups
    as well as grant them access to applications. For more information, see [Application access](manage-your-applications.md "manage-your-applications.md").

- Sign in to the AWS Management Console and access the IAM Identity Center console either as a:
  - **New to AWS (root user)** – Sign in as the
    account owner by choosing **AWS account root user** and entering
    your AWS account email address. On the next page, enter your password.
  - **Already using AWS (IAM credentials)**
    – Sign in using your IAM credentials with administrative
    permissions.
    - For more help signing in to the AWS Management Console, see [AWS Sign-In Guide.](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md")

- You can configure multi-factor authentication for your IAM Identity Center users. For more
  information, see [Configure MFA in IAM Identity Center](mfa-configure.md "mfa-configure.md").

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. In the IAM Identity Center navigation pane, choose **Users**, then select
   **Add user**.
3. On the **Specify user details** page, complete the following
   information:
   - **Username** - For this tutorial, enter
     `nikkiw`.

   When creating users, choose usernames that are easy to remember. Your users must
   remember the username to sign in to the AWS access portal and you cannot change it
   later.
   - **Password** - Choose **Send an email to this user with
     password setup instructions (Recommended)**.

   This option sends the user an email addressed from Amazon Web Services, with the subject
   line **Invitation to join IAM Identity Center**. The email comes from either
   `no-reply@signin.aws` or `no-reply@login.awsapps.com`. Add
   these email addresses to your approved senders list.
   - **Email address** - Enter an email address for the user where
     you can receive the email. Then, enter it again to confirm it. Each user must have a
     unique email address.
   - **First name** - Enter the first name for the user. For this
     tutorial, enter `Nikki`.
   - **Last name** - Enter the last name for the user. For this
     tutorial, enter `Wolf`.
   - **Display name** - The default value is the first and last name
     of the user. If you want to change the display name, you can enter something
     different. The display name is visible in the sign-in portal and users list.
   - Complete the optional information if desired. It isn’t used during this tutorial
     and you can change it later.

4. Choose **Next**. The **Add user to groups** page
   appears. We're going to create a group to assign administrative permissions to instead
   of giving them directly to `Nikki`.

Choose **Create group**

A new browser tab opens to display the **Create group** page.

    1. Under **Group details**, in **Group name**
     enter a name for the group. We recommend a group name that identifies the role of
     the group. For this tutorial, enter `Admin team`.
    2. Choose **Create group**
    3. Close the **Groups** browser tab to return to the **Add
     user** browser tab

5. In the **Groups** area, select the **Refresh**
   button. The `Admin team` group appears in the list.

Select the checkbox next to `Admin team`, and then choose
**Next**. 6. On the **Review and add user** page, confirm the following:

    * Primary information appears as you intended
    * Groups shows the user added to the group you created

If you want to make changes, choose **Edit**. When all details are
correct choose **Add user**.

A notification message informs you that the user was added.
Next, you'll add administrative permissions for the `Admin
 team` group so that `Nikki` has access to
resources.

###### Important

Follow these steps only if you enabled an [organization instance of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

1.  In the IAM Identity Center navigation pane, under **Multi-account permissions**,
    choose **AWS accounts**.
2.  On the **AWS accounts** page the **Organizational
    structure** displays your organization with your accounts underneath it in
    the hierarchy. Select the checkbox for your management account, then select
    **Assign users or groups**.
3.  The **Assign users and groups** workflow displays. It consists of
    three steps:
    1.  For **Step 1: Select users and groups** choose the
        `Admin team` group you created. Then choose
        **Next**.
    2.  For **Step 2: Select permission sets** choose **Create
        permission set** to open a new tab that steps you through the three
        sub-steps involved in creating a permission set.
        1.  For **Step 1: Select permission set type** complete the
            following:

                * In **Permission set type**, choose **Predefined
                 permission set**.
                * In **Policy for predefined permission set**, choose
                 **AdministratorAccess**.

            Choose **Next**.

        2.  For **Step 2: Specify permission set details**, keep the
            default settings, and choose **Next**.

        The default settings create a permission set named
        `AdministratorAccess` with session duration set to
        one hour. You can change the name of the permission set by entering a new name
        in the **Permission set name** field. 3. For **Step 3: Review and create**, verify that the
        **Permission set type** uses the AWS managed policy
        **AdministratorAccess**. Choose **Create**.
        On the **Permission sets** page a notification appears
        informing you that the permission set was created. You can close this tab in
        your web browser now.On the **Assign users and groups** browser tab, you are still
        on **Step 2: Select permission sets** from which you started the
        create permission set workflow.

    In the **Permissions sets** area, choose the
    **Refresh** button. The
    `AdministratorAccess` permission set you created appears
    in the list. Select the check box for that permission set and then choose
    **Next**. 3. On the **Step 3: Review and submit assignments** page, confirm
    that the `Admin team` group is selected and that the
    `AdministratorAccess` permission set is selected, then
    choose **Submit**.

    The page updates with a message that your AWS account is being configured.
    Wait until the process completes.

    You are returned to the AWS accounts page. A notification message informs you
    that your AWS account has been reprovisioned and the updated permission set
    applied.

###### Congratulations!

You have successfully set up your first user, group, and permission set.

In the next portion of this tutorial you'll test `Nikki's`
access by signing in to the AWS access portal with their administrative credentials and set their
password. Sign out of the console now.

Now that `Nikki Wolf` is a user in your organization, they can
sign in and access the resources to which they are granted permission according to their
permission set. To verify that the user is correctly configured, in this next step you'll
use `Nikki's` credentials to sign in and set up their password.
When you added the user `Nikki Wolf` in Step 1 you chose to have
`Nikki` receive an email with password setup instructions. It's
time to open that email and do the following:

1. In the email, select the **Accept invitation** link to accept the
   invitation.

###### Note

The email also includes `Nikki's` user name and the
AWS access portal URL that they'll use to sign in to the organization. Record this
information for future use.

You are taken to the **New user sign up** page where you can set
`Nikki's` password and [register their
MFA device](enable-mfa.md "enable-mfa.md"). 2. After setting `Nikki's` password, you are navigated to the
**Sign in** page. Enter `nikkiw` and choose
**Next**, then enter `Nikki's` password and
choose **Sign in**. 3. The AWS access portal opens displaying the organization and applications you can
access.

Select the organization to expand it into a list of AWS accounts then select the
account to display the roles that you can use to access resources in the account.

Each permission set has two management methods you can use, either
**Role** or **Access keys**.

    * **Role**, for example
     `AdministratorAccess` - Opens the AWS Console Home.
    * **Access keys** - Provides credentials that you can use with
     the AWS CLI or and AWS SDK. Includes the information for using either short-term
     credentials that automatically refresh or short-term access keys. For more
     information, see [Getting IAM Identity Center user credentials for the AWS CLI or AWS
     SDKs](howtogetcredentials.md "howtogetcredentials.md").

4. Choose the **Role** link to sign in to the AWS Console Home.
   You are signed in and navigated to the AWS Console Home page. Explore the console and
   confirm that you have the access you expected.

Now that you've created an administrative user in IAM Identity Center, you can:

- [Assign applications](manage-your-applications.md "manage-your-applications.md")
- [Add other users](addusers.md "addusers.md")
- [Assign users to accounts](assignusers.md "assignusers.md")
- [Configure additional permission
  sets](howtocreatepermissionset.md "howtocreatepermissionset.md")

###### Note

You can assign multiple permission sets to the same user. To follow the best
practice of applying least-privilege permissions, after you create your administrative
user, create a more restrictive permission set and assign it to the same user. That
way, you can access your AWS account with only the permissions that you require,
rather than administrative permissions.
After your users [accept their invitation](howtoactivateaccount.md "howtoactivateaccount.md") to
activate their account and they sign into the AWS access portal, the only items that appear in the
portal are for the AWS accounts, roles, and applications to which they are assigned.
