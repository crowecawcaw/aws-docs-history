# SCP syntax

Service control policies (SCPs) use a similar syntax to that used by AWS Identity and Access Management (IAM)
permission policies and [resource-based
policies](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based") (like Amazon S3 bucket policies). For more information about IAM policies
and their syntax, see [Overview of IAM
Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

An SCP is a plaintext file that is structured according to the rules of [JSON](http://json.org "http://json.org"). It uses the elements that are described in this
topic.

###### Note

All characters in your SCP count against its [maximum
size](orgs_reference_limits.md#min-max-values "orgs_reference_limits.md#min-max-values"). The examples in this guide show the SCPs formatted with extra white
space to improve their readability. However, to save space if your policy size
approaches the maximum size, you can delete any white space, such as space characters
and line breaks that are outside quotation marks.

For general information about SCPs, see [Service control policies (SCPs)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md").

## Elements summary

The following table summarizes the policy elements that you can use in SCPs. Some
policy elements are available only in SCPs that deny actions. The **Supported effects** column lists the effect type that you can use with
each policy element in SCPs.

| Element                                                    | Purpose                                                                                                                                                                                                                                                                                                                                    | Supported effects |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [Action](#scp-syntax-action "#scp-syntax-action")          | Specifies AWS service and actions that the SCP allows or<br>denies.                                                                                                                                                                                                                                                                        | `Allow`, `Deny`   |
| [Effect](#scp-syntax-effect "#scp-syntax-effect")          | Defines whether the SCP statement [allows](orgs_manage_policies_scps_evaluation.md#how_scps_allow "orgs_manage_policies_scps_evaluation.md#how_scps_allow") or [denies](orgs_manage_policies_scps_evaluation.md#how_scps_deny "orgs_manage_policies_scps_evaluation.md#how_scps_deny") access<br>to the IAM users and roles in an account. | `Allow`, `Deny`   |
| [Statement](#scp-syntax-statement "#scp-syntax-statement") | Serves as the container for policy elements. You can have multiple<br>statements in SCPs.                                                                                                                                                                                                                                                  | `Allow`, `Deny`   |
| [Statement ID (Sid)](#scp-syntax-sid "#scp-syntax-sid")    | (Optional) Provides a friendly name for the statement.                                                                                                                                                                                                                                                                                     | `Allow`, `Deny`   |
| [Version](#scp-syntax-version "#scp-syntax-version")       | Specifies the language syntax rules to use for processing the<br>policy.                                                                                                                                                                                                                                                                   | `Allow`, `Deny`   |
| [Condition](#scp-syntax-condition "#scp-syntax-condition") | Specifies conditions for when the statement is in effect.                                                                                                                                                                                                                                                                                  | `Allow,``Deny`    |
| [NotAction](#scp-syntax-action "#scp-syntax-action")       | Specifies AWS service and actions that are exempt from the SCP.<br>Used instead of the `Action` element.                                                                                                                                                                                                                                   | `Allow,``Deny`    |
| [Resource](#scp-syntax-resource "#scp-syntax-resource")    | Specifies the AWS resources that the SCP applies to.                                                                                                                                                                                                                                                                                       | `Allow,``Deny`    |
| [NotResource](#scp-syntax-resource "#scp-syntax-resource") | Specifies AWS resources that are exempt from the SCP. Used instead<br>of the `Resource` element.                                                                                                                                                                                                                                           | `Allow`, `Deny`   |

The following sections provide more information and examples of how policy elements
are used in SCPs.

###### Topics

- [Action and NotAction
  elements](#scp-syntax-action "#scp-syntax-action")
- [Condition element](#scp-syntax-condition "#scp-syntax-condition")
- [Effect element](#scp-syntax-effect "#scp-syntax-effect")
- [Resource and NotResource element](#scp-syntax-resource "#scp-syntax-resource")
- [Statement element](#scp-syntax-statement "#scp-syntax-statement")
- [Statement ID (Sid) element](#scp-syntax-sid "#scp-syntax-sid")
- [Version element](#scp-syntax-version "#scp-syntax-version")
- [Unsupported elements](#scp-syntax-unsupported "#scp-syntax-unsupported")

## `Action` and `NotAction`

elements

The value for the `Action` or `NotAction` element is a list (a
JSON array) of strings that identify AWS services and actions that are allowed or
denied by the statement.

Each string consists of the abbreviation for the service (such as "s3", "ec2", "iam",
or "organizations"), in all lowercase, followed by a colon and then an action from that
service. The actions and notactions are case-insensitive. Generally, they are all
entered with each word starting with an uppercase letter and the rest lowercase. For
example: `"s3:ListAllMyBuckets"`.

You also can use wildcard characters such as asterisk (\*) or question mark (?) in an
SCP:

- Use an asterisk (\*) as a wildcard to match multiple actions that share part of
  a name. The value `"s3:*"` means all actions in the Amazon S3 service. The
  value `"ec2:Describe*"` matches only the EC2 actions that begin with
  "Describe".
- Use the question mark (?) wildcard to match a single character.

For a list of all the services and the actions that they support in both AWS Organizations SCPs
and IAM permission policies, see [Actions, Resources,
and Condition Keys for AWS Services](../../../IAM/latest/UserGuide/reference_policies_actionsconditions.md "../../../IAM/latest/UserGuide/reference_policies_actionsconditions.md") in the
_IAM User Guide_.

For more information, see [IAM JSON Policy
Elements: Action](../../../IAM/latest/UserGuide/reference_policies_elements_action.md "../../../IAM/latest/UserGuide/reference_policies_elements_action.md") and [IAM JSON Policy
Elements: NotAction](../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md "../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md") in the _IAM User Guide_.

### Example of `Action`

element

The following example shows an SCP with a statement that permits account
administrators to delegate describe, start, stop, and terminate permissions for EC2
instances in the account. This is an example of an [allow list](orgs_manage_policies_scps_evaluation.md#how_scps_allow "orgs_manage_policies_scps_evaluation.md#how_scps_allow"), and is useful when the default `Allow *` policies
are **_not_** attached
so that, by default, permissions are implicitly denied. If the default `Allow
 *` policy is still attached to the root, OU, or account to which the
following policy is attached, the policy has no effect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances", "ec2:DescribeImages", "ec2:DescribeKeyPairs",
 "ec2:DescribeSecurityGroups", "ec2:DescribeAvailabilityZones", "ec2:RunInstances",
 "ec2:TerminateInstances", "ec2:StopInstances", "ec2:StartInstances"
 ],
 "Resource": "*"
 }
}`

```

The following example shows how you can [deny
access](orgs_manage_policies_scps_evaluation.md#how_scps_deny "orgs_manage_policies_scps_evaluation.md#how_scps_deny") to services that you don't want used in attached accounts. It
assumes that the default `"Allow *"` SCPs are still attached to all OUs
and the root. This example policy prevents the account administrators in attached
accounts from delegating any permissions for the IAM, Amazon EC2, and Amazon RDS services.
Any action from other services can be delegated as long as there isn't another
attached policy that denies them.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": [ "iam:*", "ec2:*", "rds:*" ],
 "Resource": "*"
 }
}`

```

### Example of `NotAction`

element

The following example shows how you can use a `NotAction` element to
exclude AWS services from the effect of the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LimitActionsInRegion",
 "Effect": "Deny",
 "NotAction": "iam:*",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:RequestedRegion": "us-west-1"
 }
 }
 }
 ]
}`

```

With this statement, affected accounts are limited to taking actions in the
specified AWS Region, except when using IAM actions.

## `Condition` element

You can specify a `Condition` element in allow and deny statements in an
SCP.

The following example shows how to use a condition element with an allow statement in
an SCP to permit specific principals to access AWS services.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"AllowServicesForSpecificPrincipal",
         "Effect":"Allow",
         "Action":[
            "ec2:*",
            "s3:*",
            "rds:*",
            "lambda:*",
            "cloudformation:*",
            "iam:*",
            "cloudwatch:*"
         ],
         "Resource":"*",
         "Condition":{
            "StringEquals":{
               "aws:PrincipalArn":[
                  "arn:aws:iam::123456789012:role/`specific-role`"
               ]
            }
         }
      }
   ]
}
```

The following example shows how to use a condition element with a deny statement in an
SCP to restrict access to any operations outside the `eu-central-1` and
`eu-west-1` Regions, except for actions in the specified services.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAllOutsideEU",
 "Effect": "Deny",
 "NotAction": [
 "`cloudfront:*",
 "iam:*",
 "route53:*",
 "support:*`"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:RequestedRegion": [
 "`eu-central-1",
 "eu-west-1`"
 ]
 }
 }
 }
 ]
}`

```

For more information, see [IAM JSON Policy
Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

## `Effect` element

Each statement must contain one `Effect` element. The value can be either
`Allow` or `Deny`. It affects any actions listed in the same
statement.

For more information, see [IAM JSON Policy
Elements: Effect](../../../IAM/latest/UserGuide/reference_policies_elements_effect.md "../../../IAM/latest/UserGuide/reference_policies_elements_effect.md") in the _IAM User Guide_.

### `"Effect": "Allow"`

The following example shows an SCP with a statement that contains an
`Effect` element with a value of `Allow` that permits
account users to perform actions for the Amazon S3 service. This example is useful in an
organization that uses the [allow list strategy](orgs_manage_policies_scps_evaluation.md#how_scps_allow "orgs_manage_policies_scps_evaluation.md#how_scps_allow")
(where the default `FullAWSAccess` policies are all detached so that
permissions are implicitly denied by default). The result is that the statement
[allows](orgs_manage_policies_scps_evaluation.md#how_scps_allow "orgs_manage_policies_scps_evaluation.md#how_scps_allow") the Amazon S3 permissions for any
attached accounts:

```
{
    "Statement": {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": "*"
    }
}
```

Even though this statement uses the same `Allow` value keyword as an
IAM permission policy, in an SCP it doesn't actually grant a user permission to do
anything. Instead, SCPs act as _filters_ that specify the
maximum permissions for the accounts in an organization, organizational unit (OU),
or account. In the preceding example, even if a user in the account had the
`AdministratorAccess` managed policy attached, this SCP limits
**_all_** users in
affected accounts to only Amazon S3 actions.

### `"Effect": "Deny"`

In a statement where the `Effect` element has a value of
`Deny`, you can also restrict access to specific resources or define
conditions for when SCPs are in effect.

The following shows an example of how to use a condition key in a deny
statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:*:*:instance/*",
 "Condition": {
 "StringNotEquals": {
 "ec2:InstanceType": "t2.micro"
 }
 }
 }
}`

```

This statement in an SCP sets a guardrail to prevent affected accounts (where the
SCP is attached to the account itself or to the organization root or OU that
contains the account), from launching Amazon EC2 instances if the Amazon EC2 instance isn't
set to `t2.micro`. Even if an IAM policy that allows this action is
attached to the account, the guardrail created by the SCP prevents it.

## `Resource` and `NotResource` element

In statements where the `Effect` element has a value of `Allow`,
you can specify only "\*" in the `Resource` element of an SCP. You can't
specify individual resource Amazon Resource Names (ARNs).

You can use wildcard characters such as asterisk (\*) or question mark (?) in the
resource element:

- Use an asterisk (\*) as a wildcard to match multiple actions that share part of
  a name.
- Use the question mark (?) wildcard to match a single character.

In statements where the `Effect` element has a value of `Deny`,
you _can_ specify individual ARNs, as shown in the following
example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAccessToAdminRole",
 "Effect": "Deny",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DeleteRole",
 "iam:DeleteRolePermissionsBoundary",
 "iam:DeleteRolePolicy",
 "iam:DetachRolePolicy",
 "iam:PutRolePermissionsBoundary",
 "iam:PutRolePolicy",
 "iam:UpdateAssumeRolePolicy",
 "iam:UpdateRole",
 "iam:UpdateRoleDescription"
 ],
 "Resource": [
 "arn:aws:iam::*:role/`role-to-deny`"
 ]
 }
 ]
}`

```

This SCP restricts IAM users and roles in affected accounts from making changes to a
common administrative IAM role created in all accounts in your organization.

The following example shows how to use a `NotResource` element to exclude
specific Amazon Bedrock models from the effect of the policy.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"Statement1",
         "Effect":"Deny",
         "Action":[
            "bedrock:InvokeModel",
            "bedrock:InvokeModelWithResponseStream"
         ],
         "NotResource":[
            "arn:aws:bedrock:*::foundation-model/`model-to-permit`"
         ]
      }
   ]
}
```

For more information, see [IAM JSON Policy
Elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the _IAM User Guide_.

## `Statement` element

An SCP consists of one or more `Statement` elements. You can have only one
`Statement` keyword in a policy, but the value can be a JSON array of
statements (surrounded by [ ] characters).

The following example shows a single statement that consists of single
`Effect`, `Action`, and `Resource` elements.

```
    "Statement": {
        "Effect": "Allow",
        "Action": "*",
        "Resource": "*"
    }
```

The following example includes two statements as an array list inside one
`Statement` element. The first statement allows all actions, while the
second denies any EC2 actions. The result is that an administrator in the account can
delegate any permission _except_ those from Amazon Elastic Compute Cloud
(Amazon EC2).

```
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": "ec2:*",
            "Resource": "*"
        }
    ]
```

For more information, see [IAM JSON Policy
Elements: Statement](../../../IAM/latest/UserGuide/reference_policies_elements_statement.md "../../../IAM/latest/UserGuide/reference_policies_elements_statement.md") in the _IAM User Guide_.

## Statement ID (`Sid`) element

The `Sid` is an optional identifier that you provide for the policy
statement. You can assign a `Sid` value to each statement in a statement
array. The following example SCP shows a sample `Sid` statement.

```
{
    "Statement": {
        "Sid": "AllowsAllActions",
        "Effect": "Allow",
        "Action": "*",
        "Resource": "*"
    }
}
```

For more information, see [IAM JSON Policy Elements:
Id](../../../IAM/latest/UserGuide/reference_policies_elements_id.md "../../../IAM/latest/UserGuide/reference_policies_elements_id.md") in the _IAM User Guide_.

## `Version` element

Every SCP must include a `Version` element with the value
`"2012-10-17"`. This is the same version value as the most recent version
of IAM permission policies.

For more information, see [IAM JSON Policy
Elements: Version](../../../IAM/latest/UserGuide/reference_policies_elements_version.md "../../../IAM/latest/UserGuide/reference_policies_elements_version.md") in the _IAM User Guide_.

## Unsupported elements

The following elements aren't supported in SCPs:

- `NotPrincipal`
- `Principal`
