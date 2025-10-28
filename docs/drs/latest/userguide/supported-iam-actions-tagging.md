# Grant permission to tag resources during creation

Some resource-creating Amazon DRS API actions allow you to specify tags when you
create the resource. You can use resource tags to implement attribute-based control
(ABAC).

To allow users to tag resources on creation, they must have permissions to use the
action that creates the resource, such as `drs:CreateSourceServerForDrs`
for source server or `drs:CreateRecoveryInstanceForDrs` for Recovery
instances. If tags are specified in the resource-creating action, Amazon performs
additional authorization on the `drs:TagResource` action to verify that
users have permissions to create tags. Therefore, users must also have explicit
permissions to use the `drs:TagResource` action.

In the IAM policy definition for the `drs:TagResource` action, use the Condition
element with the `drs:CreateAction` condition key to give tagging permissions to the
action that creates the resource.

The following example demonstrates a policy that allows an agent installer to
create a source server or recover instance and apply any tags to the resource on
creation. The installer is not permitted to tag any existing resources (it cannot
call the `drs:TagResource` action directly).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "drs:GetAgentInstallationAssetsForDrs",
 "drs:SendClientLogsForDrs",
 "drs:CreateSourceServerForDrs",
 "drs:CreateRecoveryInstanceForDrs",
 "drs:DescribeRecoveryInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "drs:TagResource",
 "Resource": "arn:aws:drs:*:*:source-server/*",
 "Condition": {
 "StringEquals": {
 "drs:CreateAction": "CreateSourceServerForDrs"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "drs:TagResource",
 "Resource": "arn:aws:drs:*:*:recovery-instance/*",
 "Condition": {
 "StringEquals": {
 "drs:CreateAction": "CreateRecoveryInstanceForDrs"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "drs:IssueAgentCertificateForDrs",
 "Resource": "arn:aws:drs:*:*:source-server/*"
 }
 ]
}`

```

The `drs:TagResource` action is only evaluated if tags are applied during the
resource-creating action. Therefore, an installer that has permissions to create a resource (assuming
there are no tagging conditions) does not require permissions to use the `drs:TagResource` action
if no tags are specified in the request. However, if the installer attempts to create a resource with
tags, the request fails if the installer does not have permissions to use the `drs:TagResource` action.
