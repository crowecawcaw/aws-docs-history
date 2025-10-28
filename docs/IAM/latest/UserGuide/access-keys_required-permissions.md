# Permissions required to manage access

keys

###### Note

`iam:TagUser` is an optional permission for adding and editing
descriptions for the access key. For more information, see [Tag IAM users](id_tags_users.md "id_tags_users.md")

To create access keys for your own IAM user, you must have the permissions from the
following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateOwnAccessKeys",
 "Effect": "Allow",
 "Action": [
 "iam:CreateAccessKey",
 "iam:GetUser",
 "iam:ListAccessKeys",
 "iam:TagUser"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 }
 ]
}`

```

To update access keys for your own IAM user, you must have the permissions from the
following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageOwnAccessKeys",
 "Effect": "Allow",
 "Action": [
 "iam:CreateAccessKey",
 "iam:DeleteAccessKey",
 "iam:GetAccessKeyLastUsed",
 "iam:GetUser",
 "iam:ListAccessKeys",
 "iam:UpdateAccessKey",
 "iam:TagUser"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 }
 ]
}`

```
