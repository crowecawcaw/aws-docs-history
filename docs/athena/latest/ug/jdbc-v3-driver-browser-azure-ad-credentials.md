# Browser Azure AD credentials

Browser Azure AD is a SAML-based authentication mechanism that works with the Azure AD
identity provider and supports multi-factor authentication. Unlike the standard Azure AD
authentication mechanism, this mechanism does not require a user name, password, or
client secret in the connection parameters. Like the standard Azure AD authentication
mechanism, Browser Azure AD also assumes the user has already set up federation between
Athena and Azure AD.

## Credentials provider

The credentials provider that will be used to authenticate requests to AWS. Set
the value of this parameter to `BrowserAzureAD`.

| Parameter name      | Alias                                    | Parameter type | Default value | Value to use     |
| ------------------- | ---------------------------------------- | -------------- | ------------- | ---------------- |
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required       | none          | `BrowserAzureAD` |

## Azure AD tenant ID

The tenant ID of your Azure AD application

| Parameter name  | Alias                  | Parameter type | Default value |
| --------------- | ---------------------- | -------------- | ------------- |
| AzureAdTenantId | tenant_id (deprecated) | Required       | none          |

## Azure AD client ID

The client ID of your Azure AD application

| Parameter name  | Alias                  | Parameter type | Default value |
| --------------- | ---------------------- | -------------- | ------------- |
| AzureAdClientId | client_id (deprecated) | Required       | none          |

## Identity provider response timeout

The duration, in seconds, before the driver stops waiting for the SAML response
from Azure AD.

| Parameter name     | Alias                             | Parameter type | Default value |
| ------------------ | --------------------------------- | -------------- | ------------- |
| IdpResponseTimeout | idp_response_timeout (deprecated) | Optional       | 120           |

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
