

# Troubleshooting AWS Account Management identity and access
<a name="security_iam_troubleshoot"></a>

This information is most relevant for AWS accounts that you create when you use our advanced AWS experience. To learn about how access control works for our new AWS experience, see [Compare access management](sign-up-for-aws.md#compare-access-management).

Use the following information to help you diagnose and fix common issues that you might encounter when working with Account Management and IAM.

**Topics**
+ [I am not authorized to perform an action in the Account page](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform `iam:PassRole`](#security_iam_troubleshoot-passrole)
+ [I want to allow people outside of my AWS account to access my account details](#security_iam_troubleshoot-cross-account-access)

## I am not authorized to perform an action in the Account page
<a name="security_iam_troubleshoot-no-permissions"></a>

If the AWS Management Console tells you that you are not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your user name and password.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about his AWS account in the **Account** page of the AWS Management Console but doesn't have the `account:GetAccountInformation` permissions.

![Error message states "You don't have permission to access billing information for this account." You don't have permission to access billing information for this account. Contact your AWS administrator if you need help. If you are an AWS administrator, you can provide permissions for your users or groups by making sure that (1) this account allows IAM and federated users to access billing information and (2) you have the required IAM permissions](http://docs.aws.amazon.com/accounts/latest/reference/images/AccessError.png)


In this case, Mateo asks his administrator to update his policies to allow him to access the `{{my-example-widget}}` resource using the `account:{{GetWidget}}` action.

## I am not authorized to perform `iam:PassRole`
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Account Management.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Account Management. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people outside of my AWS account to access my account details
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Account Management supports these features, see [How AWS Account Management works with IAM](security_iam_service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.