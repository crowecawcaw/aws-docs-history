# Use `UpdateOpenIdConnectProviderThumbprint` with a CLI

The following code examples show how to use `UpdateOpenIdConnectProviderThumbprint`.

CLI

**AWS CLI**

**To replace the existing list of server certificate thumbprints with a new list**

This example updates the certificate thumbprint list for the OIDC provider whose ARN is
`arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` to use a new thumbprint.

```
`aws iam update-open-id-connect-provider-thumbprint \
 --open-id-connect-provider-arn `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` \
 --thumbprint-list `7359755EXAMPLEabc3060bce3EXAMPLEec4542a3``

```

This command produces no output.

For more information, see [Creating OpenID Connect (OIDC) identity providers](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md") in the _AWS IAM User Guide_.

- For API details, see
  [UpdateOpenIdConnectProviderThumbprint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-open-id-connect-provider-thumbprint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-open-id-connect-provider-thumbprint.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example updates the certificate thumbprint list for the OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` to use a new thumbprint. The OIDC provider shares the new value when the certificate that is associated with the provider changes.**

```
Update-IAMOpenIDConnectProviderThumbprint -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com -ThumbprintList 7359755EXAMPLEabc3060bce3EXAMPLEec4542a3

```

- For API details, see
  [UpdateOpenIdConnectProviderThumbprint](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example updates the certificate thumbprint list for the OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` to use a new thumbprint. The OIDC provider shares the new value when the certificate that is associated with the provider changes.**

```
Update-IAMOpenIDConnectProviderThumbprint -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com -ThumbprintList 7359755EXAMPLEabc3060bce3EXAMPLEec4542a3

```

- For API details, see
  [UpdateOpenIdConnectProviderThumbprint](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
