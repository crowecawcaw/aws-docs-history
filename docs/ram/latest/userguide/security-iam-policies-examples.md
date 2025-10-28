# Example IAM policies for AWS RAM

This topic includes examples of IAM policies for AWS RAM that demonstrate sharing specific
resources and resource types and restricting sharing.

###### Examples of IAM policies

- [Allow sharing of specific resources](#owner-share-specific-resources "#owner-share-specific-resources")
- [Allow sharing of specific resource types](#owner-share-resource-types "#owner-share-resource-types")
- [Restrict sharing with external AWS accounts](#control-access-owner-external "#control-access-owner-external")

## Example 1: Allow sharing of specific

resources

You can use an IAM permission policy to restrict principals to associating
only specific resources with resource shares.

For example, the following policy limits principals to sharing only the
resolver rule with the specified Amazon Resource Name (ARN). The operator
`StringEqualsIfExists` allows a request if either the request doesn't
include a `ResourceArn` parameter, or if it does include that parameter, that
its value exactly matches the specified ARN.

For more
information about when and why to use `...IfExists` operators, see [...IfExists condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists") in the
_IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": ["ram:CreateResourceShare", "ram:AssociateResourceShare"],
 "Resource": "*",
 "Condition": {
 "StringEqualsIfExists": {
 "ram:ResourceArn": "arn:aws:route53resolver:us-west-2:123456789012:resolver-rule/rslvr-rr-5328a0899aexample"
 }
 }
 }]
}`

```

## Example 2: Allow sharing of specific

resource types

You can use an IAM policy to limit principals to associating only specific
resource types with resource shares.

The actions, `AssociateResourceShare` and `CreateResourceShare`,
can accept principals and `resourceArns` as independent input parameters.
Therefore, AWS RAM authorizes each principal and resource independently, so there could be
multiple [request contexts](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-reqcontext.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-reqcontext.md"). This means when a principal is being associated to a
AWS RAM resource share, the `ram:RequestedResourceType` condition key is not
present in the request context. Similarly, when a resource is being associated to a
AWS RAM resource share, the `ram:Principal` condition key is not present in the
request context. Therefore, to allow `AssociateResourceShare` and
`CreateResourceShare` when associating principals to the AWS RAM resource share, you can use the [`Null` condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null").

For example, the following policy limits principals to sharing only
Amazon Route 53 resolver
rules and allows
them to associate any principal to that share.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowOnlySpecificResourceType",
 "Effect": "Allow",
 "Action": ["ram:CreateResourceShare", "ram:AssociateResourceShare"],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ram:RequestedResourceType": "route53resolver:ResolverRule"
 }
 }
 },
 {
 "Sid": "AllowAssociatingPrincipals",
 "Effect": "Allow",
 "Action": ["ram:CreateResourceShare", "ram:AssociateResourceShare"],
 "Resource": "*",
 "Condition": {
 "Null": {
 "ram:Principal": "false"
 }
 }
 }
 ]
}`

```

## Example 3: Restrict sharing with

external AWS accounts

You can use an IAM policy to prevent principals from sharing resources
with AWS accounts that are outside of its AWS organization.

For example, the following IAM policy prevents principals from adding
external AWS accounts to resource shares.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "ram:CreateResourceShare",
 "Resource": "*",
 "Condition": {
 "Bool": {
 "ram:RequestedAllowsExternalPrincipals": "false"
 }
 }
 }]
}`

```
