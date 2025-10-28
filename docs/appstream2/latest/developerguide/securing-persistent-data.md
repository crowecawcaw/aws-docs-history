# Securing Persistent Data

Deployments of AppStream 2.0 can require the user state to persist
in some form. It might be to persist data for individual users, or
to persist data for collaboration using a shared folder. AppStream
2.0 instance storage is ephemeral and has no encryption option.

AppStream 2.0 provides user state persistence through home folders
and application settings in Amazon S3. Some use cases require
greater control over user state persistence. For these use cases,
AWS recommends using a Server Message Block (SMB) file share.

## User state and data

Because most Windows applications perform best and most securely when co-located with
application data created by the user, it is a best practice to keep this data in the same
AWS Region as AppStream 2.0 fleets. Encrypting this data is a best practice. The default
behavior of the user home folder is to encrypt files and folders at rest using Amazon S3-managed
encryption keys from the AWS key management services (AWS KMS). It is important to note that
AWS Administrative Users with access to the AWS Console or Amazon S3 bucket will be able to
access those files directly.

In designs that require a Server Message Block (SMB) target from a Windows File Share to
store user files and folders, the process is either automatic or requires
configuration.

_Table 5 — Options for securing user data_

| **SMB target**
| **Encryption-at-rest** | **Encryption-in-transit** | **Antivirus (AV)**
|
| --- | --- | --- | --- |
| **FSx for Windows File Server** | [Automatic through AWS KMS](../../../fsx/latest/WindowsGuide/encryption-at-rest.md "../../../fsx/latest/WindowsGuide/encryption-at-rest.md") | [Automatic through SMB encryption](../../../fsx/latest/WindowsGuide/encryption-in-transit.md "../../../fsx/latest/WindowsGuide/encryption-in-transit.md") | AV installed on a remote instance performs scan on mapped drive |
| **File Gateway, AWS Storage Gateway** | By default, all data stored by AWS Storage Gateway in S3 is encrypted server-side with Amazon S3-Managed Encryption Keys (SSE-S3). You can optionally configure different gateway types to encrypt stored data with AWS Key Management Service (KMS) | All data transferred between any type of gateway appliance and AWS storage is encrypted using SSL. | AV installed on a remote instance performs scan on mapped drive |
| **EC2-based Windows File Servers** | [Enable EBS encryption](../../../kms/latest/developerguide/services-ebs.md "../../../kms/latest/developerguide/services-ebs.md") | PowerShell; `Set- SmbServerConfiguration – EncryptData $True` | AV installed on server performs scan on local drives |
