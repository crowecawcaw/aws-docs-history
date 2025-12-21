# Preparing and managing certificates for content key encryption

When implementing DRM encryption, AWS Elemental MediaPackage can enhance security by encrypting the
content keys within the Content Protection Information Exchange (CPIX) document exchanged with your key provider. This additional
encryption layer protects the content keys during transmission between MediaPackage and your
DRM key provider.

## Overview

When you create or modify origin endpoint resources in MediaPackage for DRM-protected
content, you can optionally specify a certificate ARN in the SPEKE encryption settings.
This certificate ARN must point to a certificate stored in AWS Certificate Manager (ACM).
This certificate provides encryption for content keys delivery between
MediaPackage and your key provider, as described in the
[SPEKE Version 2.0 content key encryption](../../../speke/latest/documentation/content-key-encryption-v2.md "../../../speke/latest/documentation/content-key-encryption-v2.md") specification.

This is an opt-in configuration. When you don't provide a certificate in your origin
endpoint resource's SPEKE encryption configuration, DRM key providers return content keys as plain text, which is the current and
default behavior. When you provide a certificate, the content key returned by your DRM
key provider is encrypted using the certificate's public key, and MediaPackage decrypts the
encrypted content key with the certificate's private key.

To use encrypted content keys, the following requirements must be met:

- Your DRM key provider must support content key encryption. If you enable this feature
  for a key provider that doesn't handle content key encryption, playback fails.
- You must provide a certificate stored in AWS Certificate Manager (ACM) in the same Region and Account that
  you run MediaPackage. For information about ACM, see the [AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md").

When you create or update an origin endpoint resource with certificate ARN, you must have ACM permissions.

The certificate must meet the following requirements:

    + **Status**: The certificate must be in
     **ISSUED** status
    + **Domain name**: The certificate must have a domain
     name
    + **Key algorithm**: The certificate must use RSA-2048
     key algorithm
    + **Signature algorithm**: The certificate must use
     either SHA-256 or SHA-512 signature algorithm
    + **Region**: The certificate must be in the same AWS
     Region as your origin endpoint
    + **Account**: The certificate must be in the same AWS
     Account as your origin endpoint

- The origin endpoint ARN length must not exceed 222 characters. An origin endpoint ARN
  follows this format:
  `arn:aws:mediapackagev2:`region`:`123456789012`:channelGroup/`channelGroupName`/channel/`channelName`/originEndpoint/`originEndpointName``.
  If the ARN length exceeds this limit, origin endpoint creation with content key encryption will fail due to an ARN length restriction.

The following procedures describe how to prepare and manage the certificate.

###### To prepare a certificate for DRM content key encryption

1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. Import or request a certificate into ACM according to the instructions at [AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md"). Note the resulting certificate ARN because you will need it
   later.

For use in DRM encryption, your certificate must have a status of
**Issued** in ACM.
**To use a certificate in MediaPackage**

When you create or modify an origin endpoint with DRM encryption, provide your certificate
ARN in the SPEKE encryption parameters. This enables content key encryption. You can use the same
certificate ARN for multiple origin endpoints. For information, see the encryption settings
information in [Working with origin endpoints in AWS Elemental MediaPackage](endpoints.md "endpoints.md").

## How content key encryption works

When you configure certificate-based content key encryption, the following process
occurs:

1. **MediaPackage retrieves your certificate**:
   MediaPackage uses your certificate ARN to retrieve the certificate details
   from ACM.
2. **CPIX request with certificate**: MediaPackage
   includes your certificate's public key in the CPIX request sent to your DRM key
   provider.
3. **DRM provider encrypts keys**: Your DRM key provider
   uses the certificate's public key for content key encryption
4. **MediaPackage decrypts keys**: MediaPackage uses the
   certificate's private key for content key decryption
5. **Content encryption**: MediaPackage uses the
   decrypted content keys to encrypt your content

###### Note

This process follows the [SPEKE Version 2.0 content key encryption](../../../speke/latest/documentation/content-key-encryption-v2.md "../../../speke/latest/documentation/content-key-encryption-v2.md")
specification for secure key exchange. Content key encryption adds an additional layer of security to the delivery of content key
without affecting the final content encryption.

**To delete a certificate**

To delete a certificate from ACM, it must not be associated with any other resources.
Delete the certificate ARN from origin endpoint configurations where you have used it, then
delete it from ACM.

###### Note

If you delete a certificate ARN from an active origin endpoint, the endpoint keeps
running, but stops using content key encryption.
