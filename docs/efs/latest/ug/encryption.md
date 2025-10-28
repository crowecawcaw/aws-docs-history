# Data encryption in Amazon EFS

Amazon EFS provides comprehensive encryption capabilities to protect your data both at rest and
in transit.

- **Encryption at rest** – Encrypts data stored on your
  file system.
- **Encryption in transit** – Encrypts data as it travels
  between your clients and the file system.
  If your organization is subject to corporate or regulatory policies that require
  encryption of data and metadata, we recommend creating a file system that is encrypted at rest
  and mounting your file system using encryption of data in transit.

###### Topics

- [Encrypting data at rest](encryption-at-rest.md "encryption-at-rest.md")
- [Encrypting data in transit](encryption-in-transit.md "encryption-in-transit.md")
- [Using AWS KMS keys for Amazon EFS](EFSKMS.md "EFSKMS.md")
- [Troubleshooting encryption](troubleshooting-efs-encryption.md "troubleshooting-efs-encryption.md")
