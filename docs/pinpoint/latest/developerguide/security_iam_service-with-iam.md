**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# How Amazon Pinpoint works with IAM

To use Amazon Pinpoint, users in your AWS account require permissions that allow them to view
analytics data, create projects, define user segments, deploy campaigns, and more. If you
integrate a mobile or web app with Amazon Pinpoint, users of your app also require access to Amazon Pinpoint. This
access enables your app to register endpoints and report usage data to Amazon Pinpoint. To grant access to
Amazon Pinpoint features, create AWS Identity and Access Management (IAM) policies that allow Amazon Pinpoint actions for IAM identities
or Amazon Pinpoint resources.

IAM is a service that helps administrators securely control access to AWS resources. IAM
policies include statements that allow or deny specific actions by specific users or for
specific resources. Amazon Pinpoint provides a [set of actions](permissions-actions.md "permissions-actions.md")
that you can use in IAM policies to specify granular permissions for Amazon Pinpoint users and
resources. This means that you can grant the appropriate level of access to Amazon Pinpoint without
creating overly permissive policies that might expose important data or compromise your
resources. For example, you can grant unrestricted access to an Amazon Pinpoint administrator, and grant
read-only access to individuals who need access to only a specific project.

Before you use IAM to manage access to Amazon Pinpoint, you should understand what
IAM features are available for use with Amazon Pinpoint. To get a high-level view of how
Amazon Pinpoint and other AWS services work with IAM, see [AWS services that work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon Pinpoint
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon Pinpoint
  resource-based permissions policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on Amazon Pinpoint
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon Pinpoint IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon Pinpoint

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon Pinpoint supports specific actions, resources, and condition keys. To learn about all
the elements that you can use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

This means that policy actions control what users can do on the Amazon Pinpoint console. They also
control what users can do programmatically by using the AWS SDKs, the AWS Command Line Interface (AWS CLI),
or the Amazon Pinpoint APIs directly.

Policy actions in Amazon Pinpoint use the following prefixes:

- **`mobiletargeting`** – For
  actions that derive from the Amazon Pinpoint API, which is the primary API for Amazon Pinpoint.
- **`sms-voice`** – For actions that
  derive from the Amazon Pinpoint SMS and Voice API, which is a supplemental API that provides advanced
  options for using and managing the SMS and voice channels in Amazon Pinpoint.

For example, to grant someone permission to view information about all the segments for
a project, which is an action that corresponds to the `GetSegments` operation in
the Amazon Pinpoint API, include the `mobiletargeting:GetSegments` action in their policy.
Policy statements must include either an `Action` or `NotAction`
element. Amazon Pinpoint defines its own set of actions that describe the tasks that users
can perform with it.

To specify multiple actions in a single statement, separate them with commas:

```
"Action": [
      "mobiletargeting:*action1*",
      "mobiletargeting:*action2*"
```

You can also specify multiple actions by using wildcards (\*). For example, to specify
all actions that begin with the word `Get`, include the following action:

```
`"Action": "mobiletargeting:Get*"`
```

However, as a best practice, you should create policies that follow the principle of
_least privilege_. In other words, you should create
policies that include only the permissions that are required to perform a specific
action.

For a list of Amazon Pinpoint actions that you can use in IAM policies, see [Amazon Pinpoint actions for IAM policies](permissions-actions.md "permissions-actions.md").

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For example, the `mobiletargeting:GetSegments` action retrieves information
about all the segments that are associated with a specific Amazon Pinpoint project. You identify a
project with an ARN in the following format:

```
arn:aws:mobiletargeting:${Region}:${Account}:apps/${projectId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md")
in the _AWS General Reference_.

In IAM policies, you can specify ARNs for the following types of Amazon Pinpoint
resources:

- Campaigns
- Journeys
- Message templates (referred to as _templates_ in
  some contexts)
- Projects (referred to as _apps_ or _applications_ in some contexts)
- Recommender models (referred to as _recommenders_
  in some contexts)
- Segments

For example, to create a policy statement for the project that has the project ID
`810c7aab86d42fb2b56c8c966example`, use the following ARN:

```
"Resource": "arn:aws:mobiletargeting:us-east-1:123456789012:apps/810c7aab86d42fb2b56c8c966example"
```

To specify all the projects that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:mobiletargeting:us-east-1:123456789012:apps/*"
```

Some Amazon Pinpoint actions, such as certain actions for creating resources, can't be
performed on a specific resource. In those cases, you must use the wildcard (\*):

```
"Resource": "*"
```

In IAM policies, you can also specify ARNs for the following types of Amazon Pinpoint SMS and
Voice resources:

- Configuration Set
- Opt Out List
- Phone Number
- Pool
- Sender Id

For example, to create a policy statement for a phone number that has the phone
number ID `phone-12345678901234567890123456789012` use the following ARN:

```
"Resource": "arn:aws:sms-voice:us-east-1:123456789012:phone-number/phone-12345678901234567890123456789012"
```

To specify all phone numbers that belong to a specific account, use a wildcard (\*) in
place of the phone number ID:

```
"Resource": "arn:aws:sms-voice:us-east-1:123456789012:phone-number/*"
```

Some Amazon Pinpoint SMS and Voice actions are not performed on a specific resource,
such as those for managing account-level settings like spend limits. In those cases, you
must use the wildcard (\*):

```
"Resource": "*"
```

Some Amazon Pinpoint API actions involve multiple resources. For example, the
`TagResource` action can add a tag to multiple projects. To specify multiple
resources in a single statement, separate the ARNs with commas:

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Amazon Pinpoint resource types and their ARNs, see
[Resources Defined by Amazon Pinpoint](../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-resources-for-iam-policies") in the _IAM User Guide_. To learn which
actions you can specify with the ARN of each resource type, see [Actions Defined by Amazon Pinpoint](../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-actions-as-permissions") in
the _IAM User Guide_.

### Condition

keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon Pinpoint defines its own set of condition keys and also supports some global
condition keys. To see a list of all AWS global condition keys, see [AWS global condition context
keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_. To see a list of
Amazon Pinpoint condition keys, see [Condition Keys for Amazon Pinpoint](../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-policy-keys "../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-policy-keys") in the
_IAM User Guide_. To learn which actions and resources you can use a
condition key with, see [Actions Defined by Amazon Pinpoint](../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonpinpoint.md#amazonpinpoint-actions-as-permissions") in the
_IAM User Guide_.

### Examples

To view examples of Amazon Pinpoint identity-based policies, see [Amazon Pinpoint identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon Pinpoint

resource-based permissions policies

Resource-based permission policies are JSON policy documents that specify what actions a
specified principal can perform on an Amazon Pinpoint resource and under what conditions.
Amazon Pinpoint supports resource-based permissions policies for campaigns, journeys, message templates
(_templates_), recommender models (_recommenders_), projects (_apps_), and segments.

### Examples

To view examples of Amazon Pinpoint resource-based policies, see [Amazon Pinpoint identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authorization based on Amazon Pinpoint

tags

You can associate tags with certain types of Amazon Pinpoint resources or pass tags in a
request to Amazon Pinpoint. To control access based on tags, you provide tag information in
the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/${TagKey}`,
`aws:RequestTag/${TagKey}`, or `aws:TagKeys` condition keys.

For information about tagging Amazon Pinpoint resources, including an example IAM policy, see
[Manage Amazon Pinpoint resource tags](tagging-resources.md "tagging-resources.md").

## Amazon Pinpoint IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your
AWS account that has specific permissions.

### Using temporary credentials

with Amazon Pinpoint

You can use temporary credentials to sign in with federation, assume an IAM role, or
assume a cross-account role. You obtain temporary security credentials by calling AWS Security Token Service
(AWS STS) API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Pinpoint supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other services
to complete an action on your behalf. Service-linked roles appear in your IAM account and
are owned by the service. An IAM administrator can view but not edit the permissions for
service-linked roles.

Amazon Pinpoint doesn't use service-linked roles.

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in other
services to complete an action on your behalf. Service roles appear in your IAM account
and are owned by the account. This means that an IAM administrator can change the
permissions for this role. However, doing so might break the functionality of the
service.

Amazon Pinpoint supports using service roles.
