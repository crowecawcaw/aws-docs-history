# Use `GetOpenIdConnectProvider` with a CLI

The following code examples show how to use `GetOpenIdConnectProvider`.

CLI

**AWS CLI**

**To return information about the specified OpenID Connect provider**

This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/server.example.com`.

```
`aws iam get-open-id-connect-provider \
 --open-id-connect-provider-arn `arn:aws:iam::123456789012:oidc-provider/server.example.com``

```

Output:

```
{
    "Url": "server.example.com"
        "CreateDate": "2015-06-16T19:41:48Z",
        "ThumbprintList": [
        "12345abcdefghijk67890lmnopqrst987example"
        ],
        "ClientIDList": [
        "example-application-ID"
        ]
}
```

For more information, see [Creating OpenID Connect (OIDC) identity providers](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-open-id-connect-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-open-id-connect-provider.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/accounts.google.com`. The `ClientIDList` property is a collection that contains all the Client IDs defined for this provider.**

```
Get-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/oidc.example.com

```

**Output:**

```
ClientIDList         CreateDate                ThumbprintList                               Url
------------         ----------                --------------                               ---
{MyOIDCApp}          2/3/2015 3:00:30 PM       {12345abcdefghijk67890lmnopqrst98765uvwxy}   oidc.example.com
```

- For API details, see
  [GetOpenIdConnectProvider](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/accounts.google.com`. The `ClientIDList` property is a collection that contains all the Client IDs defined for this provider.**

```
Get-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/oidc.example.com

```

**Output:**

```
ClientIDList         CreateDate                ThumbprintList                               Url
------------         ----------                --------------                               ---
{MyOIDCApp}          2/3/2015 3:00:30 PM       {12345abcdefghijk67890lmnopqrst98765uvwxy}   oidc.example.com
```

- For API details, see
  [GetOpenIdConnectProvider](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
