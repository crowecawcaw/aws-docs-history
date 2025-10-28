On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Troubleshooting Amazon CodeGuru Security identity and

access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with CodeGuru Security and IAM.

###### Topics

- [I am not authorized to
  perform an action in CodeGuru Security](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I want to allow people
  outside of my AWS account to access my CodeGuru Security resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

## I am not authorized to

perform an action in CodeGuru Security

If the AWS Management Console tells you that you're not authorized to perform an action, you must
contact your administrator for assistance.

The following example error occurs when the user `mateojackson` tries to
use the console to view details about a code review, but does not have
`codeguru-security:`CreateScan``
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform:
            codeguru-security:`CreateScan` on resource: `my-example-code-scan`
```

In this case, Mateo asks his administrator to update his policies to allow him to
access the `my-example-code-scan` resource using
the `codeguru-security:`CreateScan`` action.

## I want to allow people

outside of my AWS account to access my CodeGuru Security resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether CodeGuru Security supports these features, see [How Amazon CodeGuru Security works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.
