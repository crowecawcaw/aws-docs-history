# How AWS User Experience Customization works with IAM

AWS User Experience Customization (UXC) works with IAM policies to manage access to UXC API
Operations.

Before you use IAM to manage access to AWS User Experience Customization (User Experience Customization), learn what IAM
features are available to use with User Experience Customization. We recommend you integrate with User Experience Customization
through an AWS managed policy, for more information, see [AWS managed policies for the AWS Management Console](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

Before you use IAM to manage access to User Experience Customization, learn what IAM features are
available to use with User Experience Customization.

| IAM feature                                                                                                                           | User Experience Customization support |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")        | Yes                                   |
| Resource-based policies                                                                                                               | No                                    |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions") | Yes                                   |
| Policy resources                                                                                                                      | No                                    |
| Policy condition keys                                                                                                                 | No                                    |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")           | Yes                                   |
| Cross-service principal permissions                                                                                                   | No                                    |
| Service-linked roles                                                                                                                  | No                                    |
| Service roles                                                                                                                         | No                                    |

To get a high-level view of how User Experience Customization and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based policies for User Experience Customization

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

To view examples of User Experience Customization identity-based policies, see [Identity-based policy examples for
AWS User Experience Customization](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy actions for User Experience Customization

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see all User Experience Customization actions, refer to the [API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

Policy actions in User Experience Customization use the `uxc:` prefix before the
action (for example `uxc:GetAccountCustomizations`).

To specify multiple actions in a single statement, separate them with commas:

```
"Action": [
      "uxc:GetAccountCustomizations",
      "uxc:ListServices"
         ]
```

To view examples of User Experience Customization identity-based policies, see [Identity-based policy examples for
AWS User Experience Customization](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy resources for User Experience Customization

User Experience Customization does not support policy resources.

## Using temporary credentials with User Experience Customization

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Troubleshooting AWS User Experience Customization identity and access

Use the following information to help you diagnose and fix common issues that you
might encounter when working with User Experience Customization and IAM.

If you receive an error that you're not authorized to perform an action, your
policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a fictional
`my-example-widget` resource but doesn't
have the fictional `uxc:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: uxc:GetWidget on resource: my-example-widget because no identity-based policy allows the GetWidget action
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the
`my-example-widget` resource by using the
`uxc:`GetWidget`` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

After you create your IAM user access keys, you can view your access key ID at any time. However, you can't view your secret access key again.
If you lose your secret key, you must create a new access key pair.

Access keys consist of two parts: an access key ID (for example, `AKIAIOSFODNN7EXAMPLE`) and a secret access key (for example,
`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`). Like a user name and password, you must use both the access key ID and secret access key
together to authenticate your requests. Manage your access keys as securely as you do your user name and password.

###### Important

Do not provide your access keys to a third party, even to help [find your canonical user ID](../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId "../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId").
By doing this, you might give someone permanent access to your AWS account.

When you create an access key pair, you are prompted to save the access key ID and secret access key in a secure location. The secret access key
is available only at the time you create it. If you lose your secret access key, you must add new access keys to your IAM user. You can have a
maximum of two access keys. If you already have two, you must delete one key pair before creating a new one. To view instructions, see [Managing access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey") in the
_IAM User Guide_.

To allow others to access User Experience Customization, you must grant permission to the people or applications that need access. If you are using AWS IAM Identity Center
to manage people and applications, you assign permission sets to users or groups to define their level of access. Permission sets automatically create
and assign IAM policies to IAM roles that are associated with the person or application. For more information, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people or applications that need access. You must then attach
a policy to the entity that grants them the correct permissions in User Experience Customization. After the permissions are granted, provide the credentials to the user
or application developer. They will use those credentials to access AWS. To learn more about creating IAM users, groups, policies, and permissions,
see [IAM Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") and [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
