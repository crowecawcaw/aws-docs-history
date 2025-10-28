# Data encryption in Amazon SQS

Data protection refers to protecting data while in-transit (as it travels to and from
Amazon SQS) and at rest (while it is stored on disks in Amazon SQS data centers). You can protect
data in transit using Secure Sockets Layer (SSL) or client-side encryption. By default,
Amazon SQS stores messages and files using disk encryption. You can protect data at rest by
requesting Amazon SQS to encrypt your messages before saving them to the encrypted file
system in its data centers. Amazon SQS recommends using SSE for optimized data
encryption.

###### Topics

- [Encryption at rest](sqs-server-side-encryption.md "sqs-server-side-encryption.md")
- [Key management](sqs-key-management.md "sqs-key-management.md")
