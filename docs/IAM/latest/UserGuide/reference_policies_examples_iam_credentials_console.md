# IAM: Allows IAM users

to update their own credentials programmatically and in the console

This example shows how you might create an identity-based policy that allows IAM users to update their own access keys, signing
certificates, service specific credentials, and passwords. This policy defines permissions for programmatic and console access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListUsers",
 "iam:GetAccountPasswordPolicy"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:*AccessKey*",
 "iam:ChangePassword",
 "iam:GetUser",
 "iam:*ServiceSpecificCredential*",
 "iam:*SigningCertificate*"
 ],
 "Resource": ["arn:aws:iam::*:user/${aws:username}"]
 }
 ]
}`

```

To learn how a user can change their own password in the console, see [How an IAM user changes their own
password](id_credentials_passwords_user-change-own.md "id_credentials_passwords_user-change-own.md").
