# Common authentication parameters

The parameters in this section are common to the authentication types as noted.

## Use Proxy for IdP

Enables communication between the driver and the IdP through the proxy. This
option is available for the following authentication plugins:

- AD FS
- Azure AD
- Browser Azure AD
- Browser SSO OIDC
- JWT trusted identity propagation
- JWT
- JWT trusted identity propagation
- Browser trusted identity propagation
- Okta
- Ping

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| UseProxyForIdP             | Optional           | `0`               | `UseProxyForIdP=1;`           |

## Use Lake Formation

Uses the [AssumeDecoratedRoleWithSAML](../../../lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.md "../../../lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.md") Lake Formation API action to retrieve temporary IAM
credentials instead of the [AssumeRoleWithSAML](../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md "../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md") AWS STS API action. This option is available for the
Azure AD, Browser Azure AD, Browser SAML, Okta, Ping, and AD FS authentication
plugins.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| LakeformationEnabled       | Optional           | `0`               | `LakeformationEnabled=1;`     |

## SSL insecure (IdP)

Disables SSL when communicating with the IdP. This option is available for the
Azure AD, Browser Azure AD, Okta, Ping, and AD FS authentication plugins.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| SSL_Insecure               | Optional           | `0`               | `SSL_Insecure=1;`             |
