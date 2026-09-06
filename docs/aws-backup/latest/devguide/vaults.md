

# Backup vaults
<a name="vaults"></a>

In AWS Backup, a *backup vault* is a container that stores and organizes your backups.

When creating a backup vault, you must specify the AWS Key Management Service (AWS KMS) encryption key that encrypts some of the backups placed in this vault. Encryption for other backups is managed by their source AWS services. For more information about encryption, see the chart in [Encryption for backups in AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html).

The following sections provide an overview of how to manage your backup vaults in AWS Backup.

**Topics**
+ [Backup vault creation and deletion](create-a-vault.md)
+ [Logically air-gapped vault](logicallyairgappedvault.md)
+ [Vault access policies](create-a-vault-access-policy.md)
+ [AWS Backup Vault Lock](vault-lock.md)