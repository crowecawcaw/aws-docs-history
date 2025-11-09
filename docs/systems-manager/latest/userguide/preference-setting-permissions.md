AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Grant or deny a user

permissions to update Session Manager preferences

Account preferences are stored as AWS Systems Manager (SSM) documents for each
AWS Region. Before a user can update account preferences for sessions in your
account, they must be granted the necessary permissions to access the type of
SSM document where these preferences are stored. These permissions are granted
through an AWS Identity and Access Management (IAM) policy.

###### Administrator policy to allow preferences to be created and

updated

An administrator can have the following policy to create and update
preferences at any time. The following policy allows permission to access
and update the `SSM-SessionManagerRunShell` document in
the us-east-2 account 123456789012.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ssm:CreateDocument",
 "ssm:GetDocument",
 "ssm:UpdateDocument",
 "ssm:DeleteDocument"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 ]
 }
 ]
}`

```

###### User policy to prevent preferences from being updated

Use the following policy to prevent end users in your account from
updating or overriding any Session Manager preferences.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ssm:CreateDocument",
 "ssm:GetDocument",
 "ssm:UpdateDocument",
 "ssm:DeleteDocument"
 ],
 "Effect": "Deny",
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 ]
 }
 ]
}`

```
