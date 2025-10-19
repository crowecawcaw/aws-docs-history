# Deny user access with Service Control Policies

To immediately deny access to make authorized API calls when an IAM Identity Center user's access is disabled 
 or the user is deleted, you can:


1. [Add or update](howtoviewandchangepermissionset.md "howtoviewandchangepermissionset.md") the [inline policy](permissionsetcustom.md#permissionsetsinlineconcept "permissionsetcustom.md#permissionsetsinlineconcept") of the permission set(s)
 assigned to the user by adding an explicit `Deny` effect for all actions on all
 resources.
2. Specify the `aws:userid` or `identitystore:userid`
 condition key.
Alternatively, you can use a [Service Control
 Policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html") to deny the user's access across all member accounts in your
 organization.

###### Example SCP to deny access

This denial policy blocks all AWS actions for a specific user, regardless of other permissions they might have been granted elsewhere. 
 This policy overrides any `Allow` policies.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement" : [
 {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:UserId": "*:`deleteduser@domain.com`"
 }
 }
 }
 ]
}`

```





JSON





```
`{
 "Version":"2012-10-17", 
 "Statement" : [
 {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "identitystore:UserId": "`DELETEDUSER_ID`"
 }
 }
 }
 ]
}`

```
