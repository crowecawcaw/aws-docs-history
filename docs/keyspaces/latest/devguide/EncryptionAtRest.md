# Encryption at rest in Amazon Keyspaces

Amazon Keyspaces (for Apache Cassandra) _encryption at rest_ provides enhanced security by
encrypting all your data at rest using encryption keys stored in [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). This functionality helps reduce
the operational burden and complexity involved in protecting sensitive data. With encryption at
rest, you can build security-sensitive applications that meet strict compliance and regulatory
requirements for data protection.

Amazon Keyspaces encryption at rest encrypts your data using 256-bit Advanced Encryption
Standard (AES-256). This helps secure your data from unauthorized access to the underlying
storage.

Amazon Keyspaces encrypts and decrypts the data in tables and streams transparently. Amazon Keyspaces uses
envelope encryption and a key hierarchy to protect data encryption keys. It integrates with AWS KMS
for storing and managing the root encryption key. For more information about the encryption
key hierarchy, see [Encryption at rest: How it works in Amazon Keyspaces](encryption.md "encryption.md"). For more information about AWS KMS concepts like envelope encryption, see
[AWS KMS management service concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in
the _AWS Key Management Service Developer Guide_.

When creating a new table, you can choose one of the following _AWS KMS keys
(KMS keys)_:

- AWS owned key – This is the default encryption type. The key is owned by Amazon Keyspaces
  (no additional charge).
- Customer managed key – This key is stored in your account and is created, owned, and
  managed by you. You have full control over the customer managed key (AWS KMS charges apply).
  Amazon Keyspaces automatically encrypts change data capture (CDC) streams with the same key as the
  underlying table. For more information about CDC, see [Working with change data capture (CDC) streams in Amazon Keyspaces](cdc.md "cdc.md").

You can switch between the AWS owned key and the customer managed key at any given time. You can
specify a customer managed key when you create a new table or change the KMS key of an existing table by
using the console or programmatically using CQL statements. To learn how, see [Encryption at rest: How to use customer managed
keys to encrypt tables in Amazon Keyspaces](encryption.md "encryption.md").

Encryption at rest using the default option of AWS owned keys is offered at no additional charge. However,
AWS KMS charges apply for customer managed keys. For more information
about pricing, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing").

Amazon Keyspaces encryption at rest is available in all AWS Regions, including the AWS China
(Beijing) and AWS China (Ningxia) Regions. For more
information, see [Encryption at rest: How it works in Amazon Keyspaces](encryption.md "encryption.md").

###### Topics

- [Encryption at rest: How it works in Amazon Keyspaces](encryption.md "encryption.md")
- [Encryption at rest: How to use customer managed
  keys to encrypt tables in Amazon Keyspaces](encryption.md "encryption.md")
