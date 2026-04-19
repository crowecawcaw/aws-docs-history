# Troubleshooting AWS Interconnect identity and access

Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Interconnect and IAM.

###### Topics

- [I am not authorized to perform an action in AWS Interconnect](#security-iam-troubleshoot-no-permissions "#security-iam-troubleshoot-no-permissions")
- [I am not authorized to perform iam:PassRole](#security-iam-troubleshoot-passrole "#security-iam-troubleshoot-passrole")
- [I want to allow people outside of my AWS account to access my AWS Interconnect resources](#security-iam-troubleshoot-cross-account-access "#security-iam-troubleshoot-cross-account-access")

## I am not authorized to perform an action in AWS Interconnect

If the AWS Management Console tells you that you’re not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your user name and password.

The following example error occurs when the `mateojackson`
IAM user tries to use the console to view details about a Connection but does not have `interconnect:`GetConnection`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: interconnect:GetConnection on resource: mcc-12345678
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `mcc-12345678` resource using the `interconnect:GetConnection` action.

## I am not authorized to perform iam:PassRole

If you receive an error that you’re not authorized to perform the `iam:PassRole` action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your user name and password. Ask that person to update your policies to allow you to pass a role to AWS Interconnect.

Some AWS services allow you to pass an existing role to that service, instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in AWS Interconnect. However, the action requires the service to have permissions granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary asks her administrator to update her policies to allow her to perform the `iam:PassRole` action.

## I want to allow people outside of my AWS account to access my AWS Interconnect resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:

- To learn whether AWS Interconnect supports these features, see [How AWS Interconnect works with IAM](security-iam-service-with-iam.md "security-iam-service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing Access to Externally Authenticated Users (Identity Federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the _IAM User Guide_.
