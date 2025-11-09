Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Using tags to control access to account

connection resources

Tags
can be attached to
the
resource or passed in the request to services
that support tagging.
Resources
in policies can have tags, and some actions in policies can include tags. Tagging condition
keys include the `aws:RequestTag` and
`aws:ResourceTag`
condition keys. When you create an IAM policy, you can use
tag
condition keys to control the following:

- Which users can perform actions on a connection resource, based on tags that it
  already has.
- Which tags can be passed in an action's request.
- Whether specific tag keys can be used in a request.
  The following examples demonstrate how to specify tag conditions in policies for CodeCatalyst
  account connections users. For more information about condition keys, see [Policy condition keys in IAM](security-iam.md#id-based-policies-conditionkeys "security-iam.md#id-based-policies-conditionkeys").

## Example 1: Allow actions based

on tags in the request

The following policy grants users permission to approve account connections.

To do that, it allows the `AcceptConnection` and `TagResource`
actions if the request specifies a tag named `Project` with the value
`ProjectA`. (The `aws:RequestTag` condition key is used to
control which tags can be passed in an IAM request.) The `aws:TagKeys`
condition ensures tag key case sensitivity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecatalyst:AcceptConnection",
 "codecatalyst:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Project": "ProjectA"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["Project"]
 }
 }
 }
 ]
}`

```

## Example 2: Allow actions based

on resource tags

The following policy grants users permission to perform actions on, and get
information about, account connection resources.

To do that, it
allows specific actions if the connection has a tag named `Project` with the
value `ProjectA`. (The
`aws:ResourceTag`
condition key is used to control which tags can be passed in an IAM
request.)

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecatalyst:GetConnection",
 "codecatalyst:DeleteConnection",
 "codecatalyst:AssociateIamRoleToConnection",
 "codecatalyst:DisassociateIamRoleFromConnection",
 "codecatalyst:ListIamRolesForConnection",
 "codecatalyst:PutBillingAuthorization"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Project": "ProjectA"
 }
 }
 }
 ]
}`

```
