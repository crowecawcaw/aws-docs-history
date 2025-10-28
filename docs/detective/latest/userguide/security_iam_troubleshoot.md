# Troubleshooting Amazon Detective identity

and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Detective and IAM. If you encounter access denied
issues or similar difficulties when working with AWS Identity and Access Management(IAM), consult the [Troubleshooting IAM](../../../IAM/latest/UserGuide/troubleshoot.md "../../../IAM/latest/UserGuide/troubleshoot.md") topics in the
_IAM User Guide_.

## I am not authorized to

perform an action in Detective

If the AWS Management Console tells you that you're not authorized to perform an action, then you
must contact your administrator for assistance. Your administrator is the person that
provided you with your user name and password.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to accept an invitation to become a member account for a
behavior graph, but does not have `detective:AcceptInvitation`
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: detective:AcceptInvitation on resource: arn:aws:detective:us-east-1:444455556666:graph:567856785678
```

In this case, Mateo asks his administrator to update his policies to allow him to
access the `arn:aws:detective:us-east-1:444455556666:graph:567856785678`
resource using the `detective:AcceptInvitation` action.

## I am not authorized to perform

iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Detective.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
Detective. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people

outside of my AWS account to access my Detective resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether Detective supports these features, see [How Amazon Detective works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.
