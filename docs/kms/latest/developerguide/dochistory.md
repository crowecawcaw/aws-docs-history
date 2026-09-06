

# Document history
<a name="dochistory"></a>

This topic describes significant updates to the *AWS Key Management Service Developer Guide*.

**Topics**
+ [Recent updates](#recent-updates)
+ [Earlier updates](#earlier-updates)

## Recent updates
<a name="recent-updates"></a>

The following table describes significant changes to this documentation since January 2018. In addition to major changes listed here, we also update the documentation frequently to improve the descriptions and examples, and to address the feedback that you send to us. To be notified about significant changes, subscribe to the RSS feed.

You might need to scroll horizontally or vertically to see all of the data in this table.

| Change | Description | Date | 
| --- |--- |--- |
| [Service principal grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) | AWS KMS now supports creating grants for AWS service principals. You can use the new `GranteeServicePrincipal` and `RetiringServicePrincipal` parameters in the `CreateGrant` operation to specify a service principal as the grantee or retiring principal of a grant. This release also introduces the `SourceArn` grant constraint, which restricts grant permissions to requests made on behalf of a specific AWS resource. Three new condition keys are available for `CreateGrant` requests: `kms:GranteeServicePrincipal`, `kms:RetiringServicePrincipal`, and `kms:GrantConstraintSourceArn`. For more information, see [Grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html). | March 6, 2026 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-on-demand.html) | AWS KMS supports on-demand rotation of symmetric-encryption, multi-region keys with imported key material. | November 26, 2025 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/pqtls.html#pqtls-verify) | AWS KMS supports new `keyExchange` field in the `tlsDetails` section of CloudTrail events. | November 24, 2025 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose-key-spec.html#key-spec-ecc) | AWS KMS supports new `KeySpec` ECC\_NIST\_EDWARDS25519. | November 7, 2025 | 
| [Dual-stack support](https://docs.aws.amazon.com/kms/latest/developerguide/ipv6-kms.html) | AWS KMS supports dual-stack. | June 18, 2025 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/mldsa.html) | Adds support for Module-Lattice Digital Signature Algorithm (ML-DSA) post-quantum cryptographic signatures.  | June 13, 2025 | 
| [Imported key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/list-rotations.html) | You can perform on-demand rotation of symmetric-encryption KMS keys with imported key material (`EXTERNAL` origin). | June 5, 2025 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview) | Added support for multi-Region KMS keys in China Regions. | November 21, 2024 | 
| [AWS managed policy update](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-auth-slr) | Updated the **AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy** service-linked role by adding a statement ID (`Sid`) to the managed policy with policy version v2. | November 21, 2024 | 
| [Quota change](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) | Increased the default request rate for [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html) and [DeleteImportedKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteImportedKeyMaterial.html) requests. | July 23, 2024 | 
| [Quota change](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) | Increased the default cryptographic operations request rate for symmetric encryption KMS keys, RSA KMS keys, and ECC and SM2 KMS keys. | July 8, 2024 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) | Added new `KeyUsage` type `KEY_AGREEMENT` for NIST-recommended elliptic curve (ECC) and SM2 (China Regions only) KMS keys and added support to [derive shared secrets](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html). | June 13, 2024 | 
| [Updates to key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) | Added support for custom rotation periods for automatic key rotations, on-demand key rotations, and visibility into your key material rotations. | April 12, 2024 | 
| [Updates to managed policy](https://docs.aws.amazon.com/kms/latest/developerguide/authorize-key-store.html#about-key-store-slr) | Added new permissions to `AWSKeyManagementServiceCustomKeyStoresServiceRolePolicy` that allow AWS KMS to monitor changes in the VPC that contains your AWS CloudHSM cluster so that AWS KMS can provide clear error messages in the case of failures. | November 10, 2023 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) | Added support for the `DryRun` API parameter. | July 5, 2023 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) | Added support for importing key material for all types of AWS KMS keys, except custom key stores.  | June 5, 2023 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/services-nitro-enclaves.html) | Updates to AWS KMS APIs for Nitro Enclaves | March 10, 2023 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-get-public-key-and-token.html) | The `RSAES_PKCS1_V1_5` wrapping algorithm is deprecated. AWS KMS will end all support for `RSAES_PKCS1_V1_5` by October 1, 2023 pursuant to [cryptographic key management guidance](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf) from the National Institute of Standards and Technology (NIST). We recommend that you begin using a different wrapping algorithm immediately. | February 28, 2023 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) | Added support for External key stores, a feature that lets you protect your AWS resources using cryptographic keys outside of AWS.  | November 29, 2022 | 
| [Quota change](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) | Increased the AWS KMS keys resource quota to 100,000 KMS keys in each account and Region. | July 8, 2022 | 
| [Feature update](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) | Added support for HMAC KMS keys in more AWS Regions | July 8, 2022 | 
| [New topic](https://docs.aws.amazon.com/kms/latest/developerguide/disaster-recovery-resiliency.html) | Added the [Resilience in AWS Key Management Service topic](https://docs.aws.amazon.com/kms/latest/developerguide/disaster-recovery-resiliency.html) to the Security chapter of the AWS KMS Developer Guide. | June 14, 2022 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) | Added support for AWS KMS keys and API operations that generate and verify HMAC codes. | April 19, 2022 | 
| [Documentation change](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-types) | Replace the term *customer master key (CMK)* with *AWS KMS key* and *KMS key*. | August 30, 2021 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) | Added support for [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html), a set of interoperable KMS keys in different Regions that have the same key ID and key material. You can use multi-Region keys to encrypt data in one Region and decrypt data in a different Region. | June 8, 2021 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) | Added support for attribute based access control (ABAC). You can use tags and aliases to control access to your AWS KMS keys. | December 17, 2020 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html#vpce-policy) | Added support for VPC endpoint policies. | July 9, 2020 | 
| [New content](https://docs.aws.amazon.com/kms/latest/developerguide/kms-security.html) | Explains the security properties of AWS KMS. | June 18, 2020 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) | Added support for asymmetric AWS KMS keys and asymmetric data keys. | November 25, 2019 | 
| [Updated feature](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-viewing.html) | You can view the key policy of AWS managed keys in the AWS KMS console. This feature used to be limited to customer managed keys. | November 15, 2019 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/pqtls.html) | Explains how to use [hybrid post-quantum key exchange](https://docs.aws.amazon.com/kms/latest/developerguide/pqtls.html) algorithms in TLS for your calls to AWS KMS. | November 4, 2019 | 
| [Quota change](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) | Increased the resource quotas for some APIs that manage KMS keys. | September 18, 2019 | 
| [Quota change](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) | Changed the resource quotas for KMS keys, aliases, and grants per KMS key. | March 27, 2019 | 
| [Quota change](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#rps-key-stores) | Changed the shared per-second request quota for cryptographic operations that use AWS KMS keys in a custom key store. | March 7, 2019 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) | Explains how to create and manage AWS KMS [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html). Each key store is backed by an AWS CloudHSM cluster that you own and control. | November 26, 2018 | 
| [New console](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-keys-console) | Explains how to use the new AWS KMS console, which is independent of the IAM console. The original console, and instructions for using it, will remain available for a brief period to give you time to familiarize yourself with the new console. | November 7, 2018 | 
| [Quota change](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second) | Changed the shared [request quota](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second) for use of AWS KMS keys. | August 21, 2018 | 
| [New content](https://docs.aws.amazon.com/kms/latest/developerguide/services-secrets-manager.html) | Explains [how AWS Secrets Manager uses AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-secrets-manager.html) keys to encrypt the secret value in a secret. | July 13, 2018 | 
| [New content](#dochistory) | Explains how DynamoDB uses AWS KMS AWS KMS keys to support its server-side encryption option. | May 23, 2018 | 
| [New feature](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html) | Explains how to [use a private endpoint in your VPC](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html) to connect directly to AWS KMS, instead of connecting over the internet. | January 22, 2018 | 

## Earlier updates
<a name="earlier-updates"></a>

The following table describes the important changes to the AWS Key Management Service Developer Guide prior to 2018.

You might need to scroll horizontally or vertically to see all of the data in this table.


| Change | Description | Date | 
| --- | --- | --- | 
| New content | Added documentation about [Tags in AWS KMS](tagging-keys.md). | February 15, 2017 | 
| New content | Added documentation about [Monitor AWS KMS keys](monitoring-overview.md) and [Monitor KMS keys with Amazon CloudWatch](monitoring-cloudwatch.md). | August 31, 2016 | 
| New content | Added documentation about [Imported key material](importing-keys.md). | August 11, 2016 | 
| New content | Added the following documentation: [IAM policies](iam-policies.md), [Permissions reference](kms-api-permissions-reference.md), and [Condition keys](policy-conditions.md). | July 5, 2016 | 
| Update | Updated portions of the documentation in the [KMS key access and permissions](control-access.md) chapter. | July 5, 2016 | 
| Update | Updated the [Quotas](limits.md) page to reflect new default quotas. | May 31, 2016 | 
| Update | Updated the [Quotas](limits.md) page to reflect new default quotas, and updated the [grant token](grants.md#grant_token) documentation to improve clarity and accuracy. | April 11, 2016 | 
| New content | Added documentation about [Allowing multiple IAM principals to access a KMS key](iam-policies.md#key-policy-modifying-multiple-iam-users) and [Using the IP address condition](conditions-aws.md#conditions-aws-ip-address). | February 17, 2016 | 
| Update | Updated the [Key policies in AWS KMS](key-policies.md) and [Change a key policy](key-policy-modifying.md) pages to improve clarity and accuracy. | February 17, 2016 | 
| Update | Updated the Managing KMS keys topic pages to improve clarity. | January 5, 2016 | 
| New content | Added documentation about CloudTrail. | November 18, 2015 | 
| New content | Added instructions for [Change a key policy](key-policy-modifying.md). | November 18, 2015 | 
| Update | Updated the documentation about How Amazon Relational Database Service uses AWS KMS. | November 18, 2015 | 
| New content | Added documentation about Amazon WorkSpaces. | November 6, 2015 | 
| Update | Updated the [Key policies in AWS KMS](key-policies.md) page to improve clarity. | October 22, 2015 | 
| New content | Added documentation about [Delete an AWS KMS key](deleting-keys.md), including supporting documentation about [Create an alarm](deleting-keys-creating-cloudwatch-alarm.md) and [Determine past usage of a KMS key](monitoring-keys-determining-usage.md). | October 15, 2015 | 
| New content | Added documentation about [Determining access to AWS KMS keys](determining-access.md). | October 15, 2015 | 
| New content | Added documentation about [Key states of AWS KMS keys](key-state.md). | October 15, 2015 | 
| New content | Added documentation about Amazon Simple Email Service. | October 1, 2015 | 
| Update | Updated the [Quotas](limits.md) page to explain the new request quotas. | August 31, 2015 | 
| New content | Added information about the charges for using AWS KMS. See [AWS KMS Pricing](overview.md#pricing). | August 14, 2015 | 
| New content | Added request quotas to the AWS KMS [Quotas](limits.md). | June 11, 2015 | 
| New content | Added a new Java code sample demonstrating use of the [`UpdateAlias`](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateAlias.html) operation. | June 1, 2015 | 
| Update | Moved the [AWS Key Management Service regions table](https://docs.aws.amazon.com/general/latest/gr/rande.html#kms_region) to the AWS General Reference. | May 29, 2015 | 
| New content | Added documentation about [How Amazon EMR uses AWS KMS](services-emr.md). | January 28, 2015 | 
| New content | Added documentation about Amazon WorkMail. | January 28, 2015 | 
| New content | Added documentation about How Amazon Relational Database Service uses AWS KMS. | January 6, 2015 | 
| New content | Added documentation about Amazon Elastic Transcoder. | November 24, 2014 | 
| New guide | Introduced the AWS Key Management Service Developer Guide. | November 12, 2014 | 