This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Policy

resources for Wickr

**Supports policy resources:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Wickr resource types and their ARNs, see [Resources Defined by AWS Wickr](../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-resources-for-iam-policies")
in the _Service Authorization Reference_. To learn with which actions you can
specify the ARN of each resource, see [Actions Defined by AWS Wickr](../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-actions-as-permissions "../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-actions-as-permissions").

To view examples of Wickr identity-based policies, see [Identity-based policy examples for
AWS Wickr](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
