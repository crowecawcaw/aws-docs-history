

# Accessing a member account that has OrganizationAccountAccessRole with AWS Organizations
<a name="orgs_manage_accounts_access-cross-account-role"></a>

When you create a member account using the AWS Organizations console, AWS Organizations *automatically* creates an IAM role named `OrganizationAccountAccessRole` in the account. This role has full administrative permissions in the member account. The scope of access for this role includes all principals in the management account, such that the role is configured to grant that access to the organization's management account.

You can create an identical role for an invited member account by following the steps in [Creating OrganizationAccountAccessRole for an invited account with AWS Organizations](orgs_manage_accounts_create-cross-account-role.md).

To use this role to access the member account, you must sign in as a user from the management account that has permissions to assume the role. To configure these permissions, perform the following procedure. We recommend that you grant permissions to groups instead of users for ease of maintenance.

------
#### [ AWS Management Console ]

**To grant permissions to members of an IAM group in the management account to access the role**

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/) as a user with administrator permissions in the management account. This is required to delegate permissions to the IAM group whose users will access the role in the member account.

1. <a name="step-create-policy"></a>Start by creating the managed policy that you need later in [Step 14](#step-choose-group). 

   In the navigation pane, choose **Policies** and then choose **Create policy**.

1. Choose the **Visual** option.

1. For **Service**, enter **STS** in the search box to filter the list, and then choose the **STS** option.

1. For **Actions allowed**, enter **assume** in the search box to filter the list, and then choose the **AssumeRole** option.

1. For **Resources**, choose **Specific**, and then choose **Add ARNs**.

1. For **Resources in**, choose **Other account**, and enter the ID of the member account you just created.

1. For **Resource role name with path**, enter the name of the role that you created previously (we recommended naming it `OrganizationAccountAccessRole`).

1. Choose **Add ARNs** when the dialog box displays the correct ARN.

1. (Optional) If you want to require multi-factor authentication (MFA), or restrict access to the role from a specified IP address range, expand **Request conditions**, and select the options you want to enforce.

1. Choose **Next**.

1. On the **Review and create** page, enter a name for the new policy. For example : **GrantAccessToOrganizationAccountAccessRole**. You can also add an optional description. 

1. <a name="step-end-policy"></a>Choose **Create policy** to save your new managed policy.

1. <a name="step-choose-group"></a>Now that you have the policy available, you can attach it to a group.

   In the navigation pane, choose **IAM user groups** and then choose the name of the group (not the check box) whose members you want to be able to assume the role in the member account. If necessary, you can create a new group.

1. Choose the **Permissions** tab, choose **Add permissions**, and then choose **Attach policies**.

1. (Optional) In the **Search** box, you can start typing the name of your policy to filter the list until you can see the name of the policy you just created in [Step 2](#step-create-policy) through [Step 13](#step-end-policy). You can also filter out all of the AWS managed policies by choosing **All types** and then choosing **Customer managed**.

1. Select the check box next to your policy, and then choose **Attach policies**.

------

IAM users that are members of the group now have permissions to switch to the new role in the AWS Organizations console by using the following procedure.

------
#### [ AWS Management Console ]

**To switch to the role for the member account**

When using the role, the user has administrator permissions in the new member account. Instruct your IAM users who are members of the group to do the following to switch to the new role. 

1. From the upper-right corner of the AWS Organizations console, choose the link that contains your current sign-in name and then choose **Switch Role**.

1. Enter the administrator-provided account ID number and role name.

1. For **Display Name**, enter the text that you want to show on the navigation bar in the upper-right corner in place of your user name while you are using the role. You can optionally choose a color.

1. Choose **Switch Role**. Now all actions that you perform are done with the permissions granted to the role that you switched to. You no longer have the permissions associated with your original IAM user until you switch back.

1. When you finish performing actions that require the permissions of the role, you can switch back to your normal IAM user. Choose the role name in the upper-right corner (whatever you specified as the **Display Name**) and then choose **Back to {{UserName}}**.

------