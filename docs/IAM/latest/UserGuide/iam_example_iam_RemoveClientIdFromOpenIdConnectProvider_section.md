# Use `RemoveClientIdFromOpenIdConnectProvider` with a CLI

The following code examples show how to use `RemoveClientIdFromOpenIdConnectProvider`.

CLI

**AWS CLI**

**To remove the specified client ID from the list of client IDs registered for the specified IAM OpenID Connect provider**

This example removes the client ID `My-TestApp-3` from the list of client IDs associated with the IAM OIDC provider whose
ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`.

```
`aws iam remove-client-id-from-open-id-connect-provider
 --client-id `My-TestApp-3` \
 --open-id-connect-provider-arn `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com``

```

This command produces no output.

For more information, see [Creating OpenID Connect (OIDC) identity providers](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md") in the _AWS IAM User Guide_.

- For API details, see
  [RemoveClientIdFromOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-client-id-from-open-id-connect-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-client-id-from-open-id-connect-provider.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the client ID `My-TestApp-3` from the list of client IDs associated with the IAM OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`.**

```
Remove-IAMClientIDFromOpenIDConnectProvider -ClientID My-TestApp-3 -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com

```

- For API details, see
  [RemoveClientIdFromOpenIdConnectProvider](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the client ID `My-TestApp-3` from the list of client IDs associated with the IAM OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`.**

```
Remove-IAMClientIDFromOpenIDConnectProvider -ClientID My-TestApp-3 -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com

```

- For API details, see
  [RemoveClientIdFromOpenIdConnectProvider](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
