# Troubleshooting AWS Security Agent identity and access

Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Security Agent and IAM.

## AccessDeniedException

If you receive an `AccessDeniedException` when calling an AWS API operation, then the IAM principal credentials that you’re using don’t have the required permissions to make that call.

```
 An error occurred (AccessDeniedException) when calling the CreateEnvironment operation:
User: arn:aws:iam::111122223333:user/user_name is not authorized to perform:
securityagent:CreateEnvironment on resource: arn:aws:securityagent:region:111122223333:environment/my-env
```

In the previous example message, the user does not have permissions to call the AWS Security Agent `CreateEnvironment` API operation. To provide AWS Security Agent admin permissions to an IAM principal, see [AWS Security Agent identity-based policy examples](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

For more general information about IAM, see [Control access to AWS resources using policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in the _IAM User Guide_.

## I want to allow people outside of my AWS account to access my AWS Security Agent resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:

- To learn whether AWS Security Agent supports these features, see [How AWS Security Agent works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing Access to Externally Authenticated Users (Identity Federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the _IAM User Guide_.
