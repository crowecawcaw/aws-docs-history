# AWS DataSync encryption at rest

Because AWS DataSync is a transfer service, it generally doesn't manage your storage data
at rest. The storage services and systems that DataSync supports are responsible for
protecting data in that state. However, there is some service-related data that DataSync
manages at rest.

## What's encrypted?

The only data that DataSync handles at rest relates to the details it needs to complete
your transfer. DataSync stores the following data with full at-rest encryption in
Amazon DynamoDB:

- Task configurations (for example, details about the locations in your
  transfer).
- User credentials that allow your DataSync agent to authenticate with a
  location. These credentials are encrypted by using your agent's public keys.
  The agent can decrypt these keys as needed with its private keys.

For more information, see [DynamoDB
encryption at rest](../../../amazondynamodb/latest/developerguide/EncryptionAtRest.md "../../../amazondynamodb/latest/developerguide/EncryptionAtRest.md") in the _Amazon DynamoDB Developer
Guide_.

### Key management

You can't manage the encryption keys that DataSync uses to store information in
DynamoDB related to running your task. This information includes your task
configurations and the credentials that agents use to authenticate with a
storage location.

## What's not encrypted?

Though DataSync doesn’t control how your storage data is encrypted at rest, we still
recommend configuring your locations with the highest level of security that they
support. For example, you can encrypt objects with Amazon S3 managed encryption keys
(SSE-S3) or AWS Key Management Service (AWS KMS) keys (SSE-KMS).

Learn more about how AWS storage services encrypt data at rest:

- [Amazon S3](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md")
- [Amazon EFS](../../../efs/latest/ug/encryption-at-rest.md "../../../efs/latest/ug/encryption-at-rest.md")
- [Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/encryption-at-rest.md "../../../fsx/latest/WindowsGuide/encryption-at-rest.md")
- [Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/encryption-at-rest.md "../../../fsx/latest/LustreGuide/encryption-at-rest.md")
- [Amazon FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/encryption-rest.md "../../../fsx/latest/OpenZFSGuide/encryption-rest.md")
- [Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/encryption-at-rest.md "../../../fsx/latest/ONTAPGuide/encryption-at-rest.md")
