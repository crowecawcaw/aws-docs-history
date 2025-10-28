# Create a SAML identity provider in

IAM

An IAM SAML 2.0 identity provider is an entity in IAM that describes an external
identity provider (IdP) service that supports the [SAML 2.0 (Security Assertion Markup Language
2.0)](https://wiki.oasis-open.org/security "https://wiki.oasis-open.org/security") standard. You use an IAM identity provider when you want to establish trust
between a SAML-compatible IdP such as Shibboleth or Active Directory Federation Services and
AWS, so that your users can access AWS resources. IAM SAML identity providers are used as
principals in an IAM trust policy.

For more information about this scenario, see [SAML 2.0 federation](id_roles_providers_saml.md "id_roles_providers_saml.md").

You can create and manage an IAM identity provider in the AWS Management Console or with AWS CLI, Tools for Windows PowerShell,
or AWS API calls.

After you create a SAML provider, you must create one or more IAM roles. A role is an
identity in AWS that doesn't have its own credentials (as a user does). But in this context, a
role is dynamically assigned to a SAML federated principal that is authenticated by your IdP. The role
permits your IdP to request temporary security credentials for access to AWS. The policies
assigned to the role determine what users are allowed to do in AWS. To create a
role for SAML federation, see [Create a role for a third-party identity provider](id_roles_create_for-idp.md "id_roles_create_for-idp.md") .

Finally, after you create the role, you complete the SAML trust by configuring your IdP with
information about AWS and the roles that you want your SAML federated principals to use. This is
referred to as configuring relying party trust between your IdP and AWS. To configure relying
party trust, see [Configure your SAML 2.0 IdP with
relying party trust and adding claims](id_roles_providers_create_saml_relying-party.md "id_roles_providers_create_saml_relying-party.md").

###### Topics

- [Prerequisites](#idp-manage-identityprovider-prerequisites "#idp-manage-identityprovider-prerequisites")
- [Create and manage an IAM SAML identity
  provider (console)](#idp-manage-identityprovider-console "#idp-manage-identityprovider-console")
- [Manage SAML encryption keys](#id_federation_manage-saml-encryption "#id_federation_manage-saml-encryption")
- [Create and manage an IAM SAML Identity
  Provider (AWS CLI)](#idp-create-identityprovider-CLI "#idp-create-identityprovider-CLI")
- [Create and manage an IAM SAML identity
  provider (AWS API)](#idp-create-identityprovider-API "#idp-create-identityprovider-API")
- [Next steps](#id_roles_create-for-saml-next-steps "#id_roles_create-for-saml-next-steps")

## Prerequisites

Before you can create a SAML identity provider, you must have the following information
from your IdP.

- Get the SAML metadata document from your IdP. This document includes the issuer's
  name, expiration information, and keys that can be used to validate the SAML
  authentication response (assertions) that are received from the IdP. To generate the
  metadata document, use the identity management software provided by your external
  IdP.

###### Important

This metadata file includes the issuer name, expiration information, and keys that can be
used to validate the SAML authentication response (assertions) received from the IdP. The
metadata file must be encoded in UTF-8 format without a byte order mark (BOM). To remove the
BOM, you can encode the file as UTF-8 using a text editing tool, such as Notepad++.

The X.509 certificate included as part of the SAML metadata document must use a key size
of at least 1024 bits. Also, the X.509 certificate must also be free of any repeated
extensions. You can use extensions, but the extensions can only appear once in the
certificate. If the X.509 certificate does not meet either condition, IdP creation fails and
returns an "Unable to parse metadata" error.

As defined by the [SAML
V2.0 Metadata Interoperability Profile Version 1.0](https://docs.oasis-open.org/security/saml/Post2.0/sstc-metadata-iop-os.html "https://docs.oasis-open.org/security/saml/Post2.0/sstc-metadata-iop-os.html"), IAM does not evaluate or
take action on the expiration of X.509 certificates in SAML metadata documents. If you are
concerned about expired X.509 certificates, we recommend monitoring certificate expiration
dates and rotating certificates according to your organization’s governance and security
policies.

- When you choose to enable SAML encryption, you must generate a private key file using
  your IdP, and upload this file to your IAM SAML configuration in .pem file format. AWS STS
  needs this private key to decrypt SAML responses that correspond to the public key
  uploaded to your IdP. The following algorithms are supported:

      + Encryption algorithms




      	- AES-128
      	- AES-256
      	- RSA-OAEP
      + Key transport algorithms




      	- AES-CBC
      	- AES-GCM

  See your identity provider's documentation for steps to generate a private key.

###### Note

IAM Identity Center and Amazon Cognito do not support encrypted SAML assertions from IAM SAML identity
providers. You can indirectly add support for encrypted SAML assertions to Amazon Cognito
identity pool federation with Amazon Cognito user pools. User pools have SAML federation that's
independent of IAM SAML federation and supports [SAML signing and encryption](../../../cognito/latest/developerguide/cognito-user-pools-SAML-signing-encryption.md "../../../cognito/latest/developerguide/cognito-user-pools-SAML-signing-encryption.md"). Although this feature doesn't extend directly to
identity pools, user pools can be IdPs to identity pools. To use SAML encryption with
identity pools, add a SAML provider with encryption to a user pool that is an IdP to an
identity pool.

Your SAML provider must be able to encrypt SAML assertions with a key that your user
pool provides. User pools won't accept assertions encrypted with a certificate that
IAM has provided.

For instructions on how to configure many of the available IdPs to work with AWS,
including how to generate the required SAML metadata document, see [Integrate third-party SAML solution
providers with AWS](id_roles_providers_saml_3rd-party.md "id_roles_providers_saml_3rd-party.md").

For help with SAML federation, see [Troubleshooting SAML
federation](troubleshoot_saml.md "troubleshoot_saml.md").

## Create and manage an IAM SAML identity

provider (console)

You can use the AWS Management Console to create, update, and delete IAM SAML identity providers. For
help with SAML federation, see [Troubleshooting SAML
federation](troubleshoot_saml.md "troubleshoot_saml.md").

###### To create an IAM SAML identity provider (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Identity providers** and then choose
   **Add provider**.
3. For **Configure provider**, choose **SAML**.
4. Type a name for the identity provider.
5. For **Metadata document**, choose **Choose file**,
   specify the SAML metadata document that you downloaded in [Prerequisites](#idp-manage-identityprovider-prerequisites "#idp-manage-identityprovider-prerequisites").

###### Note

The `validUntil` or `cacheDuration` attribute in your SAML
metadata document defines the **Valid until** date for the identity
provider. If your SAML metadata document does not include a validity period attribute,
the **Valid until** date will not match your X.509 certificate
expiration date.

IAM does not evaluate or take action on the expiration of X.509 certificates in
SAML metadata documents. If you are concerned about expired X.509 certificates, we
recommend monitoring certificate expiration dates and rotating certificates according to
your organization’s governance and security policies. 6. (Optional) For **SAML encryption**, choose **Choose
file** and select the private key file that you created in [Prerequisites](#idp-manage-identityprovider-prerequisites "#idp-manage-identityprovider-prerequisites"). Choose **Require
encryption** to accept only encrypted requests from your IdP. 7. (Optional) For **Add tags**, you can add key–value pairs to help you
identify and organize your IdPs. You can also use tags to control access to AWS
resources. To learn more about tagging SAML identity providers, see [Tag IAM SAML identity providers](id_tags_saml.md "id_tags_saml.md").

Choose **Add tag**. Enter values for each tag key-value pair. 8. Verify the information that you have provided. When you are done, choose **Add
provider**. 9. Assign an IAM role to your identity provider. This role gives external user
identities managed by your identity provider permissions to access AWS resources in your
account. To learn more about creating roles for identity federation, see [Create a role for a third-party identity provider](id_roles_create_for-idp.md "id_roles_create_for-idp.md") .

###### Note

SAML IDPs used in a role trust policy must be in the same account that the role is
in.

###### To delete a SAML provider (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Identity providers**.
3. Select the radio button next to the identity provider that you want to delete.
4. Choose **Delete**. A new window opens.
5. Confirm that you want to delete the provider by typing the word `delete` in
   the field. Then, choose **Delete**.

## Manage SAML encryption keys

You can configure IAM SAML providers to receive encrypted assertions in the SAML
response from your external IdP. Users can assume a role in AWS with encrypted SAML
assertions by calling `sts:AssumeRoleWithSAML`.

SAML encryption ensures that assertions are secure when passed through intermediaries or
third parties. In addition, this feature helps you meet FedRAMP or any internal compliance
policy requirements that mandate SAML assertions to be encrypted.

To configure an IAM SAML identity provider, see [Create a SAML identity provider in
IAM](id_roles_providers_create_saml.md "id_roles_providers_create_saml.md").
For help with SAML federation, see [Troubleshooting SAML
federation](troubleshoot_saml.md "troubleshoot_saml.md").

### Rotate SAML encryption key

IAM uses the private key you uploaded to the IAM SAML provider to decrypt encrypted
SAML assertions from your IdP. You can save up to two private key files for each identity
provider, allowing you to rotate private keys as necessary. When two files are saved, each
request will first attempt to decrypt with the newest **Added on** date,
then IAM attempts to decrypt the request with the oldest **Added on**
date.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Identity providers** and then
   select your provider from the list.
3. Choose the **SAML encryption** tab and choose **Add new
   key**.
4. Select **Choose file** and upload the private key you downloaded
   from your IdP as a .pem file.Then, choose **Add key**.
5. In the **Private keys for SAML decryption** section, select the
   expired private key file and choose **Remove**. We recommend you remove
   the expired private key after adding a new private key to ensure the first attempt to
   decrypt your assertion is successful.

## Create and manage an IAM SAML Identity

Provider (AWS CLI)

You can use the AWS CLI to create, update, and delete SAML providers. For help with SAML
federation, see [Troubleshooting SAML
federation](troubleshoot_saml.md "troubleshoot_saml.md").

###### To create an IAM identity provider and upload a metadata document (AWS CLI)

- Run this command: [`aws
iam create-saml-provider`](../../../cli/latest/reference/iam/create-saml-provider.md "../../../cli/latest/reference/iam/create-saml-provider.md")

###### To update an IAM SAML identity provider (AWS CLI)

You can update the metadata file, SAML encryption settings,
and rotate private key decryption files for your IAM SAML provider. To rotate private
keys, add your new private key and then remove the old key in a separate request. For more
information about rotating private keys, see [Manage SAML encryption keys](#id_federation_manage-saml-encryption "#id_federation_manage-saml-encryption").

- Run this command:[`aws iam
update-saml-provider`](../../../cli/latest/reference/iam/update-saml-provider.md "../../../cli/latest/reference/iam/update-saml-provider.md")

###### To tag an existing IAM identity provider (AWS CLI)

- Run this command:[`aws iam
tag-saml-provider`](../../../cli/latest/reference/iam/tag-saml-provider.md "../../../cli/latest/reference/iam/tag-saml-provider.md")

###### To list tags for existing IAM identity provider (AWS CLI)

- Run this command:[`aws
iam list-saml-provider-tags`](../../../cli/latest/reference/iam/list-saml-provider-tags.md "../../../cli/latest/reference/iam/list-saml-provider-tags.md")

###### To remove tags on an existing IAM identity provider (AWS CLI)

- Run this command:[`aws iam
untag-saml-provider`](../../../cli/latest/reference/iam/untag-saml-provider.md "../../../cli/latest/reference/iam/untag-saml-provider.md")

###### To delete an IAM SAML identity provider (AWS CLI)

1. (Optional) To list information for all providers, such as the ARN, creation date, and
   expiration, run the following command:
   - [`aws iam
list-saml-providers`](../../../cli/latest/reference/iam/list-saml-providers.md "../../../cli/latest/reference/iam/list-saml-providers.md")

2. (Optional) To get information about a specific provider, such as the ARN, creation
   date, expiration date, encryption settings, and private key information, run the following
   command:
   - [`aws iam
get-saml-provider`](../../../cli/latest/reference/iam/get-saml-provider.md "../../../cli/latest/reference/iam/get-saml-provider.md")

3. To delete an IAM identity provider, run the following command:
   - [`aws iam
delete-saml-provider`](../../../cli/latest/reference/iam/delete-saml-provider.md "../../../cli/latest/reference/iam/delete-saml-provider.md")

## Create and manage an IAM SAML identity

provider (AWS API)

You can use the AWS API to create, update, and delete SAML providers. For help with SAML
federation, see [Troubleshooting SAML
federation](troubleshoot_saml.md "troubleshoot_saml.md").

###### To create an IAM identity provider and upload a metadata document (AWS API)

- Call this operation: [`CreateSAMLProvider`](../APIReference/API_CreateSAMLProvider.md "../APIReference/API_CreateSAMLProvider.md")

###### To update an IAM SAML identity provider (AWS API)

You can update the metadata file, SAML encryption settings,
and rotate private key decryption files for your IAM SAML provider. To rotate private
keys, add your new private key and then remove the old key in a separate request. For more
information about rotating private keys, see [Manage SAML encryption keys](#id_federation_manage-saml-encryption "#id_federation_manage-saml-encryption").

- Call this operation: [`UpdateSAMLProvider`](../APIReference/API_UpdateSAMLProvider.md "../APIReference/API_UpdateSAMLProvider.md")

###### To tag an existing IAM identity provider (AWS API)

- Call this operation: [`TagSAMLProvider`](../APIReference/API_TagSAMLProvider.md "../APIReference/API_TagSAMLProvider.md")

###### To list tags for an existing IAM identity provider (AWS API)

- Call this operation: [`ListSAMLProviderTags`](../APIReference/API_ListSAMLProviderTags.md "../APIReference/API_ListSAMLProviderTags.md")

###### To remove tags on an existing IAM identity provider (AWS API)

- Call this operation: [`UntagSAMLProvider`](../APIReference/API_UntagSAMLProvider.md "../APIReference/API_UntagSAMLProvider.md")

###### To delete an IAM identity provider (AWS API)

1. (Optional) To list information for all IdPs, such as the ARN, creation date, and
   expiration, call the following operation:
   - [`ListSAMLProviders`](../APIReference/API_ListSAMLProviders.md "../APIReference/API_ListSAMLProviders.md")

2. (Optional) To get information about a specific provider, such as the ARN, creation
   date, expiration date, encryption settings, and private key information, call the
   following operation:
   - [`GetSAMLProvider`](../APIReference/API_GetSAMLProvider.md "../APIReference/API_GetSAMLProvider.md")

3. To delete an IdP, call the following operation:
   - [`DeleteSAMLProvider`](../APIReference/API_DeleteSAMLProvider.md "../APIReference/API_DeleteSAMLProvider.md")

## Next steps

After you create a SAML identity provider, set up the relying party trust with your IdP.
You can also use claims from your IdP's authentication response in policies to control access
to a role.

- You must tell the IdP about AWS as a service provider. This is called adding relying
  party trust between your IdP and AWS. The exact process for adding relying party trust
  depends on what IdP you're using. For details, see [Configure your SAML 2.0 IdP with
  relying party trust and adding claims](id_roles_providers_create_saml_relying-party.md "id_roles_providers_create_saml_relying-party.md").
- When the IdP sends the response containing the claims to AWS, many of the incoming
  claims map to AWS context keys. You can use these context keys in IAM policies using
  the Condition element to control access to a role. For details, see [Configure SAML assertions for the
  authentication response](id_roles_providers_create_saml_assertions.md "id_roles_providers_create_saml_assertions.md")
