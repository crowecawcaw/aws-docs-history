# Policy

resources for WorkSpaces Secure Browser

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of WorkSpaces Secure Browser resource types and their ARNs, see
[Resources defined by Amazon WorkSpaces Secure Browser](../../../service-authorization/latest/reference/list_amazonworkspacesweb.md#amazonworkspacesweb-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonworkspacesweb.md#amazonworkspacesweb-resources-for-iam-policies") in the _Service Authorization Reference_. To learn with
which actions you can specify the ARN of each resource, see
[Actions defined by Amazon WorkSpaces Secure Browser](../../../service-authorization/latest/reference/list_amazonworkspacesweb.md#amazonworkspacesweb-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonworkspacesweb.md#amazonworkspacesweb-actions-as-permissions").

To view examples of WorkSpaces Secure Browser identity-based policies, see [Identity-based policy
examples for Amazon WorkSpaces Secure Browser](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
