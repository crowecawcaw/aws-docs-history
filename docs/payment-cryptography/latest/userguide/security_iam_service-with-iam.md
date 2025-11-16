# How AWS Payment Cryptography works with IAM

Before you use IAM to manage access to AWS Payment Cryptography, you should understand what IAM
features are available to use with AWS Payment Cryptography. To get a high-level view of how AWS Payment Cryptography and
other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [AWS Payment Cryptography
  Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Authorization based on AWS Payment Cryptography
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")

## AWS Payment Cryptography

Identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. AWS Payment Cryptography
supports specific actions, resources, and condition keys. To learn about all of the
elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Payment Cryptography use the following prefix before the action:
`payment-cryptography:`. For example, to grant someone permission to execute an
AWS Payment Cryptography `VerifyCardData` API operation, you include the
`payment-cryptography:VerifyCardData` action in their policy. Policy statements
must include either an `Action` or `NotAction` element.
AWS Payment Cryptography defines its own set of actions that describe tasks that you can perform
with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "payment-cryptography*:action1*",
      "payment-cryptography*:action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `List` (such as `ListKeys` and
`ListAliases`), include the following action:

```
`"Action": "payment-cryptography:List*"`
```

To see a list of AWS Payment Cryptography actions, see [Actions Defined by AWS Payment Cryptography](../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#awskeymanagementservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#awskeymanagementservice-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The payment-cryptography key resource has the following ARN:

```
arn:${Partition}:payment-cryptography:${Region}:${Account}:key/${keyARN}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h` instance in your
statement, use the following ARN:

```
"Resource": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h"
```

To specify all keys that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:payment-cryptography:us-east-2:111122223333:key/*"
```

Some AWS Payment Cryptography actions, such as those for creating keys, cannot be performed on a
specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

To specify multiple resources in a single statement, use a comma as shown
below:

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

### Examples

To view examples of AWS Payment Cryptography identity-based policies, see [AWS Payment Cryptography identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authorization based on AWS Payment Cryptography

tags

You can attach tags to AWS Payment Cryptography resources or pass tags in a request to
AWS Payment Cryptography. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`payment-cryptography:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys.
