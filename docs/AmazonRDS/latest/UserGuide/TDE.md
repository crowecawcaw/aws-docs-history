# Backing up and restoring TDE certificates on RDS for SQL Server

RDS for SQL Server provides stored procedures for backing up, restoring, and dropping TDE certificates. RDS for SQL Server also provides a function
for viewing restored user TDE certificates.

User TDE certificates are used to restore databases to RDS for SQL Server that are on-premises and have TDE turned on. These certificates
have the prefix `UserTDECertificate_`. After restoring databases, and before making them available to use,
RDS modifies the databases that have TDE turned on to use RDS-generated TDE certificates. These certificates have the prefix
`RDSTDECertificate`.

User TDE certificates remain on the RDS for SQL Server DB instance, unless you drop them using the `rds_drop_tde_certificate`
stored procedure. For more information, see [Dropping restored TDE certificates](#TDE.BackupRestoreRDS.Drop "#TDE.BackupRestoreRDS.Drop").

You can use a user TDE certificate to restore other databases from the source DB
instance. The databases to restore must use the same TDE certificate and have TDE turned
on. You don't have to import (restore) the same certificate again.

###### Topics

- [Prerequisites](#TDE.BackupRestoreRDS.Prereqs "#TDE.BackupRestoreRDS.Prereqs")
- [Limitations](#TDE.Limitations "#TDE.Limitations")
- [Backing up a TDE certificate](#TDE.BackupRestoreRDS.Backup "#TDE.BackupRestoreRDS.Backup")
- [Restoring a TDE certificate](#TDE.BackupRestoreRDS.Restore "#TDE.BackupRestoreRDS.Restore")
- [Viewing restored TDE certificates](#TDE.BackupRestoreRDS.Show "#TDE.BackupRestoreRDS.Show")
- [Dropping restored TDE certificates](#TDE.BackupRestoreRDS.Drop "#TDE.BackupRestoreRDS.Drop")

## Prerequisites

Before you can back up or restore TDE certificates on RDS for SQL Server, make sure to perform the following tasks. The first three
are described in [Setting up for native backup and restore](SQLServer.Procedural.Importing.Native.md "SQLServer.Procedural.Importing.Native.md").

1. Create Amazon S3 buckets for storing files to back up and restore.

We recommend that you use separate buckets for database backups and for TDE certificate backups. 2. Create an IAM role for backing up and restoring files.

The IAM role must be both a user and an administrator for the AWS KMS key.

In addition to the permissions required for SQL Server native backup and restore, the IAM role also requires the
following permissions:

    * `s3:GetBucketAcl`, `s3:GetBucketLocation`, and `s3:ListBucket` on the S3
     bucket resource
    * `s3:ListAllMyBuckets` on the `*` resource

3. Add the `SQLSERVER_BACKUP_RESTORE` option to an option group on your DB instance.

This is in addition to the `TRANSPARENT_DATA_ENCRYPTION` (`TDE`) option. 4. Make sure that you have a symmetric encryption KMS key. You have the following options:

    * If you have an existing KMS key in your account, you can use it. No further action is necessary.
    * If you don't have an existing symmetric encryption KMS key in your account, create a KMS key by
     following the instructions in [Creating keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the
     *AWS Key Management Service Developer Guide*.

5. Enable Amazon S3 integration to transfer files between the DB instance and Amazon S3.

For more information on enabling Amazon S3 integration, see [Integrating an Amazon RDS for SQL Server
DB instance with Amazon S3](User.SQLServer.Options.md "User.SQLServer.Options.md").

## Limitations

Using stored procedures to back up and restore TDE certificates has the following limitations:

- Both the `SQLSERVER_BACKUP_RESTORE` and
  `TRANSPARENT_DATA_ENCRYPTION` (`TDE`) options must
  be added to the option group that you associated with your DB
  instance.
- TDE certificate backup and restore aren't supported on Multi-AZ DB instances.
- Canceling TDE certificate backup and restore tasks isn't supported.
- You can't use a user TDE certificate for TDE encryption of any other
  database on your RDS for SQL Server DB instance. You can use it to restore only other
  databases from the source DB instance that have TDE turned on and that use
  the same TDE certificate.
- You can drop only user TDE certificates.
- The maximum number of user TDE certificates supported on RDS is 10. If the number exceeds 10, drop unused TDE
  certificates and try again.
- The certificate name can't be empty or null.
- When restoring a certificate, the certificate name can't include the keyword
  `RDSTDECERTIFICATE`, and must start with the `UserTDECertificate_`
  prefix.
- The `@certificate_name` parameter can include only the following characters: a-z, 0-9, @, $, #, and
  underscore (\_).
- The file extension for `@certificate_file_s3_arn` must be .cer
  (case-insensitive).
- The file extension for `@private_key_file_s3_arn` must be .pvk
  (case-insensitive).
- The S3 metadata for the private key file must include the
  `x-amz-meta-rds-tde-pwd` tag. For more information, see
  [Backing up and restoring TDE certificates for on-premises databases](TDE.md "TDE.md").
- RDS for SQL Server does not support using cross-account keys for TDE.

## Backing up a TDE certificate

To back up TDE certificates, use the `rds_backup_tde_certificate`
stored procedure. It has the following syntax.

```
EXECUTE msdb.dbo.rds_backup_tde_certificate
    @certificate_name='UserTDECertificate_`certificate_name` | RDSTDECertificate`timestamp`',
    @certificate_file_s3_arn='arn:aws:s3:::`bucket_name`/`certificate_file_name.cer`',
    @private_key_file_s3_arn='arn:aws:s3:::`bucket_name`/`key_file_name.pvk`',
    @kms_password_key_arn='arn:aws:kms:`region`:`account-id`:key/`key-id`',
    [@overwrite_s3_files=`0|1`];
```

The following parameters are required:

- `@certificate_name` – The name of the TDE certificate to back up.
- `@certificate_file_s3_arn` – The destination Amazon
  Resource Name (ARN) for the certificate backup file in Amazon S3.
- `@private_key_file_s3_arn` – The destination S3 ARN of the private key file that secures the TDE
  certificate.
- `@kms_password_key_arn` – The ARN of the symmetric KMS key used to encrypt the private key
  password.

The following parameter is optional:

- `@overwrite_s3_files` – Indicates whether to overwrite
  the existing certificate and private key files in S3:
  - `0` – Doesn't overwrite the existing files. This value is the default.

  Setting `@overwrite_s3_files` to 0 returns an error if a file already exists.
  - `1` – Overwrites an existing file that has the specified name, even if it isn't a
    backup file.

###### Example of backing up a TDE certificate

```
EXECUTE msdb.dbo.rds_backup_tde_certificate
    @certificate_name='RDSTDECertificate20211115T185333',
    @certificate_file_s3_arn='arn:aws:s3:::`TDE_certs`/`mycertfile.cer`',
    @private_key_file_s3_arn='arn:aws:s3:::`TDE_certs`/`mykeyfile.pvk`',
    @kms_password_key_arn='arn:aws:kms:`us-west-2`:`123456789012`:key/`AKIAIOSFODNN7EXAMPLE`',
    @overwrite_s3_files=`1`;
```

## Restoring a TDE certificate

You use the `rds_restore_tde_certificate` stored procedure to restore
(import) user TDE certificates. It has the following syntax.

```
EXECUTE msdb.dbo.rds_restore_tde_certificate
    @certificate_name='UserTDECertificate_`certificate_name`',
    @certificate_file_s3_arn='arn:aws:s3:::`bucket_name`/`certificate_file_name.cer`',
    @private_key_file_s3_arn='arn:aws:s3:::`bucket_name`/`key_file_name.pvk`',
    @kms_password_key_arn='arn:aws:kms:`region`:`account-id`:key/`key-id`';
```

The following parameters are required:

- `@certificate_name` – The name of the TDE certificate to restore. The name must start with the
  `UserTDECertificate_` prefix.
- `@certificate_file_s3_arn` – The S3 ARN of the backup file used to restore the TDE
  certificate.
- `@private_key_file_s3_arn` – The S3 ARN of the private key backup file of the TDE certificate to
  be restored.
- `@kms_password_key_arn` – The ARN of the symmetric KMS key used to encrypt the private key
  password.

###### Example of restoring a TDE certificate

```
EXECUTE msdb.dbo.rds_restore_tde_certificate
    @certificate_name='UserTDECertificate_`myTDEcertificate`',
    @certificate_file_s3_arn='arn:aws:s3:::`TDE_certs`/`mycertfile.cer`',
    @private_key_file_s3_arn='arn:aws:s3:::`TDE_certs`/`mykeyfile.pvk`',
    @kms_password_key_arn='arn:aws:kms:`us-west-2`:`123456789012`:key/`AKIAIOSFODNN7EXAMPLE`';
```

## Viewing restored TDE certificates

You use the `rds_fn_list_user_tde_certificates` function to view
restored (imported) user TDE certificates. It has the following syntax.

```
SELECT * FROM msdb.dbo.rds_fn_list_user_tde_certificates();
```

The output resembles the following. Not all columns are shown here.

|                               |                  |                |                                |                       |                                                   |                                               |                       |                               |                               |                            |
| ----------------------------- | ---------------- | -------------- | ------------------------------ | --------------------- | ------------------------------------------------- | --------------------------------------------- | --------------------- | ----------------------------- | ----------------------------- | -------------------------- |
| `name`                        | `certificate_id` | `principal_id` | `pvt_key_encryption_type_desc` | `issuer_name`         | `cert_serial_number`                              | `thumbprint`                                  | `subject`             | `start_date`                  | `expiry_date`                 | `pvt_key_last_backup_date` |
| `UserTDECertificate_tde_cert` | `343`            | `1`            | `ENCRYPTED_BY_MASTER_KEY`      | `AnyCompany Shipping` | `79 3e 57 a3 69 fd 1d 9e 47 2c 32 67 1d 9c ca af` | `0x6BB218B34110388680B FE1BA2D86C695096485B5` | `AnyCompany Shipping` | `2022-04-05 19:49:45.0000000` | `2023-04-05 19:49:45.0000000` | `NULL`                     |

## Dropping restored TDE certificates

To drop restored (imported) user TDE certificates that you aren't using, use
the `rds_drop_tde_certificate` stored procedure. It has the following
syntax.

```
EXECUTE msdb.dbo.rds_drop_tde_certificate @certificate_name='UserTDECertificate_`certificate_name`';
```

The following parameter is required:

- `@certificate_name` – The name of the TDE certificate to drop.

You can drop only restored (imported) TDE certificates. You can't drop RDS-created certificates.

###### Example of dropping a TDE certificate

```
EXECUTE msdb.dbo.rds_drop_tde_certificate @certificate_name='UserTDECertificate_`myTDEcertificate`';
```
