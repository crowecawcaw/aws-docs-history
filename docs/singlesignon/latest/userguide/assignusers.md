# Assign user or group access to AWS accounts

Use the following procedure to assign single sign-on access to users and groups in
your connected directory and use permission sets to determine their level of
access.

To check existing user and group access, see [View and change a permission
set](howtoviewandchangepermissionset.md "howtoviewandchangepermissionset.md").

###### Note

To simplify administration of access permissions, we recommended that you
assign access directly to groups rather than to individual users. With groups
you can grant or deny permissions to groups of users rather than having to apply
those permissions to each individual. If a user moves to a different
organization, you simply move that user to a different group and they
automatically receive the permissions that are needed for the new
organization.

###### To assign user or group access to AWS accounts

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").

###### Note

Make sure that the IAM Identity Center console is using the Region where your
AWS Managed Microsoft AD directory is located before you move to the next
step. 2. In the navigation pane, under **Multi-account
permissions**, choose
**AWS accounts**. 3. On the **AWS accounts** page, a tree view list of your
organization displays. Select the checkbox next to the AWS account to
which you want to assign access. If you are setting up administrative access
for IAM Identity Center, select the checkbox next to the management account .

###### Note

You can select up to 10 AWS accounts at a time per permission set
when you assign single sign-on access to users and groups. To assign
more than 10 AWS accounts to the same set of users and groups, repeat
this procedure as required for the additional accounts. When prompted,
select the same users, groups, and permission set. 4. Choose **Assign users or groups**. 5. For **Step 1: Select users and groups**, on the
**Assign users and groups to
"`AWS-account-name`"** page, do
the following:

    1. On the **Users** tab, select one or more users to
     whom to grant single sign-on access.


    To filter the results, start typing the name of the user that you
     want in the search box.
    2. On the **Groups** tab, select one or more groups
     to which to grant single sign-on access.


    To filter the results, start typing the name of the group that you
     want in the search box.
    3. To display the users and groups that you selected, choose the
     sideways triangle next to **Selected users and
     groups**.
    4. After you confirm that the correct users and groups are selected,
     choose **Next**.

6. For **Step 2: Select permission sets**, on the
   **Assign permission sets to
   "`AWS-account-name`"** page, do
   the following:
   1. Select one or more permission sets. If required, you can create
      and select new permission sets.
      - To select one or more existing permission sets, under
        **Permission sets**, select the
        permission sets that you want to apply to the users and
        groups that you selected in the previous step.
      - To create one or more new permission sets, choose
        **Create permission set**, and follow
        the steps in [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md"). After you
        create the permission sets that you want to apply, in the
        IAM Identity Center console, return to **AWS accounts**
        and follow the instructions until you reach **Step
        2: Select permission sets**. When you reach
        this step, select the new permission sets that you created,
        and proceed to the next step in this procedure.

   2. After you confirm that the correct permission sets are selected,
      choose **Next**.

7. For **Step 3: Review and Submit**, on the
   **Review and submit assignments to
   "`AWS-account-name`"** page, do
   the following:
   1. Review the selected users, groups, and permission sets.
   2. After you confirm that the correct users, groups, and permission
      sets are selected, choose **Submit**.

###### Considerations

    * The user and group assignment process might take a few minutes to
     complete. Leave this page open until the process successfully
     completes.
    * ###### Note

    You might need to grant users or groups permissions to operate in the AWS Organizations management account. Because it is a highly privileged account, additional security restrictions require you to have the [IAMFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess") policy or equivalent permissions before you can set this up. These additional security restrictions are not required for any of the member accounts in your AWS organization.

8. If either of the following applies, follow the steps in [Prompt users for MFA](mfa-getting-started.md "mfa-getting-started.md") to
   enable MFA for IAM Identity Center:
   - You're using the default Identity Center directory as your
     identity source.
   - You're using an AWS Managed Microsoft AD directory or a self-managed directory
     in Active Directory as your identity source and you are not using
     RADIUS MFA with AWS Directory Service.

###### Note

If you are using an external identity provider, note that the external
IdP, not IAM Identity Center, manages MFA settings. MFA in IAM Identity Center is not supported for
use by external IdPs.
When you set up account access for the administrative user, IAM Identity Center creates a
corresponding IAM role. This role, which is controlled by IAM Identity Center, is created in the
relevant AWS account, and the policies specified in the permission set are
attached to the role.

Alternatively, you can use [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_SSO.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SSO.md") to create and assign permission sets and assign users to
those permission sets. Users can then [sign in to the
AWS access portal](howtosignin.md "howtosignin.md") or use [AWS Command Line Interface (AWS CLI)](integrating-aws-cli.md "integrating-aws-cli.md") commands.
