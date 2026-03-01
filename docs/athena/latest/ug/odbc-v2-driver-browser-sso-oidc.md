# Browser SSO OIDC

Browser SSO OIDC is an authentication plugin that works with AWS IAM Identity Center. For information on
enabling and using IAM Identity Center, see [Step 1:
Enable IAM Identity Center](../../../singlesignon/latest/userguide/get-started-enable-identity-center.md "../../../singlesignon/latest/userguide/get-started-enable-identity-center.md") in the _AWS IAM Identity Center User Guide_.

## Authentication type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**        |
| -------------------------- | ------------------ | ----------------- | ------------------------------------ |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=BrowserSSOOIDC;` |

## IAM Identity Center Start URL

The URL for the AWS access portal. The IAM Identity Center [StartDeviceAuthorization](../../../singlesignon/latest/OIDCAPIReference/API_StartDeviceAuthorization.md "../../../singlesignon/latest/OIDCAPIReference/API_StartDeviceAuthorization.md") API action uses this value for the
`startUrl` parameter.

###### To copy the AWS access portal URL

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Settings**.
3. On the **Settings** page, under **Identity
   source**, choose the clipboard icon for **AWS access
   portal URL**.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                          |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------------ |
| sso_oidc_start_url         | Required           | `none`            | `sso_oidc_start_url=https://app_id.awsapps.com/start;` |

## IAM Identity Center Region

The AWS Region where your SSO is configured. The `SSOOIDCClient` and
`SSOClient` AWS SDK clients use this value for the `region`
parameter.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| sso_oidc_region            | Required           | `none`            | `sso_oidc_region=us-east-1;`  |

## Scopes

The list of scopes that are defined by the client. Upon authorization, this list
restricts permissions when an access token is granted. The IAM Identity Center [RegisterClient](../../../singlesignon/latest/OIDCAPIReference/API_RegisterClient.md "../../../singlesignon/latest/OIDCAPIReference/API_RegisterClient.md") API action uses this value for the `scopes`
parameter.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**           |
| -------------------------- | ------------------ | ----------------- | --------------------------------------- |
| sso_oidc_scopes            | Optional           | `none`            | `sso_oidc_scopes=scope1,scope2,scope3;` |

## Account ID

The identifier for the AWS account that is assigned to the user. The IAM Identity Center [GetRoleCredentials](../../../singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.md "../../../singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.md") API uses this value for the `accountId`
parameter.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**       |
| -------------------------- | ------------------ | ----------------- | ----------------------------------- |
| sso_oidc_account_id        | Required           | `none`            | `sso_oidc_account_id=123456789123;` |

## Role name

The friendly name of the role that is assigned to the user. The name that you specify
for this permission set appears in the AWS access portal as an available role. The
IAM Identity Center [GetRoleCredentials](../../../singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.md "../../../singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.md") API action uses this value for the `roleName`
parameter.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**          |
| -------------------------- | ------------------ | ----------------- | -------------------------------------- |
| sso_oidc_role_name         | Required           | `none`            | `sso_oidc_role_name=AthenaReadAccess;` |

## Timeout

The number of seconds the polling SSO API should check for the access token.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| sso_oidc_timeout           | Optional           | `120`             | `sso_oidc_timeout=60;`        |

## Enable file cache

Enables a temporary credentials cache. This connection parameter enables temporary
credentials to be cached and reused between multiple processes. Use this option to
reduce the number of opened browser windows when you use BI tools such as Microsoft
Power BI.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| sso_oidc_cache             | Optional           | `1`               | `sso_oidc_cache=0;`           |
