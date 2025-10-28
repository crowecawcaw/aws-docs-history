# Using tags in IAM permission policies

[AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md") is the
AWS service that you use to create and manage permissions policies that determine who can
access your AWS resources. Every attempt to access an AWS service or read or write an
AWS resource is access controlled by an IAM policy.

These policies allow you to provide granular access to your resources. One of the features
you can use to fine tune this access is the [`Condition`](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") element of the policy. This element lets you specify
the conditions that must match the request to determine if the request can proceed. Among
the things you can check with the `Condition` element are the following:

- Tags that are attached to the user or role making the request.
- Tags attached to the resource that is the object of the request.

## Tags and attribute-based access control

Tags can be an important part of your AWS access control strategy. For information
about using tags as the attributes in an attribute-based access control (ABAC) strategy,
see [Controlling
access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") and [Controlling access to and for IAM users
and roles using tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md"), both in the
_IAM User Guide_.

There is a comprehensive tutorial that shows how to grant access to different projects
and groups using tags at [IAM tutorial:
Define permissions to access AWS resources based on tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the
_AWS Identity and Access Management User Guide_.

If you use a SAML-based identity provider (IdP) for single sign-in, you can attach
tags to the assumed roles providing access to your users. For more information, see
[IAM
tutorial: Use SAML session tags for ABAC](../../../IAM/latest/UserGuide/tutorial_abac-saml.md "../../../IAM/latest/UserGuide/tutorial_abac-saml.md") in the _AWS Identity and Access Management User
Guide_.

## Tag-related condition keys

The following table describes the condition keys that you can use in an IAM
permissions policy to control access based on tags. These condition keys let you do the
following:

- Compare the tags on the principal calling the operation.
- Compare the tags provided to the operation as a parameter.
- Compare the tags attached to the resource that would be accessed by the
  operation.

For complete details about a condition key and how to use it, see the page linked in
the **Condition key name** column.

| Condition key name                                                                                                                                                                                                  | Description                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [aws:PrincipalTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltag") | Compares the tag attached to the principal (IAM role or user) making the request with the tag that you specify in the policy.             |
| [aws:RequestTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag")       | Compares the tag key-value pair that was passed to the request as a parameter with the tag key-value pair that you specify in the policy. |
| [aws:ResourceTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag")    | Compares the key-value pair that is attached to the resource with the tag key-value pair that you specify in the policy.                  |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                | Compares only the tag _keys_ in the request with the keys that you specify in the policy.                                                 | ## Example IAM policies that use tags ###### Example 1: Force users to attach a specific tag when they create a resource The following example IAM permissions policy shows how to force the user who creates or modifies an IAM policy's tags to include a tag with the key `Owner`. Also, the policy requires that the value of the tag is set to the same value as the `Owner` tag currently attached to the calling principal. For this strategy to work, all principals must have an `Owner` tag attached, and users must be prevented from modifying that tag. If an attempt to create or modify a policy occurs without including the `Owner` tag, the policy doesn't match and the operation isn't allowed. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "TagCustomerManagedPolicies", "Effect": "Allow", "Action": [ "iam:CreatePolicy", "iam:TagPolicy" ], "Resource": "arn:aws:iam::123456789012:policy/*", "Condition": { "StringEquals": {"aws:RequestTag/Owner": "${aws:PrincipalTag/Owner}"} } } ] }` `` ###### Example 2: Use tags to limit access to a resource to its "owner" The following example IAM permissions policy lets the user stop a running Amazon EC2 instance only if the calling principal is tagged with the same `project` tag value as the instance. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "VisualEditor1", "Effect": "Allow", "Action": [ "ec2:StopInstances" ], "Resource": [ "arn:aws:iam::123456789012:instance/*" ], "Condition": { "StringEquals": {"aws:ResourceTag/project": "${aws:PrincipalTag/project}"} } } ] }` `` This example is an example of [attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"). For more information and additional examples of using IAM policies to implement a tag-based access control strategy, see the following topics in the _AWS Identity and Access Management User Guide_: <br>• [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") <br>• [Controlling access to and for IAM users and roles using tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md") <br>• [IAM tutorial: Define permissions to access AWS resources based on tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") – Shows how to grant access to different projects and groups using multiple tags. |
