Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# How Amazon Fraud Detector works with

IAM

Before you use IAM to manage access to Amazon Fraud Detector, you should understand what
IAM features are available to use with Amazon Fraud Detector. To get a high-level view of how
Amazon Fraud Detector and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon Fraud Detector
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon Fraud Detector
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization Based on
  Amazon Fraud Detector Tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon Fraud Detector IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon Fraud Detector

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon Fraud Detector supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

To get started with Amazon Fraud Detector, we recommend creating an user with access restricted to Amazon Fraud Detector operations and required permissions.
You can add other permissions as needed. The following policies provide the required permission to use Amazon Fraud Detector: `AmazonFraudDetectorFullAccessPolicy` and `AmazonS3FullAccess`.
For more information on setting up Amazon Fraud Detector using these policies see [Set up for Amazon Fraud Detector](set-up.md "set-up.md").

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Fraud Detector use the following prefix before the action:
`frauddetector:`. For example, to create a rule with the Amazon Fraud Detector `CreateRule` API operation, you include the `frauddetector:CreateRule` action in the policy. Policy statements must
include either an `Action` or `NotAction` element.
Amazon Fraud Detector defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "frauddetector:*action1*",
      "frauddetector:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "frauddetector:Describe*"`
```

To see a list of Amazon Fraud Detector actions, see [Actions Defined by Amazon Fraud Detector](../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

[Resource Types Defined by Amazon Fraud Detector](../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-resources-for-iam-policies") lists all Amazon Fraud Detector resource ARNs.

For example, to specify the `my_detector` detector in your statement, use the following ARN:

```
"Resource": "arn:aws:frauddetector:us-east-1:123456789012:detector/my_detector"
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

To specify all detectors that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:frauddetector:us-east-1:123456789012:detector/*"
```

Some Amazon Fraud Detector actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

To see a list of Amazon Fraud Detector resource types and their ARNs, see
[Resources Defined by Amazon Fraud Detector](../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-resources-for-iam-policies") in the _IAM User Guide_. To learn
which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon Fraud Detector](../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon Fraud Detector defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

To see a list of Amazon Fraud Detector condition keys, see [Condition Keys for Amazon Fraud Detector](../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-policy-keys "../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-policy-keys")
in the _IAM User Guide_. To learn which actions and
resources you can use a condition key, see [Actions Defined by Amazon Fraud Detector](../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonfrauddetector.md#amazonfrauddetector-actions-as-permissions").

### Examples

To view examples of Amazon Fraud Detector identity-based policies, see [Amazon Fraud Detector identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon Fraud Detector

resource-based policies

Amazon Fraud Detector does not support resource-based policies.

## Authorization Based on

Amazon Fraud Detector Tags

You can attach tags to Amazon Fraud Detector resources or pass tags in a request to
Amazon Fraud Detector. To control access based on tags, you provide tag information in
the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`aws:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys.

## Amazon Fraud Detector IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary credentials with Amazon Fraud Detector

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Fraud Detector supports using temporary credentials.

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Amazon Fraud Detector does not support service-linked roles.

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
account and are owned by the account. This means that an administrator can change
the permissions for this role. However, doing so might break the functionality of the
service.

Amazon Fraud Detector supports service roles.
