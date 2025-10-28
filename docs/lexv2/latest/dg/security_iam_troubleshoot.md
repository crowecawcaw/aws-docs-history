# Troubleshooting

Amazon Lex V2 identity and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Amazon Lex V2 and IAM.

###### Topics

- [I am not
  authorized to perform an action in Amazon Lex V2](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I am not
  authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")
- [I'm an
  administrator and want to allow others to access
  Amazon Lex V2](#security_iam_troubleshoot-admin-delegate "#security_iam_troubleshoot-admin-delegate")
- [Grant programmatic access to a user](#security_iam_programmatic_access "#security_iam_programmatic_access")
- [I
  want to allow people outside of my AWS account to access my
  Amazon Lex V2 resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

## I am not

authorized to perform an action in Amazon Lex V2

If the AWS Management Console tells you that you're not authorized to perform
an action, then you must contact your administrator for assistance.
Your administrator is the person that provided you with your sign-in
credentials.

The following example error occurs when the
`mateojackson` IAM user tries to use the console to
view details about a fictional
`my-example-widget`
resource but does not have the fictional
`lex:`GetWidget``
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: lex:`GetWidget` on resource: `my-example-widget`
```

In this case, Mateo asks his administrator to update his policies
to allow him to access the
`my-example-widget`
resource using the
`lex:`GetWidget``
action.

## I am not

authorized to perform iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Amazon Lex V2.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
Amazon Lex V2. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I'm an

administrator and want to allow others to access
Amazon Lex V2

To allow others to access Amazon Lex V2, you must grant permission to the people or applications that need access. If you are using AWS IAM Identity Center
to manage people and applications, you assign permission sets to users or groups to define their level of access. Permission sets automatically create
and assign IAM policies to IAM roles that are associated with the person or application. For more information, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people or applications that need access. You must then attach
a policy to the entity that grants them the correct permissions in Amazon Lex V2. After the permissions are granted, provide the credentials to the user
or application developer. They will use those credentials to access AWS. To learn more about creating IAM users, groups, policies, and permissions,
see [IAM Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") and [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

## Grant programmatic access to a user

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                     | To                                                                                                              | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity (Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use. <br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. <br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                        |
| IAM                                                       | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions in [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| IAM                                                       | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. <br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in the _AWS Command Line Interface User Guide_. <br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the _AWS SDKs and Tools Reference Guide_. <br>• For AWS APIs, see [Managing access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. | ## I want to allow people outside of my AWS account to access my Amazon Lex V2 resources You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources. To learn more, consult the following: <br>• To learn whether Amazon Lex V2 supports these features, see [How Amazon Lex V2 works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md"). <br>• To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_. <br>• To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _IAM User Guide_. <br>• To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_. <br>• To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_. |
