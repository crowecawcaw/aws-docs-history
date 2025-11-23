# Data protection in AWS Key Management Service

AWS Key Management Service stores and protects your encryption keys to make them highly available while
providing you with strong and flexible access control.

###### Topics

- [Protecting key material](#encryption-key-mgmt "#encryption-key-mgmt")
- [Data encryption](#data-encryption "#data-encryption")
- [Internetwork traffic privacy](#inter-network-privacy "#inter-network-privacy")

## Protecting key material

By default, AWS KMS generates and protects the cryptographic key material for KMS keys. In
addition, AWS KMS offers options for key material that is created and protected outside of
AWS KMS.

### Protecting key material generated in AWS KMS

When you create a KMS key, by default, AWS KMS generates and protects the cryptographic
material for the KMS key.

To safeguard key material for KMS keys, AWS KMS relies on a distributed fleet of [FIPS 140-3 Security Level 3–validated](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884") hardware
security modules (HSMs). Each AWS KMS HSM is a dedicated, standalone hardware appliance
designed to provide dedicated cryptographic functions to meet the security and scalability
requirements of AWS KMS. (The HSMs that AWS KMS uses in China Regions are certified by [OSCCA](https://www.oscca.gov.cn/ "https://www.oscca.gov.cn/") and comply with all pertinent Chinese regulations, but are
not validated under the FIPS 140-3 Cryptographic Module Validation Program.)

The key material for a KMS key is encrypted by default when it is generated in the
HSM. The key material is decrypted only within HSM volatile memory and only for the few
milliseconds that it takes to use it in a cryptographic operation. Whenever the key material
is not in active use, it is encrypted within the HSM and transferred to [highly durable](../cryptographic-details/durability-protection.md "../cryptographic-details/durability-protection.md")
(99.999999999%), low-latency persistent storage where it remains separate and isolated from
the HSMs. Plaintext key material never leaves the HSM [security boundary](../cryptographic-details/internal-communication-security.md#hsm-security-boundary "../cryptographic-details/internal-communication-security.md#hsm-security-boundary"); it is never written to disk or persisted in any storage
medium. (The only exception is the public key of an asymmetric key pair, which is not
secret.)

AWS asserts as a fundamental security principle that there is no human interaction
with plaintext cryptographic key material of any type in any AWS service. There is no
mechanism for anyone, including AWS service operators, to view, access, or export
plaintext key material. This principle applies even during catastrophic failures and
disaster recovery events. Plaintext customer key material in AWS KMS is used for cryptographic
operations within AWS KMS FIPS 140-3 validated HSMs only in response to authorized requests made to
the service by the customer or their delegate.

For [customer managed keys](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key"), the AWS account that creates the
key is the sole and non-transferable owner of the key. The owning account has complete and
exclusive control over the authorization policies that control access to the key. For
AWS managed keys, the AWS account has complete control over the IAM policies that
authorize requests to the AWS service.

### Protecting key material generated outside of

AWS KMS

AWS KMS provides alternatives to key material generated in AWS KMS.

[Custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview"), an optional AWS KMS
feature, let you create KMS keys backed by key material that is generated and used outside
of AWS KMS. KMS keys in [AWS CloudHSM key stores](keystore-cloudhsm.md "keystore-cloudhsm.md") are backed
by keys in AWS CloudHSM hardware security modules that you control. These HSMs are certified at
[FIPS
140-2 Security Level 3 or 140-3 Security Level 3](../../../cloudhsm/latest/userguide/compliance.md "../../../cloudhsm/latest/userguide/compliance.md"). KMS keys in [external
key stores](keystore-external.md "keystore-external.md") are backed by keys in an external key manager that you control and
manage outside of AWS, such as a physical HSM in your private data center.

Another optional feature lets you [import the key
material](importing-keys.md "importing-keys.md") for a KMS key. To protect imported key material while it is in transit
to AWS KMS, you encrypt the key material using a public key from an RSA key pair generated in
an AWS KMS HSM. The imported key material is decrypted in an AWS KMS HSM and re-encrypted under
a symmetric key in the HSM. Like all AWS KMS key material, plaintext imported key material
never leaves the HSMs unencrypted. However, the customer who provided the key material is
responsible for secure use, durability, and maintenance of the key material outside of
AWS KMS.

## Data encryption

The data in AWS KMS consists of AWS KMS keys and the
encryption key material they represent. This key material exists in plaintext only within
AWS KMS hardware security modules (HSMs) and only when in use. Otherwise, the key material is
encrypted and stored in durable persistent storage.

The key material that AWS KMS generates for KMS keys never leaves the boundary of AWS KMS
HSMs unencrypted. It is not exported or transmitted in any AWS KMS API operations. The exception
is for [multi-Region keys](multi-region-keys-overview.md "multi-region-keys-overview.md"), where AWS KMS uses a
cross-Region replication mechanism to copy the key material for a multi-Region key from an HSM
in one AWS Region to an HSM in a different AWS Region. For details, see [Replication process for multi-Region
keys](../cryptographic-details/replicate-key-details.md "../cryptographic-details/replicate-key-details.md") in AWS Key Management Service Cryptographic Details.

###### Topics

- [Encryption at rest](#encryption-at-rest "#encryption-at-rest")
- [Encryption in transit](#encryption-in-transit "#encryption-in-transit")

### Encryption at rest

AWS KMS generates key material for AWS KMS keys in [FIPS
140-3 Security Level 3](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884")–compliant hardware security modules (HSMs). The only
exception is China Regions, where the HSMs that AWS KMS uses to generate KMS keys comply
with all pertinent Chinese regulations, but are not validated under the FIPS 140-3
Cryptographic Module Validation Program. When not in use, key material is encrypted by an
HSM key and written to durable, persistent storage. The key material for KMS keys and the
encryption keys that protect the key material never leave the HSMs in plaintext form.

Encryption and management of key material for KMS keys is handled entirely by
AWS KMS.

For more details, see [Working with
AWS KMS keys](../cryptographic-details/kms-keys.md "../cryptographic-details/kms-keys.md") in AWS Key Management Service Cryptographic Details.

### Encryption in transit

Key material that AWS KMS generates for KMS keys is never exported or transmitted in
AWS KMS API operations. AWS KMS uses [key identifiers](concepts.md#key-id "concepts.md#key-id") to represent
the KMS keys in API operations. Similarly, key material for KMS keys in AWS KMS [custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview") is non-exportable and never
transmitted in AWS KMS or AWS CloudHSM API operations.

However, some AWS KMS API operations return [data keys](data-keys.md "data-keys.md").
Also, customers can use API operations to [import key
material](importing-keys.md "importing-keys.md") for selected KMS keys.

All AWS KMS API calls must be signed and transmitted using Transport Layer Security
(TLS). AWS KMS requires TLS 1.2 and recommends TLS 1.3 in all regions. AWS KMS also supports hybrid post-quantum TLS for
AWS KMS service endpoints in all regions, except China Regions. AWS KMS does not support hybrid post-quantum TLS
for FIPS endpoints in AWS GovCloud (US). Calls to
AWS KMS also require a modern cipher suite that supports _perfect
forward secrecy_, which means that compromise of any secret, such as a private
key, does not also compromise the session key.

If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a
command line interface or an API, use a FIPS endpoint. To use standard AWS KMS
endpoints or AWS KMS FIPS endpoints, clients
must support TLS 1.2 or later. For more information
about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/"). For a list of AWS KMS FIPS
endpoints, see [AWS Key Management Service endpoints and quotas](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md") in
the AWS General Reference.

Communications between AWS KMS service hosts and HSMs are protected using Elliptic Curve
Cryptography (ECC) and Advanced Encryption Standard (AES) in an authenticated encryption
scheme. For more details, see [Internal communication
security](../cryptographic-details/internal-communication-security.md "../cryptographic-details/internal-communication-security.md") in AWS Key Management Service Cryptographic Details.

## Internetwork traffic privacy

AWS KMS supports an AWS Management Console and a set of API operations that enable you to create and
manage AWS KMS keys and use them in cryptographic operations.

AWS KMS supports two network connectivity options from your private network to AWS.

- An IPSec VPN connection over the internet
- [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/"), which links your
  internal network to an Direct Connect location over a standard Ethernet fiber-optic
  cable.

All AWS KMS API calls must be signed and be transmitted using Transport Layer Security
(TLS). The calls also require a modern cipher suite that supports [perfect forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy "https://en.wikipedia.org/wiki/Forward_secrecy"). Traffic
to the hardware security modules (HSMs) that store key material for KMS keys is permitted
only from known AWS KMS API hosts over the AWS internal network.

To connect directly to AWS KMS from your virtual private cloud (VPC) without sending traffic
over the public internet, use VPC endpoints, powered by [AWS PrivateLink](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md"). For more information, see [Connect to AWS KMS through a VPC endpoint](kms-vpc-endpoint.md "kms-vpc-endpoint.md").

AWS KMS also supports a [hybrid post-quantum key exchange](pqtls.md "pqtls.md") option
for the Transport Layer Security (TLS) network encryption protocol. You can use this option
with TLS when you connect to AWS KMS API endpoints.
