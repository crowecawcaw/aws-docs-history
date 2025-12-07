# Troubleshooting Amazon Nova Act identity and access

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Nova Act and IAM.

###### Topics

- [I am not authorized to perform an action in Amazon Nova Act](#security-iam-troubleshoot-no-permissions "#security-iam-troubleshoot-no-permissions")
- [I want to allow people outside of my AWS account to access my Amazon Nova Act resources](#security-iam-troubleshoot-cross-account-access "#security-iam-troubleshoot-cross-account-access")

## I am not authorized to perform an action in Amazon Nova Act

If the AWS Management Console tells you that you’re not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your user name and password.

The following example error occurs when the `mateojackson`
IAM user tries to use the console to view details about workflow runs but does not have `nova-act:ListWorkflowRuns` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: nova-act:ListWorkflowRuns on resource: my-workflow-definition
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `my-workflow-definition` resource using the `nova-act:ListWorkflowRuns` action.

## I want to allow people outside of my AWS account to access my Amazon Nova Act resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:

- To learn whether Amazon Nova Act supports these features, see [How Amazon Nova Act works with IAM](security-iam-service-with-iam.md "security-iam-service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing Access to Externally Authenticated Users (Identity Federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the _IAM User Guide_.
