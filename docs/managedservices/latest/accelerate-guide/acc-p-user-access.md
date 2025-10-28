# Creating an IAM role for on-demand patching of AMS Accelerate

After your account is onboarded to AMS Accelerate patching, AMS Accelerate deploys a managed policy,
**amspatchmanagedpolicy**. This policy contains the required permissions for on-demand patching using the AMS automation document
`AWSManagedServices-PatchInstance`. To use this automation document, the account administrator creates a IAM role for users. Follow these steps:

**Create a role using the AWS Management Console**:

1. Sign in to the AWS Management Console and open the
   [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Roles**, then **Create role**.
3. Choose the **Another AWS account** role type.
4. For **Account ID**, enter the AWS account ID that you want to grant access to your resources.

The administrator of the specified account can grant permission to assume this role to any IAM user in
that account. To do this, the administrator attaches a policy to the user, or a group, that grants
permission for the **sts:AssumeRole** action. That policy must specify the role's Amazon Resource Name (ARN) as the resource. Note the following:

    * If you are granting permissions to users from an account that you do not control, and the users will assume this role programmatically,
     then choose **Require external ID**. The external ID can be any word or number that is agreed upon between you and the administrator of the
     third-party account. This option automatically adds a condition to the trust policy that enables the user to assume the role only if the request includes
     the correct **sts:ExternalID**. For more information, see 
     [How to use an external ID when granting access to your AWS resources to a third party](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md").
    * If you want to restrict the role to users who sign in with multi-factor authentication (MFA), choose **Require MFA**. This adds
     a condition to the role's trust policy that checks for an MFA sign-in. A user who wants to assume the role must sign in with a temporary one-time password from a
     configured MFA device. Users without MFA authentication can't assume the role. For more information about MFA, see 
     [Using multi-factor authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md").

5. Choose **Next: Permissions**.

IAM includes a list of policies in the account. Under **Add Permissions**, enter **amspatchmanagedpolicy** in the filter box and
select the checkbox for this permissions policy. Click **Next**. 6. Under **Role details**, enter a Role name such as PatchRole, add a description for the role (recommended), also add tags to
help you identify this role. Role names aren't case sensitive, but must be unique within the AWS account. When finished, click **Create Role**.

###### Note

Role names can't be edited after they've been created.
