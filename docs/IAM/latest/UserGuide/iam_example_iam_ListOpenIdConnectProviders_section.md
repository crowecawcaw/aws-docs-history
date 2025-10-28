# Use `ListOpenIdConnectProviders` with a CLI

The following code examples show how to use `ListOpenIdConnectProviders`.

CLI

**AWS CLI**

**To list information about the OpenID Connect providers in the AWS account**

This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account.

```
`aws iam list-open-id-connect-providers`

```

Output:

```
{
    "OpenIDConnectProviderList": [
        {
            "Arn": "arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com"
        }
    ]
}
```

For more information, see [Creating OpenID Connect (OIDC) identity providers](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md") in the _AWS IAM User Guide_.

- For API details, see
  [ListOpenIdConnectProviders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-open-id-connect-providers.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-open-id-connect-providers.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account.**

```
Get-IAMOpenIDConnectProviderList

```

**Output:**

```
Arn
---
arn:aws:iam::123456789012:oidc-provider/server.example.com
arn:aws:iam::123456789012:oidc-provider/another.provider.com
```

- For API details, see
  [ListOpenIdConnectProviders](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account.**

```
Get-IAMOpenIDConnectProviderList

```

**Output:**

```
Arn
---
arn:aws:iam::123456789012:oidc-provider/server.example.com
arn:aws:iam::123456789012:oidc-provider/another.provider.com
```

- For API details, see
  [ListOpenIdConnectProviders](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
