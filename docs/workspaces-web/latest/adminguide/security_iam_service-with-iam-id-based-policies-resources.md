

# Policy resources for WorkSpaces Secure Browser
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of WorkSpaces Secure Browser resource types and their ARNs, see [Resources defined by Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesweb.html#amazonworkspacesweb-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesweb.html#amazonworkspacesweb-actions-as-permissions).





To view examples of WorkSpaces Secure Browser identity-based policies, see [Identity-based policy examples for Amazon WorkSpaces Secure Browser](security_iam_id-based-policy-examples.md).