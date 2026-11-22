

# Troubleshoot Amazon EVS identity and access

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Elastic VMware Service and IAM. For other problems, see [Troubleshooting](troubleshooting.md).

## I receive an AccessDeniedException
<a name="security-iam-troubleshoot-access-denied"></a>

You receive an error like the following when you call an Amazon EVS API operation.

```text
An error occurred (AccessDeniedException) when calling the CreateEnvironment operation:
User: arn:aws:iam::111122223333:user/user-name is not authorized to perform:
evs:CreateEnvironment on resource: arn:aws:evs:region-code:111122223333:environment/my-env
```

 **Cause**: The IAM principal credentials that you’re using don’t have the required permissions to make that call. In the preceding example message, the IAM user doesn’t have permissions to call the Amazon EVS `CreateEnvironment` API operation.

 **Solution**: Ask your IAM administrator to grant the principal the permissions for the operation. To provide Amazon EVS administrator permissions to an IAM principal, see [Amazon EVS identity-based policy examples](security-iam-id-based-policy-examples.md). For the role that Amazon EVS administrators use, see [Create an IAM role for Amazon EVS administrators](setup-iam-role.md).

For more general information about IAM, see [Control access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html) in the *IAM User Guide*.

## I want to give other accounts access to my Amazon EVS resources
<a name="security-iam-troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources. Amazon EVS does not support resource-based policies or ACLs, so use a role.

To learn more, see the following:
+ To learn whether Amazon EVS supports these features, see [How Amazon EVS works with IAM](security_iam_service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing Access to Externally Authenticated Users (Identity Federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html) in the *IAM User Guide*.