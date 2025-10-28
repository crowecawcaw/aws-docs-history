# Backing up and restoring TDE certificates for on-premises databases

You can back up TDE certificates for on-premises databases, then later restore them
to RDS for SQL Server. You can also restore an RDS for SQL Server TDE certificate to an on-premises DB
instance.

###### Note

RDS for SQL Server does not support using cross-account keys for TDE.

The following procedure backs up a TDE certificate and private key. The private key is encrypted using a data key
generated from your symmetric encryption KMS key.

###### To back up an on-premises TDE certificate

1. Generate the data key using the AWS CLI [generate-data-key](../../../cli/latest/reference/kms/generate-data-key.md "../../../cli/latest/reference/kms/generate-data-key.md") command.

```
aws kms generate-data-key \
    --key-id `my_KMS_key_ID` \
    --key-spec AES_256
```

The output resembles the following.

```
{
"CiphertextBlob": "AQIDAHimL2NEoAlOY6Bn7LJfnxi/OZe9kTQo/XQXduug1rmerwGiL7g5ux4av9GfZLxYTDATAAAAfjB8BgkqhkiG9w0B
BwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMyCxLMi7GRZgKqD65AgEQgDtjvZLJo2cQ31Vetngzm2ybHDc3d2vI74SRUzZ
2RezQy3sAS6ZHrCjfnfn0c65bFdhsXxjSMnudIY7AKw==",
"Plaintext": "`U/fpGtmzGCYBi8A2+0/9qcRQRK2zmG/aOn939ZnKi/0=`",
"KeyId": "arn:aws:kms:us-west-2:`123456789012`:key/`1234abcd-00ee-99ff-88dd-aa11bb22cc33`"
}
```

You use the plain text output in the next step as the private key password. 2. Back up your TDE certificate as shown in the following example.

```
BACKUP CERTIFICATE `myOnPremTDEcertificate` TO FILE = 'D:\`tde-cert-backup`.cer'
WITH PRIVATE KEY (
FILE = 'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\`cert-backup-key`.pvk',
ENCRYPTION BY PASSWORD = 'U/fpGtmzGCYBi8A2+0/9qcRQRK2zmG/aOn939ZnKi/0=');
```

3.  Save the certificate backup file to your Amazon S3 certificate bucket.
4.  Save the private key backup file to your S3 certificate bucket, with the following tag in the file's
    metadata:

        * Key – `x-amz-meta-rds-tde-pwd`
        * Value – The `CiphertextBlob` value from generating
         the data key, as in the following example.



        ```
        AQIDAHimL2NEoAlOY6Bn7LJfnxi/OZe9kTQo/XQXduug1rmerwGiL7g5ux4av9GfZLxYTDATAAAAfjB8BgkqhkiG9w0B
        BwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMyCxLMi7GRZgKqD65AgEQgDtjvZLJo2cQ31Vetngzm2ybHDc3d2vI74SRUzZ
        2RezQy3sAS6ZHrCjfnfn0c65bFdhsXxjSMnudIY7AKw==
        ```

    The following procedure restores an RDS for SQL Server TDE certificate to an on-premises DB
    instance. You copy and restore the TDE certificate on your destination DB instance using
    the certificate backup, corresponding private key file, and data key. The restored
    certificate is encrypted by the database master key of the new server.

###### To restore a TDE certificate

1. Copy the TDE certificate backup file and private key file from Amazon S3 to the destination instance.
   For more information on copying files from Amazon S3, see [Transferring files between RDS for SQL Server and Amazon S3](Appendix.SQLServer.Options.S3-integration.md "Appendix.SQLServer.Options.S3-integration.md").
2. Use your KMS key to decrypt the output cipher text to retrieve the plain text of the data key. The cipher text is
   located in the S3 metadata of the private key backup file.

```
aws kms decrypt \
    --key-id `my_KMS_key_ID` \
    --ciphertext-blob fileb://`exampleCiphertextFile` | base64 -d \
    --output text \
    --query Plaintext
```

You use the plain text output in the next step as the private key password. 3. Use the following SQL command to restore your TDE certificate.

```
CREATE CERTIFICATE `myOnPremTDEcertificate` FROM FILE='D:\`tde-cert-backup`.cer'
WITH PRIVATE KEY (FILE = N'D:\`tde-cert-key`.pvk',
DECRYPTION BY PASSWORD = '`plain_text_output`');
```

For more information on KMS decryption, see [decrypt](../../../cli/latest/reference/kms/decrypt.md "../../../cli/latest/reference/kms/decrypt.md") in the KMS section of the _AWS CLI Command Reference_.

After the TDE certificate is restored on the destination DB instance, you can restore
encrypted databases with that certificate.

###### Note

You can use the same TDE certificate to encrypt multiple SQL Server databases on
the source DB instance. To migrate multiple databases to a destination instance,
copy the TDE certificate associated with them to the destination instance only
once.
