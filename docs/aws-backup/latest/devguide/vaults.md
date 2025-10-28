# Backup vaults

In AWS Backup, a _backup vault_ is a container that stores and organizes your
backups.

When creating a backup vault, you must specify the AWS Key Management Service (AWS KMS) encryption key that
encrypts some of the backups placed in this vault. Encryption for other backups is managed by
their source AWS services. For more information about encryption, see the chart in [Encryption for backups
in AWS](encryption.md "encryption.md").

The following sections provide an overview of how to manage your backup vaults in AWS Backup.

###### Topics

- [Backup vault creation and deletion](create-a-vault.md "create-a-vault.md")
- [Logically air-gapped vault](logicallyairgappedvault.md "logicallyairgappedvault.md")
- [Vault access policies](create-a-vault-access-policy.md "create-a-vault-access-policy.md")
- [AWS Backup Vault Lock](vault-lock.md "vault-lock.md")
