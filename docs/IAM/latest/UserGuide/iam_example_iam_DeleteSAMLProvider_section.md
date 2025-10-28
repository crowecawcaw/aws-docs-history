# Use `DeleteSAMLProvider` with an AWS SDK or CLI

The following code examples show how to use `DeleteSAMLProvider`.

CLI

**AWS CLI**

**To delete a SAML provider**

This example deletes the IAM SAML 2.0 provider whose ARN is `arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider`.

```
`aws iam delete-saml-provider \
--saml-provider-arn `arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider``

```

This command produces no output.

For more information, see [Creating IAM SAML identity providers](id_roles_providers_create_saml.md "id_roles_providers_create_saml.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeleteSAMLProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-saml-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-saml-provider.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

```
import { DeleteSAMLProviderCommand, IAMClient } from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} providerArn
 * @returns
 */
export const deleteSAMLProvider = async (providerArn) => {
  const command = new DeleteSAMLProviderCommand({
    SAMLProviderArn: providerArn,
  });

  const response = await client.send(command);
  console.log(response);
  return response;
};


```

- For API details, see
  [DeleteSAMLProvider](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteSAMLProviderCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteSAMLProviderCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the IAM SAML 2.0 provider whose ARN is `arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider`.**

```
Remove-IAMSAMLProvider -SAMLProviderArn arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider

```

- For API details, see
  [DeleteSAMLProvider](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the IAM SAML 2.0 provider whose ARN is `arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider`.**

```
Remove-IAMSAMLProvider -SAMLProviderArn arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider

```

- For API details, see
  [DeleteSAMLProvider](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
