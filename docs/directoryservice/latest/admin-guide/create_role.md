# Creating a new IAM role

If you need to create a new IAM role for use with AWS Directory Service, you must create it using
the IAM console. Once the role has been created, you must then set up a trust
relationship with that role before you can see that role in the AWS Directory Service console. For more
information, see [Editing the trust relationship for an existing IAM
role](edit_trust.md "edit_trust.md").

###### Note

The user performing this task must have permission to perform the following IAM
actions. For more information, see [Identity-based
policies (IAM policies)](IAM_Auth_Access_Overview.md#IAM_Auth_Access_ManagingAccess_IdentityBased "IAM_Auth_Access_Overview.md#IAM_Auth_Access_ManagingAccess_IdentityBased").

- iam:PassRole
- iam:GetRole
- iam:CreateRole
- iam:PutRolePolicy

###### To create a new role in the IAM console

1. In the navigation pane of the IAM console,
   choose **Roles**. For more information, see [Creating a role (AWS Management Console)](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User
   Guide_.
2. Choose **Create role**.
3. Under **Choose the service that will use this role**, choose
   **Directory Service**, and then choose
   **Next**.
4. Select the check box next to the policy (for example,
   **AmazonEC2FullAccess**) that you want to apply to your
   directory users, and then choose **Next**.
5. If necessary, add a tag to the role, and then choose
   **Next**.
6. Provide a **Role name** and optional
   **Description**, and then choose **Create
   role**.
   **Example: Create a role to enable AWS Management Console
   access**

The following checklist provides an example of the tasks you must complete to create a
new IAM role that will give specific AWS Managed Microsoft AD users access to the Amazon EC2
console.

1. Create a role with the IAM console using the procedure above. When prompted
   for a policy, choose **AmazonEC2FullAccess**.
2. Use the steps in [Editing the trust relationship for an existing IAM
   role](edit_trust.md "edit_trust.md") to
   edit the role you just created, and then add the required trust relationship
   information to the policy document. This step is necessary for the role to be
   visible immediately after you enable access to the AWS Management Console in the next
   step.
3. Follow the steps in [Enabling AWS Management Console access with AWS Managed Microsoft AD
   credentials](ms_ad_management_console_access.md "ms_ad_management_console_access.md") to configure general
   access to the AWS Management Console.
4. Follow the steps in [Assigning users or groups to an existing IAM
   role](assign_role.md "assign_role.md")
   to add the users who need full access to EC2 resources to the new role.
