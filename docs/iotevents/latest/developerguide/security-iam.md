End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Identity and access management for AWS IoT Events

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use AWS IoT Events resources. IAM is an AWS service that you can use with no
additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](security_iam_authentication.md "security_iam_authentication.md")
- [Managing access using policies](security_iam_access-manage.md "security_iam_access-manage.md")
- [More about identity and access management](#security_iam_learn-more "#security_iam_learn-more")
- [How AWS IoT Events works with IAM](#security_iam_service-with-iam "#security_iam_service-with-iam")
- [AWS IoT Events identity-based policy
  examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Cross-service confused deputy
  prevention for AWS IoT Events](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
- [Troubleshoot AWS IoT Events identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshoot AWS IoT Events identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How AWS IoT Events works with IAM](#security_iam_service-with-iam "#security_iam_service-with-iam"))
- **IAM administrator** - write policies to manage
  access (see [AWS IoT Events identity-based policy
  examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"))

## More about identity and access management

For more information about identity and access management for AWS IoT Events, continue to the
following pages:

- [How AWS IoT Events works with IAM](#security_iam_service-with-iam "#security_iam_service-with-iam")
- [Troubleshoot AWS IoT Events identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## How AWS IoT Events works with IAM

Before you use IAM to manage access to AWS IoT Events, you should understand what IAM
features are available to use with AWS IoT Events. To get a high-level view of how AWS IoT Events and other
AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [AWS IoT Events identity-based
  policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [AWS IoT Events
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on AWS IoT Events
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [AWS IoT Events IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

### AWS IoT Events identity-based

policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. AWS IoT Events
supports specific actions, resources, and condition keys. To learn about all of the
elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

#### Actions

The `Action` element of an IAM identity-based policy describes the
specific action or actions that will be allowed or denied by the policy. Policy
actions usually have the same name as the associated AWS API operation. The action
is used in a policy to grant permissions to perform the associated operation.

Policy actions in AWS IoT Events use the following prefix before the action:
`iotevents:`. For example, to grant someone permission to
create an AWS IoT Events input with the AWS IoT Events `CreateInput` API operation, you
include the `iotevents:CreateInput` action in their policy. To grant
someone permission to send an input with the AWS IoT Events `BatchPutMessage` API
operation, you include the `iotevents-data:BatchPutMessage` action in
their policy. Policy statements must include either an `Action` or
`NotAction` element. AWS IoT Events defines its own set of actions that describe
tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "iotevents:*action1*",
      "iotevents:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "iotevents:Describe*"`
```

To see a list of AWS IoT Events actions, see [Actions Defined by AWS IoT Events](../../../IAM/latest/UserGuide/list_awsiotevents.md#awsiotevents-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsiotevents.md#awsiotevents-actions-as-permissions") in the
_IAM User Guide_.

#### Resources

The `Resource` element specifies the object or objects to which the
action applies. Statements must include either a `Resource` or a
`NotResource` element. You specify a resource using an ARN or using the
wildcard (\*) to indicate that the statement applies to all resources.

The AWS IoT Events detector model resource has the following ARN:

```
arn:${Partition}:iotevents:${Region}:${Account}:detectorModel/${detectorModelName}
```

For more information about the format of ARNs, see [Identify AWS resources with
Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md").

For example, to specify the `Foobar` detector model in your statement,
use the following ARN:

```
"Resource": "arn:aws:iotevents:us-east-1:123456789012:detectorModel/Foobar"
```

To specify all instances that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:iotevents:us-east-1:123456789012:detectorModel/*"
```

Some AWS IoT Events actions, such as those for creating resources, cannot be performed on a
specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Some AWS IoT Events API actions involve multiple resources. For example,
`CreateDetectorModel` references inputs in its condition statements, so
a user must have permissions to use the input and the detector model. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of AWS IoT Events resource types and their ARNs, see
[Resources Defined by AWS IoT Events](../../../IAM/latest/UserGuide/list_awsiotevents.md#awsiotevents-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsiotevents.md#awsiotevents-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS IoT Events](../../../IAM/latest/UserGuide/list_awsiotevents.md#awsiotevents-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsiotevents.md#awsiotevents-actions-as-permissions").

#### Condition keys

The `Condition` element (or `Condition`
_block_) lets you specify conditions in which a
statement is in effect. The `Condition` element is optional. You can build
conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request.

If you specify multiple `Condition` elements in a statement, or
multiple keys in a single `Condition` element, AWS evaluates them using
a logical `AND` operation. If you specify multiple values for a single
condition key, AWS evaluates the condition using a logical `OR`
operation. All of the conditions must be met before the statement's permissions are
granted.

You can also use placeholder variables when you specify conditions. For example,
you can grant a user permission to access a resource only if it is tagged with their
user name. For more information, see [IAM policy elements:
Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

AWS IoT Events does not provide any service-specific condition keys, but it does support
using some global condition keys. To see all AWS global condition keys, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_."

#### Examples

To view examples of AWS IoT Events identity-based policies, see [AWS IoT Events identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

### AWS IoT Events

resource-based policies

AWS IoT Events does not support resource-based policies." To view an example of a detailed
resource-based policy page, see [https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md").

### Authorization based on AWS IoT Events

tags

You can attach tags to AWS IoT Events resources or pass tags in a request to AWS IoT Events. To control
access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`iotevents:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging AWS IoT Events
resources, see [Tagging your AWS IoT Events resources](tagging-iotevents.md "tagging-iotevents.md").

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [View AWS IoT Events
inputs based on tags](security_iam_id-based-policy-examples-view-input-tags.md "security_iam_id-based-policy-examples-view-input-tags.md").

### AWS IoT Events IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

#### Using temporary

credentials with AWS IoT Events

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS Security Token Service (AWS STS) API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

AWS IoT Events does not support using temporary credentials.

#### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

AWS IoT Events does not support service-linked roles.

#### Service roles

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts")
on your behalf. This role allows the service to access resources in other services to
complete an action on your behalf. Service roles appear in your IAM account and are
owned by the account. This means that an IAM administrator can change the
permissions for this role. However, doing so might break the functionality of the
service.

AWS IoT Events supports service roles.
