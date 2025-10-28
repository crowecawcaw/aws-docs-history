# Strongly recommended

controls with preventive behavior

The following strongly recommended controls have preventive behavior.

###### Topics

- [Disallow Creation of Access Keys
  for the Root User](#disallow-root-access-keys "#disallow-root-access-keys")
- [Disallow Actions as a Root
  User](#disallow-root-auser-actions "#disallow-root-auser-actions")

## Disallow Creation of Access Keys

for the Root User

Secures your AWS accounts by disallowing creation of access keys for the
root user. We recommend that you instead create access keys for the IAM users
or IAM Identity Center users, which grant limited permissions to interact with your AWS
account. This is a preventive control with strongly recommended guidance. By
default, this control is not enabled.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRRESTRICTROOTUSERACCESSKEYS",
 "Effect": "Deny",
 "Action": "iam:CreateAccessKey",
 "Resource": [
 "*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:PrincipalArn": [
 "arn:aws:iam::*:root"
 ]
 }
 }
 }
 ]
}`

```

## Disallow Actions as a Root

User

Secures your AWS accounts by disallowing account access with root user
credentials, which are credentials of the account owner that allow
unrestricted access to all resources in the account. Instead, we recommend
that you create IAM Identity Center users for everyday interaction with your AWS
account. This is a preventive control with strongly recommended guidance. By
default, this control is not enabled.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRRESTRICTROOTUSER",
 "Effect": "Deny",
 "Action": "*",
 "Resource": [
 "*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:PrincipalArn": [
 "arn:aws:iam::*:root"
 ]
 }
 }
 }
 ]
}`

```
