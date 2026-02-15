# Identity-based policies for Amazon EC2

By default, users don't have permission to create or modify Amazon EC2 resources, or perform
tasks using the Amazon EC2 API, Amazon EC2 console, or CLI. To allow users to create or modify
resources and perform tasks, you must create IAM policies that grant users permission
to use the specific resources and API actions they'll need, and then attach those
policies to the users, groups, or IAM roles that require those permissions.

When you attach a policy to a user, group of users, or role it allows or denies the users
permission to perform the specified tasks on the specified resources. For more general
information about IAM policies, see [Policies and permissions in
IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_. For more information
about managing and creating IAM policies, see [Manage IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md").

An IAM policy must grant or deny permissions to use one or more Amazon EC2 actions. It
must also specify the resources that can be used with the action, which can be all
resources, or in some cases, specific resources. The policy can also include conditions
that you apply to the resource.

To get started, you can check whether the AWS managed policies for Amazon EC2 meet your
needs. Otherwise, you can create your own custom policies. For more information, see
[AWS managed policies for Amazon EC2](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

###### Contents

- [Policy syntax](#policy-syntax "#policy-syntax")
- [Actions for Amazon EC2](#UsingWithEC2_Actions "#UsingWithEC2_Actions")
- [Supported resource-level
  permissions for Amazon EC2 API actions](#ec2-supported-iam-actions-resources "#ec2-supported-iam-actions-resources")
- [Amazon Resource Names (ARNs) for Amazon EC2](#EC2_ARN_Format "#EC2_ARN_Format")
- [Condition keys for Amazon EC2](#amazon-ec2-keys "#amazon-ec2-keys")
- [Control access using attribute-based access](#control-access-with-tags "#control-access-with-tags")
- [Grant permissions to users, groups, and roles](#granting-iam-permissions "#granting-iam-permissions")
- [Check that users have the required
  permissions](#check-required-permissions "#check-required-permissions")

## Policy syntax

An IAM policy is a JSON document that consists of one or more statements.
Each statement is structured as follows.

```
{
  "Statement":[{
    "Effect":"`effect`",
    "Action":"`action`",
    "Resource":"`arn`",
    "Condition":{
      "`condition`":{
        "`key`":"`value`"
        }
      }
    }
  ]
}
```

There are various elements that make up a statement:

- **Effect:** The _effect_ can be
  `Allow` or `Deny`. By default, users
  don't have permission to use resources and API actions, so all requests
  are denied. An explicit allow overrides the default. An explicit deny
  overrides any allows.
- **Action**: The _action_ is the
  specific API action for which you are granting or denying permission. To
  learn about specifying _action_, see [Actions for Amazon EC2](#UsingWithEC2_Actions "#UsingWithEC2_Actions").
- **Resource**: The resource that's affected by the
  action. Some Amazon EC2 API actions allow you to include specific resources
  in your policy that can be created or modified by the action. You
  specify a resource using an Amazon Resource Name (ARN) or using the
  wildcard (\*) to indicate that the statement applies to all resources.
  For more information, see [Supported resource-level
  permissions for Amazon EC2 API actions](#ec2-supported-iam-actions-resources "#ec2-supported-iam-actions-resources").
- **Condition**: Conditions are optional. They can be
  used to control when your policy is in effect. For more information
  about specifying conditions for Amazon EC2, see [Condition keys for Amazon EC2](#amazon-ec2-keys "#amazon-ec2-keys").

For more information about policy requirements, see the [IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in
the _IAM User Guide_. For example IAM policy statements
for Amazon EC2, see [Example policies to control access the Amazon EC2 API](ExamplePolicies_EC2.md "ExamplePolicies_EC2.md").

## Actions for Amazon EC2

In an IAM policy statement, you can specify any API action from any service
that supports IAM. For Amazon EC2, use the following prefix with the name of the
API action: `ec2:`. For example: `ec2:RunInstances` and
`ec2:CreateImage`.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": ["ec2:*action1*", "ec2:*action2*"]
```

You can also specify multiple actions using wildcards. For example, you can
specify all actions whose name begins with the word "Describe" as
follows:

```
"Action": "ec2:Describe*"
```

###### Note

Currently, the Amazon EC2 Describe\* API actions do not support resource-level
permissions. For more information about resource-level permissions for Amazon EC2, see
[Identity-based policies for Amazon EC2](iam-policies-for-amazon-ec2.md "iam-policies-for-amazon-ec2.md").

To specify all Amazon EC2 API actions, use the \* wildcard as follows:

```
"Action": "ec2:*"
```

For a list of Amazon EC2 actions, see [Actions defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions") in the
_Service Authorization Reference_.

## Supported resource-level

permissions for Amazon EC2 API actions

_Resource-level permissions_ refers to the ability to
specify which resources users are allowed to perform actions on. Amazon EC2 has
partial support for resource-level permissions. This means that for certain
Amazon EC2 actions, you can control when users are allowed to use those actions based
on conditions that have to be fulfilled, or specific resources that users are
allowed to use. For example, you can grant users permissions to launch
instances, but only of a specific type, and only using a specific AMI.

To specify a resource in an IAM policy statement, use its Amazon Resource
Name (ARN). For more information about specifying the ARN value, see [Amazon Resource Names (ARNs) for Amazon EC2](#EC2_ARN_Format "#EC2_ARN_Format"). If an API action
does not support individual ARNs, you must use a wildcard (\*) to specify that
all resources can be affected by the action.

To see tables that identify which Amazon EC2 API actions support resource-level
permissions, and the ARNs and condition keys that you can use in a policy, see
[Actions, resources, and condition keys for
Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md").

Keep in mind that you can apply tag-based resource-level permissions in the
IAM policies you use for Amazon EC2 API actions. This gives you better control over
which resources a user can create, modify, or use. For more information, see
[Grant permission to tag Amazon EC2 resources during creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md").

## Amazon Resource Names (ARNs) for Amazon EC2

Each IAM policy statement applies to the resources that you specify using
their ARNs.

An ARN has the following general syntax:

```
arn:aws:[*service*]:[*region*]:[*account-id*]:*resourceType*/*resourcePath*
```

_service_

The service (for example, `ec2`).

_region_

The Region for the resource (for example,
`us-east-1`).

_account-id_

The AWS account ID, with no hyphens (for example,
`123456789012`).

_resourceType_

The type of resource (for example, `instance`).

_resourcePath_

A path that identifies the resource. You can use the \* wildcard in
your paths.

For example, you can indicate a specific instance
(`i-1234567890abcdef0`) in your statement using its ARN as
follows.

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
```

You can specify all instances that belong to a specific account by using the \*
wildcard as follows.

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*"
```

You can also specify all Amazon EC2 resources that belong to a specific account by
using the \* wildcard as follows.

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:*"
```

To specify all resources, or if a specific API action does not support ARNs,
use the \* wildcard in the `Resource` element as follows.

```
"Resource": "*"
```

Many Amazon EC2 API actions involve multiple resources. For example, `AttachVolume`
attaches an Amazon EBS volume to an instance, so a user must have permissions to use
the volume and the instance. To specify multiple resources in a single
statement, separate their ARNs with commas, as follows.

```
"Resource": ["`arn1`", "`arn2`"]
```

For a list of ARNs for Amazon EC2 resources, see [Resource types defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies").

## Condition keys for Amazon EC2

In a policy statement, you can optionally specify conditions that control when
it is in effect. Each condition contains one or more key-value pairs. Condition
keys are not case-sensitive. We've defined AWS global condition keys, plus
additional service-specific condition keys.

For a list of service-specific condition keys for Amazon EC2, see [Condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-policy-keys "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-policy-keys"). Amazon EC2 also implements the AWS global
condition keys. For more information, see [Information available in all requests](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infoallreqs "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infoallreqs") in the
_IAM User Guide_.

All Amazon EC2 actions support the `aws:RequestedRegion` and
`ec2:Region` condition keys. For more information, see [Example: Restrict access to a specific Region](ExamplePolicies_EC2.md#iam-example-region "ExamplePolicies_EC2.md#iam-example-region").

To use a condition key in your IAM policy, use the `Condition`
statement. For example, the following policy grants users permission to add and
remove inbound and outbound rules for any security group. It uses the
`ec2:Vpc` condition key to specify that these actions can only be
performed on security groups in a specific VPC.

JSON

```
`{
"Version":"2012-10-17",
 "Statement":[{
 "Effect":"Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:RevokeSecurityGroupEgress"],
 "Resource": "arn:aws:ec2:us-east-1:111122223333:security-group/*",
 "Condition": {
 "StringEquals": {
 "ec2:Vpc": "arn:aws:ec2:us-east-1:111122223333:vpc/vpc-11223344556677889"
 }
 }
 }
 ]
}`

```

If you specify multiple conditions, or multiple keys in a single condition, we
evaluate them using a logical AND operation. If you specify a single condition
with multiple values for one key, we evaluate the condition using a logical OR
operation. For permissions to be granted, all conditions must be met.

You can also use placeholders when you specify conditions. For more information, see
[IAM policy elements:
Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the
_IAM User Guide_.

###### Important

Many condition keys are specific to a resource, and some API actions use
multiple resources. If you write a policy with a condition key, use the
`Resource` element of the statement to specify the resource
to which the condition key applies. If not, the policy may prevent users
from performing the action at all, because the condition check fails for the
resources to which the condition key does not apply. If you do not want to
specify a resource, or if you've written the `Action` element of
your policy to include multiple API actions, then you must use the
`...IfExists` condition type to ensure that the condition key
is ignored for resources that do not use it. For more information, see
[...IfExists Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IfExists "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IfExists") in the
_IAM User Guide_.

###### Condition keys

- [ec2:Attribute condition key](#attribute-key "#attribute-key")
- [ec2:ResourceID condition keys](#imageId-key "#imageId-key")
- [ec2:SourceInstanceARN condition key](#SourceInstanceARN "#SourceInstanceARN")

### ec2:Attribute condition key

The `ec2:Attribute` condition key can be used for conditions that filter access
by an attribute of a resource.

This condition key supports only properties that are of a primitive data type (such as
strings or integers), or complex **[AttributeValue](../APIReference/API_AttributeValue.md "../APIReference/API_AttributeValue.md")**
objects that contain only a **Value** property (such as the
**Description** or **ImdsSupport**
objects of the [ModifyImageAttribute](../APIReference/API_ModifyImageAttribute.md "../APIReference/API_ModifyImageAttribute.md") API action). The condition key can't be used with
complex objects that contain multiple properties, such as the
**LaunchPermission** object of [ModifyImageAttribute](../APIReference/API_ModifyImageAttribute.md "../APIReference/API_ModifyImageAttribute.md").

For example, the following policy uses the `ec2:Attribute/Description` condition
key to filter access by the complex **Description** object of
the **ModifyImageAttribute** API action. The condition key allows
only requests that modify an image's description to either `Production` or
`Development`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:ModifyImageAttribute",
 "Resource": "arn:aws:ec2:`us-east-1`::image/ami-*",
 "Condition": {
 "StringEquals": {
 "ec2:Attribute/Description": [
 "Production",
 "Development"
 ]
 }
 }
 }
 ]
}`

```

The following example policy uses the `ec2:Attribute` condition key to filter access
by the primitive **Attribute** property of the **ModifyImageAttribute** API action. The condition key denies all requests that attempt
to modify an image's description.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ec2:ModifyImageAttribute",
 "Resource": "arn:aws:ec2:`us-east-1`::image/ami-*",
 "Condition": {
 "StringEquals": {
 "ec2:Attribute": "Description"
 }
 }
 }
 ]
}`

```

### ec2:ResourceID condition keys

When using the following `ec2:`Resource`ID` condition
keys with the specified API actions, the condition key value is used to specify the resulting
resource that is created by the API action. `ec2:`Resource`ID`
condition keys can't be used to specify a source resource that is specified in the API request.
If you use one of the following `ec2:`Resource`ID` condition
keys with a specified API, then you must always specify the wildcard (`*`). If you
specify a different value, the condition always resolves to `*` during runtime. For
example, to use the `ec2:ImageId` condition key with the
**CopyImage** API, then you must specify the condition key as
follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:CopyImage",
 "Resource": "arn:aws:ec2:`us-east-1`::image/ami-*",
 "Condition": {
 "StringEquals": {
 "ec2:ImageID": "*"
 }
 }
 }
 ]
}`

```

We recommend that you avoid using these condition keys with these API actions:

- `ec2:DhcpOptionsID` – `CreateDhcpOptions`
- `ec2:ImageID` – `CopyImage`, `CreateImage`,
  `ImportImage`, and `RegisterImage`
- `ec2:InstanceID` – `RunInstances` and `ImportInstance`
- `ec2:InternetGatewayID` – `CreateInternetGateway`
- `ec2:NetworkAclID` – `CreateNetworkAcl`
- `ec2:NetworkInterfaceID` – `CreateNetworkInterface`
- `ec2:PlacementGroupName` – `CreatePlacementGroup`
- `ec2:RouteTableID` – `CreateRouteTable`
- `ec2:SecurityGroupID` – `CreateSecurityGroup`
- `ec2:SnapshotID` – `CopySnapshot`, `CreateSnapshot`,
  `CreateSnapshots`, and `ImportSnapshots`
- `ec2:SubnetID` – `CreateSubnet`
- `ec2:VolumeID` – `CreateVolume` and `ImportVolume`
- `ec2:VpcID` – `CreateVpc`
- `ec2:VpcPeeringConnectionID` – `CreateVpcPeeringConnection`

To filter access based on specific resource IDs, we recommend that you use the
`Resource` policy element as follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:CopyImage",
 "Resource": "arn:aws:ec2:`us-east-1`::image/ami-01234567890abcdef"
 }
 ]
}`

```

### ec2:SourceInstanceARN condition key

Use `ec2:SourceInstanceARN` to specify the ARN
of the instance from which a request is made. This is an
[AWS global condition key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md"), which means that you
can use it with services other than Amazon EC2. For a policy example,
see [Example: Allow a specific instance to view
resources in other AWS services](ExamplePolicies_EC2.md#iam-example-source-instance "ExamplePolicies_EC2.md#iam-example-source-instance").

## Control access using attribute-based access

When you create an IAM policy that grants users permission to use EC2 resources, you can
include tag information in the `Condition` element of the policy to
control access based on tags. This is known as attribute-based access control
(ABAC). ABAC provides better control over which resources a user can modify, use, or
delete. For more information, see [What is
ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")

For example, you can create a policy that allows users to terminate an instance,
but denies the action if the instance has the tag
`environment=production`. To do this, you use the
`aws:ResourceTag` condition key to allow or deny access to the
resource based on the tags that are attached to the resource.

```
"StringEquals": { "aws:ResourceTag/environment": "production" }
```

To learn whether an Amazon EC2 API action supports controlling access using the
`aws:ResourceTag` condition key, see [Actions,
resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md"). Note that the
`Describe` actions do not support resource-level permissions, so you
must specify them in a separate statement without conditions.

For example IAM policies, see [Example policies to control access the Amazon EC2 API](ExamplePolicies_EC2.md "ExamplePolicies_EC2.md").

If you allow or deny users access to resources based on tags, you must consider
explicitly denying users the ability to add those tags to or remove them from the
same resources. Otherwise, it's possible for a user to circumvent your restrictions
and gain access to a resource by modifying its tags.

## Grant permissions to users, groups, and roles

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Check that users have the required

permissions

After you've created an IAM policy, we recommend that you check whether it
grants users the permissions to use the particular API actions and resources
they need before you put the policy into production.

First, create a user for testing purposes, and then attach the IAM policy that you
created to the test user. Then, make a request as the test user.

If the Amazon EC2 action that you are testing creates or modifies a resource, you
should make the request using the `DryRun` parameter (or run the
AWS CLI command with the `--dry-run` option). In this case, the call
completes the authorization check, but does not complete the operation. For
example, you can check whether the user can terminate a particular instance
without actually terminating it. If the test user has the required permissions,
the request returns `DryRunOperation`; otherwise, it returns
`UnauthorizedOperation`.

If the policy doesn't grant the user the permissions that you expected, or is
overly permissive, you can adjust the policy as needed and retest until you get
the desired results.

###### Important

It can take several minutes for policy changes to propagate before they
take effect. Therefore, we recommend that you allow five minutes to pass
before you test your policy updates.

If an authorization check fails, the request returns an encoded message with
diagnostic information. You can decode the message using the
`DecodeAuthorizationMessage` action. For more information, see
[DecodeAuthorizationMessage](../../../STS/latest/APIReference/API_DecodeAuthorizationMessage.md "../../../STS/latest/APIReference/API_DecodeAuthorizationMessage.md") in the
_AWS Security Token Service API Reference_, and [decode-authorization-message](../../../cli/latest/reference/sts/decode-authorization-message.md "../../../cli/latest/reference/sts/decode-authorization-message.md").
