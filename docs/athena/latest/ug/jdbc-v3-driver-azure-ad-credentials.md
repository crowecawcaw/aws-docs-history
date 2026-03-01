# Azure AD credentials

A SAML-based authentication mechanism that enables authentication to Athena using the
Azure AD identity provider. This method assumes that a federation has already been set
up between Athena and Azure AD.

###### Note

Some of the parameter names in this section have aliases. The aliases are
functional equivalents of the parameter names and have been provided for backward
compatibility with the JDBC 2.x driver. Because the parameter names have been
improved to follow a clearer, more consistent naming convention, we recommend that
you use them instead of the aliases, which have been deprecated.

## Credentials provider

The credentials provider that will be used to authenticate requests to AWS. Set
the value of this parameter to `AzureAD`.

| Parameter name      | Alias                                    | Parameter type | Default value | Value to use |
| ------------------- | ---------------------------------------- | -------------- | ------------- | ------------ |
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required       | none          | `AzureAD`    |

## User

The email address of the Azure AD user to use for authentication with Azure
AD.

| Parameter name | Alias            | Parameter type | Default value |
| -------------- | ---------------- | -------------- | ------------- |
| User           | UID (deprecated) | Required       | none          |

## Password

The password for the Azure AD user.

| Parameter name | Alias            | Parameter type | Default value |
| -------------- | ---------------- | -------------- | ------------- |
| Password       | PWD (deprecated) | Required       | none          |

## Azure AD tenant ID

The tenant ID of your Azure AD application.

| Parameter name  | Alias                  | Parameter type | Default value |
| --------------- | ---------------------- | -------------- | ------------- |
| AzureAdTenantId | tenant_id (deprecated) | Required       | none          |

## Azure AD client ID

The client ID of your Azure AD application.

| Parameter name  | Alias                  | Parameter type | Default value |
| --------------- | ---------------------- | -------------- | ------------- |
| AzureAdClientId | client_id (deprecated) | Required       | none          |

## Azure AD client secret

The client secret of your Azure AD application.

| Parameter name      | Alias                      | Parameter type | Default value |
| ------------------- | -------------------------- | -------------- | ------------- |
| AzureAdClientSecret | client_secret (deprecated) | Required       | none          |

## Preferred role

The Amazon Resource Name (ARN) of the role to assume. For information about ARN
roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_AWS Security Token Service API Reference_.

| Parameter name | Alias                       | Parameter type | Default value |
| -------------- | --------------------------- | -------------- | ------------- |
| PreferredRole  | preferred_role (deprecated) | Optional       | none          |

## Role session duration

The duration, in seconds, of the role session. For more information, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the _AWS Security Token Service API Reference_.

| Parameter name      | Alias                 | Parameter type | Default value |
| ------------------- | --------------------- | -------------- | ------------- |
| RoleSessionDuration | Duration (deprecated) | Optional       | 3600          |

## Lake Formation enabled

Specifies whether to use the [AssumeDecoratedRoleWithSAML](../../../lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.md "../../../lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.md") Lake Formation API action to retrieve temporary IAM
credentials instead of the [AssumeRoleWithSAML](../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md "../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md") AWS STS API action.

| Parameter name       | Alias | Parameter type | Default value |
| -------------------- | ----- | -------------- | ------------- |
| LakeFormationEnabled | none  | Optional       | FALSE         |
