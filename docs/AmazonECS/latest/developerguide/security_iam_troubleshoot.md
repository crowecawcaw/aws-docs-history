

# Troubleshooting Amazon Elastic Container Service identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon ECS and IAM.

**Topics**
+ [I am not authorized to perform an action in Amazon ECS](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I want to allow people outside of my AWS account to access my Amazon ECS resources](#security_iam_troubleshoot-cross-account-access)
+ [I am having issues with my Amazon ECS Managed Instances instance profile](#security_iam_instance-profile)
+ [Additional troubleshooting resources](#security_iam_troubleshoot-additional-errors)

## I am not authorized to perform an action in Amazon ECS
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but doesn't have the fictional `ecs:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: ecs:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the `{{my-example-widget}}` resource by using the `ecs:{{GetWidget}}` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Amazon ECS.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Amazon ECS. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

If you use Amazon ECS Managed Instances and receive this error, your instance role name might not match the naming convention required by the managed policy. For more information, see [I am having issues with my Amazon ECS Managed Instances instance profile](#security_iam_instance-profile).

## I want to allow people outside of my AWS account to access my Amazon ECS resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Amazon ECS supports these features, see [How Amazon Elastic Container Service works with IAM](security_iam_service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## I am having issues with my Amazon ECS Managed Instances instance profile
<a name="security_iam_instance-profile"></a>

If you use the `AmazonECSInfrastructureRolePolicyForManagedInstances` managed policy, the instance role name must start with `ecsInstanceRole`. The policy scopes `iam:PassRole` to `arn:aws:iam::*:role/ecsInstanceRole*`, so a mismatched name causes an authorization error at task launch.

This is common with CloudFormation when you omit `RoleName` from your `AWS::IAM::Role` resource, because CloudFormation auto-generates names like `MyStack-InstanceRole-ABC123` that do not match the policy condition.

To resolve this issue, do one of the following:
+ Add `RoleName: ecsInstanceRole` to your `AWS::IAM::Role` resource so the name matches the managed policy.
+ Add an explicit `iam:PassRole` inline policy to your infrastructure role that targets the instance role ARN.

For CloudFormation templates and detailed steps, see [Create the instance profile using CloudFormation](managed-instances-instance-profile.md#create-instance-profile-cfn).

## Additional troubleshooting resources
<a name="security_iam_troubleshoot-additional-errors"></a>

The following pages provide information about error codes:
+  [Amazon ECS stopped tasks error messages](stopped-task-error-codes.md) 
+  [Viewing Amazon ECS service event messages](service-event-messages.md) 