End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Troubleshooting AWS IoT Analytics identity and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with AWS IoT Analytics.

###### Topics

- [I am not authorized to perform an action in AWS IoT Analytics](#iam-no-permission "#iam-no-permission")
- [I am not authorized to perform iam:PassRole](#iam-passrole "#iam-passrole")
- [I want to allow people outside of my AWS account
  to access my AWS IoT Analytics resources](#iam-cross-account-access "#iam-cross-account-access")

## I am not authorized to perform an action in AWS IoT Analytics

If the AWS Management Console tells you that you're not authorized to perform an action,
the you must contact your administrator for assistance. You administrator is the person that
provided you with your user name and password.

The following example error occurs when the `mateojackson` user tries to
use the console to view details about a `channel` but not have
`iotanalytics:ListChannels` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: iotanalytics:``ListChannels`` on resource: ``my-example-channel``
```

In this case, Mateo asks his administrator update his policies to allow him to access the
`my-example-channel` resource using the `iotanalytics:ListChannel`
action.

## I am not authorized to perform `iam:PassRole`

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to AWS IoT Analytics.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
AWS IoT Analytics. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people outside of my AWS account

to access my AWS IoT Analytics resources

You can create a role that users in other accounts or people outside of your organization
can use to access your resources. You can specify who is trusted to assume the role. For
services that support resource-based policies or access control lists (ACL), you can use those
policies to grant people access to your resources.

To learn more, consult the following:

- To learn whether AWS IoT Analytics supports these features, see [How AWS IoT Analytics works with
  IAM](security.md#security-iam-service-with-iam "security.md#security-iam-service-with-iam").
- To learn how to provide access to your resources across AWS accounts that you own, see
  [Providing access to
  an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the
  _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see
  [Providing access to
  AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to
  externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for
  cross-account access, see [How IAM roles differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the
  _IAM User Guide_.
