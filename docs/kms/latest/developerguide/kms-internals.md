# AWS KMS internal operations

AWS Key Management Service (AWS KMS) provides cryptographic keys and operations secured by [FIPS 140-3 Security Level 3 validated hardware
security modules (HSM)](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884") scaled for the cloud. AWS KMS keys and
functionality are used by multiple AWS cloud services, and you can use them to protect
data in your applications. This technical guide provides details on the cryptographic
operations that are run within AWS when you use AWS KMS.

AWS KMS internals are required to scale and secure HSMs for a globally distributed key
management service.

###### Topics

- [Domains and domain state](domains-and-domain-state.md "domains-and-domain-state.md")
- [Internal communication security](internal-communication-security.md "internal-communication-security.md")
- [Replication process for multi-Region keys](replicate-key-details.md "replicate-key-details.md")
- [Durability protection](durability-protection.md "durability-protection.md")
