

# Troubleshooting AWS Resource Explorer permissions
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Resource Explorer and AWS Identity and Access Management (IAM).

**Topics**
+ [I am not authorized to perform an action in Resource Explorer](#security_iam_troubleshoot-no-permissions)
+ [I want to allow people outside of my AWS account to access my Resource Explorer resources](#security_iam_troubleshoot-cross-account-access)

## I am not authorized to perform an action in Resource Explorer
<a name="security_iam_troubleshoot-no-permissions"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with the credentials you used to attempt this operation.

For example, the following error occurs when someone assumes the IAM role `MyExampleRole` tries to use the console to view details about a view but does not have `resource-explorer-2:GetView` permission.

```
User: arn:aws:iam::123456789012:role/MyExampleRole is not authorized to perform: resource-explorer-2:GetView on resource: arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111
```

In this case, the person using the role must ask the administrator to update the role's permission policies to allow access to the view using the `resource-explorer-2:GetView` action.

## I want to allow people outside of my AWS account to access my Resource Explorer resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Resource Explorer supports these features, see [How Resource Explorer works with IAM](security_iam_service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.