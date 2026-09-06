

# Troubleshooting Amazon Nova Act identity and access
<a name="security-iam-troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Nova Act and IAM.

**Topics**
+ [I am not authorized to perform an action in Amazon Nova Act](#security-iam-troubleshoot-no-permissions)
+ [I want to allow people outside of my AWS account to access my Amazon Nova Act resources](#security-iam-troubleshoot-cross-account-access)

## I am not authorized to perform an action in Amazon Nova Act
<a name="security-iam-troubleshoot-no-permissions"></a>

If the AWS Management Console tells you that you’re not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your user name and password.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about workflow runs but does not have `nova-act:ListWorkflowRuns` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: nova-act:ListWorkflowRuns on resource: my-workflow-definition
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `my-workflow-definition` resource using the `nova-act:ListWorkflowRuns` action.

## I want to allow people outside of my AWS account to access my Amazon Nova Act resources
<a name="security-iam-troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Amazon Nova Act supports these features, see [How Amazon Nova Act works with IAM](security-iam-service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing Access to Externally Authenticated Users (Identity Federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html) in the *IAM User Guide*.