# Use `GetSamlProvider` with a CLI

The following code examples show how to use `GetSamlProvider`.

CLI

**AWS CLI**

**To retrieve the SAML provider metadocument**

This example retrieves the details about the SAML 2.0 provider whose ARM is `arn:aws:iam::123456789012:saml-provider/SAMLADFS`.
The response includes the metadata document that you got from the identity provider to create the AWS SAML provider entity as well
as the creation and expiration dates.

```
`aws iam get-saml-provider \
 --saml-provider-arn `arn:aws:iam::123456789012:saml-provider/SAMLADFS``

```

Output:

```
{
    "SAMLMetadataDocument": "...SAMLMetadataDocument-XML...",
    "CreateDate": "2017-03-06T22:29:46+00:00",
    "ValidUntil": "2117-03-06T22:29:46.433000+00:00",
    "Tags": [
        {
            "Key": "DeptID",
            "Value": "123456"
        },
        {
            "Key": "Department",
            "Value": "Accounting"
        }
    ]
}
```

For more information, see [Creating IAM SAML identity providers](id_roles_providers_create_saml.md "id_roles_providers_create_saml.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetSamlProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-saml-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-saml-provider.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example retrieves the details about the SAML 2.0 provider whose ARM is arn:aws:iam::123456789012:saml-provider/SAMLADFS. The response includes the metadata document that you got from the identity provider to create the AWS SAML provider entity as well as the creation and expiration dates.**

```
Get-IAMSAMLProvider -SAMLProviderArn arn:aws:iam::123456789012:saml-provider/SAMLADFS

```

**Output:**

```
CreateDate                 SAMLMetadataDocument                                          ValidUntil
----------                 --------------------                                          ----------
12/23/2014 12:16:55 PM    <EntityDescriptor ID="_12345678-1234-5678-9012-example1...    12/23/2114 12:16:54 PM
```

- For API details, see
  [GetSamlProvider](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example retrieves the details about the SAML 2.0 provider whose ARM is arn:aws:iam::123456789012:saml-provider/SAMLADFS. The response includes the metadata document that you got from the identity provider to create the AWS SAML provider entity as well as the creation and expiration dates.**

```
Get-IAMSAMLProvider -SAMLProviderArn arn:aws:iam::123456789012:saml-provider/SAMLADFS

```

**Output:**

```
CreateDate                 SAMLMetadataDocument                                          ValidUntil
----------                 --------------------                                          ----------
12/23/2014 12:16:55 PM    <EntityDescriptor ID="_12345678-1234-5678-9012-example1...    12/23/2114 12:16:54 PM
```

- For API details, see
  [GetSamlProvider](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
