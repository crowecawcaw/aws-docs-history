# Use `AddClientIdToOpenIdConnectProvider` with a CLI

The following code examples show how to use `AddClientIdToOpenIdConnectProvider`.

CLI

**AWS CLI**

**To add a client ID (audience) to an Open-ID Connect (OIDC) provider**

The following `add-client-id-to-open-id-connect-provider` command adds the client ID `my-application-ID` to the OIDC provider named `server.example.com`.

```
`aws iam add-client-id-to-open-id-connect-provider \
 --client-id `my-application-ID` \
 --open-id-connect-provider-arn `arn:aws:iam::123456789012:oidc-provider/server.example.com``

```

This command produces no output.

To create an OIDC provider, use the `create-open-id-connect-provider` command.

For more information, see [Creating OpenID Connect (OIDC) identity providers](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md") in the _AWS IAM User Guide_.

- For API details, see
  [AddClientIdToOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-client-id-to-open-id-connect-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-client-id-to-open-id-connect-provider.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command adds the client ID (or audience) `my-application-ID` to the existing OIDC provider named `server.example.com`.**

```
Add-IAMClientIDToOpenIDConnectProvider -ClientID "my-application-ID" -OpenIDConnectProviderARN "arn:aws:iam::123456789012:oidc-provider/server.example.com"

```

- For API details, see
  [AddClientIdToOpenIdConnectProvider](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command adds the client ID (or audience) `my-application-ID` to the existing OIDC provider named `server.example.com`.**

```
Add-IAMClientIDToOpenIDConnectProvider -ClientID "my-application-ID" -OpenIDConnectProviderARN "arn:aws:iam::123456789012:oidc-provider/server.example.com"

```

- For API details, see
  [AddClientIdToOpenIdConnectProvider](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
