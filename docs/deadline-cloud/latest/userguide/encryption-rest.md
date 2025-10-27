# Encryption at rest

AWS Deadline Cloud protects sensitive data by encrypting it at rest using encryption keys stored in
[AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms "https://aws.amazon.com/kms"). Encryption at rest is available
in all AWS Regions where Deadline Cloud is available.

Encrypting data means sensitive data saved on disks isn't readable by a user or
application without a valid key. Only a party with a valid managed key can decrypt the
data.

For information about how Deadline Cloud uses AWS KMS for encrypting data at rest, see [Key management](key-management.md "key-management.md").
