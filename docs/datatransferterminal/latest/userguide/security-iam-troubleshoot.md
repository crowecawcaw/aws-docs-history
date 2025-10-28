# Troubleshooting AWS Data Transfer Terminal identity and access

Use the following information to help you diagnose and fix common issues that you might encounter when working with Data Transfer Terminal and IAM.

###### Topics

- [I am not authorized to perform an action in Data Transfer Terminal](#security-iam-troubleshoot-no-permissions "#security-iam-troubleshoot-no-permissions")
- [I want to allow people outside of my AWS account to access my Data Transfer Terminal resources](#security-iam-troubleshoot-cross-account-access "#security-iam-troubleshoot-cross-account-access")

## I am not authorized to perform an action in Data Transfer Terminal

If you’re unable to view or schedule reservations in the AWS Data Transfer Terminal console, you may not have the required permissions. Contact your account administrator to configure an IAM identity policy that grants you access and appropriate permissions.

## I want to allow people outside of my AWS account to access my Data Transfer Terminal resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:

- To learn whether Data Transfer Terminal supports these features, see [How Data Transfer Terminal works with IAM](security-iam-service-with-iam.md "security-iam-service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.
