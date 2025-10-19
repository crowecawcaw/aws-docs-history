# Disable user access to AWS accounts and
 applications in IAM Identity Center

When you disable user access in your IAM Identity Center directory, you cannot edit their user
 details, reset their password, add the user to a group, or view their group membership.
 Disabling user access prevents them from signing in to the AWS access portal and they will no
 longer have access to their assigned AWS accounts and applications. Use disable user access for temporary access removal when you might need to restore access later.

Use the following procedure to disable user access in your Identity Center directory using
 the IAM Identity Center console.

###### Note

When you disable user access or delete a user in IAM Identity Center, that user will immediately
 be prevented from signing in to the AWS access portal and will not be able to create new sign
 in sessions. For more information, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").

###### To disable user access in IAM Identity Center

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").


###### Important

The instructions on this page apply to [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/").
 They do not apply to [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
 (IAM). IAM Identity Center users, groups, and user credentials are different from IAM
 users, groups, and IAM user credentials. If you are looking for
 instructions on deactivating users in IAM, see [Managing
 IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html") in the *AWS Identity and Access Management User
 Guide*.
2. Choose **Users**.
3. Select the username of the user whose access you want to disable.
4. Below the username of the user whose access you want to disable, in the **General
 information** section, choose **Disable
 user access**.
5. In the **Disable user access** dialog box, choose **Disable
 user access**.
