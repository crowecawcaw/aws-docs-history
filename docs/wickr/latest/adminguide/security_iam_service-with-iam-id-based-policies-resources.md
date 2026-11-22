

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Policy resources for Wickr

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Wickr resource types and their ARNs, see [Resources Defined by AWS Wickr](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awswickr.html#awswickr-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by AWS Wickr](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awswickr.html#awswickr-actions-as-permissions).

Wickr supports resource-level permissions for network resources. A network ARN uses the following format:

```
arn:{{partition}}:wickr:{{region}}:{{account-id}}:network/{{network-id}}
```

For example:

```
arn:aws:wickr:us-east-1:123456789012:network/12345678
```

For actions that support resource-level permissions, specify the network ARN in the `Resource` element of your policy. If an action doesn't list the network resource type in [Actions Defined by AWS Wickr](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awswickr.html#awswickr-actions-as-permissions), specify all resources using `"Resource": "*"`.