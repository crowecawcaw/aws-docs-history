# Delegate who can assign single sign-on

access to users and groups in the management account

Assigning single sign-on access to the management account using the IAM Identity Center console
is a privileged action. By default, only an AWS account root user or a user who has the
**AWSSSOMasterAccountAdministrator** and
**IAMFullAccess** AWS managed policies
attached, can assign single sign-on access to the management account. The
**AWSSSOMasterAccountAdministrator** and
**IAMFullAccess** policies manage single
sign-on access to the management account within an AWS Organizations organization.

Alternatively, you can use AWS CLI to create, attach policies to, and assign
permission sets. The following lists the commands for each step:

- To create a permission set: [create-permission-set](../../../cli/latest/reference/sso-admin/create-permission-set.md "../../../cli/latest/reference/sso-admin/create-permission-set.md")
- To attach AWS Managed Policy to a permission set: [attach-managed-policy-to-permission-set](../../../cli/latest/reference/sso-admin/attach-managed-policy-to-permission-set.md "../../../cli/latest/reference/sso-admin/attach-managed-policy-to-permission-set.md")
- To attach customer managed policy to a permission set: [attach-customer-managed-policy-to-permission-set](../../../cli/latest/reference/sso-admin/attach-customer-managed-policy-reference-to-permission-set.md "../../../cli/latest/reference/sso-admin/attach-customer-managed-policy-reference-to-permission-set.md")
- To assign a permission set to a principal: [create-account-assignment](../../../cli/latest/reference/sso-admin/create-account-assignment.md "../../../cli/latest/reference/sso-admin/create-account-assignment.md")
  Use the following steps to delegate permissions to manage single sign-on access to
  users and groups in your directory.

###### To grant permissions to manage single sign-on access to users and groups in

your directory

1. Sign in to the IAM Identity Center console as a root user of the management account or with
   another user who has administrator permissions to the
   management account.
2. Follow the steps in [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md") to create a permission set,
   and then do the following:
   1. On the **Create new permission set** page, select
      the **Create a custom permission set** check box,
      and then choose **Next: Details**.
   2. On the **Create new permission set page**,
      specify a name for the custom permission set and optionally, a
      description. If required, modify the session duration and specify a
      relay state URL.

   ###### Note

   For the relay state URL, you must specify a URL that is in the
   AWS Management Console. For example:

   `https://console.aws.amazon.com/ec2/`

   For more information, see [Set relay state for quick access to the
   AWS Management Console](howtopermrelaystate.md "howtopermrelaystate.md"). 3. Under **What policies do you want to include in your
   permission set?**, select the **Attach AWS
   managed policies** check box. 4. In the list of IAM policies, choose both the
   **AWSSSOMasterAccountAdministrator**
   and **IAMFullAccess** AWS managed
   policies. These policies grant permissions to any user and groups
   who are assigned access to this permission set in the future. 5. Choose **Next: Tags**. 6. Under **Add tags (optional)**, specify values for
   **Key** and **Value
   (optional)**, and then choose **Next:
   Review**. For more information about tags, see [Tagging AWS IAM Identity Center resources](tagging.md "tagging.md"). 7. Review the selections you made, and then choose
   **Create**.

3. Follow the steps in [Assign user or group access to AWS accounts](assignusers.md "assignusers.md") to assign the appropriate users and groups
   to the permission set that you just created.
4. Communicate the following to the assigned users: When they sign in to the
   AWS access portal and choose the **Accounts** tab, they must
   choose the appropriate role name to be authenticated with the permissions
   that you just delegated.
