# IAM users in the AWS Management Console

IAM users may be able to change their password from the AWS Management Console depending on their permissions. Otherwise, they must use an AWS access portal.
An IAM user is an identity within your AWS account that's granted specific custom permissions. You're an IAM user
if you didn't create the AWS account and your administrator or help desk employee provided you your sign-in credentials that include
an AWS account ID or account alias, an IAM user name, and password. For more information, see [IAM user](../../../signin/latest/userguide/iam-user-type.md "../../../signin/latest/userguide/iam-user-type.md")
in the _AWS Sign-In User Guide_.

If you have permissions from the following policy: [AWS: Allows IAM users to change their own console password on the Security credentials page](../../../IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-password-only.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-password-only.md"), you can change your password from the console. For more information, see
[How an IAM user changes their own password](../../../IAM/latest/UserGuide/id_credentials_passwords_user-change-own.md "../../../IAM/latest/UserGuide/id_credentials_passwords_user-change-own.md")
in the _AWS Identity and Access Management User Guide_.

If you don't have the requisite permissions to change your password from the AWS Management Console see, [Resetting your AWS IAM Identity Center user password](../../../singlesignon/latest/userguide/resetpassword-accessportal.md "../../../singlesignon/latest/userguide/resetpassword-accessportal.md") in the _AWS IAM Identity Center User Guide_.
