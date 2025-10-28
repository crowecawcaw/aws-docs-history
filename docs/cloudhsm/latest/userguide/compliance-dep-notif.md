# Deprecation Notifications

From time to time, AWS CloudHSM may deprecate functionality in order to remain compliant with the requirements of FIPS 140, PCI-DSS, PCI-PIN, PCI-3DS, SOC2, or because of end-of-support hardware. This page lists the changes that currently apply.

## HSM1 Deprecation

The AWS CloudHSM hsm1.medium instance type will reach its end of support on December 1, 2025. To ensure continued service, we're introducing the following changes:

- Starting April 2025, you won't be able to create new hsm1.medium clusters.
- Starting April 2025, we will begin automatically migrating existing hsm1.medium clusters to the new hsm2m.medium instance type.

The hsm2m.medium instance type is compatible with your current AWS CloudHSM instance type and offers improved performance. To avoid disruption to your
applications, you must upgrade to latest version of client SDK. For upgrade instructions, see [Migrating from AWS CloudHSM Client SDK 3 to
Client SDK 5](client-sdk-migration.md "client-sdk-migration.md").

You have two options for migration:

1. Opt in to a CloudHSM-managed migration when you're ready. For more information, [Migrating from hsm1.medium to hsm2m.medium](hsm1-to-hsm2-migration.md "hsm1-to-hsm2-migration.md").
2. Create a new hsm2m.medium cluster from a backup of your hsm1 cluster and redirect your application to the new cluster. We recommend
   using a blue/green deployment strategy for this approach. For more information, see [Creating AWS CloudHSM clusters from backups](create-cluster-from-backup.md "create-cluster-from-backup.md").

## FIPS 140 Compliance: 2024 Mechanism Deprecation

The National Institute of Standards and Technology (NIST)[1](#dep-notif-1 "#dep-notif-1")
advises that support for Triple DES (DESede, 3DES, DES3) encryption and RSA key wrap and unwrap with PKCS#1 v1.5 padding is disallowed after December 31, 2023.
Therefore, support for these end on January 1, 2024 in our Federal Information Processing Standard (FIPS) mode clusters. Support for these remain for clusters in non-FIPs mode.

This guidance applies to the following cryptographic operations:

- Triple DES key generation
  - `CKM_DES3_KEY_GEN` for the PKCS#11 Library
  - `DESede` Keygen for the JCE Provider
  - `genSymKey` with `-t=21` for the KMU

- Encryption with Triple DES keys (note: decrypt operations are allowed)
  - For the PKCS #11 Library: `CKM_DES3_CBC` encrypt, `CKM_DES3_CBC_PAD` encrypt, and `CKM_DES3_ECB` encrypt
  - For the JCE Provider: `DESede/CBC/PKCS5Padding` encrypt, `DESede/CBC/NoPadding` encrypt, `DESede/ECB/Padding` encrypt, and `DESede/ECB/NoPadding` encrypt

- RSA key wrap, unwrap, encrypt, and decrypt with PKCS#1 v1.5 padding
  - `CKM_RSA_PKCS` wrap, unwrap, encrypt, and decrypt for the PKCS#11 SDK
  - `RSA/ECB/PKCS1Padding` wrap, unwrap, encrypt, and decrypt for the JCE SDK
  - `wrapKey` and `unWrapKey` with `-m 12` for the KMU (note `12` is the value for mechanism `RSA_PKCS`)

[1] For details on this change, refer to Table 1 and Table 5 in [Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf").
