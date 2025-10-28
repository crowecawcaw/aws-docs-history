# Example service control policies for AWS Organizations and

AWS RAM

AWS RAM supports service control policies (SCPs). SCPs are policies that you attach to
elements in an organization to manage permissions within that organization. An SCP applies
to all AWS accounts [under
the element to which you attach the SCP](../../../organizations/latest/userguide/orgs_manage_policies_inheritance_auth.md "../../../organizations/latest/userguide/orgs_manage_policies_inheritance_auth.md"). SCPs offer central control over the
maximum available permissions for all accounts in your organization. They can help you to
ensure your AWS accounts stay within your organization’s access control guidelines. For
more information, see [Service
control policies](../../../organizations/latest/userguide/orgs_manage_policies_type-auth.md "../../../organizations/latest/userguide/orgs_manage_policies_type-auth.md") in the _AWS Organizations User Guide_.

## Prerequisites

To use SCPs, you must first do the following:

- Enable all features in your organization. For more information, see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the
  _AWS Organizations User Guide_
- Enable SCPs for use within your organization. For more information, see [Enabling and disabling policy types](../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md "../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md") in the _AWS Organizations User
  Guide_
- Create the SCPs that you need. For more information about creating SCPs, see
  [Creating and updating SCPs](../../../organizations/latest/userguide/orgs_manage_policies_scp-create.md "../../../organizations/latest/userguide/orgs_manage_policies_scp-create.md") in the _AWS Organizations User
  Guide_.

## Example Service Control Policies

###### Contents

- [Example 1: Prevent external sharing](security-scp.md#example-one "security-scp.md#example-one")
- [Example 2: Prevent users from accepting resource share
  invitations from external accounts outside your organization](security-scp.md#example-two "security-scp.md#example-two")
- [Example 3: Allow specific accounts to share specific
  resource types](security-scp.md#example-three "security-scp.md#example-three")
- [Example 4: Prevent sharing with the entire
  organization or with organizational units](security-scp.md#example-four "security-scp.md#example-four")
- [Example 5: Allow sharing with only specific
  principals](security-scp.md#example-five "security-scp.md#example-five")

The following examples show how you can control various aspects of resource sharing in
an organization.

### Example 1: Prevent external sharing

The following SCP prevents users from creating resource shares that allow sharing
with principals that are outside of the sharing user's organization.

AWS RAM authorizes APIs separately for each principal and resource listed in the call.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ram:CreateResourceShare",
 "ram:UpdateResourceShare"
 ],
 "Resource": "*",
 "Condition": {
 "Bool": {
 "ram:RequestedAllowsExternalPrincipals": "true"
 }
 }
 }
 ]
}`

```

### Example 2: Prevent users from accepting resource share

invitations from external accounts outside your organization

The following SCP blocks any principal in an affected account from accepting an
invitation to use a resource share. Resource shares that are shared to other
accounts in the same organization as the sharing account don't generate invitations
and are therefore not affected by this SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ram:AcceptResourceShareInvitation",
 "Resource": "*"
 }
 ]
}`

```

### Example 3: Allow specific accounts to share specific

resource types

The following SCP allows _only_ accounts
`111111111111` and `222222222222` to
create new resource shares that share Amazon EC2 prefix lists or to associate prefix
lists with existing resource shares.

AWS RAM authorizes APIs separately for each principal and resource listed in the call.

The operator `StringEqualsIfExists` allows a request if either the
request doesn't include a resource type parameter, or if it does include that
parameter, that its value exactly matches the specified resource type. If you're
including a principal you must have `...IfExists`.

For more
information about when and why to use `...IfExists` operators, see [...IfExists condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists") in the
_IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ram:AssociateResourceShare",
 "ram:CreateResourceShare"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:PrincipalAccount": [
 "111111111111",
 "222222222222"
 ]
 },
 "StringEqualsIfExists": {
 "ram:RequestedResourceType": "ec2:PrefixList"
 }
 }
 }
 ]
}`

```

### Example 4: Prevent sharing with the entire

organization or with organizational units

The following SCP prevents users from creating resource shares that share
resources with an entire organization or with any organizational units. Users
_can_ share with individual AWS accounts in the
organization, or with IAM roles or users.

AWS RAM authorizes APIs separately for each principal and resource listed in the call.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ram:CreateResourceShare",
 "ram:AssociateResourceShare"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ram:Principal": [
 "arn:aws:organizations::*:organization/*",
 "arn:aws:organizations::*:ou/*"
 ]
 }
 }
 }
 ]
}`

```

### Example 5: Allow sharing with only specific

principals

The following example SCP allows users to share resources with
_only_ organization `o-12345abcdef,`
organizational unit `ou-98765fedcba`, and AWS account
`111111111111`.

If you're using an `"Effect": "Deny"` element with a negated
condition operator, like `StringNotEqualsIfExists`, the request is still denied even if the condition key is not present.
Use a `Null` condition operator to check if a condition key is absent at the time of authorization.

AWS RAM authorizes APIs separately for each principal and resource listed in the call.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ram:AssociateResourceShare",
 "ram:CreateResourceShare"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "ram:Principal": [
 "arn:aws:organizations::123456789012:organization/o-12345abcdef",
 "arn:aws:organizations::123456789012:ou/o-12345abcdef/ou-98765fedcba",
 "111111111111"
 ]
 },
 "Null": {
 "ram:Principal": "false"
 }
 }
 }
 ]
}`

```
