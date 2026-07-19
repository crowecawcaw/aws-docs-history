# Encryption

S3 Files provides comprehensive encryption capabilities to protect your data both at rest
and in transit.

## Encryption at rest

Your S3 bucket is encrypted using Amazon S3's encryption mechanisms. For information
on encryption of data in S3, see [Protecting data with
encryption](UsingEncryption.md "UsingEncryption.md").

S3 Files encrypts data at rest in the S3 file system using server-side encryption.
Server-side encryption is the encryption of data at its destination by the application or
service that receives it. In S3 file systems, data and metadata are encrypted by default before being written to
storage and are automatically decrypted when read. These processes are handled
transparently by S3 Files, so you don't need to modify your applications. All data at
rest in the file system is encrypted using one of the following methods:

- (Default) Server-side encryption with Amazon S3-managed encryption keys
  (SSE-S3)
- Server-side encryption with AWS Key Management Service
  (SSE-KMS)

There are additional charges for using AWS KMS keys. For more information, see
[AWS KMS key
concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service Developer
Guide_ and [AWS KMS
pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### Server-side encryption with Amazon S3-managed encryption keys (SSE-S3)

This is the default method for encrypting data at rest in your S3 file system.
Amazon S3-managed encryption keys are a collection of keys that Amazon S3 owns and
manages. S3 Files owns and manages encryption of your data and metadata at rest in
your S3 file system when you use an Amazon S3-managed encryption key. For more
information about Amazon S3-managed encryption keys, see [Protecting data
with Amazon S3 managed keys](UsingServerSideEncryption.md "UsingServerSideEncryption.md").

### Server-side encryption with AWS Key Management Service (SSE-KMS)

While creating your file system, you can choose to configure an AWS Key
Management Service (AWS KMS) key that you manage. When you use SSE-KMS encryption
with an S3 file system the AWS KMS keys must be in the same Region as the file
system.

## S3 Files key policies for AWS KMS

Key policies are the primary way to control access to customer managed keys. For more
information on key policies, see [Key policies in AWS
KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer
Guide_. The following list describes all the AWS KMS–related permissions
that are supported by S3 Files for encrypting file systems at rest:

kms:Encrypt
(Optional) Encrypts plaintext into ciphertext. This permission is
included in the default key policy.

kms:Decrypt
(Required) Decrypts ciphertext. Ciphertext is plaintext that has been
previously encrypted. This permission is included in the default key
policy.

kms:ReEncrypt
(Optional) Encrypts data on the server side with a new customer
managed key, without exposing the plaintext of the data on the client side.
The data is first decrypted and then re-encrypted. This permission is
included in the default key policy.

kms:GenerateDataKeyWithoutPlaintext
(Required) Returns a data encryption key encrypted under a customer
managed key. This permission is included in the default key policy under
kms:GenerateDataKey\*.

kms:CreateGrant
(Required) Adds a grant to a key to specify who can use the key and
under what conditions. Grants are alternate permission mechanisms to key
policies. For more information on grants, see [Grants in AWS
KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS Key Management Service Developer
Guide_. This permission is included in the default key
policy.

kms:DescribeKey
(Required) Provides detailed information about the specified customer
managed key. This permission is included in the default key
policy.

kms:ListAliases
(Optional) Lists all of the key aliases in the account. When you use
the console to create an encrypted file system, this permission populates the
Select KMS key list. We recommend using this permission to provide the best
user experience. This permission is included in the default key
policy.

## Key states and their effects

The state of your KMS key directly affects access to your encrypted file
system:

Enabled
Normal operation - full read and write access to the file
system.

Disabled
File system becomes inaccessible after some time. Can be
re-enabled.

Pending deletion
File system becomes inaccessible. Deletion can be canceled during the
waiting period. Note that after cancelling key deletion, the key needs to be
moved to enabled state.

Deleted
File system permanently inaccessible. This action cannot be
reversed.

###### Warning

If you disable or delete the KMS key used for your file system, or revoke S3 Files
access to the key, your file system will become inaccessible. This can result in data
loss if you don't have backups. Always ensure you have proper backup procedures in
place before making changes to encryption keys.

## Encryption in transit

S3 Files requires encryption of data in transit using Transport Layer Security (TLS).
When you mount your file system using the mount helper, all data traveling between your
client and the file system is encrypted using TLS. The mount helper initializes efs-proxy
process to establish a secure TLS connection with your file system.
The mount helper also creates a process called amazon-efs-mount-watchdog that monitors
the health of mounts, and is started automatically the first time an S3 file system
is mounted. It ensures that each mount's efs-proxy process is
running, and stops the process when the file system is unmounted. If for some reason
the process is terminated unexpectedly, the watchdog process restarts it.

The following describes how TLS encryption in transit works:

1. A secure TLS connection is established between your client and the file
   system
2. All NFS traffic is routed through this encrypted
   connection
3. Data is encrypted before transmission and decrypted upon
   receipt

Encryption of data in transit changes your NFS client setup. When you inspect your
actively mounted file systems, you see one mounted to 127.0.0.1, or localhost, as in the
following example.

```
$ mount | column -t
127.0.0.1:/  on  /home/ec2-user/s3files        type  nfs4         (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,port=20127,timeo=600,retrans=2,sec=sys,clientaddr=127.0.0.1,local_lock=none,addr=127.0.0.1)
```

You mount your file system using the mount helper, which always encrypts data in
transit using TLS. Therefore, while mounting, your NFS client is reconfigured to mount to
a local port.
