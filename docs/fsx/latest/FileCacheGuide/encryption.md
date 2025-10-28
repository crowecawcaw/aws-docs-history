# Data encryption in Amazon File Cache

Amazon File Cache supports two forms of data encryption for caches, encryption of
data at rest and encryption in transit. Encryption of data at rest is automatically
enabled when creating an Amazon File Cache cache. Encryption of data in transit is
automatically enabled when you access an Amazon File Cache cache from [Amazon EC2
instances](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit") that support this feature.

## When to use encryption

If your organization is subject to corporate or regulatory policies that require
encryption of data and metadata at rest, we recommend creating an encrypted
cache and mounting your cache using encryption of data in transit.

###### Topics

- [Encrypting data at rest](encryption-at-rest.md "encryption-at-rest.md")
- [Encrypting data in transit](encryption-in-transit.md "encryption-in-transit.md")
- [How Amazon File Cache uses AWS KMS](FileCacheKMS.md "FileCacheKMS.md")
