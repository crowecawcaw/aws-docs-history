

# IAM users in the AWS Management Console
<a name="iam-password"></a>

IAM users may be able to change their password from the AWS Management Console depending on their permissions. Otherwise, they must use an AWS access portal. An IAM user is an identity within your AWS account that's granted specific custom permissions. You're an IAM user if you didn't create the AWS account and your administrator or help desk employee provided you your sign-in credentials that include an AWS account ID or account alias, an IAM user name, and password. For more information, see [IAM user](https://docs.aws.amazon.com/signin/latest/userguide/iam-user-type.html) in the *AWS Sign-In User Guide*.

If you have permissions from the following policy: [AWS: Allows IAM users to change their own console password on the Security credentials page](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-password-only.html), you can change your password from the console. For more information, see [How an IAM user changes their own password](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_user-change-own.html) in the *AWS Identity and Access Management User Guide*.

If you don't have the requisite permissions to change your password from the AWS Management Console see, [ Resetting your AWS IAM Identity Center user password](https://docs.aws.amazon.com/singlesignon/latest/userguide/resetpassword-accessportal.html) in the *AWS IAM Identity Center User Guide*.